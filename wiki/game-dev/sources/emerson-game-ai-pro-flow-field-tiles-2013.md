---
title: Emerson — Crowd Pathfinding Using Flow Field Tiles (Game AI Pro)
type: source
tags: [source, pathfinding, flow-field, game-ai-pro, emerson]
keywords: [emerson, flow-field, supreme-commander, tiles, portals, crowd]
related:
  - concepts/flow-field-pathfinding.md
  - sources/leifnode-flow-field-pathfinding-2013.md
  - sources/exa-flowfields-firefly-batch-2026-06-13.md
read_status: read
source_type: book-chapter
source_url: https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter23_Crowd_Pathfinding_and_Steering_Using_Flow_Field_Tiles.pdf
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/flow-field-pathfinding.md — hierarchical tile model

## Raw Concept

**Elijah Emerson** — Game AI Pro Ch.23 (2013): *Crowd Pathfinding and Steering Using Flow Field Tiles*. Production pattern from **Supreme Commander 2** for hundreds–thousands of units.

## Narrative

### Core idea [CONFIRMED — chapter + Leif Node cross-ref]

Extends basic cost / integration / flow fields by **partitioning** the world into tiles. Each tile holds local flow-field data; **portals** connect adjacent tiles (edge nodes linking sectors). Long-distance routing:

1. A* (or similar) on **tile graph** + portals → sequence of tiles
2. Build integration+flow fields only for tiles along that path
3. All units share tile-level and field-level results

### Why tiles matter

| Flat single field | Tiled fields |
|-------------------|--------------|
| O(cells) rebuild per goal | Rebuild only traversed tiles |
| 100×100+ costly on CPU | Scales to SC2-scale maps |
| Simple to implement | Portal graph + cache invalidation |

### Steering integration [TENTATIVE — chapter scope]

Chapter covers combining flow-field direction with local steering/avoidance for crowd density — relevant Tier 2+ when archer clusters stack on walls.

### castle-sim relevance

- **Tier 2+** reference when peasant/soldier count exceeds ~30 with shared rally goals
- v0 **20×20 grid**: Leif Node benchmarks suggest single-field rebuild <2ms — tiles optional until map grows
- Portal + A* layer mirrors Stronghold "breach then flood units through gap" gameplay (one goal, many agents)

### Also cited in

- @sources/leifnode-flow-field-pathfinding-2013.md — simplified tutorial implementation
- bevy_flowfield_tiles_plugin, jdxdev Unity DOTS posts — engine ports of same idea

## Snippets

PDF mirror: `gameaipro.com` GameAIPro Chapter 23 (free chapter PDF on site).
