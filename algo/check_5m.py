"""Tradable-window check: same picks, but enter at 09:45 and exit at 15:05 using 5-minute bars (last ~58 days only)."""
import numpy as np, pandas as pd, yfinance as yf
import strategy as st, backtest as bt

p = st.load_panel(); F = st.build_features(p); X = st.outcomes(p); bench_d = st.ew_bench(F, X)
G, q, _ = bt.choose_G(F, "2022-04-01", bt.IS_END)
picks = st.pick(F["S"], F["r1"], F["uni"], G, 4)
tdates = F["S"].index
nxt = dict(zip(tdates[:-1], tdates[1:]))
picks["td"] = picks["d"].map(nxt)
win = picks[picks.td >= "2026-07-28"].dropna(subset=["td"]).copy()
syms = sorted(set(win.sym)); print("picks in window:", len(win), "symbols:", len(syms))
raw = yf.download([s + ".NS" for s in syms], period="60d", interval="5m", progress=False, group_by="ticker", threads=True)
rows = []
for _, r in win.iterrows():
    try:
        b = raw[r.sym + ".NS"].dropna(subset=["Open"])
    except KeyError:
        continue
    day = b[b.index.date == r.td.date()]
    if day.empty: continue
    t = day.index.strftime("%H:%M")
    e = day[t == "09:45"]; x = day[t == "15:05"]
    if e.empty or x.empty: continue
    ent = e["Open"].iloc[0]
    sig = F["sig"].at[r.d, r.sym]
    stop = ent * (1 + np.clip(2 * sig, 0.012, 0.035))
    after = day[(t >= "09:45") & (t < "15:05")]
    hit = (after["High"] >= stop).any()
    ex = stop if hit else x["Open"].iloc[0]
    gross = -np.log(ex / ent) * 1e4
    net = gross - 13.5 - (10 if hit else 0)
    pc = p["C"].at[r.d, r.sym]
    rows.append(dict(td=r.td, sym=r.sym, gross=gross, net=net, hit=hit, up945=(ent / pc - 1) * 100,
                     mfe=-np.log(after["Low"].min() / ent) * 1e4,
                     oc=-np.log(X["C"].at[r.d, r.sym] / X["O"].at[r.d, r.sym]) * 1e4))
d = pd.DataFrame(rows)
print("trades", len(d), "days", d.td.nunique())
print(f"tradable window (09:45->15:05, stop): gross={d.gross.mean():.1f}bp net={d.net.mean():.1f}bp win={(d.net>0).mean()*100:.1f}% stopped={d.hit.mean()*100:.1f}% "
      f"median MFE={d.mfe.median():.0f}bp")
print(f"same picks, daily open->close proxy  : gross={d.oc.mean():.1f}bp")
dn = d.groupby("td").net.mean(); print(f"day-level t(net)={st.tstat(dn):.2f}")
ex7 = d[d.up945 <= 7]; print("after dropping >7% up-at-09:45 names:", len(ex7), f"net={ex7.net.mean():.1f}bp")
d.to_csv("data/check_5m_trades.csv", index=False)
