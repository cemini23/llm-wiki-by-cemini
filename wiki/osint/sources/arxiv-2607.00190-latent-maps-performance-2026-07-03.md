---
title: "Play Like Champions — Latent Maps of Performance — arXiv 2607.00190"
type: source
tags: [arxiv, starcraft, rts, feedback, generative-ai, k141, pdf]
keywords: [LMP, counterfactual feedback, guided VAE, optimal transport, StarCraft II, esports coaching]
related:
  - concepts/latent-maps-performance-counterfactual-feedback.md
  - concepts/castle-sim-rts-micromanagement-steals.md
  - sources/arxiv-hrl-influence-map-starcraft-2606.30092-2026-06-30.md
  - sources/arxiv-ai-native-games-survey-2607.00527-2026-07-02.md
maturity: draft
read_status: read
created: 2026-07-03
updated: 2026-07-03
clusters: [game-dev, rl-marl, poker]
---

## Relations

- @concepts/latent-maps-performance-counterfactual-feedback.md — primary concept
- @concepts/castle-sim-rts-micromanagement-steals.md — sibling StarCraft steal cluster (K136 HRL-IM)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Play Like Champions: Counterfactual Feedback Generation in Latent Space |
| **Authors** | Białecki, Mastalerz, Zhou |
| **arXiv** | 2607.00190v1 |
| **sha256** | `9cb28eaf490e446279cd950ca5065a7fc692ed41aa5ef4a8d9c6c2ae5666b682` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.00190-counterfactual-feedback-generation-in-latent-spa.pdf` |
| **Retrieved** | 2026-07-03 |
| **Read status** | read (abstract + intro) |

## Narrative

**Latent Maps of Performance (LMP)** — Guided VAE on **23,305** pro StarCraft II replays; macro-economic features conditioned on match outcome. Four traversal strategies from losing → winning profiles: linear interpolation, iterative optimal transport, density-regularized gradient ascent, neural flow matching.

Decoded counterfactual paths yield **multi-granularity feedback** for human improvement (championship model from sports science).

**Cemini relevance:** castle-sim + poker Arena — counterfactual trajectory feedback pattern (not SC2 code port). REFERENCE — no public repo cited.

## Snippets

> "We model player improvement as algorithmic recourse within a learned representation space." [Source: arxiv-2607.00190 abstract (retrieved 2026-07-03)]
