---
title: Stronghold 2 — Kingmaker strategy & opening builds
type: concept
tags: [concept, stronghold-2, strategy, kingmaker]
keywords: [kingmaker, opening, tax, popularity, market, ai]
related:
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-popularity-model.md
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-estates-system.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-2-campaign-economy-curriculum.md
  - concepts/stronghold-2-military-units.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @concepts/stronghold-2-systems-inventory.md — rank unlock spine
- @sources/sh2-heaven-kingmaker-strategy-2026-06-17.md — Matt Logan cheat sheet

## Raw Concept

**Kingmaker** = SH2 skirmish sandbox (up to 7 AI). Natural **endgame mode** for personal clone. This page captures **PvE opening strategy**, popularity/tax automation, and AI behavior notes for sim tuning.

## Narrative

### Mode rules [CONFIRMED — Fandom, SH2 Heaven]

- Last lord standing; home estate + neutral **village estates**
- **Honour → rank promotions** unlock buildings/units — full table @sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
- Fallen players lose all buildings; villages transfer to killer
- Peasant supply regenerates; map caps total population

### Opening priorities [CONFIRMED — Kingmaker tips + walkthroughs]

```
1. Defensive choke (moat/wall) if map demands
2. Stockpile cluster → granary → food chain (apple/dairy/wheat/baker)
3. Woodcutters + hunters → double rations (+8 food pop)
4. Barracks + archers on keep + braziers
5. Castle services: gong, falconer, courthouse, stocks, guard posts
6. Market + honor buildings (kitchen, bedchamber, joust)
7. Rank up when honour allows — don't neglect military before first AI raid
```

### Popularity "automation profile" [CONFIRMED — Matt Logan]

Experienced players target **max tax** with offsetting generosity:

| Factor | Target | Pop effect |
|--------|--------|------------|
| Food | Double rations | +8 |
| Ale | High consumption (inn chain) | up to +8 |
| Church | Special/Exulted mass | up to +8 |
| Entertainment | Joust + Fair | +10 combined |
| Gong/Crime/Rats | Managed | 0 |
| Tax | Cruel / Extra Cruel | –12 to –16 |

**Net:** popularity >50 with **1.25–1.5 gold/peasant/month** tax income.

castle-sim: expose as **preset buttons** ("Kingmaker economy") not manual spreadsheet.

### Gold strategy [CONFIRMED — multiple]

| Source | Notes |
|--------|-------|
| Tax | Requires **treasury**; tax office in campaign |
| Market | Sell excess stone/wood/food/luxury |
| Estates | Secondary estate tax (lower rate) |

**Weapon buying:** many players skip fletcher/poleturner chains — buy weapons when market available [TENTATIVE — Matt Logan PvE guide prefers market weapons over workshops].

**Emergency levy (castle-sim):** honour/gold capped packs — see `data/sh2/emergency_levy.json`; **not** 50+ merc horse archer meta.

### Military meta (PvE) [TENTATIVE — forums + guides]

| Unit | Role |
|------|------|
| Archers on keep | Core defense; elevation matters |
| Horse archers | Raiding, estate capture — **retail:** merc post spam; **clone:** capped emergency levy only (BO2) |
| Knights (mounted) | Late-game rush lord kill |
| Crossbowmen | Wall defense vs armored attackers |

**AI harassment:** raid groups + estate capture; may bring catapults/fire ballistae [CONFIRMED — Fandom AI mechanics].

### AI lord notes [TENTATIVE — HeavenGames forums]

| Lord | Behavior sketch |
|------|-----------------|
| **The Hammer (Barclay)** | ~50 wall archers; trebuchet sometimes; foot knights |
| **The Queen** | Aggressive estate raids (horse archers); lighter wall defense |
| **Sir William / Bishop / Grey** | No merc post — different unit mix |
| **The King** | Plate units; counters siege with pikes/swords |

AI is **hard-coded**, not Crusader-style `.aic` modding [CONFIRMED — Fandom].

### Campaign vs Kingmaker differences [CONFIRMED]

- Campaign missions: scripted objectives, carry-over goods, **pause** for setup
- Kingmaker: no events; estate flags only in map editor
- Ch3 Peace: **secondary estates** introduced — separate pop on estate flag click

### castle-sim mapping

| SH2 Kingmaker | castle-sim today | Story hint |
|---------------|------------------|------------|
| Rank-gated build menu | All buildings keyboard | Kingmaker rank service |
| 8-factor popularity | Single HUD line | story-031 UI |
| Market weapon buy | No market | Phase B |
| AI raids | No AI lord | Phase E |
| Estate capture | N/A | Phase E |

### Estate outsourcing [CONFIRMED — Matt Logan pass2]

Move **innkeeper/vintner** to secondary estates — higher crime recidivism on primary [@sources/stronghold-franchise-research-pass2-2026-06-18.md].

### QoL lessons for clone

- **Auto-sell thresholds** when stockpile full (community wish — not in SH2)
- **Stocks over executioner** — faster rehab, less bug surface
- **Pause (P)** essential for RTS/sim hybrid — add early in 3D controller

## Dead Ends

- Chasing **ranked MP meta** — operator clone is solo; PvE openings sufficient
- Starting at **Freeman** vs pre-ranked Duke — difficulty option only
- Cloning Matt Logan **50+ horse archer merc** opening — conflicts with BO2 emergency levy cap
