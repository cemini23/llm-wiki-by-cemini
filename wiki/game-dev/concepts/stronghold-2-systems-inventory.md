---
title: Stronghold 2 — systems inventory (personal clone target)
type: concept
tags: [concept, stronghold, stronghold-2, reference, systems]
keywords: [stronghold-2, honour, crime, kingmaker, popularity, 3d, estates]
related:
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-popularity-model.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-architect-controls.md
  - concepts/stronghold-systems-inventory.md
  - concepts/stronghold-deconstruction.md
  - concepts/scope-tiers.md
  - entities/games/stronghold-series.md
  - entities/projects/castle-sim.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - sources/stronghold-2-heaven-targeted-2026-06-13.md
  - sources/github-stronghold-2-scan-2026-06-13.md
  - sources/mobygames-stronghold-2-2026-06-13.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - entities/tools/stronghold2-mp-ai-patch.md
maturity: draft
created: 2026-06-13
updated: 2026-06-15
---

## Relations

- @concepts/operator-vision-sh2-personal-clone.md — **operator north star** (personal play only)
- @concepts/stronghold-systems-inventory.md — SH1 baseline; SH2 deltas below
- @concepts/stronghold-2-popularity-model.md — **numeric popularity spec**
- @concepts/stronghold-2-crime-punishment-loop.md — **crime state machine + devices**
- @concepts/stronghold-2-economy-storage-chains.md — **storage + production graph**
- @concepts/stronghold-2-architect-controls.md — **Space / camera for Fork B**
- @concepts/stronghold-2-github-ecosystem-shelf.md — **GitHub patches, trainers, S2M tools**
- @sources/gamespy-stronghold-2-bradbury-qa-2004.md — siege/wall design intent

## Raw Concept

Deep systems map of **Stronghold 2 (2005)** — Firefly's 3D castle-life sim + RTS. Primary reference for operator's personal hobby clone. Study **mechanics and feel**, not Firefly assets or campaign script.

## Narrative

### What makes SH2 different from SH1 / Crusader

| Dimension | SH1 / Crusader | Stronghold 2 |
|-----------|----------------|--------------|
| Presentation | 2D isometric sprites | **Full 3D** (Vision Engine); architect top-down (Space) for building |
| Wall combat | Foot soldiers can **hack walls** | **Siege breaches only** — ladders, rams, towers; fight on/along walls |
| Economy meta | Popularity + food chains | Popularity **and** **Honour** (second currency) |
| Social sim | Religion, fear, ale (SH1) | + **Crime/punishment**, gong/rats, courthouse |
| Lord fantasy | Minimal | **Feasts, dances, jousting, church attendance**, Lady/bedchamber |
| Map meta | Single castle focus | **Estates** — honour-purchased villages feeding carts to castle |
| Progression | Campaign missions | **Kingmaker ranks** gate buildings/units by honour spend |
| Editor | Real-time (SH1) | Still-life / different workflow [TENTATIVE] |

Bradbury later called SH2 **overreach** vs fan appetite for SH1 simplicity — but SH2 remains the fan-favourite "castle life" entry for many players. [CONFIRMED — @sources/simon-bradbury-stronghold-heaven-sh3-2011.md]

### Game modes [CONFIRMED — MobyGames, Firefly press, SH2 Heaven]

| Mode | Focus |
|------|-------|
| **Military campaign** | Restore order to England; economy supports army |
| **Path of Peace** | Economy-first campaign; limited beasts/bandits |
| **Kingmaker** | Rank-gated sandbox skirmish — honour → promotions → unlock roster |
| **Free build / sandbox** | Castle builder without pressure |
| **Multiplayer / skirmish** | Steam Edition (2017+) |
| **Historical castles** | Pre-made siege/defend scenarios; Deluxe adds Windsor, Edinburgh, etc. |

### Core simulation loop

```
Peasants (hovels) → jobs at buildings → goods to stockpile/granary
        ↓
Popularity (>50 to grow) ← tax, food variety, ale, church, entertainment, gong/crime penalties
        ↓
Honour ← feasts, dances, joust, church mass, granary variety, statues, punishments, monastery
        ↓
Spend honour → military units, Kingmaker rank-ups, buy neutral estates
        ↓
RTS combat — defend siege / attack rivals; lord avatar can fight in plate
```

