---
title: Leif Node — Flow Field Pathfinding tutorial (2013)
type: source
tags: [source, pathfinding, flow-field, tutorial]
keywords: [leifnode, flow-field, dijkstra, integration-field, cost-field]
related:
  - concepts/flow-field-pathfinding.md
  - sources/emerson-game-ai-pro-flow-field-tiles-2013.md
read_status: read
source_type: blog
source_url: https://leifnode.com/2013/12/flow-field-pathfinding/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/flow-field-pathfinding.md — three-field algorithm walkthrough

## Raw Concept

Accessible implementation guide for **cost → integration → flow** pipeline; cites Planetary Annihilation stream and Emerson Game AI Pro for scale-up.

## Narrative

### When A* struggles [CONFIRMED — article]

Dense grid + hundreds of units to **same goal** + dynamic environment + frequent retargeting. Alternatives (async A*, D*, navmesh nudging) compose badly; flow fields unify.

### Three fields

| Field | Storage (article) | Role |
|-------|-------------------|------|
| Cost | byte 1–255 per cell | Terrain weight; 255 = wall |
| Integration | uint16 path cost | Dijkstra from goal |
| Flow | byte index → 8 dirs | Steer toward lowest neighbor |

Cost change → rebuild integration + flow. Unit count does **not** affect rebuild time.

### Benchmarks (C++ release, empty map) [CONFIRMED]

| Grid | ~ms |
|------|-----|
| 10×10 | 0.2 |
| 20×20 | 1.0 |
| 50×50 | 5.2 |
| 100×100 | 20 |

Walls can speed integration ~30% vs open field. Debug builds ~15× slower.

### Scale recommendation

100×100 single field heavy → **100× 10×10 tiles** with Emerson portal A* (@sources/emerson-game-ai-pro-flow-field-tiles-2013.md).

### Following

Unit world position → grid cell → lookup flow vector → blend into velocity. Float fields optional for smoother paths than 8-way.

### castle-sim hook

20×20 hobby map: **~1ms** full rebuild acceptable on wall place if goals are shared (stockpile). Per-peasant unique tree targets still favor `AStarGrid2D`.

## Snippets

Integration uses open-list Dijkstra (not priority queue in demo); production should use proper queue for weighted grids — same note as @sources/vav-labs-godot-flow-fields-2026.md.
