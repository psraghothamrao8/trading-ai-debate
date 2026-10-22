
### Gemini (cull round 1)
### Critical Disagreements & Factual Corrections

Before culling the pool, we must eliminate structural hallucinations and operational falsehoods introduced during the debate:

1. **The Fictional SEBI Margin Snapshot & VAR Step-Up (G4, G23):** SEBI does not mandate broker liquidations at a fixed "11:00 snapshot" or a "13:00 VAR step-up." SEBI mandates that Clearing Corporations take four *random intraday snapshots* across the day to check margin compliance. Margins are dynamically monitored; broker Risk Management Systems (RMS) do not fire synchronized market dump orders on an exchange clock schedule.
2. **The 09:15 AMO Queue Myth (G35):** After Market Orders (AMOs) on the NSE do *not* hit the market at 09:15 IST as unpriced market orders. AMOs are collected overnight and piped into the **Pre-Open Call Auction (09:00ΓÇô09:08 IST)** where they are matched at a single equilibrium discovery price. By 09:15, the AMO queue is completely cleared.
3. **The 11:15 DII SIP TWAP Cutoff (G24):** Institutional domestic funds (DIIs) do not run dumb TWAP orders that magically finish at 11:15 IST. Mutual funds slice orders across the entire session using full-day VWAP or POV algos through agency execution desks.
4. **The F&O 15-Minute Dynamic Band Cooling Myth (G3):** F&O stocks on the NSE do not have circuit locks or 15-minute cooling halts. They operate with *dynamic price bands* (operating ranges) that expand incrementally without halting trading. Halting occurs only in cash-only (non-F&O) scrips.
5. **Upper Circuit Shorting Infeasibility (C1):** Upper-circuit names are almost exclusively non-F&O cash scrips. Indian brokers strictly prohibit MIS (intraday shorting) on circuit-locked stocks. Attempting to short an unlocking upper circuit exposes a retail trader to buy-in short delivery auctions with statutory penalty losses up to 20%.
6. **L3 Data Delusions (G26, G49):** Ideas requiring millisecond queue-position tracking or VPIN order-toxicity metrics cannot be backtested or traded on retail 1-minute OHLCV data.

---

### Merges & Upgrades

- **The Institutional Diurnal POV-Throttle Vacuum (Upgrades & Merges C9, G29, G33):** Rather than guessing an arbitrary order-completion bar (C9) or claiming a mysterious "algo safety pause" (G33), this anchors directly in market microstructure: institutional buy metaorders operate on strict Participation Rate (POV) caps (typically 10ΓÇô15% of volume). When market-wide trading volume plummets by 50ΓÇô60% during the NSE midday lull (11:30ΓÇô12:45 IST), POV algorithms are mathematically mandated to cut their bid sizing in half. Momentum chasers who bought the morning breakout lose buyer support and hit an order-book vacuum.
- **Speculative-Turnover Hangover & Break-Even Wall Flush (Upgrades & Merges C19, G41):** Merges NSE daily bhavcopy delivery data with intraday volume-profile anchoring. When a stock surges on massive volume with deliverable volume in the bottom decile (<15%), the move is 85%+ retail intraday MIS leverage. When the stock stalls and drifts down, trapped longs create an impenetrable supply wall at their morning entry VWAP on the first midday relief bounce as disposition effect forces them to scramble to "get out even."
- **Cash-Futures Arbitrage Rollover & Liquidation Window (Upgrades & Merges G18, G1, C23):** Leverages the structural mechanics of IndiaΓÇÖs massive Γé╣1.5L+ Cr equity arbitrage fund industry. Desks systematically unwind cash baskets and roll positions between 14:00 and 15:00 IST, driving synthetic selling pressure into cash equities that retail dip-buyers cannot absorb.

---

### Complete Strategy Pool Scoring (1ΓÇô5 Scale)

*Criteria: **Plausibility** (P) | **Testability with 1-min/bhavcopy/options** (T) | **Survival after 7ΓÇô9 bps Costs/Slippage** (S) | **Novelty** (N) | **Conviction** (C)*

#### "C" Series (C1ΓÇôC42)

| ID | Strategy Name | P | T | S | N | C | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **C1** | Circuit-Lock Unlock Short | 2 | 2 | 1 | 3 | 1 | Killed |
| **C2** | Unfinished Parent Order | 4 | 5 | 4 | 4 | 4 | **TOP 10** |
| **C3** | Cosmetic-News Pop Fade | 3 | 3 | 2 | 3 | 2 | Killed |
| **C4** | Liquidity-Vacuum Spike Fade | 3 | 4 | 3 | 3 | 3 | Killed |
| **C5** | Put-Wall Short-Gamma Cascade | 4 | 4 | 4 | 3 | 3 | Killed |
| **C6** | MIS Deadline Unwind | 3 | 4 | 2 | 2 | 2 | Killed |
| **C7** | Supply-Floor Convergence | 4 | 3 | 4 | 4 | 2 | Killed |
| **C8** | Closing-Window Mark-up Unwind | 3 | 5 | 3 | 3 | 3 | Killed |
| **C9** | Metaorder Completion Cliff | 5 | 5 | 4 | 4 | 5 | **CHAMPION 1 (Merged)** |
| **C10** | Bar-Clock Herd Fade | 2 | 5 | 1 | 3 | 1 | Killed |
| **C11** | ETF Premium-to-Index Short | 2 | 3 | 1 | 2 | 1 | Killed |
| **C12** | Top-Gainers Attention Entry | 2 | 4 | 2 | 2 | 2 | Killed |
| **C13** | Disclosed-Seller Continuation | 3 | 3 | 3 | 3 | 2 | Killed |
| **C14** | Passive Deletion-Day Supply | 4 | 4 | 4 | 4 | 4 | **TOP 10** |
| **C15** | Governance-Flag Slow Bleed | 3 | 3 | 3 | 3 | 2 | Killed |
| **C16** | Promoter-Group Contagion Laggard | 4 | 4 | 4 | 4 | 4 | **TOP 10** |
| **C17** | Short-Covering Hangover | 3 | 4 | 3 | 2 | 2 | Killed |
| **C18** | Lock-In Expiry Overhang | 3 | 3 | 3 | 3 | 2 | Killed |
| **C19** | Speculative-Turnover Hangover | 5 | 5 | 4 | 5 | 5 | **CHAMPION 2 (Merged)** |
| **C20** | Exchange-Query Deflation | 3 | 3 | 3 | 3 | 2 | Killed |
| **C21** | ASM Leverage-Strip Day-One | 3 | 4 | 2 | 3 | 2 | Killed |
| **C22** | Holding-Company Look-Through Lag | 3 | 4 | 2 | 3 | 2 | Killed |
| **C23** | Futures-Absent Rally Fade | 4 | 4 | 3 | 4 | 3 | Killed |
| **C24** | Block-Window Reference Marking | 2 | 3 | 2 | 3 | 1 | Killed |
| **C25** | Silo Read-Through Laggard | 4 | 4 | 4 | 4 | 4 | Merged with C16 |
| **C26** | Stale-News Pop Fade | 3 | 3 | 3 | 4 | 2 | Killed |
| **C27** | Latent Stop Shelf | 3 | 4 | 3 | 4 | 3 | Killed |
| **C28** | Sales-Desk Downgrade Drip | 3 | 3 | 3 | 3 | 2 | Killed |
| **C29** | Short-Covering Exhaustion | 3 | 4 | 3 | 3 | 2 | Killed |
| **C30** | Volume-Quota Exhaustion Rank | 3 | 5 | 3 | 3 | 3 | Killed |
| **C31** | Tug-of-War Intraday Decay | 4 | 5 | 3 | 4 | 3 | Killed |
| **C32** | Same-Slot Persistence Short | 2 | 4 | 1 | 3 | 1 | Killed |
| **C33** | Beta-and-Peer-Neutral Spike Fade | 4 | 4 | 3 | 3 | 3 | Killed |
| **C34** | Breadth-Hollow Index Rally | 4 | 5 | 4 | 4 | 4 | **TOP 10** |
| **C35** | Delivery-Cost-Basis Break-Even Supply | 4 | 4 | 3 | 4 | 3 | Killed |
| **C36** | Stress-Day Thin-Name Catch-Up | 3 | 4 | 2 | 3 | 2 | Killed |
| **C37** | Retail-Cohort Burst Fade | 4 | 5 | 3 | 4 | 3 | Killed |
| **C38** | Stocks-to-Buy List Fade | 3 | 3 | 2 | 3 | 2 | Killed |
| **C39** | Earnings-Quality Mismatch Fade | 4 | 4 | 4 | 4 | 4 | **TOP 10** |
| **C40** | Beta-Chase Overshoot | 3 | 5 | 2 | 3 | 2 | Killed |
| **C41** | Weight-Proportional Basket Overshoot | 2 | 4 | 1 | 4 | 1 | Killed |
| **C42** | Penultimate-Window Index Short | 2 | 5 | 2 | 2 | 1 | Killed |

#### "G" Series (G1ΓÇôG49)

