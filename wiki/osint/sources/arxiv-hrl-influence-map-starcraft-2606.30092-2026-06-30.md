---
title: "HRL-IM/CBS StarCraft micromanagement — arXiv 2606.30092"
type: source
tags: [source, arxiv, rl-marl, game-dev, rts, castle-sim, k136]
keywords: [2606.30092, HRL-IM/CBS, influence map, cluster-based scripts, StarCraft, micromanagement, Q-table, interpretable RL]
related:
  - concepts/castle-sim-rts-micromanagement-steals.md
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/rl-marl-research.md
  - concepts/active-project-research-routing.md
  - concepts/latent-maps-performance-counterfactual-feedback.md
  - sources/arxiv-2607.00190-latent-maps-performance-2026-07-03.md
  - sources/arxiv-ai-native-games-survey-2607.00527-2026-07-02.md
maturity: draft
read_status: read
created: 2026-06-30
updated: 2026-10-25
clusters: [rl-marl, game-dev]
---

## Relations

- @concepts/castle-sim-rts-micromanagement-steals.md — K136 castle-sim steal synthesis
- @concepts/castle-sim-pathfinding-steals.md — sibling castle-sim routing/AI steals (K126)
- @concepts/rl-marl-research.md — MARL corpus index
- @concepts/active-project-research-routing.md — brief routes to Game Dev wiki

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hierarchical Reinforcement Learning in StarCraft Micromanagement with Influence Maps and Cluster-based Scripts |
| **Authors** | Chunhui Bai, Changhe Li, Dequan Li, Xinye Cai, Shengxiang Yang |
| **arXiv** | 2606.30092 (29 Jun 2026) |
| **sha256** | `4271f18e702cf1e1900ba830107e32da18b476e66efbacf7a15c175f0853c394` |
| **Repo** | none public |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.30092-hierarchical-reinforcement-learning-in-starcraft.pdf` |
| **Retrieved** | 2026-06-30 (inbox) |
| **Read status** | read (abstract + §1–3 methodology overview) |

## Narrative

Proposes **HRL-IM/CBS** for RTS **micromanagement** under huge state-action spaces and sparse win/lose rewards:

1. **Influence map hashing** — encodes battlefield spatial control into compact hex codes (histogram-equalized influence grids) for global situational abstraction.
2. **Cluster-based scripts (CBS)** — dynamic unit partitioning into local combat clusters; scripts execute in reduced action subspaces.
3. **Hierarchical multi-Q-table** — upper level selects clustering strategy; lower level runs tactical scripts; **reward allocation** densifies learning vs terminal-only signal.

Claims competitive results vs deep RL baselines on six asymmetric StarCraft micromanagement scenarios with better **sample efficiency** and **interpretable Q-tables** vs black-box DRL.

**Cemini posture:** **REFERENCE** for **castle-sim** — steal influence-map hashing + cluster scripts for Godot siege micromanagement; not an Adopt (no repo, StarCraft-specific sim). Complements K126 multi-criteria pathfinding steals.

## Snippets

> "Influence map hashing encodes global battlefield situations into compact hexadecimal codes, capturing spatial control and relative advantage." [Source: arXiv:2606.30092 abstract (retrieved 2026-06-30)]

> "Cluster-based scripts enable dynamic local coordination through adaptive unit partitioning." [Source: arXiv:2606.30092 abstract (retrieved 2026-06-30)]

## Dead Ends

- AlphaStar-scale DRL budget incompatible with hobby castle-sim slice — target lightweight tabular/Q-table patterns only.
- No code release — Phase-0 NO-GO for install.
