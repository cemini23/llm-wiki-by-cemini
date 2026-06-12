---
title: Avellaneda–Stoikov market making — inventory-skewed quoting baseline
type: concept
tags: [concept, market-making, quant-finance, k98]
keywords: [avellaneda-stoikov, reservation-price, spread, inventory-risk, gamma, logit]
related:
  - sources/arxiv-as-cj-forced-uniqueness-2606.01477-2026-06-11.md
  - sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md
  - sources/stanford-ml-orderbook-mm-gr4-2017.md
  - sources/trading-posts-compilation-6-2026-06-08.md
  - concepts/order-book-pressure-ml-market-making.md
  - concepts/polymarket-market-making-architectures.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/market-informedness-market-making.md
  - sources/arxiv-market-informedness-mm-profitability-2606.05882-2026-06-05.md
  - entities/people/ruujss.md
maturity: draft
created: 2026-06-04
updated: 2026-06-11
---

## Relations

- @sources/arxiv-as-cj-forced-uniqueness-2606.01477-2026-06-11.md — K111 forced ϕ=γσ²/2; CJ as AS second-order expansion
- @sources/stanford-avellaneda-stoikov-hf-mm-gr5-2018.md — implementation reference (Stanford GR5)
- @sources/stanford-ml-orderbook-mm-gr4-2017.md — sibling Stanford project: OBP ML skew vs A-S inventory skew
- @sources/trading-posts-compilation-6-2026-06-08.md — K106 @RuujSs production adaptation table
- @entities/people/ruujss.md — educator author
- @concepts/order-book-pressure-ml-market-making.md — when LOB classifiers help (and fail) as MM overlay
- @concepts/polymarket-market-making-architectures.md — PM-specific MIT OSS patterns built atop same theory

## Raw Concept

Canonical academic MM model for spread capture with inventory penalty; ingested via gr5.pdf (2018 student project).

## Narrative

**Avellaneda & Stoikov (2008)** solves for optimal bid/ask quotes as function of mid, volatility, risk aversion, and **inventory** — reservation price shifts against inventory direction to mean-revert position. GR5 adds dynamic **order-size** control for inventory risk and simulates vs naive baseline.

**Cemini mapping:** Use when designing Polymarket LP skew (logit-space variants per open-meteo cross-notes), not for sub-minute BTC up/down latency bots. Pair with `polymarket-lp-bot-phase0-spec` promotion gates before live MM capital.

### Production adaptations (K106 @RuujSs synthesis)

| Base assumption | Production fix | Cemini note |
|-----------------|----------------|-------------|
| Fixed order-arrival k | Rolling 15–30m k estimate from live flow | Highest-impact single tweak per source |
| Uninformed flow only | Cartea–Jaimungal informed-trading spread adj; HSBC FX latency model (2026) | Pair with K100 market-informedness regime |
| Constant σ | Realized vol on 5–15m rolling window | Already aligned with PM LP vol gates |
| Unbounded inventory | Guéant–Lehalle–Fernandez-Tapia hard bounds Q | Stop quoting exposed side at limit |
| Session end T | 24/7 crypto: artificial sessions, infinite horizon, or rolling T | Hummingbot supports all three |
| Continuous Brownian mid | Circuit-breaker layer outside core AS math | Pause quotes on discontinuous jumps |

Adaptive wrapper pattern: keep core reservation price + spread formulas intact; layer vol feed + circuit breaker separately — matches Cemini separation of **math core** vs **ops risk shell**.

### Parameter forcing (K111 — Feys 2606.01477)

Desk calibrating Cartea–Jaimungal **ϕ** and Avellaneda–Stoikov **γ** independently should run consistency check **γ = 2ϕ/σ²**. Terminal liquidation coefficient **α = ½ L″(0)** is microstructure-derived, not a taste parameter. Over-parametrizing (ϕ, α, γ) as three free knobs is a common LP config smell.

## Snippets

> "strategically place these bids and asks to capture the spread … while … inventory risk"

[Source: gr5.pdf p.1, retrieved 2026-06-04]
