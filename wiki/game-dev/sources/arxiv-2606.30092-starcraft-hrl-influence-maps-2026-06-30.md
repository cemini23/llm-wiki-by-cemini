---
title: arXiv 2606.30092 — HRL-IM/CBS StarCraft influence maps — 2026-06-30
type: source
tags: [source, arxiv, rts, influence-map, rl, starcraft]
keywords: [hrl-im-cbs, influence-map, starcraft, micromanagement, q-table]
related:
  - concepts/rts-siege-ai-reference.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - concepts/flow-field-pathfinding.md
  - concepts/scope-tiers.md
  - sources/inbox-arxiv-reject-batch-2026-06-30.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/2606.30092
maturity: validated
created: 2026-06-30
updated: 2026-06-30
---

## Raw Concept

**HRL-IM/CBS** — hierarchical RL for StarCraft **micromanagement** using **influence map hashing** + **cluster-based scripts** (CBS). Multi-Q-table upper/lower hierarchy with dense reward allocation; compares favorably to DRL baselines on sample efficiency and interpretability.

## Narrative

### Architecture [CONFIRMED — abstract + intro]

| Component | Role |
|-----------|------|
| **Influence map hashing** | Encodes unit distribution → compact hex codes; spatial control + relative advantage |
| **Cluster-based scripts (CBS)** | Dynamic local unit partitioning; macro actions in combat subspaces |
| **Hierarchical multi-Q-table** | Upper: clustering strategy; lower: tactical execution |
| **Reward allocation** | Dense signals mitigating win/lose-only sparse rewards |

### castle-sim mapping (Tier 2+ / Phase E+)

| Extract | Skip |
|---------|------|
| **Influence maps** as interpretable spatial state (not black-box NN) for raid micro | Training StarCraft micromanagement agents |
| Cluster/scripts pattern parallels lord **macro actions** + local unit groups | Full HRL stack for hobby Godot slice |
| Contrast with @sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md (DRL leaves on BT) | Replacing JSON `lord_profiles.json` with Q-tables |

**Verdict:** **STEAL-FROM (research shelf)** — gitignored `briefs/research/starcraft-influence-map-hrl-shelf.md`. v0–v1: hand-coded raid timer + path; Tier 2+: influence bias field before any RL leaf.

Cross-ref: @concepts/flow-field-pathfinding.md (cost/influence bias); @concepts/rts-siege-ai-reference.md (raid AI minimum).

## Dead Ends

- Porting HRL-IM/CBS to Godot for vertical slice — training cost + scope
- Conflating influence maps with flow fields — related spatial abstractions, different update semantics
