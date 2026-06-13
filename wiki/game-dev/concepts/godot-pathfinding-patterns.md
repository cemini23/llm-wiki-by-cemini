---
title: Godot pathfinding patterns — tactics + grid notes
type: concept
tags: [concept, godot, pathfinding, tilemap]
keywords: [godot, flood-fill, astargrid2d, tilemap, movement]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/flow-field-pathfinding.md
  - entities/engines/godot-4.md
  - sources/liquid-fire-godot-tactics-pathfinding-2024.md
  - sources/kobold-tactics-tilemap-pathfinding-2023.md
  - sources/vav-labs-godot-flow-fields-2026.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @entities/projects/castle-sim.md — spike implementation

## Raw Concept

Godot-specific pathfinding patterns for grid castle-sim — beyond Phase-0 one-liners.

## Narrative

### Pattern 1 — Job path (v0)

`AStarGrid2D` aligned 1:1 with wall grid. On wall place/remove → `set_point_solid`. Peasant requests path on job assign + on `wall_changed` signal (local invalidation).

### Pattern 2 — Reachable-area preview (v1)

From @sources/liquid-fire-godot-tactics-pathfinding-2024.md: **flood-fill** with breadcrumb `prev` + `distance` for all tiles within N steps — faster than N× A* queries. Use for UI highlight ("where can this peasant reach?").

### Pattern 3 — Isometric snap (art + logic)

`TileMapLayer.local_to_map` / `map_to_local` for wall draw; pathfinding grid can stay **orthogonal** internally even if visuals are isometric (common Stronghold-style cheat) [TENTATIVE — industry pattern].

### Pattern 4 — Kobold Tactics (C# reference)

Exa hit: [Kobold Tactics TileMap pathfinding](https://koboldtactics.com/tilemap-pathfinding-made-simple-godot-4-c/) — C# but documents Godot 4 `TileMapLayer` + A* integration. **Reference only** — castle-sim uses GDScript.

### Pattern 5 — NavigationAgent2D (defer)

Enable avoidance only when units crowd; pathfind on grid, optionally nudge with RVO for collision resolution.

### Pattern 6 — Flow field (Tier 2)

From @sources/vav-labs-godot-flow-fields-2026.md: when many units share a goal, build **integration field from goal** + **flow field** on the same blocked grid as walls. Rebuild on `wall_changed` or goal move — not every frame. Hybrid: A* for lone peasants, flow for rally/stockpile crowds (@concepts/flow-field-pathfinding.md).

## Snippets

Sync wall cell:

```gdscript
func _on_wall_placed(cell: Vector2i) -> void:
    astar.set_point_solid(cell, true)
    wall_changed.emit(cell)
```

## Dead Ends

- Liquid Fire series uses **3D tactics** prefabs — adapt algorithms to 2D `Node2D` slice, don't copy scene tree verbatim.
