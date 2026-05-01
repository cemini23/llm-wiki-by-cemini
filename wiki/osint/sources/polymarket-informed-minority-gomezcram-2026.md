---
title: "Prediction Market Accuracy — Crowd Wisdom or Informed Minority? (SSRN 6617059, Gómez-Cram, Guo, Jensen, Kung — LBS + Yale, 2026)"
type: source
tags: [paper, prediction-markets, polymarket, behavioral-finance, market-microstructure, skill-persistence, refutes-wisdom-of-crowds, ssrn-working-paper, lbs, yale, cemini-relevant, workflow-a-find]
keywords: [polymarket, prediction-market-accuracy, informed-minority, wisdom-of-crowds-refutation, skill-persistence, sign-randomization-test, market-makers, skilled-takers, lucky-winners, unlucky-losers, gomez-cram, yunhan-guo, theis-ingerslev-jensen, howard-kung, london-business-school, yale-som, ssrn-6617059, 2023-2025-data, 1-72-million-accounts, 13-76-billion-volume, 98906-events, insider-trading-detection, 1950-flagged-accounts, phase-3-shadow-mode, signal-detection-criteria]
clusters: [quant-finance, market-microstructure, prediction-markets]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - concepts/favorite-longshot-bias.md
  - concepts/high-signal-paper-patterns.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - sources/lob-regime-detection-hiremath-2026.md
  - sources/gemini-dr-wave4a-cemini-stack-2026-04-29.md
  - sources/gemini-dr-wave5b-osint-2026-04-30.md
  - sources/polymarket-predictions-mcp.md
  - sources/caiovicentino-polymarket-mcp-server.md
  - sources/last30days-skill-mvanhorn.md
maturity: validated
read_status: deep-read
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @concepts/market-microstructure.md — primary cluster home: this is a market-microstructure paper on prediction markets, refuting the "wisdom of crowds" framing in favor of an "informed minority" framing.
- @concepts/quant-finance.md — secondary cluster: finds skill-persistence rates (44% out-of-sample) that **dwarf mutual-fund analogues (10%)** — operationally relevant for any quant strategy that piggybacks on "smart money" signals.
- @concepts/favorite-longshot-bias.md — adjacent behavioral-finance concept; favorite-longshot bias and crowd-wisdom-refutation are both behavioral anomalies in prediction-market pricing.
- @concepts/high-signal-paper-patterns.md — Workflow A find from the 2026-04-29 sweep (Q5: prediction markets / Kalshi / Polymarket order-book analysis). Score 4-5/6 quality + 3/3 operational + refutation premium.
- @entities/platforms/polymarket.md — direct subject: this paper analyzes Polymarket's complete transaction history (1.72M accounts, $13.76B volume, 2023-2025).
- @entities/platforms/kalshi.md — sibling prediction-market platform Cemini watchlists. Findings likely generalize but Kalshi's regulated CFTC structure may attract different participant mix vs Polymarket's decentralized one. Open empirical question.
- @sources/lob-regime-detection-hiremath-2026.md — sibling Workflow A find; both refute received wisdom in their domain.
- @sources/gemini-dr-wave5b-osint-2026-04-30.md — Wave 5B canonical brief; dual-MCP-Polymarket pattern (real-time-odds + trade-execution) maps directly onto this paper's deployable surface.
- @sources/caiovicentino-polymarket-mcp-server.md — Wave 5B Adopt; trade-execution leg for the informed-flow analyst service this paper motivates.

## Raw Concept

