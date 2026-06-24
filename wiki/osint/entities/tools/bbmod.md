---
title: BBMOD — 3D graphics library for GameMaker
type: entity
tags: [entity, tool, game-dev, game-maker, 3d, k128]
keywords: [BBMOD, blueburncz, GameMaker, MIT, Assimp, PBR, 3d-rendering]
related:
  - sources/tool-eval-metaplan-81url-2026-06-24.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/active-project-research-routing.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sources/tool-eval-metaplan-81url-2026-06-24.md — K128 Adopt row
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry

## Raw Concept

Phase-0 prompted by K128 **Tool Evaluation Analysis Metaplan.docx** URL 51 — `blueburncz/BBMOD`.

## Narrative

**BBMOD** is an MIT-licensed **3D rendering library for GameMaker** (Assimp models, skinning, shadows, PBR). Active maintenance (118★, pushed 2026-05-30).

**Phase-0 (2026-06-24):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api` + LICENSE file in clone) |
| Hardcoded wiki layout | N/A — engine library, not wiki tool |
| Maturity | 118★, 4 open issues, recent commits |
| castle-sim fit | **NO-GO** — castle-sim is **Godot**, not GameMaker |
| game-dev-wiki fit | **Adopt** — 3D asset pipeline reference for hobby game-dev wiki |

**Posture:** **Adopt** for @game-dev-wiki only. Steal rendering patterns (PBR, shadow cascades) as **design reference** for Godot porting — do not vendor BBMOD into castle-sim repo.

## Snippets

> "BBMOD is a library that makes creating 3D games in GameMaker easier!" [Source: https://github.com/blueburncz/BBMOD README (retrieved 2026-06-24)]

## Dead Ends

- GameMaker runtime dependency blocks direct castle-sim integration.
