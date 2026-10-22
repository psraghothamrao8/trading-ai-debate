# AUDITED FINAL REPORT: Intraday NSE Short-Only Book (one strategy)

**Read this first.** AI conviction is not evidence of profitability. Every conviction score here is an opinion. Nothing in this report has been run on data, and every threshold is an unvalidated starting value. Only a pre-registered backtest and an unattended paper run can show whether this works. Even a pass would not guarantee future profit. There are no guarantees.

**Source tags** in the parameter table: R = from the original report, AU = from the audit, N = new in this version (unvalidated).

---

## 1. What changed after the audit

| Item | Verdict | Change (one line) |
|---|---|---|
| Strategy A | Kept, fixed | Cheapest to kill and the only idea with a plausible daily trade count. |
| Strategy B | Dropped | It fails the daily-operation bar, its payoff arithmetic is inconsistent, and my conviction is 3.5. See section 7. |
| Gate 1 timing (AU Flaw 2) | Accepted | A daily open-to-close test credits the 09:15-09:46 unwind, which cannot be traded. Gate 1 now runs on minute bars, 09:46 open to 15:08 open. |
| Gate 1 threshold | Fixed | The audit says "18 bp gross" in one place and "18 bp net" in another. The original 12 bp high-minus-low spread is only about 6 bp on the short leg, below the 13.5 bp cost. The new gate is short-leg excess of at least 20 bp gross (13.5 bp cost plus 8 bp required net, rounded down). |
| Upper-circuit and auction trap (AU Flaw 1) | Accepted, simplified | Band distance goes from 3.5% to 5.0%, with a cover trigger at 2.0%. Per-name size goes from 25% to 20% of capital, so a 20% close-out costs about 4% of capital. I dropped the audit's "95% touch probability" test because it has no spec and the stop makes it redundant. |
| Book-level stop (AU Flaw 3) | Partly rejected | A +5.5% runner cannot happen with a roughly 2.2% per-name stop unless the stock gaps. Removing the book stop would drop the only guard against correlated squeezes. I kept a backstop: day-loss stop 1.5% to 2.0% of capital, Nifty stop anchored to the 09:46 level instead of the open. |
| Exit ladder (AU) | Accepted, adjusted | Passive cover from 15:05, marketable limit at 15:08, hard flat at 15:10, with reconciliation at 15:12. |
| Minimum notional (AU) | Replaced | The audit's Rs 2 lakh floor is arbitrary. A 7.0 bp cost cap (about Rs 1.4 lakh per leg) replaces it, which implies a minimum capital of about Rs 7 lakh. |
| Delivery and float data (AU) | Accepted | Features use ratios and rupee values only (delivery %, Rs turnover / Rs free-float market cap), never raw share counts. |
| Broker MIS rejections (AU) | Accepted | The entry logic walks down the ranked list, and a rank-robustness test is added. |
| Point-in-time F&O list | Made concrete | Build it from the underlyings in each day's F&O bhavcopy. |
| A-vs-B correlation tracking | Removed | B is dropped. |
| Original gate wording | Fixed | The garbled symbols are gone and every formula is defined below. |

---

## 2. Novelty, honestly

A is not a breakthrough. It is a variant of the overnight/intraday and attention-driven reversal literature (Lou-Polk-Skouras and related). What is specific here is the feature set, the filters, and the fact that it is a fully coded daily rank rule. Whether anything survives costs is unknown. "Never tried" is unverified.

---

## 3. Shared infrastructure (final)

**3.1 Conventions.**
- All times are IST.
- A 1-minute bar stamped hh:mm spans hh:mm:00-hh:mm:59 and is known at hh:(mm+1):00.
- "Price at 09:46" means the open of the 09:46 bar.
- Prices are corporate-action adjusted.
- Nifty means the Nifty 50 index.
- Returns are log returns.

**3.2 Cost function.** For notional N rupees per leg (short sell, then buy to cover), verify every rate on a current contract note in week 1:

- brokerage = 2 x min(20, 0.0003 x N)
- STT = 0.00025 x N (sell leg)
- exchange = 0.0000297 x 2N
- SEBI = 0.000001 x 2N
- stamp = 0.00003 x N (buy leg)
- GST = 0.18 x (brokerage + exchange + SEBI)
- slippage = 3.5 bp per side (test 2-7). Stop exits take an extra 10 bp (test 5-20).

