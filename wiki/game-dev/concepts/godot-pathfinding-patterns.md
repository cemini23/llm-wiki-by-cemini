---
title: Godot pathfinding patterns — tactics + grid notes
type: concept
tags: [concept, godot, pathfinding, tilemap]
keywords: [godot, flood-fill, astargrid2d, tilemap, movement]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/flow-field-pathfinding.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - sources/liquid-fire-godot-tactics-pathfinding-2024.md
  - sources/kobold-tactics-tilemap-pathfinding-2023.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/shaggydev-tactics-engine-devlog-2023.md
  - sources/shaggydev-udd-navigation-2025.md
  - sources/papierkorp-godot-4-tactical-movement-2023.md
  - sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md
  - sources/vav-labs-astargrid2d-gotchas-2026-06-22.md
  - sources/gdquest-pathfinding-glossary-2026-06-23.md
  - sources/godot-rts-rpg-youtube-watchlist-2026-06-23.md
  - sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
  - entities/tools/binarytracking.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
maturity: validated
created: 2026-06-13
updated: 2026-06-23
---

## Relations

- @entities/projects/castle-sim.md — spike implementation
- @sources/shaggydev-tactics-engine-devlog-2023.md
- @sources/shaggydev-udd-navigation-2025.md
- @sources/vav-labs-astargrid2d-gotchas-2026-06-22.md — AStarGrid2D init + diagonal/JPS checklist
- @sources/gdquest-pathfinding-glossary-2026-06-23.md — AStar vs NavigationRegion primer
- @sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md — K125 binary segment search steal
- @entities/tools/binarytracking.md

## Raw Concept

Godot-specific pathfinding patterns for grid castle-sim — beyond Phase-0 one-liners.

## Narrative

### Pattern 1 — Job path (v0)

`AStarGrid2D` aligned 1:1 with wall grid. On wall place/remove → `set_point_solid`. Peasant requests path on job assign + on `wall_changed` signal (local invalidation).

**Init checklist** (@sources/vav-labs-astargrid2d-gotchas-2026-06-22.md): `DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES`, `jumping_enabled = false`, Octile heuristic on 8-dir grids; call `update()` only on region resize then re-sync all solids.

### Pattern 2 — Reachable-area preview (v1)

From @sources/liquid-fire-godot-tactics-pathfinding-2024.md: **flood-fill** with breadcrumb `prev` + `distance` for all tiles within N steps — faster than N× A* queries. Use for UI highlight ("where can this peasant reach?").

### Pattern 3 — Isometric snap (art + logic)

`TileMapLayer.local_to_map` / `map_to_local` for wall draw; pathfinding grid can stay **orthogonal** internally even if visuals are isometric (common Stronghold-style cheat) [TENTATIVE — industry pattern].

### Pattern 4 — Kobold Tactics (C# reference)

Exa hit: [Kobold Tactics TileMap pathfinding](https://koboldtactics.com/tilemap-pathfinding-made-simple-godot-4-c/) — C# but documents Godot 4 `TileMapLayer` + A* integration. **Reference only** — castle-sim uses GDScript.

### Pattern 5 — NavigationAgent avoidance + ORCA shelf (defer)

Enable avoidance only when units crowd; pathfind on grid, optionally nudge with RVO for collision resolution. If gate deadlocks persist at Tier 2, read MAPF/ORCA proactive-deadlock literature — @sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md (global planner + local steer split).

### Pattern 6 — Flow field (Tier 2)

From @sources/vav-labs-godot-flow-fields-2026.md: when many units share a goal, build **integration field from goal** + **flow field** on the same blocked grid as walls. Rebuild on `wall_changed` or goal move — not every frame. Hybrid: A* for lone peasants, flow for rally/stockpile crowds (@concepts/flow-field-pathfinding.md).

### Pattern 7 — Navigation Service autoload (Shaggy Dev)

From @sources/shaggydev-tactics-engine-devlog-2023.md and @sources/shaggydev-udd-navigation-2025.md:

- Single autoload owns `AStarGrid2D` or `AStar2D` built from TileMap custom data (`is_solid`, optional `blocks_movement`)
- Wall grid emits `wall_changed`; service updates solids — peasants query service, not TileMap
- Temporary disable of soft blockers during path query when units occupy cells (Tier 1 crowding)

**castle-sim M0 default:** Pattern 1 + Pattern 7 thin slice.

### Pattern 8 — Range highlight only (papierkorp)

From @sources/papierkorp-godot-4-tactical-movement-2023.md: Manhattan `range` loops + hover TileMap layer for **debug UI** ("where can unit reach in N steps without walls"). Not a substitute for A* around walls.

## Snippets

Sync wall cell:

```gdscript
func _on_wall_placed(cell: Vector2i) -> void:
    astar.set_point_solid(cell, true)
    wall_changed.emit(cell)
```

## Dead Ends

- Liquid Fire series uses **3D tactics** prefabs — adapt algorithms to 2D `Node2D` slice, don't copy scene tree verbatim.
