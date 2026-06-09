---
title: "Lighter.xyz — zk-settlement perp DEX with centralized sequencer"
type: entity
tags: [entity, tool, platform, perps, dex, k108]
keywords: [lighter, arrakis, lead-lag, sequencer, zk-proofs]
related:
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/perp-dex-price-discovery-lead-lag.md
  - entities/platforms/hyperliquid.md
  - entities/data-sources/binance.md
maturity: draft
created: 2026-06-09
updated: 2026-06-09
---

## Relations

- @sources/trading-posts-compilation-8-2026-06-09.md — K108 Post 5 (Arrakis three-venue study)
- @concepts/perp-dex-price-discovery-lead-lag.md — ~100 ms lag vs Binance on 23/29 assets
- @entities/platforms/hyperliquid.md — architectural contrast (matching at consensus vs settlement)

## Raw Concept

K108 Arrakis cross-venue study includes **Lighter.xyz** as third perp venue. Described as DEX with **off-chain sequencer** in-memory matching + **zk proofs settled to Ethereum** — trust boundary at settlement, not matching.

## Narrative

Arrakis finding: Lighter fill tape follows Binance with **~100 ms** median peak lag (estimator grid floor), much tighter than Hyperliquid's **~700 ms**. Used to falsify "HL lags because DEX" — architecture choice (where decentralization is enforced) drives latency more than on-chain label.

**Cemini posture:** stub only; no CCXT/SDK integration in stack [REFERENCE].

## Snippets

> "Lighter buys speed by relocating the trust boundary from matching to settlement." [Source: Posts.docx K108, @ArrakisFinance Post 5]
