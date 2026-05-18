---
title: "Polymarket WebSocket API"
type: entity
tags: [tool, polymarket, api, websockets, realtime, orderbook-stream, public-endpoints]
keywords: [websocket-api, ws-subscriptions-clob, market-channel, user-channel, orderbook-deltas, realtime-fills]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-clob-api.md
  - concepts/polymarket-api-reference.md
  - concepts/polymarket-bot-architecture.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @entities/platforms/polymarket.md — the platform this stream covers
- @entities/tools/polymarket-clob-api.md — REST counterpart; WebSocket is the realtime push layer over the same order book
- @concepts/polymarket-api-reference.md — canonical cross-surface index this entity belongs to
- @concepts/polymarket-bot-architecture.md — the 6-layer websocket bot architecture built directly on these channels
- @sources/alterego-eth-polymarket-endpoint-cheatsheet.md — source page (@AlterEgo_eth X post, May 2026)

## Raw Concept

What prompted this page: the K51 @AlterEgo_eth endpoint cheat sheet enumerated the Polymarket WebSocket surface. The `@concepts/polymarket-bot-architecture.md` playbook (K40, @0x_Punisher) assumes a websocket-first design; this entity page is the durable reference for the channels that playbook consumes.

## Narrative

### Identity

- **Role**: Polymarket's **realtime push** layer over the CLOB order book
- **Base URL**: `wss://ws-subscriptions-clob.polymarket.com/ws`

### Channels

| Channel | Auth | Payload |
|---------|------|---------|
| `/market` | public | Orderbook snapshots + real-time price-change deltas |
| `/user` | authenticated | Personal fills, cancellations, order updates |

### Cemini relevance

`/market` is the canonical low-latency price feed — a hot-loop poll of CLOB `GET /price` is the wrong pattern when this stream exists (see `@concepts/polymarket-bot-architecture.md` <0.5ms hot-path target). `/user` carries fills, but the bot-architecture concept page documents a silent-fill bug post-V2: WebSocket fill events alone do not confirm fills — pair with a periodic REST reconciliation pass against CLOB `/orders`.

`[NEEDS VERIFICATION 2026-05-18]` — subscription message format and snapshot/delta semantics taken from a single source; confirm against the live socket before relying on delta-only updates.

## Snippets

> "WebSockets - wss://ws-subscriptions-clob.polymarket.com/ws — /market public stream, orderbook snapshots + real-time price change deltas; /user authenticated stream, your personal fills, cancellations and order updates." [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]
