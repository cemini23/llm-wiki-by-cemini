---
title: "Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets"
type: source
tags: [pdf, time-series, prediction-markets]
clusters: [time-series, prediction-markets]
related:
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/platforms/kalshi.md

## Raw Concept

- Original title: Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets
- Authors: Nam Anh Le
- Affiliation: National Economics University, Vietnam
- Type: PDF, research paper (arXiv preprint)
- Location: research for cemini/kalshi 2 3:29.pdf
- Length: ~30+ pages
- Retrieved: 2026-04-23
- Publication date: 2025 (arXiv preprint)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: time-series, prediction-markets

## Narrative

Le studies 292 million Kalshi trades and decomposes prediction-market miscalibration into domain-specific components via a hierarchical Bayesian model. Headline finding: an aggregate Brier score hides domain-level heterogeneity — political-event contracts are *systematically underconfident* (bias ≈ +0.15 vs. realized frequency), while weather and economic categories run closer to calibrated. The model estimates separate calibration parameters per domain, letting a trader target the miscalibrated buckets rather than the market as a whole.

The paper also quantifies a **trade-size scale effect**: calibration improves materially with trade size (Δ ≈ 0.53 in a fitted scaling parameter), suggesting larger traders carry more information and aggregate prices shift toward efficiency only once size thresholds are crossed. This has operational implications — small retail flow is noisier and a Bayesian filter that down-weights small trades on open-interest-light contracts recovers a cleaner fair-value estimate.

This is one of the higher-rigor prediction-market papers in the batch: very large trade sample, hierarchical Bayesian inference with proper posterior checks, and clean separation of bias vs. variance across domains. Most relevant as (a) a calibration layer for any Kalshi trading bot, and (b) empirical support for domain-conditional edge claims (politics > weather > macro for miscalibration).

## Key findings

- 292M Kalshi trades analyzed; 87.3% of calibration variance explained by domain-level hierarchical model.
- Political contracts systematically underconfident (bias ≈ +0.15 vs. realized outcome frequency).
- Trade-size scale effect: Δ ≈ 0.53 — larger trades significantly more calibrated than small.
- Domain decomposition beats aggregate Brier on a walk-forward evaluation.
- Methodology suggests per-domain calibration layer is the right abstraction for a Kalshi bot.

## Snippets

- **abstract** — "We decompose the calibration of prediction markets into domain-specific components" — the framing: aggregate numbers lie, domain-level numbers are actionable.
- **empirics** — Political contracts' persistent underconfidence is robust across multiple cycles, not a single-election artifact.
- **implications** — "Trade size is a material moderator of calibration" — small retail flow should be filtered or down-weighted before computing implied fair value.
