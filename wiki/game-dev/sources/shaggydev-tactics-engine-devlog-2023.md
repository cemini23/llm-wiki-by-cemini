---
title: Shaggy Dev — tactics engine architecture (2023)
type: source
tags: [source, godot, tactics, pathfinding, devlog]
keywords: [shaggydev, godot, tactics, navigation-service, astar]
related:
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - sources/shaggydev-udd-navigation-2025.md
  - sources/liquid-fire-godot-tactics-pathfinding-2024.md
read_status: read
source_type: devlog
source_url: https://shaggydev.com/2023/07/04/tactics-engine-devlog/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/godot-pathfinding-patterns.md — Pattern 7 Navigation Service

## Raw Concept

Turn-based tactics engine structure: **Services** layer isolates pathfinding/LOS from units; Godot 3 `AStar2D` / Godot 4 `AStarGrid2D`.

## Narrative

### Level node tree [CONFIRMED]

```
Level → Services (Navigation, Combat, …)
      → Environment (TileMaps, objects)
      → Combatants (groups → units)
      → UI
```

**Navigation Service** owns tilemap + dynamic blockers (units, objects, terrain). Exposes `get_cell_path`, line-of-sight queries — units never reach into tilemaps directly.

### castle-sim borrow

- M0: thin **Navigation autoload** (or `PathfindingService`) between `wall_grid` and peasant AI — same decoupling, real-time not turn-based
- Turn order / combat services **defer** until M1+ combat

### Actions as Resources [TENTATIVE for castle-sim]

Shaggy uses Godot Resources for action data + Effect groups synced to animations. Overkill for v0 peasant chop loop; revisit for archer-on-wall Tier 1.

### Godot version note

Author moved Kaiju prototype to Godot 4 for typed arrays + custom resources; pixel-art rendering caveat on 4.x — relevant if castle-sim stays 2D isometric.

## Snippets

> "Rather than directly letting each entity talk to everything else, the Navigation Service is responsible for keeping track of these things." — Shaggy Dev, 2023

## Dead Ends

- Full tactics turn loop — castle-sim v0 is real-time Stronghold-style, not X-COM
