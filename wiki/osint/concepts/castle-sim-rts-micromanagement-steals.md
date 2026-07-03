---
title: castle-sim — RTS micromanagement steals (K136)
type: concept
tags: [concept, game-dev, castle-sim, rts, marl, k136]
keywords: [influence map, cluster scripts, hierarchical Q-table, micromanagement, interpretable RL, castle-sim]
related:
  - sources/arxiv-hrl-influence-map-starcraft-2606.30092-2026-06-30.md
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/latent-maps-performance-counterfactual-feedback.md
  - sources/arxiv-2607.00190-latent-maps-performance-2026-07-03.md
  - concepts/active-project-research-routing.md
  - concepts/rl-marl-research.md
maturity: draft
created: 2026-06-30
updated: 2026-07-03
---

## Relations

- @sources/arxiv-hrl-influence-map-starcraft-2606.30092-2026-06-30.md — K136 REFERENCE source (HRL-IM/CBS)
- @concepts/castle-sim-pathfinding-steals.md — K126 route-diversity steals (complementary layer)
- @concepts/latent-maps-performance-counterfactual-feedback.md — K141 counterfactual coaching in latent space
- @concepts/active-project-research-routing.md — brief → Game Dev wiki

## Raw Concept

What prompted this page: K136 arXiv **2606.30092** (StarCraft micromanagement) maps to **castle-sim** unit coordination — influence-map state hashing + cluster-based tactical scripts under a hierarchical decision stack.

## Narrative

Castle-sim siege AI needs **local micromanagement** (per-squad tactics) without AlphaStar-scale DRL. HRL-IM/CBS offers three transferable patterns:

| Pattern | Paper mechanism | castle-sim steal |
|---------|-----------------|------------------|
| State hash | Influence map → hex code via histogram equalization | Grid influence over wall breach / courtyard control for Godot squads |
| Action abstraction | Cluster-based scripts on dynamic unit groups | Partition defenders/rams into clusters; script menu per cluster |
| Hierarchy | Upper Q picks cluster strategy; lower Q runs script | Commander layer vs squad tactical layer |
| Dense reward | Local reward allocation vs terminal win/lose | Per-cluster damage dealt / units preserved shaping |

**Interpretability:** tabular Q visibility vs neural black box — fits hobby slice debug requirements.

**Posture:** REFERENCE steal — brief in `@game-dev-wiki/briefs/`; no code Adopt.

## Snippets

> "Hierarchical multi-Q-table architecture decomposes decision-making into upper-level clustering strategy selection and lower-level tactical execution." [Source: arXiv:2606.30092 abstract (retrieved 2026-06-30)]
