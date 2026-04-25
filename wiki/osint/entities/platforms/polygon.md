---
title: Polygon.io
type: entity
tags: [platform, data-vendor, equities, crypto-ticks, harvester-upstream]
keywords: [polygon, polygon.io, equity-ticks, crypto-ticks, intraday, not_authorized, plan-tier]
related:
  - entities/ticker-watchlist.md
  - entities/infrastructure/yfinance.md
  - concepts/equity-intraday-backfill-gap.md
maturity: validated
created: 2026-04-24
updated: 2026-04-24
---

## Relations

- @entities/ticker-watchlist.md — Polygon is the primary equity + crypto tick feed for the 30-symbol watchlist
- @entities/infrastructure/yfinance.md — fallback for same-day equity intraday when Polygon refuses
- @concepts/equity-intraday-backfill-gap.md — the doctrine that fires when Polygon returns `NOT_AUTHORIZED`

## Raw Concept

Stub page. Polygon.io is the primary upstream for CeminiSuite equity and crypto ticks. Consumers: `polygon_ingestor.py` and the harvester stack described in @entities/ticker-watchlist.md "Consumers". 2026-04-24 surfaced a **plan-tier** finding: same-day equity intraday requests return `NOT_AUTHORIZED` on the current plan — see @concepts/equity-intraday-backfill-gap.md for the incident + self-heal doctrine that replaces those gaps with a yfinance EOD sweep.

## Narrative

*Expand as more is learned. Known as of 2026-04-24:*

- **Role in stack**: primary equity ticks + crypto ticks feed. Crypto path via Coinbase separately (not routed through Polygon).
- **Plan tier note**: `NOT_AUTHORIZED` on same-day equity intraday — this is a permission surface, not a quota/rate-limit surface. Historical days + EOD are not affected.
- **Consumers in code**: `polygon_ingestor.py` (patched 2026-04-24 to fall back to yfinance on the refused window); the opportunity screener and related equity-dependent paths downstream of the ingestor.
- **Auth**: API key lives in `/opt/cemini/.env` (key name to be verified — likely `POLYGON_API_KEY`, same env-loader pattern as DeepSeek / Kalshi / OANDA).

## Snippets

*(populate when specific plan-tier docs, quota numbers, or error-response examples are worth inlining.)*
