---
title: Markets Are Not Random, They Are Hard to Predict (arXiv 2606.08209)
type: source
tags: [source, arxiv, quant-finance, market-efficiency, predictability, microstructure]
keywords: [2606.08209, instrumental-probability, P-Q-wedge, learnable-alpha, deflated-sharpe, reflexivity, adaptive-markets]
related:
  - concepts/instrumental-probability-learnable-alpha.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/prediction-markets-efficiency-wolfers-zitzewitz.md
  - concepts/polymarket-microstructure-findings.md
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
  - concepts/market-informedness-market-making.md
maturity: validated
read_status: deep-read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- @concepts/instrumental-probability-learnable-alpha.md — synthesis
- @concepts/regime-conditioned-evaluation.md — deflated Sharpe + falsification protocol alignment
- @concepts/prediction-markets-efficiency-wolfers-zitzewitz.md — efficiency vs exploitability distinction
- @concepts/polymarket-microstructure-findings.md — microstructure causal chain (§13)
- @sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md — informedness / adverse-selection sibling
- @concepts/market-informedness-market-making.md — informedness regime feature for LP

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Markets Are Not Random, They Are Hard to Predict: Instrumental Probability, the P–Q Wedge, and the Limits of Learnable Alpha |
| **Author** | Miquel Noguer i Alonso (Artificial Intelligence Finance Institute) |
| **arXiv** | 2606.08209 (q-fin.MF) |
| **Pages** | 27 |
| **sha256** | `9a67af7d143b82e7ff56f3a4bf5c1f555a947d8026a7d0b508ae0d057dac1f26` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.08209-markets-are-not-random-they-are-hard-to-predict.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | deep-read — abstract, intro, §§7–10, §17 falsification protocol, §18–19 synthesis |

## Narrative

Conceptual essay (not empirical backtest) separating **ontic randomness** from **epistemic unpredictability** in finance. Thesis: markets are causal economic systems whose futures are **hard to predict** because causes are hidden, costly to observe, strategically used, capacity-constrained, or governed by changing law — not because returns are literally random like quantum measurement.

**Five-axis argument:**

| Axis | Claim | Cemini hook |
|------|-------|-------------|
| Instrumental probability | Pricing under Q ≠ P is a **change of measure for valuation**, not a literal world law | Don't confuse PM mid prices with physical P(event) without risk adjustment |
| Martingale ≠ random walk | No-arbitrage ⇒ martingale under pricing measure; does **not** imply i.i.d. Gaussian returns | LP edge can live in microstructure + inventory, not "markets are a coin flip" |
| Hardness sources | Reflexivity, microstructure, capacity, Knightian regime change | WC bot / PM LP: capacity + survival layer before scaling signals |
| Doob decomposition | Predictable risk-compensated drift vs martingale innovation | Separates **tradable alpha** from **risk premia** |
| Entropy ledger | Relative entropy quantifies P–Q wedge (~½θ²T) | Theoretical frame for "how much edge is left after competition" |

**Three-way distinction (critical for bot operators):**

1. **No-arbitrage** — free-lunch violations absent under Q
2. **Informational efficiency** — prices reflect available information (Grossman–Stiglitz limits)
3. **Net exploitability** — positive signal **after costs, capacity, and competition**

Positive backtest signals need not be **scalable** (§7 capacity-and-survival). Aligns with Cemini `@concepts/regime-conditioned-evaluation.md` discipline: deflated Sharpe, multiple-testing awareness, falsifiable claims.

**Cemini posture:** REFERENCE — vocabulary for brief-audit and LP promotion gates; not a deployable model. Pair with K100 informedness paper and K107 covariance-regret audit for the full "is this edge real?" stack.

## Snippets

> "The disciplined thesis is therefore not that markets are unknowable, nor that they are literally random. Markets are hard to predict, and hardest exactly where prediction is costly, competitive, self-defeating, capacity limited, or invalidated by regime change."

> — [Source: arxiv-2606.08209-markets-are-not-random-they-are-hard-to-predict.pdf p.1, retrieved 2026-06-10]

> "Financial markets are epistemically difficult, not ontically random. Every tick has a cause; the chain 'information → order → execution → price' is causal throughout."

> — [Source: arxiv-2606.08209 p.2, retrieved 2026-06-10]

> "The paper separates no-arbitrage, informational efficiency, and net exploitability."

> — [Source: arxiv-2606.08209 Abstract, retrieved 2026-06-10]
