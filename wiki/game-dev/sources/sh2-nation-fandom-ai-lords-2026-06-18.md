---
title: SH2 AI lords — Stronghold Nation + Fandom batch (2026-06-18)
type: source
tags: [source, stronghold-2, ai, kingmaker, community]
keywords: [ai-lords, barclay, queen, nation, fandom]
related:
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - entities/projects/castle-sim.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - entities/projects/castle-sim.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-military-units.md
  - sources/sh2-heaven-military-units-2026-06-17.md
  - entities/tools/sh2-community-lord-editor.md
  - sources/sh2-community-lord-editor-phase-0-audit-2026-06-18.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
read_status: read
source_type: community-guide
source_url: https://www.stronghold-nation.com/article/25-stronghold-2-ai-lords
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Second-pass ingest for **Kingmaker AI lord behavior** where SH2 Heaven only hosts Edwin/Grey/Olaf character pages. Primary: Stronghold Nation per-lord articles (Lord_Chris); engine rules: Fandom **Stronghold 2 — AI mechanics**.

## Narrative

### Fandom engine rules [CONFIRMED — AI mechanics wiki]

- Behavior **hard-coded**; `.aic` files only for **castle templates** (AIV Editor)
- Recruits only if **≥200 gold**; weapons bought if **≥400 gold**
- Five action cycles: bodyguards → defenders → reserves → **harass raids** → siege groups
- Harass may include catapults / fire ballistae; raiders seize estates
- Economy: per-lord production set; simultaneous multi-good trade (longer intervals than human)
- May **buy estate instead of ranking up**
- No ally commands; carter can send goods to AI
- **No warrior monks** in AI armies (skips monastery) [CONFIRMED — Steam + Fandom]

### Nation lord summaries [CONFIRMED — Nation articles unless noted]

| Lord | Harass | Siege composition | Castle notes |
|------|--------|-------------------|--------------|
| **Barclay (Hammer)** | Rare horse archers/catapults | Outlaws, crossbows, knights; catapults + trebuchets | Sophisticated; economy inside walls; slow to siege |
| **Queen** | **Horse archer** waves | Berserkers, archers, swordsmen; cats + catapults | Compact; granary + merc post outside |
| **King** | **None** (siege-only) | Spears, pikes, archers, swordsmen | Gap until great tower built; often **no siege** (no spears in armoury bug) |
| **Bishop** | **Macemen** building raids | Spears, macemen, crossbows; 1 trebuchet + cats | Church **outside walls** — lord visit vulnerability |
| **Sir William** | Archer groups | Archers, spears, swordsmen; cats | Granary always outside |
| **Lady Seren** | **Light cavalry spam** | Weak sieges | Worst wall gaps; single-line stone |
| **The Hawk** | Archers + catapults | Often **no siege** (no spears in armoury) | Fast-built towers; granary outside |
| **Sir Grey** | Spearmen + catapults | Spear-heavy; fast siege assembly | Thin wall by granary; fire ballista towers |
| **Olaf** | Berserkers + axe throwers | Same + cats, fire ballista, burning carts | Circular fort; pits/hounds |
| **Edwin** | Spearmen spam | Ladder-heavy | Weakest — see Heaven DKZS |
| **The Bull** | — | Campaign boss (PoW ch4) | **No Nation Kingmaker article found** |

### Community strength ranking [TENTATIVE — Nation forums 2023]

JustAVillager ordering (strong → weak): King, Queen, Hammer, William, Hawk, Bishop, Seren, Bull, Olaf, Grey, Edwin.

Treat as subjective — useful for Phase E difficulty tiers only.

### Nation article URL map [CONFIRMED — Exa fetch 2026-06-18]

| Lord | Nation URL |
|------|------------|
| Barclay | `/article/268-lord-barclay-stronghold-2-ai-lords` |
| Queen | `/article/270-the-queen-stronghold-2-ai-lords` |
| King | `/article/273-the-king-stronghold-2-ai-lords` |
| Bishop | `/article/272-the-bishop-stronghold-2-ai-lords` |
| William | `/article/276-sir-william-stronghold-2-ai-lords` |
| Seren | `/article/274-lady-seren-stronghold-2-ai-lords` |
| Hawk | `/article/275-the-hawk-stronghold-2-ai-lords` |
| Grey | `/article/269-the-queen-stronghold-2-ai-lords` *(slug mismatch — content is Sir Grey)* |
| Olaf | `/article/271-the-king-stronghold-2-ai-lords` *(slug mismatch — content is Olaf)* |

Heaven `/gameinfo/characters/hammer|barclay|queen|bishop/` — all 404.

## Dead Ends

- Nation slug ↔ numeric ID drift — verify content by H1 title not URL slug
- Reverse-engineering `.aic` for behavior — templates only, not decision tree
