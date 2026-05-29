---
title: Diagnosing Trading Model Failures — Vectorized vs Event-Driven, Drift, Promotion Matrix
type: source
tags: [source, quant-validation, model-diagnostics, drift, k77]
keywords: [vectorized-backtest, event-driven, PSI, ADDM, calibration, threshold, promote-recalibrate-retrain]
related:
  - concepts/trading-model-failure-diagnostics.md
  - concepts/zero-trade-edge-signal-diagnostics.md
  - concepts/brier-score-model-promotion-framework.md
maturity: draft
read_status: read
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @concepts/trading-model-failure-diagnostics.md
- @concepts/zero-trade-edge-signal-diagnostics.md
- @concepts/brier-score-model-promotion-framework.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Diagnosing Trading Model Failures |
| Type | docx |
| Location | `cemini-librarian:/opt/cemini-bulk/research/Diagnosing Trading Model Failures.docx` |
| Retrieved | 2026-05-28 |
| Read-status | deep-read |

## Narrative

Failure taxonomy for quant models:

- **Engine mismatch:** vectorized backtest ≠ event-driven live (lookahead, fill assumptions) — brain v2 Arctic path must use walk-forward event semantics
- **Feature drift:** PSI / ADDM on inputs — prod paper @ 0.77 vs backtest @ 0.68 may be threshold *or* calibration shift
- **Decision matrix:** promote vs recalibrate vs retrain based on where loss concentrates (resolution vs reliability vs execution)

Ties to R7 HOLD_OVERFIT_RISK: allowlist win may be **selection bias** not alpha — run full-universe + CPCV before promotion.

## Snippets

> Threshold tuning on miscalibrated probabilities optimizes the wrong objective; fix calibration before moving buy_threshold. [Source: Diagnosing Trading Model Failures.docx — paraphrase]
