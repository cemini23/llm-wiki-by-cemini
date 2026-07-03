---
title: Latent Maps of Performance — counterfactual RTS feedback (K141)
type: concept
tags: [concept, game-dev, starcraft, feedback, generative-ai, k141, reference-only]
keywords: [LMP, guided VAE, counterfactual, optimal transport, macro features, player coaching]
related:
  - sources/arxiv-2607.00190-latent-maps-performance-2026-07-03.md
  - concepts/castle-sim-rts-micromanagement-steals.md
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/ai-native-games-taxonomy.md
  - sources/arxiv-hrl-influence-map-starcraft-2606.30092-2026-06-30.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
---

## Relations

- @sources/arxiv-2607.00190-latent-maps-performance-2026-07-03.md — Białecki et al. (2607.00190)
- @concepts/castle-sim-rts-micromanagement-steals.md — K136 squad tactics cluster

## Raw Concept

What prompted this page: K141 arXiv **2607.00190** — learn latent **performance manifold** from pro replays; traverse losing→winning profiles for **actionable counterfactual feedback** (sports championship model).

## Narrative

### Pipeline

1. Extract macro-economic feature vectors from SC2 replays
2. Train **Guided VAE** outcome-conditioned on win/loss
3. Traverse latent space (OT, flow matching, etc.)
4. Decode → feature deltas → player-facing coaching hints

### Traversal tradeoff

Methods differ on path realism vs OOD stability on amateur replays — no single dominant strategy.

### Cemini steals (REFERENCE)

| Target | Analog |
|--------|--------|
| **castle-sim** | Post-playtest latent “what-if” siege economy nudges |
| **Poker Arena** | Chart-space counterfactual: “shift mix toward profile X” literacy |

**Posture:** no code repo — brief steals only.

## Snippets

> "Points sampled along an improvement trajectory in latent space can be decoded … yielding immediate feedback on which gameplay features need to change." [Source: arxiv-2607.00190 §1 (retrieved 2026-07-03)]
