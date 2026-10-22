"""Backtest of Strategy A on daily NSE data (open -> close proxy). Prints a report and saves stats.json."""
import json, os, sys
import numpy as np, pandas as pd
import strategy as st

HERE = os.path.dirname(os.path.abspath(__file__))
IS_END, OOS1_END = "2023-12-31", "2024-09-30"   # holdout = Oct 2024 onward
rng = np.random.default_rng(7)


def summarize(tr, bench, label, cap_frac=0.20):
    if tr.empty:
        print(f"{label:34s} no trades"); return {}
    tr = tr.copy()
    tr["ex_gross"] = tr["gross"] - tr["d"].map(bench)          # excess vs equal-weight short of universe
    tr["ex_net"] = tr["net"] - tr["d"].map(bench)
    day = tr.groupby("d").agg(net=("net", "mean"), gross=("gross", "mean"), exn=("ex_net", "mean"),
                              exg=("ex_gross", "mean"), n=("net", "size"))
    pnl = day["net"] * (cap_frac * day["n"]) / 1e4          # fraction of capital, 20% per name
    eq = (1 + pnl).cumprod(); dd = (eq / eq.cummax() - 1).min()
    wins, losses = tr.loc[tr.net > 0, "net"].sum(), -tr.loc[tr.net <= 0, "net"].sum()
    res = dict(label=label, trades=len(tr), days=len(day), gross_bp=tr.gross.mean(), net_bp=tr.net.mean(),
               ex_gross_bp=tr.ex_gross.mean(), ex_net_bp=tr.ex_net.mean(), t_gross=st.tstat(day.gross),
               t_ex_gross=st.tstat(day.exg), t_ex_net=st.tstat(day.exn), t_net=st.tstat(day.net),
               win=(tr.net > 0).mean(), pf=wins / losses if losses else np.nan, stop_rate=tr.hit.mean(),
               maxdd=dd, total_ret=eq.iloc[-1] - 1)
    print(f"{label:34s} n={res['trades']:4d} days={res['days']:3d} gross={res['gross_bp']:6.1f} net={res['net_bp']:6.1f} "
          f"| excess gross={res['ex_gross_bp']:6.1f}(t={res['t_ex_gross']:5.2f}) net={res['ex_net_bp']:6.1f}(t={res['t_ex_net']:5.2f}) "
          f"| win={res['win']*100:4.1f}% PF={res['pf']:4.2f} stop={res['stop_rate']*100:4.1f}% DD={res['maxdd']*100:5.1f}%")
    return res


def choose_G(F, start, end, p=0.80):
    S, r1, uni = F["S"].loc[start:end], F["r1"].loc[start:end], F["uni"].loc[start:end]
    allS = S.where(uni).stack()
    for q in [0.80, 0.75, 0.70, 0.65, 0.60]:
        G = allS.quantile(q)
        elig = ((r1 >= 0.80) & (S >= G) & uni).any(axis=1)
        if elig.mean() >= 0.85:
            return G, q, elig.mean()
    return G, q, elig.mean()


