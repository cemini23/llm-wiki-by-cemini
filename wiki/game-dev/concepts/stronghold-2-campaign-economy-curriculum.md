---
title: Stronghold 2 — campaign economy curriculum (tutorial spine)
type: concept
tags: [concept, stronghold-2, campaign, tutorial, economy]
keywords: [path-of-peace, path-of-war, tutorial, missions]
related:
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-popularity-model.md
  - concepts/stronghold-2-crime-punishment-loop.md
  - concepts/stronghold-2-estates-system.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-pow-missions-2026-06-18.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md — mission objectives source
- @concepts/operator-vision-sh2-personal-clone.md — personal clone skips Firefly story but **keeps teaching order**

## Raw Concept

SH2 campaigns are a **designed tutorial** — Path of Peace teaches economy/lord life; Path of War teaches combat/siege. Map to castle-sim **story-0xx tutorial missions** without copying plot.

## Narrative

### Path of Peace — system unlock ladder [CONFIRMED — popmissions + walkthroughs]

| Ch | Mission | Systems taught | Walkthrough beats |
|----|---------|----------------|-------------------|
| 1 | Warning Beacon | Granary, apple farm, saw pit, hovel | Farms **adjacent to granary**; pop may dip until first harvest |
| 2 | Feast for Honor | Hunter, veg/pig → Lord's Kitchen, **feasts**, granary variety honour | Double rations → +2 honour/mo; first feast ~18 honour (pigs only) |
| 3 | Harbury Keep | **Second estate**, quarry, ox, **carter**, well/fire | 80 stone via carter; workers estate-bound; **+10 gold/mo** per secondary estate |
| 4 | Wolf Hunt | Barracks, archers, gong pit | Ale + honour production under pressure |
| 5 | Aid Sir William | **External NPC granary** feeding 24 months | Long-horizon food stability |
| 6 | Rats & Gong | **Falconer**, multi-estate gong/rats, carter food aid | Pause start; buy food; 3 gong + 4 falconer each estate |
| 7 | Outlaw Camp | Military vs camp | — |
| 8 | Sir William's Honour | **300 honour** — church, fair, bedchamber, royal foods | Mass = 150 honour; 4 food types in granary |
| 9 | Sword Production | **Industry race** vs AI Edwin | Blacksmith chain |
| 10 | Defend Sir Grey | Defense + ally | — |
| 11 | Edwin's Estate | **Pop recovery** (starts ~40 pop), cleanup | 80 pop + 100 honour in 40 months |
| 12 | Kingly Feast | **Royal food stockpile** + 400 honour | Joust 6mo build + 6mo tournament |

### Path of War — full mission roster [CONFIRMED — pow walkthrough scrape 2026-06-18]

See @sources/sh2-heaven-pow-missions-2026-06-18.md for complete 19-mission table. Summary ladder:

| Ch | Missions | Focus | Economy/combat beat |
|----|----------|-------|---------------------|
| 1 | pow1 | Lord micro | Horse combat tutorial |
| 2 | pow2-1..3 | Flanders return | Bridge, cloth chain, clear map |
| 3 | pow3 | First siege | Ladder assault on William's camp |
| 4 | pow4 | Borderlands | Multi-side-quest + kill Bull |
| 5 | pow5-1..2 | Monastery | Kill Olaf; rebuild monastery |
| 6 | pow6-1..2 | Olaf arc | **Control 6 estates**; wipe enemies |
| 7 | pow7 | Abbey defense | Honour/estate buy; ale market vs brew |
| 8 | pow8-1..3 | Hawk's Nest | Rescue William; kill 3 lords; kill Hawk |
| 9 | pow9 | Treachery | Kill Barclay |
| 10 | pow10 | Abbey siege | Kill Seren |
| 11 | pow11-1..2 | Betray William | Capture Upwey; kill William |
| 12 | pow12 | Coronation race | Kill King |

### Path of War — sampled economy beats [CONFIRMED — walkthroughs]

| Ch | Focus | Economy note |
|----|-------|--------------|
| 1 | Horse lord micro | None |
| 2-1 | Bridge rebuild | Saw/quarry/ox; 80 apples start |
| 2-2 | Cloth for Flanders | Sheep/weaver; **no treasury** — sell later |
| 2-3 | Olaf defense | **Market sells cloth** → mass spearmen; wooden palisade choke |
| 3 | Siege assault | Pre-built army; Ctrl+0–9 groups |
| 4 | Multi-quest | Side objectives before Bull fight |
| 6-1 | Estate race | Six estates + triple kill quests |
| 7 | Abbey defense | 300 honour start; **buy estate**; ale buy vs brew; tax/ration pairing |
| 8-2 | Tunnel siege | Corner tower undermining |
| 11 | Treachery | Full toolkit; capture estate |
| 12 | Kill King | Siege engines; beat rival lords to keep |

### Cross-campaign design patterns [CONFIRMED]

1. **Carry-over saves** — goods/pop persist (PoP especially)
2. **No market early** — forces basic chains before trade
3. **Scripted fires/events** — pop3 end fire (optional skip in clone)
4. **Time limits** — pop3 68mo, pop6 24mo, pop11 40mo
5. **Allied estates** — pop6 Boorswell partner needs carter support

### castle-sim tutorial mapping (proposed)

| castle-sim story | SH2 equivalent | Min systems |
|------------------|----------------|-------------|
| story-010 granary | PoP ch1 | stockpile, granary, one food |
| story-011 hunters | PoP ch2 | second food, honour tick |
| story-020 estates | PoP ch3 | carter + secondary flag |
| story-025 crime | PoP ch6 | gong, falconer, guard |
| story-028 feast | PoP ch8/12 | lord's kitchen, joust |
| story-040 siege | PoW ch3 | ladders + archers |

Operator clone can ship **PoP-equivalent sandbox scenarios** without campaign VO.

### Walkthrough UX lessons for Godot

- **Pause-friendly** — PoW/PoP assume pause for build planning
- **Buy food emergency** — pop6 opens market buy when partner estate starving
- **Don't block gate paths** with hunters (pop2)
- **Second stockpile** for flexibility (pow2-2)

## Snippets

PoP ch3 carter trick: post near estate border; route **20 stone continuously** — carters "magically" pull from stockpile without walking to each quarry.

PoP ch6 opening: buy **200 wood, 50 apples, 50 meat** immediately after pause.

## Dead Ends

- Replicating **Sir William NPC AI** feeding — scope creep; use simple ally granary drain test instead
- Full 24-chapter clone campaign — use Kingmaker + free build after tutorial spine