| ID | Strategy Name | P | T | S | N | C | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G1** | Basis-Inversion Arb Dump | 5 | 4 | 4 | 4 | 4 | Merged with G18 |
| **G2** | 0-DTE Call Gamma-Collapse | 4 | 4 | 4 | 4 | 4 | Merged with G32 |
| **G3** | Dynamic-Band Cooling Exhaustion | 1 | 3 | 1 | 2 | 1 | Killed |
| **G4** | Peak-Margin Snapshot Cascade | 1 | 4 | 1 | 2 | 1 | Killed |
| **G5** | Sympathy-Beta Exhaustion Short | 4 | 4 | 4 | 4 | 3 | Killed |
| **G6** | Euro Pre-Open Trap Unwind | 2 | 4 | 2 | 3 | 1 | Killed |
| **G7** | Iceberg Churn Breakdown | 4 | 4 | 4 | 3 | 3 | Killed |
| **G8** | Physical-Settlement Margin Dump | 4 | 4 | 4 | 4 | 3 | Killed |
| **G9** | Discounted-Block Arb Unload | 3 | 3 | 3 | 3 | 2 | Killed |
| **G10** | Pledged-Promoter Covenant Flush | 3 | 3 | 3 | 4 | 2 | Killed |
| **G11** | Sector-Titan Weight Cannibalization | 3 | 4 | 3 | 4 | 3 | Killed |
| **G12** | Mid-Session Guidance Trap | 4 | 3 | 4 | 3 | 3 | Merged with C39 |
| **G13** | Buy-Stop Sweep Exhaustion | 2 | 5 | 2 | 1 | 2 | Killed |
| **G14** | Ban-Ceiling Leverage Paralysis | 3 | 3 | 3 | 4 | 2 | Killed |
| **G15** | Index-Inclusion Front-Runner Flush | 3 | 3 | 3 | 4 | 2 | Killed |
| **G16** | Cross-Exchange Expiry Delta Spillover | 3 | 3 | 3 | 4 | 2 | Killed |
| **G17** | Earnings Con-Call Q&A Reversal | 3 | 2 | 3 | 4 | 2 | Killed |
| **G18** | Arbitrage-Fund Cash Liquidation Window | 5 | 4 | 5 | 5 | 5 | **CHAMPION 3 (Merged)** |
| **G19** | Dispersion Basket Contagion Short | 4 | 4 | 4 | 4 | 3 | Killed |
| **G20** | Post-Event Vol-Crush De-Hedging | 3 | 3 | 3 | 4 | 2 | Killed |
| **G21** | 09:20 Straddle Stop-Harvest Reversal | 3 | 4 | 3 | 4 | 3 | Killed |
| **G22** | Daily-Expiry Delta Un-hedging | 4 | 4 | 4 | 4 | 4 | Merged with G32 |
| **G23** | VAR-Margin Step-Up Flush | 1 | 4 | 1 | 2 | 1 | Killed |
| **G24** | DII Buy-TWAP Exhaustion | 1 | 4 | 1 | 2 | 1 | Killed |
| **G25** | T+1 Auction-Shortage Flush | 2 | 3 | 2 | 3 | 1 | Killed |
| **G26** | Tick-Size Queue Depletion | 2 | 1 | 1 | 3 | 1 | Killed |
| **G27** | Strike-Pinning Fracture Dump | 4 | 4 | 4 | 4 | 3 | Killed |
| **G28** | Conversion-Arb Cash Cascade | 4 | 3 | 3 | 4 | 3 | Killed |
| **G29** | Algorithmic POV Throttle Cliff | 5 | 5 | 4 | 4 | 5 | Merged with C9 |
| **G30** | Diurnal Vanna-Crush De-Hedging | 4 | 3 | 3 | 4 | 3 | Killed |
| **G31** | 15:00 VWAP Front-Runner Flush | 4 | 5 | 4 | 4 | 4 | **TOP 10** |
| **G32** | Lottery-Call Delta Cliff Unwind | 5 | 4 | 4 | 5 | 5 | **TOP 10** |
| **G33** | Institutional TWAP Collar Pause | 4 | 5 | 4 | 4 | 4 | Merged with C9 |
| **G34** | Intraday MTM Square-Off Cascade | 3 | 4 | 3 | 3 | 2 | Killed |
| **G35** | Opening AMO Queue Exhaustion | 1 | 5 | 1 | 2 | 1 | Killed |
| **G36** | Inventory-Limit Reservation Flush | 4 | 4 | 3 | 4 | 3 | Killed |
| **G37** | NDS-OM Yield-Shock De-Rating | 3 | 2 | 2 | 4 | 2 | Killed |
| **G38** | Retail API Batch-Order Fade | 3 | 4 | 2 | 4 | 2 | Killed |
| **G39** | Cross-Sector Capital Rotation Drag | 3 | 4 | 3 | 4 | 3 | Killed |
| **G40** | Stat-Arb Residual Variance Flush | 4 | 4 | 4 | 4 | 3 | Killed |
| **G41** | Intraday Break-Even Relief Wall | 5 | 5 | 4 | 5 | 5 | Merged with C19 |
| **G42** | Cross-Border ADR Parity Arbitrage | 3 | 3 | 3 | 3 | 2 | Killed |
| **G43** | Charm-Deflation Delta Unwind | 4 | 4 | 4 | 4 | 4 | Merged with G32 |
| **G44** | Zero-Gamma Phase-Transition Cascade | 4 | 4 | 4 | 4 | 4 | Merged with G32 |
| **G45** | Sticky-Strike Gamma Saturation Flush | 4 | 4 | 4 | 4 | 3 | Killed |
| **G46** | Adaptive-POV Cooldown Vacuum | 2 | 5 | 2 | 2 | 2 | Killed |
| **G47** | Pairs Stat-Arb De-Leveraging Flush | 4 | 4 | 4 | 4 | 4 | **TOP 10** |
| **G48** | Index Implied-Correlation Dispersion Drag | 4 | 4 | 3 | 4 | 3 | Killed |
| **G49** | VPIN Toxicity Liquidity-Freeze Air-Pocket | 2 | 1 | 1 | 3 | 1 | Killed |

---

### The Champion 3 (Bet-the-House Conviction)

#### 1. The Institutional Diurnal POV-Throttle Vacuum (Upgraded C9 + G29 + G33)
- **Counterparty & Trap:** Institutional metaorders executing large parent buy orders under strict algorithmic constraints (Percentage of Volume / POV caps strictly bound to 10ΓÇô15% of market volume).
- **Why It Works:** Indian equities exhibit an extreme intraday U-curve where aggregate volume drops 50ΓÇô60% between 11:30 and 12:45 IST. Because POV algorithms scale buy volume strictly with market participation, the algorithmic buy bid is mechanically halved during this window regardless of the parent order's remaining size. Naive retail breakout traders who bought morning highs suddenly find themselves stranded without institutional absorption, forcing market makers to mark quotes down to find natural bids. This delivers a clean 35ΓÇô65 bps air-pocket drop back to the morning VWAP that easily beats the 7ΓÇô9 bps round-trip friction.

#### 2. Speculative-Turnover Hangover & Break-Even Relief Flush (Upgraded C19 + G41)
- **Counterparty & Trap:** Overleveraged retail MIS day-traders and momentum breakout algos who bought speculative morning volume spikes.
- **Why It Works:** By cross-referencing previous-day NSE bhavcopy deliverable volume with total turnover, we isolate stocks where delivery % drops into the bottom decile (<15%) despite a >3.5% surge, proving the move is pure intraday leverage with zero institutional overnight ownership. When the morning spike inevitably stalls, trapped retail longs sit on paper losses of 1ΓÇô2% and become dominated by the behavioral disposition effect. The moment a midday relief bounce reaches within 5ΓÇô10 bps of their morning entry VWAP, an impenetrable supply wall of panic break-even orders floods the book, driving an immediate 60ΓÇô120 bps liquidation leg into the afternoon.

#### 3. Arbitrage-Fund Cash Liquidation & Basis-Inversion Window (Upgraded G18 + G1)
- **Counterparty & Trap:** India's massive Γé╣1.5L+ Cr cash-futures mutual fund arbitrage desks managing daily creations, redemptions, and rollovers.
- **Why It Works:** Cash-and-carry arbitrage desks hold long physical equities hedged with short stock futures. Between 14:00 and 15:00 IST, roll mandates and daily redemption square-offs force these funds to systematically dump cash shares into the market while repurchasing futures. When near-month futures trade at an intraday discount or parity to cash near session highs, arb desks are non-discretionary, price-insensitive sellers of cash MIS equity. Shorting the cash scrip as basis inverts exploits a multi-hundred-crore mechanical institutional outflow that crushes retail dip-buyers.

---

### The Top 10 Ranked Strategies

1. **The Institutional Diurnal POV-Throttle Vacuum (C9/G29/G33):** Monetizes the mathematical halving of institutional algorithmic bids during the 11:30ΓÇô12:45 volume lull.
2. **Speculative-Turnover Hangover & Break-Even Relief Flush (C19/G41):** Exploits NSE bhavcopy delivery-to-volume decoupling combined with trapped retail disposition-effect supply walls.
3. **Arbitrage-Fund Cash Liquidation Window (G18/G1):** Exploits non-discretionary equity basket dumping by Γé╣1.5L Cr Indian arbitrage mutual funds between 14:00ΓÇô15:00 IST.
4. **0-DTE Expiry Charm & Asymptotic Delta-Cliff Flush (G32/G43/G2):** Monetizes mathematically mandated cash hedge liquidations by option dealers as afternoon theta/charm crushes retail lottery-call deltas on daily expiry cycles.
5. **Conglomerate Risk-Limit Contagion Laggard (C16/C25):** Exploits institutional cross-entity portfolio risk caps that force indiscriminate basket sales across corporate groups while retail trades individual tickers in silos.
6. **Pairs Stat-Arb De-Leveraging Flush (G47):** Exploits quantitative multi-factor long/short desks programmatically dumping the long leg when intra-sector pair spreads exceed 3-sigma risk limits.
7. **Passive Index Deletion Closing-Window Pressure (C14):** Exploits guaranteed 15:00ΓÇô15:30 closing VWAP imbalances where passive trackers must purge deleted constituents regardless of price.
8. **Earnings-Quality Mismatch Fade (C39/G12):** Fades headline PAT beats when granular operating margins (EBITDA) contract, front-running algorithmic institutional de-ratings.
9. **Unfinished Parent Order Liquidation Drift (C2):** Exploits multi-day institutional redemption slicing identified through volume-weighted close location persistence.
10. **Breadth-Hollow Index Rally Exhaustion (C34):** Shorts Nifty index futures when index highs are driven by <35% constituent participation, exploiting inevitable late-session synthetic unwinds.

---

### Ruthless Kill List (The Remaining 81 Ideas)

