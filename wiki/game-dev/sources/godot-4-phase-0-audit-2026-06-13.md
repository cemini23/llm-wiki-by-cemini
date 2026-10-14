---
title: Godot 4 Phase-0 audit — license, Mac, kits, pathfinding
type: source
tags: [source, godot, phase-0, audit]
keywords: [godot, phase-0, astargrid2d, markodm, mit]
related:
  - entities/engines/godot-4.md
  - concepts/vertical-slice-v0.md
read_status: read
source_type: operator-audit
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @entities/engines/godot-4.md — entity updated with verdict
- @concepts/vertical-slice-v0.md — repo gate

## Raw Concept

Phase-0 deep-read for Godot 4 before opening `castle-sim` implementation repo.

## Narrative

### Scope

License, Mac editor stability, grid-building kit audit (hardcoded paths), pathfinding risk for dynamic walls — per `CLAUDE.md` Phase-0 pattern.

### Artifacts

| Artifact | Location |
|----------|----------|
| Engine source | `/tmp/godot-audit/godot` @ `4.5.2-stable` |
| Mac editor binary | `/tmp/godot-audit/Godot.app` (4.5.2 universal) |
| Kit clone | `/tmp/godot-audit/kits/GodotInGameBuildingSystemGDS` |

### Primary references

- [Godot LICENSE (MIT)](https://github.com/godotengine/godot/blob/4.5.2-stable/LICENSE.txt)
- [AStarGrid2D docs](https://docs.godotengine.org/en/stable/classes/class_astargrid2d.html)
- [Navigation performance guide](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_optimizing_performance.html)
- [MarkoDM GodotInGameBuildingSystemGDS](https://github.com/MarkoDM/GodotInGameBuildingSystemGDS)

### Outcome

**CONDITIONAL-GO** on @entities/engines/godot-4.md — vertical slice may proceed with pinned stable editor and custom 2D grid + `AStarGrid2D` stack.
