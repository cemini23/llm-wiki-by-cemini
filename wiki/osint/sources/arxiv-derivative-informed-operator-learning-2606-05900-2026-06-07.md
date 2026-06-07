---
title: "Derivative-Informed Operator Learning for Finance (arXiv 2606.05900)"
type: source
tags: [source, arxiv, quant-finance, neural-operators, greeks, hedging]
keywords: [derivative-informed-training, neural-operators, fno, deeponet, greeks, xva, hedging]
related:
  - concepts/derivative-informed-operator-learning.md
  - concepts/options-derivatives.md
maturity: draft
read_status: read
created: 2026-06-07
updated: 2026-06-07
clusters: [quant-finance, ml-methods]
---

## Relations

- @concepts/derivative-informed-operator-learning.md — synthesized concept

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Derivative-Informed Operator Learning for Finance: On-the-Fly Greeks, Surfaces, Hedging, and Control |
| **Author** | Miquel Noguer i Alonso (Artificial Intelligence Finance Institute) |
| **arXiv** | 2606.05900 |
| **sha256** | `1f8b1b5ba5f9120b0833c09d2d4d59976303b354659fe6f1c1cbabbeb9d34c1e` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.05900-derivative-informed-operator-learning-for-financ.pdf` |
| **Retrieved** | 2026-06-07 |
| **Read status** | read (abstract + intro + experiment summary) |

## Narrative

Proposes training financial surrogate models (neural operators, random-feature operators) to match **directional Fréchet derivatives** (Greeks, curve sensitivities, exposure gradients) generated on the fly via adjoint algorithmic differentiation — not just prices.

Three reproducible experiments separate mechanism from deployment claims:

1. **Black–Scholes network** (8 seeds): tuned derivative weight cuts vega error ~40%, delta ~15%, modest price RMSE gain; unsupervised second-order Greek unreliable.
2. **Heston/Bates random features**: SV/jump-parameter sensitivity errors down 60–76%.
3. **Curve-to-surface DeepONet/Galerkin operator**: JVP error −44%, price RMSE −23% over 8 seeds; derivative consistency alone does **not** remove no-arbitrage violations — economic constraints must be explicit.

**Cemini relevance:** REFERENCE for any future neural surrogate pricing layer on librarian research stack — not prod execution path today. Hedging-error bounds tie gamma accuracy to discrete-time hedging slippage.

## Snippets

> "Derivative accuracy controls local stress errors, hedging error, and optimizer instability, and discrete-time hedging error is additionally governed by second-order (gamma) accuracy." [Source: arxiv-2606.05900 p.1 abstract]

> "Derivative consistency does not by itself remove no-arbitrage violations, so economic constraints must be imposed explicitly." [Source: arxiv-2606.05900 abstract]
