---
title: Stronghold 2 — military units & siege equipment (stat reference)
type: concept
tags: [concept, stronghold-2, military, units, siege]
keywords: [archer, knight, trebuchet, gold, honour, barracks]
related:
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-systems-inventory.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-ai-lords.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/sh2-heaven-military-units-2026-06-17.md
  - sources/sh2-nevikov-new-balance-sheet-2026-06-18.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @concepts/stronghold-2-siege-warfare.md — attack/defense tactics and phased clone delivery
- @sources/sh2-heaven-military-units-2026-06-17.md — raw Heaven ingest

## Raw Concept

Complete **qualitative + cost** reference for SH2 troops and siege/defense equipment from SH2 Heaven units1–5 / siege1–5. Use for castle-sim `UnitDefinition` / `SiegeEquipment` data files — numeric DPS/HP not published by Firefly.

## Narrative

### Barracks & monastery troops [CONFIRMED — SH2 Heaven]

| Unit | Gold | Honour | Weapon | Armour | Speed | Ranged | Melee | Notes |
|------|------|--------|--------|--------|-------|--------|-------|-------|
| Armed Peasant | 5 | — | — | — | Fast | — | Poor | Trap probe |
| Spearman | 8 | — | Spear | — | Fast | — | Poor | Moat dig; **push ladders** |
| Archer | 12 | 2 | Bow | — | Fast | Long | Poor | Standard ranged |
| Maceman | 20 | 1 | Mace | Leather | Fast | — | Good | Weak vs missiles |
| Crossbowman | 20 | 2 | Crossbow | Leather | Medium | Medium | Poor | **Pierces metal** |
| Pikeman | 20 | 2 | Pike | Metal | Medium | — | Good def / Poor off | Wall line holder |
| Swordsman | 40 | 8 | Sword | Metal | **Slow** | — | Excellent | Elite melee |
| Knight | 100 | 25 | Sword | Metal | Slow foot / fast horse | — | **Best** | Near-lord tier |
| Fighting Monk | 25 | 1 | — | — | Medium | — | Very Good | Monastery |
| Warrior Monk | 1 | 10 | — | — | Medium | — | Medium | Cheap gold, honour gate |
| Engineer | 30 | — | — | — | Fast | — | None | Siege crew |

### Mercenary post [CONFIRMED]

| Unit | Gold | Honour | Speed | Ranged | Melee | Notes |
|------|------|--------|-------|--------|-------|-------|
| Axe Thrower | 100 | — | Fast | Short | Poor | Infinite axes; anti-armour |
| Berserker | 80 | — | Fast | — | Excellent | **Largest charge bonus**; weak vs missiles |
| Horse Archer | 60 | 2 | Fast | Long | Poor | **Fire while moving** |
| Light Cavalry | 40 | 2 | Fast | — | Medium | Fastest; anti-siege sally |
| Outlaw | 60 | — | — | Medium | Poor | Javelin + sword; **hide in woods** |
| Pictish Boat Warrior | 40 | — | Medium | — | Poor | Cross water with boat |
| Assassin | 60 | 200 | Fast | — | Good | **Invisible at range**; grappling hook |
| Thief | 10 | 50 | Fast | — | Good | Disguise; steal treasury |

### Lord [CONFIRMED]

- Death = loss; medium foot / fast horse; **absolute best** melee

### Siege & defense equipment [CONFIRMED — SH2 Heaven siege pages]

| Equipment | Built | Gold | Other | Engineers | Role |
|-----------|-------|------|-------|-----------|------|
| Mantlet | Siege camp | 10 | — | 1 | Missile soak |
| Man Trap | Military | 1 | 6 wood | — | Hidden kill |
| Killing Pit | Military | 2 | 20 wood | — | Weight-trigger pit |
| Pitch Ditch | Military | 0 | 1 pitch | — | Hidden until lit |
| Brazier | Military | 50 | — | — | Fire arrows; light pitch |
| Moat | Military | 100/section | — | — | Delay infantry |
| Ballista | Military | 100 | — | 2 | Tower; anti-siege |
| Mangonel | Military | 100 | — | 2 | Tower; friendly fire risk |
| Fire Ballista | Siege camp / Eng guild | 150 | — | 2 | Burns wood; not stone |
| Burning Cart | Siege camp | 100 | — | 2 | Pitch/hay rush |
| Cat | Siege camp | 100 | — | 2 | Moat-fill cover |
| Battering Ram | Siege camp | 150 | — | 4 | Gatehouse |
| Catapult | Siege camp / Eng guild | 200 | — | 2 | Low arc; **cattle disease** |
| Siege Tower S/L | Siege camp | 150 / 250 | — | 4 | Gangplank; L has upper archers |
| Rolling Logs | Military | 200 | — | — | Wall defense |
| Rock Basket | Military | 100 | — | — | Infantry wall rocks |
| Stone Tipper | Military | 200 | — | — | Wall drop; replenishes |
| Oil Smelter | Military | 100 | 10 iron | 4 auto | Pitch → flaming pots |
| Tunnel | Military | 100 | 20 wood | 1+ | Undermine walls |
| War Hounds | Military | 200 | — | — | **Attacks everyone** nearby |
| Trebuchet | Siege camp | 200 | — | 3 | High arc; **immobile deployed**; cattle |

### Unit counter cheat sheet [INFERRED — Heaven + guides]

| Threat | Counter |
|--------|---------|
| Berserkers / macemen | Missiles, pikemen wall |
| Swordsmen / knights | Crossbows, oil, traps |
| Axe throwers | Archers at range; avoid melee rush |
| Ladders | Spearmen on wall push |
| Catapults | Archers, fire ballista, trebuchet duel |
| Thieves | Guards near treasury |

### castle-sim implementation notes

| Priority | Units for vertical slice |
|----------|-------------------------|
| **Now** | Armed peasant, archer, spearman (story combat v0) |
| **Phase B** | Maceman, crossbowman — honour costs |
| **Phase D** | Ladderman, catapult, ram |
| **Phase E** | Knight, trebuchet, assassin |

Data file suggestion: `data/units/sh2_reference.json` keyed by slug with gold/honour/building/rank_gate.

### Known Heaven gaps

- Shot range numeric values unpublished
- Engineer counts sometimes differ Steam guide vs Heaven (trebuchet 3 vs community 2) — use Heaven as primary [CONFIRMED source]

## Dead Ends

- Porting **exact** SH2 combat formulas without retail playtest — tune in Godot
- Pictish boat / outlaw — merc-only; defer until merc post building exists
