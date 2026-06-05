---
title: Avellaneda–Stoikov market making — inventory-skewed quoting baseline
type: concept
tags: [concept, market-making, quant-finance, k98]
keywords: [avellaneda-stoikov, reservation-price, spread, inventory-risk, gamma, logit]
related:
  - sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/market-informedness-market-making.md
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
maturity: draft
created: 2026-06-04
updated: 2026-06-05
---

## Relations

- @sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md — implementation reference (Stanford GR5)
- @concepts/polymarket-market-making-architectures.md — PM-specific MIT OSS patterns built atop same theory

## Raw Concept

Canonical academic MM model for spread capture with inventory penalty; ingested via gr5.pdf (2018 student project).

## Narrative

**Avellaneda & Stoikov (2008)** solves for optimal bid/ask quotes as function of mid, volatility, risk aversion, and **inventory** — reservation price shifts against inventory direction to mean-revert position. GR5 adds dynamic **order-size** control for inventory risk and simulates vs naive baseline.

**Cemini mapping:** Use when designing Polymarket LP skew (logit-space variants per open-meteo cross-notes), not for sub-minute BTC up/down latency bots. Pair with `polymarket-lp-bot-phase0-spec` promotion gates before live MM capital.

## Snippets

> "strategically place these bids and asks to capture the spread … while … inventory risk"

[Source: gr5.pdf p.1, retrieved 2026-06-04]
