---
title: Vav Labs — Flow Field Pathfinding in Godot (2026)
type: source
tags: [source, godot, pathfinding, flow-field]
keywords: [godot, flow-field, integration-field, vav-labs, pathforge]
related:
  - concepts/flow-field-pathfinding.md
  - concepts/godot-pathfinding-patterns.md
  - entities/engines/godot-4.md
  - concepts/rts-pathfinding-approaches.md
  - sources/exa-flowfields-firefly-batch-2026-06-13.md
read_status: read
source_type: blog
source_url: https://vav-labs.com/blog/godot-flow-fields-shared-goal/
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @entities/projects/castle-sim.md — Tier 2 Godot reference implementation

## Raw Concept

Godot 4–oriented explainer: invert pathfinding (goal → whole grid), integration + flow passes, hybrid with A*, dynamic rebuild discipline.

## Narrative

### Problem stated [CONFIRMED]

200 units × A* to same rally point = redundant searches and frame spikes. Flow field: **one compute per goal**, O(1) per-agent steer lookup.

### Algorithm (GDScript sketch in article)

1. `build_integration(goal, w, h, blocked)` — BFS/Dijkstra relaxation from goal; `INF` blocked
2. `build_flow(cost, w, h)` — each cell points to lowest-cost neighbor
3. `steer(agent, flow, w)` — `velocity = flow[cell] * speed`

Article notes: use **priority queue** on large weighted grids (demo uses queue for clarity).

### When to use [CONFIRMED]

| Flow field wins | A* wins |
|---------------|---------|
| Many agents, 1–few goals | Few agents, many distinct goals |
| Attack-move, TD lane, flee one exit | Solo peasant to unique job |

**Hybrid** both on same grid in production games.

### Dynamic goals / map

Rebuild on **change**, not every frame. Cap rebuild frequency; regional repair for localized wall edits. Wandering target → coarser field at lower Hz beats perfect stutter.

### PathForge mention [NEEDS VERIFICATION — product marketing]

Author building **PathForge** for Godot 4 (influence maps, clearance, diagnostics). Treat as WATCH — not vetted for castle-sim adoption.

### castle-sim Tier gate

Adopt when: shared-goal unit count > ~30 **and** pathfinding shows in profiler. Until then: @concepts/vertical-slice-v0.md spike on `AStarGrid2D`.

## Snippets

See article for full `build_integration` / `build_flow` / `steer` functions — portable to castle-sim wall grid with `blocked` synced from `TileMapLayer`.
