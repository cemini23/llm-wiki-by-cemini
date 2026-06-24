---
title: RTS pathfinding approaches — grid, navmesh, flow fields
type: concept
tags: [concept, pathfinding, rts, godot, research]
keywords: [pathfinding, astar, flow-field, navigation, dynamic-walls]
related:
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - concepts/vertical-slice-v0.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/flow-field-pathfinding.md
  - sources/liquid-fire-godot-tactics-pathfinding-2024.md
  - sources/exa-deep-research-batch-2026-06-13.md
  - sources/exa-flowfields-firefly-batch-2026-06-13.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/vav-labs-astargrid2d-gotchas-2026-06-22.md
  - sources/gdquest-pathfinding-glossary-2026-06-23.md
  - sources/godot-rts-rpg-youtube-watchlist-2026-06-23.md
  - sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
  - concepts/agentic-pcg-level-design.md
  - concepts/scope-tiers.md
  - sources/shaggydev-tactics-engine-devlog-2023.md
  - sources/shaggydev-udd-navigation-2025.md
maturity: validated
created: 2026-06-13
updated: 2026-06-24
---

## Relations

- @entities/engines/godot-4.md — Phase-0 chose `AStarGrid2D` for v0
- @concepts/stronghold-deconstruction.md — pathfinding = high engineering risk

## Raw Concept

Decision guide for castle-sim unit movement around **dynamic walls** — synthesized from Godot Phase-0, Exa paper cluster, and game-dev tutorials.

## Narrative

### Problem shape (Stronghold-like)

- Walls placed/removed during play → navigation graph changes frequently
- v0: ~5–20 peasants, ~10 archers — not 500-unit swarm
- Grid-aligned walls (Tier 1) vs free-angle (SH3+) — we chose grid

### Approach matrix

| Approach | Dynamic walls | Unit count sweet spot | Godot 4 API | castle-sim tier |
|----------|---------------|----------------------|-------------|-----------------|
| **Grid A* (`AStarGrid2D`)** | `set_point_solid` O(1) per cell | Low–medium | Built-in | **v0 — GO** |
| **Navmesh rebake** | Expensive per wall; tile-dense = slow queries | Medium if static | `NavigationRegion2D` | **NO-GO v0** |
| **Flow fields** | Recompute integration on wall change; O(1) per-agent steer | **High** shared destination | Custom; see @concepts/flow-field-pathfinding.md | **Tier 2** if many units same goal |
| **Potential fields (RTS AI papers)** | Soft steering; complements grid | AI micro, not peasants | Custom | Tier 2 combat |
| **RVO / NavigationAgent avoidance** | Does not replace pathfind | Small groups | `NavigationAgent2D` / `NavigationAgent3D` | Optional polish |
| **MAPF / ORCA-class local steer** | Complements global planner | Crowds in chokes | Custom or ORCA libs | **Tier 2+** — @sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md |

### Exa paper cluster (filtered for games)

| Hit | Verdict |
|-----|---------|
| Springer "Path-Planning for RTS Games Based on Potential Fields" | Micro/combat steering — not wall placement |
| "An Improved Pathfinding Algorithm in RTS Games" | General RTS grid — reference only |
| Nature 2025 flow-field BFS integration | Academic; validate before adopt |
| arXiv 2606.22757 Cooperative-ORCA* MAPF | **STEAL-FROM** local avoidance shelf — proactive deadlock vs reactive fallback |
| arXiv UAV/robotics papers in default digest | **Noise** — tighten paper queries |

### Recommended evolution

```
v0:  AStarGrid2D synced to wall TileMapLayer
v1:  Flood-fill for "reachable job sites" preview (see @concepts/godot-pathfinding-patterns.md)
v2:  Flow field for shared goals (stockpile, rally) if unit count > ~30 — @concepts/flow-field-pathfinding.md
v2b: ORCA/RVO nudge if gate deadlocks persist — @sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
MP:  Deterministic sim + lockstep if ever needed (@concepts/rts-networking-deferred.md)
```

### Failure modes (Godot-specific)

- Calling `AStarGrid2D.update()` after `set_point_solid()` → clears solids [CONFIRMED]
- Unreachable target on navmesh → expensive full search [CONFIRMED Godot docs]
- Per-frame `target_position` reset on NavigationAgent → path thrash [CONFIRMED perf guide]

## Snippets

Wall seal check before commit:

```gdscript
grid.set_point_solid(cell, true)
if grid.get_id_path(from, to).is_empty():
    grid.set_point_solid(cell, false)  # reject wall
```

## Dead Ends

- Default Exa query `"RTS pathfinding research paper"` without game filter → UAV papers (2026 digest noise).
