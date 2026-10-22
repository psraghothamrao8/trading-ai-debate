**1. Retail-Crowding Hangover** (C19/C31/C37/C17)
- **Mechanism:** MIS-funded retail and operator churn chases yesterday's winners. Margin products set a hard exit deadline, and the fresh buyers are the same crowd.
- **Entry:** At 09:45, rank F&O names on prior-day gain, volume, low delivery % vs own 60-day history, and turnover/free float. Short the top 3ΓÇô5 that fail to reclaim yesterday's close.
- **Exit/stop:** Cover at 15:10. Stop at day-high.
- **Data:** Bhavcopy delivery %, 1-min.
- **Failure:** The overnight gap may take most of the reversal (test openΓåÆclose only). A real re-rating also breaks it.
- **Known-variant?** Llorente et al. and LouΓÇôPolkΓÇôSkouras; no coded Indian version known.
- **CONVICTION:** Claude 4/5, Gemini 5/5

**2. Unconfirmed-Pop Fade** (C4/C33/C23/G19/G40/G47/G48)
- **Mechanism:** Market-order chasers push a stock out of line with its beta and sector. Liquidity providers who absorb it are paid when it reverts.
- **Entry:** After 45 min, a 20-min move ΓëÑ3╧â vs own time-of-day range, unexplained by beta├ùNifty or the peer basket, with no futures-volume confirmation and no filing in 2 h. Short the first lower 1-min close. Test the volume sign both ways.
- **Exit/stop:** Cover at 50% retrace or after 30 min. Stop above the high.
- **Data:** 1-min cash and futures, filing timestamps.
- **Failure:** Undisclosed news or leaks cause squeezes.
- **Known-variant?** Yes, Nagel and AvellanedaΓÇôLee residual reversal; the futures-absent/peer-absent filter is unverified.
- **CONVICTION:** Claude 4/5, Gemini 4/5

**3. Downside Peer-Lag** (C25/C16/G5/G11/G39)
- **Mechanism:** Analyst and fund coverage is siloed by ticker. Less-covered peers reprice over minutes to hours, while their holders think "only the leader got hit".
- **Entry:** Leader ΓëñΓêÆ3% on >3├ù volume with Nifty > ΓêÆ0.5%. Pick lower-ADV F&O peers (correlation, sector tag and promoter-group map) that have captured <35% of their beta-scaled move. Short the first lower 5-min close.
- **Exit/stop:** Cover at 80% of the implied move or 15:10. Stop +0.7%.
- **Data:** 1-min, static peer map.
- **Failure:** Company-specific bad news helps competitors, so split by news type.
- **Known-variant?** Yes, Hou, CohenΓÇôFrazzini and FosterΓÇôHou intra-industry information transfer; no coded intraday rule known.
- **CONVICTION:** Claude 3/5, Gemini 4.5/5

**4. Unfinished Parent Order** (C2)
- **Mechanism:** Redeeming funds can't liquidate in one day without moving the price, so they slice sells at a steady participation rate and the remainder must trade tomorrow.
- **Entry:** At 09:50, rank F&O names on signed-volume persistence. This means ΓëÑ70% of 5-min windows over the prior day and the first 30 min with a below-mid volume-weighted close location, steady volume share, and no news. Short the top few.
- **Exit/stop:** Cover at 15:10. Stop at day-high +0.3 ATR.
- **Data:** 1-min.
- **Failure:** The net edge is thin, and absorbing buyers can end it.
- **Known-variant?** Order-splitting persistence (LilloΓÇôFarmerΓÇôBouchaud); not in retail books.
- **CONVICTION:** Claude 3/5, Gemini 4/5

**5. Breadth-Hollow Nifty Futures Short** (C34/C42)
- **Mechanism:** An index high carried by a few heavyweights has no discretionary breadth behind it, and futures chasers only see the index candle. The ~3 bp futures cost lets small edges survive.
- **Entry:** Nifty within 0.1% of day-high and ΓëÑ+0.4% from open, with Γëñ40% of constituents above their own VWAP. Short Nifty futures.
- **Exit/stop:** Cover when breadth >55%, after 60 min, or at +0.25%.
- **Data:** 1-min for 50 constituents plus weights.
- **Failure:** Heavyweight-led trend days. The sign of dealer flow is unknown, so test both.
- **Known-variant?** A/D-divergence lore; the constituent-VWAP rule isn't standard.
- **CONVICTION:** Claude 3/5, Gemini 3.5/5

**6. Square-Off Shelf** (C6/G41/G34/C27), F&O names only
- **Mechanism:** Leveraged MIS longs must exit by the broker's auto square-off. Signed up-leg volume maps the late-buyer inventory above price, and the deadline guarantees the supply arrives.
- **Entry:** After 11:00, when the underwater share of up-leg volume exceeds a frozen threshold vs expected remaining volume, short a retest rejection of the shelf on >2├ù volume.
- **Exit/stop:** Cover at 15:10. Stop 0.4% above entry.
- **Data:** 1-min.
- **Failure:** Large F&O names have little MIS volume, and the supply isn't tied to real traders. Treat this as a feature test, not a thesis.
- **Known-variant?** Volume-profile and disposition-effect cousin.
- **CONVICTION:** Claude 2/5, Gemini 4/5

**7. Closing-Mark Next-Day Unwind** (C8)
- **Mechanism:** The close is the 15:00ΓÇô15:30 VWAP, so a modest buyer can cheaply mark a stock up (collateral, NAV, window-dressing). Nobody defends the mark next day.
- **Entry:** Prior day ΓëÑ+2% inside 15:00ΓÇô15:30 on ΓëÑ3├ù normal per-minute volume, with no news. At 09:30, short if price is above yesterday's 14:59 level and has made no new high since 09:20.
- **Exit/stop:** Cover at the 14:59 level or 15:10. Stop at day-high.
- **Data:** 1-min.
- **Failure:** Real late news, and the gap-down may already hold the move.
- **Known-variant?** Gap-fade subset; close-marking is a known concept.
- **CONVICTION:** Claude 3/5, Gemini 3.5/5

**8. Volume Absorption Near Highs** (G7/C30/G29/C9)
- **Mechanism:** Heavy churn with no price progress near the day high suggests a large buyer is finished or inventory is being distributed into retail bids. The mechanism is unproven; this is a testable observable.
- **Entry:** Stock within 0.3% of day-high, 20-min volume >3├ù median with ΓëÑ65% lower-half closes. Short the break of the churn floor.
- **Exit/stop:** Cover at 15:10. Stop at churn high.
- **Data:** 1-min.
- **Failure:** A genuine whale sweeps the supply, and real trend days continue.
- **Known-variant?** Yes, Wyckoff-style absorption.
- **CONVICTION:** Claude 2/5, Gemini 4/5
