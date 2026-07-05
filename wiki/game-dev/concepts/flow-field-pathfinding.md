---
title: Flow field pathfinding — integration fields, tiles, Tier 2 adoption
type: concept
tags: [concept, pathfinding, rts, flow-field, research]
keywords: [flow-field, integration-field, emerson, dijkstra, crowd, rts]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/godot-pathfinding-patterns.md
  - entities/projects/castle-sim.md
  - sources/emerson-game-ai-pro-flow-field-tiles-2013.md
  - sources/leifnode-flow-field-pathfinding-2013.md
  - sources/vav-labs-godot-flow-fields-2026.md
  - sources/redblobgames-flow-field-pathfinding-2024.md
  - sources/exa-flowfields-firefly-batch-2026-06-13.md
  - concepts/godot-castle-sim-tool-gap-shelf.md
  - sources/godot-castle-sim-tool-gap-research-2026-06-17.md
  - sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
  - sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md
maturity: validated
created: 2026-06-13
updated: 2026-06-30
---

## Relations

- @concepts/rts-pathfinding-approaches.md — decision matrix; v0 stays on `AStarGrid2D`
- @entities/projects/castle-sim.md — Tier 2 spike candidate when unit count grows

## Raw Concept

**Flow fields** answer one inverted question: for every cell on the map, which direction moves toward the goal? Many agents read the same field — cost scales with **goals**, not **agents**.

## Narrative

### When to adopt (castle-sim tiers)

| Signal | v0 (`AStarGrid2D`) | Tier 2 flow field |
|--------|-------------------|-------------------|
| Agents sharing one goal | Few (5–20 peasants) | Many (30+ attack-move, flee crowd) |
| Distinct goals per frame | Most jobs unique | Rally point / stockpile / breach |
| Dynamic walls | `set_point_solid` cheap | Rebuild integration on `wall_changed` |
| Map size | 20×20 spike OK | Partition if > ~50×50 [Leif Node benchmarks] |

**Rule of thumb [CONFIRMED — Vav Labs 2026]:** many agents, few goals → flow field; few agents, many goals → per-agent A*. Real games hybrid both on the same grid.

### Three-field model [CONFIRMED — Leif Node / Emerson]

1. **Cost field** — per-cell traversal weight (1 = open, 2–254 = avoid, 255 = blocked). Maps to influence-map bias later.
2. **Integration field** — Dijkstra-style expansion **from goal**; stores cheapest accumulated cost to reach goal from each cell. Also powers reachability (unreachable = sentinel max).
3. **Flow field** — each cell points to lowest-cost neighbor (8-way or float vectors for smooth steering).

Rebuild trigger: goal moves **or** cost field changes (wall placed). Budget full rebuilds; localize repair when possible [@sources/vav-labs-godot-flow-fields-2026.md].

### Emerson tile hierarchy (large maps) [TENTATIVE — Game AI Pro Ch.23 summary]

For kilometer-scale RTS (Supreme Commander 2 pattern):

- Partition map into **flow-field tiles** (e.g. 10×10 cells each)
- Connect tiles with **portals** on shared edges
- **A\*** at tile graph level → path through sectors
- Compute integration+flow only for tiles on the route
- Amortize across all units sharing destination

castle-sim Tier 1 maps (20×40) likely **single field** suffices — tile hierarchy deferred until perf proves need [Leif Node: 50×50 ≈ 5ms C++ empty field].

### Relation to A* outputs [CONFIRMED — Red Blob Games 2024]

Standard graph A* already produces distance + predecessor data (`cost_so_far`, `came_from`). Flow fields are the **grid-wide** version of running Dijkstra once from the goal instead of A* per agent. Distance fields tie to roguelike Dijkstra maps and RTS influence maps.

### Godot implementation notes

- v0: built-in `AStarGrid2D` only (@concepts/godot-pathfinding-patterns.md Pattern 1)
- Tier 2: custom integration+flow on same grid as walls; see @sources/vav-labs-godot-flow-fields-2026.md for GDScript sketch
- Commercial layer: PathForge (Vav Labs) targets multi-size + influence + diagnostics — **evaluate at Tier 2**, not v0

### Dynamic walls (Stronghold-like)

Wall place/remove → mark affected cells impassable in cost field → re-run integration from active goals. Same discipline as `AStarGrid2D.set_point_solid` but **one field rebuild** serves all units heading to stockpile/siege point. Cap rebuild rate if player spam-placements.

### Dead ends for castle-sim v0

- Full-grid flow field for 5 peasants with unique tree targets = wasted work
- Continuum crowds / corridor-map papers — academic Tier 3; not v0
- GPU flow fields (Unity DOTS demos) — overkill for hobby 2D slice

## Snippets

**Operator benchmark (castle-sim spike):** gitignored `briefs/research/flow-field-benchmark-2026-06-17.md` — 20×20 grid, 50 agents, A* vs flow build/query; flow wins at shared-goal steady state.

Adoption gate (pseudocode):

```gdscript
func pick_pathfinder(agents: int, shared_goals: int) -> String:
    if agents > 30 and shared_goals <= 3:
        return "flow_field"
    return "astar_grid2d"
```

## Dead Ends

- Exa cluster `gdc-stronghold-firefly` — no Firefly GDC postmortem exists; use Bradbury interviews instead (@sources/exa-flowfields-firefly-batch-2026-06-13.md).
