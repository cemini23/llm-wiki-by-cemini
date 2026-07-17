---
title: "YieldPilot — Polymarket Q-score LP farming bot"
type: entity
tags: [tool, polymarket, lp-rewards, steal-from, k171]
keywords: [YieldPilot, Q-score, maxSpread, FARM_SPREAD_FRACTION]
related:
  - concepts/polymarket-lp-comprehensive-backtest.md
  - concepts/polymarket-lp-rewards-farming.md
  - entities/tools/polymarket-quotebot.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- @concepts/polymarket-lp-comprehensive-backtest.md — heuristic input for spread grid
- @concepts/polymarket-lp-rewards-farming.md — LP farming context
- @entities/tools/polymarket-quotebot.md — complementary measurement rig

## Raw Concept

GitHub `Bachamht/YieldPilot` — farms Polymarket daily Q-score rewards with persistent two-sided quotes. Default quote distance ≈ **40% of `maxSpread`** (`FARM_SPREAD_FRACTION`).

## Narrative

**Reference / steal-from only.** Useful default for v2 sweep mid-point between tight (high Q, more fills) and wide (low Q, fewer fills). Live Q estimator samples YES/NO books — align with official docs, not a substitute for Cemini markout gates.

## Snippets

> YieldPilot quotes at maxSpread × 40% from mid by default. [Source: https://github.com/Bachamht/YieldPilot (retrieved 2026-07-16)]