At N = Rs 2 lakh, statutory plus brokerage is about 5.9 bp. With 7 bp slippage the all-in cost is about 13 bp, and 13.5 bp is kept as the hurdle. **Pre-trade cost cap:** reject any name where statutory plus brokerage at the planned notional exceeds 7.0 bp (N below about Rs 1.4 lakh). At 20% per name and 4 names, minimum viable capital is therefore about Rs 7 lakh. Below that, paper-trade only.

**3.3 Universe, evaluated on D-1 data.**
- The top 120 names by 60-day median daily turnover (Rs), among underlyings present in the D-1 F&O bhavcopy.
- Price at D-1 close of at least Rs 250.
- A spread filter cannot be computed from OHLCV, so the backtest relies on the turnover rank. Live, skip any name with a quoted spread above 8 bp at 09:45.

**3.4 Per-name exclusions.**
- F&O ban list, ASM/GSM, T2T.
- Names the broker will not short on MIS (morning list, plus order rejection).
- A result or board-meeting date, or an ex-date, falls on D.
- Up more than 7% from the D-1 close at the 09:45 close.
- If an exchange price band exists for the name, within 5.0% of the upper band at 09:45. Read bands from the exchange's daily price-band file. Do not assume F&O names carry static cash-segment bands.

**3.5 Day-level rules.**
- No trading on Budget day or general-election result day.
- Live, run half size on RBI policy days and on monthly stock-F&O expiry days. Tag expiry as the date the near-month contract disappears from the F&O bhavcopy.
- The backtest runs these days at full size, flagged, and reports them separately.

**3.6 Risk and sizing.**
- Notional per name = min(20% of capital, 0.5% of the rupee turnover in the 09:41-09:45 bars).
- At most 4 names, so gross is at most 80% of capital. No leverage above 1x until after 100 live days.
- **Per-name stop:** see 4.3.
- **Nifty stop:** flatten everything if Nifty is at least +1.2% above its 09:46 close (test 0.8-1.6 or off).
- **Day-loss stop:** flatten if mark-to-market loss reaches 2.0% of capital (test 1.5-3.0 or off). This is a backstop for gaps through stops.
- **Auction tail:** an intraday short that cannot be covered becomes an exchange auction obligation next day. Close-out can be around 20% above the reference price plus penalties (verify the exact rule with the broker). Worst case at 20% sizing is about 4% of capital per event.
- **Benchmark:** report P&L against the equal-weight return of the same universe over the same window, not against zero.

**3.7 Exit ladder, all names.**
- 15:05: passive buy-to-cover at the bid.
- 15:08: marketable limit.
- 15:10: market-with-protection.
- 15:12: pull the broker position API and reconcile.
- 15:13: if anything is open, emergency market-with-protection plus an alert.

The ladder finishes before the broker's own auto-square-off. Confirm that time with the broker, since it varies and could not be verified here.

**3.8 Broker and operations.**
- Use a domestic API broker. Confirm static-IP, order-rate and algo-registration rules under SEBI's retail-algo framework.
- Stops are software stops on the tick feed. On trigger, send a marketable limit buy at LTP x 1.003 and re-price every 3 seconds.
- The system needs a heartbeat alert, a stale-feed halt, an idempotent order manager and position reconciliation.

---

## 4. Strategy A: Overnight Hangover Panel (final spec)

### 4.1 Mechanism and who loses
Retail and operator money chases yesterday's winners, especially in the first half hour. Liquidity providers who sold into that demand lay off inventory during the day. A late-session mark-up (the NSE close is the last-30-minute VWAP) has no one defending it the next day. The counterparty is behaviourally wrong, not forced, so this is not a "forced seller" trade.

### 4.2 Definitions (day D; D-1 is the previous trading day)
1. R_i = ln(C_i,D-1 / C_i,D-2). R_N is the same for Nifty.
2. beta_i is the OLS slope of daily R_i on R_N over days D-61..D-2, clipped to [0.3, 2.0].
3. e_i = R_i - beta_i x R_N, the residual return.
4. z(x) = (x_D-1 - mean of x over D-61..D-2) / stdev of x over D-61..D-2.
5. Features:
   - f1 = z(e_i)
   - f2 = z(Rs turnover_i / Rs free-float market cap_i). Free-float shares come from the latest shareholding filing dated before D-1, times C_D-1.
   - f3 = -z(delivery %), using DELIV_PER from the security-wise delivery file for D-1. A low delivery % means a high score.
   - f4 = z(L_i), where L_i = ln(close of 15:29 bar / close of 14:59 bar) - beta_i x Nifty return over the same window. If D-1 was an index-rebalance or expiry-settlement day, f4 is missing and S averages the remaining features.
