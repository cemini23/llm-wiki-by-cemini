---
title: Favorite-longshot bias (FLB)
type: concept
tags: [concept, prediction-markets, behavioral]
keywords: []
related:
  - sources/3-19-kalshi-trading-strategy-research.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - sources/polymarket-informed-minority-gomezcram-2026.md
maturity: validated
created: 2026-04-23
updated: 2026-04-29
---

## Relations

- @sources/3-19-kalshi-trading-strategy-research.md
- @entities/platforms/kalshi.md
- @entities/platforms/polymarket.md

## Raw Concept

Synthesized across 1 source(s) in the Cemini research corpus that reference this concept directly or by equivalent terminology.

## Narrative

The **favorite-longshot bias** is the robust empirical finding that
prediction-market participants systematically overpay for longshot
(low-probability) outcomes and underpay for favorites. On Kalshi event
contracts, the bias manifests as longshot contracts (quoted at
\$0.05–0.15) trading above their fair implied probability, and favorites
(\$0.85–0.95) trading slightly below.

### Cemini's strategies that monetize FLB

**[TENTATIVE — 2026-04-24 Track C audit]** The Avellaneda-Stoikov logit-space quoting engine on Kalshi is real; the three sub-strategies below are not yet carved out of it, and two of the three (Gumbel-fit longshot-fade, Polymarket cross-venue arb) have no code. Gap: quoting infrastructure exists but is not sliced into the three FLB-monetizing sub-strategies the wiki describes. Ticket (**P2**): *Carve FLB strategies out of generic logit pricing engine* — add explicit flags/modules for (a) favorite-side MM, (b) longshot-fade, (c) Polymarket cross-venue. Gap memo: `briefs/track-c-walk-results.md`.

1. **Favorite-side market-making** `[CONFIRMED 2026-04-24]` — Avellaneda-Stoikov quotes in
   **logit space** on favorites, capturing the bias as a consistent
   drift term. Positive skew even after venue fees. *Real: `logit_pricing/pricing_engine.py` (240 lines); `LogitPricingEngine.assess_contract()` produces `ContractAssessment` via logit + indicators + jump_diffusion. Kalshi WS rover publishes `intel:logit_assessments` consumed by cemini_mcp tool `get_contract_pricing`. Not yet flagged as favorite-side-only.*
2. **Longshot-fade** `[RETRACTED 2026-04-24]` — ~~fade grossly-mispriced longshots when the
   implied-probability delta vs a Gumbel-fit model exceeds a
   threshold; position-sized by Kelly-fractional.~~ *Gumbel has 0 hits in main-tree code. Not implemented.*
3. **FLB arbitrage across venues** `[RETRACTED 2026-04-24]` — ~~Polymarket (less retail-driven)
   typically shows weaker FLB than Kalshi. Cross-venue legs capture
   the efficiency gradient.~~ *No Polymarket adapter in `core/ems/adapters/`. Cross-venue arb not wired.*

### Why FLB persists
Behavioral: loss-aversion distorts small-probability weighting; retail
bettors chase payoff, not expected value. Structural: longshot
contracts have wider spreads on Kalshi, making arbitrage capital-
expensive; the market-maker inventory is typically positioned against
the bias, creating a quasi-equilibrium that never fully closes.

## Snippets

*(populate as source stubs are deep-read.)*