def run(use_f4=False, tag=""):
    p = st.load_panel()
    F = st.build_features(p, use_f4=use_f4)
    X = st.outcomes(p)
    bench = st.ew_bench(F, X)
    start = F["S"].dropna(how="all").index[0]
    G, q, fr = choose_G(F, "2022-04-01", IS_END)
    print(f"\n===== {tag or 'BASE'} | Gate G={G:.3f} (p{int(q*100)}), IS day-coverage {fr*100:.0f}% =====")
    base = st.pick(F["S"], F["r1"], F["uni"], G, 4)
    sim = st.simulate(base, F, X, stop=True)
    sim0 = st.simulate(base, F, X, stop=False)
    periods = {"IS 2022-04..2023-12": ("2022-04-01", IS_END), "OOS1 2024-01..2024-09": ("2024-01-01", OOS1_END),
               "HOLDOUT 2024-10..now": ("2024-10-01", "2027-01-01"), "ALL": ("2022-04-01", "2027-01-01")}
    out = {}
    for name, (a, b) in periods.items():
        m = (sim.d >= a) & (sim.d <= b)
        out[name] = summarize(sim[m], bench, name + " [stop]")
    for name in ["IS 2022-04..2023-12", "HOLDOUT 2024-10..now"]:
        a, b = periods[name]
        m = (sim0.d >= a) & (sim0.d <= b)
        summarize(sim0[m], bench, name + " [no stop]")
    # yearly stability (net, with stop)
    print("-- per half-year (stop): mean excess-net bp / absolute net bp / n")
    sim["h"] = sim.d.dt.year.astype(str) + "H" + ((sim.d.dt.month > 6) + 1).astype(str)
    for h, g in sim.groupby("h"):
        ex = (g.net - g.d.map(bench)).mean()
        print(f"   {h}: excess_net={ex:6.1f}  abs_net={g.net.mean():6.1f}  n={len(g)}")
    # placebos (all periods, stop on)
    print("-- placebos & robustness (ALL, stop on)")
    mir = st.simulate(st.pick(F["S"], F["r1"], F["uni"], G, 4, mirror=True), F, X)
    summarize(mir, bench, "mirror: prior-day LOSERS")
    rk = st.simulate(st.pick(F["S"], F["r1"], F["uni"], G, 4, lo=2), F, X)
    summarize(rk, bench, "ranks 3-6 instead of 1-4")
    # permutation: shuffle S within date among universe, same selection rule, 200 reps
    means = []
    Sv, uv = np.array(F["S"].values, copy=True), np.array(F["uni"].values, copy=True)
    for _ in range(200):
        arr = Sv.copy()
        for i in range(len(arr)):
            idx = np.where(uv[i])[0]
            arr[i, idx] = rng.permutation(arr[i, idx])
        Sp = pd.DataFrame(arr, index=F["S"].index, columns=F["S"].columns)
        pk = st.pick(Sp, F["r1"], F["uni"], G, 4)
        s = st.simulate(pk, F, X)
        s = s[(s.d >= "2022-04-01")]
        means.append((s.gross - s.d.map(bench)).mean())
        if len(means) >= 40: break
    real = (sim.gross - sim.d.map(bench)).mean()
    print(f"   permutation(S shuffled in-universe, r1 kept): real excess_gross={real:.1f}bp vs null mean={np.mean(means):.1f} "
          f"p95={np.percentile(means,95):.1f} max={np.max(means):.1f}  (40 draws)")
    # ablation: score only f1 (pure prior-day winner) = does S add anything?
    # conditional hit-rate table by S bucket for the live "confidence" figure
    sim["bucket"] = pd.cut(sim.S, [0, G, 0.85, 0.90, 0.95, 1.01])
    print("-- by S bucket (ALL):")
    print(sim.groupby("bucket", observed=True).agg(n=("net", "size"), net=("net", "mean"), win=("net", lambda x: (x > 0).mean())).round(3))
    return dict(G=float(G), sim=sim, bench=bench, F=F, X=X, out=out, quantile=q)


if __name__ == "__main__":
    r = run(False, "BASE (f1,f2,f3)")
    r4 = run(True, "VARIANT with close-location stand-in for f4")
    sim = r["sim"]
    stats = dict(G=r["G"], n_trades=int(len(sim)),
                 win_rate=float((sim.net > 0).mean()), mean_net_bp=float(sim.net.mean()),
                 mean_gross_bp=float(sim.gross.mean()), stop_rate=float(sim.hit.mean()),
                 mfe_median_bp=float(sim.mfe.median()), mfe_p25_bp=float(sim.mfe.quantile(.25)),
                 mfe_p75_bp=float(sim.mfe.quantile(.75)), summary={k: v for k, v in r["out"].items()})
    json.dump(stats, open(os.path.join(HERE, "stats.json"), "w"), indent=1, default=float)
    print("\nsaved stats.json")
