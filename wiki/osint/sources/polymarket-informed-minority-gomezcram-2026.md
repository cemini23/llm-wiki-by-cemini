---
title: "Prediction Market Accuracy — Crowd Wisdom or Informed Minority? (SSRN 6617059, Gómez-Cram, Guo, Jensen, Kung — LBS + Yale, 2026)"
type: source
tags: [paper, prediction-markets, polymarket, behavioral-finance, market-microstructure, skill-persistence, refutes-wisdom-of-crowds, ssrn-working-paper, lbs, yale, cemini-relevant, workflow-a-find]
keywords: [polymarket, prediction-market-accuracy, informed-minority, wisdom-of-crowds-refutation, skill-persistence, sign-randomization-test, market-makers, skilled-takers, lucky-winners, unlucky-losers, gomez-cram, yunhan-guo, theis-ingerslev-jensen, howard-kung, london-business-school, yale-som, ssrn-6617059, 2023-2025-data, 1-72-million-accounts, 13-76-billion-volume, 98906-events]
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
  - sources/polymarket-predictions-mcp.md
  - sources/last30days-skill-mvanhorn.md
maturity: validated
read_status: read-skim
created: 2026-04-29
updated: 2026-04-30
---

## Relations

- @concepts/market-microstructure.md — primary cluster home: this is a market-microstructure paper on prediction markets, refuting the "wisdom of crowds" framing in favor of an "informed minority" framing.
- @concepts/quant-finance.md — secondary cluster: finds skill-persistence rates (44% out-of-sample) that **dwarf mutual-fund analogues (10%)** — operationally relevant for any quant strategy that piggybacks on "smart money" signals.
- @concepts/favorite-longshot-bias.md — adjacent behavioral-finance concept; favorite-longshot bias and crowd-wisdom-refutation are both behavioral anomalies in prediction-market pricing.
- @concepts/high-signal-paper-patterns.md — Workflow A find from the 2026-04-29 sweep (Q5: prediction markets / Kalshi / Polymarket order-book analysis). Originally surfaced indirectly via Coindesk + Cryptonews + TradingView articles; primary source located via Exa secondary search. Score 4-5/6 quality + 3/3 operational + refutation premium.
- @entities/platforms/polymarket.md — direct subject: this paper analyzes Polymarket's complete transaction history (1.72M accounts, $13.76B volume, 2023-2025).
- @entities/platforms/kalshi.md — sibling prediction-market platform Cemini watchlists; the paper's findings about informed-minority-driven accuracy probably generalize, but Kalshi's regulated structure (CFTC oversight) may attract different participant mix vs Polymarket's decentralized one. Open empirical question for Cemini.
- @sources/lob-regime-detection-hiremath-2026.md — sibling Workflow A find from the same 2026-04-29 sweep. Both papers are quant-finance / market-microstructure flavor; both refute received wisdom in their domain ("early-warning signals are inherently reactive" → wrong; "prediction markets work by crowd wisdom" → wrong).

## Raw Concept

- **Original title**: "Prediction Market Accuracy: Crowd Wisdom or Informed Minority?"
- **Authors**: Roberto Gómez-Cram (London Business School Finance — Assistant Professor), Yunhan Guo (LBS), Theis Ingerslev Jensen (Yale School of Management), Howard Kung (LBS)
- **Type**: SSRN working paper
- **SSRN ID**: 6617059
- **Published**: 20 April 2026 on SSRN
- **Revised**: 25 April 2026
- **License**: SSRN academic working-paper terms (extract math + paraphrase findings into Cemini documentation; do not redistribute the paper itself; standard academic fair use)
- **Primary source URL**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6617059 (abstract page; full PDF requires SSRN session)
- **PDF location**: NOT downloaded to librarian — SSRN PDF download requires session cookies. Source page synthesizes from abstract + 3 independent secondary-source articles (Coindesk 2026-04-26, TradingView/Cointelegraph 2026-04-27, Cryptonews 2026-04-26).
- **Author homepage**: http://rgomezcram.com (research papers listed)
- **Read status**: read-skim (no full PDF; synthesis from abstract page + 3 detailed news articles; primary source verification pending — Cemini-deployment gate would require full-paper read via SSRN access)
- **Discovered via**: Workflow A Tier-2 Exa sweep 2026-04-29 (Q5 prediction markets); primary paper located via secondary Exa search after the news articles surfaced
- **Primary cluster**: quant-finance
- **All clusters**: quant-finance, market-microstructure, prediction-markets

## Narrative

### What it claims

