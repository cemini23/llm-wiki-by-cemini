---
title: CCXT
type: entity
tags: [library, framework, crypto, exchange-connectivity]
keywords: []
related:
  - sources/3-18-crypto-integration-technical-audit.md
  - sources/3-19-compliance-research.md
  - entities/platforms/hyperliquid.md
  - sources/vibe-trading-hkuds.md
  - sources/eval-repository-revenue-integration-2026-07-07.md
  - entities/tools/hyperliquid-python-sdk.md
maturity: validated
created: 2026-04-23
updated: 2026-10-25
---

## Relations

- @sources/3-18-crypto-integration-technical-audit.md — primary; deep-read 2026-04-26 (K4)
- @sources/eval-repository-revenue-integration-2026-07-07.md — K148 Integrate reaffirm (xsp-killer multi-venue)
- @entities/platforms/hyperliquid.md

## Raw Concept

CCXT is the canonical Python crypto-exchange-connectivity library: ~34K GitHub stars, MIT license, normalizes order placement / market data / account state across 100+ centralized venues. K4 deep-read of @sources/3-18-crypto-integration-technical-audit.md (2026-04-26) confirmed CCXT IS deployed on the Cemini stack (`ccxt>=4.2.80` in `/opt/cemini/requirements.txt` + `ccxt_normalizer` Docker container running) — making this the lightest of the K-series reframes. One narrative claim was stripped:

| Pre-K4 claim | Server reality / source reality |
|---|---|
| "Hyperliquid… uses its native SDK + CCXT's contributed adapter simultaneously — orders double-sign for the tamper-evident audit trail" | The K4 source does not prescribe double-signing. It prescribes CCXT for **CEX legs** and the Hyperliquid native SDK for the **DEX leg** — distinct order paths, not a redundant double-sign. The "tamper-evident audit trail" framing also tied into the pg_tamperlog/Merkle leg `[RETRACTED 2026-04-24]` per @concepts/cryptographic-audit-trail.md. |

## Narrative

### Deployed integration (what's actually on the server, 2026-04-26)
- `ccxt>=4.2.80` in `/opt/cemini/requirements.txt`.
- `ccxt_normalizer` container running (1 of 40 active containers).
- Multi-venue ingest containers running alongside (`cemini_coinbase_ingestor`, `alpaca_ingestor`, `polygon_ingestor`, `oanda_streamer`, `kalshi_autopilot`) — CCXT's normalization role sits on the centralized-crypto leg of that ingest matrix.

### What CCXT is for in the K4 architecture
Per @sources/3-18-crypto-integration-technical-audit.md para 165:

> CCXT normalizes deeply fragmented order book data into a unified schema containing standard keys for bids, asks, timestamp, and datetime. The Cemini platform can fetch this unified dictionary and immediately push it to the Redis intel:orderbook pub/sub channel without intermediary translation functions.

The library role is correctly captured. **However**, two adjacent claims need calibration:

1. **Channel naming**: server probe found zero references to `intel:orderbook` in `/opt/cemini/services/*.py`. The deployed Redis channel naming convention is different from what the source assumes; downstream pages that propagated `intel:orderbook` as deployed-fact were off. (Same issue affects `intel:sentiment` for the unbuilt sentiment layer.)
2. **WebSocket coverage gap**: CCXT's REST coverage is comprehensive; its WebSocket coverage is patchier than native exchange SDKs. For latency-sensitive paths (orderbook deltas, trade ticks on a high-volume venue), CCXT's WebSocket layer is a known weak point — the K4 source flags this implicitly via the recommendation to use the Hyperliquid native SDK for the DEX leg rather than going through CCXT's adapter.

### Documented choices

- **CEX legs route through CCXT**. Binance, Bybit, Coinbase Advanced — single normalized order-submission and market-data surface.
- **Hyperliquid (DEX) uses its native SDK**. CCXT has a contributed Hyperliquid adapter, but the K4 source's prescription is to use the native SDK for DEX execution (custody, EIP-712 signing, Agent Wallet flow are SDK-internal). See @entities/platforms/hyperliquid.md for the full reframe.
- **Rate-limit budgeting**. CCXT's built-in throttling is supplemented by a Redis-backed global rate-limit layer because multiple strategy instances share credentials. (Pattern visible in deployed services; specific implementation details not enumerated here.)
- **Deal-killer flag** per @sources/3-19-compliance-research.md: CCXT's MIT license is clean, but some venue-specific adapters bundle venue-provided snippets with murkier licenses — the IP-sale due-diligence ledger tracks these per-adapter at @concepts/ip-sale-readiness.md.

## Snippets

> CCXT normalizes deeply fragmented order book data into a unified schema containing standard keys for bids, asks, timestamp, and datetime. The Cemini platform can fetch this unified dictionary and immediately push it to the Redis intel:orderbook pub/sub channel without intermediary translation functions.
>
> *— @sources/3-18-crypto-integration-technical-audit.md para 165. CCXT IS deployed; the channel-naming assertion (`intel:orderbook`) is not. Library role is real, the surrounding routing layer the source assumes is not what's deployed.*

> Hummingbot's architecture is fundamentally incompatible with the current deployed stack… The custom FastAPI + Redis + CCXT architecture currently deployed is vastly superior for resource-constrained environments.
>
> *— @sources/3-18-crypto-integration-technical-audit.md para 224. The "currently deployed" phrasing on FastAPI + Redis + CCXT is **partially accurate** — those three components are real on the server. But the K4 source itself collapses "individual libraries are present" into "the architecture is deployed" — same prescription-as-as-built pattern caught from the source side, mirroring the K2 pymerkle/OpenTimestamps name-drop in @concepts/cryptographic-audit-trail.md.*
