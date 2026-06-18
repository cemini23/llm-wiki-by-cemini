---
title: SH2 mod ecosystem scan — ModDB, Nexus, YouTube, GitHub (2026-06-18)
type: source
tags: [source, stronghold-2, modding, youtube, moddb, nexus]
keywords: [mods, qol, mp-ai, lord-editor, matteele, nexus, moddb]
related:
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - sources/github-stronghold-2-scan-2026-06-13.md
  - entities/tools/stronghold2-mp-ai-patch.md
  - entities/tools/sh2-mp-ai-enabler.md
  - entities/tools/sh2-community-lord-editor.md
  - sources/sh2-mp-ai-enabler-phase-0-audit-2026-06-18.md
  - sources/sh2-community-lord-editor-phase-0-audit-2026-06-18.md
  - entities/tools/stronghold2-analyse-hub.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/sh2-nevikov-new-balance-sheet-2026-06-18.md
  - concepts/stronghold-2-visual-qol-presets.md
  - entities/projects/castle-sim.md
read_status: read
source_type: web-scan
source_url: https://www.moddb.com/games/stronghold-2/mods
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Operator-requested pass: **popular Stronghold 2 mods** across ModDB, Nexus Mods, YouTube, Stronghold Nation, and GitHub/GitLab. Focus: **quality-of-life** and **mechanics** worth **integrating into castle-sim** (greenfield), not asset rips.

Method: Brave web + video search; GitHub `Stronghold2` star sort; Nexus top-all-time; ModDB downloads page; Stronghold Nation SH2 miscellaneous category; cross-check prior @sources/github-stronghold-2-scan-2026-06-13.md.

## Narrative

### Landscape [CONFIRMED — 2026-06-18]

SH2 modding is **small vs Crusader** — no community balance patch (no “SH2 UCP2”). Mods split into:

1. **Visual reskins / ENB** (majority of downloads)
2. **Total conversions** (Matteele Crusader Edition — active 2025)
3. **Memory/runtime patches** (MP AI enabler — highest gameplay QoL)
4. **Data editors** (Lord Editor, Official AI Editor — `gameRules.dat`)
5. **Micro-fixes** (spear/armoury bug for King/Hawk/Bull)

Steam Edition (2017) already ships **widescreen**, **Workshop** hook, exclusive maps — baseline QoL Firefly never backported to disk editions.

### ModDB — most active downloads (2024–2025)

