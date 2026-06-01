---
title: World Cup Bot CLOB V2 live — index
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [world-cup-bot, clob-v2, prod-handoff]
ai-first: true
related:
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - egress live layout.md
  - projects/world-cup-bot/CLOB-V2-live/OPEN-GAPS.md
  - projects/world-cup-bot/CLOB-V2-live/README.md
  - entities/tools/world-cup-bot.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/World Cup Bot.md — project hub
- @entities/tools/world-cup-bot.md — public OSS entity

# World Cup Bot — CLOB V2 live patch pack

## Pages

- [[World Cup Bot - CLOB V2 patch spec]] — **start here** (repo patches)
- [[World Cup Bot - egress live layout]] — cemini-prod vs egress-fi systemd
- [[OPEN-GAPS]] — follow-ups after V2 merge

## Context

Shadow soak on **cemini-prod** completed Phase 1. **egress-fi** trading units installed 2026-06-01. Live POST blocked by **`order_version_mismatch`** until `py-clob-client-v2` lands in the public repo (**shipped** @ `7054500`).

## Quick links

| Item | Path |
|------|------|
| Public repo | `github.com/cemini23/world-cup-bot` |
| Cemini wrapper | `/opt/cemini/scripts/wc_run.sh` |
| Egress installer | `/opt/cemini/deploy/systemd/install-wc-egress.sh` |
| Shadow ledger (prod) | `/opt/cemini/logs/wc_shadow_ledger.jsonl` |
| Live ledger (egress) | `/opt/cemini/logs/wc_ledger.jsonl` |
