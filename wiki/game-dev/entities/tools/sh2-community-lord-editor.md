---
title: SH2 Community Lord Editor — gameRules.dat AI tool
type: entity
tags: [entity, tool, stronghold-2, modding, ai]
keywords: [lord-editor, asophix, gamerules, ai, stronghold-nation]
related:
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - entities/projects/castle-sim.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - entities/tools/stronghold2-mp-ai-patch.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @concepts/stronghold-2-ai-lords.md — retail lord behaviour canon
- `castle-sim/data/sh2/lord_profiles.json` — greenfield reimplementation target

## Raw Concept

**Stronghold 2 Community Lord Editor v1.1** by Asophix — Windows GUI to view/edit **AI lord behaviour** in Stronghold 2 via **`gameRules.dat`**. Hosted on [Stronghold Nation SH2 miscellaneous](https://www.stronghold-nation.com/downloads/category/stronghold-2/miscellaneous/) (Aug 2025). Adapted from Stronghold Legends Community Lord Editor.

## Narrative

### Capabilities [CONFIRMED — Stronghold Nation forums]

- Edit per-lord **harass** and **siege** unit mixes
- Adjust **castle** / defence weights (companion **AI Castle Editor** lineage from Stronghold-Knights)
- Community **lord packs** (e.g. Radu, campaign villains) replace skirmish slots
- Writes retail dat files — **no source code** published

### Value for castle-sim

| Use | Action |
|-----|--------|
| Validate `@concepts/stronghold-2-ai-lords.md` tables | Cross-check harass/siege counts against editor exports |
| Rapid AI experiments on retail | Operator tweaks dat → transcribe deltas into `lord_profiles.json` |
| Schema discovery | Field names in editor UI → JSON keys for `LordProfile` loader |

### castle-sim boundary

- **Do not** ship `gameRules.dat` or editor in public repo
- **Do not** depend on editor at runtime — JSON is source of truth in Godot
- OK in gitignored briefs: install path + export workflow notes

### Phase-0 verdict

**STEAL-FROM (design)** — best available **structured AI lord UI** for SH2; informs Phase D–E director weights.

## Dead Ends

- Expecting MIT source — closed Windows binary only
- Importing binary dat into castle-sim — reimplement as JSON