6. r_k,i is the cross-sectional percentile rank (0 to 1) of f_k across the universe on D-1.
7. **Score** S_i = mean(r_1..r_4).
8. **Eligible set** E = names with r_1 >= 0.80.
9. **Gate G** is the 80th percentile of S over all in-sample stock-days. It is frozen from scores only, never from outcomes. If fewer than 85% of in-sample days have at least one eligible name with S >= G, step G down through the 75th, 70th, 65th and 60th percentiles until that holds.
10. **LPS control** (regression only) = mean over D-61..D-2 of (overnight return - intraday return). A high value means the stock habitually loses intraday. It is a control, not a penalty.

### 4.3 Daily procedure
- **09:00:** compute S and E from D-1 data. The score is never refreshed intraday.
- **09:45:59:** apply the day-level rules and per-name exclusions to the list E with S >= G, sorted by S descending (ties by f1). Walk down the list and keep the first 4 names that pass the exclusions, the cost cap and the size cap.
- **09:46:00:** send a marketable limit sell at best bid x (1 - 0.0005). Cancel any unfilled remainder at 09:47:00. Do not chase. Keep partial fills.
- **Stop price** = entry fill x (1 + k x sigma_i). Here sigma_i is the stdev over D-61..D-2 of ln(open of 15:08 bar / open of 09:46 bar). Start with k = 2.0 and clip the stop distance to [1.2%, 3.5%].
- **Band cover trigger:** if an upper band exists and the price comes within 2.0% of it, cover immediately.
- **15:05-15:13:** exit ladder (3.7).

**Backtest fills:**
- Entry fill = open of 09:46 bar x (1 - 3.5 bp).
- Exit fill = open of 15:08 bar x (1 + 3.5 bp).
- A stop triggers on the first bar with high >= stop. Fill = max(stop, bar open) x 1.0010, then plus 3.5 bp slippage.
- Fees follow 3.2, at actual rupee sizes.
- "Gross" means mid-price, zero cost.

### 4.4 Parameters

| Parameter | Start | Test range | Source |
|---|---|---|---|
| Universe size | 120 | 80-150 | R |
| Min price | Rs 250 | 150-400 | R |
| Beta and z windows | 60 days | 40-120 | R |
| Eligibility cutoff on r_1 | 0.80 | 0.70-0.90 | R |
| Gate G (percentile of S) | 80th | 60th-85th, frequency rule only | R |
| Max names | 4 | 2-6 | R |
| Entry time | 09:46 | 09:20, 09:30, 09:46, 10:00, 10:30, and 09:47 (latency) | R |
| Exit reference | 15:08 | 15:00, 15:05, 15:08, 15:12 | AU/N |
| Stop k | 2.0 | 1.5, 2.0, 3.0, none | R |
| Stop floor and cap | 1.2% / 3.5% | n/a | N |
| Per-name notional | 20% capital | 10-25% | N |
| Participation cap | 0.5% of 09:41-09:45 turnover | 0.25-1% | R |
| Day-loss stop | 2.0% capital | 1.5-3.0 or off | N |
| Nifty stop | +1.2% above 09:46 level | 0.8-1.6 or off | N |
| Band reject / cover | 5.0% / 2.0% | 3.5-7 / 1-3 | AU |
| Up-on-day exclusion | 7% | 5-10% | R |
| Cost cap | 7.0 bp | 6-8 | AU |
| Slippage per side | 3.5 bp | 2-7 | R |
| Extra stop slippage | 10 bp | 5-20 | R |

### 4.5 Ablations (descriptive only)
The base spec is frozen before the first test. An ablation changes the base only if it adds at least t = 2 on OOS1 and improves in-sample net edge. The ablations are:
- Confirmation arms: none (base), `P < C_prev`, `P < Open`. Do not use `P < VWAP`.
- Entry-time curve.
- Open-ended stop vs. no stop.
- Residual against Nifty plus a sector index (a carry-over from B).
- Extra features: change in OI x sign(return), a bulk/block net-sell flag, turnover per trade (retail proxy).
- Regime skip: no trade if Nifty is more than +0.6% up over 09:15-09:45.

