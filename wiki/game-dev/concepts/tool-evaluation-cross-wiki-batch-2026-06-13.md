---
title: Tool evaluation cross-wiki batch — June 2026 (56 targets)
type: concept
tags: [concept, tools, routing, phase-0, audit]
keywords: [tool-evaluation, steal-from, reject, defer, license]
related:
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/deferred-engine-candidates.md
  - meta/cross-wiki-routing.md
  - entities/tools/serpent-ai.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/gamedev-resources.md
  - entities/tools/airtest.md
  - sources/airtest-phase-0-audit-2026-06-13.md
  - sources/serpent-ai-phase-0-audit-2026-06-13.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @sources/tool-evaluation-cross-wiki-routing-2026-06-13.md — raw ingest
- @meta/cross-wiki-routing.md — routing rules

## Raw Concept

Structured Phase-0 + cross-wiki routing pass over **56 GitHub targets** from operator docx (2026-06-13). Canonical verdict shelf for game-dev-wiki adoption posture.

## Narrative

### Actionable for castle-sim / W2 now

| Tool | Tier | Posture | Page |
|------|------|---------|------|
| Claude-Code-Game-Studios | Steal-from | Patterns only (existing audit) | @entities/tools/claude-code-game-studios.md |
| SerpentAI | Steal-from | Visual parsing architecture (dormant repo) | @entities/tools/serpent-ai.md |
| UnofficialCrusaderPatch2 | Steal-from | AIV / balance / pathfix study | @entities/tools/unofficial-crusader-patch2.md |
| GameDev-Resources | Reference-only | Asset link index | @entities/tools/gamedev-resources.md |
| Airtest | Adopt | UI automation — **@ccc-wiki owns install** | @entities/tools/airtest.md |

### Unity shelf (steal patterns when Unity Phase-0 runs)

| Tool | Tier | Extract |
|------|------|---------|
| GameFramework | Steal-from | Event bus, object pool, resource provider |
| GameDevelopmentKit | Steal-from | UniTask async loop patterns |
| Path-Creator | Steal-from | Spline/curve math [CONFIRMED MIT post-ingest] |

### Deferred engines

@concepts/deferred-engine-candidates.md — libGDX (Java), Duality (C# 2D).

### Stronghold modding cluster

@concepts/stronghold-modding-ecosystem-shelf.md — 20 Crusader repos; 19 rejected on license; OpenSHC GPL-3.0 reference-only.

### Full target table

| # | Name | Tier | Primary fit | License (docx) | Notes |
|---|------|------|-------------|----------------|-------|
| 1 | SerpentAI | Steal-from | game-dev | MIT | Visual game automation |
| 2 | AITradeGame | Reference | OSINT | MIT | LLM trading sim — not game-dev |
| 3 | CCGS | Steal-from | game-dev | MIT | Existing entity |
| 4 | AI-Aimbot | Reject | cybersec | GPL-3.0† | No game-dev adoption |
| 5 | Airtest | Adopt | CCC | Apache-2.0 | Image-based UI test |
| 6 | AIGoodGames | Reject | — | none | Prompt simulators |
| 7 | GameDevelopmentToolset | Reject | — | proprietary | Houdini-only |
| 8 | libgdx | Defer | game-dev | Apache-2.0 | Java engine |
| 9 | GameFramework | Steal-from | game-dev | MIT | Unity modules |
| 10 | GameDev-Resources | Reference | game-dev | CC0 | Asset lists |
| 11 | SFML-Game-Development-Book | Reject | game-dev | non-commercial | NC clause |
| 12 | GameDevelopmentKit | Steal-from | game-dev | MIT | Unity + UniTask |
| 13–14 | anything_about_game, magictools | Reject | game-dev | none | Unlicensed lists |
| 15 | Hilo | UNAVAILABLE | — | — | |
| 16 | GameDevelopmentLinks | Reject | game-dev | none | MonoGame links |
| 17 | duality | Defer | game-dev | MIT | 2D C# engine |
| 18 | SpriteBuilder | UNAVAILABLE | — | — | |
| 19 | jmonkeyengine | Reject | game-dev | none† | Out of Phase-0 scope |
| 20 | Path-Creator | Steal-from† | game-dev | MIT† | Unity splines |
| 21–22 | UnityGameFramework, gamedevguide | Reject | game-dev | none | Unreal/duplicate |
| 23 | GameZone | UNAVAILABLE | — | — | |
| 24–28 | awesome-learn-gamedev … Packt UE | Reject | game-dev | none/proprietary | Lists / book code |
| 29–36 | GameEngineBook … Android-NDK | UNAVAILABLE | — | — | |
| 33 | Packt Godot 4 book | Reject | game-dev | proprietary | Publisher encumbered |
| 37 | UnofficialCrusaderPatch2 | Steal-from | game-dev | MIT | Active SHC patch |
| 38–54 | SHC_AIV … AICs-Xander10alpha | Reject | game-dev | none | Unlicensed mod data |
| 40 | OpenSHC | Reject† | game-dev | GPL-3.0† | Reference-only archaeology |
| 55 | StrongMod | Reject | game-dev | explicit none | README denies license |
| 56 | Stronghold-Crusader (SUT) | Reject | game-dev | none | Student clone |

† = corrected via `gh api` after docx ingest.

### Reject reasons (pattern)

1. **NO LICENSE FOUND** — default reject on IP-sale surfaces (35 targets)
2. **Scope mismatch** — Unreal, HTML5 mobile, RPG char gen, Houdini
3. **Proprietary / NC** — Packt repos, SFML book, SideFX toolset
4. **Superseded** — UCP v1 vs UCP2; unlicensed AIV dumps vs MIT patch project

## Dead Ends

- Bulk ingest of Stronghold AIV/map binaries without license — legal dead end; design from @concepts/stronghold-systems-inventory.md instead
- Full SerpentAI install — Python 3.8, dormant since 2020; steal architecture only