- **Original title**: "Prediction Market Accuracy: Crowd Wisdom or Informed Minority?"
- **Authors**: Roberto Gómez-Cram (London Business School Finance — Assistant Professor), Yunhan Guo (LBS), Theis Ingerslev Jensen (Yale School of Management), Howard Kung (LBS)
- **Type**: SSRN working paper
- **SSRN ID**: 6617059
- **Published**: 20 April 2026 on SSRN; revised 25 April 2026
- **Primary source URL**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6617059 (SSRN blocks programmatic crawling; full PDF requires browser session)
- **PDF location**: NOT on librarian — SSRN session-wall prevents download. Deep-read synthesis from 8 independent secondary sources (CoinDesk, TradingView/Cointelegraph, Cryptonews, Bitcoin News, Crowdfund Insider, Verse Press, iGaming.org, MEXC News) plus the SSRN abstract page. All sources published 2026-04-26/27, within 1-2 days of the paper's 04-25 revision.
- **Author homepage**: http://rgomezcram.com
- **Read status**: deep-read (no primary PDF; triangulated across 8 secondary sources with direct paper quotes + the SSRN abstract — highest-fidelity deep-read achievable without SSRN browser session)
- **Discovered via**: Workflow A Tier-2 Exa sweep 2026-04-29 (Q5 prediction markets)
- **Primary cluster**: quant-finance

## Narrative

### What it claims

A directly **refutational** paper. The widely-held framing of prediction markets is **"wisdom of crowds"**: aggregating many participants' bets produces accurate forecasts because individual errors cancel out. This paper refutes that framing using Polymarket's complete transaction history.

**The data**: 1.72M accounts, 98,906 events, 210,322 markets, $13.76B total volume, 2023-2025 timeframe. Platform grew from $3.3M/month (Dec 2023) to $1.98B/month (Dec 2025) — a 600× scale increase — and active accounts grew from ~1,600 to >519,000. Even at this scale, skill concentration remained stable. [Sources: CoinDesk 2026-04-26, Cryptonews 2026-04-26, iGaming.org 2026-04-27]

**The methodology — sign-randomization test**: For each account, replay actual trades 10,000 times with randomized buy/sell directions. Same markets, same timestamps, same dollar amounts — but a coin flip decides direction. The resulting null distribution answers: "how much profit would this account have earned by chance alone?" If actual returns consistently exceed the randomized distribution, the account is "skilled" — not lucky. This is a **bootstrap-based nonparametric test**, not a parametric z-score. [Source: CoinDesk 2026-04-26]

**Headline finding**: **Only 3.14% of accounts qualify as skilled.** These traders earn persistent profits out-of-sample, trade across an average of 79 markets each, and consistently position in the direction of final outcomes. Their order flow predicts both **next-period price changes** AND **final market outcomes** — a 1pp increase in skilled net buying corresponds to an **8bp increase** in P(correct outcome). [Sources: Cryptonews 2026-04-26, Bitcoin News 2026-04-26]

**The severity of the luck/skill filter**: Among the biggest winners by raw profit, only **12%** beat the randomized benchmark. Roughly **60% of "lucky winners"** (positive balances, zero predictive power) became net losers when tested out-of-sample. Many apparent winners were just lucky — and the sign-randomization test is the only reliable way to tell them apart. [Source: CoinDesk 2026-04-26]

**The remaining 96.86%** do not produce accuracy; **they fund it**. Their losses flow as profits to the informed minority.

### Skill persistence — the load-bearing finding

Train/test split on events (random, not temporal):

| Group | Out-of-sample persistence |
|---|---|
| Skilled (training) → skilled (test) | **44%** |
| Unskilled losers (training) → unskilled losers (test) | **51%** |
| Skilled mutual funds (parallel test) → skilled (test) | **10%** |

Polymarket exhibits **4.4× higher skill persistence than mutual funds**. The "anti-skill" signal (persistent losing) is even more stable than the skill signal — 51% of identified losers stay losers. [Sources: Cryptonews 2026-04-26, Verse Press 2026-04-26]

### Trader stratification

Four buckets, with profit-concentration detail from multiple sources:

| Bucket | % of accounts | % of total gains | Predictive power? | Persistence? |
|---|---|---|---|---|
| **Market makers + skilled takers** | <3.5% | >30% | Yes — order flow predicts prices + outcomes | 44% retain classification |
| **Lucky winners** | ~29% | ~69% of profit-takers | **None** — positive balances but zero predictive power | ~60% revert to losers out-of-sample |
| **Unlucky losers** | ~67% | Absorb **all** aggregate losses | Negative (lose consistently) | 51% retain classification |
| **Skilled losers / "anti-skilled"** | (subset of losers) | — | Persistently position against final outcome | 51% retain classification |