**Late-surge feature (f4) slot rule.** f4 keeps its slot only if both hold:
- The top late-surge decile's next-day 09:46-15:08 short-leg excess is at least 15 bp with date-clustered t >= 3.
- The effect is at least 1.5x larger for "opposed" surges than for "aligned" ones.

A surge is "opposed" if its sign differs from the sign of the residual open-to-14:59 return. Otherwise S = mean(r_1..r_3), and G is re-frozen once by the frequency rule.

### 4.6 Failure regimes
- Strong trend-up days with persistent FPI/DII inflow, where all four shorts get squeezed together.
- The overnight gap having already absorbed the reversal, which would make this a gap-fade, a pattern the brief rejects.
- Real news re-rating a stock.
- Retail leverage and margin regime changes. Split reporting at September 2021 and October 2024.
- Stuck, band-adjacent or ban-list names.
- Expiry-day closes that are real settlement marks.
- Budget, RBI and election days.
- Delivery-% data being public, so others may crowd the same signal.
- Broker MIS blacklists removing the top-ranked names.

### 4.7 Conviction (not evidence of profitability)
- Pre-audit: Claude 4/5, Gemini 4.5/5.
- **Mine now: 3.5/5.** I suspect much of the effect, if it exists, happens before 09:46, which would make it untradable. This is a suspicion, not a finding.
- My prior that A clears Gate 1 is about 20-30%, down from 35-40% because the tradable window is harsher.
- Gemini's 38-55 bp gross per basket-day is unverified and treated as hope.
- A is still the first thing to test because it is the cheapest to kill.

---

## 5. Test plan and kill criteria

**Data needed:**
- Adjusted 1-minute OHLCV for the universe, plus Nifty 50 minute data.
- Daily bhavcopy with delivery quantities.
- Daily F&O bhavcopy, for the point-in-time list and expiry tags.
- Free-float history.
- Ban, ASM/GSM, price-band and board-meeting/ex-date calendars.
- Bulk/block files (ablations only).

**Splits.**
- Holdout: October 2024 - September 2026, touched once, at the end.
- In-sample (IS) and OOS1: IS is 2018-2021 and OOS1 is 2022-September 2024. If minute data begins later, split the pre-October-2024 data 60/40 by date.
- If fewer than 600 trading days precede October 2024, the verdict is "inconclusive", not "pass".

**Gate 0 (data audit).**
- Corporate-action continuity checks on known split/bonus days.
- Timestamps are known to be bar-start.
- Point-in-time F&O list rebuilt.
- No-look-ahead assertions on every feature.

**Gate 1 (IS, tradable window). Kill if any one fails:**
- Outcome per stock-day: y_i,d = -[ln(open 15:08 / open 09:46) - EW_d] in bp, where EW_d is the equal-weight mean of the same-window log return over the universe. Positive is good for a short.
- (a) **Portfolio test:** the mean of y over selected stock-days is at least 20 bp gross, with date-clustered t at least 3.0.
- (b) **Regression:** within E, y on S with date fixed effects and controls: opening gap residual, 09:15-09:45 return, opening-window volume z-score, LPS. The coefficient on S must be positive with date-clustered t at least 3.0.
- (c) **Sign stability:** mean y is positive in at least 5 of 7 calendar years, or in at least 70% of half-years if the sample is shorter.
- (d) **Placebo 1 (mirror):** run the identical pipeline on the bottom r_1 quintile (prior-day losers). Kill if their short-leg excess is at least +5 bp with t at least 2, because then the effect is not specific to winners.
- (e) **Placebo 2 (stale features):** use f2-f4 from D-2. The edge must fall by at least 50%, or the score is capturing a persistent stock trait.
- (f) **Placebo 3 (permutation):** the real mean must exceed the 99th percentile of 1,000 within-date permutations of S.
- (g) **Frequency:** at least 85% of days have at least one trade.
- (h) **Rank robustness:** using ranks 3-6 instead of 1-4 must retain at least 60% of the base edge, or at least 12 bp.

Report the open-to-09:46 and 15:08-to-close segments separately as diagnostics. Count every variant tried.

**Gate 2 (OOS1 minute simulation, Rs 10 lakh capital, 20% per name). Kill if any one fails:**
- Net edge vs. equal-weight benchmark of at least 8 bp per name (t at least 2).
- Absolute net P&L positive, and net profit factor at least 1.2.
- Profit factor at least 1.1 at 1.5x costs.
- Profit factor at least 1.0 after adding one random -20%-of-notional auction loss per year.
- Max drawdown no more than 15% of capital.
- Report per-year, per-regime, expiry/RBI-flagged days, stop vs. no-stop, and the entry-time curve.

