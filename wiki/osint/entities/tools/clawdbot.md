---
title: "Clawdbot — Claude-powered AI agent framework for Polymarket weather bots"
type: entity
tags: [entity, tool, polymarket, claude-bot-framework, weather-trading, automation, k55, openclaw-lineage]
keywords: [clawdbot, openclaw, coldmath, polymarket-weather-trader-1, pilot-aviation-reports, 24-7-bot, name-collision]
related:
  - entities/tools/openclaw.md
  - sources/openclaw-ios-node-2026-06-29.md
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - concepts/polymarket-weather-trading-strategy.md
  - entities/people/polymarketsuccubus.md
  - entities/people/polydao-mr-buzzoni.md
  - entities/platforms/polymarket.md
  - sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md
  - entities/people/coldmath-polymarket.md
  - concepts/polymarket-weather-bot-methodology-taxonomy.md
  - sources/alterego-eth-five-weather-methodologies-2026-05-27.md
maturity: draft
created: 2026-05-20
updated: 2026-06-29
---

## Relations

- @entities/tools/openclaw.md — **disambiguation:** Steinberger project renamed Clawdbot → Moltbot → **OpenClaw** (MIT); K55 Posts.docx "Clawdbot" may name ColdMath's stack OR pre-rename framework [TENTATIVE]
- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — K55 Posts.docx Post 5 references Clawdbot as the framework underpinning ColdMath (#1 weather trader, +$124K PnL)
- @concepts/polymarket-weather-trading-strategy.md — concept page where Clawdbot is now cross-referenced
- @entities/people/polymarketsuccubus.md — referencing creator
- @entities/people/polydao-mr-buzzoni.md — K57 weather post watchlist cites ColdMath stack
- @sources/alterego-eth-coldmath-weather-deconstruction-2026-05-24.md — K61 micro-scaling + narrow-bin forensics on ColdMath
- @concepts/polymarket-weather-bot-methodology-taxonomy.md — K70 type 5 cites Claude-powered agents (ColdMath lineage)
- @sources/alterego-eth-five-weather-methodologies-2026-05-27.md — K70 source
- @entities/people/coldmath-polymarket.md — operator entity

## Raw Concept

K55 ingest surfaces Clawdbot as "a Claude-powered AI agent framework" used by ColdMath, the #1-ranked weather-market trader on Polymarket per the @polysuccubus Top-7 ranking. The framework is mentioned but not deep-described in the source post; this page records what is known and flags follow-up Phase-0.

## Narrative

### Source attribution (from K55 Posts.docx Post 5)

> "[ColdMath] doesn't trade manually. Instead, he runs a highly sophisticated automated trading bot built on Clawdbot (a Claude-powered AI agent framework). ColdMath himself developed and refined this bot, which scans real-time weather data from multiple sources (including pilot aviation reports), compares it against market prices 24/7, and executes trades with machine-like precision."

### Reported usage

| Operator | Framework | Strategy | Result (per Parity/@polysuccubus) |
|---|---|---|---|
| ColdMath | Clawdbot | Real-time weather data → pilot aviation reports → market-price comparison → small-entry-large-payout trades | +$124,896 PnL, 81.7% WR, 6,575 predictions, biggest single win $12,400 |

### Open questions [NEEDS VERIFICATION 2026-05-20]

1. **Same artifact as OpenClaw?** The public **OpenClaw** gateway (formerly Clawdbot/Moltbot, MIT, @entities/tools/openclaw.md) may be what ColdMath's post meant — confirm via ColdMath primary source before merging pages.
2. **License?** If OpenClaw: **MIT** confirmed (2026-06-29). If separate proprietary fork: reference-only.
3. **Architecture?** If OpenClaw: gateway + optional iOS node; weather bot = gateway skills/channels on isolated host.
4. **Adoption surface?** OpenClaw **Tier C NO-GO** on cemini-prod trading; **Tier A CONDITIONAL-GO** for operator personal gateway only (@sources/openclaw-ios-node-2026-06-29.md).

### Cemini-relevant signal

Whether or not Clawdbot is adoptable, the **datapoint that a Claude-driven bot framework was the #1 performer** in a competitive Polymarket vertical is meaningful. It validates that LLM-orchestrated trading agents in narrow domains (with clean data feeds + price-comparison logic + small-entry-large-payout discipline) can outperform manual operators by a significant margin. The 81.7% WR + 6,575-trade volume is exceptional regardless of framework name.

### Cemini fit

- **If OpenClaw lineage [TENTATIVE]:** evaluate via @entities/tools/openclaw.md — not a PM bot framework substitute; weather strategy class remains the takeaway.
- **If proprietary ColdMath fork:** Reference-only; compare to Hermes (@entities/tools/hermes-agent.md) for self-hosted agent patterns.

### Follow-up action

Confirm ColdMath ↔ OpenClaw link via operator OSINT or primary tweet/repo. Until then, keep this page as **name-collision stub** pointing to @entities/tools/openclaw.md for the public framework.
