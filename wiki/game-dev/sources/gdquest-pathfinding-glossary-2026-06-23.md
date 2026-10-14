---
title: GDQuest — pathfinding glossary (Godot AStar vs Navigation)
type: source
tags: [source, godot, pathfinding, gdquest, glossary]
keywords: [astar, navigation, gdquest, godot-4]
related:
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - entities/engines/godot-4.md
  - sources/vav-labs-astargrid2d-gotchas-2026-06-22.md
  - sources/shaggydev-udd-navigation-2025.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-23.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: web-article
source_url: https://www.gdquest.com/library/glossary/pathfinding/
maturity: validated
created: 2026-06-23
updated: 2026-06-23
---

## Raw Concept

**GDQuest Library glossary** (Jun 2026) — beginner-facing map of Godot pathfinding: direct `AStar2D`/`AStar3D` vs NavigationRegion + NavigationAgent stacks.

## Narrative

### castle-sim mapping [CONFIRMED]

| GDQuest layer | castle-sim choice |
|---------------|-------------------|
| `AStar2D` / `AStarGrid2D` grid paths | **v0 default** — peasant job paths (@sources/vav-labs-astargrid2d-gotchas-2026-06-22.md) |
| NavigationRegion2D + NavigationAgent2D | **Defer** — RVO/crowd nudge (Pattern 5 @concepts/godot-pathfinding-patterns.md) |
| `AStar3D` | Fork B 3D — architect spike uses navmesh hybrid (@concepts/godot-3d-sh2-architect-spike-plan.md) |

### Verdict

**STEAL-FROM (terminology)** — onboarding link for harness agents; no runtime dependency.

## Dead Ends

- Replacing grid `AStarGrid2D` with NavigationAgent for v0 — overkill before crowding profiler signal
