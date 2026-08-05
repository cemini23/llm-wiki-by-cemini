---
title: VIX-first joint SPX–VIX calibration (VDV pattern)
type: concept
tags: [concept, volatility, vix, xsp, k222]
keywords: [VDV, joint calibration, VIX futures, SPX options]
related:
  - sources/arxiv-2608.02778-nnlci-options-pricing.md
  - sources/arxiv-2608.01479-vix-derived-volatility-model.md
  - sources/arxiv-2608.01217-lsv-calibration-neural-operator.md
  - concepts/xsp-lane-trading-framework.md
maturity: draft
created: 2026-08-04
updated: 2026-08-05
---

## Relations

- @sources/arxiv-2608.02778-nnlci-options-pricing.md

- @sources/arxiv-2608.01479-vix-derived-volatility-model.md — primary VDV paper
- @sources/arxiv-2608.01217-lsv-calibration-neural-operator.md — amortizing LSV operator (complementary vol stack)
- @concepts/xsp-lane-trading-framework.md

## Raw Concept

How to structure joint SPX–VIX model work so VIX futures/options stay primary and SPX vol is a derived latent — vs black-box joint optimizers that fight both markets at once.

## Narrative

From Zaugg/Grzelak (2608.01479): calibrate explicit VIX dynamics first; use rolling-window VIX definition to couple SPX stochastic volatility without rewriting VIX. Useful frame for **xsp** Lane B / LEAPS hedge research and for interpreting GuruWatcher VIX level polls as regime context, not as a live calibrator. Pair with amortizing LSV operators (2608.01217) when thinking about offline surface solves vs online latency.

**Out of scope:** auto-trading from paper numerics; inventing vol surfaces without market data.
