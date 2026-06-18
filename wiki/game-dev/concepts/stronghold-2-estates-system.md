---
title: Stronghold 2 — estates & carter logistics
type: concept
tags: [concept, stronghold-2, estates, economy]
keywords: [estates, carter, village, multi-base]
related:
  - concepts/stronghold-2-economy-storage-chains.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-systems-inventory.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/gamespot-stronghold-2-honor-sieges-2004.md
  - concepts/stronghold-2-campaign-economy-curriculum.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - entities/projects/castle-sim.md
maturity: validated
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- @concepts/stronghold-2-economy-storage-chains.md — storage caps per estate
- Path of Peace ch3 walkthrough — first secondary estate tutorial

## Raw Concept

**Estates** extend SH2 from single-castle sim to **multi-node economy** on one map — critical for Kingmaker scaling and late campaign. Carter posts are the **manual/auto logistics glue**.

## Narrative

### Estate types [CONFIRMED — walkthroughs, Fandom]

| Type | Control | UI |
|------|---------|-----|
| **Primary (castle)** | Player HQ | Main popularity panel, immigration |
| **Secondary castle** | Player/allegiance | Own stockpile/granary; flag shows pop |
| **Neutral village** | AI / purchasable | Produce goods; **100 gold + honour** to buy [CONFIRMED] |

Unused or defeated **castle estates** revert to **village estates** in Kingmaker.

### Secondary estate rules [CONFIRMED — pop3 walkthrough]

- Self-sufficient workers, granary, stockpile
- **Popularity on flag click** — not on main panel
- May need **food gifts** from primary when struggling
- **Gong/rats/crime** on main estate only for panel penalties [CONFIRMED — Stronghold Nation popularity guide]

### Carter post logistics [CONFIRMED — Kingmaker tips + walkthroughs]

**Endpoints:** stockpile, granary, lord's kitchen, armoury (any estate → same building type elsewhere).

**Auto-routes (typical):** apples, wood, stone, iron, pitch [CONFIRMED — Matt Logan quirks list].

**Manual-only:** luxury goods — pork, candles, wine, cloth, etc. Player must set routes.

**Scale:** competitive Kingmaker → **10+ carter posts** per productive estate hauling to primary.

### Strategic outsourcing [CONFIRMED — Kingmaker tips]

Move to villages:

- Bulk food (apples, wood, bread)
- **High-crime industries** (innkeeper, vintner)
- Stone/iron production with ox tether near village stockpile

Primary estate → **military + honor + market hub** only.

### Honour & gold from estates [CONFIRMED]

- Village purchase: **100 gold** (+ honour gate in missions)
- Estate tax income lower than primary cruel tax
- Royal food chains on estates need **lord's kitchen on that estate** for feasts

### AI estate behavior [CONFIRMED — Fandom AI]

- AI **buys neutral estates** vs spending honour on rank (tradeoff)
- Garrisons on estate flags; raiding parties to **steal villages**
- Some lords rush **Duke** regardless of start [TENTATIVE]

### Campaign examples [CONFIRMED — walkthroughs]

- **PoW ch7:** buy Quincetown (300 honour start) — market buy wood/stone; ale purchase vs brewing
- **PoP ch3:** restore ruined second castle — carter intro
- **PoP ch8:** honor mission for Sir William — luxury chain on primary

### castle-sim implementation sketch

```
EstateManager
  - primary_id
  - villages: { id, owner, production_tags, garrison }
CarterService
  - routes: [{ from, to, good_type, auto? }]
  - tick: move loads (visual cart optional story-026)
```

**Phase E** — defer until single-estate popularity/honour stable.

Minimum viable estate v1:

- One neutral village buying with honour
- Single carter route (wood → primary stockpile)
- Separate pop counter on village flag

### UX pain points to fix in clone [INFERRED]

- Manual luxury routing is tedious — **route templates** ("send all wine home")
- Stockpile full on estate stalls remote industry — alert when export blocked
- Cannot inspect remote stockpile except via carter panel [CONFIRMED — pop3]

## Dead Ends

- **Estates before Kingmaker rank spine** — honour economy must work on one castle first
- Full map editor estate flags — out of scope for castle-sim v1
