---
title: Stronghold 2 — siege warfare (attack, defense, equipment)
type: concept
tags: [concept, stronghold-2, siege, combat]
keywords: [siege, trebuchet, ladder, ram, breach, engineer]
related:
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/gamespy-stronghold-2-siege-dev-diary-2005.md
  - sources/gamespot-stronghold-2-qanda-2004.md
  - sources/gamespot-stronghold-2-honor-sieges-2004.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-2-military-units.md
  - concepts/stronghold-2-ai-lords.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-military-units-2026-06-17.md
  - concepts/stronghold-2-castle-structures.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/firefly-sh2-production-interview-youtube-2026-06-17.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @sources/gamespy-stronghold-2-siege-dev-diary-2005.md — Bradbury attack pipeline
- @concepts/godot-3d-sh2-architect-spike-plan.md — wall gap QA before siege

## Raw Concept

SH2 siege = **no sword-wall hacking** + **multi-path assault** (breach, scale, tower fight, keep interior). Reference for castle-sim Phase D–E combat.

## Narrative

### Core rule change [CONFIRMED — GameSpy, GameSpot]

Foot troops **cannot** destroy walls with melee. Entry requires:

1. **Siege engines** → breach (engineers may **repair** if defenders control breach)
2. **Ladders / siege towers** → fight **on and along walls**
3. **Rams** → gatehouse focus
4. **Tunnels** → corner tower undermining [CONFIRMED — campaign walkthrough pow8-2]

### Victory condition [CONFIRMED — GameSpot 2004 preview]

Hold **top of main tower** until flag flips — lord kill optional (lord may escape).

### Attack pipeline [CONFIRMED — Bradbury dev diary]

```mermaid
flowchart LR
  A[Siege camp] --> B[Softening fire]
  B --> C[Mantlets + archers]
  C --> D[Moat fill / cat cover]
  D --> E[Ladders or breach]
  E --> F[Wall/tower fights]
  F --> G[Keep interior stairs]
  G --> H[Flag hold win]
```

Alternative: **economic siege** — army camps outside until defender breaks [CONFIRMED].

### Siege equipment roster [CONFIRMED — SH2 Heaven, Steam guide, Fandom]

| Equipment | Built at | Notes |
|-----------|----------|-------|
| **Ladderman** | Barracks (Knight+) | Returns to **siege camp** for free ladder resupply |
| **Mantlet** | Siege camp | Mobile missile soak; 1 engineer |
| **Cat** | Earl+ | Troop cover |
| **Burning cart** | Knight Errant+ | Burns traps/troops |
| **Battering ram** | Royal Champion+ | Slow; needs escort |
| **Siege tower S/L** | Knight Errant / Royal Champion | Tall tower = archer platform |
| **Catapult** | Baron+ | Faster fire, less range than trebuchet |
| **Fire ballista** | Earl+ | Anti-siege / anti-troop |
| **Trebuchet** | Duke+ | Packed on wheels → deploy **immobile**; high arc; **less accurate** than catapult; can hurl **cattle** for disease [CONFIRMED — Fandom] |

**Rank gates** align with Kingmaker table — trebuchet is end-tier fantasy weapon.

### Defense roster [CONFIRMED]

| Defense | Role |
|---------|------|
| **Mangonel** | Tower-mounted; friendly fire risk on walls |
| **Tower ballista** | Long range anti-siege |
| **Arrow slits** | Archer nearly invulnerable |
| **Oil smelter** | 4 engineers; pitch → flaming pots |
| **Pitch ditch / moat** | Delay + kill zone |
| **Man trap, killing pit** | Hidden damage |
| **Rolling logs, rock tipper** | Choke slaughter |
| **War hounds** | Baron+ |
| **Hoardings** | Extended wall fighting space |

### Unit combat notes

Full stat tables → @concepts/stronghold-2-military-units.md. Summary:

| Unit | Siege role |
|------|------------|
| **Swordsman** | Strong melee; slowest — kited by cavalry/missiles |
| **Spearman** | Push ladders; moat labor |
| **Knight** | Mounted rush; 25 honour |
| **Ladderman** | Resupply at siege camp |

**Height advantage:** archers on hills/towers shoot down [CONFIRMED — GameSpot].

### Player strategies [TENTATIVE — walkthroughs + forums]

**Defense:**

- Trebuchets **behind walls** targeting enemy siege camp spawn
- Melee on walls to **push ladders**
- Braziers along wall paths
- Rolling logs in **double-wall kill box**

**Offense:**

- Multiple **siege camps** around estate → trebuchet crossfire
- Catapults + mantlets faster than trebuchets for some walls (pow8-2)
- Fire ballistae clear wall troops before ground advance

### 3D interior combat [CONFIRMED — GameSpot Q&A]

- Keep: **4 fightable levels**; towers: spiral stair fights
- Opens building interiors for combat routing — high dev cost

### castle-sim phased delivery

| Phase | Scope |
|-------|-------|
| **D0** | Grid walls + archer v0 (done) |
| **D1** | Ladders + wall segment occupancy |
| **D2** | Siege camp + catapult placeholder |
| **D3** | Breach + engineer repair |
| **D4** | Trebuchet + flag victory |
| **E** | Keep interior multi-floor (optional) |

### Clone QoL opportunities

- Formation/rally pain was community complaint [TENTATIVE — MobyGames] — group move, rally points
- Trebuchet **immobile after deploy** — clear UI state in Godot
- Ladder **push** interaction — simple physics or delete-on-melee

## Dead Ends

- **Trebuchet on wall** (LOTR fantasy) — not in SH2 [CONFIRMED — FAQ]
- **Low walls like Crusader** — SH2 high walls only
