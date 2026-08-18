---
title: Clean-room software design — GPL isolation for trading bot forks
type: concept
tags: [concept, legal, clean-room, pmxt, discountifu, k77]
keywords: [clean-room, GPL, AGPL, reverse-engineering, pmxt, discountifu, trade-secret]
related:
  - sources/clean-room-design-proprietary-software-2026-05-28.md
  - entities/tools/discountifu-polymarket-trading-bot.md
  - concepts/polymarket-bot-architecture.md
  - concepts/clob-rate-limit-mitigation-strategies.md
  - sources/arxiv-2608.16112-strategic-technical-debt-2026-08-18.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/clean-room-design-proprietary-software-2026-05-28.md
- @entities/tools/discountifu-polymarket-trading-bot.md
- @concepts/polymarket-bot-architecture.md
- @concepts/clob-rate-limit-mitigation-strategies.md — WS behavior spec'd black-box

## Raw Concept

K77: legal/technical pattern for R11 (discountifu diff) and pmxt integration without license bleed.

## Narrative

### R11 workflow (spec-only)

1. Black-box observe discountifu: WS reconnect cadence, order types, rate behavior — **no source paste into cemini/**
2. Write functional spec in brief; implement in prod with different module layout
3. Diff report = behavioral parity tests, not line diff

### When clean-room is insufficient

Direct fork of AGPL bot into prod path → **NO-GO** without legal review. Prefer py-clob-client (MIT) + in-house orchestration.

## Snippets

> Specification team never reads reference source; implementation team never reads proprietary legacy. [Source: Clean-Room Design for Proprietary Software.docx]
