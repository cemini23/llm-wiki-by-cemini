---
title: PM LP backtest cadence
type: concept
tags: [meta, polymarket, backtest, cadence]
keywords: [pm-lp, backtest, quarterly, ritual]
related:
  - concepts/cemini-backtest-report-kit.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - meta/hl-funding-backtest-cadence.md
maturity: core
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @concepts/cemini-backtest-report-kit.md — kit + PM pilot
- @concepts/polymarket-lp-bot-phase0-spec.md — strategy gates
- @meta/hl-funding-backtest-cadence.md — parallel HL funding ritual

## Narrative

| Field | Value |
|-------|-------|
| **Last run** | 2026-05-27 |
| **Next due** | 2026-08-27 |
| **Command** | `bash scripts/run_pm_lp_backtest.sh` |
| **Check** | `scripts/check_pm_lp_backtest_due.sh` |

User-gated — agent prompts when due; does not auto-run. Re-run when changing LP spread tiers or before prod LP briefs.