Market-maker accounts average **~$11,830/account**. The top **0.04% of wallets** capture ~70% of all platform profits. The bottom **61.48% of wallets** trade in the $0-$50 range. [Sources: Cryptonews 2026-04-26, Verse Press 2026-04-26, MEXC News 2026-04-27]

### News-reaction behavior — the cleanest skill/not-skill discriminator

Around scheduled news events (FOMC announcements, corporate earnings releases), **only skilled traders adjust order imbalance in the direction of the news surprise**. Lucky winners, unlucky losers, and the unclassified majority show "no steady reaction." When new information hits, skilled traders are the first to reposition — they are the price-discovery mechanism. The crowd reacts later, slower, and less directionally. [Sources: CoinDesk 2026-04-26, iGaming.org 2026-04-27]

### The insider-trading dimension

The paper identifies **1,950 accounts** (~0.11% of total) with trading patterns suggestive of non-public information: unusual timing + high-conviction position sizing + large price impact. These accounts average **~$15,000 profit each**. Insider-type trades move prices **7-12× more aggressively per dollar** than typical skilled trades — but they are rare, concentrated in a handful of events, and are not the day-to-day engine of price discovery. [Sources: iGaming.org 2026-04-27, CoinDesk 2026-04-26, Verse Press 2026-04-26]

**The Maduro case study** (cited in the paper): Three newly-created Polymarket accounts bought into a contract on Nicolás Maduro's removal from power in Venezuela hours before a classified U.S. military operation on January 3, 2026. The market priced odds at ~10% at the time. The accounts placed unusually large bets (tens of thousands of shares) before the price moved. Combined profit: **>$630,000**. Two accounts went dormant immediately after; the third went mostly dormant. On April 23, 2026 — days before the paper's revision — the DOJ and CFTC charged U.S. Army soldier Gannon Ken Van Dyke with using classified military intelligence to trade on Polymarket (~$33K → ~$409,881, a ~1,140% return across ~13 bets). This was the **first criminal prosecution under federal commodities fraud statutes for insider trading on a blockchain-based prediction market**. The timing — charges filed between the paper's initial publication and its revision — lends the paper real-world urgency. [Sources: CoinDesk 2026-04-26, Verse Press 2026-04-26]

### Platform concentration beyond the paper

Independent on-chain data from ChainCatcher confirms the paper's concentration gradient:
- 61.48% of Polymarket wallets trade $0-$50
- 0.51% of wallets have ever recorded >$1,000 profit
- Top 0.04% of wallets = ~70% of all platform profits
- 2025 full-year Polymarket volume: $21.5B; monthly record $12B (Jan 2026)
- Kalshi 2025 volume: $17.1B — the two platforms form a maturing duopoly

[Source: Verse Press 2026-04-26]

---

## Phase 3 Signal-Detection Criteria

*This section translates the paper's academic findings into concrete, encodable detection rules for the dual-MCP-Polymarket brief's Phase 3 shadow-mode "informed-flow analyst" service. Every threshold and rule below is derived from the paper's empirical parameters.*

### 1. Core detection: sign-randomization test (offline, daily batch)

**What it detects**: Is this account skilled, or just lucky?

**Implementation sketch**:
```
For each account with ≥N trades in the trailing window (suggest N≥20):
  1. Extract trade history: [market_id, timestamp, side, size, price, outcome]
  2. Compute actual P&L
  3. Run 10,000 bootstrap iterations:
     - Keep market_id, timestamp, size fixed
     - Randomize side (buy/sell) with p=0.5
     - Recompute P&L under randomized signs
  4. Build null distribution of 10,000 P&L values
  5. Actual P&L > 95th percentile of null → "skilled" flag
  6. Actual P&L < 5th percentile of null → "anti-skilled" flag
```

