---
title: Market informedness impact on market makers' profitability (arXiv 2606.05882)
type: source
tags: [source, arxiv, market-making, microstructure, quant-finance, reinforcement-learning]
keywords: [2606.05882, market-informedness, market-makers, profitability, adverse-selection, hawkes, mappo]
related:
  - concepts/market-informedness-market-making.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-microstructure-findings.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
  - concepts/avellaneda-stoikov-market-making-baseline.md
maturity: validated
read_status: deep-read
created: 2026-06-05
updated: 2026-06-05
---

## Relations

- @concepts/market-informedness-market-making.md — synthesis
- @concepts/polymarket-market-making-architectures.md — Cemini LP posture
- @concepts/polymarket-microstructure-findings.md — informed-trader literature cluster
- @sources/polymarket-informed-minority-gomezcram-2026.md — Polymarket informed-minority empirical prior

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Impact of Market Informedness on Market Makers' Profitability |
| **Authors** | Konrad Ochedzan (UZH/ETH); Nino Antulov-Fantulin (ETH / Aisot) |
| **arXiv** | 2606.05882 (q-fin.TR) |
| **Pages** | 45 |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.05882-the-impact-of-market-informedness-on-market-make.pdf` |
| **Retrieved** | 2026-06-05 |
| **Read status** | deep-read — abstract, intro, RL/Hawkes setup, headline results |

## Narrative

Simulation study of **heterogeneous market makers** in a LOB with endogenous prices, fundamental-value dynamics, and **self-exciting Hawkes** market-taker flow. MMs differ in information sets and inventory-risk aversion; policies trained via **MAPPO** (CTDE).

**Headline result (counter-intuitive for naive LP heuristics):** although informed order flow is **most dangerous in poorly informed markets** (severe adverse selection), aggregate MM profitability shows an **overall upward trend as market informedness increases** — higher informedness improves price discovery enough to offset adverse-selection drag. Training noise yields **local non-monotonicity**, but the global trend holds `[CONFIRMED — paper abstract + intro, single source]`.

**Theory contribution:** finite-horizon stability guarantees for the state-dependent Hawkes taker process (non-explosion, mispricing integrability, occupation-time bounds).

**Cemini implications:**

| Takeaway | LP / bot action |
|----------|-----------------|
| Don't assume "more informed flow ⇒ always worse MM PnL" | Regime labels need both informedness **and** market maturity |
| Poorly informed markets + informed bursts | Tightest spread tiers are highest adverse-selection risk |
| Hawkes clustering | Align with `@concepts/polymarket-microstructure-findings.md` burst/FLB work — inventory caps near event clusters |

Pair with quarterly `@meta/pm-lp-backtest-cadence.md` — proxy informedness from PM flow features still `[NEEDS VERIFICATION 2026-06-05]` on live CLOB.

## Snippets

> "Informed market order flow is particularly dangerous in poorly informed markets, leading to severe adverse-selection risk."

> "The results nevertheless reveal an overall upward trend in market makers' profitability as market informedness increases, suggesting that price discovery resulting from higher market informedness offsets the negative impact of adverse selection."

> — [Source: arxiv-2606.05882-the-impact-of-market-informedness-on-market-make.pdf p.1, retrieved 2026-06-05]

> "The study employs a reinforcement learning framework based on the multi-agent proximal policy optimization (MAPPO) algorithm in a centralized training with decentralized execution (CTDE) setting."

> — [Source: arxiv-2606.05882 p.1, retrieved 2026-06-05]
