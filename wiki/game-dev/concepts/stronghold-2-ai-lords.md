---
title: Stronghold 2 — AI lords (Kingmaker opponents)
type: concept
tags: [concept, stronghold-2, ai, kingmaker]
keywords: [ai-lords, edwin, barclay, skirmish, harassment]
related:
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-2-military-units.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-systems-inventory.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - sources/sh2-heaven-military-units-2026-06-17.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/sh2-mod-ecosystem-scan-youtube-moddb-2026-06-18.md
  - entities/tools/sh2-community-lord-editor.md
  - sources/sh2-community-lord-editor-phase-0-audit-2026-06-18.md
  - sources/sh2-nation-fandom-ai-lords-2026-06-18.md
  - entities/tools/evrey-shc-aiv.md
  - entities/tools/krarilotus-crusader-efficient-ai.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - concepts/stronghold-2-production-buildings.md
  - sources/sh2-heaven-buildings-industry-civilian-2026-06-18.md
  - entities/projects/castle-sim.md
  - concepts/stronghold-franchise-best-of-shelf.md
  - sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md
  - concepts/llm-npc-runtime-ai-shelf.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
maturity: validated
created: 2026-06-17
updated: 2026-06-21
---

## Relations

- @concepts/stronghold-2-kingmaker-strategy.md — player openings vs AI
- @sources/sh2-nation-fandom-ai-lords-2026-06-18.md — Nation + Fandom second pass
- Stronghold Fandom AI mechanics — hard-coded behavior [CONFIRMED]

## Raw Concept

SH2 Kingmaker AI lords are **scripted personalities** (not Crusader `.aic` files). Reference for castle-sim Phase E **LordAI** stubs — economy priorities, harassment cadence, siege composition.

## Narrative

### Engine behavior [CONFIRMED — Fandom + Nation]

- **Hard-coded** decisions; `.aic` files = **castle templates only** (AIV Editor)
- Recruits if **≥200 gold**; buys weapons if **≥400 gold**
- Five cycles: bodyguards → wall defenders → reserves → **harass** → siege
- Harass: estate capture + catapult/fire ballista escorts [CONFIRMED]
- May **buy estate** instead of ranking up
- **No warrior monks** in AI armies [CONFIRMED]
- Simultaneous multi-good market trades (longer intervals than human)

### Lord profiles

#### Edwin [CONFIRMED — Heaven DKZS + Nation]

| Aspect | Behavior |
|--------|----------|
| Economy | Iron, stone, bread/apple/meat; **statues** for honour |
| Defense | Rectangle castle; wall archers |
| Troops | **Spearmen spam** (~50 early waves); armed peasants patrol |
| Siege | ~80 spearmen, 40 peasants, archers, swordsmen; **many laddermen**; occasional catapults |
| Weakness | Weakest lord; granary snipe drops pop; gatehouse weak point |
| Counter | Missiles; axe throwers/crossbows vs spears |

#### Sir Grey [CONFIRMED — Heaven DKZS]

| Aspect | Behavior |
|--------|----------|
| Castle | Medium gatehouse; **round towers + ballista** |
| Economy | Stone/iron; meat/apples; **grapes/wine**; 1–2 statues |
| Harass | Spearmen groups + **2 catapults** periodically |
| Siege | Dozens spearmen, archers, swordsmen; siege camp: **laddermen, 4 catapults, mantlet** |
| Threat | **Swordsmen** high HP — need ballista/catapult |
| Counter | Fire ballista/trebuchet to kill tower ballista; breach then rush |

#### Olaf Grimtooth [CONFIRMED — Heaven Grimbold]

| Aspect | Behavior |
|--------|----------|
| Units | **Berserkers**, **axe throwers** (merc post) |
| Siege | Catapults + ballistae; ladders for berserkers |
| Castle | Circular fort; **war hounds**, killing pits |
| Counter | Pikemen line + archers vs berserkers; archers vs axe throwers at range |

#### The Hammer (Lord Barclay) [CONFIRMED — Nation + Fandom]

