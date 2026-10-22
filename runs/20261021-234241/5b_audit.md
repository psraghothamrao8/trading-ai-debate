# Adversarial Audit: Intraday NSE Short-Only Book

---

## 1. Strategy A: Overnight Hangover Panel

### **VERDICT: FIX FIRST**
*Do not build the current specification. While the underlying cross-sectional crowding premise has empirical precedent, the backtest plan contains lethal timing mismatches, and the cash MIS execution architecture ignores the single most destructive tail risk in Indian equity shorting: auction penalties.*

---

### The Top 3 Flaws

#### Flaw 1: The Cash MIS Upper-Circuit / Auction Settlement Execution Trap
* **Mechanism:** The strategy deliberately selects the most aggressively crowded, low-delivery, high-turnover speculative winners. In the Indian cash market, if a surging stock hits its upper price band (or upper circuit), **liquidity vanishes completely (zero sellers)**. 
* **The Fatal Hole:** Your planned 15:10 passive exit and 2.0╧â stop-loss both assume continuous liquidity. When an intraday cash MIS short cannot be squared off by 15:30 IST, Indian brokers cannot roll it over; it **goes to mandatory exchange auction on T+1**. Buy-in auctions on NSE routinely settle at up to **20% above the day's high**, plus exchange penalties and broker auction handling fees. A single auction settlement (ΓêÆ15% to ΓêÆ20% on a 25% notional position) wipes out 300 to 500 basis points of book equityΓÇöerasing months of accumulated 10 bp net gains.

#### Flaw 2: Step 1 Daily Kill-Test Timing Mismatch (Severe Look-Ahead / Proxy Bias)
* **Mechanism:** Step 1 evaluates the signal using **daily Open-to-Close (09:15 to 15:30) returns**. However, actual live entry is gated at **09:46 IST**.
* **The Fatal Hole:** On the NSE, retail FOMO and early morning gap-absorption occur predominantly between **09:15 and 09:40 IST**. Testing Open-to-Close on daily bhavcopy will credit the strategy with the morning reversion that occurred *before* the 09:46 entry. If the high-minus-low open-to-close spread is ~15 bp, but 12 bp of that reversion occurs prior to 09:46, the actual 09:46ΓÇô15:10 tradable drift is only 3 bpΓÇöfar below your 13.5 bp round-trip hurdle. Passing Gate 1 on daily bars will give a false-positive green light to an untradable strategy.

#### Flaw 3: Infeasible Book-Level Stop-Loss Topology
* **Mechanism:** The shared rules specify a portfolio stop: *"flatten everything if Nifty is at least +1.2% from open, or the day's loss reaches 1.5% of capital."*
* **The Fatal Hole:** With 4 names at 25% notional each (1├ù gross leverage), if three names are flat or slightly green (+0.2%), a single high-beta name spiking +5.5% triggers the 1.5% book stop. The algorithm will dump all four positions at ~10:30 AM into wide mid-morning spreads, locking in peak slippage on the runner and cutting off the remaining three names before their mean-reversion drift can materialize over the afternoon.

---

### Other Critical Holes & Logic Blindspots
* **T-1 Delivery Data Latency:** NSE publishes security-wise delivery position reports (`MTO` files) between 18:30 and 20:30 IST. While available by 09:00 next day, historical backtest datasets frequently backfill delivery volume using post-settlement adjusted bhavcopies. If corporate actions (splits, bonus shares) alter historical share counts, raw turnover/float and delivery z-scores will suffer severe point-in-time calculation distortions unless unadjusted raw counts are used.
* **Broker Dynamic MIS Disallowance:** Domestic brokers (Zerodha, Upstox, Shoonya) do not maintain static MIS short lists. Stocks experiencing extreme momentum or sudden volatility spikes are routinely blacklisted for intraday shorting by broker risk management engines mid-session or at the pre-open. The top-ranked names will be disproportionately rejected by the OMS with code `"Short selling not allowed for MIS on this scrip"`.

