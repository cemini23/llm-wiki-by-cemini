---
title: Vertical slice v0 — first playable milestone
type: concept
tags: [concept, milestone, godot, vertical-slice]
keywords: [vertical-slice, milestone, walls, wood, peasants, archers]
related:
  - concepts/scope-tiers.md
  - concepts/stronghold-deconstruction.md
  - concepts/agent-harness-castle-project.md
  - entities/engines/godot-4.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/agent-harness-castle-project.md — how agents implement slices
- @entities/engines/godot-4.md — target engine (Phase-0 pending)

## Raw Concept

Single sentence **magic moment** for Tier 1 before any `castle-sim` repo is mandatory.

## Narrative

### Player-visible goal

> I can draw walls on a grid, assign peasants to gather wood, and archers shoot from battlements at a approaching target.

### Acceptance criteria (playtest gate)

- [ ] Place/remove wall segments on isometric or top-down grid
- [ ] Peasants path around walls to trees; wood increments
- [ ] At least one building (woodcutter or stockpile) placeable
- [ ] Archers on walls fire at stationary or slow-moving target
- [ ] Session runs 10 minutes without crash on operator Mac
- [ ] No multiplayer, no AI lord, no siege weapons

### Out of scope for v0

Food chain, stone, popularity, enemy raids, save/load (nice-to-have later)

### Repo gate

Do **not** open `castle-sim` implementation repo until Godot Phase-0 is **CONDITIONAL-GO** or **GO** on `@entities/engines/godot-4.md`.

## Snippets

*(none)*
