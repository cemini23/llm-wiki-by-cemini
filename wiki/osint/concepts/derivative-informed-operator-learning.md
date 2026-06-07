---
title: Derivative-informed operator learning for finance
type: concept
tags: [concept, neural-operators, greeks, hedging, quant-finance]
keywords: [derivative-informed-training, fno, deeponet, adjoint-ad, xva, gamma-accuracy]
related:
  - sources/arxiv-derivative-informed-operator-learning-2606-05900-2026-06-07.md
  - concepts/options-derivatives.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- @sources/arxiv-derivative-informed-operator-learning-2606-05900-2026-06-07.md — K103 arXiv ingest

## Raw Concept

Prompted by arXiv 2606.05900 (Noguer i Alonso, June 2026): financial decision systems need surrogates whose **derivatives** (Greeks, curve sensitivities) are accurate, not just level prices.

## Narrative

Standard neural surrogates minimize price RMSE; downstream hedging, XVA, and portfolio optimization depend on **Jacobian structure**. The paper trains operators with on-the-fly directional derivatives (adjoint AD + tangent sensitivity + random Jacobian sketches) alongside value matching.

Empirical headline: derivative-weighted training improves vega/delta and local stress metrics; **gamma** and no-arbitrage still need explicit economic constraints.

**Cemini posture:** REFERENCE on librarian research stack. Any prod adoption would require clean-room validation against existing pricing paths — no current `/opt/cemini` integration planned.

## Snippets

> "The framework provides a disciplined route from value-only surrogates to derivative-aware financial engines." [Source: arxiv-2606.05900 abstract]
