---
title: "polymarket-quotebot (kamilch1k) — LP measurement / paper MM"
type: entity
tags: [tool, polymarket, lp-rewards, backtest, steal-from, k171]
keywords: [quotebot, q-score, markout, paper-mm, adverse-selection]
related:
  - concepts/polymarket-lp-comprehensive-backtest.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/cemini-pm-lp-vs-copy-capital-decision.md
  - entities/tools/yieldpilot.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- @concepts/polymarket-lp-comprehensive-backtest.md — primary steal-from for v2 backtest
- @concepts/polymarket-lp-rewards-farming.md — strategy context
- @concepts/cemini-pm-lp-vs-copy-capital-decision.md — measurement before capital
- @entities/tools/yieldpilot.md — sibling farm-bot heuristic

## Raw Concept

GitHub `kamilch1k/polymarket-quotebot` (public, updated 2026-07-15). Paper-first bot that **measures** whether small accounts can earn LP rewards: reward share vs real book, fills vs real tape, 30-minute adverse markouts. Phase 0 = no orders, no key.

## Narrative

**Steal-from / Phase-0 not required for Cemini adopt** — patterns only; do not deploy foreign bot on prod wallets.

Useful patterns:

- Accrue simulated rewards with published Q-shape; dollar figure needs calibration vs real payout.
- Fill only when prints cross **strictly through** quote (at-price assumed ahead in queue).
- Score every paper fill with 30m markout; net = rewards + spread − adverse.
- Hard live caps + kill on near-expiry / fast mid move (if ever used as reference).

Does **not** overturn Cemini empirical LP kill without Cemini-calibrated runs.

## Snippets

> "You can't *copy* a market maker (your copy crosses the spread he just earned — the sign flips at the boundary)." [Source: https://github.com/kamilch1k/polymarket-quotebot (retrieved 2026-07-16)]
