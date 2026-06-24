---
title: Vertical slice v0 — first playable milestone
type: concept
tags: [concept, milestone, godot, vertical-slice]
keywords: [vertical-slice, milestone, walls, wood, peasants, archers]
related:
  - concepts/scope-tiers.md
  - concepts/stronghold-deconstruction.md
  - concepts/stronghold-systems-inventory.md
  - concepts/agent-harness-castle-project.md
  - concepts/art-pipeline-v0-requirements.md
  - entities/engines/godot-4.md
  - entities/projects/castle-sim.md
  - sources/stronghold-hd-manual-2001.md
  - concepts/ccgs-workflow-extraction.md
  - concepts/godot-stagehand-ci-smoke-plan.md
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/rts-siege-ai-reference.md
  - entities/games/stronghold-series.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
  - sources/gdc-kingdoms-and-castles-postmortem-2019.md
  - sources/godot-4-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/agent-harness-castle-project.md — how agents implement slices
- @entities/engines/godot-4.md — **CONDITIONAL-GO**
- @entities/projects/castle-sim.md — implementation repo (scaffolded)
- @concepts/stronghold-systems-inventory.md — full SH1 reference; v0 is ~5% building count

## Raw Concept

Single sentence **magic moment** for Tier 1 before any `castle-sim` repo is mandatory.

## Narrative

### Player-visible goal

> I can draw walls on a grid, assign peasants to gather wood, and archers shoot from battlements at an approaching target.

Maps to Stronghold (2001) subsets: **§8 walls**, **woodcutters + stockpile**, **archers on fortifications** — no granary popularity sim yet (@concepts/stronghold-systems-inventory.md).

### Acceptance criteria (playtest gate)

**Milestone 0 — pathfinding spike** (before feature polish):

- [ ] 20×20 grid; place/remove wall cells
- [ ] 5 peasants path around walls to trees; no stuck units
- [ ] 60 fps × 10 minutes on operator Mac

**Milestone 1 — vertical slice v0**:

- [ ] Place/remove wall segments on isometric or top-down grid (Stronghold-style draw, grid-backed)
- [ ] Peasants path around walls to trees; wood increments at stockpile
- [ ] At least one building (woodcutter hut or stockpile) placeable
- [ ] Archers on walls fire at stationary or slow-moving target
- [ ] Session runs 10 minutes without crash on operator Mac
- [ ] No multiplayer, no AI lord, no siege weapons, no popularity/tax UI

### Explicit SH1 cuts for v0

| SH1 system | v0 |
|------------|-----|
| Granary + 4 food types | — |
| Popularity / tax | — |
| Stone, iron, pitch | — |
| Barracks full roster | archers only |
| Siege camp | — |
| Lord death lose condition | optional stub |

### Out of scope for v0

Food chain, stone, popularity, enemy raids, save/load (nice-to-have later). See @concepts/scope-tiers.md Tier 1.

### Repo gate

Godot Phase-0 **CONDITIONAL-GO** (2026-06-13). **`castle-sim` scaffolded** at `/Users/claudiobarone/Projects/castle-sim/`. Open as separate Cursor workspace for code.

### Tier 1 rendering (2026-06-13)

**Accepted exception:** top-down colored grid + placeholder rects for Tier 1 close-out (`castle-sim` D-014). Isometric `TileMapLayer` deferred to W3 art pass (`art-pipeline-v0-requirements.md`). Does not block M1 v0 **PROCEED** or story-003 gate.

## Snippets

Playtest script:

1. Place L-shaped wall around keep area
2. Assign 3 peasants to nearest trees
3. Place archer on wall segment
4. Spawn target dummy; confirm projectile hit
5. Remove wall mid-session; confirm peasants reroute
