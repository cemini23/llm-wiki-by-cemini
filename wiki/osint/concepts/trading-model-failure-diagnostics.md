---
title: Trading model failure diagnostics — promote / recalibrate / retrain matrix
type: concept
tags: [concept, quant-validation, drift, calibration, brain-v2, k77]
keywords: [PSI, ADDM, vectorized-backtest, event-driven, calibration-drift, threshold-tuning]
related:
  - sources/diagnosing-trading-model-failures-2026-05-28.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - concepts/brier-score-model-promotion-framework.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/algorithmic-auditing-covariance-regret.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/diagnosing-trading-model-failures-2026-05-28.md
- @concepts/zero-trade-edge-signal-diagnostics.md — execution-side abort vs model-side
- @concepts/brier-score-model-promotion-framework.md — reliability fixes
- @concepts/regime-conditioned-evaluation.md — regime-specific drift

## Raw Concept

K77: structured triage when backtest/live diverge or R7 returns HOLD.

## Narrative

### Diagnosis order

1. **Engine parity** — walk-forward event loop vs vectorized sweep (R7 script)
2. **Feature PSI** — input distribution shift post-2017 Arctic gap / live paper window
3. **Calibration** — reliability curve; if broken → recalibrate (Platt/isotonic), not threshold bump
4. **Threshold** — only after calibration OK
5. **Retrain** — only if resolution collapses across regimes

### R8 proxy-live checklist extension

Add: log `model_score_raw`, `model_score_calibrated`, `buy_threshold`, `abort_reason` per signal — enables matrix routing without guessing.

## Snippets

> Vectorized backtests systematically overstate edge when fills and latency are optimistic. [Source: Diagnosing Trading Model Failures.docx]
