---
title: SH2 Heaven — industry, farm, civilian & castle-service buildings (2026-06-18)
type: source
tags: [source, stronghold-2, buildings, economy, industry]
keywords: [buildings, wood, gold, workers, production]
related:
  - concepts/stronghold-2-production-buildings.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/projects/castle-sim.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-resources-luxury-deep-read-2026-06-19.md
read_status: read
source_type: community-wiki
source_url: https://stronghold2.heavengames.com/gameinfo/buildings/
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Full cost/worker scrape of SH2 Heaven **industry1–3**, **farmfood1–3**, **civilian1–3**, **cservices1–3**, **military1** (2026-06-18). Castle structures remain in @sources/sh2-heaven-castle-structures-2026-06-18.md.

## Narrative

### Industry & logistics [CONFIRMED]

| ID | Wood | Gold | Workers | Output / notes |
|----|------|------|---------|----------------|
| sawpit | 3 | — | 1 | 16 wood/load |
| beehive | 5 | — | 0 | wax for chandler |
| oxtether | 5 | — | 1 | hauls stone/iron |
| carterpost | 10 | — | 1 | inter-estate haul |
| chandlers | 10 | — | 1 | 2 candles/load |
| poleturners | 10 | 100 | 1 | spears/pikes |
| tanners | 10 | 100 | 1 | leather armour |
| weavers | 10 | — | 1 | cloth |
| ironmine | 20 | — | 2 | 8 iron/load via ox |
| stonequarry | 20 | — | 3 | needs ox |
| sheepfarm | 20 | — | 1 | 1 wool/load |
| pitchrig | 20 | — | 1 | on marsh |
| armourers | 20 | 100 | 1 | plate → armoury |
| blacksmiths | 20 | 200 | 1 | swords/maces |
| fletchers | 20 | 100 | 1 | bows/crossbows |

| ID | Notes |
|----|-------|
| stockpile | 30 sections; per-good caps vary |
| market | buy/sell; mission may restrict |

### Food chain [CONFIRMED]

| ID | Wood | Workers | Chain |
|----|------|---------|-------|
| applefarm | 5 | 1 | peasant food |
| hunterspost | 5 | 1 | meat |
| dairyfarm | 10 | 1 | cheese; cows for tanner |
| bakery | 10 | 1 | wheat→mill→bread |
| brewery | 10 | 1 | hops→ale |
| hopfarm | 15 | 1 | → stockpile |
| wheatfarm | 15 | 1 | → mill |
| pigfarm | 20 | 1 | lord food |
| gardenershut | 20 | 1 | vegetables → lord's kitchen |
| vineyard | 20 | 1 | grapes |
| vintners | 20 | 1 | wine |
| fishpond | 10 | 1 | eels/geese for feasts |
| mill | 20 | 3 | flour |
| inn | 100 | 1 | ale consumption / pop |
| granary | 0 | 0 | **unlimited** storage (SH2 vs SH1) |
| lordskitchen | — | 10 stone | 4 workers; feasts |

### Civilian & honour [CONFIRMED]

| ID | Stone | Gold | Workers | Effect |
|----|-------|------|---------|--------|
| treasury | 10 | — | 1 | tax + gold storage |
| bedchamber | 25 | — | — | marriage honour |
| church | 50 | 500 | 1 | mass honour |
| musiciansguild | 100 | 100 | 2 | feast entertainers |
| monastery | 100 | 1000 | 6 | manuscripts; fighting/warrior monks |
| statue | 10 | 250 | — | passive honour |
| travellingfair | 50 | 250 | 0 | seasonal pop |
| jousting | 200 | 500 | 0 | seasonal honour/pop |
| hovel | 6 wood | — | — | 8 peasants each |

Keeps (civilian1): saxon hall (wood), small/medium/large stone — qualitative defense only on Heaven.

### Castle services & crime [CONFIRMED]

| ID | Wood | Stone | Gold | Workers |
|----|------|-------|------|---------|
| falconerspost | 20 | — | — | 1 |
| guardpost | 20 | — | — | 1 |
| apothecary | 20 | — | 200 | 1 |
| courthouse | — | 25 | — | 1 |
| torturersguild | 10 | — | 100 | 2 |
| waterpot | 60 | — | — | 0 |

Punishment devices (cservices3) — honour bonus + rehab months: stocks (5g, 20mo), mask (10g), gibbet (20g), wheel (50g), flogging (80g), rack (120g), branding chair (150g), burning post (200 wood), gallows (300g).

### Military buildings [CONFIRMED — military1]

| ID | Wood | Stone | Gold |
|----|------|-------|------|
| armoury | 5 | 5 | — |
| barracks | — | 10 | — |
| engineersguild | — | 10 | 100 |
| mercenarypost | 15 | — | — |
| siegecamp | — | — | 500 |

## Snippets

- Weapon workshops deliver to **armoury**; food to **granary**; resources to **stockpile**
- Ox distance scales ox tether count per quarry/mine

## Dead Ends

- `/gameinfo/structures/` — 404; use `/gameinfo/buildings/` index
