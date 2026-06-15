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
  - concepts/godot-stagehand-ci-smoke-plan.md
  - concepts/art-pipeline-v0-requirements.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/flow-field-pathfinding.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/stronghold-2-systems-inventory.md
  - meta/sibling-wiki-inventory.md
  - sources/godot-stagehand-castle-sim-ci-eval-2026-06-13.md
  - sources/shaggydev-udd-navigation-2025.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
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
| **Status** | Tier 2 slice 1 **Done** (food/popularity); Tier 1 complete |
| **North star** | Personal **Stronghold 2** clone — Fork **B (3D)** |
| **Next gate** | M0.3D architect spike — `briefs/story-005-3d-architect-spike.md` |
| **GDD** | `briefs/GDD-sh2-personal-clone.md` (local) |
| **Decision log** | `castle-sim/docs/PROJECT_LOG.md` |

### Repo layout

```
castle-sim/
  project.godot
  scenes/game_3d/                # Fork B primary (story-005+)
  scenes/game/game.tscn          # 2D logic lab — maintenance only
  scripts/world3d/               # architect camera, wall placer
  scripts/labor/                 # port to 3D after M0.3D PROCEED
  scripts/grid/wall_grid.gd
  assets/placeholders/           # Kenney-style PNGs (tools/art/generate_placeholders.py)
  scripts/rendering/placeholder_art.gd
  docs/PROJECT_LOG.md            # ADR-lite + session log
  addons/stagehand/              # godot-stagehand (pin: STAGEHAND_PIN.txt)
  scripts/ci/stagehand_l0_smoke.sh
```

### Cursor workflow

Open **castle-sim** as its own folder for implementation. Keep **Game Dev wiki** open for ingest and spec updates. Never commit game binaries or secrets to the public wiki repo.

## Snippets

```bash
open -a Cursor "/Users/claudiobarone/Desktop/projects/castle-sim"
```
