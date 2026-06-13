---
title: Stronghold deconstruction — systems inventory
type: concept
tags: [concept, stronghold, rts, castle, reference]
keywords: [stronghold, firefly, economy, siege, ai, castle-building]
related:
  - concepts/scope-tiers.md
  - concepts/vertical-slice-v0.md
  - concepts/stronghold-systems-inventory.md
  - entities/games/stronghold-series.md
  - entities/engines/godot-4.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @entities/games/stronghold-series.md — reference titles
- @concepts/scope-tiers.md — what to cut for hobby scope

## Raw Concept

Decompose Firefly **Stronghold / Crusader** into implementable subsystems for scope planning. Not a clone spec — a **checklist of complexity**.

## Narrative

### Core systems (full commercial game)

| System | Stronghold behavior | Hobby slice (Tier 1) |
|--------|---------------------|----------------------|
| **Wall building** | Draw walls, crenellations, gates | Grid/free wall segments only |
| **Economy** | Food chain, wood/stone/iron, taxes | Wood only |
| **Population** | Popularity, housing, rationing | Peasant count cap |
| **Production** | Chains (wheat→flour→bread) | One gather job |
| **Military** | Many unit types, formations | Archers only |
| **Siege** | Trebuchet, ram, ladder, tunneling | None in v0 |
| **AI lords** | Build, raid, siege player | Scripted wave timer |
| **Multiplayer** | Skirmish, co-op trails | Solo sandbox |
| **Pathfinding** | Units around dynamic walls | Required early — high risk |
| **Morale / popularity** | Happiness affects efficiency | Defer |

### Engineering risk order (build sequence)

1. Grid placement + wall collision
2. Pathfinding around placed walls
3. Resource gather + job assignment
4. Ranged combat + projectiles
5. Enemy waves
6. Everything else

## Snippets

> Stronghold feels simple in UI but bundles economy simulation, siege physics, and AI lord strategy — treat commercial depth as **aspirational**, not v0 target. [TENTATIVE — operator synthesis 2026-06-13]