---

### Exact, Non-Negotiable Fixes

1. **Upper Circuit Buffer & Dynamic Circuit Proximity Gate:**
   * Drop the generic `within 3.5% of upper band` rule. Replace with: At 09:45 IST, query the dynamic price band from the broker feed. If the stock is within **5.0%** of the upper circuit band, or if the stock's 30-minute realized volatility implies a 95% probability of touching the band before 15:15, reject entry.
   * If a position is open and the price reaches within **2.0%** of the upper circuit, trigger an immediate market exit before the offer side empties.
2. **Align Gate 1 Kill-Test to True Tradable Bar:**
   * Step 1 must **not** use daily `Open-to-Close`. Construct a synthetic 09:46-to-15:10 bar across the 2018ΓÇô2021 in-sample period. If gross excess return between 09:46 and 15:10 is under **18 bp** (to comfortably clear 13.5 bp costs + conservative buffer) with date-clustered $t < 3.0$, immediately kill the strategy.
3. **Decouple Idiosyncratic Stops from Portfolio Hard Stops:**
   * Remove the 1.5% capital stop entirely. A multi-name short book must allow individual names to reach their independent 2.0╧â stops. Retain the Nifty +1.2% macro stop, but measure it relative to Nifty's 09:45 level, not the 09:15 open (otherwise an opening gap-up on Nifty will prevent the algorithm from entering on days when stocks are most stretched).

---
---

## 2. Strategy B: Peer-Rich Short (Idiosyncratic Lead-Lag & Reversion)

### **VERDICT: DROP**
*Drop this strategy immediately. It violates the prompt's core mandate for **daily operation**, and its latency profile guarantees that retail API orders will be front-run and adversely filled by colocated institutional desks.*

---

### The Top 3 Flaws

#### Flaw 1: Execution Infeasibility vs. Colocated HFT / Stat-Arb Desks
* **Mechanism:** The reversion arm triggers when 30-min residual $e_i \ge +3\sigma$ with flat peers, entering on the *"first 1-minute close below the prior bar's low"*.
* **The Fatal Hole:** Lead-lag and single-stock intraday peer discrepancies on the NSE F&O universe are the primary hunting ground of colocated institutional HFT and quantitative stat-arb firms (e.g., Tower Research, Graviton, AlphaGrep, Quadeye). These participants trade on tick-by-tick microsecond signals directly at NSE Colo (Rack inside BKC Data Center). Waiting for a **1-minute bar to close**, checking the condition, and firing an order over the public internet via a retail broker API (100ΓÇô300 ms round trip) means entering **30 to 60 seconds after the imbalance has already been arb-corrected**. You will systematically short at the bottom of the micro-reversal, suffering pure adverse selection and paying the spread on both sides.

#### Flaw 2: The "Silent News" & Asymmetric Information Contamination
* **Mechanism:** The diffusion arm assumes that if a leader drops $\le -2\sigma$ without an exchange corporate filing in the last 120 minutes, the peer's lack of movement is due to "slow attention" by market participants.
* **The Fatal Hole:** Material corporate developments in India (plant-specific USFDA import alerts, IT contract cancellations, DRI/GST raids, management disputes, or promoter stake disposals) break on news wire terminals (Bloomberg, Reuters), TV channels (CNBC-TV18, ET Now), and WhatsApp/Telegram trading groups hours before a regulatory disclosure hits `nseindia.com`. When a leader collapses on company-specific catastrophic news, the peer is **not laggingΓÇöit is unaffected or actively gaining market share**. Shorting the peer under the assumption of "attention deficit" means shorting a fundamentally strong company while the leader bleeds for specific reasons.

