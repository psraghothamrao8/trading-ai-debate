"""Live scanner for Strategy A (Overnight Hangover Panel). Notifies on THIS laptop only (Windows toasts + alerts.log).

  python live_signal.py --preview   # test now with latest available prices, any time of day
  python live_signal.py --loop      # run for the day: wait for 09:46 IST, alert, monitor stops, remind to cover at 15:05

It never places orders. Prices come from Yahoo (may lag a few minutes): verify on your broker before acting.
"""
import argparse, datetime as dt, json, os, subprocess, sys, time
import numpy as np, pandas as pd, requests, yfinance as yf
import fetch_data, strategy as st

HERE = os.path.dirname(os.path.abspath(__file__))
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
STATS = json.load(open(os.path.join(HERE, "stats.json")))
MAX_NAMES = 4
TARGET_BP = 80          # median best-case move 09:45->15:05 in the 5-min check (82 bp)
EXP_GROSS_BP = 25       # mean gross move in the same check (24.8 bp)
LOG = os.path.join(HERE, "alerts.log")


def now():
    return dt.datetime.now(IST)


def log(msg):
    line = f"[{now():%Y-%m-%d %H:%M:%S}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


PS = r'''
$t=$env:TOAST_TITLE; $b=$env:TOAST_BODY
[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml("<toast duration='long'><visual><binding template='ToastGeneric'><text></text><text></text></binding></visual><audio src='ms-winsoundevent:Notification.Reminder'/></toast>")
$n = $xml.GetElementsByTagName('text')
$n.Item(0).AppendChild($xml.CreateTextNode($t)) | Out-Null
$n.Item(1).AppendChild($xml.CreateTextNode($b)) | Out-Null
$toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe').Show($toast)
'''


def toast(title, body):
    log(f"TOAST | {title} | {body.replace(chr(10), ' / ')}")
    env = dict(os.environ, TOAST_TITLE=title, TOAST_BODY=body)
    try:
        subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command", PS], env=env, timeout=30,
                       capture_output=True)
    except Exception as e:
        log(f"toast failed: {e}")


