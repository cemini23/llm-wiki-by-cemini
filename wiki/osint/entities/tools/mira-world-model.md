---
title: MIRA — multiplayer interactive world models
type: entity
tags: [entity, tool, world-models, game-dev, k160]
keywords: [mira-wm, representation autoencoder, Rocket League, latent diffusion, multiplayer]
related:
  - sources/arxiv-multiplayer-world-models-2607.05352-2026-07-09.md
maturity: draft
created: 2026-07-12
updated: 2026-07-12
---

## Relations

- @sources/arxiv-multiplayer-world-models-2607.05352-2026-07-09.md — arXiv:2607.05352 primary

## Raw Concept

Phase-0 on `mira-wm/mira` during K160 inbox re-archive. Apache-2.0; 5B-param latent diffusion world model for **multiplayer** Rocket League (4 agents, 20 FPS on B200). Dataset + training/inference code + live demo released.

## Narrative

| Signal | Value |
|--------|-------|
| **License** | Apache-2.0 |
| **Maturity** | 362★; active Jul 2026 |
| **Verdict** | **Watch** — castle-sim shelf reference; no Godot dependency |
| **Fit** | MP action attribution, coherence under arbitrary action combos, physical-interaction evals |

**Blockers for castle-sim port:** Rocket League domain; GPU inference cost; hobby slice uses deterministic sim not generative rollouts.

**Steal (design patterns):** per-player action conditioning in replay verification; stress desync under combined inputs; eval beyond pixels.

## Snippets

> "Conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player" [Source: arXiv:2607.05352 abstract — paraphrase]
