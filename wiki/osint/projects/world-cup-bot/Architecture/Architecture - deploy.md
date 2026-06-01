---
title: Architecture — deploy (systemd)
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
module: deploy
scanned-commit: 17a6647
tags: [architecture, world-cup-bot, systemd]
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
  - concepts/shadow-to-live-transition-engineering.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/Architecture/Architecture - Overview.md
- @concepts/shadow-to-live-transition-engineering.md — shadow → live gates

## For future Claude

**`deploy/systemd/`** ships generic operator units (no Cemini hostnames in git). Installed via `deploy/systemd/install-systemd.sh --profile monitor|trading`. Wrapper: `deploy/systemd/wc_run.sh` (prod may symlink from `/opt/cemini/scripts/wc_run.sh`). **Enable trading profile / `live-plan` timer only after** @projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md.

<!-- @generated:start -->

## Layout

| Path | Role |
| --- | --- |
| `deploy/systemd/install-systemd.sh` | Install timers/services for chosen profile |
| `deploy/systemd/wc_run.sh` | Invoke `world-cup-bot` with env from unit |
| `deploy/systemd/units/*.service` | One-shot or long-running jobs |
| `deploy/systemd/units/*.timer` | Cadence for scan, shadow-plan, cross-venue, etc. |
| `deploy/systemd/README.md` | Operator install notes |

## Monitor profile units (present in repo)

| Unit | Typical command |
| --- | --- |
| `world-cup-bot-shadow-plan` | `plan --record --liquidity-gate` |
| `world-cup-bot-cross-venue` | `cross-venue-scan` (add `--record` per prod brief) |
| `world-cup-bot-scan` / `discover` | discovery timers |
| `world-cup-bot-calendar-guard` | auto-cancel window |
| `world-cup-bot-conviction-staleness` / `fixture-check` | DR cadence helpers |
| `world-cup-bot-pnl-daily` | PnL rollup (shadow ledger, no L2) |
| `world-cup-bot-rewards-sync` | opt-in after Phase 2 L2 |
| `world-cup-bot-preflight` | connectivity burst |
| `world-cup-bot-live-plan` | trading profile (non-US host, post-SHADOW) |

Env vars such as `WC_LEDGER_PATH`, `DRY_RUN`, and phase-router flags are set in unit files or drop-ins — not committed with secrets.

<!-- @generated:end -->