**Gate 3 (holdout, once, no retuning). Kill if any one fails:**
- Net edge of at least 5 bp per name vs. benchmark.
- Net profit factor of at least 1.15.
- Same sign as OOS1.

**Power note.** Absolute basket P&L (daily sigma about 1.0-1.1%) needs about 900 days to show a 10 bp net edge at t = 3. The market-neutral excess test needs far fewer days. Measure sigma_excess in week 1.

---

## 6. Paper trading

**Operations check, 40 trading days, unattended on the broker API.**
- Pass criteria: zero unreconciled positions, flat by 15:12 every day, no unhandled rejection, and realized round-trip slippage within about 3 bp of the model.
- This verifies operations and cost assumptions only. It cannot prove profitability.

**Live validation.**
- Run at least 100 live days at the minimum cost-efficient size (about Rs 1.4-2 lakh per name, at most 2 names). Below that size, brokerage inflates costs.
- Review realized net per name against the model before any scaling.

---

## 7. Strategy B: dropped

Agreed with the audit on the conclusion, not on every reason.

**Agreed:**
- The diffusion arm trades about 150-250 events a year, which fails the daily-operation bar.
- The report's 62% breakeven could not be derived from its own numbers. The audit's inputs (45 bp target, about 75 bp stop, about 20 bp friction) give about 79%. Even a stop half as wide gives about 70%.
- My conviction is 3.5 and the prior of passing its event study is about 25%, which is below the bar for listing.

**Not accepted:**
- The audit's HFT-latency argument concerns microsecond mispricings. The reversion arm targets 30-minute moves, and the report's own kill criterion (under 40% of reversion after minute 5) already tests whether the effect outruns a retail system.
- The audit's fixes work against each other. A 2-peer sector-basket requirement changes the premise, and the ADV > Rs 100 Cr and spread <= 3 bp caps push the universe into the most arbitraged names.

B is not revived without a new, written case. The one piece carried forward is the sector-residual ablation in 4.5.

---

## 8. Build order

1. **Gate 0: data audit, fee function and spec freeze.** It blocks everything else. Pre-register the parameter file before any outcome is computed.
2. **A Gate 1 (IS only).** It is the cheapest decisive test. Do not unlock OOS1 until the IS verdict is written down.
3. **A Gate 2 (OOS1 minute simulation)**, only if Gate 1 passes.
4. **Execution skeleton and paper-trading harness**, started only after Gate 1 passes. Building them earlier risks wasted work.
5. **Gate 3 (holdout, once)**, then 40-day paper trading, then 100+ live days at minimum size.

If A dies at Gate 1, the adjusted minute panel, universe and fee model carry over. The next step is new ideation, not a fallback to B.

---

## 9. First week

- **Day 1: spec and data.** Write the parameter file (4.4) and commit it before any test. The working directory is not a git repo, so `git init` first. Inventory the data and check minute coverage. Rebuild the point-in-time F&O list from daily bhavcopies. In parallel, check the broker's static-IP, rate-limit and algo-registration rules, and its MIS short list and auto-square-off times.
- **Day 2: infrastructure.** Implement the fee function and unit-test it against one real contract note. Build the adjusted daily panel: returns, beta, z-scores, f1-f4, S, E. Add the no-look-ahead assertions.
- **Day 3: Gate 1 core.** Build the 09:46-15:08 outcomes and the equal-weight benchmark. Run the portfolio test and the regression on IS. Choose G by the frequency rule, using scores only.
- **Day 4: Gate 1 robustness.** Run the three placebos, the rank-robustness test, the year splits and the open-to-09:46 diagnostic. Then run the f4 slot test and the entry-time curve.
- **Day 5: verdict.** Write a one-page pass/kill memo against the Gate 1 criteria. If it passes, start the Gate 2 simulator and the paper harness. If it fails, record the kill and stop. Do not retune on OOS1.

---

## 10. Bottom line

One strategy survives the audit, and its conviction is lower than before. The most likely failure is that the effect lives in the first 30 minutes and is gone by 09:46. If it is real, the 20 bp gross, 8 bp net and 5 bp holdout gates are meant to catch it before any capital is risked. AI conviction is not evidence of profitability, and nothing here is guaranteed.
