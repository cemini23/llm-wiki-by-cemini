---
title: Binance — spot and USD-M futures market data
type: entity
tags: [data-source, crypto, exchange]
keywords: [binance, websocket, cvd, order-book, usd-m-futures]
related:
  - concepts/polymarket-binance-oracle-latency-fusion.md
  - concepts/crypto-pair-trading-drl-shielded-execution.md
  - sources/arxiv-crypto-pair-trading-drl-shielded-2606-04574-2026-06-04.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/perp-dex-price-discovery-lead-lag.md
  - entities/tools/lighter-xyz.md
maturity: draft
created: 2026-06-04
updated: 2026-06-09
---

## Relations

- @concepts/polymarket-binance-oracle-latency-fusion.md — K98 CVD/OBI leading signal for PM up/down
- @concepts/perp-dex-price-discovery-lead-lag.md — K108 Arrakis: Binance leads HL ~700 ms on perp fills [TENTATIVE]
- @sources/arxiv-crypto-pair-trading-drl-shielded-2606-04574-2026-06-04.md — USD-M futures 1h backtest venue

## Raw Concept

Canonical **crypto price + flow** feed referenced in PM latency-arbitrage operator posts and academic crypto pair-trading work (K98).

## Narrative

Public APIs: spot WebSocket (`stream.binance.com`), USD-M futures REST/WS for quant backtests. Cemini PM stack may consume spot ticks for BTC/ETH up/down fusion — wire per prod brief `2026-06-04_k98-pm-latency-fusion-queue-telemetry-cemini-prod.md` [NEEDS VERIFICATION 2026-06-04] for which endpoints are already in `/opt/cemini`.

## Snippets

> "Binance websocket for real-time spot price, order flow and cumulative volume delta."

[Source: Posts.docx K98 Post 2, retrieved 2026-06-04]
