---
title: Altcoin screener workflow — Orion Terminal five-column filter
type: concept
tags: [concept, crypto-trading, discretionary, screener, k64]
keywords: [orion-terminal, trd-5m, volume-5m, altcoin-discovery, koroushak, breakout-reversal-regime]
related:
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - entities/people/koroushak.md
  - concepts/quant-finance.md
maturity: draft
created: 2026-05-24
updated: 2026-05-24
---

## Relations

- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64 Post 3
- @entities/people/koroushak.md — author

## Raw Concept

Discretionary workflow to pick **5–6 altcoins per day** using @OrionTerminal (third-party scanner): sort by short-term trade count, enforce liquidity floor, favor extreme 5m/1d movers. Regime heuristics separate breakout vs reversal days.

## Narrative

### Column semantics

| Column | Question answered | Rule of thumb |
|--------|-------------------|---------------|
| TRD (5M) | Is anyone watching? | Sort desc; top 10 |
| Volume (5M) | Can I trade safely? | ≥ **$500k** / 5m |
| Change % (5M) | Moving now? | +1–5% momentum |
| Change % (1D) | Recently hot? | Extreme gainers **and** losers |

### Regime signals [TENTATIVE]

- **Breakout-favoring:** elevated TRD, high cross-market volume, clean direction, +10–20% leaders.
- **Reversal-favoring:** low TRD, mixed colors, small top moves, spike-and-fade charts.

### Cemini relevance

Orthogonal to Polymarket stack — useful for **crypto spot/perp watchlist generation** on prod if Orion or internal scanner adopts same gates. Do not treat Orion as vetted infrastructure without Phase-0.

## Snippets

> "If it is not at least $500k per 5 minutes, I will not be trading it." [Source: posts.docx K64, @KoroushAK]
