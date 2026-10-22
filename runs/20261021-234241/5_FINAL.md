# FINAL REPORT: Intraday NSE Short-Only Book, Two Surviving Strategies

**Read this first.** Both AIs' conviction scores are opinions. They are not evidence of profitability. Nothing here has been run on data. Only the pre-registered backtest and unattended paper trading can show whether any of this works, and a pass would still not guarantee future profit.

**Novelty.** Neither strategy is a breakthrough in the sense the brief asked for. After the debate, the ideas that were most original on paper, the square-off shelf, the breadth-hollow futures short and the parent-order detector, were dropped. They failed on mechanism, cost or trade frequency. What remains are two well-motivated variants of published anomalies:
- **A** is a variant of the LouΓÇôPolkΓÇôSkouras overnight/intraday effect and attention-driven reversal.
- **B** is a variant of residual reversal and intra-industry lead-lag (Hou, CohenΓÇôFrazzini).
- What is non-standard is the specific feature set, the filters, and the fact that both are fully coded as daily, rank-based rules. Whether anything survives costs is unknown.

**Selection.**
- Strategy A is the only one both AIs rated 4 or higher.
- Strategy B is a gated candidate that ships only if its event study passes.
- No third idea reached 4 from both AIs, so none is listed.

**Figures I added.** Numbers marked **[added]** were proposed in this report and were not debated by the two AIs. Review them before freezing.

---

## Shared infrastructure and cost model

**Instrument.** Cash-segment MIS shorts are the default. Futures STT may have risen, and single-stock futures lot sizes are coarse.

**Costs per round trip, at about Γé╣2 lakh notional per leg:**

| Item | bp |
|---|---|
| Brokerage (Γé╣20 ├ù 2) | 2.0 |
| STT (0.025%, sell side) | 2.5 |
| Exchange charge | 0.6 |
| SEBI fee | 0.02 |
| Stamp duty (buy leg) | 0.3 |
| GST | 0.5 |
| **Statutory + brokerage** | **Γëê5.9** |
| Slippage (liquid F&O) | 3ΓÇô7 |
| **All-in** | **Γëê13ΓÇô16 for typical F&O names** |

The slippage line is an estimate. Calibrate it from paper trading.

**Flat brokerage inflates the cost on small positions.** At Γé╣50k per leg, the Γé╣40 round-trip brokerage is about 8 bp, not 2. The backtest must use actual rupee position sizes.

**Rates to verify.** Check every statutory rate on a current contract note. One AI recalled a 2026 rise in futures STT, but this was never confirmed. It doesn't affect these strategies, because they are cash MIS.

**Expiry days.** Do not hard-code the weekday. The two AIs disagreed on Tuesday versus Thursday. Tag an expiry day as the date the near-month contract disappears from the F&O bhavcopy.

