---
title: World Cup Bot (repo)
type: project
status: active
date: 2026-06-01
updated: 2026-06-01
tags: [project, architecture, world-cup-2026, polymarket, open-source]
keywords: [world-cup-bot, cemini23, advance-lp, MIT, shadow-mode]
local-path: /Users/claudiobarone/Desktop/projects/world-cup-bot
github: cemini23/world-cup-bot
ai-first: true
related:
  - projects/world-cup-bot/Architecture/Architecture - Overview.md
  - projects/world-cup-bot/Architecture/Architecture - world_cup_bot.md
  - projects/world-cup-bot/Architecture/Architecture - deploy.md
  - projects/world-cup-bot/Architecture/Architecture - Key decisions.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - projects/world-cup-bot/CLOB-V2-live/Index.md
  - projects/world-cup-bot/CLOB-V2-live/OPEN-GAPS.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - CLOB V2 patch spec.md
  - projects/world-cup-bot/CLOB-V2-live/World Cup Bot - egress live layout.md
  - projects/world-cup-bot/CLOB-V2-live/README.md
  - entities/tools/world-cup-bot.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - projects/cemini-financial-suite/Cemini Financial Suite.md
maturity: validated
---

## Relations

- [[projects/world-cup-bot/Architecture/Architecture - Overview|Architecture - Overview]] — codebase map @ `17a6647` (`/obsidian-architect`)
- [[projects/world-cup-bot/Architecture/Architecture - Key decisions|Architecture - Key decisions]] — ADRs + commit-mined decisions
- [[projects/world-cup-bot/Architecture/OPEN-GAPS|OPEN-GAPS]] — deferred operator + doc gaps after architect pass
- @entities/tools/world-cup-bot.md — entity/tool page (features, prod boundary)
- @concepts/world-cup-advance-market-bot-v1.md — private Cemini spec (shared codebase history)

## For future Claude

Project hub for the **public MIT** repo `cemini23/world-cup-bot`: Polymarket FIFA 2026 advance-market LP bot + Kalshi cross-venue alerts/paper/exec. Entry CLI: `world-cup-bot` → `world_cup_bot/__main__.py`. Maintainer prod runs same code on VPS with private `.env`; CeminiSuite imports via briefs only. Refresh architecture from `Architecture - Overview.md` (`scanned-commit: 17a6647`).

## Overview

| Field | Value |
| --- | --- |
| **Role** | Conviction LP + shadow gates + cross-venue paper/exec (flags default OFF) |
| **Canonical path** | `/Users/claudiobarone/Desktop/projects/world-cup-bot` |
| **Logic versions** | `wc_advance_lp_v4`, `wc_cross_venue_paper_v1`, `wc_cross_venue_exec_v1` |
| **CI** | `.github/workflows/ci.yml` — pytest, ruff, threshold guard, TruffleHog, vet docs |

## Architecture notes

- [[projects/world-cup-bot/Architecture/Architecture - Overview|Architecture - Overview]]
- [[projects/world-cup-bot/Architecture/Architecture - world_cup_bot|Architecture - world_cup_bot]]
- [[projects/world-cup-bot/Architecture/Architecture - deploy|Architecture - deploy]]
- [[projects/world-cup-bot/Architecture/Architecture - Key decisions|Architecture - Key decisions]]
- [[projects/world-cup-bot/Architecture/OPEN-GAPS|OPEN-GAPS]]
- [[projects/world-cup-bot/CLOB-V2-live/Index|CLOB V2 live handoff]] — `order_version_mismatch` patch spec (prod 2026-06-01)

## Recent activity

- **2026-06-01** — CLOB V2 handoff ingested; `py-clob-client-v2` patch implemented (pending push).
- **2026-06-01** — Prod brief `2026-06-01_wc-prod-bugbot-exports-pull.md` → `/opt/cemini/briefs/`.
