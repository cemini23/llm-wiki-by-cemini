---
title: castle-sim — implementation repo
type: entity
tags: [entity, project, godot, castle-sim]
keywords: [castle-sim, godot, vertical-slice, implementation]
related:
  - concepts/vertical-slice-v0.md
  - concepts/stronghold-systems-inventory.md
  - entities/engines/godot-4.md
  - concepts/agent-harness-castle-project.md
  - concepts/art-pipeline-v0-requirements.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/vertical-slice-v0.md — acceptance criteria (canonical)
- @entities/engines/godot-4.md — **CONDITIONAL-GO** engine

## Raw Concept

Separate git repo for runnable Godot code. Wiki holds spec; repo holds implementation.

## Narrative

| Field | Value |
|-------|-------|
| **Path** | `/Users/claudiobarone/Desktop/projects/castle-sim/` |
| **Visibility** | Local (private GitHub TBD — ROADMAP D3) |
| **Engine** | Godot 4.5+ (pin 4.5.2 or 4.6.x stable) |
| **Language** | GDScript |
| **Status** | Scaffolded 2026-06-13; milestone 1 = pathfinding spike |

### Repo layout

```
castle-sim/
  project.godot
  scenes/main.tscn
  scenes/spike/pathfinding_spike.tscn
  scripts/grid/wall_grid.gd
  scripts/pathfinding/pathfinding_spike.gd
  assets/placeholders/
```

### Cursor workflow

Open **castle-sim** as its own folder for implementation. Keep **Game Dev wiki** open for ingest and spec updates. Never commit game binaries or secrets to the public wiki repo.

## Snippets

```bash
open -a Cursor "/Users/claudiobarone/Desktop/projects/castle-sim"
```
