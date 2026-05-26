---
title: Polymarket marginal-polytope arbitrage — dependent markets beyond YES+NO=1
type: concept
tags: [concept, polymarket, arbitrage, market-structure, k67]
keywords: [marginal-polytope, combinatorial-arbitrage, dependent-markets, 40-million-arbitrage, robrtcode, probabilistic-forest-paper]
related:
  - sources/trading-posts-compilation-38-2026-05-26.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/non-latency-arbitrage-strategies.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/trading-posts-compilation-38-2026-05-26.md — Post 26 (@robrtcode)
- @concepts/cross-venue-arbitrage-pattern.md — cross-venue; this is **intra-platform logical** arb
- @entities/platforms/polymarket.md — venue

## Raw Concept

Arbitrage on Polymarket is not only "YES + NO < $1" on one condition. **Logically dependent** markets (e.g., Trump wins PA vs GOP wins PA by 5+) create mispricings solvable as **constraint satisfaction** over exponential outcome spaces — the **marginal polytope** framing from 2025 academic work cited in K67.

## Narrative

### Naive vs structural arb

| View | Failure mode |
|------|----------------|
| Pairwise sum check | Misses cross-market logical implications |
| Marginal polytope / ILP | Scans dependent constraints; sizes across book depth + fees |

K67 cites paper *"Unravelling the Probabilistic Forest: Arbitrage in Prediction Markets"* (2025) [NEEDS VERIFICATION 2026-05-26]: **~$39.7M** extracted Apr 2024–Apr 2025; top wallet **~$2.0M / 4,049 trades** (~$496/trade) [TENTATIVE — from @robrtcode summary].

### Why retail loses the race

Bots resolve large constraint systems in milliseconds, parallelize across correlated markets, rotate capital. Manual "I noticed YES+NO≠1" arrives after correction.

### Cemini relevance

- Informs **market selection** for non-latency strategies: dependent election/geopolitical clusters may still harbor structural gaps vs single binaries.
- Distinct from @concepts/three-formula-system-polymarket-rare-events.md rare-event edge (directional), not replacement.

## Snippets

> "This was mathematics identifying situations where an outcome pays $1 and you can buy it for less." [Source: Posts.docx K67 Post 26, @robrtcode summary]
