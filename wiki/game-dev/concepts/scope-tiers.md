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
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/games/stronghold-series.md
  - sources/bootstrap-game-dev-wiki-2026-06-13.md
  - concepts/rts-networking-deferred.md
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-systems-inventory.md
  - sources/gdc-kingdoms-and-castles-postmortem-2019.md
  - sources/leiden-medieval-city-builder-accuracy-2020.md
  - sources/northgard-economy-case-study-2018.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/vertical-slice-v0.md — Tier 1 target spec
- @concepts/stronghold-deconstruction.md — what full Stronghold includes
- @entities/engines/godot-4.md — likely Tier 1 engine

## Raw Concept

Honest scope ladder for a solo (+ friends) Stronghold-inspired project. Prevents unbounded scope creep.

**Operator north star (2026-06-13):** personal **Stronghold 2** clone — see @concepts/operator-vision-sh2-personal-clone.md. Tiers below still apply as **time boxes**; SH2 full fidelity maps to **Tier 3+** unless fork choice simplifies (2D mechanics-only).

## Narrative

| Tier | Timeline (part-time) | Deliverable | Difficulty |
|------|----------------------|-------------|------------|
| **1 — Toy castle** | Weeks–few months | Grid walls, 3–5 buildings, one resource, peasants, sandbox only | Moderate |
| **2 — Mini Stronghold** | 6–18 months | Food+wood+stone economy, wave raids, one siege weapon, hot-seat | Hard |
| **3 — Stronghold feel** | Years (studio-scale) | AI lords, full siege roster, skirmish, real-time online MP | Very hard solo |
| **3b — SH2 personal clone** | Years part-time | Popularity + honour + crime + Kingmaker + estates + SH2 siege rules | Operator goal — see @concepts/stronghold-2-systems-inventory.md |

**Project default:** complete **Tier 1 spine** on current repo, then climb SH2 phases in `briefs/GDD-sh2-personal-clone.md` — do not skip economy before honour.

### Explicit cuts (until Phase 2 GO)

- No smart AI lords
- No campaign / historical missions
- No real-time internet multiplayer
- **Fork B (Godot 3D)** active for SH2 clone — 2D path closed (operator 2026-06-13)
- No runtime LLM NPC dialogue (@concepts/llm-npc-runtime-ai-shelf.md)
- No runtime agentic map generation (@concepts/agentic-pcg-level-design.md)

## Snippets

> Industry pattern: RTS combat systems are among the hardest game-dev engineering problems — start with placement + economy before combat at scale. [TENTATIVE — general gamedev consensus]