| Aspect | Behavior |
|--------|----------|
| Harass | Minimal building raids; occasional horse archers/catapults |
| Siege | Outlaws, crossbowmen, knights; multiple catapults + trebuchets |
| Castle | Most sophisticated; granary/industry inside walls; slow siege build |
| Counter | Crossbow towers; treb breach outer gate; stairwell keep rush |

#### The Queen [CONFIRMED — Nation + Fandom]

| Aspect | Behavior |
|--------|----------|
| Harass | **Horse archer** waves — ~20 archers on tower counters |
| Siege | Berserkers + archers + swordsmen; cats + ~6 catapults |
| Economy | Strong; granary + merc post **outside** wall |
| Counter | Kill horse archers at range; snipe outside economy |

#### The King [CONFIRMED — Nation]

| Aspect | Behavior |
|--------|----------|
| Harass | **None** — siege-only opponent |
| Siege | Spears, pikes, archers, swordsmen; often **never sieges** (no spears in armoury) |
| Castle | Fast build; gap until great tower; second template = moat + sally ports |
| Counter | Treb towers first; cats protect engines; exploit northeast gap early |

#### The Bishop [CONFIRMED — Nation]

| Aspect | Behavior |
|--------|----------|
| Harass | **Macemen** vs wooden/outside buildings |
| Siege | Spear/macemen/crossbow; 1 trebuchet + weak catapults |
| Weakness | **Church outside walls** — lord visit exposes him |
| Counter | Crossbows on walls; treb breach; armed peasants trigger man traps |

#### Sir William [CONFIRMED — Nation]

| Aspect | Behavior |
|--------|----------|
| Harass | Archer groups (easy with wall towers) |
| Siege | Archers, spears, swordsmen; cats |
| Weakness | Granary always outside |

#### Lady Seren [CONFIRMED — Nation]

| Aspect | Behavior |
|--------|----------|
| Harass | **Light cavalry spam** |
| Castle | Worst designs — wall gaps, killing pits only |
| Threat | Low — missile defense trivializes |

#### The Hawk (Pascal) [CONFIRMED — Nation]

| Aspect | Behavior |
|--------|----------|
| Harass | Archers + catapults |
| Siege | Often **broken** — no spears → no ladders/siege |
| Note | Campaign boss pow8-3; Kingmaker lord shares spear-armoury bug |

#### The Bull [TENTATIVE — campaign only]

- PoW ch4 boss ("Kill the Bull"); **no Nation Kingmaker article** found

### Community difficulty tier [TENTATIVE — Nation forums 2023]

Strong → weak: King, Queen, Hammer, William, Hawk, Bishop, Seren, Bull, Olaf, Grey, Edwin. Use as Phase E ordering hint only.

### AI design lessons for castle-sim

| SH2 pattern | Clone adaptation |
|-------------|------------------|
| Harass before siege | Phase E: small raid timer |
| Estate capture priority | Simple flag capture unit order |
| Spear spam (Edwin) | Low honour early aggression difficulty tier |
| Tower ballista (Grey) | Requires player siege engines mid-game |
| Hard-coded not data-driven | Use **JSON lord profiles** for moddability QoL |

### Phase E minimum viable LordAI

1. **Edwin profile** — spearmen waves every N minutes, weak wall
2. **Grey profile** — harass catapults + ballista defense
3. Economy: AI buys estates at honour threshold OR ranks up (coin flip)

**Data stub:** `castle-sim/data/sh2/lord_profiles.json` + `LordProfile` / `LordAIDirector3D` loaders (2026-06-18).

### LLM lord research contrast (Tier 3+ shelf)

@sources/arxiv-2606.29932-saga-civrealm-strategy-agents-2026-07-05.md documents **multi-domain specialist decomposition** (economy / military / diplomacy) under long-horizon sparse reward — useful contrast when JSON lord weights feel too flat, but **not** a replacement for SH2-authentic scripted cycles in Phase E. Brief: gitignored `briefs/research/saga-civrealm-strategy-agent-shelf.md`.

## Dead Ends

- Reverse-engineering SH2 `.exe` AI — use behavioral reimplementation only
- Full 12-lord parity before single-lord fun — ship Edwin first

## Snippets

Forum Kingmaker opener vs King: mounted knights + catapult breach — not representative of early game; AI gets implicit bonuses [TENTATIVE — Reddit complaints].
