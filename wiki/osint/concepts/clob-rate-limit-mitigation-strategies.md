---
title: CLOB rate limit mitigation — hybrid WS + batch + backoff roles
type: concept
tags: [concept, execution, polymarket, kalshi, hyperliquid, rate-limits, k77]
keywords: [429, websocket-first, order-batching, exponential-backoff, TCP_NODELAY, adverse-selection]
related:
  - sources/clob-rate-limit-mitigation-strategies-2026-05-28.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/prediction-market-statistical-arbitrage.md
  - entities/tools/discountifu-polymarket-trading-bot.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/clob-rate-limit-mitigation-strategies-2026-05-28.md
- @concepts/shadow-to-live-transition-engineering.md — token-bucket preflight before live
- @concepts/prediction-market-statistical-arbitrage.md — R10 PM×KL execution
- @entities/tools/discountifu-polymarket-trading-bot.md — R11 patch target

## Raw Concept

K77 synthesis: how to assign backoff vs batch vs WebSocket per execution profile on Cemini PM/KL/Hyperliquid paths.

## Narrative

### Recommended hybrid stack

1. **WebSocket-first** for taker legs, cancels, book deltas (prod `polymarket_lp_flox_ws`, KL autopilot)
2. **Micro-batch** (sub-ms window) for multi-quote MM refresh only
3. **Backoff** only as ban-avoidance on 429/418 — never on defensive cancel path without alt route

### R10 / R11 implications

- PM×KL shadow must log **429 rate**, in-flight cap hits, cancel latency — not fee-only edge.
- R11 discountifu diff: prioritize **heartbeat/reconnect** and subscription parity — cosmetic gaps HOLD.

### R14 tie-in

Alpaca/polygon REST polling is wrong tier for tick freshness; aligns with @concepts/tick-staleness-ingestion-diagnosis.md.

## Snippets

> Hybrid: WS for taker + book; batched REST for bulk quote maintenance; backoff as isolated catastrophic fallback. [Source: CLOB Rate Limit Mitigation Strategies.docx]
