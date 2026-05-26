---
title: "Chainlink Data Streams — low-latency oracle price feed"
type: entity
tags: [entity, tool, oracle, price-feed, chainlink, low-latency, polymarket-btc-bot, k55]
keywords: [chainlink-data-streams, oracle-price-feed, low-latency-price-oracle, off-chain-pull-oracle, btc-price-feed, gustafssonkotte-bot, price-feed-separate-from-venue]
related:
  - sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - entities/people/gustafssonkotte.md
  - entities/tools/pyth-terminal.md
maturity: draft
created: 2026-05-20
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-2-time-series-openhuman-conflict-detector-lp-tactics-2026-05.md — K55 Posts 2.docx Post 3 explicitly uses Chainlink Data Streams as the BTC price feed
- @concepts/multi-module-bot-conflict-detector-pattern.md — concept where this is identified as a structural choice (price feed separate from execution venue)
- @entities/people/gustafssonkotte.md — bot operator using it

## Raw Concept

Chainlink's low-latency oracle price-feed service — a pull-based off-chain price feed signed by Chainlink's decentralized oracle network. Used by @Gustafssonkotte (K55 Posts 2.docx Post 3) as the **truth-source price feed** for his Polymarket BTC 5-minute Up/Down bot, deliberately decoupled from any exchange API.

## Narrative

### What it is

**Chainlink Data Streams** is Chainlink's low-latency oracle-feed product (distinct from the standard Chainlink Price Feeds which are higher-latency push-based on-chain feeds). Data Streams:
- **Pull-based**: app requests a signed price report on demand.
- **Low-latency**: designed for sub-second response.
- **Cryptographically signed**: prices come with verifiable Chainlink-oracle signatures.
- **Cross-chain**: deliverable to multiple chains.

### Cited usage in K55

@Gustafssonkotte's bot stack (Posts 2.docx Post 3):
- Chainlink Data Streams **for BTC price feed** (truth source).
- Polymarket CLOB **for execution** (different surface).
- Multi-exchange WebSocket feeds (Binance/Bybit/OKX/Coinbase) **for orderbook levels + walls** (sentiment + microstructure).

**Why this matters architecturally**: the price-truth source is independent of the execution venue. The bot does not trade against an exchange that also tells it the price. This avoids:
- Exchange price manipulation feedback loops.
- Single-source price feed failures during venue downtime.
- Latency vulnerabilities where the venue you trade against gives you priced data.

### Architectural pattern: "oracle separate from venue"

This is a generalizable pattern worth recording explicitly:

```
TRUTH SOURCE          EXECUTION VENUE
───────────────       ──────────────────────
Chainlink             ┌──────────────────┐
Data Streams ──────►  │   BOT BRAIN      │ ──────► Polymarket CLOB
(signed price)        │                  │         (orders)
                      └──────────────────┘
                              ▲
MICROSTRUCTURE                │
SOURCES ──────────────────────┘
(Binance/Bybit/OKX/Coinbase
 orderbook + walls)
```

Three independent surfaces:
1. **Price truth**: signed oracle feed (Chainlink).
2. **Microstructure**: multi-exchange orderbook + flow (cross-checked across venues).
3. **Execution**: the venue you actually trade on (Polymarket CLOB here).

### Cemini relevance

- **Adopt-candidate** for any future Cemini Polymarket workstream on tradeable-asset markets (BTC > X, ETH > Y, etc.) where the bot needs a venue-independent price feed.
- **Cost + latency**: pull-based + signed → has per-request cost (gas if on-chain, possibly API metering off-chain). Phase-0 audit needs to compare actual latency + cost against simpler alternatives (e.g., direct Binance WebSocket BTC ticker as price truth).

### Open questions [NEEDS VERIFICATION 2026-05-20]

1. **Cost model**: per-request gas / off-chain subscription pricing.
2. **Latency**: actual end-to-end fetch + verify time.
3. **Coverage**: which assets are available? (BTC + ETH at minimum; deeper coverage TBD.)
4. **Off-chain vs on-chain consumption**: does the bot need to be on-chain (smart contract) or can it consume signed reports off-chain in Python?
5. **Alternative**: would a simpler "median across 4 exchange WebSockets" oracle give comparable signal quality at zero cost? Probably yes for BTC; less obvious for less-liquid assets.

### Cemini fit

- **Defer for general adoption**, **Adopt for the specific case** when Cemini builds a Polymarket-on-financial-asset bot following the @Gustafssonkotte template. The architectural lesson (price oracle separate from venue) is recordable even if the specific Chainlink Data Streams tool isn't ultimately selected.

### Phase-0 checklist (when triggered)

1. Get Chainlink Data Streams pricing + API documentation.
2. Test latency vs Binance WebSocket BTC for the same 1-second window.
3. Cost model: monthly bill estimate for ~12/hour requests (matches 5-min market cadence).
4. Implementation effort: Python client maturity for off-chain consumption.
