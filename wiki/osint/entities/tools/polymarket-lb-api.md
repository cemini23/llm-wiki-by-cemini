---
title: "Polymarket LB-API"
type: entity
tags: [tool, polymarket, api, lb-api, leaderboard, pnl, public-endpoints]
keywords: [lb-api, polymarket-leaderboard, pnl-history, profit-window, wallet-pnl]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-data-api.md
  - concepts/polymarket-api-reference.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
maturity: draft
created: 2026-05-18
updated: 2026-05-29
---

## Relations

- @entities/platforms/polymarket.md — the platform this API ranks
- @entities/tools/polymarket-data-api.md — sibling analytics layer; LB-API is the leaderboard/PnL slice
- @concepts/polymarket-api-reference.md — canonical cross-surface index this entity belongs to
- @sources/alterego-eth-polymarket-endpoint-cheatsheet.md — source page (@AlterEgo_eth X post, May 2026) that first documented this layer for Cemini

## Raw Concept

What prompted this page: the K51 @AlterEgo_eth endpoint cheat sheet documented a fourth Polymarket API surface — **LB-API**, a leaderboard / PnL endpoint distinct from the Data API.

## Narrative

### Identity

- **Role**: Polymarket's **leaderboard / PnL-history** layer
- **Base URL**: `https://lb-api.polymarket.com`
- **Auth**: **None required** — fully public
- **Used for**: per-wallet profit history over a time window

### Endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/profit?window=all&address={address}` | Full PnL history |
| GET | `/profit?window=1d&address={address}` | PnL, last 24h |
| GET | `/profit?window=7d&address={address}` | PnL, last 7 days **`[CONFIRMED 2026-05-29]`** |
| GET | `/profit?window=30d&address={address}` | PnL, last 30 days **`[CONFIRMED 2026-05-29]`** |

Invalid `window` values (e.g. `1w`, `1m`) return HTTP 400 `{"error":"invalid request"}` [live probe 2026-05-29].

### Cemini relevance

`/profit?window=all` gives a wallet's lifetime PnL — a direct skill-scoring input that complements the Data API's `/closed-positions`. Combined with `/holders` it lets Cemini rank a market's current participants by historical track record (the informed-minority signal). **`[CONFIRMED 2026-05-29]`** — live windows: `all`, `1d`, `7d`, `30d` (empty list if wallet has no history in window). Richer leaderboard also on Data API `GET /v1/leaderboard?timePeriod=DAY|WEEK|MONTH|ALL` — prefer Data API for category filters; keep LB-API for per-wallet `/profit` time series.

## Snippets

> "LB-API - http://lb-api.polymarket.com (public, no auth) — GET /profit?window=all&address={address} - full PnL history" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]