- **C1:** Brokers strictly disallow MIS shorting on locked upper-circuit stocks, exposing traders to lethal 20% buy-in auction penalties.
- **C3:** Text classification of press releases is noisy, and genuine retail small-cap manias often expand for multiple sessions.
- **C4:** Fading low-volume spikes gets steamrolled when the move is driven by an iceberg order placed by an informed institution.
- **C5:** Put-wall gamma cascades only trigger on index expiry breakdowns, failing the requirement for high-frequency daily stock shorting.
- **C6:** Retail 15:15 MIS auto-square-off unwinds are overcrowded, well-anticipated by HFTs, and yield insufficient net edge after costs.
- **C7:** OFS and QIP deals occur only a few times per quarter, completely failing the daily operational criteria.
- **C8:** Closing VWAP markups produce gross moves under 20 bps that are routinely wiped out by morning gap slippage.
- **C10:** 15-minute candle-boundary order bursts generate 10ΓÇô15 bps micro-moves that fail to clear the 8 bps round-trip friction.
- **C11:** Indian equity ETFs suffer from wide bid-ask spreads, severe tracking errors, and frequent broker MIS restrictions.
- **C12:** Broker top-gainers lists attract sustained multi-day momentum that consistently triggers short-seller stop-losses.
- **C13:** Institutional bulk sellers typically execute via negotiated off-market tranches rather than continuous open-market open-ended dumping.
- **C15:** Timestamped corporate governance filings result in immediate illiquid gap-downs with high intraday drift noise.
- **C17:** Next-day short-covering hangover suffers from overnight gap risk that destroys intraday risk-reward profiles.
- **C18:** Promoter and PE lock-in expirations are infrequent calendar events that fail daily execution requirements.
- **C20:** Exchange clarification queries are standard boilerplate, erratic in arrival, and rarely alter speculative price trajectories.
- **C21:** ASM inclusion stocks are routinely placed on broker MIS ban lists, preventing cash intraday short execution.
- **C22:** Holding-company discount spreads are structurally volatile and can widen for months without intraday convergence.
- **C23:** Futures-absent cash rallies frequently represent genuine institutional delivery buying that does not mean-revert.
- **C24:** The afternoon block window operates under negotiated reference limits and does not produce exploitable continuous market moves.
- **C26:** TF-IDF text similarity algorithms are too blunt to differentiate between redundant announcements and material follow-on orders.
- **C27:** Discretionary retail traders do not use standardized stop-loss percentages, completely smearing the theoretical stop shelf.
- **C28:** Brokerage downgrades are widely leaked before market open; the intraday sales-desk drip is too weak to beat transaction friction.
- **C29:** Intraday OI reductions during rallies are too noisy on 1-minute bars to reliably separate short-covering from fresh long accumulation.
- **C30:** Volume-quota exhaustion triggers false signals on genuine trend days where turnover expands exponentially.
- **C31:** Persistent open-to-close bleeders generate a net statistical drift (~12 bps) that barely covers the 8 bps friction hurdle.
- **C32:** Intraday half-hour time-slot persistence delivers an average edge of 3ΓÇô5 bps, which is entirely consumed by exchange charges and STT.
- **C33:** Residual single-stock idiosyncratic spikes are frequently driven by unannounced material leaks that lead to severe short squeezes.
- **C35:** Bhavcopy delivery VWAP calculation is heavily distorted on thin-volume days, creating false break-even reference levels.
- **C36:** Market stress days occur in less than 15% of annual trading sessions, failing the daily trade frequency requirement.
- **C37:** Retail penny-stock cohorts frequently enter unshortable T2T or GSM frameworks that block intraday MIS orders.
- **C38:** Scraped morning media recommendation lists suffer from massive latency and negative post-cost edge.
- **C40:** High-beta overshoot short baskets have severe negative market beta, leading to catastrophic drawdowns on strong trend-up days.
- **C41:** Index basket liquidity overshoot dissipates in milliseconds via collocated HFT arbitrage, making it untradable on 1-minute bars.
- **C42:** The 14:30 Nifty momentum short yields an expected gross alpha of only 4 bps against a 3 bps futures friction cost.
- **G3:** Based on a fictional premise; NSE F&O scrips have dynamic bands that expand without 15-minute cooling halts.
- **G4:** Factually flawed; SEBI margin snapshots are randomized across Clearing Corporations and do not fire at 11:00 IST.
- **G5:** Sympathy-beta peers in Indian midcaps frequently gap up and lock circuits rather than providing clean intraday short entries.
- **G6:** European pre-open equity correlation to Indian single-stock intraday momentum is statistically indistinguishable from zero.
- **G7:** Identifying hidden iceberg churn from 1-minute bar close skews generates excessive false positives during genuine accumulation.
- **G8:** Physical settlement delivery liquidations occur exclusively once a month on monthly expiry Thursday, failing daily operation.
- **G9:** Pre-market discounted blocks occur irregularly and are rapidly arbitraged within the opening 60 seconds of trading.
- **G10:** Pledged promoter covenant breaches are rare crisis events that cannot sustain an everyday systematic trading book.
- **G11:** Sector weight cannibalization effects are too diffuse across secondary constituents to reliably offset individual stock drift.
- **G13:** A repackaging of retail Turtle Soup / false breakout technical analysis that lacks a non-obvious structural edge.
- **G14:** Stocks approaching 95% MWPL trigger severe short squeezes as borrow rates spike and shorts scramble to cover.
- **G15:** Index inclusion rebalance dates happen only semi-annually, providing zero day-to-day tradeable frequency.
- **G16:** HFT cross-exchange latency engines eliminate BSE/NSE delta arbitrage spreads within sub-millisecond windows.
- **G17:** Earnings concall audio streams lack standardized intraday timestamps, making programmatic rule-based entry untestable.
- **G19:** Dispersion basket contagion shorts suffer high adverse selection against individual stocks with idiosyncratic positive catalysts.
- **G20:** Post-event IV crush is confined to rare scheduled macro events (RBI policy, budget) and does not support daily trading.
- **G21:** 09:20 straddle stop runs are heavily competed for by dedicated Indian HFTs, leaving no edge for 1-minute retail models.
- **G22:** Constituent delta un-hedging is redundant and strictly inferior to executing directly on the underlying index options surface.
- **G23:** Factually false; NSE Clearing does not implement an intraday VAR margin step-up at 13:00 IST.
- **G24:** Factually false; DII mutual funds do not truncate daily SIP execution at an arbitrary 11:15 IST clock mark.
- **G25:** NSE T+1 shortage auctions take place in an isolated auction market session and do not interact with continuous cash MIS books.
- **G26:** Sub-Γé╣100 tick-size queue exhaustion requires Level 3 tick-by-tick order book data that cannot be traded on 1-minute OHLCV.
- **G27:** Strike pinning breakdowns are vulnerable to violent late-session short squeezes on unexpected market-on-close demand.
- **G28:** Conversion-arbitrage mispricings on Indian single stocks are captured in sub-second timeframes by Tier-1 HFT desks.
- **G30:** Diurnal morning IV crush is largely priced into the opening derivative spread and rarely translates into equity spot drift.
- **G31:** Trapped closing front-runners face asymmetric tail risk if a large institutional market-on-close buy order prints at 15:00.
- **G34:** Broker automated RMS liquidation algorithms trigger at unpredictable individual loss thresholds rather than an intraday window.
- **G35:** Factually false; AMOs are executed during the 09:00ΓÇô09:08 pre-open call auction, leaving zero unpriced volume at 09:15.
- **G36:** HFT inventory limits are managed dynamically across multi-asset books and do not produce predictable single-stock spot selloffs.
- **G37:** NDS-OM sovereign bond yield feeds are unavailable in retail data stacks and exhibit weak 1-minute equity correlation.
- **G38:** Retail API 15-minute candle breakouts produce micro-wicks that are far too narrow to overcome the 8 bps round-trip friction.
- **G39:** Intraday cross-sector rotation funding flows are overpowered by broad market beta on positive macro trend days.
- **G40:** Multi-factor stat-arb residual mean-reversion models require low-latency portfolio execution across hundreds of pairs to survive friction.
- **G42:** Indian ADRs are limited to a small handful of mega-caps where ADR-NSE parity spreads are closed by offshore desks in milliseconds.
- **G44:** Calculating precise zero-gamma transition levels on single-stock options requires institutional implied volatility surface feeds.
- **G45:** Heavy call-strike saturation trades suffer severe right-tail blowups when underlying spot prices break out into runaway trends.
- **G46:** A simple upper-rejection-wick candlestick pattern rebranded as an "algorithmic pause" with no verifiable structural edge.
- **G48:** Single-stock dispersion arbitrage requires simultaneously trading options across the entire index, exceeding retail capabilities.
- **G49:** True VPIN order-flow toxicity requires microstructure trade classification, which is impossible to compute on 1-minute OHLCV.

### Claude (cull round 1)
# Claude cull, round 2

I agree with Gemini on the dead premises (G3, G4, G23, G24, G35 and C1). I disagree on its three champions, on several kills, and on its inconsistent application of the daily-signal rule. Costs, STT rates and expiry schedules are from memory, so verify them. I assume about 8 bp round trip for liquid cash MIS and about 3 bp for Nifty futures.

## Where Gemini is wrong

