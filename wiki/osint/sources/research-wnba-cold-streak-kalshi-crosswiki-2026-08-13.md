---
title: "Cross-wiki — WNBA cold-streak / last-2:00 Kalshi research (2026-08-13)"
type: source
tags: [source, research, wnba, kalshi, cross-wiki, live-betting]
keywords: [wnba, kalshi, quarter total, last two minutes, cold streak, espn pbp]
related:
  - entities/platforms/kalshi.md
  - concepts/kalshi-api-reference.md
  - concepts/gambling-wiki-federation.md
  - "@gambling-wiki/entities/sports/wnba-betting.md"
  - "@gambling-wiki/sources/research-wnba-cold-streak-live-unders-2026-08-13.md"
  - "@gambling-wiki/entities/platforms/kalshi.md"
read_status: deep-read
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @gambling-wiki/entities/sports/wnba-betting.md — **canonical strategy synthesis** (PBP edge tables, social, bot posture)
- @gambling-wiki/sources/research-wnba-cold-streak-live-unders-2026-08-13.md — methods + artifact paths
- @entities/platforms/kalshi.md — Cemini venue / execution home
- @concepts/kalshi-api-reference.md — public series listing + game_stats WNBA note
- @concepts/gambling-wiki-federation.md — retail strategy stays on gambling-wiki
- @gambling-wiki/entities/platforms/kalshi.md — retail Kalshi entity (WNBA series section)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WNBA cold-streak / last-2:00 live unders — OSINT cross-wiki pointer |
| **Type** | Operator research (cross-wiki) |
| **Location** | Strategy + tables: gambling-wiki; this page = Kalshi/prod routing stub |
| **Retrieved** | 2026-08-13 |
| **Read-status** | deep-read |

Prompt: five consecutive FG misses → quarter under; last 2:00 each team under 5; Kalshi (no sportsbook login). Full empirics filed on gambling-wiki.

## Narrative

**Route:** wagering strategy + retail bot posture → `@gambling-wiki`. OSINT keeps **Kalshi API / series inventory / no auto-order** notes for CeminiSuite.

### Kalshi findings relevant to prod [CONFIRMED 2026-08-13]

- Public `trade-api/v2` lists **88** WNBA / Women’s Pro Basketball series — auth **not** required for catalog/quotes.
- Liquid: `KXWNBAGAME`, `KXWNBATOTAL`, `KXWNBASPREAD`, half/quarter totals, `KXWNBATEAMTOTAL`.
- **No** last-2-minute / each-team-under-5 time-window series (Sports-wide search empty).
- Live 4Q ladders can be too wide to fill; game totals carry most OI.
- Prod `KALSHI_*` env was **not** needed for this pass; use only for authenticated history/orders.

### Empirics (summary — see gambling-wiki for tables)

- 189 ESPN PBP games (2026-06-01…08-12): **no edge** after 5 team FG misses vs clock baseline.
- Last 2:00 both under 5: **23.8%** all / **12.2%** close / **34.0%** blowout at 2:00 — fair ~+320 / +720 / +194.
- Product if any: **alert-only** paper log; no sportsbook auto-submit; do not invent a Kalshi proxy for the friend’s ticket.

## Snippets

> "Kalshi: 88 WNBA series; zero last-2-minute contracts; closest live objects are KXWNBAnQTOTAL and game totals." [Source: Kalshi public trade-api/v2, 2026-08-13; hub `@gambling-wiki/entities/sports/wnba-betting.md`]
