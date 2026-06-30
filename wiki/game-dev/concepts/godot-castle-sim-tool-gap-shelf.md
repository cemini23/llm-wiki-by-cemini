---
title: Godot castle-sim tool gap shelf — post Phase 7 3D
type: concept
tags: [concept, godot, tools, castle-sim, research]
keywords: [godot, castle-sim, gdunit4, stagehand, kenney, flow-field, testing]
related:
  - entities/projects/castle-sim.md
  - entities/tools/godot-stagehand.md
  - entities/tools/godot-mcp-landscape.md
  - concepts/flow-field-pathfinding.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/art-pipeline-v0-requirements.md
  - sources/godot-castle-sim-tool-gap-research-2026-06-17.md
  - entities/tools/pcgodot.md
maturity: validated
created: 2026-06-17
updated: 2026-06-30
---

## Relations

- @entities/projects/castle-sim.md — implementation status (Phase 7 3D done)
- Local operator brief: `briefs/research/godot-castle-sim-tool-gap-research.md` (gitignored, full tables)

## Raw Concept

Targeted Godot tool/workflow research after castle-sim story-012–029 — closes engineering gaps (monolithic controller, test pyramid, 3D art, UI, nav scale) without replatforming.

## Narrative

### Gap summary [CONFIRMED — code audit 2026-06-17]

| Area | Current | Target |
|------|---------|--------|
| Architecture | ~1656-line `Game3DController` | Split input / HUD / test harness |
| Unit tests | CLI integration only | GdUnit4 or GUT on economy services |
| Automation | Stagehand L0 on 2D spike | L1 on `game_3d.tscn` |
| Art | CSG `MeshFactory3D` | Kenney GridMap steal + CC0 meshes |
| UI | Keyboard modes | Build bar + SH2 popularity panel |
| Nav | Per-agent `AStarGrid2D` | Flow-field spike when crowds stutter |

### Recommended posture

| Tool | Verdict | When |
|------|---------|------|
| GdUnit4 | **CONDITIONAL-GO** | Service unit tests + CI |
| GUT | **CONDITIONAL-GO** alt | If GdUnit4 pin fails on 4.5.2 |
| godot-stagehand | **GO** extend | L1 `game_3d` smoke |
| Kenney City Builder kit | **STEAL-FROM** | 3D art + GridMap patterns |
| Custom flow field (Vav Labs) | **STEAL-FROM** | Spike before any addon |
| PCGODOT | **CONDITIONAL-GO** | Tier 2+ prop scatter — @entities/tools/pcgodot.md |
| VectorFieldNavigation addon | **EVAL** | Phase-0 clone first |
| rluders/rts-framework | **STEAL-FROM** | Signal decoupling only |
| godot-debug-menu | **GO** | Dev perf overlay |
| Cyclops Level Builder | **CONDITIONAL-GO** | Editor map blockout only |
| hi-godot-ai MCP | **Defer** | After controller split |

### Priority order

1. `briefs/architecture.md` + controller split stories  
2. Stagehand L1 on primary 3D scene  
3. GdUnit4 on `PopularityService` / rank gates  
4. Kenney mesh pass (one building at a time)  
5. Flow-field spike on trigger (perf profile)

### Explicit non-goals

Merge Open RTS codebase; install SerpentAI; adopt NavigationRegion3D for wall paint; multiplayer stack.

## Snippets

Full research + planner prompt: `briefs/research/godot-castle-sim-tool-gap-research.md`
