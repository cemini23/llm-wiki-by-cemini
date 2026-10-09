---
title: Equity signal backtest cadence
type: concept
tags: [meta, equities, backtest, arcticdb, cadence]
keywords: [equity, momentum, arcticdb, quarterly]
related:
  - sources/goldman-sachs-eq-positioning-key-levels-2026-06-08.md
  - concepts/cemini-backtest-report-kit.md
  - entities/tools/arcticdb.md
  - meta/internal-benchmark-deployment-map.md
  - meta/librarian-decommission-2026-06-14.md
  - sources/arxiv-regime-vol-forecast-return-prediction-2606.09478-2026-06-15.md
  - meta/pta-backtest-cadence.md
maturity: core
created: 2026-05-27
updated: 2026-10-09
---

## Narrative

| Field | Value |
|-------|-------|
| **Last run** | 2026-10-09 |
| **Next due** | 2027-01-07 |
| **Command** | `bash scripts/run_equity_signal_backtest.sh` |
| **Requires** | Laptop Arctic `.local/arctic-market-dataset/` or `scripts/refresh_arctic_equity_bars.py` — **not** `ssh cemini-librarian` (deleted 2026-06-14) |

User-gated quarterly. Re-run before promoting new equity signals to prod briefs.
