---
title: arXiv 2607.02222 — CoFL-S sector flow fields for language navigation — 2026-07-16
type: source
tags: [source, arxiv, flow-field, navigation, robotics, research]
keywords: [cofl-s, sector-flow-field, language-conditioned, habitat, vln]
related:
  - concepts/flow-field-pathfinding.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/godot-pathfinding-patterns.md
  - sources/inbox-arxiv-reject-batch-2026-07-16.md
  - sources/emerson-game-ai-pro-flow-field-tiles-2013.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: research-paper
source_url: https://arxiv.org/abs/2607.02222
maturity: validated
created: 2026-07-16
updated: 2026-07-16
---

## Raw Concept

**CoFL-S** (UTokyo Dragon Lab) — **spatially queryable sector flow fields** for local language-conditioned navigation. Extends continuous flow-field policies (CoFL lineage) to ego-centric sector fields over RGB-D + natural-language sub-instructions; continuous-time Habitat benchmark; zero-shot real-world closed-loop claims [TENTATIVE — abstract].

## Narrative

### Architecture [CONFIRMED — abstract / first pages]

| Piece | Role |
|-------|------|
| Vision-language encoder | RGB-D + local instruction → field conditioning |
| CoFL-S decoder | Sector flow field over ego workspace |
| Continuous control | Velocity / action-chunk rollout (Habitat 60 Hz / 30 Hz obs) |

### castle-sim mapping (STEAL-FROM — research shelf)

| Extract | Skip |
|---------|------|
| **Queryable local sectors** — flow field as dense direction map readable from many agents/queries (aligns with Emerson “one field, many agents”) | VLN / Habitat / language-instruction stack |
| Contrast: classical RTS flow fields are goal-Dijkstra; CoFL-S is **learned** language-conditioned field | Training vision-language policies for peasants |
| Tier 2+ note only — v0 stays `AStarGrid2D` | Phase-0 adoption — robotics research stack, no public package found 2026-07-16 |

**Verdict:** **STEAL-FROM (research)** — update @concepts/flow-field-pathfinding.md. Brief: gitignored `briefs/research/cofl-s-sector-flow-field-shelf.md`. **No Phase-0** (no SPDX repo discovered).

## Dead Ends

- Replacing Godot grid flow fields with CoFL-S Habitat models
- Language-conditioned lord AI via VLN policies for v0–v2
