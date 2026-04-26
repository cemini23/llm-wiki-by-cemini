---
title: CoinGecko
type: entity
tags: [data-source, crypto-native, market-data, reference-data]
keywords: [coingecko, crypto, market-cap, price, volume, dev-metrics, social-metrics]
related:
  - concepts/crypto-asset-taxonomy.md
maturity: draft
created: 2026-04-25
updated: 2026-04-25
---

## Relations

- @concepts/crypto-asset-taxonomy.md — primary use case: the 4-category crypto-asset taxonomy (store-of-value / programmable L1 / memecoin-PoW / oracle middleware) is sourced from CoinGecko-style market and developer metrics; this entity is the canonical source for those facts on each of the 7 crypto watchlist tickers

## Raw Concept

Added 2026-04-25 from the [public-apis](https://github.com/public-apis/public-apis) curated list. Cemini already has venue-API access (Coinbase + CCXT-via-Binance/Bybit/Hyperliquid) for tradeable pairs, but no broad reference-data source for crypto market structure. CoinGecko fills that gap.

## Narrative

CoinGecko is the de-facto free reference API for crypto market data —
prices, volume, market cap, fully-diluted valuation, developer activity
(GitHub commits, contributors), social signals (Twitter/Reddit
mentions), and exchange listings — across thousands of coins.

**Why this is additive over existing exchange APIs**:

- **Venue APIs** (Coinbase, CCXT/Binance/Bybit/Hyperliquid) only return
  what's tradeable on that venue. CoinGecko covers the long tail.
- **Cross-venue price aggregation** — CoinGecko's price is a
  volume-weighted average across listed exchanges, useful as a
  fair-value reference for arbitrage detection.
- **Developer + social metrics** — GitHub commit cadence, Twitter
  follower count, Reddit subscriber count. These feed alt-data
  signals that pure price/volume can't surface.
- **No-auth public tier** — most endpoints work without an API key
  (rate-limited to ~10-30 req/min). Demo plan API key bumps to ~30
  req/min; paid Pro tier ($129/mo) bumps to 500 req/min.

**Cemini integration candidates** (not yet wired):

1. Per-crypto-ticker page enrichment — pull market-cap rank, FDV,
   circulating supply, dev activity at ingest time.
2. Long-tail discovery — when a new memecoin or L1 candidate is being
   evaluated for the watchlist, CoinGecko's category pages give a
   ranked starting point.
3. Cross-source price triangulation — CoinGecko aggregate vs. Coinbase
   vs. Hyperliquid spot for the same token; large divergence flags
   either an arb opportunity or a data-quality issue.

**License**: free public use; attribution required. Commercial use
permitted on paid plans.

## Snippets

- API root: http://www.coingecko.com/api
- Free public docs: https://docs.coingecko.com/v3.0.1/reference/introduction
- Coin list: `GET https://api.coingecko.com/api/v3/coins/list`
- Per-coin data: `GET https://api.coingecko.com/api/v3/coins/bitcoin?developer_data=true&community_data=true`
