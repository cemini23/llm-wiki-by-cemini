---
title: Monsterfisch Strongholds of Conquest — historical AIV pack
type: entity
tags: [entity, tool, stronghold, crusader, modding, steal-from]
keywords: [monsterfisch, conquest, aiv, historical, ucp]
related:
  - sources/monsterfisch-conquest-aiv-phase-0-audit-2026-06-20.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - entities/tools/crusader-ai-manager.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/tools/evrey-shc-aiv.md — parallel full-roster AIV set
- @entities/tools/krarilotus-crusader-efficient-ai.md — aggressive AIC pairing

## Raw Concept

[Monsterfisch/StrongholdsOfConquest_](https://github.com/Monsterfisch/StrongholdsOfConquest_) — **16 historical Crusader castles** as `.aiv` replacements + bundled **aggressive AIC** (UCP-dependent).

**License:** none declared — **study layouts only**; README reserves all rights.

## Narrative

### Content

- Per-lord historical castle layouts (screenshots + build order)
- Optional visual edit zip for presentation
- Requires @entities/tools/unofficial-crusader-patch2.md

### castle-sim mapping

| Crusader | Godot target |
|----------|--------------|
| Historical choke layouts | `castle_templates/<lord>.json` density reference |
| UCP aggressive AIC | `lord_profiles.json` harass/siege weights |

### Phase-0 verdict

**STEAL-FROM (design)** — @sources/monsterfisch-conquest-aiv-phase-0-audit-2026-06-20.md

## Dead Ends

- Redistributing `.aiv` binaries in public castle-sim repo
