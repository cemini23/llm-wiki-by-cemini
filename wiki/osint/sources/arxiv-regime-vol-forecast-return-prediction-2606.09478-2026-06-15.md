---
title: "Volatility Forecasting and Return Prediction under Market Regimes — CSI 300 (arXiv 2606.09478, 2026)"
type: source
tags: [source, volatility-forecasting, regime-switching, harq, xgboost, walk-forward, k117]
keywords: [HARQ, GJR-GARCH, markov-switching, low-vol-gating, turnover-control, csi-300]
related:
  - concepts/markov-regime-switching-models.md
  - concepts/time-series-arima-garch-framework.md
  - concepts/regime-conditioned-evaluation.md
  - meta/equity-signal-backtest-cadence.md
  - sources/arxiv-bavar-bled-portfolio-regime-2606-09104-2026-06-09.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
clusters: [quant-finance, time-series, ml-methods]
---

## Relations

- @concepts/markov-regime-switching-models.md — regime detection machinery
- @concepts/time-series-arima-garch-framework.md — GARCH vol-scaling discipline
- @concepts/regime-conditioned-evaluation.md — disclose regime in backtests
- @meta/equity-signal-backtest-cadence.md — laptop quarterly equity harness
- @sources/arxiv-bavar-bled-portfolio-regime-2606-09104-2026-06-09.md — sibling regime-aware portfolio DRL

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data |
| **Authors** | Fang, Ślepaczuk (University of Warsaw) |
| **arXiv** | 2606.09478 |
| **sha256** | `399e2ff424309ccb…` |
| **Location** | `.local/archives/research/arxiv-2606.09478-volatility-forecasting-and-return-prediction-und.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (abstract + §2–4 methodology + walk-forward design) |

## Narrative

Two-stage **walk-forward** framework on CSI 300 5-minute data (2005–2023):

**Stage 1 — volatility:** log-HARQ baseline augmented with **Markov-switching GJR-GARCH** filtered regime probabilities on HARQ residuals. Regime-aware specs beat baseline HARQ on forecast metrics with formal comparison-test support.

**Stage 2 — returns:** **XGBoost** one-step-ahead return model fed vol forecasts, regime indicators, and lagged return features — strictly OOS (expanding window, quarterly re-fit).

**Headline asymmetry:**

| Lane | Finding |
|------|---------|
| Volatility forecasting | Regime info **helps** consistently |
| Return prediction | Weak, **state-dependent** — economically relevant signal concentrated in **low-volatility regimes** |
| Naive strategies | Fail after realistic transaction costs |
| Engineered strategies | **Vol scaling + low-vol gating + threshold calibration + turnover controls** can improve defensive performance — implementation-sensitive |

**Cemini posture:** **REFERENCE** for equity-signal harness — reinforces existing wiki emphasis that **GARCH/vol scaling beats directional alpha** (@concepts/time-series-arima-garch-framework.md). Steal **low-vol regime gating** as a quarterly backtest diagnostic before promoting equity briefs to prod. CSI 300 ≠ US watchlist — replicate on laptop Arctic panel before prod claims.

## Snippets

> "Regime-aware volatility forecasting consistently outperforms baseline HARQ models… In contrast, return predictability remains weak, state-dependent, and concentrated primarily in low-volatility regimes." [Source: arxiv-2606.09478-volatility-forecasting-and-return-prediction-und.pdf abstract]

> "The practical value of predictive systems in financial markets may depend less on generating strong unconditional return forecasts and more on transforming weak state-dependent signals into economically robust portfolio allocation rules." [Source: arxiv-2606.09478-volatility-forecasting-and-return-prediction-und.pdf abstract]

> "Walk-forward evaluation… mimics real-time forecasting and prevents the use of future information." [Source: arxiv-2606.09478-volatility-forecasting-and-return-prediction-und.pdf §3.3]