A directly **refutational** paper. The widely-held framing of prediction markets (Polymarket, Kalshi, Augur, etc.) is **"wisdom of crowds"**: aggregating many participants' bets produces accurate forecasts because individual errors cancel out. This paper refutes that framing using Polymarket's complete transaction history.

**The data**:
- 1.72 million accounts
- 98,906 events
- 210,322 markets
- $13.76 billion total trading volume
- 2023-2025 timeframe

**The methodology**: a **sign-randomization test** — for each account, the researchers repeated past trades 10,000 times with randomized profit signs to simulate the null distribution of profits expected by chance. Accounts whose actual returns sit beyond the null distribution are classified as "skilled" (statistically significant winners) — not lucky.

**The headline finding**: **only 3.14% of accounts qualify as skilled.** These traders:
- Earn persistent profits that hold up out-of-sample
- Trade across an average of 79 markets each
- Consistently position in the direction of final outcomes
- Their order flow predicts both **next-period price changes** AND **final market outcomes** at statistically significant levels — a 1pp increase in skilled net buying corresponds to an **8 basis-point increase** in the probability of the correct final outcome.

**The remaining 96.86% of accounts** either break even by luck or lose money. They do not produce accuracy; **they fund it**. Their losses flow as profits to the informed minority.

### Skill persistence — the load-bearing finding

The authors split events randomly into training and test sets:
- **44% of skilled-classified-in-training traders retained skilled classification in test** — a strikingly high persistence rate.
- **51% of unskilled-loser-classified-in-training retained that classification in test** — the loser side is also persistent.
- **Comparison: skilled mutual funds in a parallel test retained classification only 10% of the time.**

So Polymarket exhibits **4× higher skill persistence than mutual funds**. This refutes both the "luck dominates" framing AND the "you can't tell skill from luck in finance" framing — at least for prediction markets.

### Trader stratification

The paper classifies accounts into four buckets:

| Bucket | Approx % of accounts | Profit characteristic |
|---|---|---|
| **Market makers + skilled takers** | ~3.5% | Earn >30% of total gains; persistent skill |
| **Lucky winners** | ~29% | Positive returns but no predictive power; reverts |
| **Unlucky losers** | (sum to >67%) | Absorb the entirety of aggregate losses |
| **Skilled losers / "anti-skilled"** | (subset of losers) | Persistently positioned against final outcome |

Market-maker accounts earn an average of **~$11,830 per account**. Concentrated, identifiable, persistent — not crowd-noise.

### Author summary (the line that names the paper's claim)

> "Their trades generate most of the volume, but little of the information, and their losses flow as profits to the informed minority. Prediction market accuracy thus reflects the wisdom of an informed minority, not the wisdom of the crowd."

### Why this matters for Cemini

1. **Strategy design** — Cemini's prediction-market exposure (currently Kalshi-watchlist research; potential future Polymarket integration) should NOT model prices as "the crowd's aggregated belief". They should model prices as **"the informed minority's signal, with crowd liquidity around it"**. Operational implications:
   - **Trade with the order flow of identified-skilled traders, not against the median bettor.** The paper's sign-randomization test is the methodology — Cemini could apply it offline to public Polymarket data to identify skilled accounts before placing trades.
   - **Liquidity is provided by the unskilled majority** — Cemini's market-maker analyst path can target this liquidity, but the win-rate would depend on Cemini being on the informed-minority side. Without that, Cemini IS the unskilled majority being skimmed.

2. **Skill identifiability + persistence is a usable signal** — 44% out-of-sample skill retention is high enough to power production strategies. **Concrete deployable surface**: a "Polymarket informed-trader follower" service that ingests public Polymarket trade data, applies the sign-randomization test offline daily, identifies the top 3% accounts, and emits their order flow as a signal Cemini's analysts can consult.

3. **Refutes "crowd wisdom" framing for procurement** — when Cemini eventually evaluates "should we add Polymarket as a data source?" or "should we add Polymarket as a trading venue?", the answer is qualitatively different given this paper. Cemini's interest in Polymarket should be **"the informed minority's signal is identifiable and persistent"**, not "the median bet is informative". The data-source value is in the trade-flow of the 3%, not the price.

4. **Generalization to Kalshi (which Cemini already watches)** — the paper's data is Polymarket-specific, but the structural finding (information concentrated in a minority) likely generalizes to Kalshi. Kalshi's regulated CFTC structure may shift the population mix (more institutional, fewer retail), which could AMPLIFY the informed-minority concentration. **Open empirical question for a follow-on Cemini brief**: replicate the sign-randomization test on Kalshi if/when public data is available.

### Risks & open questions

