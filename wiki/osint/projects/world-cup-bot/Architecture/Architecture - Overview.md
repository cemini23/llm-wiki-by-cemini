---
title: Architecture — World Cup Bot Overview
type: architecture-overview
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, world-cup-bot]
scanned-commit: 17a6647
ai-first: true
related:
  - projects/world-cup-bot/World Cup Bot.md
  - projects/world-cup-bot/Architecture/Architecture - world_cup_bot.md
  - projects/world-cup-bot/Architecture/Architecture - deploy.md
  - projects/world-cup-bot/Architecture/Architecture - Key decisions.md
  - projects/world-cup-bot/Architecture/OPEN-GAPS.md
  - entities/tools/world-cup-bot.md
maturity: validated
---

## Relations

- @projects/world-cup-bot/World Cup Bot.md
- @projects/world-cup-bot/Architecture/Architecture - world_cup_bot.md — main package
- @projects/world-cup-bot/Architecture/Architecture - deploy.md — systemd / wc_run
- @projects/world-cup-bot/Architecture/Architecture - Key decisions.md
- @projects/world-cup-bot/Architecture/OPEN-GAPS.md
- @entities/tools/world-cup-bot.md

## For future Claude

Codebase map for **cemini23/world-cup-bot** @ `17a6647`. Package entry: `world_cup_bot/__main__.py`. See module notes for deploy and `world_cup_bot/` tree.

## Narrative

Public MIT Polymarket FIFA 2026 advance-market LP + Kalshi cross-venue tooling. Prod runs on Cemini VPS via `deploy/systemd/`; flags default shadow/OFF per @projects/world-cup-bot/Architecture/OPEN-GAPS.md.
