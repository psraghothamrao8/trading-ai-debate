# Strategy A: Overnight Hangover Panel (code + backtest)

| File | Purpose |
|---|---|
| `fetch_data.py` | Downloads NSE bhavcopy (prices + delivery %) since 2022 into `data/bhav/` |
| `strategy.py` | Features f1 (residual return), f2 (turnover), f3 (low delivery %), score S, picks, simulator |
| `backtest.py` | Daily open-to-close backtest with stop, costs (13.5 bp), placebos; writes `stats.json` |
| `check_5m.py` | Tradable-window check (09:45 to 15:05) on 5-minute bars, last ~59 trading days |
| `live_signal.py` | `--preview` to test any time; `--loop` runs the day: alert at 09:46, stop/target watch, cover reminder 15:05 |

## Backtest results (Apr 2022 - Oct 2026, 4,416 trades, 4 shorts/day, 13.5 bp round-trip cost)

- Daily proxy (enter at open, exit at close): gross +19.8 bp/trade; vs. equal-weight universe +9.6 bp (t = 2.9); after costs -5.1 bp vs. universe; absolute net +5.0 bp, win rate 51.9%, profit factor 1.07, max drawdown -24%.
- Tradable window (5-min, last 59 days, 236 trades): gross +24.8 bp, net +10.9 bp, win rate 51%, t = 0.7 (not significant).
- Mirror placebo (prior-day losers) shows no edge (good sign); permutation test only at about the 95th percentile (weak); the highest-score bucket (S > 0.95) lost money.
- Spec gates (20 bp gross, 8 bp net vs. benchmark) are NOT met. Treat as unvalidated: paper trade or very small size.

Substitutions vs. the spec (no free minute history): f2 uses rupee turnover z-score instead of turnover / free-float market cap; f4 (late surge) omitted in the base run; universe is today's F&O list (survivorship bias); no results/ex-date calendar.
