---
title: PM LP backtest cadence
type: concept
tags: [meta, polymarket, backtest, cadence]
keywords: [pm-lp, backtest, quarterly, ritual]
related:
  - concepts/cemini-backtest-report-kit.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-comprehensive-backtest.md
  - meta/internal-benchmark-deployment-map.md
  - meta/hl-funding-backtest-cadence.md
  - meta/kalshi-lp-backtest-cadence.md
  - concepts/market-informedness-market-making.md
maturity: core
created: 2026-05-27
updated: 2026-07-16
---

## Relations

- @concepts/cemini-backtest-report-kit.md — kit + PM pilot
- @concepts/polymarket-lp-bot-phase0-spec.md — strategy gates
- @concepts/polymarket-lp-comprehensive-backtest.md — **v2** Q-score + markout target (supersedes proxy-only interpretation of this ritual)
- @meta/hl-funding-backtest-cadence.md — parallel HL funding ritual

## Narrative

| Field | Value |
|-------|-------|
| **Last run (v1 proxy)** | 2026-05-27 |
| **Next due** | 2026-08-27 (or sooner when v2 engine ships) |
| **Command** | `bash scripts/run_pm_lp_backtest.sh` |
| **Check** | `scripts/check_pm_lp_backtest_due.sh` |

User-gated — agent prompts when due; does not auto-run. Re-run when changing LP spread tiers or before prod LP briefs.

### v1 vs v2

- **v1 (current runner):** reward-proxy + mid-crossing adverse — useful for report-kit plumbing only. OpenSpec disclaimer still applies.
- **v2 (in progress):** official \(Q_{\min}\) scoring, trade-tape fills, 30m markout, capital × $1/day clearance — see `@concepts/polymarket-lp-comprehensive-backtest.md` + prod brief `pm-2026-07-16_comprehensive-lp-backtest.md`.
