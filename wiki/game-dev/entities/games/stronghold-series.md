---
title: Stronghold franchise — series reference (games, engines, scope)
type: entity
tags: [entity, game, stronghold, firefly, reference, franchise]
keywords: [stronghold, crusader, firefly, unreal, vision-engine, franchise]
related:
  - concepts/stronghold-systems-inventory.md
  - concepts/stronghold-deconstruction.md
  - concepts/scope-tiers.md
  - concepts/vertical-slice-v0.md
  - sources/stronghold-hd-manual-2001.md
  - sources/stronghold-series-wikipedia-2026-06-13.md
  - sources/gamespy-stronghold-2-bradbury-qa-2004.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
  - sources/firefly-about-us-studio-history.md
  - sources/firefly-making-of-stronghold-legends-2018.md
  - sources/firefly-sh2-production-interview-youtube-2026-06-17.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-systems-inventory.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
  - sources/mobygames-stronghold-2-2026-06-13.md
  - concepts/medieval-sim-fun-vs-accuracy.md
  - sources/leiden-medieval-city-builder-accuracy-2020.md
  - sources/unofficial-crusader-patch2-phase-0-audit-2026-06-13.md
  - sources/stronghold-franchise-best-of-research-2026-06-18.md
  - sources/stronghold-4-public-demo-2026-06-24.md
maturity: validated
created: 2026-06-13
updated: 2026-06-24
---

## Relations

- @concepts/stronghold-systems-inventory.md — SH1 buildings, units, economy depth
- @entities/projects/castle-sim.md — hobby implementation (not a clone)
- @sources/gamespy-stronghold-2-bradbury-qa-2004.md — siege/wall design (no GDC postmortem exists)
- @sources/simon-bradbury-stronghold-heaven-sh3-2011.md — scope discipline, SH1 return
- @sources/firefly-about-us-studio-history.md — studio timeline, Definitive Edition success
- @entities/tools/unofficial-crusader-patch2.md — community MIT patch (AIV / balance study)
- @concepts/stronghold-2-systems-inventory.md — **SH2 mechanics depth** (operator clone target)
- @concepts/operator-vision-sh2-personal-clone.md — personal-use north star

Firefly Studios **Stronghold** franchise as design north star — mechanics and feel are fair research; assets and lore are not.

## Narrative

### Developer & genre

**Firefly Studios** (UK) — real-time strategy / castle simulation set in medieval (and spin-off) settings. Player is a lord: build castle, run economy, raise armies, survive sieges. Publisher history includes Gathering of Developers, Take-Two, 2K, Devolver (via Firefly acquisition). [CONFIRMED — Wikipedia 2026-06-13]

### Engine generations

| Generation | Engine | Titles | Perspective | Hobby Tier 1 fit |
|------------|--------|--------|-------------|------------------|
| **1 — 2D isometric** | Proprietary 2D (DirectX 7 era); pre-rendered-style sprites | Stronghold (2001), Crusader (2002), Crusader Extreme (2008), Kingdoms (2012 MMO) | Isometric 2D | **Primary reference** |
| **2 — Early 3D** | Vision Engine (buggy at launch) | Stronghold 2 (2005), Legends (2006) | Full 3D castle | **Operator north star** — @concepts/operator-vision-sh2-personal-clone.md |
| **3 — Later 3D** | New proprietary 3D | Stronghold 3 (2011), Crusader II (2014), Warlords (2021) | 3D, free-angle walls (SH3+) | Out of scope |
| **4 — UE5** | Unreal Engine 5 | Stronghold 4 (announced 2026) | Modern 3D | Watch only |

Stronghold (2001) used **2D isometric** presentation with sprite-based units/buildings — same broad technique class as Age of Empires II contemporaries, not a live 3D camera. [CONFIRMED — Wikipedia, Giant Bomb sysreqs, community pre-render lists]