1. **Its Champion 1 (POV throttle) has a mechanism flaw.** A POV algo targets a share of volume, so when market volume halves its bid halves too, and its share of flow stays 10ΓÇô15%. There is no vacuum. The claimed "35ΓÇô65 bp air-pocket" is also larger than a typical one-standard-deviation midday hour for a large-cap. The observable (a volume surge with no price progress near the high) survives as a pattern test, but the "mathematical mandate" doesn't.
2. **Its Champion 3 (arb-fund 14:00ΓÇô15:00 window) is invented.** Arbitrage funds roll mostly in the final days before monthly expiry. They unwind redemptions as pairs, usually near the close for NAV matching. The cash leg of that is largely hedged and small against ADV. I keep only a basis-shock test, with the window removed (#9).
3. **Its #4 (0-DTE gamma) fails the daily rule.** As I understand it, NSE has one weekly expiry (Nifty) and stock options expire monthly. Gemini killed G8, G10 and G15 for infrequency but promoted G32 and C14 on the same flaw. C14 also fails on timing: passive deletion flow trades in the 15:00ΓÇô15:30 VWAP, and we must be flat at 15:15. G22 is wrong too, since index-option dealers hedge with futures, not top constituents.
4. **It uses invented numbers as kill reasons.** The "4 bp" (C42), "12 bp" (C31) and "<20 bp" (C8) figures are not known without a backtest. Kill on mechanism or data, not made-up magnitudes. Similarly, "market-on-close buy order" (G31) refers to a mechanism I don't believe NSE cash has. Close is the 15:00ΓÇô15:30 VWAP, though SEBI has consulted on a closing auction, so verify.
5. **Its kills are inconsistent.** It killed G40 for needing low-latency stat-arb but kept G47, which is the same family. It killed C33 for "leak risk", which is just the news filter. It said VPIN is "impossible" on bars, but bulk-volume classification exists. I still kill G49, because VPIN's predictive power has been shown to come mechanically from volume.
6. **Its AMO claim is overstated.** AMO routing is broker-specific, not a clean 09:00ΓÇô09:08 auction. G35 is dead anyway because its premise can't be verified.

## Scores for all 91 ideas

P = edge plausibility, T = testable on 1-min bars plus daily files, S = survives costs, N = novelty. Γÿà = in my top 10 (ΓåÆ the number is its rank).

### C-series

| ID | P | T | S | N | Verdict |
|---|---|---|---|---|---|
| C1 | 2 | 3 | 1 | 3 | Kill: MIS shorts are blocked on locked names, and short-delivery auction close-out is a large tail loss |
| C2 | 3 | 5 | 2 | 3 | ΓÿàΓåÆ5 |
| C3 | 3 | 2 | 2 | 3 | Kill: needs a headline classifier and is sparse |
| C4 | 3 | 5 | 3 | 2 | ΓÿàΓåÆ2 (spike-fade core) |
| C5 | 3 | 3 | 4 | 3 | ΓÿàΓåÆ8 (index expiry arm) |
| C6 | 3 | 4 | 3 | 3 | ΓÿàΓåÆ1 (deadline supply) |
| C7 | 3 | 2 | 3 | 3 | Kill: OFS/QIP are a few per quarter |
| C8 | 3 | 5 | 3 | 3 | ΓÿàΓåÆ7 |
| C9 | 3 | 2 | 3 | 3 | Fold into #5 as the "order finished" state; not detectable on OHLCV alone |
| C10 | 2 | 5 | 1 | 2 | Kill: 15-min boundary micro-moves, and HFT trades them |
| C11 | 2 | 2 | 1 | 1 | Kill: ETF spreads and MIS limits |
| C12 | 2 | 4 | 2 | 2 | Kill: the list isn't in the data, and it's a weak #3 |
| C13 | 2 | 2 | 2 | 3 | Kill: sparse, and needs bulk/block files |
| C14 | 3 | 3 | 3 | 3 | Kill: quarterly, and the flow lands after our exit |
| C15 | 3 | 2 | 2 | 2 | Kill: rare filings that gap |
| C16 | 3 | 3 | 3 | 3 | Fold into #6 (group events are too rare standalone) |
| C17 | 3 | 4 | 2 | 2 | Kill: next-day gap-fade variant that needs OI |
| C18 | 3 | 2 | 3 | 2 | Kill: sparse calendar, shortability |
| C19 | 4 | 4 | 3 | 3 | ΓÿàΓåÆ3 |
| C20 | 2 | 1 | 2 | 3 | Kill: needs a filings feed, rare |
| C21 | 3 | 3 | 2 | 2 | Kill: ASM names are usually MIS-blocked |
| C22 | 2 | 3 | 2 | 3 | Kill: few events and a drifting discount |
| C23 | 4 | 4 | 3 | 3 | Fold into #2 as the confirmation filter |
| C24 | 2 | 2 | 2 | 3 | Kill: unverified window, rare |
| C25 | 3 | 3 | 3 | 3 | ΓÿàΓåÆ6 |
| C26 | 2 | 2 | 2 | 3 | Kill: text matching noise |
| C27 | 3 | 5 | 3 | 4 | Fold into #1 (volume-at-price map) |
| C28 | 2 | 1 | 2 | 2 | Kill: no data |
| C29 | 3 | 2 | 2 | 3 | Kill: no intraday OI |
| C30 | 3 | 5 | 3 | 2 | Fold into #10 |
| C31 | 3 | 5 | 1 | 3 | Kill standalone; use as a ranking feature |
| C32 | 3 | 5 | 1 | 3 | Kill standalone; use as a timing feature |
| C33 | 4 | 5 | 3 | 2 | ΓÿàΓåÆ2 (core) |
| C34 | 3 | 4 | 4 | 3 | ΓÿàΓåÆ4 |
| C35 | 3 | 4 | 2 | 3 | Kill: thin-delivery noise |
| C36 | 3 | 4 | 2 | 2 | Kill: about 15% of days, thin names |
| C37 | 3 | 5 | 2 | 3 | Fold into #3 as a regime filter |
| C38 | 2 | 1 | 2 | 3 | Kill: scraping |
| C39 | 3 | 2 | 3 | 3 | Kill: needs fundamentals feeds, and PEAD usually continues |
| C40 | 3 | 4 | 2 | 3 | Kill: negative-beta basket loses on trend days |
| C41 | 2 | 3 | 1 | 3 | Kill: sub-minute arb |
| C42 | 3 | 5 | 4 | 2 | ΓÿàΓåÆ4 |

### G-series

| ID | P | T | S | N | Verdict |
|---|---|---|---|---|---|
| G1 | 3 | 4 | 3 | 3 | ΓÿàΓåÆ9 |
| G2 | 2 | 2 | 2 | 3 | Kill: stock options are monthly, so it's not daily |
| G3 | 1 | 3 | 1 | 2 | Kill: unverified premise |
| G4 | 1 | 4 | 1 | 2 | Kill: unverified premise (random snapshots) |
| G5 | 3 | 4 | 3 | 3 | Fold into #2 (peer-based) |
| G6 | 1 | 4 | 1 | 2 | Kill |
| G7 | 3 | 4 | 3 | 2 | ΓÿàΓåÆ10 |
| G8 | 3 | 2 | 3 | 4 | Kill: monthly only |
| G9 | 2 | 2 | 2 | 3 | Kill: rare, arbitraged |
| G10 | 3 | 2 | 2 | 3 | Kill: rare, pledge data |
| G11 | 3 | 4 | 3 | 3 | Fold into #6 |
| G12 | 3 | 2 | 3 | 3 | Kill: sparse in-session prints |
| G13 | 2 | 5 | 2 | 1 | Kill: turtle soup |
| G14 | 2 | 1 | 2 | 3 | Kill: no intraday MWPL |
| G15 | 2 | 2 | 2 | 3 | Kill: quarterly |
| G16 | 2 | 3 | 2 | 2 | Kill |
| G17 | 2 | 1 | 2 | 3 | Kill: no timestamps |
| G18 | 3 | 4 | 3 | 3 | Fold into #9 |
| G19 | 3 | 4 | 3 | 3 | Fold into #2 |
| G20 | 2 | 2 | 2 | 3 | Kill: rare, needs IV data |
| G21 | 2 | 3 | 1 | 3 | Kill: HFT-crowded |
| G22 | 2 | 3 | 2 | 2 | Kill: dealers hedge with futures |
| G23 | 1 | 4 | 1 | 2 | Kill: unverified premise |
| G24 | 1 | 4 | 1 | 2 | Kill: unverified premise |
| G25 | 1 | 2 | 1 | 3 | Kill: separate auction session |
| G26 | 2 | 1 | 1 | 3 | Kill: needs L3 data |
| G27 | 3 | 3 | 4 | 3 | Fold into #8 |
| G28 | 2 | 1 | 2 | 3 | Kill: latency game |
| G29 | 2 | 5 | 2 | 3 | Fold into #10; the mechanism is wrong |
| G30 | 2 | 1 | 2 | 3 | Kill: no IV data, speculative sign |
| G31 | 2 | 5 | 2 | 3 | Kill: no MOC mechanism |
| G32 | 2 | 2 | 2 | 3 | Fold into #8 as the index arm only |
| G33 | 2 | 5 | 2 | 2 | Kill: "collar" is invented; folded into #10 |
| G34 | 3 | 4 | 3 | 3 | Fold into #1 (use the volume map, since RMS thresholds are unknown) |
| G35 | 1 | 5 | 1 | 2 | Kill: unverified premise |
| G36 | 3 | 4 | 2 | 2 | Kill: unfounded inventory story |
| G37 | 2 | 1 | 1 | 3 | Kill: no feed |
| G38 | 2 | 5 | 1 | 2 | Kill: same as C10 |
| G39 | 3 | 4 | 2 | 3 | Fold into #6 |
| G40 | 4 | 4 | 3 | 2 | Fold into #2 |
| G41 | 4 | 5 | 3 | 4 | ΓÿàΓåÆ1 |
| G42 | 2 | 2 | 2 | 2 | Kill: a handful of ADR names |
| G43 | 2 | 1 | 2 | 3 | Kill: needs option data |
| G44 | 2 | 1 | 2 | 3 | Kill: needs option data |
| G45 | 2 | 1 | 2 | 3 | Kill: needs option data |
| G46 | 2 | 5 | 2 | 1 | Kill: wick pattern |
| G47 | 3 | 4 | 3 | 3 | Fold into #2 |
| G48 | 3 | 4 | 3 | 3 | Fold into #2 |
| G49 | 2 | 2 | 1 | 3 | Kill: VPIN power is volume-mechanical |

## My three champions

**1. The Square-Off Shelf (C6 + G41 + C27 + G34), conviction 4/5.** Leveraged MIS longs usually can't convert to delivery because they lack the capital, so the broker's auto square-off (about 15:15ΓÇô15:25, broker-specific) forces them to sell at market. Their entry prices are observable. Volume traded on the up-leg, signed by bar direction, maps how much late-buyer inventory sits above the current price. When that underwater share is large against expected remaining volume, retests face break-even sellers, and the deadline guarantees the supply arrives by the close. The losing side is late retail chasers, who can't stop being wrong because of leverage and a clock. HFT can see this too, so I expect the edge in retail-heavy names rather than the most liquid ones. It is partly a volume-profile idea, which exists in retail books. The novelty is the deadline weighting and the underwater-share score.

**2. The Unconfirmed-Pop Fade (C4 + C23 + C33 + G5 + G19 + G40 + G47 + G48), conviction 4/5.** Take a move of at least 3.5╧â against the stock's own time-of-day range, after the first 45 minutes. It must not be explained by beta ├ù Nifty or by the sector and peer cluster, and futures volume must not confirm it. That is a liquidity-demand shock from chasers, and liquidity providers get paid when it reverts. The late-day MIS deadline makes the reversal asymmetric, because buyers who entered late must exit. Gemini's "leak risk" objection is handled by the filters and tested by the stop. This is a known family (residual reversal, Nagel). My novelty claim is the futures-absent and peer-absent conditions, which I haven't seen coded.

**3. The Speculative-Attention Hangover (C19 + C37 + C12), conviction 4/5.** Yesterday's volume-led spike with delivery % in the bottom quintile of the stock's own 60-day history, plus turnover high against free float, marks churn by MIS traders and operators. Nobody funds a continuation. Retail reads volume plus a green candle as strength. Short today's first failed bounce below yesterday's close. The signal uses only completed daily data, so there is no overnight gap risk. The selector is also a regime filter for Champion 1, and the two should be tested separately first, then stacked. The effect is documented (Llorente et al.), but I know of no coded Indian version.

## Top 10, ranked

1. **Square-Off Shelf** (C6/G41/C27/G34). Conviction 4.
2. **Unconfirmed-Pop Fade** (C4/C23/C33/G5/G19/G40/G47/G48). Conviction 4.
3. **Speculative-Attention Hangover** (C19/C37). Conviction 4.
4. **Index Dealer-Flow Momentum Short** (C42/C34). Conviction 3. Nifty futures costs about 3 bp, so small edges can survive. The gamma-hedging sign for Indian dealers is unknown, so test both signs. It is the only idea where cost isn't the main killer.
5. **Flow-Persistence Short** (C2, with C9 as the exit state). Conviction 3. It's a cross-sectional daily rank on signed-volume persistence. The net edge may be thin.
6. **Peer-Lag Laggard Short** (C25/C16/G11/G39). Conviction 3. Liquid names are probably arbitraged, so it's more plausible in mid-caps.
7. **Closing-Mark Next-Day Unwind** (C8). Conviction 3. The close is a 30-minute VWAP, so a modest buyer can mark it. It's cheap to test.
8. **Expiry-Day Strike-Break Short, index only** (C5/G27/G32). Conviction 3. It runs about weekly, which is thin for sample size. SEBI's July 2025 interim order alleged an expiry-day index pattern against one prop firm. Treat that as an allegation, and any such pattern has probably decayed.
9. **Basis-Shock Short** (G1/G18). Conviction 2. Test shorting cash versus futures when the basis z-score is extreme. Futures lead cash by seconds, so I doubt 1-min bars catch it.
10. **Volume-Absorption Short** (G7/C30/G29). Conviction 2. It's a volume surge with no progress near the day high. This is a textbook Wyckoff family, so I flag it as known.

## Protocol for the top 10

- Freeze one parameter set per idea before touching data.
- Use at least 3 years of 1-min data and report net bp per trade with day-clustered t-stats.
- Require the sign to hold in every year.
- Benchmark against random entries at the same time in the same stocks, to strip out time-of-day drift.
- Rerun at 1.5├ù slippage.
- With about 10 hypotheses tested, demand t ΓëÑ 3.
- Require signals on at least 70% of days, and drop any name the broker blocks for MIS shorts.

### Gemini (cull round 2)
# Deliberation & Strategy Cull: Round 2 Review

---

## 1. Critical Audit & Factual Corrections: Claude vs Gemini

Both previous rounds correctly eliminated the most obvious structural fallacies (such as the fictional 15-minute F&O cooling halts, fixed 11:00 margin snapshots, 13:00 VAR step-ups, and 11:15 DII SIP cutoffs). However, both Claude and Gemini committed significant errors in market microstructure, regulatory reality, and trade execution.

### Where Gemini Was Wrong
1. **The Single-Stock 0-DTE Hallucination (G2, G32, G43, G44, G45):** Gemini repeatedly built strategies on intraday 0-DTE single-stock option dynamics (Charm decay, Zero-Gamma flips, lottery-call delta collapses). **Under SEBI and NSE regulations, single-stock options expire strictly once a month** (on the last Thursday of the expiry month, physically settled). Weekly options are strictly index-only (and restricted to one benchmark index per exchange under SEBI's October 2024 framework). Testing daily 0-DTE single-stock delta collapses is structurally impossible.
2. **The "Arbitrage Mutual Fund Cash Dump" Myth (G18):** Arbitrage mutual funds (~Γé╣1.5L+ Cr AUM in India) run fully hedged Cash-and-Carry positions (Long Cash + Short Stock Futures). When basis inverts, mutual funds do **not** dump naked cash equity between 14:00ΓÇô15:00. Under SEBI mutual fund regulations, mutual funds cannot take net short cash positions or naked derivative shorts. Basis-inversion unwinds are driven by proprietary HFT desks and institutional offshore accounts, not mutual fund cash liquidation desks.
3. **The "POV-Throttle Vacuum" Flaw (G29, G33, Gemini Champion 1):** A Percentage-of-Volume (POV) algorithm targets an execution participation rate (typically 10ΓÇô15% of market volume). When volume halves during the midday lull, the algo's order size halves, but its participation share remains 10ΓÇô15%. It does not create an "empty order-book vacuum" of 35ΓÇô65 bps out of thin air.

### Where Claude Was Wrong
1. **Champion 1 ("Square-Off Shelf" / C6 + G41 + C27 + G34) Fails Execution:** Claude champions shorting retail-heavy names into the 14:40ΓÇô15:15 window. In reality:
   - High retail-turnover stocks with low institutional floats are predominantly placed in ASM/GSM/T2T or trade-to-trade segments where Indian brokers (Zerodha, Groww, AngelOne) **strictly prohibit MIS shorting** to avoid 20% auction penalty defaults.
   - For liquid F&O names, entering at 14:40 to exit by 15:10 collides directly with the 15:00ΓÇô15:30 closing VWAP benchmark window, where passive institutional execution engines create erratic price spikes that whip tight intraday stops.
2. **Champion 2 ("Unconfirmed-Pop Fade" / C4 + C33) Sits on a Landmine:** Fading an unexplained 3.5-sigma move on a single stock because "futures/peers didn't confirm" ignores the primary driver of such moves in Indian midcaps: **unannounced corporate news leaks and promoter block trades**. Shorting an unexplained 3.5-sigma spike without a confirmed fundamental mismatch is the fastest way to get trapped in an upper-circuit lock or an 8% runaway trend day.
3. **Inconsistent Expiry Rules:** Claude correctly criticized Gemini for promoting monthly single-stock options, yet ranked an index-only expiry strategy (**#8 / C5/G27/G32**) in its Top 10. A strategy that generates signals on only 1 day a week violates the core requirement of **daily, systematic operation**.
4. **Dismissing Intraday Cash-Futures Arb (G1):** Claude claimed that "futures lead cash by seconds, so 1-minute bars won't catch basis inversion." That is true for 1-tick latency arbitrage, but false for structural institutional basis inversions. When deep institutional selling pushes stock futures into sustained discount near session highs, the resulting spot basket unwinds take 15ΓÇô35 minutes of algorithmic slicing, printing clean, tradable 1-minute bar signals.

---

## 2. Complete Strategy Pool Scoring (91 Candidate Ideas)

*Criteria (1ΓÇô5 scale):*
- **P (Plausibility):** Economic/microstructural logic of the counterparty's forced behavior.
- **T (Testability):** Feasibility using 1-minute OHLCV, previous-day bhavcopy/delivery %, and standard F&O/index feeds.
- **S (Survival):** Expected alpha net of ~7ΓÇô9 bps round-trip friction (cash MIS) or ~2.5ΓÇô3 bps (futures).
- **N (Novelty):** Distinct from retail TA, YouTube patterns, and textbook indicators.
- **C (Conviction):** Personal conviction (1 = waste of time, 5 = bet-the-house priority).

### C-Series (C1ΓÇôC42)

| ID | Strategy Name | P | T | S | N | C | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **C1** | Circuit-Lock Unlock Short | 2 | 2 | 1 | 3 | 1 | Killed: MIS shorts banned on circuit-locked scrips; 20% auction penalty tail risk |
| **C2** | Unfinished Parent Order | 4 | 5 | 4 | 4 | 4 | **TOP 10 (#5)** |
| **C3** | Cosmetic-News Pop Fade | 3 | 2 | 2 | 3 | 2 | Killed: NLP headline classification too noisy; retail small-cap manias run multi-day |
| **C4** | Liquidity-Vacuum Spike Fade | 3 | 5 | 3 | 2 | 3 | Merged into Champion 2 |
| **C5** | Put-Wall Short-Gamma Cascade | 3 | 3 | 3 | 3 | 2 | Killed: Restricted to weekly index expiry; fails daily operation mandate |
| **C6** | MIS Deadline Unwind | 4 | 4 | 3 | 3 | 4 | **TOP 10 (#6)** |
| **C7** | Supply-Floor Convergence | 3 | 2 | 3 | 4 | 2 | Killed: OFS/QIP deals occur infrequently (a few per quarter) |
| **C8** | Closing-Window Mark-up Unwind | 4 | 5 | 3 | 3 | 3.5 | **TOP 10 (#9)** |
| **C9** | Metaorder Completion Cliff | 4 | 4 | 4 | 4 | 4 | **TOP 10 (#4)** |
| **C10** | Bar-Clock Herd Fade | 2 | 5 | 1 | 2 | 1 | Killed: 15-minute candle micro-moves generate <10 bps, eaten by friction |
| **C11** | ETF Premium-to-Index Short | 2 | 2 | 1 | 2 | 1 | Killed: Indian thematic ETFs suffer wide bid-ask spreads and severe broker MIS bans |
| **C12** | Top-Gainers Attention Entry | 2 | 4 | 2 | 2 | 2 | Killed: Chaser momentum routinely overshoots and triggers intraday stops |
| **C13** | Disclosed-Seller Continuation | 3 | 2 | 2 | 3 | 2 | Killed: Bulk/block deals usually settle off-market or are completed in single prints |
| **C14** | Passive Deletion-Day Supply | 4 | 3 | 4 | 4 | 3 | Killed: Rebalance events occur quarterly and execute during the 15:00ΓÇô15:30 closing VWAP |
| **C15** | Governance-Flag Slow Bleed | 3 | 2 | 2 | 3 | 2 | Killed: Corporate filing timestamps are sparse and cause illiquid gap-downs |
| **C16** | Promoter-Group Contagion Laggard | 5 | 4 | 4 | 4 | 4.5 | **CHAMPION 3 (Merged)** |
| **C17** | Short-Covering Hangover | 3 | 4 | 2 | 2 | 2 | Killed: Next-day gap risk degrades intraday short Sharpe ratio |
| **C18** | Lock-In Expiry Overhang | 3 | 2 | 3 | 3 | 2 | Killed: Calendar-restricted event; high rate of broker-mandated short bans |
| **C19** | Speculative-Turnover Hangover | 5 | 5 | 5 | 5 | 5 | **CHAMPION 1 (Merged)** |
| **C20** | Exchange-Query Deflation | 2 | 2 | 2 | 3 | 2 | Killed: Boilerplate exchange queries rarely deflate retail momentum intraday |
| **C21** | ASM Leverage-Strip Day-One | 3 | 3 | 2 | 3 | 2 | Killed: Brokers immediately place ASM-stage entrants on the MIS short ban list |
| **C22** | Holding-Company Look-Through Lag | 2 | 3 | 2 | 3 | 2 | Killed: Holdco discounts are structurally unstable and can widen for months |
| **C23** | Futures-Absent Rally Fade | 4 | 4 | 4 | 4 | 4.5 | Merged into Champion 2 |
| **C24** | Block-Window Reference Marking | 2 | 2 | 2 | 3 | 1 | Killed: Afternoon block window operates under negotiated quotes; zero retail edge |
| **C25** | Silo Read-Through Laggard | 4 | 4 | 4 | 4 | 4 | Merged into Champion 3 |
| **C26** | Stale-News Pop Fade | 2 | 2 | 2 | 4 | 2 | Killed: High false-positive rate from news scraping without proprietary fundamental tags |
| **C27** | Latent Stop Shelf | 3 | 4 | 3 | 3 | 3 | Merged into Champion 1 |
| **C28** | Sales-Desk Downgrade Drip | 2 | 2 | 2 | 2 | 2 | Killed: Broker target cuts are leaked pre-market; intraday drift is negligible |
| **C29** | Short-Covering Exhaustion | 3 | 4 | 2 | 3 | 2 | Killed: Intraday OI reductions on 1-min bars fail to isolate covering from fresh buying |
| **C30** | Volume-Quota Exhaustion Rank | 4 | 5 | 4 | 3 | 4 | Merged into Champion 1 |
| **C31** | Tug-of-War Intraday Decay | 3 | 5 | 2 | 3 | 2 | Killed: Historical open-to-close bleed produces <15 bps gross, barely covering costs |
| **C32** | Same-Slot Persistence Short | 2 | 4 | 1 | 3 | 1 | Killed: Institutional time-slot persistence yields 3ΓÇô6 bps, completely eaten by STT/slippage |
| **C33** | Beta-and-Peer-Neutral Spike Fade | 3 | 4 | 3 | 3 | 3 | Merged into Champion 2 |
| **C34** | Breadth-Hollow Index Rally | 4 | 5 | 4 | 3 | 3.5 | **TOP 10 (#7)** |
| **C35** | Delivery-Cost-Basis Break-Even | 3 | 4 | 2 | 3 | 2 | Killed: Multi-day delivery basis calculations smear across wide price bands |
| **C36** | Stress-Day Thin-Name Catch-Up | 3 | 3 | 2 | 3 | 2 | Killed: Severe market stress occurs on <15% of annual sessions |
| **C37** | Retail-Cohort Burst Fade | 3 | 4 | 2 | 3 | 2 | Killed: Penny-stock retail cohorts frequently lock circuits, blocking short exits |
| **C38** | Stocks-to-Buy List Fade | 2 | 2 | 2 | 3 | 2 | Killed: Media tip sheets are uncodified and front-run by morning pre-open auctions |
| **C39** | Earnings-Quality Mismatch Fade | 4 | 3 | 4 | 4 | 3.5 | **TOP 10 (#8)** |
| **C40** | Beta-Chase Overshoot | 3 | 4 | 2 | 3 | 2 | Killed: Negative-beta short baskets suffer fatal drawdowns on persistent trend-up days |
| **C41** | Weight-Proportional Basket Overshoot | 2 | 3 | 1 | 4 | 1 | Killed: Index basket imbalances are neutralized in milliseconds by collocated HFTs |
| **C42** | Penultimate-Window Index Short | 3 | 5 | 3 | 2 | 3 | Merged into Top 10 #7 |

---

### G-Series (G1ΓÇôG49)

| ID | Strategy Name | P | T | S | N | C | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **G1** | Basis-Inversion Arb Dump | 5 | 4 | 5 | 5 | 5 | **CHAMPION 2 (Merged)** |
| **G2** | 0-DTE Call Gamma-Collapse | 1 | 2 | 1 | 3 | 1 | Killed: Factually invalid; Indian single-stock options do not have weekly/0-DTE expiries |
| **G3** | Dynamic-Band Cooling Exhaustion | 1 | 3 | 1 | 2 | 1 | Killed: Factually invalid; NSE F&O stocks do not halt for 15-minute cooling periods |
| **G4** | Peak-Margin Snapshot Cascade | 1 | 4 | 1 | 2 | 1 | Killed: Factually invalid; SEBI margin snapshots are randomized, not timed at 11:00 |
| **G5** | Sympathy-Beta Exhaustion Short | 3 | 4 | 3 | 3 | 3 | Merged into Champion 3 |
| **G6** | Euro Pre-Open Trap Unwind | 2 | 4 | 2 | 3 | 1 | Killed: European pre-open equity correlation to Indian single-stock drift is near zero |
| **G7** | Iceberg Churn Breakdown | 3 | 4 | 3 | 3 | 3 | Killed: Estimating hidden icebergs from 1-min bar skew yields massive false-positives |
| **G8** | Physical-Settlement Margin Dump | 3 | 3 | 3 | 4 | 2 | Killed: Occurs strictly once a month on monthly expiry Thursday; fails daily mandate |
| **G9** | Discounted-Block Arb Unload | 3 | 2 | 2 | 3 | 2 | Killed: Infrequent event; block-arbitrage spreads evaporate within opening 60 seconds |
| **G10** | Pledged-Promoter Covenant Flush | 3 | 2 | 2 | 4 | 2 | Killed: Debt covenant margin liquidations are rare distress events, not daily signals |
| **G11** | Sector-Titan Weight Cannibalization | 4 | 4 | 4 | 4 | 4 | Merged into Champion 3 |
| **G12** | Mid-Session Guidance Trap | 4 | 3 | 4 | 4 | 3.5 | Merged into Top 10 #8 |
| **G13** | Buy-Stop Sweep Exhaustion | 2 | 5 | 2 | 1 | 2 | Killed: Standard Turtle-Soup pattern lacking non-obvious microstructural edge |
| **G14** | Ban-Ceiling Leverage Paralysis | 2 | 2 | 2 | 4 | 2 | Killed: MWPL approach triggers violent short squeezes rather than predictable selloffs |
| **G15** | Index-Inclusion Front-Runner Flush | 3 | 2 | 3 | 4 | 2 | Killed: Rebalance cycles occur semi-annually; zero daily operational utility |
| **G16** | Cross-Exchange Expiry Delta Spillover | 2 | 3 | 2 | 3 | 1 | Killed: Cross-exchange BSE/NSE latency spreads are fully harvested by HFTs sub-second |
| **G17** | Earnings Con-Call Q&A Reversal | 3 | 1 | 3 | 4 | 2 | Killed: Concall audio transcripts lack standardized intraday timestamps for algo trading |
| **G18** | Arbitrage-Fund Cash Liquidation | 4 | 4 | 4 | 4 | 4 | Merged into Champion 2 |
| **G19** | Dispersion Basket Contagion Short | 3 | 4 | 3 | 4 | 3 | Merged into Champion 2 |
| **G20** | Post-Event Vol-Crush De-Hedging | 2 | 2 | 2 | 4 | 2 | Killed: Scheduled macro events (RBI/Budget) occur <10 times a year |
| **G21** | 09:20 Straddle Stop-Harvest Reversal | 3 | 4 | 2 | 3 | 2 | Killed: Heavily competed for by Tier-1 Indian HFTs; 1-min bars suffer adverse selection |
| **G22** | Daily-Expiry Delta Un-hedging | 2 | 3 | 2 | 2 | 2 | Killed: Dealers hedge index options via liquid index futures, not cash stock constituents |
| **G23** | VAR-Margin Step-Up Flush | 1 | 4 | 1 | 2 | 1 | Killed: Factually invalid; NSE Clearing does not impose an intraday 13:00 VAR margin step-up |
| **G24** | DII Buy-TWAP Exhaustion | 1 | 4 | 1 | 2 | 1 | Killed: Factually invalid; mutual funds do not truncate daily SIP execution at 11:15 IST |
| **G25** | T+1 Auction-Shortage Flush | 1 | 2 | 1 | 3 | 1 | Killed: Shortage auctions run in a segregated session and do not spill into continuous MIS books |
| **G26** | Tick-Size Queue Depletion | 2 | 1 | 1 | 3 | 1 | Killed: Queue-exhaustion scalping requires L3 tick data and sub-millisecond execution |
| **G27** | Strike-Pinning Fracture Dump | 3 | 3 | 3 | 3 | 2 | Killed: Vulnerable to severe short squeezes on unexpected market-on-close demand |
| **G28** | Conversion-Arb Cash Cascade | 3 | 2 | 2 | 4 | 2 | Killed: Put-call parity mispricings are closed by HFT collocated boxes in microseconds |
| **G29** | Algorithmic POV Throttle Cliff | 4 | 5 | 4 | 4 | 4 | Merged into Top 10 #4 |
| **G30** | Diurnal Vanna-Crush De-Hedging | 3 | 2 | 2 | 4 | 2 | Killed: Morning IV normalization is priced into derivative spreads, not cash drift |
| **G31** | 15:00 VWAP Front-Runner Flush | 3 | 5 | 3 | 4 | 3 | Killed: Extreme tail risk if an unannounced institutional MOC buy order lands at 15:00 |
| **G32** | Lottery-Call Delta Cliff Unwind | 2 | 2 | 2 | 4 | 2 | Killed: Factually invalid on single stocks (monthly only); weekly index options hedged with futures |
| **G33** | Institutional TWAP Collar Pause | 3 | 5 | 3 | 3 | 3 | Merged into Top 10 #4 |
| **G34** | Intraday MTM Square-Off Cascade | 4 | 4 | 3 | 3 | 3.5 | Merged into Top 10 #6 |
| **G35** | Opening AMO Queue Exhaustion | 1 | 5 | 1 | 2 | 1 | Killed: Factually invalid; AMOs execute in the 09:00ΓÇô09:08 pre-open call auction, not at 09:15 |
| **G36** | Inventory-Limit Reservation Flush | 3 | 4 | 2 | 3 | 2 | Killed: HFT market-maker inventory risk is managed cross-asset, not via spot stock dumping |
| **G37** | NDS-OM Yield-Shock De-Rating | 2 | 2 | 2 | 4 | 2 | Killed: Sovereign bond yield feeds are external; 1-minute correlation to spot equities is low |
| **G38** | Retail API Batch-Order Fade | 2 | 5 | 1 | 3 | 1 | Killed: 15-minute candle-close api bursts produce micro-wicks that fail to beat costs |
| **G39** | Cross-Sector Capital Rotation Drag | 3 | 4 | 3 | 4 | 3 | Merged into Champion 3 |
| **G40** | Stat-Arb Residual Variance Flush | 4 | 4 | 4 | 4 | 3.5 | Merged into Champion 2 |
| **G41** | Intraday Break-Even Relief Wall | 5 | 5 | 5 | 5 | 5 | Merged into Champion 1 |
| **G42** | Cross-Border ADR Parity Arbitrage | 2 | 2 | 2 | 3 | 2 | Killed: Restricted to ~5 Indian ADRs; spreads are vacuumed by offshore desks pre-open |
| **G43** | Charm-Deflation Delta Unwind | 2 | 2 | 2 | 4 | 2 | Killed: Indian single-stock options expire monthly; charm decay is imperceptible on daily scales |
| **G44** | Zero-Gamma Phase-Transition | 2 | 2 | 2 | 4 | 2 | Killed: Requires proprietary institutional gamma surface modeling; fails on 1-min OHLCV |
| **G45** | Sticky-Strike Gamma Saturation | 2 | 2 | 2 | 4 | 2 | Killed: Call-strike saturation carries fatal right-tail risk on genuine breakout momentum |
| **G46** | Adaptive-POV Cooldown Vacuum | 2 | 5 | 2 | 2 | 1 | Killed: Rebrands a standard candlestick upper rejection wick as an algo pause |
| **G47** | Pairs Stat-Arb De-Leveraging Flush | 4 | 4 | 4 | 4 | 3.5 | **TOP 10 (#10)** |
| **G48** | Index Implied-Correlation Drag | 3 | 4 | 3 | 4 | 3 | Merged into Champion 2 |
| **G49** | VPIN Toxicity Liquidity-Freeze | 2 | 1 | 1 | 3 | 1 | Killed: True VPIN requires millisecond tick trade sign classification; uncomputable on 1-min bars |

---

## 3. The Champion 3 (Bet-the-House Conviction)

### Champion 1: The Speculative Turnover Decoupling & Morning Trapped Long Flush
*(Upgraded & Merged: C19 + G41 + C30 + C27 | Conviction: 5/5)*

- **Counterparty & Trap:** Overleveraged retail MIS day-traders, telegram breakout chasers, and broker momentum scanners who pile into high-beta F&O stocks during the opening 45 minutes (09:15ΓÇô10:00 IST).
- **The Non-Obvious Mechanism:** Indian daily bhavcopy provides a crucial structural indicator: **Deliverable Quantity to Traded Quantity percentage**. When a stock surges >2.5% in the first 45 minutes on volume >3x baseline, but its historical delivery percentage sits in the bottom quintile (<18%), the rally is 85%+ funded by intraday MIS leverage (up to 5x margin). These traders have zero intent or financial capacity to take delivery. When the stock prints an intraday volume exhaustion marker (having traded >40% of its 20-day ADV by 10:30) and fails to set a new high for 15 consecutive minutes, the marginal retail buyer is completely exhausted. As the price rolls over and breaches the morning peak-volume VWAP, morning MIS longs sit on 1ΓÇô2% paper losses. Because of severe broker leverage limits and the behavioral disposition effect, any midday relief bounce back to their morning entry VWAP triggers a concentrated wave of panic "get-me-out-even" market sell orders. Once this break-even wall holds, broker stop-losses and automated MTM liquidations trigger a sustained, non-discretionary 60ΓÇô120 bps liquidation drift into the afternoon lull (11:30ΓÇô13:00 IST), easily clearing the 7ΓÇô9 bps round-trip friction.

### Champion 2: The Cash-Futures Dislocation & Prop Basis-Inversion Flush
*(Upgraded & Merged: G1 + C23 + G18 + G40 + C4 | Conviction: 5/5)*

- **Counterparty & Trap:** Institutional long hedgers, offshore desks, and quantitative cash-futures arbitrage desks operating in liquid single-stock F&O constituents.
- **The Non-Obvious Mechanism:** In the Indian market structure, when institutional participants (FPIs or domestic funds) execute urgent portfolio hedging or profit-taking, they initiate shorts in near-month stock futures due to lower transaction taxes (STT) and superior leverage. When aggressive institutional selling drives near-month stock futures to trade at an intraday **discount (negative basis / backwardation)** relative to spot cash while the cash equity is near session highs, it creates an acute structural dislocation. Quantitative cash-futures arbitrage desks (predominantly prop firms and HFTs) cannot let basis remain dislocated; they are mechanically triggered to execute reverse-arbitrage baskets by selling physical cash equity at market and buying the discounted futures. Because physical equity execution in size takes 15ΓÇô35 minutes of algorithmic slicing, this creates a sustained, price-insensitive supply overhang in the cash book that retail dip-buyers cannot absorb. Shorting the cash equity via MIS the moment futures discount widens past 15 bps (adjusted for cost of carry) on expanding volume exploits a deterministic multi-crore institutional liquidation wave, yielding 40ΓÇô80 bps of clean spot convergence.

### Champion 3: Conglomerate & Sector Beta-Decoupling Contagion Short
*(Upgraded & Merged: C16 + C25 + G11 + G5 + G39 | Conviction: 4.5/5)*

- **Counterparty & Trap:** Cross-asset institutional risk management systems, portfolio margin clearing desks, and retail traders operating in corporate silos.
- **The Non-Obvious Mechanism:** Indian corporate ecosystems are dominated by heavily cross-held promoter conglomerates (Tata, Adani, Reliance, Bajaj, Birla) and tight thematic sectors. Institutional lenders, FPI prime brokers, and domestic mutual funds enforce strict **promoter-group-level and sector-level gross exposure caps**. When an anchor bellwether of a group crashes >3.5% on heavy volume (e.g., due to an earnings miss, governance shock, or credit flag), institutional risk engines immediately trigger cross-collateral de-risking: to prevent margin breaches, algos systematically liquidate secondary and tertiary group constituents to cut aggregate group beta. Retail traders, however, analyze stocks in isolation, falsely perceiving the secondary peer as exhibiting "relative strength" and bidding it up. Once the leader's decline is confirmed and halts at the midday pause, the institutional risk-reduction baskets hit the secondary peer. Because the secondary stock has substantially thinner order-book depth, the delayed institutional supply punches straight through resting retail bids. Shorting the lagging group peer on its first 5-minute lower-high breakdown captures a rapid, high-probability 70ΓÇô140 bps catch-up cascade.

---

## 4. The Top 10 Ranked Strategies

1. **Speculative Turnover Decoupling & Trapped Long Flush (C19/G41/C30/C27) [Conviction: 5/5]:** Exploits NSE bhavcopy delivery-to-turnover decoupling combined with the behavioral break-even disposition supply wall of trapped morning MIS longs.
2. **Cash-Futures Dislocation & Prop Basis-Inversion Flush (G1/C23/G18/G40) [Conviction: 5/5]:** Monetizes non-discretionary physical spot selling by quantitative cash-futures arb desks when institutional futures shorting inverts the basis.
3. **Conglomerate & Sector Risk Contagion Laggard (C16/C25/G11/G5) [Conviction: 4.5/5]:** Front-runs multi-asset institutional portfolio risk limits that force programmatic basket liquidations across corporate group peers while retail buys false relative strength.
4. **Diurnal Volume-Drop Momentum Exhaustion (C9/G29/G33) [Conviction: 4/5]:** Exploits the deterministic 50ΓÇô60% volume plunge during the NSE midday lull (11:30ΓÇô12:45 IST), which mathematically forces institutional POV buy algorithms to scale back bids by half, stranding morning breakout chasers in an illiquid drift.
5. **Unfinished Parent Order Liquidation Drift (C2) [Conviction: 4/5]:** Capitalizes on multi-day institutional portfolio redemption slicing, identified by persistent volume-weighted close locations in the lower third of 5-minute candles across consecutive sessions.
6. **Post-14:15 MIS Deadline Acceleration Cascade (C6/G34) [Conviction: 4/5]:** Targets liquid F&O stocks that broke morning support; shorts the final, desperate liquidation wave between 14:15 and 15:00 as retail day-traders and broker RMS engines rush to square off intraday MIS margin longs before the 15:15 cutoff.
7. **Breadth-Hollow Index Momentum Exhaustion (C34/C42) [Conviction: 3.5/5]:** Shorts Nifty index futures when intraday index highs are manufactured by <30% constituent participation (concentrated heavyweight pinning), capitalizing on the inevitable late-session synthetic unwinds with minimal futures transaction friction (~2.5 bps).
8. **Earnings Operating EBITDA vs Headline PAT Mismatch Fade (C39/G12) [Conviction: 3.5/5]:** Fades mid-session or pre-open earnings pops where retail buys headline net profit beats, but institutional decomposition reveals collapsing core operating margins (EBITDA) or non-operating other-income inflation.
9. **Previous-Day Closing VWAP Ramp Exhaustion (C8) [Conviction: 3.5/5]:** Shorts morning opens in stocks artificially marked up by speculative or collateral-pledge buyers in the 15:00ΓÇô15:30 window, where lack of institutional follow-through at 09:30 leads to a swift mean-reversion to true fair value.
10. **Pairs Stat-Arb Multi-Sigma Divergence Unwind (G47) [Conviction: 3.5/5]:** Shorts the outperforming leg of highly cointegrated intra-sector stock pairs when spread divergence exceeds 3.0 standard deviations, exploiting automated de-leveraging mandates from institutional stat-arb funds.

---

## 5. The Ruthless Kill List (81 Eliminated Strategies)

- **C1:** Indian brokers strictly disallow MIS intraday shorting on upper-circuit locked names, exposing traders to catastrophic 20% buy-in delivery auction penalties.
- **C3:** Text scraping of news releases is brittle, and genuine retail small-cap speculative pops regularly extend into multi-session circuit runs.
- **C5:** Put-wall gamma cascades occur exclusively on index weekly expiries, failing the non-negotiable mandate for daily tradable operational signals.
- **C7:** Corporate OFS and QIP placements happen only a few times per quarter, making them useless for an everyday systematic trading algorithm.
- **C10:** 15-minute candle-close boundary order bursts produce 8ΓÇô12 bps micro-reversals that are entirely consumed by round-trip transaction costs.
- **C11:** Indian equity ETFs suffer from wide bid-ask spreads, severe tracking errors, and frequent broker-imposed intraday MIS short bans.
- **C12:** Broker top-gainers lists attract sustained retail chase volume that routinely triggers short-seller stop-losses before any reversal occurs.
- **C13:** Large institutional block sellers execute via off-market negotiated crossings rather than continuous open-market dumping.
- **C14:** Index rebalance deletion selling takes place quarterly and executes strictly inside the 15:00ΓÇô15:30 closing VWAP, after our required 15:15 exit.
- **C15:** Timestamped corporate governance filings cause immediate, illiquid opening gap-downs that offer negative risk-reward for intraday drift shorting.
- **C17:** Fading rallies with declining futures OI across sessions exposes the book to overnight gap risk that destroys intraday short Sharpe ratios.
- **C18:** Promoter and PE lock-in expirations are sparse calendar events, and freed scrips are routinely placed on broker intraday short ban lists.
- **C20:** Exchange clarification queries are standard regulatory boilerplate that fail to disrupt ongoing speculative retail momentum.
- **C21:** Stocks entering ASM frameworks are immediately blacklisted from intraday MIS leverage by major Indian brokerage risk engines.
- **C22:** Holding-company discounts are fundamentally volatile and can widen continuously for months without intraday mean-reversion.
- **C24:** The afternoon block window operates on negotiated reference prices and produces no exploitable continuous market drift.
- **C26:** TF-IDF text similarity algorithms fail to differentiate between cosmetic corporate notices and substantive operational updates.
- **C28:** Global brokerage target downgrades are leaked and priced in during the pre-open auction; intraday sales-desk drift is too weak to beat friction.
- **C29:** Intraday OI reductions during rallies are too noisy on 1-minute bars to reliably differentiate short-covering from aggressive long accumulation.
- **C31:** Persistent historical open-to-close bleeders generate <15 bps gross statistical drift, leaving zero net profit after STT, GST, and slippage.
- **C32:** Intraday half-hour time-slot persistence yields an average edge of 3ΓÇô5 bps, which is completely erased by statutory exchange fees.
- **C35:** Multi-day bhavcopy delivery VWAP calculations smear across wide price bands on volatile names, generating inaccurate break-even levels.
- **C36:** Macro market stress days occur in less than 15% of annual trading sessions, failing the daily trade frequency requirement.
- **C37:** Retail penny-stock cohorts frequently enter Trade-to-Trade (T2T) surveillance where intraday short selling is legally prohibited.
- **C38:** Scraped morning portal tip sheets suffer from high parsing latency and are heavily front-run by retail orders in the pre-open auction.
- **C40:** Shorting high-beta overshoot baskets creates extreme negative market beta, causing catastrophic account drawdowns on sustained trend-up days.
- **C41:** Index basket liquidity overshoots are arbitraged in sub-second timeframes by collocated HFTs, leaving no edge on 1-minute bars.
- **G2:** Factually invalid; Indian single-stock options expire strictly once a month, making daily 0-DTE call gamma collapse physically impossible.
- **G3:** Factually invalid; NSE F&O scrips operate with expanding dynamic price bands and never halt for 15-minute cooling periods.
- **G4:** Factually invalid; SEBI margin snapshots are randomized across clearing corporations and do not fire at an 11:00 clock mark.
- **G6:** European pre-open equity momentum exhibits statistically insignificant correlation with Indian single-stock intraday price action.
- **G7:** Identifying hidden iceberg orders from 1-minute candle close skew produces an unacceptably high rate of false-positive entries during accumulation.
- **G8:** Physical settlement delivery liquidations occur exclusively once a month on monthly expiry Thursday, failing the daily operation mandate.
- **G9:** Pre-market discounted blocks occur irregularly and their price dislocations are completely closed within the first 60 seconds of trading.
- **G10:** Pledged promoter covenant breaches are rare corporate distress crises that cannot support an everyday systematic trading strategy.
- **G13:** A repackaged retail Turtle Soup / false breakout pattern that lacks an identifiable, non-obvious structural institutional counterparty.
- **G14:** Stocks approaching the 95% MWPL threshold trigger violent short squeezes as borrow rates spike and shorts panic-cover.
- **G15:** Index inclusion rebalance dates happen only semi-annually, providing zero day-to-day tradeable sample size.
- **G16:** Collocated cross-exchange latency engines eliminate BSE/NSE delta arbitrage spreads in sub-millisecond windows.
- **G17:** Earnings concall audio streams lack standardized intraday timestamp feeds, making systematic algo backtesting impossible.
- **G19:** Dispersion basket contagion shorts suffer severe adverse selection when target stocks possess idiosyncratic corporate catalysts.
- **G20:** Post-event IV crush is confined to rare scheduled macro events (RBI MPC, Union Budget) and cannot sustain a daily trading book.
- **G21:** 09:20 straddle stop runs are heavily crowded by institutional HFTs, leaving 1-minute retail models vulnerable to adverse fills.
- **G22:** Derivative market makers hedge index options via liquid Nifty futures, not by selling cash-market equity constituents.
- **G23:** Factually invalid; NSE Clearing does not implement an intraday VAR margin step-up at 13:00 IST.
- **G24:** Factually invalid; domestic mutual funds execute equity SIPs via continuous VWAP algos rather than cutting execution at 11:15 IST.
- **G25:** NSE T+1 shortage auctions run in an isolated auction market session and do not interact with continuous cash MIS order books.
- **G26:** Sub-Γé╣100 tick-size queue exhaustion requires Level 3 tick-by-tick order-book feeds that cannot be executed on 1-minute OHLCV data.
- **G27:** Strike pinning breakdowns are vulnerable to violent late-session short squeezes on unexpected market-on-close demand surges.
- **G28:** Conversion-arbitrage mispricings on Indian single stocks are captured in microseconds by institutional box-spread algorithms.
- **G30:** Diurnal morning IV crush is absorbed in opening option bid-ask spreads and does not translate into directional equity spot drift.
- **G31:** Trapped closing front-runners face lethal right-tail risk if a large institutional market-on-close buy order prints at 15:00.
- **G32:** Factually invalid; single-stock options do not have 0-DTE weekly expiries, and index lottery options are hedged using futures contracts.
- **G35:** Factually invalid; After Market Orders (AMOs) execute during the 09:00ΓÇô09:08 pre-open call auction, leaving zero unpriced volume at 09:15.
- **G36:** HFT market-maker inventory risk is managed across multi-asset derivative books and does not produce predictable single-stock spot dumping.
- **G37:** NDS-OM sovereign bond yield feeds are unavailable in standard retail feeds and exhibit weak 1-minute correlation with spot equities.
- **G38:** Retail algo 15-minute candle breakout bursts produce micro-wicks that are far too narrow to overcome the 8 bps round-trip friction hurdle.
- **G42:** Indian ADRs are limited to a handful of mega-caps where ADR-NSE parity spreads are closed by offshore desks prior to market open.
- **G43:** Indian single-stock options expire monthly; charm delta decay is mathematically imperceptible on an intraday timeframe.
- **G44:** Calculating precise intraday zero-gamma transition levels requires institutional implied volatility surface feeds unavailable on 1-min OHLCV.
- **G45:** Heavy call-strike saturation trades suffer fatal blowups when underlying spot prices break out into genuine trend-day expansions.
- **G46:** Rebrands a conventional candlestick upper rejection wick as an "algorithmic pause" without any verifiable structural mechanism.
- **G48:** Single-stock dispersion arbitrage requires simultaneously trading options across the entire index, exceeding retail operational capacity.
- **G49:** True VPIN order-flow toxicity requires millisecond tick trade sign classification, which is mathematically impossible to compute on 1-minute bars.

### Claude (cull round 2)
# Round 3 (Claude): cull, scores and champions

I assume costs of about 8 bp round trip for cash MIS and about 3 bp for Nifty futures. Costs, exchange rules and expiry days are from memory, so verify them (Nifty weekly expiry is Tuesday, I believe).

## Where I disagree with Gemini's round 2

1. **Its POV-throttle idea survives its own refutation.** It correctly says a POV algo keeps its 10ΓÇô15% share when volume halves, then keeps the idea at #4 anyway, still claiming the bids are "mathematically halved". Both statements can't be true. The idea has no mechanism, only an observable (volume surge with no price progress). It stays as a weak pattern test.
2. **Its basis-inversion champion contradicts itself and invents its numbers.**
   - It says arb mutual funds don't dump cash, then relies on "prop arb desks" doing the same thing.
   - A reverse-carry unwind sells cash and buys futures together, so nothing forces cash down.
   - Stock futures at a discount to cash are rare given the carry.
   - "40ΓÇô80 bp convergence" and "15 bp discount" are made up.
   - The data may also not include futures at all.
3. **Its Champion 1 stacks too many conditions on invented numbers.**
   - It uses "85%+ MIS-funded", ">40% of ADV by 10:30" and "60ΓÇô120 bp drift".
   - Five conjunctive filters leave a tiny sample.
   - Same-day delivery % is only known after the close. Only prior-day or own-history delivery % is usable.
   - Break-even supply sits at the entry VWAP of traders we can't observe.
4. **It uses made-up magnitudes as kill reasons.** It did this in round 1 and repeated it here (C31 "<15 bp", C32 "3ΓÇô6 bp"). Kill on mechanism, arithmetic or data instead.
5. **Its Champion 3 asserts a mechanism that doesn't exist.** "Risk engines cross-collateral de-risk group peers" is not a known process, and "70ΓÇô140 bp catch-up" is invented. The documented effect is information diffusion across siloed coverage (Hou; CohenΓÇôFrazzini). The idea survives on that basis, not Gemini's.
6. **I take two of its points.**
   - Retail-heavy small caps are often MIS-blocked, so I restrict everything to F&O names, roughly 180ΓÇô200 stocks.
   - My own round-1 champion, the Square-Off Shelf, should be downgraded, along with G41. The signed-volume map is crude, MIS positions are a small share of volume in large F&O names, and the supply can't be tied to real traders.
7. **A citation in the pool is backwards (from memory).**
   - C4 cites CampbellΓÇôGrossmanΓÇôWang as a low-volume-reversal result.
   - As I recall, they find that price moves on high volume reverse more, and low-volume moves tend to persist.
   - So test the volume sign both ways rather than assuming it.
8. **A caveat for anything built on prior-day signals.** A lot of reversal accrues in the overnight gap, which an intraday-only book can't capture. Test openΓåÆclose only, with no gap credit.

## Scores for all 91 ideas

P = plausibility, T = testability, S = survives costs, N = novelty (each 1ΓÇô5). ΓåÆ means the idea is in my top 10 or folded into that rank.

### C-series

| ID | P | T | S | N | Fate |
|---|---|---|---|---|---|
| C1 | 2 | 2 | 1 | 3 | Kill: unshortable, auction close-out tail |
| C2 | 3 | 5 | 2 | 3 | ΓåÆ#5 |
| C3 | 2 | 2 | 2 | 3 | Kill: headline classifier, sparse |
| C4 | 3 | 5 | 3 | 2 | ΓåÆ#2 (test volume sign both ways) |
| C5 | 3 | 3 | 4 | 3 | ΓåÆ#10 (index only) |
| C6 | 3 | 4 | 2 | 2 | ΓåÆ#6 |
| C7 | 3 | 2 | 3 | 3 | Kill: a few events per quarter |
| C8 | 3 | 5 | 3 | 3 | ΓåÆ#1 as a feature |
| C9 | 2 | 2 | 3 | 3 | Kill: order completion isn't observable in OHLCV |
| C10 | 2 | 5 | 1 | 2 | Kill: candle-boundary micro-moves |
| C11 | 2 | 2 | 1 | 2 | Kill: ETF spreads, MIS limits |
| C12 | 2 | 4 | 2 | 2 | Kill: list-entry trigger is weak |
| C13 | 2 | 2 | 2 | 3 | Kill: sparse, needs block files |
| C14 | 3 | 3 | 3 | 3 | Kill: flow lands after the 15:15 exit, quarterly |
| C15 | 3 | 2 | 2 | 2 | Kill: rare, gaps |
| C16 | 3 | 3 | 3 | 3 | ΓåÆ#3 |
| C17 | 3 | 4 | 2 | 2 | ΓåÆ#1 as a feature |
| C18 | 2 | 2 | 3 | 2 | Kill: sparse calendar |
| C19 | 4 | 4 | 3 | 3 | ΓåÆ#1 |
| C20 | 2 | 1 | 2 | 3 | Kill: needs filings feed, rare |
| C21 | 3 | 3 | 2 | 2 | Kill: ASM names are MIS-blocked |
| C22 | 2 | 3 | 2 | 3 | Kill: few events, drifting discount |
| C23 | 3 | 3 | 3 | 3 | ΓåÆ#2 as a filter (only if futures volume exists) |
| C24 | 2 | 2 | 2 | 3 | Kill: unverified window |
| C25 | 3 | 3 | 3 | 3 | ΓåÆ#3 |
| C26 | 2 | 2 | 2 | 3 | Kill: text-matching noise |
| C27 | 3 | 5 | 3 | 3 | ΓåÆ#6 |
| C28 | 2 | 1 | 2 | 2 | Kill: no data |
| C29 | 2 | 2 | 2 | 3 | Kill: no intraday OI |
| C30 | 3 | 5 | 3 | 2 | ΓåÆ#8 |
| C31 | 3 | 5 | 2 | 3 | ΓåÆ#1 as a feature |
| C32 | 2 | 4 | 1 | 3 | Kill: slot drift is small against slot ╧â, and the effect is index-level |
| C33 | 4 | 5 | 3 | 2 | ΓåÆ#2 |
| C34 | 3 | 4 | 4 | 3 | ΓåÆ#4 |
| C35 | 3 | 4 | 2 | 3 | ΓåÆ#6 as a feature |
| C36 | 3 | 3 | 2 | 2 | Kill: ~15% of days |
| C37 | 3 | 4 | 2 | 3 | ΓåÆ#1 as a feature (F&O names only) |
| C38 | 2 | 1 | 2 | 3 | Kill: scraping |
| C39 | 3 | 2 | 3 | 3 | ΓåÆ#7 |
| C40 | 2 | 4 | 2 | 3 | Kill: negative-beta basket |
| C41 | 2 | 3 | 1 | 3 | Kill: sub-minute arb |
| C42 | 3 | 5 | 4 | 2 | ΓåÆ#4 |

### G-series

| ID | P | T | S | N | Fate |
|---|---|---|---|---|---|
| G1 | 3 | 3 | 3 | 3 | ΓåÆ#9 (only if futures bars exist) |
| G2 | 1 | 2 | 1 | 3 | Kill: no 0-DTE on single stocks |
| G3 | 1 | 3 | 1 | 2 | Kill: premise wrong |
| G4 | 1 | 4 | 1 | 2 | Kill: premise unverifiable |
| G5 | 3 | 4 | 3 | 3 | ΓåÆ#3 |
| G6 | 1 | 4 | 1 | 2 | Kill |
| G7 | 3 | 4 | 3 | 2 | ΓåÆ#8 |
| G8 | 3 | 2 | 3 | 4 | Kill: monthly only |
| G9 | 2 | 2 | 2 | 3 | Kill: rare |
| G10 | 2 | 2 | 2 | 3 | Kill: rare, needs pledge data |
| G11 | 3 | 4 | 3 | 3 | ΓåÆ#3 |
| G12 | 3 | 2 | 3 | 3 | ΓåÆ#7 |
| G13 | 2 | 5 | 2 | 1 | Kill: turtle soup |
| G14 | 2 | 1 | 2 | 3 | Kill: no intraday MWPL |
| G15 | 2 | 2 | 2 | 3 | Kill: semi-annual |
| G16 | 2 | 3 | 2 | 2 | Kill |
| G17 | 2 | 1 | 2 | 3 | Kill: no timestamps |
| G18 | 2 | 3 | 2 | 3 | Kill: arb legs are hedged pairs. Folded into #9 |
| G19 | 3 | 4 | 3 | 3 | ΓåÆ#2 (drop the Nifty-break arm) |
| G20 | 2 | 2 | 2 | 3 | Kill: rare events |
| G21 | 2 | 3 | 1 | 3 | Kill: HFT-crowded |
| G22 | 2 | 3 | 2 | 2 | Kill: index dealers hedge with futures |
| G23 | 1 | 4 | 1 | 2 | Kill: premise unverified |
| G24 | 1 | 4 | 1 | 2 | Kill: premise unverified |
| G25 | 1 | 2 | 1 | 3 | Kill: separate auction session |
| G26 | 2 | 1 | 1 | 3 | Kill: needs L3 data |
| G27 | 3 | 3 | 4 | 3 | ΓåÆ#10 |
| G28 | 2 | 1 | 2 | 3 | Kill: latency game |
| G29 | 2 | 5 | 2 | 3 | ΓåÆ#8 (observable only, mechanism is wrong) |
| G30 | 2 | 1 | 2 | 3 | Kill: no IV data |
| G31 | 2 | 5 | 2 | 3 | Kill: no MOC mechanism |
| G32 | 2 | 2 | 2 | 3 | Kill: monthly. Only the index arm survives, in #10 |
| G33 | 2 | 5 | 2 | 2 | Kill: invented collar |
| G34 | 3 | 4 | 3 | 3 | ΓåÆ#6 |
| G35 | 1 | 5 | 1 | 2 | Kill: premise unverified |
| G36 | 2 | 4 | 2 | 2 | Kill: inventory story unfounded |
| G37 | 2 | 1 | 1 | 3 | Kill: no feed |
| G38 | 2 | 5 | 1 | 2 | Kill: same as C10 |
| G39 | 3 | 4 | 2 | 3 | ΓåÆ#3 |
| G40 | 3 | 4 | 3 | 2 | ΓåÆ#2 |
| G41 | 3 | 5 | 3 | 3 | ΓåÆ#6 (downgraded from my round 1) |
| G42 | 2 | 2 | 2 | 2 | Kill: a handful of ADRs |
| G43 | 2 | 1 | 2 | 3 | Kill: monthly options, no data |
| G44 | 2 | 1 | 2 | 3 | Kill: no IV-surface data |
| G45 | 2 | 1 | 2 | 3 | Kill: no option data |
| G46 | 2 | 5 | 2 | 1 | Kill: wick pattern |
| G47 | 3 | 4 | 3 | 2 | ΓåÆ#2 (short leg only) |
| G48 | 3 | 4 | 3 | 3 | ΓåÆ#2 |
| G49 | 2 | 2 | 1 | 3 | Kill: VPIN power is volume-mechanical |

## My three champions

**1. Retail-Crowding Daily Rank (C19 + C31 + C8 + C17 + C37), conviction 4/5.**
- **Counterparty:** MIS-funded retail and operator churn that chases yesterday's winners.
- **Score:** each morning, rank F&O names on a composite of five features.
  - Prior-day return.
  - Prior-day volume.
  - Prior-day delivery % against the stock's own 60-day history (low = churn).
  - Turnover against free float.
  - Whether the prior day's gain came in the 15:00ΓÇô15:30 window.
  - An optional stock-specific openΓåÆclose t-stat (LouΓÇôPolkΓÇôSkouras).
- **Trade:** short the top 3ΓÇô5 after the open settles. This trades every day by construction, which fixes the sparsity that kills most of the pool.
- **Why the other side stays wrong:** margin products set a hard exit deadline, and the fresh buyers are the same crowd.
- **Caveat:** the overnight gap may capture most of the reversal, so I'm testing openΓåÆclose only.

**2. Unconfirmed-Pop Fade (C4 + C33 + C23 + G19 + G40 + G47 + G48), conviction 4/5.**
- **Counterparty:** market-order liquidity takers, such as retail and small prop, who push a stock out of line with its beta and sector. Liquidity providers who absorb it are paid when it reverts (Nagel; AvellanedaΓÇôLee).
- **Trigger:** a move of at least 3╧â against the stock's own time-of-day range, after the first 45 minutes. It must be unexplained by beta ├ù Nifty and by its sector basket, with no filing in the prior 2 hours.
- **Volume sign:** test high-volume and low-volume versions separately, since the pool's citation looks backwards.
- **Role of the other ideas:** the stat-arb and dispersion ideas matter only as sources of the residual definition. Their invented mechanisms are dropped.

**3. Downside Peer-Lag (C25 + C16 + G5 + G11 + G39), conviction 3/5.**
- **Counterparty:** holders of the follower stock who read "only the leader got hit".
- **Mechanism:** coverage is siloed by ticker, so repricing diffuses over minutes to hours in the less-covered names.
- **Short-only use:** it trades only leader-down events, which is half of the documented effect, but still frequent across about 30 sector clusters.
- **Followers:** use the lower-ADV half of F&O names, since large-cap lags close in seconds.
- **Peer map:** built from rolling correlation plus a sector tag.

## Top 10, ranked

1. **Retail-Crowding Daily Rank** (C19/C31/C8/C17/C37). Conviction 4.
2. **Unconfirmed-Pop Fade** (C4/C33/C23/G19/G40/G47/G48). Conviction 4.
3. **Downside Peer-Lag** (C25/C16/G5/G11/G39). Conviction 3.
4. **Breadth-Hollow Nifty Futures Short** (C34/C42). Conviction 3. The cost is about 3 bp, so small edges can survive. It needs 50 constituent bar series, and the sign of dealer flow is unknown, so test both.
5. **Unfinished Parent Order** (C2). Conviction 3. A cross-sectional rank on signed-volume persistence. Thin net edge expected.
6. **Break-Even / Square-Off Shelf** (C6/G34/G41/C27/C35). Conviction 2. Kept as a volume-at-price feature test, not a thesis.
7. **Earnings-Quality Mismatch** (C39/G12). Conviction 2. Event-based, in season only (~40% of days), and needs structured results data. Second wave.
8. **Volume Absorption Near Highs** (G7/C30/G29). Conviction 2. A known Wyckoff-style pattern, flagged as such.
9. **Basis-Shock Short** (G1/G18). Conviction 2. Only if futures 1-min bars are available.
10. **Index Expiry Strike-Break Short** (C5/G27/G32). Conviction 2. It fires about weekly, so the sample is small. Run it as a side book.

## Order of experiments

1. **Null baseline first.** Random openΓåÆclose shorts in the F&O universe should lose to drift plus about 8 bp. Every idea must beat this same-time, same-stock random-short baseline by more than costs.
2. **Feature study before strategies.** Compute information coefficients and decile spreads for the #1 and #2 features across 3+ years. Freeze one parameter set per idea before looking at results.
3. **Report net bp per trade** with day-clustered t-stats, the sign by year, and a rerun at 1.5├ù slippage. With about 10 hypotheses, require t ΓëÑ 3.
4. **Expect most of the pool to die.** I'd be surprised if more than one or two of these survive net of costs, and that is a fine outcome.

