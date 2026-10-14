---
title: Liquid Fire — Godot Tactics RPG pathfinding (2024)
type: source
tags: [source, godot, pathfinding, tactics, tutorial]
keywords: [godot, pathfinding, flood-fill, astar, tactics-rpg]
related:
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - entities/engines/godot-4.md
  - sources/shaggydev-tactics-engine-devlog-2023.md
read_status: read
source_type: tutorial-series
source_url: https://theliquidfire.com/2024/04/11/godot-tactics-rpg-05-pathfinding/
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/godot-pathfinding-patterns.md
- @entities/projects/castle-sim.md

## Raw Concept

Part 5 of Godot Tactics RPG series — movement range via **flood-fill breadcrumbs**, not A* to every tile.

## Narrative

### Technique [CONFIRMED]

- Problem: A* finds one A→B path fast; computing **all reachable tiles** via repeated A* is slow
- Solution: BFS/flood-fill with `prev` tile pointers + `distance` — single pass for movement range
- A* reserved for future AI / multi-turn path QoL

### Godot specifics

- `class_name Directions` enum for facings
- Tile holds `content`, `prev`, `distance`
- Unit ↔ tile bidirectional references

### castle-sim mapping

- **Peasant job range preview** — use flood-fill (like tactical movement range)
- **Point-to-point jobs** — `AStarGrid2D.get_id_path` after wall updates (Phase-0 stack)
- Tactical series is grid/turn-based; our slice is real-time but algorithms transfer

## Snippets

> "Finding a path from A to B-Z is a lot of individual paths" — rationale against naive A* for all destinations.
