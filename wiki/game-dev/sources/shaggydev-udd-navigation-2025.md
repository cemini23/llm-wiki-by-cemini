---
title: Shaggy Dev — Unto Deepest Depths navigation deep dive (2025)
type: source
tags: [source, godot, pathfinding, astar, tilemap]
keywords: [shaggydev, astar2d, tilemap, custom-data, navigation-autoload]
related:
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - sources/shaggydev-tactics-engine-devlog-2023.md
  - entities/projects/castle-sim.md
  - sources/papierkorp-godot-4-tactical-movement-2023.md
read_status: read
source_type: devlog
source_url: https://shaggydev.com/2025/05/19/udd-navigation/
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @entities/projects/castle-sim.md — M0 spike patterns

## Raw Concept

Grid navigation via **Navigation autoload** + `AStar2D` built from TileMap custom data (`is_solid`, `blocks_movement`).

## Narrative

### Why AStar2D not AStarGrid2D [CONFIRMED]

Author needs **non-grid adjacency** (teleporters). castle-sim M0 can use **`AStarGrid2D`** (simpler wall solid toggles) unless drawbridges/portals added Tier 2.

### Cell types

| Custom data | Pathfinding | Line-of-sight / attacks |
|-------------|-------------|-------------------------|
| `is_solid` | point disabled at init | blocks |
| `blocks_movement` | disabled **temporarily** during move queries | may not block ranged |
| (none) | open | open |

**castle-sim mapping:** wall cells = `is_solid`; trees/stockpile occupancy could use temporary disable pattern when many units share chokepoints (Tier 1).

### Path query pattern

1. Temporarily disable `blocks_movement` cells
2. `get_point_path(start, end)`
3. Re-enable

UDD uses path length for **AI scoring**, not locomotion — castle-sim uses path for **actual movement** along waypoints.

### Action blocking

Separate API scans ray of cells for archer shots — units + level objects + solid cells. v0 archer-on-wall can steal **cell scan along relative offsets** without full action Resource system.

## Snippets

```gdscript
# Wall place → disable point (AStar2D style; AStarGrid2D: set_point_solid)
astar_grid.set_point_disabled(id, true)
```

## Dead Ends

- 8-connected diagonal grid + distance checks — more complex than castle-sim v0 needs; stick 4-dir or AStarGrid2D defaults
