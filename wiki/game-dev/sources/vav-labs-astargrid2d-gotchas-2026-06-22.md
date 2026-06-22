---
title: vav_labs — AStarGrid2D gotchas and sandbox — 2026-06-22
type: source
tags: [source, godot, pathfinding, astargrid2d, devto]
keywords: [astargrid2d, godot-4, diagonal, jumping, octile]
related:
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/shaggydev-udd-navigation-2025.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/rts-pathfinding-approaches.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - sources/inbox-arxiv-reject-batch-2026-06-22.md
  - meta/cross-wiki-routing.md
read_status: read
source_type: web-article
source_url: https://dev.to/vav_labs/astargrid2d-in-godot-4-the-gotchas-and-an-interactive-sandbox-3dl8
maturity: validated
created: 2026-06-22
updated: 2026-06-22
---

## Raw Concept

**vav_labs** (Jun 2026) — practical `AStarGrid2D` gotcha list + interactive browser sandbox. Full reference: https://vav-labs.com/blog/astargrid2d-complete-reference/

Same author as @sources/vav-labs-godot-flow-fields-2026.md.

## Narrative

### Five gotchas [CONFIRMED]

| Gotcha | castle-sim impact |
|--------|-------------------|
| Must call `update()` after region/cell size change | Empty path, no error — spike must rebuild grid on map resize |
| **`update()` wipes solids + weights** | Re-apply `set_point_solid` after every `update()` — aligns with Phase-0 note on issue #8893 |
| `DIAGONAL_MODE_ALWAYS` corner-cuts walls | Use **`ONLY_IF_NO_OBSTACLES`** for peasant paths |
| `jumping_enabled` ignores weight scale | Keep JPS off if swamp/slow terrain weights matter later |
| Manhattan heuristic overestimates on 8-dir grids | Prefer **Octile** heuristic when diagonals enabled |

### castle-sim defaults (v0)

```gdscript
# NavigationService init sketch
grid.diagonal_mode = AStarGrid2D.DIAGONAL_MODE_ONLY_IF_NO_OBSTACLES
grid.jumping_enabled = false
# After resize only:
grid.update()
# Then re-sync all wall solids from TileMapLayer
```

### vs flow fields

Peasant job paths stay **AStarGrid2D** (Pattern 1 @concepts/godot-pathfinding-patterns.md). Flow fields remain Tier 2 for shared-goal crowds (@sources/vav-labs-godot-flow-fields-2026.md).

### Verdict

**STEAL-FROM (implementation checklist)** — gitignored `briefs/research/astargrid2d-gotchas-checklist.md`

## Dead Ends

- Enabling JPS for castle-sim v0 — no weighted terrain yet, but breaks future granary-distance weights
- 8-dir diagonals without `ONLY_IF_NO_OBSTACLES` — moat/wall corner exploits