**Universal rules for both strategies:**
- **Universe:** top ~120 F&O names by 60-day turnover, using a point-in-time F&O list, a price of at least Γé╣250 and a median spread of at most 5 bp. B may relax the spread limit to 8 bp.
- **Exclusions:**
  - F&O ban list, ASM/GSM and T2T names
  - names the broker will not short on MIS (pull the broker's list each morning)
  - result and ex-date days
  - names up more than 7% on the day, or within 3.5% of the upper band
  - index-rebalance dates (MSCI, FTSE, Nifty) for the late-surge feature
- **Blackouts:**
  - Budget day and election-result days: no trading.
  - RBI policy days: halve size in rate-sensitive names.
  - Expiry days: half size until the data says otherwise.
- **Exits:**
  - Passive cover at 15:10.
  - Escalate to market-with-protection at 15:12.
  - Flat by 15:13, before the broker's 15:15ΓÇô15:25 auto-square-off.
- **Book stop:** flatten everything if Nifty is at least +1.2% from the open, or the day's loss reaches 1.5% of capital. A short-only book cannot hedge a trending-up day, so this is the main tail risk.
- **Sizing at 1├ù gross.** Per-name notional is at most 25% of capital, and at most 0.5% of 5-minute volume at entry **[added]**. Leverage is increased only after paper trading.
- **Benchmark:** report all P&L against the equal-weight F&O return over the same window, not against zero. A short book that merely times the market's intraday drift has no alpha.
- **Broker:** a domestic API broker (Zerodha Kite, Upstox, Shoonya or similar). Interactive Brokers does not offer MIS shorting in Indian cash equities. Confirm static-IP, order-rate and algo-registration rules under SEBI's retail-algo framework.

---

## Strategy A: Overnight Hangover Panel

### Core insight
Retail and operator money chases yesterday's top gainers, especially in the first half hour. Liquidity providers who supplied that demand lay off inventory during the day. A 15:00ΓÇô15:30 mark-up also unwinds. The NSE close is the VWAP of the last 30 minutes, so a modest buyer can lift it cheaply, and nobody defends that level the next day.

It is not "stocks go down". It is a cross-sectional bet that prior-day crowding predicts a weaker 09:46ΓÇô15:10 return than the rest of the F&O universe.

**Honest caveat:** the counterparty is behaviourally wrong, not forced. That is why Claude caps conviction at 4.

### Exact rules
- **Score time:** about 09:00, from prior-day data, with a refresh at about 09:40 if needed.
- **Eligible set:** F&O names in the top quintile of prior-day residual return, where residual = R ΓêÆ ╬▓ΓéåΓéÇd ├ù R_Nifty.
- **Features:** four, each a cross-sectional percentile rank, averaged with equal weights and no tuned parameters:
  1. Prior-day residual return z-score (z vs own 60-day history).
  2. Turnover divided by free float, z-score.
  3. Minus the delivery-% z-score (low delivery means more speculative churn).
  4. Late-session (14:59 to 15:29) residual return z-score.
- **Entry:** short the top 4 names whose score clears a frozen minimum gate. The gate is the 80th percentile of the in-sample distribution of this score across all stock-days **[added]**. Fewer than 4 trades is allowed. Fill at the 09:46 open plus half-spread via market-with-protection.
- **Entry-time ablation:** also run 09:20, 09:30 and 09:46. If most of the reversal happens before 09:46, the strategy is not tradable at 09:46.
- **Confirmation arms (ablations only):** none, `P < C_prev`, `P < Open`. There is no confirmation filter in the base spec. `P < Open or P < VWAP` is true almost always and is retail VWAP lore.
- **Stop:** a catastrophe stop at entry + 2.0╧â of the stock's intraday move (about 2.0ΓÇô2.2%). Test against no stop, because tight stops destroy reversion edges.
- **Exit:** cover at 15:10 as described above.
- **Candidate features, tested only as ablations** (each must add at least t Γëê 2 in held-out years):
  - ╬öOI ├ù sign(return)
  - bulk/block net-sell flag from the previous evening
  - trade-count retail proxy (turnover divided by trade count)
- **Control in every regression:** the 60-day (overnight ΓêÆ intraday) drift of the stock. A high value means the stock habitually loses intraday, so it is a control, not a penalty. The first draft had the sign backwards.

### Who is on the other side, and why they lose
- **Late chasers (09:15ΓÇô09:45).** They buy the winners-list stocks at market into wide opening spreads. They respond to attention, not to price.
- **Passive liquidity providers.** They must lay off the inventory they took from the previous day's buyers.
- **Close-markers.** After the official close is recorded, they have no reason to commit fresh capital to defend the mark.

**Late-surge sub-hypothesis ("square-off echo").** The next-day reversal should concentrate in late surges that run opposite to the day's trend, such as a late jump in a stock that fell all day. That pattern looks like price-insensitive short-covering at the deadline. If aligned and opposed surges behave the same, drop the square-off story and keep only the plain close-mark story, or drop the feature.

### Conviction
- **Claude: 4/5.** It has the best edge-to-cost ratio of the shortlist, because a roughly 5-hour hold has time to accrue the effect against about 13.5 bp of cost. It is a documented family of anomalies, and a 2-hour daily-data test can kill it cheaply. Claude's honest prior is 10ΓÇô25 bp gross per name and about 35ΓÇô40% odds of passing gate 1.
- **Gemini: 4.5/5** (4.6 earlier). Gemini sees the multi-hour hold, the retail attention rush and the unbacked close-mark as a strong structural story. It claims 38ΓÇô55 bp gross per basket-day. Claude considers that a hope, not an estimate.

### Failure regimes
- Strong trend or gap-up days with persistent FPI/DII inflow, where all four shorts get squeezed together.
- The overnight gap having already absorbed the reversal, which makes it a gap-fade the brief rejects.
- A genuine re-rating on real news.
- Changes in retail leverage rules. Split the sample at September 2021 (peak margin) and October 2024 (F&O curbs).
- Names stuck near the upper band. A stuck short is a tail loss and is not hedged.
- Ban-list names, which are the most crowded and the most prone to squeezes.
- Expiry-day closes that are real settlement marks.
- Budget, RBI and election days.
- Delivery-% data being public, so crowding by others could erode the edge.

### Backtest plan
- **Data:**
  - 1-minute OHLCV, corporate-action-adjusted, as far back as available (4 years minimum)
  - daily bhavcopy with delivery quantities, 2018 onward
  - F&O bhavcopy for OI and expiry tagging
  - free-float history
  - bulk/block files
  - ban, ASM/GSM and band lists
  - a point-in-time F&O universe
- **Splits:** freeze all thresholds on the in-sample period.
  - In-sample: 2018 to 2021.
  - Out-of-sample 1: 2022 to September 2024.
  - Final holdout: October 2024 to September 2026, touched once.
  - Report separately across the September 2021 and October 2024 breaks.
- **Step 1, daily-data kill test (about 2 hours).** Within the top prior-day-residual quintile, compare open-to-close return for high-score versus low-score names. Regress on gap, volume z-score and LPS drift. Cluster standard errors by date.
- **Step 2, minute-level simulation of survivors.**
  - Signal at the close of bar t, fill at the open of bar t+1 plus half-spread.
  - Use the full statutory fee matrix at actual rupee sizes.
  - A stop fills at the worse of the stop price and the next open.
  - Model stopped fills 10ΓÇô20 bp worse.
- **Metrics:**
  - net bp per name versus the equal-weight benchmark
  - net profit factor
  - daily Sharpe
  - date-clustered t-statistic
  - hit rate
  - max drawdown and worst day
  - per-year and per-regime results
  - entry-time curve
  - stop versus no-stop
  - results at 1.5├ù costs
- **Placebos, which should kill the effect if the signal is real:** delivery data lagged one day, and the mirror run on prior-day losers.
- **Statistical power:** basket daily ╧â is about 1.0ΓÇô1.1%. Detecting 10 bp net at t = 3 needs about 900 days. Detecting 20 bp needs about 225. This is why the cross-sectional regression comes first.
- **Kill criteria (abandon if any hold):**
  - Gate 1: high-minus-low open-to-close spread is under 12 bp gross; date-clustered t is under 3, counting every variant tried; the sign fails in more than 2 of 7 years; or the effect disappears after the controls. (Claude's gate was t ΓëÑ 3; Gemini's was 2.8. Use 3.)
  - The effect survives the placebos.
  - Minute-level: out-of-sample net edge under 8 bp per name versus benchmark, or net profit factor below 1.2 after costs **[added]**, or profit factor below 1.1 at 1.5├ù costs **[added]**.
  - The late-surge feature earns a slot only if next-day open-to-close for the top late-surge decile is at least 15 bp negative and the effect is concentrated in opposed-trend surges. Otherwise drop the feature.

### Paper-trading plan
- Run at least 40 trading days unattended on the broker API. It needs a heartbeat alert, a stale-feed halt, an idempotent order manager, position reconciliation, and the 15:10/15:12/15:13 exit ladder.
- **Pass criteria:** zero unreconciled positions, no missed exits, and realized slippage within about 3 bp of the model. 40 days cannot prove profitability; it can only verify operations and cost assumptions. For example, run 100 or more live days at small size before scaling **[added]**.
- Log realized versus modeled slippage and the A-versus-B daily P&L correlation. Require it to stay below 0.5.

---

## Strategy B: Peer-Rich Short (idiosyncratic lead-lag and reversion)

**Status: gated candidate.** It goes live only if the event study clears its gates. If it fails, shelve it and ship A alone.

### Core insight
Coverage and attention are siloed by ticker. When a stock pops alone, with no peer, sector or futures support, market-order chasers have pushed it away from its peer-implied fair move, and it reverts. When a leader suffers an idiosyncratic drop, lower-coverage peers reprice over minutes to hours, because their holders think only the leader was hit. The signal is a stock that is rich against its peer-implied move.

One honest note on mechanism: the daily-frequency version has no legally forced seller. The promoter-pledge cascade was debated and Gemini conceded it. A lender who is margin-called sells the pledged company's own shares, not the sister companies' shares. Pledge is now only a tag to test.

### Exact rules
- **Peer map.** The top 3 F&O peers per stock by 60-day partial correlation of 5-minute Nifty/sector-residual returns, with correlation at least 0.35. The transfer coefficient ╬│_ij is estimated on idiosyncratic residuals, not total betas, with ridge shrinkage, on rolling 60-day 15-minute bars, re-estimated monthly and frozen intraday.
- **Scan.** 5-minute bars from 10:00 to 14:30. At most 2 concurrent positions and 6 trades per day **[added]**. Per-position notional is at most 15% of capital **[added]**.
- **Reversion arm.**
  - **Trigger:** the 30-minute residual e_i ΓëÑ +3╧â against the stock's own time-of-day ╧â. Peers must be flat. There must be no filing in the last 120 minutes. Where single-stock futures 1-minute data exists, there must be no futures-volume confirmation.
  - **Entry:** the first 1-minute close below the prior bar's low, within 10 minutes of the trigger. A candlestick "engulfing" pattern is not allowed.
- **Diffusion arm.**
  - **Trigger:** the leader's 30-minute idiosyncratic drop is at least ΓêÆ2╧â, with Nifty not below ΓêÆ0.5%.
  - **Sector gate:** the sector residual |╬╡_sec| is at most 0.5%, so a whole-sector move is not mistaken for an idiosyncratic one.
  - **Peer deficit:** the peer's deficit ╬ö = ╬│┬╖╬╡_L ΓêÆ ╬╡_P is at most ΓêÆ0.60%, meaning it has captured under 35% of its implied move.
  - **Filing gate:** no peer filing in 120 minutes.
  - **Entry:** the first 1-minute close below the trailing 5-minute low, at least 5 minutes after the leader's drop.
- **Pledge-tagged arm.** A subset of diffusion events, tested as a split, not assumed.
- **Exits.**
  - Reversion: cover at a 50% retrace of the pop or after 30 minutes.
  - Diffusion: cover when ╬ö ΓëÑ ΓêÆ0.15% or after 75 minutes.
  - Stop: entry + 1.2╧â(15-minute), volatility-scaled and wide. Test against no stop.

### Who is on the other side, and why they lose
- **Reversion arm.** Market-order chasers, including retail and breakout bots, who push a thin book away from fair value. The liquidity providers who absorb the move are paid when it reverts.
- **Diffusion arm.** Holders and analysts of the lower-coverage peer who treat a sector-linked shock as leader-only. They lose because their attention is slow, not because anything forces them to.

### Conviction
- **Claude: 3.5/5.**
  - The signal is a known variant, with the stat-arb and HFT desks most likely already crowding the reversion arm.
  - The transfer coefficient is unproven; Claude thinks a leader-specific drop transmits at 0.1ΓÇô0.2, not 0.7.
  - The diffusion arm has only about 150ΓÇô250 independent events a year and does not trade daily.
  - The reversion arm needs a retrace-before-stop rate of about 62% against a roughly 60% breakeven.
  - Claude's prior odds that B passes its event study: about 25%.
  - It moves to 4 only if both arms pass.
- **Gemini: 3.8/5**, down from 4.2 after conceding the pledge mechanism. Gemini rates the information-diffusion lag and the 30ΓÇô75-minute hold as reachable by retail systems, with a high gross payout per event (45ΓÇô70 bp, an unverified estimate).

### Failure regimes
- Sector-wide or macro moves that look idiosyncratic, such as Budget and RBI days.
- Competitor-benefit events. A company-specific loss at the leader (e.g. a regulatory action on one plant) can help the peer, so the sign flips. Split by news type.
- Leaked news before filings, where a "pop" is real informed buying.
- Stat-arb crowding at short horizons, which would complete the reversion before entry.
- Wider spreads in lower-ADV peers eat the edge.

### Backtest plan
- **Data:** 1-minute OHLCV for cash (2022ΓÇô2026 or the longest available) and corporate-announcement timestamps. Single-stock futures 1-minute data is optional, and without it the futures-confirmation filter becomes an optional arm. Also needed: a static peer and sector map, and pledge data for the tag.
- **Step 1, event study with no trading rule.** Align peer cumulative abnormal return on the leader's time t0 out to +120 minutes. For the reversion arm, plot the cumulative residual path from the trigger, split by entry delay (0, 1, 2 and 5 minutes). Split by news filing versus none, same promoter group versus not, and peer ADV tercile.
- **Step 2, minute-level simulation of the surviving arms.** Same fill and cost conventions as A, at B's wider all-in friction of about 15ΓÇô20 bp.
- **Split:** hold 2022 to 2023 for development and 2024 to 2026 as out-of-sample.
- **Kill criteria (shelve B if any hold):**
  - Lower-ADV peers' CAR from t0+10 to t0+90 is not at or below ΓêÆ22 bp gross out of sample.
  - Less than 50% of the diffusion move occurs after minute 10.
  - The random-pair placebo shows |t| of 1 or more.
  - The retrace-before-stop hit rate is under 62%.
  - Under 40% of the reversion arm's reversion occurs after minute 5. In that case it completes before a retail system can enter.
  - More than 15% of triggers are followed by a filing within 60 minutes. The filing filter is then useless.
  - The effect lives only in the pledge-tagged subset, with fewer than about 40 events a year. That is not a daily strategy.
  - Minute-level net profit factor is under 1.2 after costs **[added]**.

### Paper-trading plan
Same infrastructure and 40-day minimum as A. B starts only after passing the event study and the minute-level gate. Track per-arm P&L separately. Also track the daily correlation of A and B.

---

## Remaining disagreements

1. **B's conviction.** Claude 3.5 versus Gemini 3.8. Claude thinks B's forced-seller mechanism is mostly narrative and that prop desks crowd the reversion arm. The event study decides.
2. **Size of A's edge.** Gemini expects 38ΓÇô55 bp gross per basket-day. Claude's prior is 10ΓÇô25 bp gross per name. The two-hour daily-data test will show which is closer.
3. **The late-surge feature inside A.** Gemini rated close-marking higher (4.2 as a standalone idea). Claude gave it 3.5 and made its slot conditional on the square-off-echo sub-test.
4. **Unverified facts.** The futures STT rate and the expiry weekday were never confirmed. Neither changes the cash-MIS plan.
5. **Settled in the debate** (listed only so nobody reopens them):
   - Per-ticker client-category OI does not exist.
   - The 5├ù intraday-margin cascade is off by about 10├ù.
   - The month-end 2.5├ù sizing knob is data-mined.
   - The LPS sign was corrected.
   - The 7-feature, hand-weighted score was cut to 4 equal-rank features.

## Build order
1. Data audit: point-in-time F&O list, adjusted 1-minute data, and whether futures minute data exists.
2. A, gate 1 (daily-data test).
3. B event study.
4. Minute-level backtest of the survivors.
5. Paper trading (40 days minimum), then small live size.

## Bottom line
After the debate, one strategy (A) has both AIs' backing and one (B) is conditional. Neither has been tested. Claude's own prior is only about 35ΓÇô40% that A passes its first gate and about 25% that B passes its event study. Their convictions are opinions. The pre-registered backtests and the unattended paper run decide, and even a pass would not guarantee profit.
