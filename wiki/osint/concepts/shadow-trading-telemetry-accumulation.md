---
title: Shadow trading telemetry accumulation — dual-track and selection bias
type: concept
tags: [concept, shadow-trading, paper-trading, pm-kl-stat-arb, k77]
keywords: [shadow-telemetry, Heckman, IPW, dual-track, counterfactual-fills, R10]
related:
  - sources/shadow-trading-data-accumulation-strategies-2026-05-28.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/prediction-market-statistical-arbitrage.md
maturity: draft
created: 2026-05-28
updated: 2026-05-28
---

## Relations

- @sources/shadow-trading-data-accumulation-strategies-2026-05-28.md
- @concepts/shadow-to-live-transition-engineering.md
- @concepts/lp-algorithm-live-promotion-gates.md
- @concepts/prediction-market-statistical-arbitrage.md

## Raw Concept

K77: how to grow shadow datasets for R10 PM×KL and LP promotion without fooling promotion gates.

## Narrative

### Dual-track pattern

| Track | Purpose | Writes |
|-------|---------|--------|
| **Strict** | Production risk path | `paper_adapter` executed rows only |
| **Relaxed** | Research counterfactuals | `shadow_intents` table — blocked signals + markout |

### R10 action

PM×KL curated pairs: log **would-trade** on spread breach even when size=0; 8422 obs → usable markout series.

### Promotion coupling

Relaxed track **never** feeds live GO alone — only strict track + @concepts/lp-algorithm-live-promotion-gates.md.

## Snippets

> Counterfactual logging at gate boundary preserves information destroyed by hard aborts. [Source: Shadow Trading Data Accumulation Strategies.docx]