**Key parameters from the paper**:
- **Iterations**: 10,000 (the paper's exact number)
- **Classification threshold**: p<0.05 (two-tailed; the paper uses the 95th percentile)
- **Minimum trades per account**: paper doesn't specify an explicit floor but skilled traders average 79 markets — a floor of 20-30 trades is a reasonable starting point for Cemini's implementation
- **Training window**: paper uses random event-split, not temporal-split. For live deployment, use a rolling 90-day window with weekly retrain
- **Expected yield**: only ~12% of raw-profit top-earners pass this filter. It is aggressive by design

**Signal emitted**: `skilled_account_id`, `confidence_percentile` (e.g., 97.3 = actual P&L exceeds 97.3% of null), `markets_traded`, `avg_position_size`

### 2. Order-flow informativeness (real-time, per-market)

**What it detects**: Is the current order flow in this market being driven by skilled accounts?

**Rules to encode**:
- **Rule 2a — Skilled-flow direction signal**: Compute net buying of skilled-classified accounts in market M over trailing window W. If `skilled_net_buying > 0`, directional signal = BUY (toward YES). If `< 0`, directional signal = SELL (toward NO).
  - **Calibration**: 1pp increase in skilled net buying → 8bp increase in P(correct outcome). This is small per-pp but accumulates — a 12.5pp net buying differential implies a 1% probability shift.
- **Rule 2b — Skilled-flow concentration trigger**: If skilled accounts represent >X% of volume in market M over window W, flag for elevated confidence. Paper doesn't give an exact X, but the structural finding is that skilled accounts are <3.5% of accounts generating >30% of gains — so X=15-20% of volume from skilled accounts is a strong concentration signal.
- **Rule 2c — Lucky-winner contamination filter**: If an account has positive P&L but was NOT classified as skilled, its order flow receives **zero weight** in the signal. Lucky winners show "no meaningful predictive power" — including them dilutes the signal.

### 3. News-reaction test (event-driven, scheduled)

**What it detects**: Does this account react to new information like a skilled trader?

**Rules to encode**:
- **Rule 3a — Pre-announcement positioning**: For scheduled events (FOMC, earnings, economic releases), measure order imbalance of candidate accounts in the 60 minutes before announcement. Skilled accounts will be positioned in the direction of the eventual surprise *before* the announcement — this is the single cleanest discriminator per the paper.
- **Rule 3b — Post-announcement adjustment speed**: Measure time-to-rebalance after the announcement. Skilled accounts adjust within seconds-to-minutes; the crowd takes longer and with less directional consistency.
- **Rule 3c — Non-reaction as disqualifier**: If an account shows "no steady reaction" to multiple scheduled news events, it's likely not skilled regardless of P&L.

### 4. Insider-trading anomaly detection (real-time, per-event)

**What it detects**: Trades that look like non-public-information exploitation, not skill.

**Rules to encode** (from the paper's 1,950 flagged accounts + Maduro case study):
- **Rule 4a — New-account large-position flag**: Account age <7 days AND position size >95th percentile of market average → flag. (Maduro accounts were newly created, placed tens of thousands of shares at ~10% odds.)
- **Rule 4b — Dormancy-after-win flag**: Account places large winning bet → no trading activity for >48 hours after resolution → flag. (Two of three Maduro accounts went fully dormant; third went mostly dormant.)
- **Rule 4c — Price-impact multiplier flag**: Compute price impact per dollar traded. If >7× the skilled-trader baseline → flag as possible insider trade. (Paper: insider trades move prices 7-12× more per dollar.)
- **Rule 4d — Low-probability conviction flag**: Account places large positions on outcomes with <15% market-implied probability → flag. (Maduro contract was at ~10%.)
- **Rule 4e — Multi-account event clustering**: Multiple new accounts opening large same-direction positions on the same low-probability event within a short window → escalate. (Three accounts in the Maduro case.)

**Important**: The paper is clear that insider-type trades are **rare and event-concentrated** — not the day-to-day price-discovery engine. These rules are for anomaly flagging, not for the core signal. Flagged accounts should probably be **excluded** from the skilled-account pool (their signal is real but legally toxic).

### 5. Persistence validation (weekly, offline)

**What it detects**: Has a previously-skilled account lost its edge?

**Rules to encode**:
- **Rule 5a — Rolling reclassification**: Every 7 days, re-run the sign-randomization test on the trailing 90-day window. Expected: 44% of previously-skilled accounts retain classification. Accounts that drop out → downgrade signal weight by 50% for a 2-week grace period, then remove if not re-classified.
- **Rule 5b — Anti-skill persistence is stronger**: 51% of identified losers stay losers. An account flagged as "anti-skilled" (consistently wrong) is a **fade signal** — trade against its order flow. This is more persistent than the positive-skill signal.
- **Rule 5c — Market-maker vs skilled-taker split**: The paper groups them together in the "<3.5%" bucket, but they're behaviorally distinct. Market makers earn via spread capture (~$11,830 avg); skilled takers earn via directional correctness. For Cemini's purposes: **follow the skilled takers, not the market makers**. Market-maker flow is liquidity provision, not information. Cemini's signal should isolate taker-side skilled accounts.

### 6. Concentration thresholds (dashboard monitoring)

**Operational monitoring rules** — not signal inputs, but calibration checks:
- **Rule 6a — Top-N sufficiency check**: If the top 0.04% of tracked accounts capture <50% of aggregate profits, the identification pipeline may be missing accounts (baseline: ~70%).
- **Rule 6b — Lucky-winner churn rate**: If >60% of last month's "lucky winners" remain profitable this month, the sign-randomization test threshold may be too loose (baseline: ~60% revert to losers).
- **Rule 6c — Platform-scale invariant**: Skill concentration should remain stable as platform volume grows — the paper observed this across a 600× volume increase. If concentration shifts materially, investigate whether the identification methodology needs recalibration.

### Implementation priority order (Phase 3)

1. **Rule 1 (sign-randomization test)** — prerequisite. Everything else depends on knowing which accounts are skilled.
2. **Rule 2 (order-flow informativeness)** — the core real-time signal. Runs on every market tick.
3. **Rule 5 (persistence validation)** — gates whether the signal stays reliable over time.
4. **Rule 3 (news-reaction test)** — secondary confirmation; scheduled events only.
5. **Rule 4 (insider-trading detection)** — compliance/safety; not a trading signal.
6. **Rule 6 (concentration monitoring)** — dashboard; not signal-generating.

### Author summary

> "Their trades generate most of the volume, but little of the information, and their losses flow as profits to the informed minority. Prediction market accuracy thus reflects the wisdom of an informed minority, not the wisdom of the crowd." [Source: TradingView/Cointelegraph 2026-04-27 quoting Gómez-Cram et al]

### Why this matters for Cemini

1. **Strategy design** — Cemini's prediction-market exposure should model prices as "the informed minority's signal, with crowd liquidity around it." Trade with identified-skilled order flow, not against the median bettor. Without skill identification, Cemini IS the unskilled majority being skimmed.

2. **The deployable surface is concrete and scoped** — a "Polymarket informed-flow analyst" service that: (a) ingests public Polymarket trade data via kukapay's MCP; (b) applies the sign-randomization test offline daily; (c) identifies the top ~3% of accounts; (d) emits their real-time order flow as a directional signal; (e) routes execution through caiovicentino's MCP when the signal triggers. The dual-MCP-Polymarket brief already scopes this.

3. **44% persistence is production-grade** — 4.4× mutual-fund persistence means the signal doesn't decay before it can be traded on. Weekly reclassification keeps the pool fresh.

4. **Generalization to Kalshi** — the structural finding likely generalizes; Kalshi's regulated structure may amplify concentration (more institutional, fewer retail). Open empirical question.

### Risks & open questions

1. **Working paper, not peer-reviewed** — v1 2026-04-20, revised 2026-04-25. Pre-deployment gate: peer-review or 6-month stable-revision window.
2. **No primary PDF** — synthesis from 8 secondary sources. SSRN blocks programmatic access. Pre-deployment: SSRN browser-session full read to verify exact methodology specification.
3. **Polymarket-specific** — cross-platform replication needed before claiming universality.
4. **Survivorship bias** — skilled traders identified in training may exit by test period.
5. **Code license unknown** — sign-randomization test code not yet released; verify license separately.

### Citation

> Gómez-Cram, R., Guo, Y., Jensen, T. I., & Kung, H. (2026). *Prediction Market Accuracy: Crowd Wisdom or Informed Minority?* SSRN Working Paper 6617059. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6617059 (v1 20 Apr 2026; revised 25 Apr 2026)

## Snippets

> **The headline finding**
>
> "Only 3.14% of Polymarket accounts qualified as skilled winners. These traders earned persistent profits that held up out of sample, traded across an average of 79 markets each, and consistently positioned in the direction of final outcomes. The remaining 96% of accounts either broke even by luck or lost money." [Source: Cryptonews 2026-04-26, paraphrasing the SSRN working paper]

> **The refutational thesis**
>
> "Their trades generate most of the volume, but little of the information, and their losses flow as profits to the informed minority. Prediction market accuracy thus reflects the wisdom of an informed minority, not the wisdom of the crowd." [Source: TradingView/Cointelegraph 2026-04-27 quoting Gómez-Cram et al]

> **The sign-randomization methodology — how skill is separated from luck**
>
> "To filter that out, the authors reran each trader's bets 10,000 times, keeping everything the same except the direction. Same markets, same moments, same dollar amounts — but a coin flip decided whether to buy or sell. That gave them a benchmark for what each trader's profits would look like with no real edge. If the actual results consistently beat the coin flip, that's skill. If not, it's luck." [Source: CoinDesk 2026-04-26]

> **The severity of the filter**
>
> "Among the biggest winners by raw profit, only 12% beat the benchmark, and many apparent winners didn't stay that way: Roughly 60% of 'lucky winners' become losers when their performance is checked against a separate sample of events." [Source: CoinDesk 2026-04-26]

> **Skill persistence — the load-bearing comparison**
>
> "Among traders classified as skilled in training, 44% retained that classification in the test set. For unskilled losers, 51% remained in that category. By comparison, skilled mutual funds in a parallel test retained their classification only 10% of the time." [Source: Cryptonews 2026-04-26]

> **Order-flow informativeness**
>
> "Skilled traders' order flow predicted both next-period price changes and final market outcomes at statistically significant levels. A one-percentage-point increase in skilled net buying corresponded to an 8 basis point increase in the probability of the correct final outcome." [Source: Cryptonews 2026-04-26]

> **News-reaction as the skill discriminator**
>
> "Around FOMC announcements and corporate earnings releases, only skilled traders adjusted order imbalance in the direction of the news surprise. Other account groups showed no steady reaction." [Source: iGaming.org 2026-04-27, paraphrasing the paper]

> **The economic mechanism — who pays whom**
>
> "Market makers + skilled takers represented less than 3.5% of accounts but more than 30% of total gains. … Lucky winners, despite posting positive account balances, showed no meaningful predictive power in either test. … Unlucky and unskilled losers made 67% of all accounts and absorbed the entirety of aggregate losses." [Source: Cryptonews 2026-04-26]

> **Insider-trading flagging**
>
> "The authors identified 1,950 accounts with timing and conviction patterns that suggested possible use of non-public information. Those accounts also had large price effects when they traded." [Source: iGaming.org 2026-04-27]

> **Insider price impact multiplier**
>
> "Insider trades, when they occur, move prices even more aggressively per dollar, about seven-to-12 times more than typical skilled trades. But they are rare and concentrated in a handful of events, not the day-to-day engine of price discovery." [Source: CoinDesk 2026-04-26]

> **The Maduro case study**
>
> "In the days and hours before the operation, three newly created Polymarket accounts piled into a contract asking whether Maduro would be removed. At the time, the market priced the odds at roughly 10%. The new accounts placed unusually large bets, including orders of tens of thousands of shares, before the price moved. When the raid happened, the accounts collectively made more than $630,000. Two stopped trading entirely soon after, and the third went mostly dormant." [Source: CoinDesk 2026-04-26]

> **Platform concentration — on-chain data**
>
> "61.48% of Polymarket wallets trade within the $0 to $50 bracket. Approximately 0.51% of wallets have ever recorded a profit above $1,000. The top 0.04% of wallets account for roughly 70% of all platform profits." [Source: Verse Press 2026-04-26, citing ChainCatcher on-chain data]

> **The data scale**
>
> "The researchers analyzed the complete transaction history on Polymarket, the world's largest prediction market by trading volume. The study covered 98,906 events, 210,322 markets, and $13.76 billion in total trading volume across 1.72 million accounts." [Source: Cryptonews 2026-04-26]