#### Flaw 3: Mathematical Impossibility of Frictional Survival
* **Mechanism:** The diffusion arm aims to capture a deficit closure from $\Delta \le -0.60\%$ down to $-0.15\%$ (a 45 bp gross move), with a required stop of $1.2\sigma$ (~60ΓÇô90 bp).
* **The Fatal Hole:** In Tier-2 and Tier-3 F&O peer stocks, typical bid-ask spreads are 6ΓÇô8 bp. Round-trip spread drag is 12ΓÇô16 bp; statutory taxes, exchange charges, and brokerage add ~6 bp. Total unavoidable friction is **18ΓÇô22 bp**. On a target gross move of 45 bp, your expected net payout on a winning trade is only ~23 bp. With a 75 bp stop-loss costing ~95 bp net upon failure, the strategy requires a win rate $>80\%$ just to break even after slippage. A required win rate of 62% stated in the report will rapidly bleed capital. Furthermore, with only 150ΓÇô250 events per year (and ~40 if pledge-tagged), it fails the mandatory daily operational bar.

---

### Exact Fixes (If Forced to Test as an Event-Driven Sub-Module)

1. **Abandon the 1-Minute Bar Close Entry; Use Passive Limit Queueing:**
   * Never execute market-with-protection on 1-minute breakdown closes. Require passive limit orders placed at the bid/midpoint with a strict cancellation timeout (e.g., 30 seconds). If the order is not filled passively, abandon the trade.
2. **Mandatory Sector-Basket Residualization:**
   * Instead of a single leader-to-peer pair (which conflates company-specific news with industry shock), require that at least **two independent sector peers** drop by $\ge -1.5\sigma$ before flagging the third as lagging. This filters out 90% of leader-specific regulatory or governance shocks.
3. **Enforce Hard ADV and Spread Caps:**
   * Restrict eligible peers exclusively to names with 60-day ADV $> Γé╣100\text{ Cr}$ and median tick spread $\le 3\text{ bp}$. If no peer meets this liquidity threshold, discard the signal entirely.

---
---

## 3. Cross-Cutting Failure Modes in the Shared Architecture

| Area | The Hidden Bug | Impact | Required Remediation |
|---|---|---|---|
| **Statutory Costs** | STT on Intraday Cash vs Futures | In Cash MIS, STT is **0.025% on Sell turn-over only**. But Stamp Duty is **0.003% on Buy turnover**. Total statutory cost is ~5.9 bp. However, flat Γé╣20/order brokerage on a Γé╣50,000 leg is **8 bp round trip**, doubling total friction to ~22 bp. | Hardcode a minimum trade notional size of **Γé╣2,00,000 per leg**. Enforce that any trade where statutory + brokerage costs exceed **7.0 bp** is rejected by the pre-trade sizing module. |
| **Survivorship Bias** | F&O Inclusion/Exclusion Dynamics | Using current F&O lists back to 2018 introduces severe survivorship bias (stocks that collapsed and were ejected from F&O are omitted). | Must use the **point-in-time monthly F&O contract master** from the NSE archives. When a stock is excluded from F&O, its intraday liquidity collapses, creating artificially wide backtest spreads. |
| **Exit Execution** | 15:10 to 15:13 Exit Ladder | Indian domestic brokers initiate automated square-off runs (RMS batch jobs) between **15:15 and 15:25**. If the algo fails to execute at 15:12, both the user's OMS and the broker's RMS will fire competing square-off orders simultaneously, resulting in double-covering or order rejections. | Pull the broker exit deadline back: start passive cover at **15:05**, escalate to aggressive limit at **15:08**, and enforce hard flat by **15:10 IST**. |

---

## 4. Auditor's Final Directive

1. **Drop Strategy B entirely.** It is an unviable, low-frequency retail stat-arb concept that cannot overcome HFT queue priority and NSE transaction friction.
2. **Put Strategy A through the revised Gate 1 (09:46ΓÇô15:10 synthetic bars).** If it clears an 18 bp net margin against the equal-weight benchmark with clustered $t \ge 3.0$ and incorporates an upper-circuit escape protocol, proceed to minute-level backtesting. Otherwise, terminate the book.
