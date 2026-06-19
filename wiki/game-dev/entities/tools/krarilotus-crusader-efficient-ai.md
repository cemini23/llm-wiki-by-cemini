---
title: Krarilotus Crusader efficient AI — AIV + aggressive AIC
type: entity
tags: [entity, tool, stronghold, crusader, modding, steal-from]
keywords: [krarilotus, aic, aiv, crusader, aggressive]
related:
  - sources/krarilotus-efficient-ai-phase-0-audit-2026-06-19.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @entities/tools/evrey-shc-aiv.md — layout partner pack
- @entities/tools/unofficial-crusader-patch2.md — AIC injection host

## Raw Concept

[Krarilotus/Stronghold-Crusader-efficient-AI](https://github.com/Krarilotus/Stronghold-Crusader-efficient-AI) — WIP **efficient AIV** set (8 castles/lord, equal build steps) + **aggressive AIC** tuned for 2k start gold.

**License:** none declared — reference only.

## Narrative

### Status (2026-06-19)

Stage 1 prototyping — **Rat** complete; Snake/Pig/Frederick/Emir/Marshal/Wazir near done; others in design.

### castle-sim mapping

| Extract | Target |
|---------|--------|
| First-attack timing under pressure | `lord_profiles.json` harass/siege timing |
| Aggressive AIC deltas | Director weights vs retail SH2 lords |

### Phase-0 verdict

**STEAL-FROM (WIP)** — @sources/krarilotus-efficient-ai-phase-0-audit-2026-06-19.md

## Dead Ends

- Replacing Evrey AIV entirely before Krarilotus Stage 2 completes
