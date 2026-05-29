---
title: Equity signal backtest cadence
type: concept
tags: [meta, equities, backtest, arcticdb, cadence]
keywords: [equity, momentum, arcticdb, quarterly]
related:
  - concepts/cemini-backtest-report-kit.md
  - entities/tools/arcticdb.md
  - meta/internal-benchmark-deployment-map.md
  - meta/pta-backtest-cadence.md
maturity: core
created: 2026-05-27
updated: 2026-05-27
---

## Narrative

| Field | Value |
|-------|-------|
| **Last run** | 2026-05-27 |
| **Next due** | 2026-08-27 |
| **Command** | `bash scripts/run_equity_signal_backtest.sh` |
| **Requires** | `ssh cemini-librarian` + ArcticDB `equity_bars` |

User-gated quarterly. Re-run before promoting new equity signals to prod briefs.
