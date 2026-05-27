---
title: Prediction-market → BTC → equity transmission hedge (IPS)
type: concept
tags: [concept, prediction-markets, macro, cross-asset, hedge, k69]
keywords: [implied-probability-spread, ips, brier-score, transmission-chain, ruujss]
related:
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/prediction-market-statistical-arbitrage.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
---

## Relations

- @sources/trading-posts-compilation-20-2026-05-27.md — Post 0 (@RuujSs)
- @concepts/prediction-market-statistical-arbitrage.md — venue microstructure stat-arb (different layer)
- @entities/platforms/polymarket.md

## Raw Concept

K69 @RuujSs long-form: same macro/policy event priced on **three speeds** — prediction markets (minutes), Bitcoin (hours), equities (sessions). Strategy: position all three in the direction the PM already established; capture convergence as slower markets catch up.

## Narrative

### Core signal — Implied Probability Spread (IPS)

- **P(t)** — prediction-market contract price (= direct probability)
- **Q(t)** — equity-implied probability backed out from sector return vs historical event-conditional means (μ_yes, μ_no)
- **IPS(t) = P(t) − Q(t)** — positive → equities underpriced vs PM; negative → overpriced

Entry when |IPS| exceeds ~1.5σ (author threshold [TENTATIVE]).

### Accuracy claim [TENTATIVE single author]

Brier scores cited: PM **0.08–0.12** vs equity-implied **0.14–0.20** on US policy/political events 2020–2026.

### Cemini relevance

Macro overlay for **crypto watchlist** and event-driven alerts — not a substitute for Polymarket microstructure bots. Distinct from @concepts/prediction-market-statistical-arbitrage.md (cross-venue order-book arb).

## Snippets

> "Prediction markets price events first… Bitcoin prices the same events second… Equity markets price the same events last." [Source: Posts.docx K69 Post 0]
