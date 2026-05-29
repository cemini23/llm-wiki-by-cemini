---
title: PTA metric backtest cadence
type: concept
tags: [meta, quant, backtest, pta, arcticdb, cadence]
keywords: [pta, price-to-52-week-anchor, reproduction]
related:
  - sources/pta-metric-anchoring-ssrn-4549819.md
  - meta/internal-benchmark-deployment-map.md
  - meta/equity-signal-backtest-cadence.md
maturity: core
created: 2026-05-29
updated: 2026-05-29
---

## Narrative

| Field | Value |
|-------|-------|
| **Compute** | **Laptop only** — `bash scripts/run_pta_backtest.sh` |
| **Data** | **cemini-librarian** ArcticDB `equity_bars` via SSH (`scripts/equity_signal_backtest/fetch.py`) |
| **Prod / egress** | **Never** — adoption brief only after pilot pass |
| **Last run** | 2026-05-29 — **FAIL** (−0.16% / −0.22% quintile spreads; stale 2017 bars) |
| **Next due** | On demand before any MAPPO / TimescaleDB PTA brief |
| **Report** | `.local/reports/pta-pilot-YYYY-MM-DD.md` |

User-gated. Re-run when librarian migrates fresher equity bars or before promoting PTA into prod feature vector.

## Relations

- @sources/pta-metric-anchoring-ssrn-4549819.md
- @meta/internal-benchmark-deployment-map.md
