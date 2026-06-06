---
title: MrFadiAi/Polymarket-bot — streak sizing + multi-layer risk gates
type: entity
tags: [entity, tool, polymarket, steal-from, phase-0, k102]
keywords: [polymarket-bot, streak-sizing, drawdown, risk-gates, nodejs]
related:
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - entities/tools/world-cup-bot.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
maturity: validated
created: 2026-06-06
updated: 2026-06-06
phase_0_verdict: STEAL-FROM
license_verified: MIT
repo: https://github.com/MrFadiAi/Polymarket-bot
---

## Relations

- @entities/tools/world-cup-bot.md — Python OSS target for ported sizing logic
- @concepts/world-cup-advance-market-bot-v1.md — Module 7 ledger/rewards

## Raw Concept

K102 eval Steal-from; eval claimed NO LICENSE → **MIT verified** (`gh api` + LICENSE file, 2026-06-06). ~206★; Node.js/TypeScript stack — **no direct adopt** on `/opt/cemini` Python path.

## Narrative

Reference implementation for **four-layer PnL protection** and **streak-based dynamic position sizing** (`bot-config.ts` / `bot-with-dashboard.ts` v3.1):

| Gate | Threshold | Action |
|------|-----------|--------|
| Daily loss | 5% of capital | 60 min pause |
| Monthly loss | 15% | 30-day pause |
| Peak drawdown | 25% | 7-day pause |
| Total loss | 40% | **Permanent halt** |

Dynamic sizing (when `enableDynamicSizing`):

- After **>2 consecutive losses**: multiply size by `(1 − 0.20)^(losses − 2)`
- After **>3 consecutive wins**: multiply by `1 + min(wins − 3, 5) × 0.10`
- Floor 1% / ceiling 5% of capital per trade

**Phase-0 verdict: STEAL-FROM** — port math to `world-cup-bot` conviction YAML + ledger module; do not run Node bot on prod.

## Snippets

> `lossSizingReduction: 0.20` / `winSizingIncrease: 0.10` with `Math.pow(1 - reduction, consecutiveLosses - 2)` [Source: MrFadiAi/Polymarket-bot `bot-config.ts`; K102 clone]
