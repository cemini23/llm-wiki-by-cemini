---
title: Instrumental probability and learnable alpha limits
type: concept
tags: [concept, quant-finance, market-efficiency, predictability, evaluation-discipline]
keywords: [instrumental-probability, P-Q-wedge, learnable-alpha, capacity-constraints, net-exploitability, reflexivity]
related:
  - sources/arxiv-instrumental-probability-hard-to-predict-2606.08209-2026-06-10.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - concepts/polymarket-microstructure-findings.md
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
  - concepts/market-informedness-market-making.md
  - concepts/strategy-half-life-live-monitoring.md
  - sources/arxiv-pandaai-neuro-symbolic-quant-2606.06823-2026-06-12.md
  - concepts/proper-betting-clob-prediction-markets.md
  - sources/arxiv-prophets-profit-prediction-markets-2607.06166-2026-07-09.md
maturity: draft
created: 2026-06-10
updated: 2026-10-25
---

## Relations

- @sources/arxiv-instrumental-probability-hard-to-predict-2606.08209-2026-06-10.md — K110 anchor
- @concepts/regime-conditioned-evaluation.md — deflated Sharpe + falsification discipline
- @concepts/prediction-markets-efficiency-wolfers-zitzewitz.md — PM efficiency prior vs local edge
- @concepts/polymarket-microstructure-findings.md — microstructure causal chain
- @sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md — informedness / adverse selection
- @concepts/market-informedness-market-making.md — MM profitability vs informedness

## Raw Concept

K110 synthesis from Noguer i Alonso (2026) arXiv 2606.08209 — vocabulary for separating **market hardness** from **literal randomness**, and for why positive backtests may not survive scaling.

## Narrative

### Three efficiency notions (do not conflate)

| Notion | Meaning | Bot operator mistake |
|--------|---------|---------------------|
| No-arbitrage | No free lunch under pricing measure Q | Assuming any drift ⇒ easy money |
| Informational efficiency | Prices reflect available info (with Grossman–Stiglitz costs) | Assuming PM mids are perfect forecasts |
| Net exploitability | Signal survives costs, capacity, competition | Promoting backtest without capacity layer |

### P–Q wedge

Derivatives pricing uses **instrumental** probability: Q is chosen for martingale pricing, not asserted as the physical data-generating measure P. Relative entropy between P and Q quantifies the wedge (~½θ²T in their framework). Useful mental model when interpreting PM prices as probabilities vs when applying risk-neutral hedging logic.

### Why alpha is hard to learn

Hardness sources beyond partial observation: reflexivity (prediction moves the object), microstructure frictions, **capacity limits**, Knightian regime change, model-selection landscape risk. Positive in-sample signals can be **real but non-scalable** — aligns with LP promotion gates and `@concepts/regime-conditioned-evaluation.md` (deflated Sharpe, multiple testing).

### Cemini use

- **Brief-audit language** — reject "markets are random" as justification for skipping rigor; require capacity + regime disclosure
- **PM LP** — pair with informedness regime labels (K100); hardest prediction where flow is competitive and self-defeating
- **Not a trading model** — no parameters to deploy; REFERENCE framing only

## Snippets

> "Only the arbitrageable part is unpredictable by construction."

> — [Source: arxiv-2606.08209 p.2, retrieved 2026-06-10]

> "Positive signals need not be scalable."

> — paraphrase of §7 capacity-and-survival layer; [Source: arxiv-2606.08209, retrieved 2026-06-10]
