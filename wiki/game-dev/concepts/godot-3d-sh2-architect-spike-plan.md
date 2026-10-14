---
title: Godot 3D — SH2 architect spike plan
type: concept
tags: [concept, godot, 3d, stronghold-2, camera, spike]
keywords: [godot-3d, architect-camera, wall-build, navigation-region3d]
related:
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-castle-structures.md
  - concepts/stronghold-2-architect-controls.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - concepts/godot-pathfinding-patterns.md
  - sources/arxiv-2606.26925-vr-dynamic-feedback-pointing-2026-07-02.md
maturity: draft
created: 2026-06-13
updated: 2026-07-02
---

## Relations

- @concepts/operator-vision-sh2-personal-clone.md — **Fork B locked** (operator 2026-06-13)
- @concepts/stronghold-2-architect-controls.md — retail SH2 hotkey parity target
- `briefs/story-005-3d-architect-spike.md` — first implementation story

## Raw Concept

Phase-0 **3D presentation spike** for personal SH2 clone: Godot 4 **3D** with **architect top-down camera** (SH2 Space-bar mode), gridded wall placement, and one peasant pathing on the ground plane — before honour/crime sim layers.

## Narrative

### Why 3D (operator rationale)

Operator would buy SH2 on Mac if 2D were enough — **3D castle building and tower sightlines are the product**. A 2D fork duplicates neither SH2 nor the motivation to build a personal clone.

**Reference play on Mac:** no native port. **Operator: zero spend** — use YouTube parity ingest (@sources/sh2-youtube-parity-watchlist-2026-06-17.md) + SH2 Heaven; optional free retail only (Whisky / CrossOver trial / friend's PC). Godot clone does not require running retail SH2.

### What to salvage from current `castle-sim` (2D)

| Keep (logic) | Rewrite (presentation) |
|--------------|------------------------|
| `LaborDirector`, `JobBehavior`, economy services | Scene tree — `Node2D` → `Node3D` / subviewport |
| Popularity / granary rules (if implemented) | HUD layout |
| Headless test **patterns** (CLI gates) | 2D-specific tests; new 3D smoke |
| Grid occupancy **ideas** | `AStarGrid2D` → **XZ grid** + `NavigationRegion3D` or layered grid A* |

Do **not** extend 2D wall drawing further — freeze 2D main scene except bugfixes until 3D spike passes.

### SH2 3D targets (Bradbury Q&A + play reference)

| Feature | Spike | Later |
|---------|-------|-------|
| **Architect camera** — top-down build, rotate optional | **M0.3D** | polish |
| **Wall paint** — thick segments, no 2D gap bugs | **M0.3D** | crenellations, gates |
| **Play camera** — closer third-person or RTS orbit | defer | lord avatar later |
| Tower interiors | defer | spiral stair fights |
| Siege on walls | defer | no sword-wall-hack rule |

### Recommended Godot 3D stack (hobby)

```
Ground: StaticBody3D + MeshInstance (flat plane) or GridMap floor
Walls:  Grid-snapped CSGBox3D or glTF segments instanced on XZ cell
Camera: Orthographic or low-FOV perspective; "architect" = high Y, pitch -90° or -75°
Input:  Raycast from camera → world XZ → snap to cell (Vector2i x,z)
Nav:    Option A — NavigationRegion3D rebake on wall change (OK for small maps)
        Option B — AStar3D / custom grid on XZ mirroring 2D spike pattern
Peasants: CharacterBody3D + NavigationAgent3D (start with 1 unit)
```

**Start with Option A** on 32×32 or smaller — rebake cost acceptable at hobby unit counts. Switch to grid A* if rebake stutters.

MarkoDM 3D building kit (@entities/engines/godot-4.md Phase-0) — **reference only**, not dependency.

### M0.3D spike gate (before SH2 sim layers)

| # | Acceptance |
|---|------------|
| 1 | Toggle architect camera (Space or key) — top-down, pan/zoom |
| 2 | LMB paints wall segment on snapped grid; RMB erases |
| 3 | Walls are **3D meshes** with collision — visibly thick, not flat tiles |
| 4 | One peasant walks from keep → tree → stockpile around placed walls |
| 5 | 60 fps × 5 min on operator Mac (editor or export) |
| 6 | Document PROCEED / PIVOT / KILL in PROJECT_LOG |

**PIVOT triggers:** rebake unusable, grid snap feels wrong vs SH2 memory, Mac perf collapse.

### Repo layout (proposed)

```
castle-sim/
  scenes/
    game_3d/           # new main line
      architect_test.tscn
    game/              # legacy 2D — maintenance only
  scripts/
    world3d/
      grid_snap.gd
      wall_placer_3d.gd
      architect_camera.gd
    navigation/
      nav_service_3d.gd
```

### Art v0

- CSG gray blocks + Kenney CC0 kit if needed — **no SH2 asset rips**
- `@image-gen-wiki` for texture pass later; blockout first

## Snippets

Architect camera sketch:

```gdscript
# architect mode: fixed yaw, high position, look_at castle center
camera.position = focus + Vector3(0, 40, 0)
camera.rotation_degrees = Vector3(-90, 0, 0)  # or Camera3D.PROJECTION_ORTHOGONAL
```

Wall snap (XZ):

```gdscript
var hit := raycast_to_ground(screen_pos)
var cell := Vector2i(floori(hit.x / CELL), floori(hit.z / CELL))
```

## Dead Ends

- **Continuing 2D as primary** — operator rejected; reference play available via CrossOver if needed
- **Full 3D + all SH2 sim at once** — architect spike first, then port popularity from 2D codebase
- **Unity pivot** — Godot Phase-0 already passed; stay unless spike KILLs