Sound: Miles Sound System (AIL). Map editor: **real-time** in SH1/Crusader; replaced with still-life editor in SH2. [TENTATIVE — MobyGames group metadata]

### Release timeline (mainline + notable spin-offs)

| Year | Title | Notes |
|------|-------|-------|
| 2001 | **Stronghold** | England, 21-mission combat campaign + economic campaign; The Rat, Snake, Pig, Wolf |
| 2002 | **Stronghold: Crusader** | Middle East, Third Crusade; **8 AI lords**, Skirmish Trail (50 missions), mercenary post |
| 2005 | **Stronghold 2** | 3D; **crime/punishment**, **honour**, jousting, Kingmaker mode; launch bugs → Deluxe |
| 2006 | **Stronghold Legends** | Arthur / Vlad / Siegfried campaigns; dragons, myth units |
| 2008 | **Crusader Extreme** | Crusader + larger armies / extreme mode |
| 2011 | **Stronghold 3** | New 3D engine; non-parallel walls; story sequel |
| 2012 | **Stronghold Kingdoms** | F2P MMO-RTS world map |
| 2014 | **Stronghold Crusader II** | SH3 engine; Crusader sequel; co-op MP |
| 2021 | **Stronghold: Warlords** | China setting; warlords, aesthetics ↔ population |
| 2023 | **Stronghold: Definitive Edition** | SH1 remaster; 500k+ sales reported ~14 months [TENTATIVE] |
| 2024 | **Stronghold Castles** | Mobile; commercial failure reported [TENTATIVE] |
| 2025 | **Crusader: Definitive Edition** | Remaster; new AI, larger maps, co-op |
| 2026 | **Stronghold 4** | UE5; Windows/Steam; **public demo** 2026-06-23 [CONFIRMED — @sources/stronghold-4-public-demo-2026-06-24.md] |

### Game modes (Stronghold 2001 baseline)

From official HD manual [CONFIRMED — @sources/stronghold-hd-manual-2001.md]:

- **Combat campaign** — 21 missions vs four villains
- **Economic campaign / missions** — rebuild kingdom, resource goals, no combat focus
- **Siege missions** — attack/defend historical castles; pure combat
- **Invasion / free build** — sandbox build; invasion optional
- **Multiplayer** — up to 8 (GameSpy era; modern DE uses Steam)
- **Map editor** — real-time; economic, combat, landscape, multiplayer maps

Crusader adds **Skirmish Trail**, **Custom Skirmish** (up to 8 AI lords), **historical campaigns** (Crusader + Arabic).

### Per-title feature deltas (hobby-relevant)

| Feature | SH1 | Crusader | SH2 | SH3+ |
|---------|-----|----------|-----|------|
| Wall draw | Stone/wood, crenellations, towers | Same + desert maps | 3D wall types changed | Free-angle 3D |
| Economy depth | Food chains, popularity, tax | + merc gold rush | + crime, honour, ranks | Varies |
| AI lords | Campaign villains | **8 skirmish personalities** | + Queen, Bishop, Grey | Improved but 3D |
| Siege roster | Ram, tower, catapult, trebuchet, tunnel | + fire ballista | Expanded | Expanded |
| Arabic units | — | Mercenary post | — | In Crusader II |

### Mac play (operator research)

- Legacy discs + GOG HD (older Mac builds)
- **Definitive Edition / Crusader DE** — Windows; CrossOver/Wine path for play research
- Not native Mac for DE as of 2025–2026 [TENTATIVE — verify at playtest]

### Legal boundary

Study **systems** (economy loops, wall placement feel, siege pacing). Do not ship Firefly names, voice lines, campaign plot, or asset rips.

## Snippets

> **Operator target (2026-06-13):** personal **Stronghold 2** clone — mechanics + feel, not Firefly assets. Implementation may stay 2D (Fork A) while layering SH2 honour/crime/kingmaker. See `briefs/GDD-sh2-personal-clone.md`.
