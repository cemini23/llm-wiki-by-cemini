---
title: FOMC IV-Surface Dynamics — pre-announcement vol elevation
type: concept
tags: [concept, options, vol-surface, fomc, xsp, k233]
keywords: [fomc, implied-volatility, pre-announcement-effect, short-dated-otm, convlstm, high-vol-regime]
related:
  - sources/arxiv-addmart-iv-surface-2610.25671-2026-10-20.md
  - sources/arxiv-gromm-risk-neutral-option-market-2610.16732-2026-10-14.md
  - sources/arxiv-2608.10693-fed-speaks-vol-surface-2026-08-12.md
  - concepts/xsp-lane-trading-framework.md
  - concepts/xsp-vol-regime-gates.md
maturity: draft
created: 2026-08-12
updated: 2026-10-20
---

## Relations

- @sources/arxiv-2608.10693-fed-speaks-vol-surface-2026-08-12.md
- @concepts/xsp-lane-trading-framework.md
- @concepts/xsp-vol-regime-gates.md

## Raw Concept

What this page answers: does implied volatility build ahead of scheduled FOMC meetings, where is the effect concentrated, and can ML beat random walk at forecasting it? Synthesized from Adamski & Ślepaczuk, arXiv 2608.10693.

## Narrative

**Pre-announcement IV elevation is real** and strongest for **short-dated OTM options** in **high-volatility regimes**. The effect is amplified when the vol regime is already elevated — the market bids up near-dated convexity into the event.

**Forecasting:** a convolutional 2D LSTM (ConvLSTM) applied directly to the IV surface (no PCA/dimensionality reduction) with a FOMC-date feature can forecast the surface during announcement days, but the edge over random walk is bounded by surface noise. Conclusion: ML forecasting works on abnormal days; treat IV-surface ML as an enhancement to regime conditioning, not a standalone alpha source.

**K293 — ADDMART (2026-10-20).** @sources/arxiv-addmart-iv-surface-2610.25671-2026-10-20.md rebuilds a sparse quote grid as an exponential additive martingale, so static no-arbitrage holds by construction. It is a surface tool, not an FOMC forecast. No trade.

**XSP application:** pre-FOMC short-dated vol elevation creates a timing edge for the long-call lanes — entering long calls *before* scheduled meetings captures the IV bid-up (not just the directional move). Strength scales with vol regime: high-vol regime → stronger pre-event elevation → favor earlier entry / larger sizing per the lane's regime gates.

[Source: arXiv:2608.10693]
