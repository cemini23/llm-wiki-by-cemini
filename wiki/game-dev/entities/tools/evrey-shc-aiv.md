---
title: Evrey SHC_AIV — Crusader castle layout mod
type: entity
tags: [entity, tool, stronghold, crusader, modding, steal-from]
keywords: [aiv, evrey, crusader, skirmish, castle]
related:
  - sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - entities/tools/crusader-ai-manager.md
  - entities/tools/monsterfisch-strongholds-of-conquest.md
  - sources/monsterfisch-conquest-aiv-phase-0-audit-2026-06-20.md
  - concepts/stronghold-2-ai-lords.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @concepts/stronghold-crusader-ai-modding-shelf.md — toolchain context
- `castle-sim/data/sh2/lord_profiles.json` — behaviour JSON (separate from layout)

## Raw Concept

[Evrey/SHC_AIV](https://github.com/Evrey/SHC_AIV) — community **128-file AIV replacement** for Stronghold Crusader HD/Extreme. Skirmish + History packs; optional `firefly_fixed/` vanilla bugfixes.

**License:** none declared — **study only**; do not ship AIV files in public castle-sim.

## Narrative

### Install (retail research)

Copy `./skirmish/` or `./history/` → `.../Stronghold Crusader Extreme/aiv/` after backing up vanilla. See gitignored `briefs/research/crusader-aiv-study-loop.md`.

### castle-sim mapping

| Crusader | Godot target |
|----------|--------------|
| `.aiv` build order | `data/sh2/castle_templates/<lord>.json` (TBD) |
| 8 layouts / lord | Template rotation per skirmish seed |

### Phase-0 verdict

**STEAL-FROM (layout)** — @sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md

## Dead Ends

- Importing AIV into SH2 Kingmaker — format mismatch; manual transcribe only
