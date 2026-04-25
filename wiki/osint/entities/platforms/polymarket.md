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
  - sources/cftc-anprm-prediction-markets-2026-03-16.md
  - sources/cftc-selig-house-ag-testimony-2026-04-16.md
  - concepts/favorite-longshot-bias.md
  - concepts/publishers-exclusion-apa.md
  - concepts/dcm-state-preemption.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-04-23
updated: 2026-04-25
---

## Relations

- @sources/3-19-kalshi-trading-strategy-research.md
- @sources/3-9-pm-research.md
- @sources/kalshi-3-3-29.md
- @sources/kalshi-4-3-29.md
- @sources/osint-prediction-markets-trading-architecture.md
- @sources/cftc-anprm-prediction-markets-2026-03-16.md — March 12 2026 ANPRM Question 19 will define "gaming" under CEA §5c(c)(5)(C); outcome shapes whether sports-event contracts (Polymarket included) survive at federal level
- @sources/cftc-selig-house-ag-testimony-2026-04-16.md — Polymarket-Trump-family proximity (Trump Jr. advisor + investor; Truth Social launching competing Truth Predict) raised by Rep. McGovern (D-MA) during testimony
- @concepts/favorite-longshot-bias.md
- @concepts/publishers-exclusion-apa.md
- @concepts/dcm-state-preemption.md — federal-vs-state preemption fight extends beyond Kalshi; Polymarket's on-chain non-DCM status is structurally weaker than Kalshi's
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
