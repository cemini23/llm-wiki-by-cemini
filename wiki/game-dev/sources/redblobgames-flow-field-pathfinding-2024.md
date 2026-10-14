---
title: Red Blob Games — Flow field pathfinding (2024 blog)
type: source
tags: [source, pathfinding, flow-field, redblobgames]
keywords: [redblobgames, amit-patel, flow-field, distance-field, dijkstra]
related:
  - concepts/flow-field-pathfinding.md
  - sources/leifnode-flow-field-pathfinding-2013.md
read_status: read
source_type: blog
source_url: https://www.redblobgames.com/blog/2024-04-27-flow-field-pathfinding/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/flow-field-pathfinding.md — conceptual tie to A* outputs

## Raw Concept

Amit Patel clarifies flow fields after years of reader questions — separates flow fields from hierarchical pathfinding conflation.

## Narrative

### Definition [CONFIRMED]

1. **Flow field** — vector per graph location pointing toward a single destination
2. Optional interpolation between graph nodes for sub-cell agents
3. Optional **hierarchy** of coarse+fine fields for speed (separate concern)

### Distance fields [CONFIRMED]

Related but distinct: Dijkstra maps (roguelikes), influence maps (strategy), SDF uses in graphics. Vector calculus: **gradient of distance field ≈ flow field**.

### A* connection [CONFIRMED]

Graph A* already emits `cost_so_far` (distance) and `came_from` (flow predecessor). Flow fields on grids = run that once from goal for all cells.

### Updated tutorials

- Stanford pathfinding variations (flow-field section)
- Tower defense pathfinding page updated for flow + distance

### castle-sim use

Conceptual validation only — no Godot code. Pair with @sources/vav-labs-godot-flow-fields-2026.md for implementation.

## Snippets

Interactive A* tutorial: https://www.redblobgames.com/pathfinding/a-star/introduction.html
