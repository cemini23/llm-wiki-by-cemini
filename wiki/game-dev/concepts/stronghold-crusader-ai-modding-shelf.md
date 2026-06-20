---
title: Stronghold Crusader — AI & modding toolchain shelf
type: concept
tags: [concept, stronghold, crusader, modding, ai, reference]
keywords: [ucp, aiv, aic, skirmish, github, krarilotus, evrey]
related:
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - entities/tools/crusader-ai-manager.md
  - entities/tools/monsterfisch-strongholds-of-conquest.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - entities/projects/castle-sim.md
  - sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md
  - sources/krarilotus-efficient-ai-phase-0-audit-2026-06-19.md
  - sources/crusader-ai-manager-phase-0-audit-2026-06-20.md
  - sources/monsterfisch-conquest-aiv-phase-0-audit-2026-06-20.md
  - concepts/rts-siege-ai-reference.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
maturity: validated
created: 2026-06-18
updated: 2026-06-20
---

## Relations

- @entities/tools/unofficial-crusader-patch2.md — MIT Phase-0 GO
- @entities/tools/evrey-shc-aiv.md — STEAL-FROM AIV layouts (Phase-0 2026-06-19)
- @entities/tools/krarilotus-crusader-efficient-ai.md — STEAL-FROM aggressive AIC + WIP AIV (Phase-0 2026-06-19)
- @entities/tools/crusader-ai-manager.md — STEAL-FROM 16-slot lord swap UX (Phase-0 2026-06-20, MIT)
- @entities/tools/monsterfisch-strongholds-of-conquest.md — STEAL-FROM historical AIV + AIC bundle (Phase-0 2026-06-20)
- @concepts/game-ai-rl-augmentation-shelf.md — EA DRL augmentation pattern for Phase E+ lord AI
- @concepts/stronghold-2-ai-lords.md — SH2 lord tables to transcribe into JSON
- Gitignored brief: `briefs/research/crusader-aiv-study-loop.md`

## Raw Concept

Curated **Crusader skirmish AI ecosystem** — the franchise's best modding surface. Use to inform **castle-sim LordAIDirector** and optional AIV-style castle templates; do not runtime-depend on Crusader binaries.

## Narrative

### Why Crusader for AI study (not SH2)

| | Crusader | SH2 |
|--|----------|-----|
| Castle files | External **`.aiv`** per lord (8 each) | Hard-coded AI castles + `.s2m` maps |
| Behaviour | **`.aic`** moddable via UCP | `gameRules.dat` + closed editor |
| Community | Evrey, Krarilotus, Monsterfisch, DE AIVE | Nation lord editor, MP-AI patches |
| Binks / taunts | Video per lord | Absent |

SH2 clone target: **JSON lord profiles + template castles** mirroring Crusader separation of **layout (AIV)** vs **behaviour (AIC)**.

### Toolchain stack

```
UCP2 (MIT) → AIC behaviour edits + bugfixes
     ↓
AIV files / AIVE (.aivjson DE) → castle build order + layout
     ↓
CrusaderAIManager → swap lords without replacing all 16 slots
     ↓
castle-sim: lord_profiles.json + castle_templates/*.json
```

### Repos to study [CONFIRMED — pass2 scan]

| Repo | Focus |
|------|-------|
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | AI Swapper, ByBurton AIC editor integration |
| @entities/tools/evrey-shc-aiv.md | Full skirmish AIV replacement set — **STEAL-FROM** |
| @entities/tools/krarilotus-crusader-efficient-ai.md | Per-lord prototype castles + aggressive AIC — **STEAL-FROM (WIP)** |
| @entities/tools/monsterfisch-strongholds-of-conquest.md | Historical ↔ AIV + aggressive AIC bundle — **STEAL-FROM** |
| @entities/tools/crusader-ai-manager.md | Load custom lord into base mod — **STEAL-FROM (MIT)** |
| [gynt/stronghold-mapeditortools](https://github.com/gynt/stronghold-mapeditortools) | SH1/Crusader map editor utilities |

### Behaviour patterns to transcribe

From @concepts/stronghold-2-kingmaker-strategy.md + Crusader Fandom AI mechanics:

| Phase | Crusader AI | SH2 AI | Director stub |
|-------|-------------|--------|---------------|
| Natural | Build, harass, repair moat | Raid groups, estate capture | `harass_interval`, `estate_target_weight` |
| Siege | Army to weakest neighbor | Siege camp + trebuchet | `siege_build_threshold` |
| Defence | Ranged on walls, oil | Troop pools replace fallen | `wall_garrison_ratio` |

### Crusader DE caveat [TENTATIVE]

Community reports **DE vanilla skirmish AI** passive vs **UCP**-enhanced HD — if operator ever installs Crusader DE for research, budget UCP + custom AIV for meaningful skirmish.

### castle-sim mapping

| Crusader artifact | Godot target |
|-------------------|--------------|
| `.aic` personality | `lord_profiles.json` behaviour block |
| `.aiv` castle | `data/sh2/castle_templates/<lord>.json` (TBD) |
| Lord binks | Advisor panel strings + portrait (Phase D) |
| Skirmish lobby | Kingmaker lobby extensions (story-032 later) |

## Dead Ends

- Shipping UCP2 or AIV files in public repo — MIT study only
- Expecting SH2 `gameRules.dat` ≡ Crusader `.aic` — different schemas; Nation editor for SH2 only
