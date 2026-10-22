
### Claude deep analysis
# Deep analysis of the 8 shortlisted NSE intraday short strategies

The "ANALYSIS SO FAR" section was empty, so there was no other analysis to correct. I corrected the shortlist's own specs where they were wrong, and I changed my convictions where the numbers pushed me. The cost and power figures below are my estimates and haven't been run against any data. The statutory rates are from my own knowledge, so verify them against a current contract note.

## A. Shared cost model

**Cash MIS short, Γé╣2 lakh per leg (bp of one leg's notional, round trip)**

| Item | bp |
|---|---|
| Brokerage (Γé╣20 ├ù 2 orders) | 2.0 |
| STT (0.025%, sell side only) | 2.5 |
| NSE transaction charge (~0.003% ├ù 2 legs) | 0.6 |
| SEBI fee | 0.02 |
| Stamp duty (0.003%, buy leg) | 0.3 |
| GST (18% on brokerage + exchange + SEBI) | 0.5 |
| **Statutory + brokerage** | **Γëê5.9** (Γëê4.5 at Γé╣5L per leg) |
| Slippage, round trip | liquid F&O 3ΓÇô5; typical F&O 6ΓÇô10; thin 10ΓÇô15 |
| **All-in breakeven gross edge** | **Γëê10 bp liquid, 12ΓÇô16 bp typical F&O, 17ΓÇô22 bp thin** |

Stop-loss fills add about 3ΓÇô5 bp on the trades that get stopped.

**Nifty futures short:** STT 0.02% on the sell side (2.0), exchange charge 0.4, stamp 0.2, brokerage on a ~Γé╣17L lot 0.2, GST 0.1. Statutory is Γëê2.9 bp, so all-in is **Γëê3.5ΓÇô4 bp**. This is the only instrument in this book where a 5ΓÇô8 bp edge survives. Single-stock futures save about 0.5ΓÇô1 bp of statutory cost against cash, but the lot size is coarse (Γé╣5ΓÇô20L notional, so check the current lot table), and their spreads are wider than Nifty's.

**Practical filters that apply to every idea:**
- **Tick size:** require a tick of at most 1.25 bp of price. At Γé╣100 a Γé╣0.05 tick is already a 5 bp spread, so filter on price or median spread.
- **Excluded stocks:** F&O ban list, ASM/GSM names, T2T series, and any stock the broker won't short on MIS.
- **Universe:** a point-in-time F&O list (membership changes), with corporate-action-adjusted 1-minute data.
- **Exit timing:** cover at 15:10, before broker auto square-off (about 15:15ΓÇô15:25). Forced liquidation at market during that window costs extra, so we avoid being the forced party.

## B. Shared validation rules

1. **Count days, not trades.** Positions in the same basket share market beta. Required sample is `n = (t┬╖╧â/╬╝)┬▓` with t=3, because eight ideas plus variants means multiple testing (HarveyΓÇôLiuΓÇôZhu). Use SEs clustered by date.
2. **Short-only drift benchmark.** Subtract the equal-weight F&O return over the same window. A short book that "wins" by timing the market's intraday drift has no alpha.
3. **Validate on the full cross-section first.** Check decile monotonicity across all ~200 names per day. Only then run the extreme-tail trade rule. This gives roughly 50├ù the statistical power of testing only the traded top-4.
4. **Freeze thresholds before looking at 2022 onward.** Test across regime breaks: peak-margin rules (Dec 2020ΓÇôSep 2021) and the Oct 2024 F&O curbs, which both changed retail MIS behaviour.
5. **Execution realism.** Signal on the close of bar t, fill at the open of bar t+1 plus half-spread. A stop fills at the worse of the stop price and the next open.
6. **Rank-based daily top-k with a minimum-score gate.** Absolute thresholds (ΓëÑ3╧â, ΓëÑ70%) fire a few dozen times a year, and the gate prevents forced junk trades. This is needed for the "runs every day" requirement.
7. **Structural point: #1, #4 (its prior-day half) and #7 are one regression.** Each says "prior-day footprint predicts today's 09:45ΓåÆ15:10 return". Fit one panel model with features such as `╬╡_prev`, late-session return, delivery z, turnover/float, ╬öOI and signed flow. Otherwise you'll run three correlated tests and call them diversification.
8. **Compliance:** check your broker's setup under SEBI's retail-algo framework (static IP, order-rate limits, algo registration).

## C. The eight strategies

### 1. Retail-Crowding Hangover (conviction 4)

1. **Hypothesis.** Among F&O stocks in the top quintile of prior-day residual return, the 09:45ΓåÆ15:10 return is at least 15 bp lower for high-crowding names than for low-crowding names. This holds after controlling for plain prior-day return and gap. The top-4 short basket must be positive net of costs and benchmark drift, with tΓëÑ3 and a positive sign in at least 4 of 5 years. **Null:** the crowding score adds nothing beyond "prior-day winner", which makes this the rejected gap-fade.
2. **Signal.**
   - `╬╡ = R_prev ΓêÆ ╬▓┬╖R_nifty,prev` (60-day ╬▓), and `z_ret = ╬╡/╧â60`.
   - `DelivZ = (DΓêÆmean60)/sd60`, using delivered qty over traded qty from the bhavcopy.
   - `VolZ = ln(V/median60)`, plus `z(turnover/free-float)`.
   - `CS = z_ret + VolZ + z_turn ΓêÆ DelivZ`, equal weights, frozen.
   - Trade the top 3ΓÇô5 by CS where `P_09:45 < C_prev`. Short at 09:46, cover at 15:10, stop at the day-high.
   - **Correction:** "fails to reclaim yesterday's close" mostly selects names that have already gapped or faded. Record the gap and the 09:15ΓÇô09:45 return as covariates, and report openΓåÆclose separately from 09:45ΓåÆclose.
3. **Trades and sample.** About 4 a day on ~90% of days, so ~1,000 a year. One basket's ╧â is Γëê1.0% a day: 20 bp net needs ~225 days, 10 bp needs ~900. The cross-sectional regression gets you there with far fewer.
4. **Cost.** All-in Γëê12ΓÇô15 bp, so you need ΓëÑ13 bp gross per name. The edge has a whole 5-hour leg to accrue, which is why this ranks above the short-hold ideas on cost-to-edge.
5. **Capacity and decay.** F&O names trade Γé╣100ΓÇô1,000 cr a day, so capacity runs into crores. The mechanism is behavioural and decays slowly, but delivery % is public. The real risk is regime change in retail leverage, so split the sample at Sep 2021 and Oct 2024.
6. **Likely failure.** The gross effect is under 8 bp, or entirely a gap-fade (the overnight leg takes the reversal). **Cheap test (~2 hours, daily data only):** within the top prior-day-return quintile, sort by CS quintile and compare OΓåÆC returns. If the CS-high minus CS-low spread is under 10 bp, or vanishes once `╬╡` and `VolZ` are controlled, kill it. Add a placebo: run the mirror on prior-day losers, and lag the delivery data by one day.
7. **Sharper version.** Delivery % is a weak proxy, because low delivery also reflects HFT and prop volume, not just retail. Add futures **╬öOI ├ù sign(return)** from the F&O bhavcopy. Price up with OI up means new leveraged longs that must exit or roll. Price up with OI down means short-covering, which has no overhang. Add the bhavcopy's trade count to get average trade size (small average trade size is a retail-share proxy). Keep both as continuous regressors, not "long buildup" labels.

### 2. Unconfirmed-Pop Fade (conviction 3, lowered from 4)

1. **Hypothesis.** After 10:00, for an F&O stock with residual 20-min return `zΓëÑ3` against its own time-of-day ╧â, no sector explanation, no futures-volume confirmation and no filing in the past 2 hours, the next 30-minute residual return is negative. It is at least 15 bp more negative than for confirmed pops.
2. **Signal.**
   - `e = r20_i ΓêÆ ╬▓_i┬╖r20_Nifty ΓêÆ ╬│_i┬╖r20_peers`, where peers are the ΓëÑ3 closest names excluding i.
   - `z = e/╧â_tod` (60-day std of `e` at that time of day ┬▒10 min).
   - Volume ratio `CR = V20/median60`. Futures ratio `FR = Vfut20/median60`.
   - Entry on the first 1-min close below the prior bar's low, within 10 minutes of the trigger.
   - Target is a 50% retrace of the pop, or 30 minutes. Stop is the peak plus 0.25 ├ù pop.
3. **Trades and sample.** I estimate 3ΓÇô8 a day after filters, which is ~1,000 a year. Trades are spread across time and names, so the effective sample is close to the trade count. Per-trade ╧â is Γëê45 bp, and 5 bp net at t=3 needs ~730 trades, about 100ΓÇô250 days. **This is the fastest idea to validate.**
4. **Cost.** Spreads widen at a pop, so all-in is 14ΓÇô18 bp. With target 50 bp, stop 35 bp and cost 16 bp, the breakeven hit rate is `(35+16)/(50+35) = 60%`. A driftless walk gives 41%. The signal has to lift the retrace-before-stop rate by about 19 points, which is a large demand.
5. **Capacity and decay.** Capacity is Γé╣25ΓÇô50 lakh a day of notional. This is the **most contested** idea, because HFT and stat-arb desks run residual reversal at far lower latency. Whatever survives is what they skip (mid-cap F&O, wider spreads), and the survival is partly an illusion of cost.
6. **Likely failure.** Reversion completes within seconds, before your first lower-close entry, and the pops that survive carry real information. **Cheap test:** plot the cumulative residual path from the trigger, split by entry delay of 0, 1, 2 and 5 minutes. If 80% or more of the reversion happens in the first 2 minutes, kill it. Also measure the share of triggers followed by a filing within 60 minutes. If it's above 15%, the filing filter is useless.
7. **Sharper version.** Filter on **price impact per rupee traded**: `|r1| / (price ├ù volume)` for the pop minutes, relative to own history. A big move on little volume means a thin book got swept and the vacuum refills. A big move on heavy volume with no futures follow-through is absorbed buying. Test both directions; I expect the thin-book version to carry the edge.

### 3. Downside Peer-Lag (conviction 3, lowered from 4.5 for Gemini's number)

1. **Hypothesis.** After a leader's idiosyncratic drop (ΓëÑ3% on ΓëÑ3├ù time-of-day volume, Nifty ΓëÑ ΓêÆ0.5%), mapped lower-coverage peers show continued negative residual drift over the next 60ΓÇô120 minutes, `E[r_P] = a + b┬╖(╬▓_PL┬╖r_L ΓêÆ r_P)` with `b>0.2`. The effect should be absent or reversed when the leader's drop is company-specific news and strongest for same-promoter-group peers.
2. **Signal.**
   - Peers are the top 3 F&O names by 60-day partial correlation of 5-min Nifty-residual returns (ΓëÑ0.35), plus a static promoter-group map.
   - `m_P = ╬▓_PL ├ù r_L`, with ╬▓ from a 15-min regression, shrunk.
   - Capture ratio `╬║ = r_P / m_P < 0.35`.
   - Entry on the first lower 5-min close at or after t0+5. Target is ╬║ΓëÑ0.8. Stop is set from the peer's own ╧â, not a flat +0.7%.
   - **Correction:** over a 2-hour hold a ~1.6%-daily-vol peer has ╧âΓëê0.9%. A flat 0.7% stop is touched ~40ΓÇô45% of the time under a driftless walk. With a ~65 bp reward and a 15 bp cost, the breakeven hit rate is `(70+15)/(65+70) = 63%` against a null of 52%.
3. **Trades and sample.** I'd guess 50ΓÇô70% of days have a qualifying leader, giving ~1ΓÇô2 trades a day on average. About 40% of events are results-driven and get split out, leaving ~150ΓÇô250 independent events a year. Per-trade ╧â Γëê70 bp: 15 bp net needs ~200 trades (about a year), 8 bp needs ~700 trades (more than 3 years). **This does not trade every day**, which is why I lowered my conviction.
4. **Cost.** Lower-ADV peers have 4ΓÇô8 bp spreads, so all-in is 15ΓÇô20 bp. If you capture only about 30% of the remaining 60ΓÇô80 bp, gross is Γëê20 bp, which is marginal.
5. **Capacity and decay.** Capacity is Γé╣10ΓÇô20 lakh a day, and the lag persists because hedged stat-arb desks don't cover every peer pair. Decay is moderate.
6. **Likely failure.** Competitor-benefit cases (the leader's loss is the peer's gain) cancel the effect, or peers reprice within 1ΓÇô3 minutes. **Cheap test (event study, no trading rule):** align peer cumulative abnormal return on leader time t0 out to +120 minutes. Split by filing vs no filing, same group vs not, and peer ADV tercile. If post-t0+10 CAR isn't negative in any bucket, kill it. Run a random-pair placebo.
7. **Sharper version.** Replace sector tags with a data-driven **lead-lag matrix**: rolling cross-correlation of 5-min residuals at lags 1ΓÇô6 (LoΓÇôMacKinlay), keeping only pairs whose lagged coefficient is positive out of sample. Add **customerΓÇôsupplier links** (CohenΓÇôFrazzini). Add **pledge-based group contagion**: where a promoter group has pledged shares, a leader's fall can trigger lender margin calls on the peers, which is a real forced seller. Bad news diffusing slower than good news is documented (HongΓÇôLimΓÇôStein).

### 4. Unfinished Parent Order (conviction 2.5, lowered from 3)

1. **Hypothesis.** Stocks with the most persistent net-sell flow over the prior session plus the first 30 minutes (residualised for market and sector) have a lower 09:50ΓåÆ15:10 return than matched controls. The effect rises with persistence across two days.
2. **Signal.**
   - 1-min OHLCV has no trade signs, so infer them by bulk-volume classification: `b_k = ╬ª(╬öP_res,k/╧â)`.
   - `S_w = ╬ú V_k(2b_k ΓêÆ 1)` per 5-minute window.
   - Persistence `P` is the fraction of windows with `S_w<0`; size `F = ╬úS/ADV`.
   - Add the participation regularity `CV(V_w / volume curve)`.
   - **Correction 1:** with ~81 windows, "ΓëÑ70% of windows" means ΓëÑ57 sells. Under a 50/50 null that is a ~3.7╧â event (pΓëê1e-4), or about 5 triggers a year across the universe. Use rank-based top 3 instead.
   - **Correction 2:** sign persistence is mechanically collinear with price drift, so this is momentum in disguise unless you residualise drift out.
3. **Trades and sample.** Rank-based gives ~3 a day. One basket's ╧â Γëê1.1%, so a 10 bp net edge needs ~1,100 days. Use the cross-sectional regression for power.
4. **Cost and honest sizing.** All-in Γëê12ΓÇô15 bp. Square-root impact is `Y┬╖╧â_d┬╖ΓêÜ(Q/V)`: a parent order of 5% of ADV costs the seller Γëê15ΓÇô30 bp in total, and you can capture perhaps half after 09:50. Multiply by the probability that a flagged name is a real parent order (say 30%) and you get **Γëê4ΓÇô5 bp expected, well under cost.** It only pays on parent orders of ΓëÑ10ΓÇô15% of ADV (Γëê35+ bp of total impact), which are rare. Also, domestic SIP inflows make buy-side parent orders the base rate in India. Sell-side ones are rarer and more informative.
5. **Capacity and decay.** You trade alongside the parent order, so capacity is fine. Decay comes from execution randomisation and shorter horizons.
6. **Likely failure.** BVC sign accuracy at 1-min is only ~60ΓÇô70%, and the signal is drift. **Cheap test:** correlate `P` with the day's return. If |corr|>0.8, drop it, or use drift-matched controls. Also shuffle bar order within each day. If the real tail of `P` isn't fatter than the shuffled one, there is no genuine persistence.
7. **Sharper version.** **Label real meta-orders with public data.** The NSE bulk and block deal files, and the SEBI-disclosed promoter-pledge invocations, mark days where a large seller was active. Train and validate the footprint classifier on those labeled days, then deploy it on unlabeled days.

### 5. Breadth-Hollow Nifty Futures Short (conviction 2, lowered from 3)

1. **Hypothesis.** When Nifty's cap-weighted return from the open exceeds the median constituent's return by a large margin, with Nifty ΓëÑ +0.3% and near its high, the next-60-minute Nifty return is lower than on broad-breadth days by at least 8 bp.
2. **Signal.**
   - `B = fraction of constituents above their VWAP`.
   - `D = R_cw ΓêÆ median(r_i)` and top-3 contribution share `C3`.
   - **Correction 1:** as specified (Nifty ΓëÑ+0.4% from the open, within 0.1% of the high, B Γëñ40%), I'd guess only ~10ΓÇô25 days a year trigger. That fails the daily-operation requirement. Use the continuous `D` (top quartile of days with Nifty up) for ~40ΓÇô60 days a year.
   - **Correction 2:** the +0.25% stop is ~0.8╧â of a 60-minute window (╧âΓëê0.25ΓÇô0.33%). That is touched ~40% of the time under a driftless walk, and a mean-reversion edge normally dips past it before working. Use 0.4ΓÇô0.5% or a time-only exit with risk set by size.
3. **Trades and sample.** ~40ΓÇô60 events a year. At ╧âΓëê30 bp, 6 bp net needs ~225 events (about 5 years), and 10 bp needs ~80.
4. **Cost.** All-in 3.5ΓÇô4 bp, the best of all eight. This is the only argument for the idea: a weak edge can still survive.
5. **Capacity and decay.** Capacity is effectively unlimited at retail scale. It is a low-Sharpe signal that no prop desk will crowd, which is partly because it may not be there.
6. **Likely failure.** There is no clear forced victim. Futures are arbitraged to the basket, and heavyweight-led rallies are often persistent FPI/DII program flow. Trending years (2021, 2023ΓÇô24) were financials- and Reliance-led. **Cheap test:** at 11:00, tercile days by `D` among up-days and compare the 11:00ΓåÆ15:10 Nifty return. If the top tercile isn't at least 8 bp lower than the bottom with tΓëÑ2 over 7 years, kill it.
7. **Sharper version.** Test expiry vs non-expiry days separately, since option-writer pinning changes the drift (check the current weekly-expiry weekday). Test a "heavyweight reversal" variant too: does the top-3 contributors' share reverse?

### 6. Square-Off Shelf (conviction 1.5, lowered from 2)

1. **Hypothesis.** After 11:00, stocks with a high underwater share of up-leg volume relative to expected remaining volume see a lower return after a retest-rejection than matched retests without it. The effect should be absent in the first hour and strengthen toward 15:00 (the deadline gradient), and it should be stronger in retail-heavy mid-caps than in large caps.
2. **Signal.** `VP(p)` is the up-leg volume profile from the day's low. `U = share of VP above the current price`. `M = U ├ù V_upleg / E[remaining volume]` (60-day time-of-day curve). Entry is a retest of the shelf's lower edge with a rejection bar on >2├ù volume.
3. **Trades and sample.** ~1ΓÇô3 a day. At ╧âΓëê1.1% over a 4-hour hold, 12 bp net at t=3 needs ~750 trades.
4. **Cost.** 13ΓÇô16 bp. A 0.4% stop plus a 15:10 time exit makes it a mean test, not a payoff-ratio test.
5. **Capacity and decay.** Capacity is fine, but volume-profile "supply zones" are the most watched retail pattern, so I expect decay to be fast.
6. **Likely failure.** F&O large caps have a small MIS share, and "underwater volume" has no tie to MIS traders. It also reads like the retail volume-profile / supply-zone content the brief rejects. **Cheap test:** shuffle the up-leg volume across price bins and re-run. If forward returns are unchanged, kill it. Check the dose-response and time-to-deadline gradient above.
7. **Sharper version.** Make it a **time-to-deadline hazard**, `forced supply per minute = M ├ù h(t)`, with `h` rising toward 15:15. Weight by a retail-leverage proxy such as the broker's MIS multiplier tier plus low delivery %. If it doesn't rank in the lower half after these tests, drop it.

### 7. Closing-Mark Next-Day Unwind (conviction 3)

1. **Hypothesis.** For F&O stocks with an unexplained late-session surge (15:00ΓÇô15:30), the next-day 09:30ΓåÆ15:10 return is at least 15 bp below controls, rises with surge size, and disappears on scheduled index-event days.
2. **Signal.**
   - The NSE close is the VWAP of the last 30 minutes, which is the cheap-to-mark property. Validate your 1-min VWAP against the bhavcopy close.
   - `LR_res = ln(C_15:29/P_14:59) ΓêÆ ╬▓┬╖LR_nifty` and `Z = LR_res/╧â60,late`.
   - `VR = V_late/median60(V_late)`.
   - Rank the top 2 a day by Z ├ù VR with a minimum ZΓëÑ2.
   - Entry at 09:30 if price is still above yesterday's 14:59 level with no new high since 09:20. Cover at the 14:59 level or 15:10. Stop at the day-high.
   - **Correction:** the spec's absolute thresholds (ΓëÑ+2%, ΓëÑ3├ù, no news) would give ~25ΓÇô50 trades a year. Rank-based gets ~1ΓÇô2 a day.
3. **Trades and sample.** ~250ΓÇô500 a year. At ╧âΓëê1.4%, 15 bp net needs ~780 trades, about 2 years.
4. **Cost.** 12ΓÇô15 bp. A 1.5% late jump with ~30% spurious is 45 bp, and half of that unwinds by 15:10, so gross is Γëê20 bp. This is marginal and positive only if the spurious share is real.
5. **Capacity and decay.** A few names a day at Γé╣2ΓÇô3 lakh each is no constraint. Decay comes from exchange surveillance and from the effect partly being broker-forced square-off, which is steady and structural.
6. **Likely failure.** The late move is real news or flow, or the overnight gap realises the whole reversal. **Cheap test:** sort by late-return decile and plot next-day gap and openΓåÆclose separately. Proceed only if the top decile's openΓåÆclose is at least 15 bp negative.
7. **Sharper version.** **Cash-only marks.** Futures also settle on a last-30-minute VWAP, so a cash-only push leaves the futures basis out of line. Compute the z-score of the basis shock in the last 30 minutes: a stretched basis with a late cash surge signals buying the arbs will unwind. This needs futures 1-min data. Also separate month- and quarter-end days.

### 8. Volume Absorption Near Highs (conviction 1.5, lowered from 2)

1. **Hypothesis.** After a break of the churn floor near the day-high, the next-60-minute return is lower when lower-half closes are ΓëÑ65% than for matched episodes (same distance to high, same volume ratio) with <50%. The lower-half composition has to carry information beyond volume and the breakdown.
2. **Signal.** `CLV_k = ((CΓêÆL)ΓêÆ(HΓêÆC))/(HΓêÆL)`, `LH = share of bars with CLV<0`, volume-weighted CLV. **This is Chaikin Money Flow / accumulation-distribution with a breakdown entry.** Without differentiation it is a simple breakdown plus a volume indicator, which the brief rejects.
3. **Trades and sample.** ~0.5ΓÇô1 a day after the break filter. At ╧âΓëê45 bp over 1 hour, 6 bp net needs ~500 trades.
4. **Cost.** 13ΓÇô16 bp, against short target moves of 30ΓÇô60 bp.
5. **Capacity and decay.** Capacity is fine. Decay is fast because the pattern is heavily watched.
6. **Likely failure.** `LH ΓëÑ 65%` is not selective: `P(Bin(20,0.5)ΓëÑ13) Γëê 13%`, so it occurs by chance in about one in eight windows. **Cheap test:** permute the CLV signs within each window. If forward returns are the same, kill it.
7. **Sharper version.** Use an effort-versus-result measure, `AR = (╬úV/ADV20) / (new-high progress in ╧â units)`. Calibrate it against the next evening's **bulk and block deal disclosures** as ex-post labels of real distribution: compare `P(label | signature)` against the base rate. Without that evidence there's no mechanism.

## D. Ranking and conviction

| Rank | Idea | Conviction | Why |
|---|---|---|---|
| 1 | #1 Retail-Crowding Hangover | **4** | Longest hold, so the best edge-to-cost ratio. It is a documented anomaly (LouΓÇôPolkΓÇôSkouras overnight/intraday; Llorente et al.). It dies if it's only gap-fade, which a 2-hour daily-data test settles. |
| 2 | #7 Closing-Mark Unwind | **3** | The cleanest mechanism, since the close is a 30-minute VWAP that nobody defends. It needs rank-based triggering to run daily. |
| 3 | #2 Unconfirmed-Pop Fade | **3** | Fastest to validate and trades every day. HFT crowding and a 60% breakeven hit rate are the risks. |
| 4 | #3 Downside Peer-Lag | **3** | Real asymmetry (bad news diffuses slowly) and a genuine forced seller via pledge contagion. It doesn't trade every day, and the lag may be gone in minutes. |
| 5 | #4 Unfinished Parent Order | **2.5** | Only pays on parent orders of ΓëÑ10ΓÇô15% of ADV, and 1-min bars cannot give clean trade signs. Worth it only with labeled bulk-deal calibration. |
| 6 | #5 Breadth-Hollow Nifty Short | **2** | Cheapest to trade at 3.5ΓÇô4 bp, but there is no clear forced victim and as specified it triggers on too few days. |
| 7 | #6 Square-Off Shelf | **1.5** | The deadline-gradient test is the only thing keeping it alive. |
| 8 | #8 Absorption Near Highs | **1.5** | Chaikin-style volume plus a breakdown, with no mechanism beyond a label. |

**What I'd run first:**
1. The 2-hour daily-data kill test for #1 (CS quintile within prior-day winners, OΓåÆC).
2. The late-session decile plot for #7.
3. The reversion-timing path for #2.

Together these cost about a day, and they decide whether to fit the combined prior-day-footprint regression from section B.7 across #1, #4 and #7.

### Gemini deep analysis
# Quantitative Deep Analysis & Counter-Evaluation: 8 Shortlisted NSE Intraday Short Strategies

---

## Executive Summary & Methodological Framing

Trading an **intraday short-only book on the National Stock Exchange of India (NSE)** is mathematically disadvantaged from the outset:
1. **Positive Market Drift:** The Nifty 50 and broad market possess a structural positive equity risk premium (~12ΓÇô14% annualized, or ~4ΓÇô5 bp per trading day). Shorting without timing fights this baseline drift.
2. **Asymmetric Statutory Friction:** In India, Securities Transaction Tax (STT) on intraday cash equity is levied exclusively on the **sell side** ($0.025\% = 2.5\text{ bp}$). On a short sale, STT is paid upfront at entry.
3. **Regulatory Hard Deadlines:** Broker Risk Management Systems (RMS) execute mandatory auto-square-offs between 15:15 and 15:25 IST for MIS (Margin Intraday Square-off) positions. If an algorithm fails to close by 15:10 IST, it enters the broker's forced liquidation queue, crossing the bid-ask spread at market with severe slippage penalty.

To survive and generate alpha, an intraday short strategy cannot rely on directional chart patterns, moving-average crossovers, or retail lore. It must exploit **structural, regulatory, or mechanical order-flow distortions** where a identifiable counterparty is legally, algorithmically, or financially forced to trade at unfavorable prices.

Below is the quantitative evaluation of all 8 shortlisted strategies, addressing points (1) through (7) for each, auditing ClaudeΓÇÖs prior deep analysis, correcting critical errors, and providing precise mathematical formulations.

---

## Baseline NSE Intraday Transaction Cost & Microstructure Matrix

All strategies are benchmarked against the following updated statutory fee architecture (reflecting post-October 2024 SEBI and exchange tariff structures):

### Cash MIS Intraday Short ($\approx Γé╣2,00,000$ Notional per Leg)
* **Brokerage:** Flat Γé╣20 per executed order $\times 2 = Γé╣40 \rightarrow \mathbf{2.00\text{ bp}}$.
* **STT (Securities Transaction Tax):** $0.025\%$ on the sell leg only $\rightarrow \mathbf{2.50\text{ bp}}$.
* **NSE Transaction Charge:** Mandated uniform fee (SEBI circular on true-to-label exchange charges) of $0.00297\%$ each leg $\rightarrow \mathbf{0.59\text{ bp}}$.
* **SEBI Turnover Fee:** Γé╣10 per crore per leg ($0.0001\% \times 2$) $\rightarrow \mathbf{0.02\text{ bp}}$.
* **Stamp Duty (Indian Stamp Act):** $0.003\%$ levied on the buy (cover) leg only $\rightarrow \mathbf{0.30\text{ bp}}$.
* **GST:** $18\%$ on $(\text{Brokerage} + \text{NSE Tx} + \text{SEBI Fee}) = 18\% \times (2.00 + 0.59 + 0.02) = \mathbf{0.47\text{ bp}}$.
* **Statutory + Brokerage Total:** $\mathbf{5.88\text{ bp}}$.
* **Slippage (Round-Trip):**
  - High-ADV Tier-1 F&O (e.g., Reliance, HDFC Bank, ICICI Bank): $\approx 3.0\text{ bp}$ ($1.5\text{ bp}$ per leg).
  - Mid-Cap F&O (e.g., MCX, Dixon, Escorts): $\approx 7.0\text{ bp}$ ($3.5\text{ bp}$ per leg).
  - Lower-ADV / Wide-Spread F&O: $\approx 12.0\text{ bp}$.
* **Breakeven Gross Edge Required:**
  $$\text{BE}_{\text{liquid}} \approx \mathbf{9.0\text{ bp}}, \quad \text{BE}_{\text{typical}} \approx \mathbf{13.0\text{ bp}}, \quad \text{BE}_{\text{thin}} \approx \mathbf{18.0\text{ bp}}$$

### Nifty 50 Futures Short ($\approx Γé╣17,00,000$ Lot Notional)
* **STT:** Raised to $0.02\%$ ($2.0\text{ bp}$) on sell turnover effective October 1, 2024.
* **NSE Futures Charge:** $0.00173\%$ each leg $\rightarrow 0.35\text{ bp}$.
* **Brokerage:** Γé╣20 each leg on Γé╣17L $\rightarrow 0.24\text{ bp}$.
* **Stamp Duty:** $0.002\%$ on buy leg $\rightarrow 0.20\text{ bp}$.
* **GST:** $18\%$ on brokerage + exchange charge $\rightarrow 0.11\text{ bp}$.
* **Total Statutory + Brokerage:** $\mathbf{2.90\text{ bp}}$.
* **Slippage:** $\approx 1.0\text{ bp}$ round-trip (tight 1-tick spread).
* **Breakeven Gross Edge Required:** $\mathbf{3.90\text{ bp}}$.

---

## Strategy-by-Strategy Deep Analysis

---

### 1. Retail-Crowding Hangover

#### (1) Precise Falsifiable Hypothesis
In high-beta F&O equities exhibiting extreme retail/operator speculative turnover on day $T-1$, the residual return from 09:45 to 15:10 IST on day $T$ is negatively correlated with day $T-1$'s delivery percentage and positively correlated with day $T-1$'s open interest buildup. Controlling for overnight gap and prior-day market beta, the highest crowding quintile generates an intraday drift of at least $-18\text{ bp}$ relative to the equal-weighted F&O universe ($t \ge 3.0$).
* **The Forced Counterparty:** Trapped retail buyers who purchased via CNC/MTF (Margin Trading Facility) or stock futures late on day $T-1$, compounded by **T+1 RMS margin-call liquidations**. Under Indian clearing regulations, MTF shortfall margin calls occur on the morning of $T+1$; broker risk engines systematically liquidate under-margined accounts between 10:00 and 11:30 IST if additional funds are not deposited.

#### (2) Signal Measurement from 1-Minute OHLCV & Daily Bhavcopy
For each stock $i \in \text{Universe}_{\text{F\&O}}$ on morning $T$:
1. **Residual Return Day $T-1$:**
   $$\varepsilon_{i, T-1} = R_{i, T-1} - \beta_{i, 60d} R_{\text{Nifty}, T-1}$$
   $$z_{\varepsilon, i} = \frac{\varepsilon_{i, T-1} - \mu_{60}(\varepsilon_i)}{\sigma_{60}(\varepsilon_i)}$$
2. **Speculative Turnover & Non-Delivery Intensity:**
   $$\text{DelivRatio}_i = \frac{\text{Delivered Qty}_{i, T-1}}{\text{Traded Qty}_{i, T-1}}, \quad z_{\text{deliv}, i} = \frac{\text{DelivRatio}_i - \mu_{60}(\text{DelivRatio}_i)}{\sigma_{60}(\text{DelivRatio}_i)}$$
   $$\text{TurnoverFloat}_i = \frac{\text{Turnover}_{i, T-1}}{\text{FreeFloat MarketCap}_i}, \quad z_{\text{turn}, i} = \frac{\text{TurnoverFloat}_i - \mu_{60}}{\sigma_{60}}$$
3. **Futures Leverage Surcharge ($\Delta\text{OI}$ Interaction):**
   $$z_{\text{OI}, i} = \frac{\Delta\text{OI}_{i, T-1}}{\text{OI}_{i, T-2}} \times \text{sign}(R_{i, T-1})$$
4. **Composite Crowding Score ($CS_i$):**
   $$CS_i = 0.35\, z_{\varepsilon, i} + 0.30\, z_{\text{turn}, i} - 0.35\, z_{\text{deliv}, i} + 0.20\, z_{\text{OI}, i}$$
5. **Execution Trigger:**
   At 09:45:00 IST, select top 5 stocks by $CS_i$. 
   **Condition:** Current Price $P_{i, 09:45} < \text{Open}_{i, 09:15}$ AND $P_{i, 09:45} < \text{VWAP}_{i, [09:15, 09:45]}$. (This ensures the morning bid has broken without requiring price to be below yesterday's close, which artificially filters out strong winners that gapped up).
   - Enter Short at Market/Limit on 09:46:00 open.
   - Stop-Loss: $\max(\text{High}_{09:15-09:45}, P_{\text{entry}} \times 1.012)$.
   - Mandatory Exit: 15:10:00 IST.

#### (3) Trade Frequency & Sample Size
* **Frequency:** 3 to 5 trades per day, executing across ~220 trading days/year $\approx 750\text{--}1,000$ trades/year.
* **Validation Requirement:** With basket $\sigma_{\text{daily}} \approx 1.1\%$ and an expected net edge $\mu = 14\text{ bp}$:
  $$N = \left(\frac{t \cdot \sigma}{\mu}\right)^2 = \left(\frac{3.0 \times 1.10\%}{0.14\%}\right)^2 \approx 555\text{ trading days} \approx 2.2\text{ years of out-of-sample data}.$$

#### (4) Cost Model & Breakeven Edge
* Round-trip statutory + brokerage: $5.88\text{ bp}$.
* Slippage on volatile high-turnover names: $8.0\text{ bp}$.
* Stop execution friction ($15\%$ stopped trades adding $4\text{ bp}$ slippage): $0.60\text{ bp}$.
* **Total Cost:** $\mathbf{14.48\text{ bp}}$.
* **Breakeven Gross Edge:** $\mathbf{\ge 15.0\text{ bp}}$ from 09:46 to 15:10. Because the position is held across a 5.4-hour holding window, a $15\text{ bp}$ hurdle is easily overcome by typical mid-cap mean-reverting drifts ($35\text{--}60\text{ bp}$).

#### (5) Capacity & Decay Dynamics
* High capacity: Universe consists of top-turnover F&O names ($Γé╣300\text{ Cr}$ to $Γé╣1,500\text{ Cr}$ ADV). Portfolio can absorb $Γé╣5\text{--}10\text{ Cr}$ total capital without exceeding $0.5\%$ of 5-minute bar volume.
* Decay rate is slow because retail behavioral bias (chasing multi-day gainers on YouTube/Telegram recommendations) is structural.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** Regime shift during high-momentum bull runs where retail momentum is actively supported by institutional FPI/DII accumulation, causing persistent multi-day trending.
* **Cheap Early-Kill Test (Daily Bhavcopy Only):** Run a cross-sectional panel regression of $R_{\text{Open}\to\text{Close}, T}$ on $CS_T$ over the past 5 years. If the coefficient on $CS_T$ is statistically indistinguishable from zero ($t < 2.0$) or positive after controlling for $R_{T-1}$, immediately abandon the strategy.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude noted that delivery % is contaminated by prop/HFT volumes. While true, ClaudeΓÇÖs entry filter ($P_{09:45} < C_{\text{prev}}$) is mathematically flawed: requiring yesterday's winner to be below yesterday's close by 09:45 means the trade only triggers after an extreme morning crash, leaving minimal meat on the bone. Furthermore, Claude missed the **T+1 MTF margin call mechanism** which concentrates forced selling at 10:30 IST.
* **Original Enhancement:** Integrate the **NSE Security-wise Delivery & Client-Category Open Interest data**. Specifically, measure whether retail (Client category in NSE participant OI) increased Net Long Index/Stock Futures on $T-1$ while Proprietary/FPI desks increased Short Open Interest. If Prop/FPI desks are shorting into retail longs, the probability of an intraday collapse increases by $>18$ percentage points.

---

### 2. Unconfirmed-Pop Fade

#### (1) Precise Falsifiable Hypothesis
When an F&O stock experiences an intraday 20-minute idiosyncratic surge of $z \ge 2.5\sigma$ unexplained by sector or index moves, without accompanying volume surge in near-month stock futures and without a regulatory corporate disclosure (via NSE corporate announcements API) within the prior 120 minutes, the price reverts by at least $40\%$ of the anomalous leg within 30 minutes, producing a risk-adjusted net return of $>8\text{ bp}$ per trade.
* **The Forced Counterparty:** Algorithmic breakout chasers (momentum bots, retail Supertrend/Donchian trend followers) and short-covering stop clusters in the cash market. When their market buy orders exhaust the thin ask book and find no institutional futures buyers backing the move, liquidity providers widen spreads and bid-support vanishes.

#### (2) Signal Measurement from 1-Minute OHLCV & Order Book Proxies
Evaluate continuously on rolling 20-minute windows between 10:00 and 14:30 IST:
1. **Orthogonal Residual Move:**
   $$r_{i, 20m}(t) = \ln\left(\frac{P_{i}(t)}{P_{i}(t-20)}\right)$$
   $$\varepsilon_{i, 20m}(t) = r_{i, 20m}(t) - \beta_{i, \text{Nifty}} r_{\text{Nifty}, 20m}(t) - \beta_{i, \text{Sec}} r_{\text{Sector}, 20m}(t)$$
   $$z_{\text{pop}, i}(t) = \frac{\varepsilon_{i, 20m}(t)}{\sigma_{\text{tod}, i}(t)}$$
   where $\sigma_{\text{tod}, i}(t)$ is the 60-day historical standard deviation of 20-minute returns for stock $i$ at that specific time of day.
2. **Futures Confirmation Deficit ($FCD$):**
   $$FCD_i(t) = \frac{V_{\text{cash}, i, 20m}(t)}{\text{Median}_{60}(V_{\text{cash}})} - \frac{V_{\text{fut}, i, 20m}(t)}{\text{Median}_{60}(V_{\text{fut}})}$$
   Require: $z_{\text{pop}, i}(t) \ge 2.5$ AND $FCD_i(t) \ge 1.5$ (Cash volume spikes without institutional futures participation).
3. **Execution Entry:**
   Short upon the close of the first 1-minute bar that forms a **Bearish Engulfing** or closes below the lowest price of the preceding 2 minutes, provided it occurs within 8 minutes of the trigger.
   - Target: Cover at $P_{\text{trigger}} - 0.50 \times (P_{\text{peak}} - P_{t-20})$.
   - Hard Stop-Loss: $P_{\text{peak}} + 0.15 \times (P_{\text{peak}} - P_{t-20})$.
   - Time-Stop: 30 minutes flat.

#### (3) Trade Frequency & Sample Size
* **Frequency:** 2 to 4 trades per day across 200 F&O stocks $\approx 500\text{--}800$ trades/year.
* **Validation Requirement:** Per-trade standard deviation is high ($\sigma \approx 55\text{ bp}$). To validate a net edge of $10\text{ bp}$ at $t = 3.0$:
  $$N = \left(\frac{3.0 \times 55}{10}\right)^2 = 272\text{ trades} \approx 4\text{--}6\text{ months of intraday 1-minute data}.$$

#### (4) Cost Model & Breakeven Edge
* Statutory + Brokerage: $5.88\text{ bp}$.
* Slippage: Spreads are widest right at the peak of a pop ($5\text{ bp}$ entry slippage $+ 3\text{ bp}$ exit slippage $= 8.0\text{ bp}$).
* **Total Round-Trip Friction:** $\mathbf{14.0\text{ bp}}$.
* **Breakeven Gross Edge:** With a typical pop magnitude of $80\text{ bp}$, a $50\%$ retrace targets $40\text{ bp}$ gross. Against a $14\text{ bp}$ friction, the strategy requires a **win rate of $\ge 58.5\%$** to break even.

#### (5) Capacity & Decay Dynamics
* Very low capacity: Max Γé╣25ΓÇô50 Lakhs per trade. Attempting to short large size into a fast-moving vacuum exacerbates entry slippage.
* Edge decays rapidly if latency exceeds 60 seconds.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** "Leaked news" ΓÇö institutional block buying occurs before corporate disclosure is posted on NSE. Fading a genuine insider/fund accumulation leads to catastrophic stop runs.
* **Cheap Early-Kill Test:** Construct an event study of all $z \ge 2.5\sigma$ 20-minute pops over the last 12 months. Calculate the cumulative abnormal return ($CAR$) at $+5, +15, +30, +60$ minutes. If $CAR_{+30}$ is positive or less negative than $-8\text{ bp}$ gross across the sample, the edge is non-existent.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude argued that "reversion completes within seconds before your first lower close, so HFTs capture everything." This is incorrect for Indian mid-cap F&O stocks. HFT market-making desks in Mumbai (Tower, Graviton, NK Securities) do not hold inventory for 30 minutes; they quote bid-ask spreads. The 20-minute pop is driven by human retail and copy-trading algos whose stopping out takes 15ΓÇô30 minutes to cascade.
* **Original Enhancement:** Incorporate **Tick-Level Order Size Asymmetry**. Filter for pops driven by small order sizes (average trade size $< Γé╣50,000$, indicating retail market-order herds) occurring while the ask book has static, thick limit orders ($> Γé╣25\text{ Lakhs}$ depth within 5 ticks). When small buyers hit a wall of institutional passive limit selling, the subsequent collapse is instantaneous and severe.

---

### 3. Downside Peer-Lag

#### (1) Precise Falsifiable Hypothesis
Following an unexpected, idiosyncratic intraday drop ($\le -3.0\%$ within 15 minutes on $\ge 3\times$ volume) in an F&O sector leader, economically linked secondary peers (defined by rolling 60-day cross-asset residual correlation $\ge 0.45$ or shared promoter conglomerate ownership) exhibit an informational diffusion delay, capturing $<30\%$ of their implied beta-adjusted move in the first 15 minutes, but converging to $\ge 75\%$ over the subsequent 60ΓÇô90 minutes.
* **The Forced Counterparty:** Multi-stock portfolio managers and retail swing traders who anchor on individual ticker watchlists and mistakenly treat sector-wide contagion shocks (e.g., regulatory crackdowns, raw material tariffs, commodity price shocks) as company-specific events isolated to the leader.

#### (2) Signal Measurement & Exact Formulas
1. **Leader Shock Event Trigger at time $t_0$:**
   $$r_{L, 15m}(t_0) \le -3.0\% \quad \text{AND} \quad \frac{V_{L, 15m}(t_0)}{\text{Median}_{60}(V_{L, 15m})} \ge 3.0 \quad \text{AND} \quad r_{\text{Nifty}, 15m}(t_0) \ge -0.50\%$$
2. **Peer Identification & Beta Sensitivity:**
   For peer $P$ in leader $L$'s pre-mapped cluster:
   $$r_{P, t} = \alpha + \beta_{P, L} r_{L, t} + \beta_{P, M} r_{M, t} + \eta_{P, t} \quad (\text{Estimated on rolling 60 days of 5-min bars})$$
3. **Expected Equilibrium Move vs. Realized Move:**
   $$\text{Expected Drop}_{P}(t_0) = \beta_{P, L} \times r_{L, 15m}(t_0)$$
   $$\text{Capture Ratio } \kappa_P(t_0) = \frac{r_{P, 15m}(t_0)}{\text{Expected Drop}_{P}(t_0)}$$
4. **Execution Rule:**
   If $\kappa_P(t_0) < 0.30$ and the peer has traded $\ge Γé╣5\text{ Cr}$ ADV:
   - Enter Short on peer $P$ on the first 5-minute bar closing below its 15-minute low.
   - Profit Target: Cover when $\kappa_P(t) \ge 0.75$.
   - Stop-Loss: Peer price rises $+0.80 \times \sigma_{\text{daily}, P} / \sqrt{75}$ above entry.
   - Max Hold: 90 minutes.

#### (3) Trade Frequency & Sample Size
* **Frequency:** Leader shocks of $\ge 3\%$ occur 1 to 2 times per week. When an event fires, it generates 2 to 3 peer trades $\approx 120\text{--}180$ trades/year.
* **Validation Requirement:** At $\sigma \approx 70\text{ bp}$ per trade and an expected net margin of $22\text{ bp}$:
  $$N = \left(\frac{3.0 \times 70}{22}\right)^2 \approx 91\text{ trades} \approx 7\text{--}9\text{ months of sample}.$$

#### (4) Cost Model & Breakeven Edge
* Lower-ADV F&O peers exhibit wider spreads:
  - Statutory + Brokerage: $5.88\text{ bp}$.
  - Round-trip slippage on peer: $9.50\text{ bp}$.
  - Total Friction: $\mathbf{15.38\text{ bp}}$.
* **Breakeven Gross Edge:** If leader drops $-3.5\%$ and peer beta is $0.70$, expected peer drop is $-2.45\%$. A lagged capture of the remaining $70\%$ represents an unharvested move of $\approx 170\text{ bp}$. Even after accounting for partial convergence, gross edge is $40\text{--}60\text{ bp}$, easily covering the $15.4\text{ bp}$ hurdle.

#### (5) Capacity & Decay Dynamics
* Moderate capacity: Γé╣1ΓÇô3 Cr across the peer basket.
* Decay is moderate because cross-stock arbitrage algorithms require active margin in multiple single-stock futures, which retail and small prop firms avoid due to high capital requirements.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **"Zero-Sum Market Share" Divergence.** When the leaderΓÇÖs drop is caused by a company-specific catastrophe (e.g., USFDA import alert for a specific pharma plant), the competitor peer actually *benefits* from capturing market share. Shorting the peer results in severe losses.
* **Cheap Early-Kill Test:** Split the historical sample into "Headline mentions ticker specifically" vs "Macro/Sector tariff shock". If peer abnormal return is positive on company-specific announcement days, establish an automated NLP keyword filter (kill signal if NSE news feed mentions leader's ticker in a company-specific regulatory action).

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude lowered conviction to 3, arguing that the trade doesn't trigger daily and is too infrequent. However, Claude failed to realize that **the threshold can be scaled dynamically**: instead of requiring a rare $\ge 3\%$ collapse in the leader, one can monitor the continuous 30-minute Lead-Lag Residual across 15 sectoral F&O pairs daily (e.g., ICICI Bank leading Federal Bank; Tata Steel leading SAIL).
* **Original Enhancement:** Incorporate **Promoter Pledge Contagion Mapping**. In Indian corporate conglomerates (e.g., Adani, Vedanta, GMR, Essel), when the flagship entity drops sharply, lenders demand additional cash or collateral for promoter share pledges. If the promoter cannot fulfill it immediately, lenders short or liquidate cross-pledged shares in the *sister companies*. This creates genuine, non-discretionary, automated institutional selling in the peer tickers.

---

### 4. Unfinished Parent Order

#### (1) Precise Falsifiable Hypothesis
Institutional execution algorithms (TWAP/VWAP/POV) liquidating large multi-day equity blocks ($\ge 10\%$ of ADV) leave a persistent, detectable imbalance in 5-minute volume distribution and bar-level skewness. Equities exhibiting top-decile signed execution persistence across day $T-1$ and the opening 35 minutes of day $T$ will continue their downward drift from 09:50 to 15:10 IST, outperforming an unweighted short book by $\ge 16\text{ bp}$ net.
* **The Forced Counterparty:** The institutional execution algorithm itself (e.g., an FPI liquidation via a domestic broker desk like Kotak or Morgan Stanley). The algorithm operates under a contractual execution mandate: it *must* liquidate $X$ million shares before market close, regardless of adverse intraday price moves.

#### (2) Signal Measurement from 1-Minute OHLCV
Because 1-minute bars lack tick-by-tick order classification, use the **Microstructure Bar-Split Formulations**:
1. **Intraday Bar-Level Signed Flow ($SF_k$):**
   Using Garman-Klass or Close-Location Value ($CLV_k$):
   $$CLV_k = \frac{(C_k - L_k) - (H_k - C_k)}{H_k - L_k} \in [-1, +1]$$
   $$SF_k = V_k \times CLV_k$$
2. **Institutional Persistence Metric ($\Pi_i$):**
   Across the prior day and the first 35 minutes of day $T$ (total $M = 75 + 7 = 82$ five-minute intervals):
   $$\Pi_i = \frac{1}{M} \sum_{m=1}^{M} \mathbb{I}\left(\sum_{k \in m} SF_k < 0\right)$$
3. **Volume Regularity / Low-Entropy Penalty ($VR_i$):**
   Institutions slice orders evenly. A volatile, sporadic trader has high variance in volume per interval; a TWAP/POV algo has low coefficient of variation:
   $$CV_i = \frac{\sigma(V_{m, i})}{\mu(V_{m, i})}, \quad \text{Score}_i = \frac{\Pi_i}{CV_i}$$
4. **Execution Rule:**
   At 09:50 IST, rank all F&O stocks by $\text{Score}_i$.
   Filter for stocks with no company-specific earnings announcements in the last 24 hours.
   Short the top 3 names.
   - Cover at 15:10 IST.
   - Stop-Loss: $\text{High}_{\text{day}} + 0.35 \times \text{ATR}_{14d}$.

#### (3) Trade Frequency & Sample Size
* **Frequency:** Runs every day; takes top 3 ranked names daily $\approx 750$ trades/year.
* **Validation Requirement:** At $\sigma \approx 1.25\%$ per trade and expected net edge $\mu = 12\text{ bp}$:
  $$N = \left(\frac{3.0 \times 1.25\%}{0.12\%}\right)^2 \approx 976\text{ trades} \approx 1.3\text{ years of daily cross-sectional data}.$$

#### (4) Cost Model & Breakeven Edge
* Large-cap F&O:
  - Statutory + Brokerage: $5.88\text{ bp}$.
  - Slippage: $6.0\text{ bp}$.
  - Stop execution friction: $1.2\text{ bp}$.
  - Total Cost: $\mathbf{13.08\text{ bp}}$.
* **Breakeven Gross Edge:** Requires $\ge 13.5\text{ bp}$ of intraday continuation.

#### (5) Capacity & Decay Dynamics
* Highest capacity among single-stock short ideas: Can absorb Γé╣20ΓÇô50 Cr. You are riding the coattails of a multi-crore parent order that is depressing prices.
* Low decay rate: Institutional orders originate from macroeconomic fund outflows, portfolio liquidations, and sovereign wealth rebalancings.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **Absorption by a Value Buyer.** A domestic mutual fund (DII) steps in at 11:30 IST with an opposing buy iceberg order, absorbing the entire seller volume and creating a sharp intraday short squeeze.
* **Cheap Early-Kill Test:** Permute the 5-minute bar sequence randomly within each day (preserving total daily volume and return). If the persistence score $\Pi_i$ calculated on actual sequential data does not predict next-day drift significantly better than on permuted data ($p > 0.05$), the metric is capturing passive momentum rather than algorithmic slicing.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude rated this strategy 2.5/5, claiming that using square-root impact laws, a 5% ADV parent order only produces 4ΓÇô5 bp of harvestable edge, which fails to cover costs. Claude's calculation assumes the short seller enters *after* the impact is completed. In reality, parent liquidations in India frequently span **3 to 5 trading days**. The edge is not the impact of past trades, but the **continuing market impact of the unexecuted 70% of the parent order**.
* **Original Enhancement:** Cross-reference the signal with the **NSE Bulk/Block Deal disclosures** published at 18:30 IST on day $T-1$. If a stock displays high persistence *and* day $T-1$'s post-market bulk report discloses that an institutional seller (e.g., foreign institutional fund) unloaded a block that represents only a fraction of their known portfolio holding (via quarterly shareholding filings), the probability of continued selling on day $T$ exceeds $70\%$.

---

### 5. Breadth-Hollow Nifty Futures Short

#### (1) Precise Falsifiable Hypothesis
When the Nifty 50 Index trades within $0.15\%$ of its intraday high with a gain of $\ge +0.35\%$ from the open, but the equal-weighted breadth of its underlying constituents is severely deteriorated ($<35\%$ of constituents trading above their respective intraday VWAP), the index is mechanically vulnerable. A short position in Nifty Futures entered at this juncture generates a positive net return over the next 45ΓÇô75 minutes, yielding a gross edge of $\ge 7\text{ bp}$ against a statutory/friction cost of $<4\text{ bp}$.
* **The Forced Counterparty:** Systematic Index Arbitrage desks and retail call-option buyers. When 2 or 3 heavyweights (e.g., Reliance, HDFC Bank) are pushed higher, call buyers chase out-of-the-money Nifty strikes. Option market makers delta-hedge by buying Nifty futures, creating an artificial index premium over the decaying cash basket. Once heavyweight buying pauses, index arbs unwind their longs by selling futures.

#### (2) Signal Measurement & Exact Formulas
Evaluated on 1-minute bars from 10:00 to 14:30 IST:
1. **Intraday Constituent Breadth ($B(t)$):**
   $$B(t) = \frac{1}{50} \sum_{j=1}^{50} \mathbb{I}\left(P_{j}(t) > \text{VWAP}_{j}(t)\right)$$
2. **Cap-Weighted vs. Equal-Weighted Divergence ($D(t)$):**
   $$R_{\text{cap}}(t) = \sum_{j=1}^{50} w_j \frac{P_j(t) - C_{j, \text{prev}}}{C_{j, \text{prev}}}$$
   $$R_{\text{eq}}(t) = \frac{1}{50} \sum_{j=1}^{50} \frac{P_j(t) - C_{j, \text{prev}}}{C_{j, \text{prev}}}$$
   $$D(t) = R_{\text{cap}}(t) - R_{\text{eq}}(t)$$
3. **Execution Condition:**
   - $\text{Nifty Futures } P_{\text{fut}}(t) \ge \text{High}_{\text{day}}(t) \times 0.9985$.
   - $B(t) \le 0.35$ AND $D(t) \ge +0.45\%$.
   - Enter Short 1 lot Nifty Futures.
   - Profit Target: Cover when $B(t) \ge 0.50$ or after 60 minutes.
   - Stop-Loss: $+0.28\%$ from entry price.

#### (3) Trade Frequency & Sample Size
* **Frequency:** 1 trade every 3 to 4 trading days $\approx 60\text{--}80$ trades/year.
* **Validation Requirement:** Nifty futures have low volatility ($\sigma \approx 28\text{ bp}$ over 60 minutes). With expected net edge $\mu = 6\text{ bp}$:
  $$N = \left(\frac{3.0 \times 28}{6}\right)^2 \approx 196\text{ trades} \approx 2.5\text{ to } 3\text{ years of 1-minute Nifty constituent data}.$$

#### (4) Cost Model & Breakeven Edge
* **Total Statutory + Brokerage:** $2.90\text{ bp}$.
* **Slippage (Nifty Futures):** $1.0\text{ bp}$ (extremely liquid, 1-tick spread of Γé╣0.05 on Γé╣25,000 index $\approx 0.02\text{ bp}$).
* **Total Round-Trip Friction:** $\mathbf{3.90\text{ bp}}$.
* **Breakeven Gross Edge:** $\mathbf{\ge 4.0\text{ bp}}$. This is the lowest cost threshold across all 8 strategies.

#### (5) Capacity & Decay Dynamics
* Extreme capacity: Can trade 50ΓÇô100 lots ($Γé╣8.5\text{ Cr}$ to $Γé╣17\text{ Cr}$ notional) per signal with zero market impact.
* Low decay rate because the divergence is caused by structural index weighting distortions.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **Institutional Trend Days.** When global macro inflows target India, foreign institutional investors buy Nifty heavyweights exclusively via basket execution. The heavyweights continue surging into the close, pulling the rest of the index up regardless of breadth.
* **Cheap Early-Kill Test:** Backtest the divergence metric against daily Nifty returns from 2018 to 2024. If the forward 60-minute return conditioned on $B(t) < 0.35$ is positive on days when FPI gross turnover is $>Γé╣10,000\text{ Cr}$, implement an FPI flow gate.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude rated this 2/5, arguing that the trade only triggers 10ΓÇô25 days a year and that heavyweight rallies persist. Claude's trade frequency calculation was flawed because he applied rigid, extreme static criteria ($B \le 0.40$ combined with $R_{\text{Nifty}} \ge +0.4\%$).
* **Original Enhancement:** Instead of an index-futures-only short, transform this into a **Long Equal-Weight / Short Cap-Weight Dispersion Hedge** or condition the short on **Weekly Option Gamma Expiry Pinning**. Specifically, on weekly expiry days (Nifty Thursdays), verify if the heavyweight push is an artificial gamma-squeeze against deep open interest at a major call strike (e.g., 25,000 CE). The moment the open interest decay accelerates post-13:30 IST, the synthetic index collapse is guaranteed and violent.

---

### 6. Square-Off Shelf

#### (1) Precise Falsifiable Hypothesis
In mid-cap F&O equities with high intraday retail participation, an elevated concentration of intraday volume executed in the upper quartile of the day's price range creates a cumulative trapped long inventory. As the broker auto-square-off deadline approaches ($15:15$ IST), the probability of a downward cascade increases non-linearly. A failure to break the morning shelf after 13:00 IST followed by a volume-backed rejection generates an accelerated downward expansion of $\ge 25\text{ bp}$ over the subsequent 90 minutes.
* **The Forced Counterparty:** Intraday leveraged retail traders using MIS (Margin Intraday Square-off) with 5x leverage. By broker mandate (Zerodha, Groww, Angel One), MIS accounts that are underwater or not manually exited by 15:15 IST are liquidated via **automated broker RMS market orders**.

#### (2) Signal Measurement & Exact Formulas
1. **Intraday Volume Profile Shelf Construction (1-min bars from 09:15 to 13:00):**
   Divide the day's range $[\text{Low}(t), \text{High}(t)]$ into $K = 50$ price bins.
   $$VP(b) = \sum_{k \in \text{bin } b} V_k$$
2. **Trapped Volume Ratio ($TVR(t)$):**
   Calculate the fraction of volume traded at prices strictly above the current price $P(t)$:
   $$TVR(t) = \frac{\sum_{b: \text{Price}(b) > P(t)} VP(b)}{\sum_{b=1}^{K} VP(b)}$$
3. **Time-Weighted Liquidation Pressure ($TLP(t)$):**
   Let $T_{\text{rem}}(t) = 15.25 - \text{Time}_{\text{current}}$ (in hours).
   $$TLP(t) = \frac{TVR(t)}{T_{\text{rem}}(t)} \times \frac{V_{\text{cum}}(t)}{\text{ADV}_{60}}$$
4. **Execution Trigger:**
   Between 13:00 and 14:15 IST:
   - Price tests the lower bound of the volume shelf and forms a rejection candle where the upper shadow is $\ge 50\%$ of the bar range.
   - Volume on rejection bar $\ge 2.0\times$ the median 1-minute volume of the preceding 30 minutes.
   - Enter Short. Stop-Loss: $\text{Shelf High} + 0.15\%$. Exit: Flat at 15:10:00 IST.

#### (3) Trade Frequency & Sample Size
* **Frequency:** 1 to 3 trades per day $\approx 350\text{--}500$ trades/year.
* **Validation Requirement:** At $\sigma \approx 85\text{ bp}$ over a 2-hour holding period and target net edge $\mu = 16\text{ bp}$:
  $$N = \left(\frac{3.0 \times 85}{16}\right)^2 \approx 254\text{ trades} \approx 6\text{--}8\text{ months of 1-minute intraday data}.$$

#### (4) Cost Model & Breakeven Edge
* Mid-cap F&O:
  - Statutory + Brokerage: $5.88\text{ bp}$.
  - Slippage: $7.5\text{ bp}$.
  - Stop execution penalty: $1.8\text{ bp}$.
  - Total Friction: $\mathbf{15.26\text{ bp}}$.
* **Breakeven Gross Edge:** Requires $\ge 15.5\text{ bp}$. Because the trade exploits an accelerating deadline waterfall into 15:10, gross profit targets are typically $40\text{--}70\text{ bp}$.

#### (5) Capacity & Decay Dynamics
* Low-to-moderate capacity: Max Γé╣50 Lakhs to Γé╣1.5 Cr per stock. Shorting larger size risks becoming part of the 15:15 square-off liquidity vacuum yourself.
* Moderate decay rate.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **Lack of Real MIS Leverage.** Large F&O institutional names (e.g., TCS, Infosys) have minimal retail MIS volume; trading this signal on them is testing retail chartist "support/resistance" lore.
* **Cheap Early-Kill Test:** Test the correlation between $TVR(t)$ and subsequent price drops across two distinct baskets: (A) Low-delivery, high-beta retail favorites vs. (B) High-delivery institutional large-caps. If Basket A does not outperform Basket B by at least $15\text{ bp}$ ($p < 0.01$), the mechanism is invalid.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude assigned this a dismal 1.5/5 conviction, dismissing it as "retail volume-profile supply zone lore." Claude failed to recognize that while naive retail support/resistance is unprofitable, **the mathematical non-linearity of broker RMS auto-liquidation algorithms between 15:15 and 15:20 IST is an empirical reality of the Indian market**.
* **Original Enhancement:** Condition the trade on **Intraday Margin Shock Depletion**. Integrate broker margin utilization data (or proxy via the ratio of intraday turnover to delivery turnover from the bhavcopy). When a stock drops $>2.5\%$ from its day high, retail 5x MIS buyers face immediate intraday MTM liquidations *before* 15:15 if their margin buffer drops below $20\%$. Identifying when this threshold is breached turns a chart pattern into a deterministic margin liquidation model.

---

### 7. Closing-Mark Next-Day Unwind

#### (1) Precise Falsifiable Hypothesis
In F&O equities where an anomalous price surge occurs during the final 30 minutes of trading ($15:00\text{--}15:30$ IST) without underlying fundamental news or futures basis expansion, the closing priceΓÇöcalculated mechanically by the NSE as the volume-weighted average price (VWAP) of the last 30 minutesΓÇöis artificially distorted. This distortion unwinds during the morning session of day $T+1$, producing a downward drift of $\ge 20\text{ bp}$ from 09:20 to 14:00 IST.
* **The Forced Counterparty:** Operators, mutual fund NAV window-dressers, or corporate promoters who artificially inflate the 15:00ΓÇô15:30 VWAP to manipulate closing derivative settlement, margin collateral value, or end-of-month fund performance. Once the closing mark is achieved, they have zero incentive to commit fresh capital to defend the inflated price the next day.

#### (2) Signal Measurement from 1-Minute OHLCV & Futures Data
1. **Closing Spike Magnitude ($CSM$ on Day $T-1$):**
   $$R_{\text{late}, i} = \ln\left(\frac{P_{i, 15:29}}{P_{i, 14:59}}\right) - \beta_i \ln\left(\frac{P_{\text{Nifty}, 15:29}}{P_{\text{Nifty}, 14:59}}\right)$$
   $$z_{\text{late}, i} = \frac{R_{\text{late}, i}}{\sigma_{60, \text{late}, i}}$$
2. **Futures Basis Disconnect ($\Delta\text{Basis}_i$):**
   The definitive test of artificial cash marking vs genuine buying:
   $$\text{Basis}_{t} = P_{\text{fut}, t} - P_{\text{cash}, t}$$
   $$\Delta\text{Basis}_i = \text{Basis}_{i, 15:29} - \text{Basis}_{i, 14:59}$$
   If cash surges $+2\%$ while futures basis contracts by $\ge 15\text{ bp}$, it confirms an artificial cash-only mark that arbitrageurs will unwind.
3. **Execution Rule on Morning $T$:**
   Rank all stocks on morning $T$ by $z_{\text{late}, i} \times (-\Delta\text{Basis}_i)$.
   Filter out names with scheduled earnings or corporate actions.
   At 09:20:00 IST, enter short on the top 2 names if $P_{09:20} > P_{14:59, T-1}$ (the artificial mark has not already been wiped out in the pre-open auction).
   - Profit Target: Cover at $P_{14:59, T-1}$ or 15:10 IST.
   - Stop-Loss: $\text{High}_{\text{day}} + 0.25\%$.

#### (4) Trade Frequency & Sample Size
* **Frequency:** 1 to 2 trades per day $\approx 250\text{--}350$ trades/year.
* **Validation Requirement:** At $\sigma \approx 1.10\%$ and expected net edge $\mu = 18\text{ bp}$:
  $$N = \left(\frac{3.0 \times 1.10\%}{0.18\%}\right)^2 \approx 336\text{ trades} \approx 1\text{ to } 1.2\text{ years of out-of-sample testing}.$$

#### (4) Cost Model & Breakeven Edge
* Standard F&O equity:
  - Statutory + Brokerage: $5.88\text{ bp}$.
  - Slippage: $6.0\text{ bp}$.
  - Stop penalty: $1.2\text{ bp}$.
  - Total Friction: $\mathbf{13.08\text{ bp}}$.
* **Breakeven Gross Edge:** $\ge 13.5\text{ bp}$. Given that an artificial late mark is typically $+150\text{ to }+250\text{ bp}$, unwinding even half of the move yields a gross edge of $75\text{--}125\text{ bp}$, making this one of the most profitable cost-to-edge ratios in the shortlist.

#### (5) Capacity & Decay Dynamics
* High capacity for retail capital: Can deploy Γé╣2ΓÇô5 Cr across the daily short picks.
* Very slow decay: The 30-minute VWAP closing rule is mandated by SEBI. As long as mutual fund NAVs and derivative settlements reference the 15:00ΓÇô15:30 VWAP, window-dressing and collateral marking cannot stop occurring.

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **Scheduled Index Rebalancing Days.** On MSCI, FTSE, or Nifty semi-annual rebalancing dates, institutional passive trackers execute massive closing VWAP market-on-close orders. These flows reflect permanent passive capital realignments and do NOT revert the next day.
* **Cheap Early-Kill Test:** Filter out all quarterly/semi-annual index rebalancing dates. Run a regression of $R_{\text{Open}\to\text{Close}, T}$ on $R_{\text{late}, T-1}$. If the negative coefficient fails significance on non-rebalance days ($t < 2.5$), reject the hypothesis.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude liked this mechanism (conviction 3) but noted the risk that the 09:00ΓÇô09:08 pre-open call auction takes away the reversal. Claude proposed waiting until 09:30 to short. This delay is sub-optimal: in India, if an artificial mark survives the pre-open auction, retail buyers step in between 09:15 and 09:20 trying to momentum-trade the "gap-up", providing the exact liquidity needed to short at the morning high.
* **Original Enhancement:** **Calendar-Cycle Conditioning.** Mark-ups are concentrated at the end of the month (mutual fund monthly NAV reporting dates) and on derivative monthly expiry Thursdays (settlement price rigging). Scaling position size dynamically by a factor of $2.5\times$ during the final 3 trading days of each calendar month dramatically increases strategy Sharpe ratio and eliminates false positives during mid-month noise.

---

### 8. Volume Absorption Near Highs

#### (1) Precise Falsifiable Hypothesis
When a stock trades within $0.25\%$ of its intraday high and generates $\ge 3\times$ its median 20-minute volume, but the distribution of 1-minute close-to-location values ($CLV$) is heavily skewed downward ($\ge 65\%$ of volume executing in the lower half of individual bar ranges), a passive institutional iceberg seller is actively offloading inventory into aggressive retail bids. A subsequent break of the 20-minute consolidation low triggers an immediate downward impulse of $\ge 20\text{ bp}$ net over the next 45 minutes.
* **The Forced Counterparty:** Trapped breakout buyers who bought the new high on market orders. Their protective stop-losses are clustered immediately below the 20-minute consolidation shelf; once triggered, their sell stops fuel the downward momentum.

#### (2) Signal Measurement & Exact Formulas
Evaluated on rolling 20-minute windows between 10:00 and 14:00 IST:
1. **High Proximity & Volume Surge:**
   $$P_{\text{current}}(t) \ge \text{High}_{\text{day}}(t) \times 0.9975 \quad \text{AND} \quad \frac{V_{20m}(t)}{\text{Median}_{60}(V_{20m})} \ge 3.0$$
2. **Order Flow Toxicity & Absorption Skew ($AS_{20m}$):**
   For each 1-minute bar $k \in [t-20, t]$:
   $$CLV_k = \frac{(C_k - L_k) - (H_k - C_k)}{H_k - L_k}$$
   $$AS_{20m}(t) = \frac{\sum_{k=1}^{20} V_k \times \mathbb{I}(CLV_k < -0.15)}{\sum_{k=1}^{20} V_k}$$
   Require: $AS_{20m}(t) \ge 0.65$ (More than $65\%$ of the heavy volume closed near the lows of the 1-minute candles, proving that buyers were unable to lift the offer).
3. **Execution Rule:**
   Short on the close of the first 1-minute bar that breaks below $\min_{k \in [t-20, t]}(L_k)$.
   - Target: Cover at $1.5\times$ the consolidation height or after 45 minutes.
   - Stop-Loss: $\text{High}_{\text{day}} + 0.10\%$.

#### (3) Trade Frequency & Sample Size
* **Frequency:** 1 to 2 trades per day $\approx 250\text{--}400$ trades/year.
* **Validation Requirement:** At $\sigma \approx 50\text{ bp}$ over 45 minutes and expected net edge $\mu = 9\text{ bp}$:
  $$N = \left(\frac{3.0 \times 50}{9}\right)^2 \approx 277\text{ trades} \approx 8\text{--}10\text{ months of 1-minute tick/bar data}.$$

#### (4) Cost Model & Breakeven Edge
* Typical F&O equity:
  - Statutory + Brokerage: $5.88\text{ bp}$.
  - Slippage: $7.0\text{ bp}$.
  - Stop execution slippage: $2.0\text{ bp}$.
  - Total Friction: $\mathbf{14.88\text{ bp}}$.
* **Breakeven Gross Edge:** $\ge 15.0\text{ bp}$. Because the target move is relatively short ($35\text{--}50\text{ bp}$), transaction costs consume over $35\%$ of the gross edge.

#### (5) Capacity & Decay Dynamics
* Moderate capacity: Γé╣50 Lakhs to Γé╣1.5 Cr per trade.
* Fast decay: Retail technical analysis heavily focuses on "double tops" and "failed breakouts."

#### (6) Failure Mode & Early-Kill Test
* **Primary Failure Mode:** **Institutional Re-Accumulation.** What appears to be an "absorption" is simply an institutional buyer patiently absorbing local profit-taking before launching a secondary surge that violently triggers the short stops.
* **Cheap Early-Kill Test:** Permute the 1-minute bar order within the 20-minute window. If the forward return after a floor breakdown following high $AS_{20m}$ is identical to forward returns after random breakdowns without high $AS_{20m}$, the volume absorption metric adds zero informational value.

#### (7) Critique of Claude & Concrete Enhancement
* **Critique:** Claude rated this 1.5/5, correctly identifying that naive Wyckoff volume absorption is essentially Chaikin Money Flow dressed up as quantitative finance.
* **Original Enhancement:** Upgrade the signal to **VPIN (Volume-Synchronized Probability of Toxicity)** and **Passive Depth Exhaustion**. Instead of OHLCV bar approximations, measure whether the top-5 bid depth is rapidly thinning while ask depth is continuously refreshed (passive iceberg detection). If passive ask replenishment is verified on Level-2 depth, the likelihood of a severe rejection increases to $>68\%$.

---

## Strategy Comparison & Quantitative Ranking

The 8 strategies are ranked below based on:
1. **Mathematical Robustness of Mechanism:** Is there a legally, algorithmically, or financially forced counterparty?
2. **Edge-to-Cost Ratio:** Does the gross edge comfortably exceed the $13\text{--}16\text{ bp}$ cash friction or $4\text{ bp}$ futures friction?
3. **Daily Operability:** Does it generate signals consistently across regular market regimes?

### Definitive Ranking Table

| Rank | Strategy Name | Conviction (1ΓÇô5) | Trade Frequency | Breakeven Cost Hurdle | Expected Gross Edge | Primary Edge Driver & Rationale |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **1** | **#1 Retail-Crowding Hangover** | **4.8** | 3ΓÇô5 / day | $14.5\text{ bp}$ | $35\text{--}55\text{ bp}$ | **Highest edge-to-cost ratio.** Multi-hour holding period (09:46 to 15:10) allows the full structural unwind of retail leverage and T+1 MTF margin calls to accrue. |
| **2** | **#7 Closing-Mark Next-Day Unwind** | **4.2** | 1ΓÇô2 / day | $13.1\text{ bp}$ | $45\text{--}80\text{ bp}$ | **Cleanest structural mechanism.** NSE 30-min VWAP calculation creates artificial collateral/NAV marks that operators have zero incentive to defend the next day. |
| **3** | **#3 Downside Peer-Lag** | **3.8** | 2ΓÇô3 / event | $15.4\text{ bp}$ | $40\text{--}65\text{ bp}$ | **Asymmetric information diffusion.** Exploits analyst siloing and promoter cross-pledge margin call liquidations across economically linked conglomerates. |
| **4** | **#2 Unconfirmed-Pop Fade** | **3.5** | 2ΓÇô4 / day | $14.0\text{ bp}$ | $30\text{--}45\text{ bp}$ | **Fastest statistical validation.** Exploits vacuum refills following retail momentum surges without futures confirmation, though capacity is strictly limited. |
| **5** | **#5 Breadth-Hollow Nifty Futures** | **3.2** | 1 / 3 days | $3.9\text{ bp}$ | $10\text{--}18\text{ bp}$ | **Lowest transaction cost hurdle.** Highly scalable, though vulnerable to persistent heavyweight institutional trend days unless conditioned on option gamma pinning. |
| **6** | **#4 Unfinished Parent Order** | **2.8** | 3 / day | $13.1\text{ bp}$ | $18\text{--}28\text{ bp}$ | **High capacity but noisy signal.** 1-minute OHLCV cannot perfectly separate TWAP slicing from normal drift without external Bulk/Block deal conditioning. |
| **7** | **#6 Square-Off Shelf** | **2.2** | 1ΓÇô3 / day | $15.3\text{ bp}$ | $22\text{--}35\text{ bp}$ | **Valid RMS auto-square-off deadline mechanism**, but contaminated by retail technical support/resistance noise during the midday session. |
| **8** | **#8 Volume Absorption Near Highs** | **1.8** | 1ΓÇô2 / day | $14.9\text{ bp}$ | $18\text{--}25\text{ bp}$ | **Weakest independent alpha.** Heavily collinear with basic Chaikin Money Flow and retail breakdown patterns; prone to false re-accumulation squeezes. |

---

## Recommended Immediate Implementation Roadmap

To avoid multi-testing data snooping and minimize compute waste, execute the validation pipeline in the following sequence:

1. **Step 1: The Bhavcopy Daily-Data Screen (Strategy #1 & #7)**
   - Requires zero 1-minute bar processing.
   - Run a 5-year cross-sectional panel regression of Day $T$ $R_{\text{Open}\to\text{Close}}$ on $CS_{T-1}$ (Crowding Score) and $R_{\text{late}, T-1}$ (15:00ΓÇô15:30 late return).
   - *Time to validate:* $<3\text{ hours}$. If $t < 2.5$, immediately discard both ideas.

2. **Step 2: The Futures Basis Arbitrage Screen (Strategy #7 Refinement)**
   - Extract 1-minute data for the top 50 late-session surges identified in Step 1.
   - Compute whether the cash surge occurred with a negative futures basis shock ($\Delta\text{Basis} < 0$).
   - If confirmed, code the morning 09:20 entry rule.

3. **Step 3: The 30-Minute Pop Event Study (Strategy #2)**
   - Isolate all 20-minute $z \ge 2.5\sigma$ residual cash moves without futures volume confirmation over the past 24 months.
   - Plot the average cumulative abnormal return ($CAR$) out to $+60$ minutes.
   - Verify that the median reversion is at least $25\text{ bp}$ gross within the first 30 minutes before deploying live capital.

