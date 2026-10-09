---
title: Kalshi LP backtest cadence
type: concept
tags: [meta, kalshi, backtest, cadence]
keywords: [kalshi-lp, backtest, quarterly]
related:
  - concepts/cemini-backtest-report-kit.md
  - concepts/kalshi-api-reference.md
  - meta/pm-lp-backtest-cadence.md
  - entities/platforms/kalshi.md
maturity: core
created: 2026-05-27
updated: 2026-10-09
---

## Relations

- @concepts/cemini-backtest-report-kit.md — Phase 1 Kalshi pilot
- @concepts/kalshi-api-reference.md — candlesticks + trades API
- @meta/pm-lp-backtest-cadence.md — sibling PM ritual

## Narrative

| Field | Value |
|-------|-------|
| **Last run** | 2026-10-09 |
| **Next due** | 2027-01-07 |
| **Command** | `bash scripts/run_kalshi_lp_backtest.sh` |
| **Check** | `scripts/check_kalshi_lp_backtest_due.sh` |

User-gated quarterly re-run before Kalshi MM / arb briefs.
