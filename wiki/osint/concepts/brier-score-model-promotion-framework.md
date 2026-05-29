---
title: Brier score model promotion framework — six-stage institutional gate
type: concept
tags: [concept, quant-validation, brier-score, model-promotion, brain-v2, k77]
keywords: [brier-score, BSS, murphy-decomposition, CPCV, diebold-mariano, HLN, PBO, ROPE, calibration]
related:
  - sources/algorithmic-trading-model-benchmarking-framework-2026-05-28.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - concepts/trading-model-failure-diagnostics.md
  - sources/diagnosing-trading-model-failures-2026-05-28.md
maturity: draft
created: 2026-05-28
updated: 2026-05-29
---

## Relations

- @sources/algorithmic-trading-model-benchmarking-framework-2026-05-28.md
- @concepts/monte-carlo-permutation-test-mcpt.md — trade-level MCPT complements forecast-level Brier
- @concepts/regime-conditioned-evaluation.md — CPCV + regime tables
- @concepts/lp-algorithm-live-promotion-gates.md — add Brier/calibration pillar for PM probability engines
- @concepts/zero-trade-edge-signal-diagnostics.md — miscalibrated probs → zero fills or toxic entries

## Raw Concept

K77 ingest: institutional promotion pipeline for **probabilistic** models — applies to brain_playbook_v2 confidence scores, PM fair-value probs, LP fill forecasts.

## Narrative

### Six stages (sequential)

| Stage | Gate | Fail action |
|-------|------|-------------|
| 1 | Embargoed **CPCV** only | Reject — leakage invalidates all metrics |
| 2 | Murphy **reliability** ≤ tolerance; Platt/isotonic if overconfident | Recalibrate head; do not promote raw logits |
| 3 | **BSS > 0** vs base rate on OOS folds | HOLD — no edge vs naive |
| 4 | **HLN-DM** + block bootstrap on loss differential | HOLD if n small |
| 5 | Bayesian **ROPE** — delta must matter operationally | HOLD if statistically real but tiny |
| 6 | **PBO** low across full hyperparameter search | REJECT — data-mined winner |

### Cemini mapping

- **R7 brain allowlist:** extend walk-forward JSON with per-policy Brier/BSS on proxy scores; MCPT on trade PnL is necessary but not sufficient.
- **LP / PM:** pair with @concepts/lp-algorithm-live-promotion-gates.md — add calibration table before live size.
- **Live paper @ 0.77 avg vs backtest @ 0.68:** treat as **reliability drift** — run calibration layer (R8) before threshold promotion.

## Snippets

> Brier score: mean squared error of probabilistic forecasts; 0.25 = constant 50% predictor. [Source: Algorithmic Trading Model Benchmarking Framework.docx]
