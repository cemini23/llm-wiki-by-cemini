---
title: Stronghold systems inventory — buildings, units, economy (SH1 + deltas)
type: concept
tags: [concept, stronghold, reference, buildings, units, economy]
keywords: [stronghold, buildings, units, granary, popularity, crusader, siege]
related:
  - entities/games/stronghold-series.md
  - concepts/stronghold-deconstruction.md
  - concepts/vertical-slice-v0.md
  - concepts/scope-tiers.md
  - sources/stronghold-hd-manual-2001.md
  - sources/stronghold-series-wikipedia-2026-06-13.md
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - entities/projects/castle-sim.md
  - entities/tools/unofficial-crusader-patch2.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/gdc-total-war-warhammer-siege-ai.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @entities/games/stronghold-series.md — franchise timeline & engines
- @concepts/stronghold-deconstruction.md — hobby cut matrix
- @concepts/vertical-slice-v0.md — Tier 1 subset

## Raw Concept

Implementable inventory of Stronghold (2001) systems plus Crusader and later-title deltas — for scope planning, not cloning.

## Narrative

### Core simulation loop (Stronghold 2001)

1. Place **Keep** → unlocks granary/stockpile chain
2. **Hovels** → population cap; peasants spawn and seek jobs
3. **Gather** wood, food, stone, iron, pitch on map-dependent tiles
4. **Workshops** convert stockpile goods → weapons/armor in **Armory**
5. **Barracks** spends gold + weapons → military units (troops don't eat from granary)
6. **Popularity** (tax + rations + religion + ale + fear factor + events) → immigration/emigration
7. **Castle** walls/towers/traps → survive sieges; **lord death** = lose

Popularity below ~50 → peasants leave. [CONFIRMED — HD manual §2.7]

---

### Resources (SH1)

| Resource | Source | Storage | Primary use |
|----------|--------|---------|-------------|
| **Wood** | Woodcutter's hut | Stockpile | Buildings, basic weapons |
| **Stone** | Quarry (on white boulders) | Stockpile | Castle walls, towers |
| **Iron** | Iron mine (red rock hills) | Stockpile | Maces, swords, metal armor |
| **Pitch** | Pitch rig (marsh) | Stockpile | Boiling oil, pitch ditches |
| **Food** | Farms/hunter | **Granary** | Rations → popularity |
| **Gold** | Taxes, market sell | Treasury | Troops, mercenaries (Crusader) |
| **Weapons/Armor** | Workshops | **Armory** | Barracks recruitment |

---

### Food economy (SH1)

**Granary** stores all food; ration slider sets consumption vs popularity tradeoff. Multiple food types eaten = popularity bonus. [CONFIRMED — manual §2.5, §4]

| Food | Chain | Notes |
|------|-------|-------|
| **Meat** | Hunter's post → granary | Fast early food |
| **Cheese** | Dairy farm → granary | Also cows → tanner → leather armor |
| **Apples** | Apple farm (orchard) → granary | Simple farm tile |
| **Bread** | Wheat farm → **Mill** (flour) → **Bakery** → granary | Highest late-game efficiency |
| **Ale** | Hops farm → **Brewery** → **Inn** | Worker efficiency + popularity (not food) |

Optimal placement pattern (community consensus): mills near stockpile; bakeries between stockpile and granary; hunters/apple/dairy near granary. [TENTATIVE — Stronghold Heaven, TheGamer Crusader DE guide]

**Crusader** adds same four food types; granary cap **250 units per building** (adjacent granaries stack). [TENTATIVE — Fandom]

---

### Popularity modifiers (SH1)

| Factor | Effect |
|--------|--------|
| Tax rate | Higher tax ↓ popularity; gold income |
| Ration level | None/low ↓; generous ↑ |
| Food variety | More types ↑ |
| Religion | Chapel / church / cathedral |
| Ale coverage | Working inns |
| **Fear factor** | Punishments (gallows, stocks) vs decorations ( gardens, statues) — efficiency vs happiness tradeoff |
| Fairs / jugglers | Temporary events |
| Crowding | Too many hovels cramped ↓ |

**Tier 1 cut:** defer fear factor, religion, ale, fairs — use single resource + simple cap.

---

### Castle buildings (Stronghold 2001)

#### Fortifications

| Building | Function |
|----------|----------|
| **Keep** | Lord home; starting building; loss condition |
| **Wooden / stone walls** | Draw placement; wood cheaper, weak |
| **Crenellations** | Added to wall face |
| **Gatehouse** | Entry; controllable |
| **Drawbridge** | Span moat |
| **Towers / turrets** | Garrison archers; square vs round |
| **Stairs** | Access wall tops |
| **Moat** | Dug around walls; slows attackers |
| **Killing pit** | Hidden trap |
| **Pitch ditch** | Fire trap (needs pitch) |

#### Defensive engines & traps

| Building | Function |
|----------|----------|
| **Engineer's guild / Tunneler's guild** | Train engineers, tunnelers |
| **Mangonel / Ballista** | Wall-mounted; engineer-operated |
| **Oil smelter / tipper** | Boiling oil |
| **Brazier** | Fire arrows |
| **Mounted rolling logs** | Wall trap |
| **Wardog** | Released vs attackers |

#### Industry & storage

| Building | Function |
|----------|----------|
| **Stockpile** | Wood, stone, iron, pitch, wheat, flour |
| **Granary** | All food |
| **Armory** | Weapons & armor stock |
| **Market** | Buy/sell goods (map-limited assortment) |

#### Food production

Hunter's post, dairy farm, apple farm, wheat farm, hops farm, mill, bakery, inn (+ brewery).

#### Weapons production

| Workshop | Output |
|----------|--------|
| Fletcher | Bows (2 wood), crossbows (3 wood) |
| Poleturner | Spears (1 wood), pikes (2 wood) |
| Blacksmith | Maces (1 iron), swords (1 iron) |
| Tanner | Leather armor (1 cow → 3 suits) |
| Armorer | Metal armor (1 iron) |

#### Civilian / morale

Hovel, well, apothecary, chapel → church → cathedral, statue, goods cart (carter), pitch rig, quarry, ox tether, woodcutter's hut.

#### Military structures

| Building | Function |
|----------|----------|
| **Barracks** | Hire European troops (gold + weapons) |
| **Stable** | Horses for knights |
| **Siege camp** | Build catapult, trebuchet, etc. |

---

### Military units (Stronghold 2001 — Barracks + guilds)

#### Barracks (8 types)

| Unit | Role | Notes |
|------|------|-------|
| **Archer** | Ranged | Fast, no armor, weak melee |
| **Crossbowman** | Ranged | Slow reload; pierces metal |
| **Spearman** | Melee | Cheap; **fills moats**; ladders |
| **Pikeman** | Melee | Heavy defense, slow |
| **Maceman** | Melee | Fast assault |
| **Swordsman** | Melee | Elite slow infantry |
| **Knight** | Melee | Fast, deadly; needs stable horse |
| **Ladderman** | Siege | Cheap; very vulnerable |

#### Guild / special

| Unit | Source | Role |
|------|--------|------|
| **Engineer** | Engineer's guild | Build/man siege equipment |
| **Tunneler** | Tunneler's guild | Undermine walls |
| **Black monk** | Event | Story assistance |

#### Siege equipment (requires engineers)

Portable shield, battering ram, siege tower, catapult, trebuchet; tunneling; moat filling by troops.

**Unit commands:** group (Ctrl+#), patrol, stances (stand ground / defensive / aggressive), fortify on walls, bookmarks. [CONFIRMED — manual §7]

---

### Stronghold: Crusader additions

#### Mercenary post (Arabic) — gold-only recruitment

Assassin (scale walls), horse archer, slave (fire raids), fire thrower, slinger, Arabian bowman, Arabian swordsman, fire ballista. [CONFIRMED — Crusader wiki summary]

Later DE content: Bedouin stockade units (skirmisher, sapper, camel lancer, etc.) [TENTATIVE — DE patch notes]

#### Skirmish AI lords (8)

Personalities with distinct castle layouts and aggression — e.g. Saladin (balanced), Caliph (pitch mazes), Richard (knights), Sultan (weak military). [TENTATIVE — community lore]

#### Modes

- **Skirmish Trail** — 50 linked missions, escalating difficulty
- **Custom Skirmish** — pick lords, alliances, start conditions (Crusader / Deathmatch / Building modes)
- **Map editor** — full scenario scripting

---

### Stronghold 2 additions (reference only — Tier 2+)

Full inventory: @concepts/stronghold-2-systems-inventory.md

- **Full 3D** castle construction; wall/tower types changed
- **Crime system** — peasants commit crimes; guards, courthouse, trials
- **Punishments** — stocks → torture devices → gallows (honour tradeoffs)
- **Honour** currency — ranks, troop training, Kingmaker mode
- **Jousting / feasts** — lord activities
- **Gong / falconer / monastery** — hygiene and honour sources
- Launch instability → **Stronghold 2 Deluxe** [CONFIRMED — Firefly press, patches]

---

### Stronghold 3 / Crusader II / Warlords (abbreviated)

| Title | Notable systems |
|-------|-----------------|
| **SH3** | Free-angle walls; night/day; weather; physics-ish siege |
| **Crusader II** | SH3 engine; co-op; refined skirmish |
| **Warlords** | East Asia; **warlord powers**; aesthetics affect population; lighting focus |

---

### Engineering mapping → castle-sim Tier 1

| Stronghold system | v0 vertical slice | Tier 1 full | Defer |
|-------------------|-------------------|-------------|-------|
| Wall draw | ✓ grid segments | crenellations, gates | moat, pitch |
| Wood economy | ✓ gather only | stone, iron | market |
| Peasants | ✓ one job | workshop chains | fear/religion |
| Archers on walls | ✓ shoot target | stances, oil | full roster |
| Pathfinding | ✓ **spike** | dynamic walls | 1000s of units |
| Popularity | — | simplified meter | full sim |
| Siege engines | — | — | Tier 2 |
| AI lords | — | timer wave | skirmish AI |
| Mercenaries | — | — | Crusader phase |

---

### Non-military characters (flavor / UI)

Lord (death = lose), Lady, Jester, children, mothers, drunkards, priests, healer, traders, fair performers — **personality layer** that sells the sim. Defer all for v0; optional audio barks Tier 2. [CONFIRMED — manual §10.1]

## Snippets

### SH1 weapon → workshop quick ref

```
Bow=2w  Crossbow=3w  Spear=1w  Pike=2w  Mace=1i  Sword=1i
Leather=1 cow→3 suits  Metal armor=1 iron
```

### v0 ⊆ SH1

```
walls + wood + peasants + archers ≈ 5% of SH1 building count, ~15% of unit roster
```

## Dead Ends

- **Cloning Crusader mercenary economy in v0** — gold instant army skips the workshop fantasy; defer.
- **SH2 crime/honour in Tier 1** — was deferred when target was SH1; **reopened** for operator SH2 clone — phase after popularity spine (@concepts/operator-vision-sh2-personal-clone.md).
