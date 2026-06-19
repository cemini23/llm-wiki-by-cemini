---
title: Stronghold franchise research pass 2 — strategy, mods, interviews (2026-06-18)
type: source
tags: [source, stronghold, franchise, youtube, github, strategy, interview]
keywords: [kingmaker, ucp, aiv, warlords, bradbury, modding]
related:
  - concepts/stronghold-franchise-best-of-shelf.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-github-ecosystem-shelf.md
  - sources/stronghold-franchise-best-of-research-2026-06-18.md
  - sources/sh2-heaven-kingmaker-strategy-2026-06-17.md
  - sources/sh2-youtube-parity-watchlist-2026-06-17.md
  - sources/sh2-kingmaker-youtube-watchlist-2026-06-19.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
  - sources/firefly-sh2-production-interview-youtube-2026-06-17.md
  - entities/projects/castle-sim.md
  - sources/evrey-shc-aiv-phase-0-audit-2026-06-19.md
  - sources/krarilotus-efficient-ai-phase-0-audit-2026-06-19.md
read_status: read
source_type: web-scan
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Pass-2 harvest after operator locked BO1–BO5 on `@concepts/stronghold-franchise-best-of-shelf.md`. Focus: **Kingmaker strategy depth**, **Crusader AI/mod toolchain**, **Firefly dev interviews**, **YouTube Kingmaker walkthroughs**, **SH2 GitHub reverse-engineering**.

## Narrative

### Kingmaker strategy — Matt Logan Heaven guide [CONFIRMED — full scrape 2026-06-18]

Source: https://stronghold2.heavengames.com/strategy/kingmakertips/

| Topic | Takeaway for castle-sim |
|-------|-------------------------|
| Opening | 2–3 stockpiles, 5 wood/apple/dairy, 4 wheat + mill + 6 bakers, barracks + archers on keep + braziers |
| Popularity automation | Double food (+8), church +6, entertainment +10, cruel tax –12/–16 — net >50 |
| Gold | Tax + market sell excess + estate taxes; **buy weapons** instead of full workshop chains (PvE meta) |
| Estates | Move **crime-prone industries** (innkeeper, vintner) to secondary estates; 10+ carter posts late |
| Crime | Prefer **stocks** over executioner (buggy); guard posts at granary/treasury |
| Mercenary | Author builds **50+ horse archers** — retail meta; clone uses **capped emergency levy** only (BO2) |
| Quirks | Carter auto-routes skip luxuries; stockpile full blocks production; granary does not |

### YouTube — Kingmaker / tutorial shelf [TENTATIVE — metadata only]

| Video ID | Title | Use |
|----------|-------|-----|
| vy4546WfkCg | SH2 Steam Edition Tutorial | Controls + economy intro |
| 1NDb5LxGY1I | Beginners Guide — strong economy | Build order reference |
| MD8MfO3BuZw | Kingmaker Freeman→King, Three Bridges | Long-form PvE, riding archers |
| fJ8wjeMdz9k | Kingmaker Part 2 | Castle management pacing |
| 2xcDg5RscRc | Kingmaker mode overview | Lobby / mode UX |
| P0SrfrucRTo | Multiplayer versus | MP estate fights |
| DBD-20osfiA | Kingmaker India map | Map-specific choke strategy |

Prior parity batch: @sources/sh2-youtube-parity-watchlist-2026-06-17.md (campaign/free build).

### Firefly dev interviews [CONFIRMED — web summaries]

| Source | Claim | Clone relevance |
|--------|-------|-----------------|
| Bradbury SH3 Heaven 2011 | SH2 overreach; crime out in SH3; tight maps | Validates SH2 baseline + BO1 crime-only |
| Bradbury Warlords (TheGamer, TechRaptor, Prima) | Warlords = estate successor; diplomacy slower cycle; Bradbury soft spot for **Legends** | BO3 estate picker + warlord edicts later |
| Firefly Making Of Crusader (site) | Crusader = faster RTS + unique economy | Skirmish AI north star, not economy model |
| WorthPlaying Kingmaker 2005 | Estates + honour promotions explained pre-launch | Estates design intent |

### Crusader mod / AI toolchain [CONFIRMED — GitHub]

| Repo | License | Steal for castle-sim |
|------|---------|----------------------|
| [UnofficialCrusaderPatch2](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2) | MIT | AIC editor, AI swapper, balance — **lord director patterns** |
| [Evrey/SHC_AIV](https://github.com/Evrey/SHC_AIV) | — | Castle template quality bar; 128 AIV replacement study |
| [Krarilotus/Stronghold-Crusader-efficient-AI](https://github.com/Krarilotus/Stronghold-Crusader-efficient-AI) | — | Build-order documented castles per lord |
| [Monsterfisch/StrongholdsOfConquest_](https://github.com/Monsterfisch/StrongholdsOfConquest_) | — | Historical castle ↔ AIV mapping |
| [NMme/CrusaderAIManager](https://github.com/NMme/CrusaderAIManager) | — | JSON paths for speech/binks — advisor UI later |
| [Sh0wdown/UnofficialCrusaderPatch AI+](https://github.com/UnofficialCrusaderPatch/UnofficialCrusaderPatch2/issues/486) | — | AI level tiers without breaking personality |
| Crusader DE **AIVE** (ModDB) | — | Visual `.aivjson` editor — if we import AIV-style templates |
| [Budschie/StrongholdWarlordsModdingHelper](https://github.com/Budschie/StrongholdWarlordsModdingHelper) | — | Warlords AI override tooling — edict/castle study |

**Crusader DE note:** Steam forums report vanilla DE skirmish AI weak vs **UCP** — community treats UCP as required for skirmish [TENTATIVE].

### SH2 GitHub (unchanged high value)

| Repo | Use |
|------|-----|
| [Eren121/Stronghold](https://github.com/Eren121/Stronghold) | SiegeExporter `.s2m`, unit pointer map |
| [Ald0s/Stronghold2-Trainer](https://github.com/Ald0s/Stronghold2-Trainer) | Player struct offsets — balance validation |
| [Jpnock/Stronghold2-MP-AI](https://github.com/Jpnock/Stronghold2-MP-AI) | MIT MP-AI patch |
| [EBoespflug/stronghold-maps](https://github.com/EBoespflug/stronghold-maps) | Kingmaker map playtest |

### SH2 Steam guides [TENTATIVE]

| Guide | Notes |
|-------|-------|
| Steam 1163315277 units | Trebuchet at siege spawn points; laddermen weak; moat estate glitch |
| Steam 2194134092 achievements | Duke start for testing; custom small-enemy maps |

## Snippets

Matt Logan popularity target: Church +6, Food +8, Entertainment +10, Tax –16.

UCP Krarilotus AI: Saladin uses siege towers + assassins effectively on balanced maps.

## Dead Ends

- Importing Crusader `.aic`/`.aiv` binaries into Godot — study only; JSON lord profiles are source of truth
- Adopting Matt Logan 50-horse-archer merc meta — conflicts with BO2 capped levy
