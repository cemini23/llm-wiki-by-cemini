---
title: SH2 Heaven — castle structures & walls (2026-06-18)
type: source
tags: [source, stronghold-2, buildings, castle, walls]
keywords: [gatehouse, tower, walls, stone, wood]
related:
  - concepts/stronghold-2-castle-structures.md
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - concepts/stronghold-2-production-buildings.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-systems-inventory.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - entities/projects/castle-sim.md
read_status: read
source_type: community-wiki
source_url: https://stronghold2.heavengames.com/gameinfo/buildings/
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Castle **gatehouses, towers, walls** cost and qualitative durability notes from SH2 Heaven `cstructures1–3` (2026-06-18). Supersedes dead `/gameinfo/castle/castle1/` URLs.

## Narrative

### Gatehouses [CONFIRMED — cstructures1]

| Structure | Material cost | Notes |
|-----------|---------------|-------|
| Wooden gatehouse | 20 wood | Early Freeman rank |
| Small gatehouse | 15 stone | Knight rank unlock |
| Medium gatehouse | 30 stone | Knight Errant |
| Large gatehouse | 50 stone | Earl rank |

### Towers [CONFIRMED — cstructures2]

| Tower | Stone | Wood | Arrow slits | Siege top |
|-------|-------|------|-------------|-----------|
| Lookout | 15 | — | 0 | No — weak |
| Bastion | 10 | — | 0 | Low |
| Square | 24 | — | 1 | Yes |
| Square hoarded | 24 | 20 | 1 | No — hoarding burns to square |
| Round | 30 | — | 2 | Yes |
| Round hoarded | 30 | 20 | 2 | No |
| Great | 50 | — | 4 | Yes — strongest/tallest |

### Walls & access [CONFIRMED — cstructures3]

| Structure | Cost | Behavior |
|-----------|------|----------|
| Wooden wall | 1 wood / section / layer | Foot soldiers can break through |
| Stone wall (single) | 1 stone / section | Blocks infantry; weak vs siege |
| Stone wall (double) | 2 stone / section | Crenellations; stronger |
| Thicker walls | Manual stacking | Auto-build 3 thicknesses max |
| Wooden platform | 10 wood | Archers; freestanding or on wood walls |
| Stone staircase | 10 stone | Adjacent to wall access |
| Sally port | 20 stone | Hidden wall exit; smash to use |

### Design implications for castle-sim

- **Material tiers:** wood → single stone → double stone matches Kingmaker rank gates (Knight = stone walls)
- **Hoarding trade-off:** + troop protection, − siege engine placement; fire reverts tower
- **Great tower** = endgame anchor (Duke unlock: tower ballista)

## Dead Ends

- `/gameinfo/castle/walls1/` — 404; use `/gameinfo/buildings/cstructures3/#stonewalls`
