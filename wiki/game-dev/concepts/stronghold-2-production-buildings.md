---
title: Stronghold 2 — production & civilian buildings (cost reference)
type: concept
tags: [concept, stronghold-2, buildings, economy, production]
keywords: [buildings, workshops, farms, honour, crime]
related:
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-castle-structures.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-ai-lords.md
  - entities/projects/castle-sim.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-resources-luxury-deep-read-2026-06-19.md
  - concepts/stronghold-2-lord-feasts-luxury-chains.md
maturity: validated
created: 2026-06-18
updated: 2026-06-19
---

## Relations

- @sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md — raw Heaven tables
- @concepts/stronghold-2-economy-storage-chains.md — storage routing graph

## Raw Concept

Complete **wood/gold/stone/worker cost** reference for SH2 non-siege buildings. Use for castle-sim `BuildingDefinition` data and rank-gate validation against @sources/sh2-heaven-kingmaker-ranks-2026-06-18.md.

## Narrative

### Storage hubs [CONFIRMED]

| Building | Cost | Role |
|----------|------|------|
| Stockpile | free | 30 sections; goods + candles |
| Granary | free | unlimited peasant food (SH2 change) |
| Armoury | 5w + 5s | weapons/armour |
| Treasury | 10s, 1 worker | tax rates + gold |
| Lord's Kitchen | 10s, 4 workers | noble foods + feasts |

### Core production chains

```
Wood: sawpit(3w) → workshops
Bread: wheatfarm(15w) → mill(20w,3) → bakery(10w)
Ale: hopfarm(15w) → brewery(10w) → inn(100w)
Cloth: sheepfarm(20w) → weaver(10w) → market/cloth goal
Weapons: ironmine + poleturner/fletcher/blacksmith/armourer/tanner → armoury
Honour food: garden/pig/vineyard/vintner/fishpond → lord's kitchen — detail @concepts/stronghold-2-lord-feasts-luxury-chains.md
```

### Gold-heavy buildings (Kingmaker economy pressure)

| Building | Gold | Notes |
|----------|------|-------|
| blacksmiths | 200 | swords/maces |
| monastery | 1000 | 6 monks |
| church | 500 | mass honour |
| jousting | 500 | +200 wood |
| statue | 250 | passive honour |
| siege camp | 500 | siege engine build site |

### Crime loop buildings [CONFIRMED]

Guard post (20w) → courthouse (25s) → punishment device (5–300g) + optional torturers guild (10w, 100g, 2 workers).

Falconer (20w) and apothecary (20w, 200g) are **mission-conditional** (rats/disease).

### castle-sim mapping (proposed)

| Phase | Buildings to data-file first |
|-------|------------------------------|
| Tier 1 (done) | sawpit, granary, farms, mill, bakery, quarry |
| Tier 2 | market, iron chain, weapon workshops |
| Tier 3 | church, joust, fair, monastery |
| Tier 4 | crime full roster + punishment devices |

Reference implementation stub: `castle-sim/data/sh2/lord_profiles.json` for AI; building JSON can mirror same `data/sh2/` pattern.

## Dead Ends

- Numeric **stockpile section caps** — @sources/sh2-heaven-resources-luxury-deep-read-2026-06-19.md (2026-06-19)
