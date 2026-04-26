---
title: OpenFIGI (Bloomberg symbology)
type: entity
tags: [data-source, symbology, identifiers, infrastructure, equities]
keywords: [figi, isin, cusip, sedol, ticker, bloomberg, symbology, mapping]
related:
  - entities/ticker-watchlist.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @entities/ticker-watchlist.md — primary use case: 30-symbol watchlist spans NYSE/NASDAQ equities + crypto-native + ETF tickers; OpenFIGI gives a single canonical identifier per instrument that survives venue-specific renames (Strategy ↔ MicroStrategy ↔ MSTR is the recent example)

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. Symbology infrastructure is silent in the current wiki — Cemini implicitly relies on string-equality of ticker symbols across venues, which is fine until a corporate action breaks it. This page exists so the gap is named.

## Narrative

OpenFIGI is Bloomberg's free, public symbology API. It maps any
financial instrument identifier (ticker, ISIN, CUSIP, SEDOL,
exchange-specific) to its Financial Instrument Global Identifier
(FIGI) — a 12-character permanent code that persists through corporate
actions, ticker changes, and exchange migrations.

**Why Cemini needs this**:

1. **Cross-venue identifier resolution** — Alpaca uses `MSFT`, IBKR
   uses `MSFT`, OANDA's CFD pricing uses `MSFT.US`, broker statements
   may use `594918104` (CUSIP). OpenFIGI normalizes all of these to a
   single FIGI per instrument.
2. **Corporate-action survival** — when MicroStrategy renamed itself
   to Strategy (still trading as `MSTR`), the ticker stayed but the
   issuer name changed. Tracking by FIGI makes this a non-event;
   tracking by ticker requires manual reconciliation.
3. **Crypto-native disambiguation** — exchange-specific perp symbols
   on Hyperliquid / Binance / Bybit don't have FIGIs (yet), but spot
   tokens that have been listed do. Useful for cross-venue arbitrage
   surveillance.

**Authentication**: none required for ≤25 req/min and ≤10 jobs per
request. Free API key bumps to 250 req/min and 100 jobs per request.

**License**: free public use; commercial use permitted under Bloomberg
[OpenFIGI terms](https://www.openfigi.com/api).

**Integration angle (not yet wired)**: a one-shot resolver in
`cemini_contracts/` that takes a watchlist row and stamps it with
FIGI + ISIN + CUSIP at ingest time. Removes the brittle string-match
assumption silently underlying the broker-statement reconciliation.

## Snippets

- API root: https://www.openfigi.com/api
- Mapping endpoint: `POST https://api.openfigi.com/v3/mapping`
- Search endpoint: `GET https://api.openfigi.com/v3/search?query=apple`
- Terms of use: https://www.openfigi.com/about/terms
