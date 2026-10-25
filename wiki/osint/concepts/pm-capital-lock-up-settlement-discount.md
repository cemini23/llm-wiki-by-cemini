---
title: Prediction market settlement discounting and capital lock-up
type: concept
tags: [concept, polymarket, prediction-markets, microstructure, k94]
keywords: [settlement discount, capital lock-up, near-certain, oracle delay]
related:
  - sources/arxiv-pm-settlement-discounting-2605-31431-2026-06-02.md
  - entities/platforms/polymarket.md
  - concepts/polymarket-microstructure-findings.md
  - concepts/kalshi-implied-macro-belief-distributions.md
  - concepts/settlement-manipulation-prediction-markets.md
  - sources/arxiv-kalshi-macroeconomic-beliefs-2606.30040-2026-07-02.md
  - sources/arxiv-settlement-manipulation-pm-2606.31675-2026-07-01.md
maturity: draft
created: 2026-06-02
updated: 2026-10-25
---

## Relations

- @sources/arxiv-pm-settlement-discounting-2605-31431-2026-06-02.md
- @entities/platforms/polymarket.md

## Narrative

Collateralized PMs lock capital until **oracle settlement**. Near-certain outcomes can still trade below $1 because the claim is a **delayed dollar** — prices embed a **settlement discount** (term structure / annualized wedge) on top of outcome probability.

**Trading implication:** hold-to-resolution and LP strategies must compare return on locked collateral vs opportunity cost; “99¢ certain” arbs are not risk-free without time value. [TENTATIVE] until calibrated on Polymarket WC markets.