def banned():
    try:
        r = requests.get("https://nsearchives.nseindia.com/content/fo/fo_secban.csv",
                         headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        r.raise_for_status()
        return {ln.split(",")[-1].strip() for ln in r.text.splitlines()[1:] if "," in ln}
    except Exception as e:
        log(f"ban list unavailable ({e}) - CHECK THE F&O BAN LIST YOURSELF")
        return set()


def candidates():
    """Rank names from the last completed trading day's data (never today's)."""
    fetch_data.main("2022-01-03")  # cached days are skipped; this just adds new ones
    p = st.load_panel()
    F = st.build_features(p)
    today = pd.Timestamp(now().date())
    sig_date = p["C"].index[p["C"].index < today][-1]
    S, r1, uni = F["S"].loc[sig_date], F["r1"].loc[sig_date], F["uni"].loc[sig_date]
    ok = (r1 >= 0.80) & (S >= STATS["G"]) & uni
    c = S[ok].sort_values(ascending=False)
    df = pd.DataFrame({"sym": c.index, "S": c.values})
    df["r1"] = df.sym.map(r1)
    df["sigma"] = df.sym.map(F["sig"].loc[sig_date])
    df["prev_close"] = df.sym.map(p["C"].loc[sig_date])
    return sig_date, df


def prices(syms):
    """Latest 1-minute price per symbol and the bar time."""
    out = {}
    if not syms:
        return out
    raw = yf.download([s + ".NS" for s in syms], period="1d", interval="1m", progress=False,
                      group_by="ticker", threads=True)
    for s in syms:
        try:
            b = (raw[s + ".NS"] if len(syms) > 1 else raw).dropna(subset=["Close"])
            if not b.empty:
                since = b[(b.index.hour > 9) | ((b.index.hour == 9) & (b.index.minute >= 46))]
                hi = float(since["High"].max()) if len(since) else float(b["Close"].iloc[-1])
                out[s] = (float(b["Close"].iloc[-1]), b.index[-1].to_pydatetime(), hi)
        except Exception:
            pass
    return out


def build_plan(cands, preview):
    ban = banned()
    px = prices(list(cands.sym.head(MAX_NAMES * 3)))
    plan = []
    for _, r in cands.iterrows():
        if len(plan) >= MAX_NAMES:
            break
        if r.sym in ban:
            log(f"skip {r.sym}: in F&O ban list"); continue
        if r.sym not in px:
            log(f"skip {r.sym}: no live price"); continue
        last, ts, _ = px[r.sym]
        chg = (last / r.prev_close - 1) * 100
        if chg > 7:
            log(f"skip {r.sym}: already +{chg:.1f}% today (>7% rule)"); continue
        if abs(chg) > 20:
            log(f"skip {r.sym}: {chg:+.1f}% vs prev close looks like a corporate action"); continue
        sell = last * (1 - 0.0005)
        stop_pct = float(np.clip(2.0 * r.sigma, 0.012, 0.035))
        lag = (now() - ts).total_seconds() / 60
        plan.append(dict(sym=r.sym, S=r.S, last=last, sell=sell, stop=sell * (1 + stop_pct), stop_pct=stop_pct * 100,
                         target=sell * (1 - TARGET_BP / 1e4), exp=sell * (1 - EXP_GROSS_BP / 1e4),
                         chg=chg, lag=lag, bar=ts))
    return plan


CONF = ("Confidence: LOW. Backtest win-rate ~52% per trade; after costs the average edge is about zero to +10 bp "
        "(Rs 10-20 per Rs 1 lakh). NOT validated. Use paper/very small size.")


def announce(plan, sig_date, preview):
    tag = "PREVIEW " if preview else ""
    if not plan:
        toast(f"{tag}Hangover scan: NO TRADE today", f"No name passed the filters (signals from {sig_date:%d-%b}). Stay flat.")
        return
    toast(f"{tag}Hangover scan: {len(plan)} SHORT candidates",
          ", ".join(p["sym"] for p in plan) + f"\nSignals from {sig_date:%d-%b}. Details follow. Exit all by 15:05.\n" + CONF)
    for i, p in enumerate(plan, 1):
        lagtxt = f" (price {p['lag']:.0f} min old)" if p["lag"] > 3 else ""
        toast(f"{tag}SHORT {p['sym']}  ({i}/{len(plan)})",
              f"Sell ~Rs {p['sell']:.2f}{lagtxt}\n"
              f"Stop ~Rs {p['stop']:.2f} (+{p['stop_pct']:.1f}%)   Target ~Rs {p['target']:.2f} (-{TARGET_BP/100:.1f}%)\n"
              f"Typical outcome: ~Rs {p['exp']:.2f} by 15:05. Target is hit in ~half of past cases. Cover by 15:05.\n"
              f"Confidence LOW (~52% win-rate). Check price/spread in broker app first.")


def monitor(plan):
    done = set()
    ref_nifty = None
    while now().time() < dt.time(15, 12):
        t = now().time()
        if t >= dt.time(15, 5) and "exit" not in done:
            toast("COVER ALL SHORTS NOW (15:05)", "Buy-to-cover every open short: " + ", ".join(p["sym"] for p in plan)
                  + ". Must be flat by ~15:10 (broker auto square-off is later but charges extra).")
            done.add("exit")
        px = prices([p["sym"] for p in plan])
        for p in plan:
            if p["sym"] not in px:
                continue
            last, ts, hi = px[p["sym"]]
            if hi >= p["stop"] and ("stop", p["sym"]) not in done and last >= p["stop"] * 0.998:
                toast(f"STOP: COVER {p['sym']} NOW", f"Price Rs {last:.2f} reached the stop Rs {p['stop']:.2f}. Buy to cover.")
                done.add(("stop", p["sym"]))
            if last <= p["target"] and ("tgt", p["sym"]) not in done:
                toast(f"TARGET: {p['sym']} at Rs {last:.2f}", f"Reached target Rs {p['target']:.2f}. Consider covering and booking.")
                done.add(("tgt", p["sym"]))
        try:
            n = yf.download("^NSEI", period="1d", interval="1m", progress=False)["Close"].dropna().squeeze()
            if ref_nifty is None and len(n):
                ref_nifty = float(n.iloc[min(len(n) - 1, 30)])
            elif ref_nifty and float(n.iloc[-1]) >= ref_nifty * 1.012 and "nifty" not in done:
                toast("NIFTY +1.2% SINCE 09:46: COVER EVERYTHING", "Market squeeze rule triggered - flatten all shorts.")
                done.add("nifty")
        except Exception:
            pass
        time.sleep(60)
    log("session over")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--loop", action="store_true")
    a = ap.parse_args()
    sig_date, cands = candidates()
    log(f"signal date {sig_date:%Y-%m-%d}: {len(cands)} eligible names: {', '.join(cands.sym.head(10))}")
    if a.preview or not a.loop:
        announce(build_plan(cands, True), sig_date, True)
        return
    if now().weekday() >= 5:
        log("weekend - nothing to do"); return
    target = now().replace(hour=9, minute=46, second=15, microsecond=0)
    while now() < target:
        time.sleep(10)
    if now().time() > dt.time(10, 30):
        toast("Hangover scan skipped", "Started after 10:30 - entry window missed. No trade today."); return
    plan = build_plan(cands, False)
    announce(plan, sig_date, False)
    if plan:
        monitor(plan)


if __name__ == "__main__":
    main()
