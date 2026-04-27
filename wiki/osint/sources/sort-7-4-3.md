---
title: Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection
type: source
tags: [pdf, portfolio-strategy, ml-methods, time-series]
related:
  - concepts/portfolio-strategy.md
  - entities/components/kelly-cvar-risk-engine.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-26
clusters:
  - portfolio-strategy
  - ml-methods
  - time-series
---

## Relations

- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub (Q 2026-04-27)
- @entities/components/kelly-cvar-risk-engine.md — risk engine covering options-derivatives and portfolio-strategy concepts

## Raw Concept

- Original title: Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection
- Authors: Ryan Engel, Chen (co-author), Polak (co-author), Boier (co-author)
- Affiliation: Stony Brook University + NVIDIA
- Type: PDF, conference paper (ICAIF '25)
- Location: research for cemini/sort 7 4:3.pdf
- Length: ~15+ pages
- Retrieved: 2026-04-23
- Publication date: 2025 (ICAIF '25)
- Read status: deep-read
- Primary cluster: time-series
- All clusters: portfolio-strategy, ml-methods, time-series

## Narrative

The authors extend the Conditional Autoencoder (CAE) approach to equity factor modeling by adding an explicit uncertainty layer: CAE produces factor loadings per name/period, then Chronos (time-series foundation model) generates distributional forecasts of factor returns, then XGBoost-quantile does uncertainty-aware factor selection — picking factors whose expected return-to-uncertainty ratio clears a threshold. The pipeline runs at S&P-500 scale and is benchmarked against vanilla CAE and Fama-French baselines.

Results: the uncertainty-aware selection materially improves out-of-sample Sharpe and max drawdown vs. CAE-alone on a rolling-window backtest. The contribution is less about the individual components (CAE, Chronos, XGBoost are all existing) and more about the *composition* — using a foundation model's distributional output to gate factor inclusion is a clean, reproducible idea with clear hooks for a GPU-less deployment (Chronos can run on CPU at batch cadence; XGBoost is CPU-native).

ICAIF '25 venue gives this paper a decent peer-review floor. For Cemini specifically, the gating layer (distributional forecast → quantile threshold → select/reject factor) is an architectural pattern directly applicable to any factor-based portfolio construction block.

## Key findings

- CAE + Chronos + XGBoost-quantile three-stage factor modeling pipeline.
- Uncertainty-aware factor selection beats vanilla CAE on rolling Sharpe and max drawdown.
- Scales to S&P-500 universe; computational profile is CPU-friendly at batch cadence.
- ICAIF '25 peer-reviewed; methodology is reproducible with off-the-shelf components.
- Core contribution is architectural: distributional forecast → quantile threshold → factor gate.

## Snippets

- **abstract** — "We use Chronos to produce distributional forecasts of factor returns, then XGBoost-quantile for uncertainty-aware factor selection" — the clean three-stage pipeline.
- **results** — Uncertainty-gated portfolios dominate the CAE-only baseline on Sharpe and MDD in rolling windows.
- **engineering** — "The pipeline is designed for batch cadence and does not require GPU inference at runtime" — directly relevant to CPU-only deployment.
