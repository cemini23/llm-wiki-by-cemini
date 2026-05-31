---
title: "Polymarket negative-filter trading — what not to trade first"
type: concept
tags: [concept, polymarket, bot-design, risk, k88]
keywords: [negative filter, myttle, trade selection, polymarket bot]
related:
  - sources/trading-posts-compilation-42-2026-05-31.md
  - concepts/polymarket-bot-architecture.md
  - concepts/world-cup-advance-market-bot-v1.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @sources/trading-posts-compilation-42-2026-05-31.md — Post 10 (@myttle_web3)
- @concepts/polymarket-bot-architecture.md — operator taxonomy
- @concepts/world-cup-advance-market-bot-v1.md — world-cup-bot applies liquidity + conviction gates before entry

## Raw Concept

K88 @myttle_web3 thread: PM bot builders optimize execution speed before fixing **selection** — most PnL leakage is trading markets that should have been skipped.

## Narrative

**Negative filter before alpha:** classify markets/trades into pass/skip using historical self-analysis (spread, resolution risk, category fit, time-to-event). Aligns with world-cup-bot **liquidity gate** + **conviction** layers — speed optimizations (FOK, websocket) only matter after skip logic is calibrated.

`[TENTATIVE]` — promoter PnL not independently verified; pattern is structurally sound for Cemini bot design reviews.

## Snippets

> "I wanted a Polymarket bot to trade faster. then i looked at my own trades and realized speed was not the first problem." [Source: Posts.docx K88 Post 10, @myttle_web3]
