---
title: Stronghold 2 — popularity model (implementation spec)
type: concept
tags: [concept, stronghold-2, popularity, simulation]
keywords: [popularity, tax, food-rations, ale, religion, entertainment, gong, crime]
related:
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/operator-vision-sh2-personal-clone.md
  - sources/stronghold-2-heaven-targeted-2026-06-13.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-campaign-economy-curriculum.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/gamespot-stronghold-2-qanda-2004.md
maturity: validated
created: 2026-06-13
updated: 2026-06-17
---

## Relations

- @concepts/stronghold-2-systems-inventory.md — parent systems map
- @concepts/stronghold-2-crime-punishment-loop.md — crime category (−1 per criminal)
- @sources/stronghold-2-heaven-targeted-2026-06-13.md — numeric tables source

## Raw Concept

Monthly **popularity score 0–100** from eight UI categories. Immigration requires **>50**; below 50 peasants emigrate until fixed.

## Narrative

### Core rule [CONFIRMED — SH2 Heaven popularity]

```
if popularity <= 50:
    peasants leave (no immigration)
if popularity > 50:
    immigration possible (subject to hovel/campfire caps — see economy doc)
```

Each category applies a **monthly delta** shown on the Popularity Panel (eight rows + total).

### 1. Tax [CONFIRMED]

Per-capita gold/month and popularity effect. **Lower tax revenue than SH1** at same band names.

| Tax band | Pop Δ / month | Gold / person / month |
|----------|---------------|------------------------|
| Large Bribe | +8 | −0.50 |
| Small Bribe | +4 | −0.25 |
| No Tax | +1 | 0.00 |
| Low Tax | −2 | +0.25 |
| Normal Tax | −4 | +0.50 |
| High Tax | −6 | +0.75 |
| Extortionate Tax | −8 | +1.00 |
| Cruel Tax | −12 | +1.25 |
| Extra Cruel Tax | −16 | +1.50 |

**Clone note:** One enum → `(pop_delta, gold_per_capita)`; multiply gold by population each month.

### 2. Food rations [CONFIRMED]

| Ration level | Pop Δ / month |
|--------------|---------------|
| No Rations | −8 |
| Half | −4 |
| Normal | 0 |
| Extra | +4 |
| Double | +8 |

Granary must hold food types consumed; honour gets separate bonus for variety (see systems inventory).

### 3. Gong [CONFIRMED]

Each **uncollected gong pile** in the estate: **−1 pop / month**. Gong pit worker removes waste; gong may be mission-gated off.

### 4. Rats [CONFIRMED]

Each **rat pack**: **−1 pop / month**. Falconer's Post trains falcons to control rats; rats mission-gated.

### 5. Crime [CONFIRMED]

Each **active criminal** (red noose on building): **−1 pop / month**. See @concepts/stronghold-2-crime-punishment-loop.md.

### 6. Ale [CONFIRMED]

Requires **Inn** + steady ale supply (Brewery chain). Higher consumption = more popularity but peasants drink instead of work.

| Ale consumption | Pop Δ / month |
|-----------------|---------------|
| None | 0 |
| Half | +2 |
| Normal | +4 |
| Extra | +6 |
| Double | +8 |

### 7. Religion [CONFIRMED]

Requires **Church** + **candles** (Chandler ← Bee Hive). Mass tier sets candle burn rate.

| Mass tier | Pop Δ / month |
|-----------|---------------|
| Simple | +2 |
| Standard | +4 |
| Special | +6 |
| Exulted | +8 |

Lord attending mass grants separate **honour** spike (~150, yearly cadence — systems inventory).

### 8. Entertainment [CONFIRMED]

**Jousting Arena** (500 gold build):

- 6 months construction → 6 months tournament active → dismantled → repeat
- **+5 pop / month** and **+20 honour / month** during tournament months
- Peasants leave jobs to watch (production hit)

**Travelling Fair** (250 gold build):

- 3 months assembly → 6 months active → 3 months rebuild cycle
- **+5 pop / month** while fair runs
- Same spectator production hit

Between seasons the fair/joust site is a **wood pile** that auto-rebuilds — no player action.

### Implementation sketch (Godot / castle-sim)

```gdscript
# Pseudocode — monthly tick
func recalc_popularity() -> int:
    var score := 50  # or carry forward from prior month
    score += TAX_TABLE[tax_band].pop_delta
    score += FOOD_TABLE[ration_level].pop_delta
    score += ale_table[ale_level].pop_delta
    score += religion_table[mass_level].pop_delta
    score += entertainment_bonus()  # joust/fair month flags
    score -= gong_pile_count
    score -= rat_pack_count
    score -= active_criminal_count
    return clampi(score, 0, 100)
```

**Phase B clone gate:** tax + food + one penalty (gong OR crime) before ale/church/entertainment.

## Snippets

Walkthrough opener (Mission 2 economy): double rations + tax ladder from −6 → −12 as ale stock allows — see SH2 Heaven Edwin walkthrough in targeted source.

## Dead Ends

- **Copying SH1 tax numbers** — SH2 table is strictly different per Heaven
- **Entertainment before granary loop** — joust/fair are honour/pop accelerators, not substitutes for food
