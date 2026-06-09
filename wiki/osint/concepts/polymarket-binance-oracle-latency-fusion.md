---
title: Polymarket–Binance–oracle latency fusion — CVD/OBI vs implied UP/DOWN
type: concept
tags: [concept, polymarket, crypto, latency, k98]
keywords: [binance, chainlink, cvd, order-book-imbalance, websocket, up-down, mispricing]
related:
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - entities/tools/polymarket-websocket-api.md
  - entities/data-sources/binance.md
  - concepts/perp-dex-price-discovery-lead-lag.md
maturity: draft
created: 2026-06-04
updated: 2026-06-09
---

## Relations

- @concepts/polymarket-bot-architecture.md — canonical @0x_Punisher 6-layer stack; this page isolates **cross-venue fusion** layer
- @sources/trading-posts-compilation-18-2026-06-04.md — K98 Posts 2, 13

## Raw Concept

K98 @0x_Punisher + @Nekt_0: edge = **Polymarket implied probability lags** Binance spot flow (and oracle feeds), not directional prediction.

## Narrative

**Dual-feed stack** [TENTATIVE operator recipe, corroborates latency taxonomy in `polymarket-updown-bot-taxonomy`]:

1. **Binance WS** — spot price, CVD, order-book imbalance (OBI); optional 1m delta confirmation.
2. **Oracle reference** — Chainlink (post cites) for settlement-aligned spot [NEEDS VERIFICATION 2026-06-04: Cemini prod feed list].
3. **Polymarket CLOB WS** — active window UP/DOWN share prices.

**Signal:** When Binance momentum (CVD spike + buy-side OBI) diverges from PM UP price by calibrated threshold → entry before PM reprices. Window is short; competes with other latency bots.

**Cemini implications:** Requires sub-second fused feature bus + pre-built order templates on hot path; shadow-log divergence events before live capital. Top-wallet concentration narrative (67–76% profit share) is **single-source** [TENTATIVE].

## Snippets

> "That gap between real price and Polymarket's implied probability is where mispricing lives."

[Source: Posts.docx K98 Post 2, retrieved 2026-06-04]
