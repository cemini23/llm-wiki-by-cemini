---
title: Polymarket
type: entity
tags: [platform, prediction-markets, on-chain, cemini-venue-adjacent]
keywords: []
related:
  - sources/3-19-kalshi-trading-strategy-research.md
  - sources/3-9-pm-research.md
  - sources/kalshi-3-3-29.md
  - sources/kalshi-4-3-29.md
  - sources/osint-prediction-markets-trading-architecture.md
  - concepts/favorite-longshot-bias.md
  - concepts/publishers-exclusion.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-9-pm-research.md
- @sources/kalshi-3-3-29.md
- @sources/kalshi-4-3-29.md
- @sources/osint-prediction-markets-trading-architecture.md
- @concepts/favorite-longshot-bias.md
- @concepts/publishers-exclusion.md
- @entities/platforms/kalshi.md

## Raw Concept

Synthesized from 5 source(s) referencing this entity across the Cemini research corpus. Category: platforms.

## Narrative

Polymarket is an on-chain prediction market running on Polygon, offering
USDC-denominated binary event contracts. For Cemini it primarily serves as
a **cross-venue price reference** — arbitrage and divergence signals
between Kalshi and Polymarket feed the signal-fusion engine — rather than a
primary execution venue, because US retail access is geofenced and because
the institutional buyer archetype targeted by the IP-sale thesis prefers
CFTC-regulated venues.

Documented across the corpus: Polymarket's AMM-adjacent LMSR mechanics
produce tighter spreads on political/macro contracts than Kalshi during
high-volume events; the lack of US retail access means retail-driven
favorite-longshot bias is weaker than on Kalshi, creating a useful
efficiency-gradient signal. Polymarket is explicitly flagged in the
compliance research as a venue Cemini can **reference** (via public
on-chain data) but not **execute on** without restructuring — hence its
status as a read-only data source in the current stack.

## Snippets

*(populate as source stubs are deep-read.)*
