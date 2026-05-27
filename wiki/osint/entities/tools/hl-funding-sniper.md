---
title: "hl-funding-sniper — Hyperliquid funding-rate capture bot (TheSmartApe)"
type: entity
tags: [entity, tool, hyperliquid, funding-rate, open-source]
keywords: [hl-funding-sniper, thesmartape, hyperliquid-funding-bot, funding-rate-spike, telegram-alerts]
related:
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/platforms/hyperliquid.md
  - entities/people/the-smart-ape.md
  - sources/trading-posts-compilation-25-2026-05-27.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @concepts/perps-dex-funding-carry-strategy.md — strategy template
- @entities/platforms/hyperliquid.md
- @entities/people/the-smart-ape.md — author post
- @sources/trading-posts-compilation-25-2026-05-27.md — Post 16

## Raw Concept

Open-source bot referenced in K72 @the_smart_ape post: `https://github.com/TheSmartApe/hl-funding-sniper` — **license not verified in ingest** [NEEDS VERIFICATION 2026-05-27].

## Narrative

### Claimed features (post) [TENTATIVE]

- Monitors funding spikes (e.g. +80% APR alts), shorts to collect funding + mean-reversion
- Config-driven thresholds (no magic numbers in code)
- Backtest engine, Rich TUI, Telegram alerts
- Native HL stop-loss / take-profit triggers

### Cemini posture

- **Reference-only** until `gh api` license + Phase-0 vs existing Hyperliquid adapter on cemini-egress-fi
- Architecture lessons already captured on @concepts/perps-dex-funding-carry-strategy.md (K55 @morpphhhaw + K72 reinforcement)
- **Do not** run third-party trading keys on prod from this workspace