**Key rule:** Honour is useless without popularity — both meters matter. [CONFIRMED — Stronghold Nation, SH2 Heaven]

### Popularity system [CONFIRMED — SH2 Heaven]

Full tables → @concepts/stronghold-2-popularity-model.md

- Range **0–100**; must stay **>50** for immigration
- Eight monthly categories: tax, food, gong, rats, crime, ale, religion, entertainment

Emergency reset: if all peasants gone and pop long low, game may reset popularity to **70** [TENTATIVE — community guides]

### Honour — gains [CONFIRMED — SH2 Heaven honour page]

| Source | Mechanism | Typical yield |
|--------|-----------|---------------|
| **Feast** (Lord's Kitchen) | Royal foods: duck, eel, pig, veg, wine | `(4 × guests × food_types) + 10`; max ~190 + musician bonus |
| **Musicians Guild** | Jester/troubadour at feasts | +10 per feast |
| **Lady's dance** | 4 cloth → dresses → dance | **200** honour (repeat after 4 more dresses) |
| **Monastery** | ~6 monks, manuscripts over ~2 years each | +5 per manuscript |
| **Jousting** | 6 on / 6 off months | +20/month during tournament |
| **Church mass** | Lord on civilian duty, ~yearly | **150** |
| **Granary variety** | +1/month per food type over 1; doubled if double rations | up to +6/month at 4 types |
| **Statues** | Passive | +1/month each (no known cap) |
| **Marriage / bedchamber** | Lord + Lady event ~yearly | +1 |
| **Punishments** | While sentence runs | +1/month per device (stocks 20 months = 20 honour total, etc.) |

### Honour — spends [CONFIRMED — SH2 Heaven]

**Units (honour + gold + gear):**

| Unit | Honour |
|------|--------|
| Archer, Crossbow, Maceman, Pikeman, Horse Archer, Light Cavalry | 1–2 |
| Swordsman | 8 |
| Knights, Warrior Monks | 25 |
| Thief | 50 |
| Assassin | 200 |

**Kingmaker rank promotions:** Freeman→Yeoman 10 … Earl→Duke 300 (see rank table below)

**Estates:** buy neutral villages for **100 gold** (honour-gated in some missions) — carts deliver goods to castle [CONFIRMED — MobyGames, casting overview]

### Crime & punishment [CONFIRMED — SH2 Heaven FAQ + cservices]

Full state machine + device stats → @concepts/stronghold-2-crime-punishment-loop.md

- Red **noose** = criminal worker; building idle until caught/rehabbed/executed
- Minimum: Guard Post → Courthouse (dungeon) → punishment; torturer for flogging+
- **Guard post by granary** — criminals steal food

Stealing from **enemy treasury** via **Thief** unit — 25 gold per tick [TENTATIVE — community]

### Kingmaker rank unlock table [CONFIRMED — SH2 Heaven kingmaker page]

| Rank | Honour cost | Notable unlocks |
|------|-------------|-----------------|
| **Freeman** | — | Wood walls, barracks, hovels, granary, hunter/apple/dairy farms, market, **armed peasants** |
| **Yeoman** | 10 | Lord's Kitchen, wheat/mill/bakery, pig farm, quarry, ox, **gong pit** |
| **Squire** | 15 | Monastery, musicians guild, veg garden, iron mine, falconer |
| **Knight** | 30 | **Stone walls**, armoury, merc post, siege camp, joust, bedchamber, courthouse, stocks, spearmen/archers/cavalry/ladders |
| **Knight Bachelor** | 50 | Lookout, man trap, mangonel, church, vineyard, pikemen |
| **Knight Errant** | 100 | Bastion, pitch ditch, fair, torturer's guild, crossbowmen, siege tower |
| **Royal Champion** | 150 | Square towers, stables, statues, swordsmen, battering ram |
| **Baron** | 200 | Round towers, war hounds, inn/ale chain, macemen, catapult |
| **Earl** | 250 | Large gatehouse, oil smelter, moat, horse archers, thieves, fire ballista |
| **Duke** | 300 | Great tower, tower ballista, knights, assassins, **trebuchet** |

This table is the **natural milestone spine** for a SH2-like hobby project — each rank ≈ one vertical slice.

### Building categories (SH2 Heaven index)

Tabs in UI: **Farms & Food**, **Industry**, **Castle Services** (punishments), **Civilian** (keeps), **Castle Structure** (walls/gates/towers), **Military** (+ siege/defensive in military units section).

Notable SH2-only or emphasized vs SH1:

- **Gong pit** + workers; **falconer** (pest control)
- **Lord's Kitchen**, royal food chain (eel pond, bee hive, vineyard/vintner)
- **Bedchamber / Lady**, **Musicians Guild**
- **Courthouse**, **Guard Post**, full torture roster
- **Jousting Arena**, **Travelling Fair**
- **Estates** (map-level, not a building tab)
- Traps: man trap, killing pit, pitch ditch, brazier, rolling logs, moat, tunnel

Industry + castle services costs → @concepts/stronghold-2-economy-storage-chains.md + crime doc. Military unit stats → deferred Phase D [NEEDS VERIFICATION 2026-06-20].

### Military & siege (overview)

**Troop families:** peasants → spearmen/archers/pikemen/swordsmen/macemen; cavalry tiers; monks; mercenary oddities (Pictish boat warrior, berserker); thieves/assassins.

**Siege equipment:** ladders, mantlets, burning cart, siege towers (S/L), battering ram, catapult, fire ballista, trebuchet.

**Defensive:** mangonel, tower ballista, oil/fire, hoardings, engineer-built traps.

**Combat UX pain (community):** formation micro is tedious; economy vs invasion pacing feels like "Stalin's dilemma" — design note for clone: consider QoL (group move, rally points). [TENTATIVE — MobyGames player review]

### 3D-specific design wins [CONFIRMED — GameSpy Bradbury Q&A]

- **Tower interiors** — spiral stair fights
- **Architect camera** — gap spotting, thick wall "paint" → @concepts/stronghold-2-architect-controls.md
- **Lord avatar** — third-person melee in campaign
- **No sword-wall hacking** — forces siege roster depth

For Godot: either **true 3D** (Vision-like) or **2.5D fake** (SH1 camera + SH2 mechanics only) — see @concepts/operator-vision-sh2-personal-clone.md.

### AI lords (Deluxe / Steam)

Base roster + Deluxe adds **The Queen, The Pontifex, Sir Grey** [CONFIRMED — MobyGames Deluxe notes]. Full personality matrix → separate ingest from SH2 Heaven AI page.

### Engineering mapping → castle-sim (current fork)

| SH2 system | castle-sim today (~2026-06-13) | Clone phase |
|------------|----------------------------------|-------------|
| 3D castle build | 2D prototype only | **Fork B** — story-005 architect spike |
| Popularity | — | Phase B |
| Honour | — | Phase B |
| Crime/punishment | — | Phase C |
| Kingmaker ranks | — | Phase D (progression spine) |
| Food chains (4+ types) | Wood only | Phase B |
| Gong/falconer | — | Phase C |
| Feasts/joust/dance | — | Phase C |
| Estates | — | Phase E |
| Siege roster | Archer v0 | Phase D–E |
| No wall-hacking | N/A (grid walls) | Phase D siege |
| Lord avatar combat | — | Phase E optional |

### Personal-use legal boundary [CONFIRMED — wiki policy]

Operator intent: **play alone, no sale, no redistribution.** Still:

- Do **not** ship Firefly `.pak` assets, voice lines, campaign text, or trademarked branding in a public repo
- **OK:** reimplement mechanics, original placeholder art, inspired UI layout
- Buying **Stronghold 2: Steam Edition** for side-by-side reference is the cleanest research setup

## Snippets

Honour feast formula (from SH2 Heaven):

```
honour = (4 × guests × food_types) + 10
(+ 10 if Musicians Guild present)
```

Kingmaker as milestone generator:

```
Freeman → … → Duke  ≈  10+15+30+50+100+150+200+250+300 = 905 honour to max rank
(each rank also unlocks build menu — natural "episode" boundaries)
```

## Dead Ends

- **1:1 asset clone** — unnecessary for personal fun; legal noise if repo ever public
- **SH2 crime sim before economy spine** — honour/popularity need granary/tax loop first
- **Starting 3D + full Kingmaker** — Bradbury's own team struggled with scope; rank-gate one tier at a time
