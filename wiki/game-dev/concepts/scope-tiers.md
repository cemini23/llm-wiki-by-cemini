---
title: Scope tiers — hobby castle sim realism
type: concept
tags: [concept, scope, stronghold, planning]
keywords: [scope, tiers, vertical-slice, solo-dev, stronghold, rts]
related:
  - concepts/game-dev-wiki-scope.md
  - concepts/stronghold-deconstruction.md
  - concepts/vertical-slice-v0.md
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/rts-pathfinding-approaches.md
  - concepts/medieval-sim-fun-vs-accuracy.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/agentic-pcg-level-design.md
  - entities/engines/godot-4.md
  - entities/games/stronghold-series.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/vertical-slice-v0.md — Tier 1 target spec
- @concepts/stronghold-deconstruction.md — what full Stronghold includes
- @entities/engines/godot-4.md — likely Tier 1 engine

## Raw Concept

Honest scope ladder for a solo (+ friends) Stronghold-inspired project. Prevents "clone Crusader" scope creep.

## Narrative

| Tier | Timeline (part-time) | Deliverable | Difficulty |
|------|----------------------|-------------|------------|
| **1 — Toy castle** | Weeks–few months | Grid walls, 3–5 buildings, one resource, peasants, sandbox only | Moderate |
| **2 — Mini Stronghold** | 6–18 months | Food+wood+stone economy, wave raids, one siege weapon, hot-seat | Hard |
| **3 — Stronghold feel** | Years (studio-scale) | AI lords, full siege roster, skirmish, real-time online MP | Very hard solo |

**Project default:** aim for **Tier 1 complete** before any Tier 2 commitment. Tier 3 is explicitly **out of scope** unless team grows.

### Explicit cuts (until Tier 2 GO)

- No smart AI lords
- No campaign / historical missions
- No real-time internet multiplayer
- No 3D Stronghold 2-style engine (prefer 2D isometric)
- No runtime LLM NPC dialogue (@concepts/llm-npc-runtime-ai-shelf.md)
- No runtime agentic map generation (@concepts/agentic-pcg-level-design.md)

## Snippets

> Industry pattern: RTS combat systems are among the hardest game-dev engineering problems — start with placement + economy before combat at scale. [TENTATIVE — general gamedev consensus]