1. **Working paper, not yet peer-reviewed** — first version published 2026-04-20, revised 2026-04-25. Treat as preliminary. **Pre-Cemini-deployment gate**: peer-reviewed publication or at least a 6-month-stable-revision window before treating as core.

2. **Polymarket-specific data may not generalize**: Polymarket is a decentralized prediction market with crypto-native participants; Kalshi is regulated; Augur is now mostly inactive; PredictIt is academic-tier. Cross-platform replication is needed before claiming "all prediction markets work this way."

3. **Skill identification has survivorship bias risk**: skilled traders identified in training set may have already exited by the test period. The 44% retention number is robust but the population composition may shift over time.

4. **Adoption-blocking license check**: the SSRN paper terms allow extraction + paraphrase but do not allow redistribution of the paper itself or derivative works. Cemini cannot incorporate the SAS-randomization-test code (when released) without verifying the code license separately.

5. **No primary-source PDF deep-read in this ingest** — synthesis based on abstract page + 3 detailed news articles. Possible misinterpretation of nuanced claims (e.g., the 3.14% vs 3.5% number — depends on whether "informed minority" includes market makers or only skilled takers). Pre-deployment requires SSRN session + full-paper read.

### Cemini-side adoption assessment

**Decision: Watch-and-replicate**. Strong refutational finding directly relevant to Cemini's prediction-market thinking. Concrete next-steps:

1. **Get the full paper via SSRN session** (user has SSRN access? If not, request via library or wait for arXiv mirror). ~5 min when available.
2. **Read methodology section** of the full paper for exact sign-randomization-test specification. ~30 min.
3. **Run the test against public Polymarket data** for a 30-day window as a reproduction. Cemini already has Polymarket data infrastructure plans. ~half-day.
4. **If reproduction validates skill persistence: build a "Polymarket informed-flow" analyst node** in `agents/analyst/polymarket_informed_flow.py` consuming the daily sign-randomization output. Brief to cemini-prod for production wiring.
5. **Track for arXiv mirror** — many SSRN finance papers eventually get arxiv'd in q-fin.MF; check monthly.

### Citation

> Gómez-Cram, R., Guo, Y., Jensen, T. I., & Kung, H. (2026). *Prediction Market Accuracy: Crowd Wisdom or Informed Minority?* SSRN Working Paper 6617059. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6617059 (first version 20 Apr 2026; revised 25 Apr 2026)

## Snippets

> **The headline-finding statement — pulled from the secondary articles**
>
> "Only 3.14% of Polymarket accounts qualified as skilled winners. These traders earned persistent profits that held up out of sample, traded across an average of 79 markets each, and consistently positioned in the direction of final outcomes. The remaining 96% of accounts either broke even by luck or lost money." [Source: Cryptonews summary 2026-04-26, paraphrasing the SSRN working paper Gómez-Cram et al]

> **The skill-persistence comparison — the load-bearing finding**
>
> "Among traders classified as skilled in training, 44% retained that classification in the test set. For unskilled losers, 51% remained in that category. By comparison, skilled mutual funds in a parallel test retained their classification only 10% of the time. The authors describe prediction markets as showing unusually high persistence of both skill and anti-skill." [Source: Cryptonews summary 2026-04-26, paraphrasing the SSRN working paper]

> **The refutational thesis — directly from the authors' framing**
>
> "Their trades generate most of the volume, but little of the information, and their losses flow as profits to the informed minority. Prediction market accuracy thus reflects the wisdom of an informed minority, not the wisdom of the crowd." [Source: TradingView/Cointelegraph 2026-04-27 quoting Gómez-Cram et al]

> **The economic mechanism — who pays whom**
>
> "Market makers + skilled takers represented less than 3.5% of accounts but more than 30% of total gains. … Lucky winners, despite posting positive account balances, showed no meaningful predictive power in either test. … Unlucky and unskilled losers made 67% of all accounts and absorbed the entirety of aggregate losses." [Source: Cryptonews summary 2026-04-26]

> **The order-flow predictive-power finding**
>
> "Skilled traders' order flow predicted both next-period price changes and final market outcomes at statistically significant levels. A one-percentage-point increase in skilled net buying corresponded to an 8 basis point increase in the probability of the correct final outcome." [Source: Cryptonews summary 2026-04-26]

> **The data scale**
>
> "The researchers analyzed the complete transaction history on Polymarket, the world's largest prediction market by trading volume. The study covered 98,906 events, 210,322 markets, and $13.76 billion in total trading volume across 1.72 million accounts." [Source: Cryptonews summary 2026-04-26]
