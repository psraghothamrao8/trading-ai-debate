"""Download NSE security-wise bhavcopy (prices + delivery %) into data/bhav/ and the F&O underlying list."""
import io, os, sys, time, datetime as dt
import requests, pandas as pd
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data", "bhav")
os.makedirs(OUT, exist_ok=True)
H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "Accept": "*/*"}
KEEP = ["SYMBOL", "SERIES", "DATE1", "PREV_CLOSE", "OPEN_PRICE", "HIGH_PRICE", "LOW_PRICE",
        "CLOSE_PRICE", "TTL_TRD_QNTY", "TURNOVER_LACS", "NO_OF_TRADES", "DELIV_QTY", "DELIV_PER"]

def fetch(d):
    f = os.path.join(OUT, d.strftime("%Y%m%d") + ".csv")
    if os.path.exists(f):
        return d, "cached"
    url = f"https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{d:%d%m%Y}.csv"
    for attempt in range(4):
        try:
            r = requests.get(url, headers=H, timeout=30)
            if r.status_code == 404:
                return d, "holiday"
            r.raise_for_status()
            df = pd.read_csv(io.StringIO(r.text), skipinitialspace=True)
            df.columns = [c.strip() for c in df.columns]
            df = df[df["SERIES"].str.strip() == "EQ"][KEEP]
            df.to_csv(f, index=False)
            return d, "ok"
        except Exception as e:
            time.sleep(1.5 * (attempt + 1))
    return d, "fail"

def main(start="2022-01-03", end=None):
    end = pd.Timestamp(end or dt.date.today())
    days = [d for d in pd.bdate_range(start, end)]
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(fetch, days))
    from collections import Counter
    print(Counter(s for _, s in res))
    print("failed:", [d.strftime("%Y-%m-%d") for d, s in res if s == "fail"][:20])
    # F&O underlyings (current list)
    try:
        r = requests.get("https://nsearchives.nseindia.com/content/fo/fo_mktlots.csv", headers=H, timeout=30)
        r.raise_for_status()
        lots = pd.read_csv(io.StringIO(r.text), skipinitialspace=True)
        lots.columns = [c.strip() for c in lots.columns]
        syms = sorted(set(lots["SYMBOL"].str.strip()) - {"Symbol", "SYMBOL"})
        pd.Series(syms, name="SYMBOL").to_csv(os.path.join(HERE, "data", "fno_symbols.csv"), index=False)
        print("fno symbols:", len(syms))
    except Exception as e:
        print("fno list failed", e)

if __name__ == "__main__":
    main(*sys.argv[1:])
