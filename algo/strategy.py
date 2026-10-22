"""Strategy A: Overnight Hangover Panel (daily-data version).

Signal on close of day t, short on t+1.
Score S = mean of cross-sectional percentile ranks of
  f1 = z(beta-adjusted residual return)          (prior-day winner)
  f2 = z(rupee turnover)                          (proxy for turnover / free-float mcap)
  f3 = -z(delivery %)                             (speculative, low-delivery volume)
  f4 = z(close location in day range)  [optional, crude stand-in for the late-session surge]
Eligible: r1 >= 0.80 and S >= G.  Take the top N by S.
"""
import glob, os
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
W = 60

PARAMS = dict(universe_n=120, min_price=250.0, elig_r1=0.80, max_names=4, stop_k=2.0,
              stop_floor=0.012, stop_cap=0.035, cost_bp=13.5, stop_extra_bp=10.0)


def load_panel():
    cache = os.path.join(HERE, "data", "panel.pkl")
    files = sorted(glob.glob(os.path.join(HERE, "data", "bhav", "*.csv")))
    if os.path.exists(cache) and os.path.getmtime(cache) >= os.path.getmtime(files[-1]):
        return pd.read_pickle(cache)
    fno = set(pd.read_csv(os.path.join(HERE, "data", "fno_symbols.csv"))["SYMBOL"])
    fr = []
    for f in files:
        d = pd.read_csv(f)
        d["SYMBOL"] = d["SYMBOL"].str.strip()
        d = d[d["SYMBOL"].isin(fno)]
        d["DATE"] = pd.to_datetime(d["DATE1"].str.strip(), format="%d-%b-%Y")
        fr.append(d)
    df = pd.concat(fr).drop_duplicates(["DATE", "SYMBOL"], keep="last")
    for c in ["PREV_CLOSE", "OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE", "CLOSE_PRICE",
              "TURNOVER_LACS", "DELIV_PER"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    p = {k: df.pivot(index="DATE", columns="SYMBOL", values=v).sort_index()
         for k, v in dict(O="OPEN_PRICE", H="HIGH_PRICE", L="LOW_PRICE", C="CLOSE_PRICE",
                          PC="PREV_CLOSE", T="TURNOVER_LACS", DP="DELIV_PER").items()}
    p["T"] = p["T"] * 1e5  # rupees
    pd.to_pickle(p, cache)
    return p


def _z(x, w=W):
    m = x.rolling(w, min_periods=40).mean().shift(1)
    s = x.rolling(w, min_periods=40).std().shift(1)
    return (x - m) / s


def build_features(p, use_f4=False):
    O, H, L, C, PC, T, DP = (p[k] for k in ["O", "H", "L", "C", "PC", "T", "DP"])
    R = np.log(C / PC)
    R = R.where(R.abs() < 0.35)  # drop unadjusted corporate-action artefacts
    M = R.median(axis=1)  # equal-weight market proxy (F&O universe median)
    cov = R.rolling(W, min_periods=40).cov(M).shift(1)
    var = M.rolling(W, min_periods=40).var().shift(1)
    beta = cov.div(var, axis=0).clip(0.3, 2.0)
    e = R.sub(beta.mul(M, axis=0))
    f1 = _z(e)
    f2 = _z(np.log(T.where(T > 0)))
    f3 = -_z(DP)
    clv = ((C - L) / (H - L).replace(0, np.nan))
    f4 = _z(clv)
    # universe on the signal date t (uses data through t)
    med_t = T.rolling(W, min_periods=40).median()
    rank_t = med_t.rank(axis=1, ascending=False)
    uni = (rank_t <= PARAMS["universe_n"]) & (C >= PARAMS["min_price"]) & C.notna()
    feats = [f1, f2, f3] + ([f4] if use_f4 else [])
    ranks = [f.where(uni).rank(axis=1, pct=True) for f in feats]
    S = sum(ranks) / len(ranks)
    r1 = ranks[0]
    return dict(S=S, r1=r1, uni=uni, M=M, e=e, beta=beta, sig=np.log(C / O).rolling(W, min_periods=40).std())


def outcomes(p):
    """Trade-day (t+1) outcomes aligned to the signal-day row t. Entry at open, exit at close."""
    O, H, L, C = p["O"], p["H"], p["L"], p["C"]
    on = lambda x: x.shift(-1)
    return dict(O=on(O), H=on(H), L=on(L), C=on(C))


def pick(S, r1, uni, G, n, elig=0.80, lo=0, mirror=False):
    """Return DataFrame of picks: for each signal date, up to n symbols (ranks lo..lo+n-1)."""
    out = []
    for d in S.index:
        s = S.loc[d]
        if mirror:
            ok = (r1.loc[d] <= 1 - elig) & uni.loc[d]
            sc = (1 - s)[ok]
        else:
            ok = (r1.loc[d] >= elig) & (s >= G) & uni.loc[d]
            sc = s[ok]
        if sc.empty:
            continue
        sc = sc.sort_values(ascending=False).iloc[lo:lo + n]
        for sym, v in sc.items():
            out.append((d, sym, v))
    return pd.DataFrame(out, columns=["d", "sym", "S"])


def simulate(picks, F, X, stop=True, params=PARAMS):
    """Per-trade short P&L (log-return bp). gross: no costs; net: after costs/slippage."""
    if picks.empty:
        return picks
    d, s = picks["d"].values, picks["sym"].values
    O = np.array([X["O"].at[a, b] for a, b in zip(d, s)])
    H = np.array([X["H"].at[a, b] for a, b in zip(d, s)])
    L = np.array([X["L"].at[a, b] for a, b in zip(d, s)])
    Cc = np.array([X["C"].at[a, b] for a, b in zip(d, s)])
    sig = np.array([F["sig"].at[a, b] for a, b in zip(d, s)])
    ok = ~(np.isnan(O) | np.isnan(Cc) | np.isnan(sig) | np.isnan(H) | np.isnan(L))
    k = params["stop_k"]
    dist = np.clip(k * sig, params["stop_floor"], params["stop_cap"])
    stop_px = O * (1 + dist)
    hit = (H >= stop_px) & stop
    exit_px = np.where(hit, stop_px, Cc)
    gross = -np.log(exit_px / O) * 1e4
    net = gross - params["cost_bp"] - np.where(hit, params["stop_extra_bp"], 0.0)
    bench = np.array([-(np.log(X["C"].loc[a] / X["O"].loc[a])).where(
        F["uni"].loc[a]).mean() * 1e4 for a in d]) if False else None
    out = picks.copy()
    out["gross"], out["net"], out["hit"], out["mfe"] = gross, net, hit, -np.log(L / O) * 1e4
    out["ok"] = ok
    return out[ok].reset_index(drop=True)


def ew_bench(F, X):
    """Equal-weight universe short return (bp) per signal date, same open->close window."""
    r = np.log(X["C"] / X["O"])
    return -(r.where(F["uni"]).mean(axis=1)) * 1e4


def tstat(x):
    x = pd.Series(x).dropna()
    return x.mean() / (x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 2 and x.std() > 0 else np.nan
