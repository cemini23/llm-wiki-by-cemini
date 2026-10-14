---
title: SH2 Heaven — resources, stockpile caps & luxury feast chains (2026-06-19)
type: source
tags: [source, stronghold-2, economy, storage, luxury, feast, honour]
keywords: [stockpile, lords-kitchen, inn, feast, resources, heaven]
related:
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-lord-feasts-luxury-chains.md
  - concepts/stronghold-2-production-buildings.md
  - concepts/stronghold-2-popularity-model.md
  - concepts/stronghold-2-systems-inventory.md
  - entities/projects/castle-sim.md
read_status: read
source_type: community-wiki
source_url: https://stronghold2.heavengames.com/gameinfo/resources/
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Raw Concept

Focused Heaven scrape closing the **stockpile per-section caps** queue item and **luxury / Lord's Kitchen / feast** production detail from `resources/`, `buildings/farmfood1–3`, `buildings/industry3`, and `honour/` (2026-06-19).

## Narrative

### Storage buildings [CONFIRMED — resources intro]

Four storage types: **Stockpile** (12 goods), **Armoury** (8 weapon types), **Granary** (4 peasant foods), **Lord's Kitchen** (4 noble foods + wine).

### Stockpile — per-section caps [CONFIRMED — resources table]

| Good | Load units | Max units / section |
|------|------------|---------------------|
| Ale | 1 | 16 |
| Candles | 2 | 16 |
| Cloth | 1 | 25 |
| Flour | 1 | 32 |
| Grapes | 1 | 15 |
| Hops | 2 | 16 |
| Iron | 8 | 36 |
| Pitch | 2 | 16 |
| Stone | 16 | **95** |
| Wheat | 2 | 32 |
| Wood | 16 | 36 |
| Wool | 1 | 16 |

**Stockpile building [CONFIRMED — industry3]:** **30 sections** each; additional stockpiles must be **adjacent** (no Heaven-stated hard cap — community guides use 2–3 for layout). **Full stockpile blocks production** [CONFIRMED — Matt Logan; not on Heaven resources page].

### Armoury market prices [CONFIRMED — resources]

| Item | Buy | Sell |
|------|-----|------|
| Bows | 31 | 15 |
| Crossbows | 58 | 30 |
| Spears | 20 | 10 |
| Pikes | 36 | 18 |
| Maces | 58 | 30 |
| Swords | 58 | 30 |
| Leather armour | 25 | 12 |
| Plate armour | 58 | 30 |

### Peasant food — production yields [CONFIRMED — farmfood1–2]

| Chain | Delivery | Granary units |
|-------|----------|---------------|
| Apple farm | each harvest | **3** apples |
| Hunter | each load | **6** meat |
| Dairy | each load | **4** cheese |
| Bakery | per flour bag | **16** bread |
| Hop farm | each load | **2** hops |
| Granary | — | **unlimited** (SH2 vs SH1 cap) |

### Luxury / Lord's Kitchen chain [CONFIRMED — farmfood1–3 + resources]

| Item | Building | Cost | Workers | Notes |
|------|----------|------|---------|-------|
| Eels / Geese | Fishpond | 10w | 1 | **Alternates** 1 unit each delivery → Lord's Kitchen |
| Vegetables | Gardener's Hut | 20w | 1 | 1 unit/load |
| Pigs | Pig Farm | 20w | 1 | 1 unit/load |
| Grapes | Vineyard | 20w | 1 | → stockpile, 1 unit |
| Wine | Vintner | 20w | 1 | grapes → Lord's Kitchen, 1 unit |
| Lord's Kitchen | — | **10 stone** | **4** | cook + pages → keep feasts |

**Honour page** lists feast foods as *Ducks, Eels, Pigs, Vegetables, Wine* — Heaven resources table uses **Eels + Geese** from fishpond, not ducks. Treat **geese as 5th noble protein** alongside eels; "ducks" likely legacy wording.

### Ale / Inn popularity tradeoff [CONFIRMED — farmfood2 + popularity]

- **Inn:** 100 wood, 1 worker
- Higher ale consumption → higher popularity (see @concepts/stronghold-2-popularity-model.md)
- **Worker penalty:** peasants drink at inn, wander **drunk** instead of working — **production suffers** (explicit Heaven text)

### Feast honour math [CONFIRMED — honour page]

```
feast_honour = (4 × guests × food_types) + 10
```

- Each guest eats **1 unit of each available food type**
- **Large Keep** max **9 guests**; max **5 food types** → theoretical cap **190** before musician bonus
- **Musicians Guild:** +10 honour per feast
- Lord's Kitchen panel shows stock, expected guests, projected feast honour

### Other honour sinks using luxury chain [CONFIRMED — honour]

| Source | Honour | Notes |
|--------|--------|-------|
| Lady's dance | **200** | 4× cloth (page from kitchen) → dance; repeat after 4 new dresses |
| Church mass (lord attends) | **150** | ~1×/year; civilian duty |
| Joust | **20/mo** × 6 mo/yr | +5 pop/mo; peasants watch → production hit |
| Granary variety | +1/mo per type >1 | **Double** if double rations |
| Monastery manuscript | +5 each | ~2 years/monk × 6 monks |

### Bee / candle luxury [CONFIRMED — industry1]

- Beehive: 5w, **0 workers** — wax for chandler near hive
- Chandler: 10w, 1 worker — **2 candles/load** → stockpile → church masses

## Snippets

```
Feast example: 6 guests × 3 food types → (4×6×3)+10 = 82 honour
Stone section cap 95 vs wood 36 — quarry overflow risk highest on stone
```

## Dead Ends

- Per-building `/lordskitchen/` URLs — 404; use `farmfood3` batch pages
- Hard **3 stockpile cap** — not in Heaven industry3; community Kingmaker guides only
