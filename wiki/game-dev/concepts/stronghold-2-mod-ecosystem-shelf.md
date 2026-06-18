---
title: Stronghold 2 — mod ecosystem shelf (QoL + integration map)
type: concept
tags: [concept, stronghold-2, modding, qol, reference]
keywords: [mods, moddb, nexus, mp-ai, lord-editor, matteele, integration, visual]
related:
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - sources/sh2-nevikov-new-balance-sheet-2026-06-18.md
  - concepts/stronghold-2-visual-qol-presets.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/operator-vision-sh2-personal-clone.md
  - entities/projects/castle-sim.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - entities/tools/sh2-mp-ai-enabler.md
  - entities/tools/sh2-community-lord-editor.md
  - sources/sh2-mp-ai-enabler-phase-0-audit-2026-06-18.md
  - sources/sh2-community-lord-editor-phase-0-audit-2026-06-18.md
  - entities/tools/stronghold2-analyse-hub.md
  - concepts/stronghold-2-visual-qol-presets.md
  - concepts/art-pipeline-v0-requirements.md
  - sources/github-stronghold-2-scan-2026-06-13.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @concepts/stronghold-modding-ecosystem-shelf.md — **Crusader** UCP2 / AIV stack (much larger)
- @concepts/stronghold-2-github-ecosystem-shelf.md — code-focused GitHub scan
- @concepts/stronghold-2-visual-qol-presets.md — **visual comfort** preset catalog
- @sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md — raw ModDB/Nexus/YouTube pass
- @sources/sh2-nevikov-new-balance-sheet-2026-06-18.md — Nevikov New Balance CSV ingest

## Raw Concept

Catalog of **Stronghold 2 (Steam Edition)** community mods and tools. **QoL includes visuals** — sharper textures, ENB, and biome packs improve long-session play. Rank by popularity; map features into `castle-sim` as **native presets** (no unlicensed asset import).

## Narrative

### Tier summary (revised 2026-06-18)

| Tier | What | castle-sim action |
|------|------|-------------------|
| **A — Mechanics QoL** | MP AI, lord editor, spear fix, debug overlay, sim speed | First-class sim features |
| **A′ — Visual / comfort QoL** | HD Reworked, ENB, Matteele, Winter, Pixel | `graphics_presets.json` + Godot post-FX |
| **B — Balance tuning** | Nevikov NB sheet, spear fix dat | `balance_presets.json` |
| **C — Official baseline** | Steam Edition widescreen / workshop | Match in UX |
| **D — Content** | Maps, campaigns, lord packs | Fixtures / deferred `.s2m` |

There is **no SH2 UCP2** — balance is per-mod or crossover-sheet only.

---

### Tier A — Mechanics QoL

#### 1. Multiplayer / skirmish AI slots

- [sh2_mp_ai_enabler](https://gitlab.com/Daerandin/sh2_mp_ai_enabler) + [Jpnock MIT](https://github.com/Jpnock/Stronghold2-MP-AI)
- **→** Native co-op vs AI Kingmaker (Phase E)

#### 2. Community Lord Editor → `lord_profiles.json`

- [Asophix SH2 Lord Editor](https://www.stronghold-nation.com/downloads/category/stronghold-2/miscellaneous/)
- **→** JSON lord schema + hot reload

#### 3. King/Hawk/Bull spear fix

- Nation `gamerules.dat` patch (Sir Windows, 2026-05)
- **→** `balance_presets.json` → `community_spear_fix`

#### 4. Debug overlay

- MIT AnalyseHub
- **→** Godot debug panel

#### 5. Sim speed slider [GAP on SH2]

- **→** 0.5×–4× architect-mode speed in clone

---

### Tier A′ — Visual / comfort QoL [integrate]

Most **Nexus downloads** and **ModDB 2025 activity** are visual — treat as equal-priority comfort.

| Mod | Popularity | Comfort benefit | Preset ID |
|-----|------------|-----------------|-----------|
| [HD Reworked 5.0](https://www.nexusmods.com/stronghold2/mods/5) | Nexus #1 | Sharper models/textures | `enhanced_hd` |
| AI enhanced / Enhanced Graphics | Nexus #2–3 | Less blur, cleaner UI | `enhanced_hd` |
| ENB / [SH2 Lighting](https://www.nexusmods.com/stronghold2/mods/6) | Nexus #4; 850K DL ModDB | Contrast, bloom, AO | `cinematic_enb` |
| [Matteele Crusader Edition](https://www.moddb.com/mods/stronghold-2-crusader-matteele-edition) | ModDB flagship 2025 | Desert biome + audio refresh | `matteele_desert_crusader` |
| Winter / Christmas mods | ModDB seasonal | Snow biome + mood | `winter_seasonal` |
| Pixel mod (Matteele) | YouTube | Retro readability | `pixel_retro` |

**Implementation:** @concepts/stronghold-2-visual-qol-presets.md + `castle-sim/data/sh2/graphics_presets.json`.

**Operator retail:** HD/ENB/Matteele optional for long playtest sessions; not required for mechanics notes.

---

### Tier B — Balance presets

| Source | Game | Preset |
|--------|------|--------|
| Retail SH2 Heaven stats | SH2 | `retail_sh2` (default) |
| Spear fix dat | SH2 | `community_spear_fix` |
| [Nevikov New Balance sheet](https://docs.google.com/spreadsheets/d/1pZ-6cPoc9YkytVDPWSZurC6wXaqi052vm0KVXJdN2GU) | **Crusader 1.14 crossover** | `nevikov_new_balance_inspired` |

**Matteele SH2 mod** has no published stat table — visual-sound TC only.

Sheet deltas scraped → @sources/sh2-nevikov-new-balance-sheet-2026-06-18.md.

---

### Tier C — Official Steam Edition baseline

Widescreen, Workshop, Steamworks MP, partial art refresh → ultrawide + scalable UI in M0.3D+.

---

### Tier D — Content & tools

Official AI Editor, atmospheric castles, Workshop maps, Eren121 S2M RE — fixtures only.

---

### Operator retail stack

```
Stronghold 2 Steam Edition
  Mechanics: sh2_mp_ai_enabler (host) + optional Lord Editor + AnalyseHub
  Visual (pick one): HD Reworked OR ENB OR Matteele desert TC OR Winter
  → wiki JSON specs + castle-sim presets
```

---

### castle-sim QoL backlog

| Feature | Source | Data file | Phase |
|---------|--------|-----------|-------|
| Co-op vs AI | MP AI enabler | — | E |
| Lord JSON + hot reload | Lord Editor | `lord_profiles.json` | D–E |
| Spear-fix lords | Nation patch | `balance_presets.json` | D |
| Nevikov-inspired tuning | NB sheet | `balance_presets.json` | Post-combat model |
| Graphics preset menu | Nexus/ModDB visual mods | `graphics_presets.json` | C |
| Sim speed | SH2 gap | settings | B+ |
| Debug overlay | AnalyseHub | debug UI | B |
| Desert / winter biomes | Matteele / Winter | art pipeline | C+ |

## Snippets

Mod install trap (Steam + visual mods):

```
Never overlay mod fx/ without restoring vanilla fx first
```

## Dead Ends

- Waiting for SH2 community balance patch — use presets instead
- Importing Nexus 2.4 GB AI texture pack into public repo
- Confusing Nevikov NB sheet with Matteele SH2 mod balance
