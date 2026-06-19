---
title: Stronghold Crusader modding ecosystem — research shelf
type: concept
tags: [concept, stronghold, modding, aiv, reference]
keywords: [stronghold, crusader, ucp, aiv, modding, openshc]
related:
  - entities/games/stronghold-series.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - concepts/stronghold-systems-inventory.md
  - concepts/rts-siege-ai-reference.md
  - sources/tool-evaluation-cross-wiki-routing-2026-06-13.md
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - sources/github-stronghold-2-scan-2026-06-13.md
  - sources/unofficial-crusader-patch2-phase-0-audit-2026-06-13.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @entities/tools/unofficial-crusader-patch2.md — **only MIT-licensed mod stack** in 2026-06 batch
- @concepts/rts-siege-ai-reference.md — Tier 2+ siege AI (greenfield design)

## Raw Concept

Community reverse-engineering and modding repos for **Stronghold Crusader** — catalogued in 56-target tool eval. Most are **reject** on license; one **steal-from** for design archaeology.

**Stronghold 2** has a separate, much smaller GitHub footprint → @concepts/stronghold-2-github-ecosystem-shelf.md (MP-AI MIT patch, AnalyseHub, unlicensed S2M/trainers).

## Narrative

### Verified adoptable reference

| Repo | License | Value for castle-sim |
|------|---------|---------------------|
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | MIT | AIV injection, balance fixes, pathfinding patches — study reimplementation patterns |

### GPL reference-only (no code merge)

| Repo | License | Notes |
|------|---------|-------|
| [OpenSHC](https://github.com/sourcehold/OpenSHC) | GPL-3.0 | DLL-hook reimplementation of Crusader engine — illuminates legacy loop; **reference read only** |

### High analytic value, rejected (unlicensed)

These inform **design intent** but must not be copied into castle-sim assets or configs:

- **AIV / AIC files** — Xander10alpha, FAPLZ, Krarilotus efficient-AI, Evrey SHC_AIV (archived)
- **Castle layouts** — StrongholdsOfConquest_, community AIV efficiency studies
- **Data extraction** — CrusaderData (balancing tables — proprietary Firefly IP risk)
- **Tools** — gtk-crusader-village (AIV editor), TexEditor (.tex strings), map editor toolsets
- **Memory utilities** — trainers, live stat readers, mouse-clicker (superseded by licensed Airtest patterns for automation)

### Explicit license trap

**StrongMod** README states no license — treat as **forbidden** even for laptop-side study.

### Design takeaway for castle-sim

Community modders solved **AI village layouts (AIV)**, **economic weight tuning**, and **engine path bugs** outside Firefly source. For greenfield Godot:

1. Reimplement AIV as **data-driven castle templates** + behavior weights (JSON in repo)
2. Do **not** import binary AIV files from unlicensed repos
3. Use UCP2 issue threads (e.g. Nomad AI) as **behavior spec inspiration**, not code

## Snippets

License gate for any Stronghold community asset:

```
[ ] SPDX license on repo (MIT/Apache/CC0 preferred)
[ ] No ripped Firefly binaries in tree
[ ] If GPL — reference-only, no derivative merge into castle-sim
```
