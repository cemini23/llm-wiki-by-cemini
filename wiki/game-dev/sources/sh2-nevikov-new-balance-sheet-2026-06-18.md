---
title: SH2 Nevikov New Balance spreadsheet ingest (2026-06-18)
type: source
tags: [source, stronghold, balance, community, crusader]
keywords: [new-balance, nevikov, spreadsheet, units, buildings]
related:
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - concepts/stronghold-2-visual-qol-presets.md
  - concepts/stronghold-2-military-units.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - entities/projects/castle-sim.md
read_status: read
source_type: community-sheet
source_url: https://docs.google.com/spreadsheets/d/1pZ-6cPoc9YkytVDPWSZurC6wXaqi052vm0KVXJdN2GU/edit#gid=1449736525
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Ingest of **Nevikov / community New Balance** Google Sheet linked from [Mod-Release: Stronghold 2 in Crusader](https://www.youtube.com/watch?v=OExWfpX-7V8). Method: `gviz/tq` CSV export, compare gid **0** (Vanilla) vs **1449736525** (New Balance).

**Scope trap [CONFIRMED]:** sheet covers **Stronghold Crusader 1.14** unit/building economy (internal HP ×1000 scale, Arab units, tunneler, etc.) — **not** native SH2 Steam stats. Matteele Crusader Edition (SH2 desert TC) has **no public balance sheet**; this sheet is the crossover-mod balance pack bundled with Nevikov's SH2-lords-in-Crusader release.

## Narrative

### Sheet tabs

| gid | Label | Role |
|-----|-------|------|
| 0 | Vanilla Values | Crusader retail baseline in sheet |
| 1449736525 | New Balance / Nevikov Balance | Community rebalance |

### Unit deltas (Vanilla → New Balance) — SH2-overlapping roles

| Unit | Change |
|------|--------|
| Spearman | HP +20%; base melee damage +50% |
| Maceman | HP +33% |
| Swordsman | HP +20%; speed level 4→3 (faster) |
| Knight | HP +50%; base damage +25% |
| Ladderman | HP ×4 |
| Engineer | HP ×2 |
| Siege Tower | HP ×2; speed level 3→9 |
| Battering Ram | HP +60%; speed level 3→4 |

Archer / Crossbowman / Catapult / Trebuchet / Mangonel / Lord: **no row change** between tabs in June 2026 export.

### Building wood-cost deltas

| Building | Vanilla | New Balance |
|----------|---------|-------------|
| Killing Pit | 6 | 3 |
| Pitch Rig | 20 | 10 |

(Crusader building names — map to SH2 `Killing Pit` / pitch economy only by analogy.)

### Goods market (unchanged between tabs in export)

Buy-5 / Sell-5 prices identical for Wood, Stone, Iron, weapons, food chain — **New Balance focuses on combat survivability**, not market spreads.

### castle-sim mapping

→ `castle-sim/data/sh2/balance_presets.json` preset `nevikov_new_balance_inspired` — relative multipliers only, applied when SH2 combat HP model lands.

→ `community_spear_fix` preset — separate SH2-native `gamerules.dat` fix (King/Hawk/Bull).

## Dead Ends

- Treating sheet as **Matteele SH2 mod** balance — wrong game/mod; Matteele is visual-sound TC without published stat table
- Copying Crusader HP integers into SH2 sim — different engines and qualitative Heaven tiers
