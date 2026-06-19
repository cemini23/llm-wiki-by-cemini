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
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/flow-field-pathfinding.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/stronghold-2-systems-inventory.md
  - meta/sibling-wiki-inventory.md
  - sources/godot-stagehand-castle-sim-ci-eval-2026-06-13.md
  - sources/godot-castle-sim-tool-gap-research-2026-06-17.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md
  - concepts/stronghold-2-lord-feasts-luxury-chains.md
  - sources/sh2-heaven-resources-luxury-deep-read-2026-06-19.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-estates-system.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-campaign-economy-curriculum.md
  - concepts/stronghold-2-castle-structures.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/sh2-heaven-pow-missions-2026-06-18.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - concepts/stronghold-2-production-buildings.md
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-nevikov-new-balance-sheet-2026-06-18.md
  - entities/tools/sh2-mp-ai-enabler.md
  - concepts/stronghold-2-visual-qol-presets.md
  - entities/tools/sh2-community-lord-editor.md
  - sources/sh2-community-lord-editor-phase-0-audit-2026-06-18.md
  - concepts/stronghold-2-military-units.md
  - sources/shaggydev-udd-navigation-2025.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
maturity: validated
created: 2026-06-13
updated: 2026-06-17
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
| **Status** | **Phase 7 3D Done** — story-012–029; operator perf PASS 2026-06-17 |
| **North star** | Personal **Stronghold 2** clone — Fork **B (3D)** |
| **Next gate** | SH2 retail playtest parity — `briefs/story-030-sh2-playtest-parity.md` |
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