| Mod | Type | Notes |
|-----|------|-------|
| [Stronghold 2 Crusader Matteele Edition](https://www.moddb.com/mods/stronghold-2-crusader-matteele-edition) | Total conversion | Desert/Crusader reskin + reworked Peace/War campaigns + custom map campaign; assets from SHC2; **final v May 2025** |
| Winter mod / Christmas variant | Visual | Seasonal terrain + UI |
| [SH2 Lighting](https://www.moddb.com/games/stronghold-2/downloads/sh2-lighting) | ENB | Ambient occlusion, color; ~850K DL on Gamepressure mirror |
| Gigachad HD Textures | Texture pack | Large-address-aware note in comments |
| Imperium Condita | TC (legacy) | Middle-earth themed; dormant |

**Install trap [CONFIRMED — Reddit/ModDB]:** do **not** copy `fx/` folder from older mods into **Steam Edition** — breaks FX; replace with vanilla `fx` first.

### Nexus Mods — entire catalog ≈12 mods [CONFIRMED]

Top endorsed (all-time, non-adult filter):

| Rank | Mod | Endorsements | DL | Type |
|------|-----|--------------|-----|------|
| 1 | [HD Reworked Project 5.0](https://www.nexusmods.com/stronghold2/mods/5) | 99 | 405 MB | Model/texture rework |
| 2 | [AI enhanced textures](https://www.nexusmods.com/stronghold2/mods/1) | 31 | 2.4 GB | AI upscale |
| 3 | [Enhanced Graphics](https://www.nexusmods.com/stronghold2/mods/7) | 20 | 278 MB | ChaiNNer 2–4× upscale |
| 4 | [ENB Steam 1.5](https://www.nexusmods.com/stronghold2/mods/6) | 17 | 90 KB | Bloom/shadows/darker grade |
| 5 | Play As The Lamb | 15 | 1 KB | Lord model swap → Seren |
| 6+ | Custom maps + UA translation | ≤8 | — | Content/localization |

No Nexus mod changes **sim rules** except cosmetic swaps.

### YouTube — SH2-specific mod coverage

| Video | Topic | URL |
|-------|-------|-----|
| Matteele mod review (DE) | “Best 3D Stronghold mod” — Crusader TC | https://www.youtube.com/watch?v=5zFp5lJAJbQ |
| Matteele release + install | Includes link to **New Balance** spreadsheet | https://www.youtube.com/watch?v=OExWfpX-7V8 |
| Pixel mod showcase | Matteele visual style | https://www.youtube.com/watch?v=V5Yhw7Xd4I4 |
| HD Reworked 5.0 | Nexus mod trailer | https://www.youtube.com/watch?v=M9uMTdaeo3s |
| MP AI tool (DE stream) | questforgaming enabler live | https://www.youtube.com/watch?v=v7tbBMu7ZSk |
| Legacy MP AI how-to | Pre-Steam disk versions | https://www.youtube.com/watch?v=FvMu4Y4-OfY |
| Firefly Steam Edition | Official visual comparison | https://www.youtube.com/watch?v=vbTdNoJKGHc |
| Workshop competition | Custom maps only | https://www.youtube.com/watch?v=4jz6hE2F96k |

**Not SH2:** most “QoL mod” YouTube hits are **Crusader DE / UCP** — do not assume feature parity.

### Stronghold Nation — utilities (mechanics > cosmetics)

| File | Author | Size | QoL value |
|------|--------|------|-----------|
| **Spear fix for Hawk/King/Bull** | Sir Windows | 2 KB | Patches `gamerules.dat` — armoury spear priority bug |
| **SH2 Community Lord Editor v1.1** | Asophix | 23 KB | GUI editor for AI lord behaviour in `gameRules.dat` |
| **Official AI Editor** | Firefly via Lord_Chris | 1.4 MB | Castle layout tool for AI estates |
| SH2 AI Atmospheric castles | Avrelian | 154 KB | Prebuilt AI castle packs |
| v1.2 Fixed Castles | Alfred The Baker | 12 KB | Legacy castle layout fixes |

Lord Editor thread: Stronghold Nation forums topic 1182 (SH2 adaptation of Legends editor).

### GitHub / GitLab — code mods (refreshed 2026-06-18)

Same tiny set as June scan; star leaders still FRC robotics false positives.

| Repo | Stars | License | Role |
|------|-------|---------|------|
| [Jpnock/Stronghold2-MP-AI](https://github.com/Jpnock/Stronghold2-MP-AI) | 13 | MIT | Pattern-scan NOP — MP AI |
| [Przodownik/Stronghold2-MP-AI-Patch](https://github.com/Przodownik/Stronghold2-MP-AI-Patch) | 0 | MIT | Fork |
| [crycodebaby/Stronghold2AnalyseHub](https://github.com/crycodebaby/Stronghold2AnalyseHub) | 1 | MIT | DX9 hook overlay |
| [Alleyv2/Stronghold2-AI-Enabler-Proton](https://github.com/Alleyv2/Stronghold2-AI-Enabler-Proton) | 1 | **None** | Proton offset variant |
| [gitlab.com/Daerandin/sh2_mp_ai_enabler](https://gitlab.com/Daerandin/sh2_mp_ai_enabler) | — | **None declared** | **Primary maintained** MP AI tool v0.3.1; questforgaming binary |
| [Ald0s/Stronghold2-Trainer](https://github.com/Ald0s/Stronghold2-Trainer) | 1 | None | Economy struct RE |
| [Eren121/Stronghold](https://github.com/Eren121/Stronghold) | — | None | S2M + unit pointer map |

**Steam forum consensus [TENTATIVE]:** older MP-AI tools may fail on Steam 1.5; AI sometimes **only attacks host** in MP co-op; Firefly **no plans** to add MP AI officially.

### What players ask for but mods don't solve

- Skirmish **game speed** slider (Crusader DE has community mod; **no SH2 equivalent** found)
- **Balance patch** changelog (Crusader UCP2 class)
- **Pathfinding bug fixes** (community reports; no MIT patch)
- **Stockpile section UI** clarity

→ These are **greenfield opportunities** for castle-sim.

### Visual / comfort QoL [UPDATED 2026-06-18]

Nexus top-4 mods are **all visual** — operator-validated as session QoL. See @concepts/stronghold-2-visual-qol-presets.md.

### Balance follow-up [2026-06-18]

[Nevikov New Balance sheet](https://docs.google.com/spreadsheets/d/1pZ-6cPoc9YkytVDPWSZurC6wXaqi052vm0KVXJdN2GU) (from [SH2-in-Crusader release video](https://www.youtube.com/watch?v=OExWfpX-7V8)) scraped → @sources/sh2-nevikov-new-balance-sheet-2026-06-18.md. **Crusader crossover balance**, not native Matteele SH2 stats.

## Dead Ends

- **Nexus “top mods” as mechanics reference** — cosmetic only; still valid **visual QoL** reference
- **Matteele TC as code base** — total conversion assets; license unclear; use as **design inspiration** only
- **WilliamVenner/stronghold2-ultimate-multiplayer-ai-patch** — GitHub search **0 results** (Steam forum mention only; dead link risk)
- **Importing ENB/HD packs into castle-sim** — wrong pipeline; build Godot materials instead
