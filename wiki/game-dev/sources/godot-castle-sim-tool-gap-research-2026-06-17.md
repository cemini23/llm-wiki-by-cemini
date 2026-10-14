---
title: Godot castle-sim tool gap research — 2026-06-17
type: source
tags: [source, godot, tools, castle-sim, research]
keywords: [gdunit4, gut, kenney, flow-field, stagehand, rts-framework]
related:
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - entities/projects/castle-sim.md
  - entities/tools/godot-stagehand.md
  - concepts/flow-field-pathfinding.md
  - sources/vav-labs-godot-flow-fields-2026.md
read_status: read
source_type: operator-research
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Raw Concept

Deep-targeted Godot tool/workflow research for castle-sim — codebase audit + Brave/GitHub scan. Output: gitignored `briefs/research/godot-castle-sim-tool-gap-research.md` + @concepts/godot-castle-sim-tool-gap-shelf.md.

## Narrative

### Method

1. Explore castle-sim repo (autoloads, `Game3DController`, tests, addons)  
2. Cross-check existing wiki Phase-0 (@entities/tools/godot-mcp-landscape.md)  
3. Web search: GUT, GdUnit4, flow-field addons, Kenney city builder, RTS framework, debug overlay, godot-ci  

### Key findings

- **Testing:** GdUnit4 preferred for new unit layer; keep CLI `*_3d_test` integration suite  
- **Automation:** Extend pinned stagehand to `game_3d.tscn` L1 (FPS assert already headless via `perf_3d_test`)  
- **Art:** Kenney Starter-Kit-City-Builder MIT + CC0 — steal GridMap/camera, not full merge  
- **Nav:** Custom flow field from @sources/vav-labs-godot-flow-fields-2026.md before third-party addon  
- **Architecture:** rluders/rts-framework signal patterns; internal split before more gameplay  

### Phase-0 queue (not run this session)

GdUnit4, Kenney kit, VectorFieldNavigation, rts-framework, godot-debug-menu — clone audit before `addons/` install.

## Snippets

Operator brief path: `briefs/research/godot-castle-sim-tool-gap-research.md`
