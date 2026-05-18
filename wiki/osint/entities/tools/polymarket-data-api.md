---
title: "Polymarket Data API"
type: entity
tags: [tool, polymarket, api, data-api, analytics, positions, public-endpoints]
keywords: [data-api, polymarket-analytics, market-positions, holders, open-interest, portfolio-value, closed-positions, user-activity, whale-flow]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-lb-api.md
  - concepts/polymarket-api-reference.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @entities/platforms/polymarket.md — the platform this API analyzes
- @entities/tools/polymarket-gamma-api.md — discovery layer; conditionIds resolved there index into Data API queries
- @entities/tools/polymarket-clob-api.md — execution layer; Data API is the post-trade / position-analytics counterpart
- @entities/tools/polymarket-lb-api.md — leaderboard/PnL slice; `/profit` complements this layer's `/closed-positions`
- @concepts/polymarket-api-reference.md — canonical cross-surface index this entity belongs to
- @sources/alterego-eth-polymarket-endpoint-cheatsheet.md — source page (@AlterEgo_eth X post, May 2026) that first documented this layer for Cemini

## Raw Concept

What prompted this page: the K51 @AlterEgo_eth endpoint cheat sheet documented a third Polymarket API surface Cemini had not catalogued — the **Data API** for per-trader and per-market analytics. Cemini previously had Gamma (discovery) and CLOB (execution) but no entity page for the layer that answers "who holds this market and what is their PnL."

## Narrative

### Identity

- **Role**: Polymarket's **trader + market analytics** layer
- **Base URL**: `https://data-api.polymarket.com`
- **Auth**: **None required** — fully public
- **Used for**: position snapshots, PnL history, holder lists, open interest, portfolio value — keyed by wallet `address` or market `conditionId`

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/v1/market-positions?market={conditionId}` | All trader positions in a market |
| GET | `/positions?user={address}&limit=500` | Open positions (max 500) |
| GET | `/closed-positions?user={address}&limit=50` | Closed positions + PnL history |
| GET | `/activity?user={address}&limit=500` | User transactions (TRADE/REDEEM/YIELD) |
| GET | `/trades?user={address}&limit=100` | Trade history by wallet |
| GET | `/trades?market={conditionId}&limit=100` | Trade history by market |
| GET | `/oi?market={conditionId}` | Open interest in USD |
| GET | `/holders?market={conditionId}&limit=50` | Top holders |
| GET | `/value?user={address}` | Portfolio value |

### Cemini relevance

This is the data substrate for whale-flow and informed-minority analysis. `/holders` + `/v1/market-positions` + `/oi` feed any "Polymarket informed-flow analyst" surface (see `@sources/polymarket-informed-minority-gomezcram-2026.md`); `/closed-positions` and `/value` give per-wallet skill scoring over time. Public + no-auth means these are cheap to poll. Geo: read-public, works from a US IP per the 2026-05-18 geo-profiling.

`[NEEDS VERIFICATION 2026-05-18]` — endpoint paths taken from a single source (the @AlterEgo_eth cheat sheet); confirm exact response shapes and rate limits against the live API before wiring into the stack.

## Snippets

> "Data API - http://data-api.polymarket.com (public, no auth)" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]
