---
title: Stronghold franchise — best-of shelf (SH2 baseline)
type: concept
tags: [concept, stronghold, franchise, scope, reference]
keywords: [best-of, stronghold, crusader, warlords, steal-from, sh2-baseline]
related:
  - concepts/operator-vision-sh2-personal-clone.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/stronghold-systems-inventory.md
  - entities/games/stronghold-series.md
  - entities/projects/castle-sim.md
  - concepts/scope-tiers.md
  - concepts/stronghold-2-estates-system.md
  - concepts/stronghold-2-ai-lords.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/stronghold-2-mod-ecosystem-shelf.md
  - sources/stronghold-franchise-best-of-research-2026-06-18.md
  - sources/stronghold-franchise-research-pass2-2026-06-18.md
  - concepts/stronghold-2-kingmaker-strategy.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
  - sources/simon-bradbury-stronghold-heaven-sh3-2011.md
  - sources/stronghold-hd-manual-2001.md
  - sources/stronghold-4-public-demo-2026-06-24.md
  - sources/stronghold-invasion-vs-freebuild-shelf-2026-07-12.md
maturity: validated
created: 2026-06-18
updated: 2026-07-13
---

## Relations

- @concepts/operator-vision-sh2-personal-clone.md — **SH2 is baseline**, not SH1/Crusader reskin
- @concepts/stronghold-2-systems-inventory.md — what we are already building
- @entities/games/stronghold-series.md — franchise timeline

## Raw Concept

Curated **steal / defer / skip** matrix across Firefly Stronghold titles. Goal: **best-of-series** personal sim — honour, crime, kingmaker, 3D architect from SH2, plus high-identity picks from siblings that SH2 lacked or did worse.

## Narrative

### Design rule

| Rule | Rationale |
|------|-----------|
| **SH2 skeleton first** | Popularity, honour, crime, estates, kingmaker ranks, lord activities, SH2 siege rules |
| **Steal mechanics, not setting** | No Crusader desert reskin, no Warlords East Asia, no Legends dragons — extract systems |
| **Workshop > mercenary gold** | Crusader merc post breaks weapon-chain fantasy — **BO2: capped emergency levy only** |
| **Tight maps** | Bradbury + operator pacing — avoid Crusader Extreme 10k-unit scale |
| **Moddable AI aspiration** | Crusader AIV/UCP2 is north star for lord director; SH2 dat editor informs JSON |

---

### Verdict matrix

**Legend:** **Steal** = plan for castle-sim · **Later** = post-MVP · **Optional** = mode flag · **Skip** = off identity or bad design

#### Stronghold (2001) / Definitive Edition

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| Fear factor (gardens ↔ gallows, efficiency ↔ pop ↔ troop damage) | **Skip** | — | **Operator BO1:** crime loop only — no SH1 fear buildings |
| Moat, pitch ditch, killing pit | **Steal** | B | SH2 kingmaker unlocks moat/pitch late — ensure full trap roster in clone |
| Unit stances, patrol, fortify, Ctrl groups | **Steal** | B | SH2 has some; SH1 manual is clearest spec |
| Siege-only attack/defend scenarios | **Optional** | C | Historical castle scenarios — content mode |
| Economic campaign (no combat) | **Optional** | C | SH2 Path of Peace covers similar |
| Real-time map editor | **Later** | D | Dev/content tool; SH2 editor weaker |
| SH1 DE skirmish AI | **Skip** | — | Never existed; Crusader owns skirmish |

#### Stronghold: Crusader (2002) / Crusader DE

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| **8 skirmish AI personalities** (castles + aggression) | **Steal** | C | SH2 lords exist but AI **less moddable**; `lord_profiles.json` + AIV-style castle templates |
| **Lord binks** (video taunts / ally requests) | **Later** | D | SH2 removed; CR2 restored — placeholder: advisor panel + portrait reactions |
| Custom skirmish (lords, alliances, start gold/stock) | **Steal** | C | Extend Kingmaker lobby |
| Skirmish Trail (linked missions) | **Optional** | D | Content pipeline, not engine |
| Mercenary post (gold → instant Arab units) | **Skip (retail meta)** | — | **Operator BO2:** capped **emergency levy** only — `data/sh2/emergency_levy.json` |
| Assassin (wall climb), horse archer harass | **Later** | C | SH2 has thieves/cat; assassin = distinct harass fantasy |
| Oasis / scarce farmland map design | **Optional** | C | Map authoring pattern |
| Crusader DE: co-op vs AI, larger maps, 20 lords | **Later** | E | Multiplayer milestone |
| UCP2 / AIV ecosystem | **Steal (patterns)** | C | @concepts/stronghold-modding-ecosystem-shelf.md — AI castle files |

#### Stronghold 2 (2005) — baseline [CONFIRMED in build plan]

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| Honour + kingmaker ranks | **Steal** | A | Core identity |
| Crime / punishment / courthouse | **Steal** | A | Core identity |
| 8-category popularity panel | **Steal** | A | Core identity |
| Estates + carter logistics | **Steal** | B | @concepts/stronghold-2-estates-system.md |
| 3D architect (Space), wall siege-only breaches | **Steal** | A | Fork B spike |
| Lord activities (joust, feast, church, Lady) | **Steal** | B | Honour sources |
| Gong / falconer / monastery | **Steal** | B | Popularity + honour |
| Still-life map editor | **Skip** | — | Prefer SH1-style real-time editor later if any |

#### Stronghold Legends (2006)

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| **Estate production picker** on capture | **Steal** | B | **Upgrade SH2** — map-fixed estate goods → player chooses industry |
| Streamlined estate reset + carter | **Later** | B | QoL for multi-estate |
| King of the Hill mode | **Optional** | E | MP variant |
| Dragons, myth heroes, factions | **Skip** | — | Wrong tone for realistic medieval clone |
| Legends Trails | **Optional** | D | Content |

#### Stronghold 3 (2011)

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| **Free-angle / non-grid walls** | **Later** | B+ | Organic castles; validate in 3D architect after axis-aligned MVP |
| **Hovel quality ∝ distance from keep** | **Steal** | B | Housing tier visual + pop cap — Warlords expanded to 6 tiers |
| Night siege fog-of-war | **Optional** | D | **Event-driven** night raid missions, not 24h clock (@sources/simon-bradbury-stronghold-heaven-sh3-2011.md) |
| Diseased animal trebuchet ammo | **Optional** | D | Fun siege variant; morale/disease hook |
| Havok wall crumble juice | **Later** | C | VFX polish |
| Instant build (no worker walk) | **Skip** | — | Kills sim fantasy |
| Removed crime / no skirmish at launch | **Skip** | — | Anti-patterns |

#### Stronghold Crusader II (2014)

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| Lord binks + personality UI | **Later** | D | Same as Crusader row |
| Co-op skirmish | **Later** | E | With MP-AI enabler class feature |
| Sandbox / free build naming & UX | **Steal** | C | SH2 free build + clearer "no enemies" sandbox — **not** a replacement for invasion pacing [@sources/stronghold-invasion-vs-freebuild-shelf-2026-07-12.md] |

#### Stronghold: Warlords (2021)

| Feature | Verdict | Phase | Notes |
|---------|---------|-------|-------|
| **Neutral capturable warlords** + edicts | **Steal** | C | **Best upgrade to SH2 estates** — neutral villages with perks (tax boost, raid aid, fear bonus) |
| Diplomacy points over time | **Later** | C | Currency for edicts; simpler: honour cost per edict |
| **Housing quality tiers** (6 levels) | **Steal** | B | Extends hovels; ties to keep distance + aesthetics |
| Clothing / tea luxury chains | **Later** | C | Extra popularity sources beyond ale — defer until bread/ale stable |
| Aesthetics ↔ population mood | **Later** | C | Decoration buildings (SH1 fear "good" side + Warlords cosmetics) |
| Military Academy hero abilities | **Optional** | D | Bounded cooldown abilities vs Legends dragons |
| East Asian factions / setting | **Skip** | — | Mechanics only |

#### Spin-offs / remasters

| Title | Verdict | Notes |
|-------|---------|-------|
| Crusader Extreme (10k units) | **Skip** | Pacing / scope |
| Stronghold Kingdoms MMO | **Skip** | Different genre |
| SH / Crusader DE remasters | **Steal (QoL)** | Larger maps option, co-op trails, UI clarity — not 2D pivot |
| Stronghold 4 (announced UE5) | **Watch** | Revisit at release |

---

### Recommended "best-of" bundle for castle-sim

Priority order after SH2 core sim is playable:

```mermaid
flowchart LR
  subgraph core [Phase A-B SH2 baseline]
    POP[Popularity 8 categories]
    HON[Honour + Kingmaker]
    CRM[Crime loop]
    EST[Estates + carter]
    ARC[3D architect]
  end
  subgraph cherry [Phase B-C franchise cherry-picks]
    EL[Emergency levy cap]
    EP[Estate production picker]
    HT[Housing tiers by keep distance]
    AI[Crusader-grade lord personalities]
    WL[Warlord edicts on neutrals]
  end
  subgraph late [Phase D-E optional]
    NB[Night siege scenarios]
    BK[Lord binks / advisor drama]
    CO[Co-op vs AI]
  end
  core --> cherry --> late
```

| # | Pick | From | Why |
|---|------|------|-----|
| 1 | Estate **production choice** on capture | Legends | **BO3 locked** — player agency vs map-fixed SH2 villages |
| 2 | **Emergency levy** (capped) | Crusader-inspired | **BO2 locked** — honour/gold harass packs, not merc economy |
| 3 | **Housing tiers** by keep proximity | SH3 / Warlords | Visual progression + pop quality |
| 4 | **Warlord edicts** on neutral map nodes | Warlords | Estates as strategic objectives |
| 5 | **Crusader AI depth** + castle templates | Crusader / UCP2 | @concepts/stronghold-crusader-ai-modding-shelf.md |
| 6 | **Unit stances + fortify** | SH1 | Wall defense feel |
| 7 | Lord **advisor reactions** (binks-lite) | Crusader II | Text/portrait first |
| 8 | **Free-angle walls** (limited) | SH3 | After axis MVP |
| 9 | Night **scenario** flag | SH3 | **BO4 locked** — event missions only |
| 10 | Co-op skirmish vs AI | Crusader DE | Late multiplayer |

---

### Explicitly NOT in best-of (protect SH2 identity)

- Crusader **mercenary gold army** as primary recruitment (**BO2:** emergency levy only)
- SH1/Crusader **fear factor** buildings (**BO1:** crime-only popularity)
- Legends **dragons / myth units**
- SH3 **instant placement** without workers
- Crusader Extreme **massive unit counts**
- Replacing honour/crime with SH3-simplified honour-only
- 2D isometric pivot (Fork B locked)

---

### Mapping → existing castle-sim / briefs

| Best-of item | Current artifact |
|--------------|------------------|
| Lord personalities | `data/sh2/lord_profiles.json` |
| Balance presets | `data/sh2/balance_presets.json` (retail + community + Nevikov-inspired) |
| Estates + production picker | @concepts/stronghold-2-estates-system.md — **BO3** |
| Emergency levy | `castle-sim/data/sh2/emergency_levy.json` + `briefs/story-032-franchise-cherry-picks.md` |
| Crusader AI study | @concepts/stronghold-crusader-ai-modding-shelf.md |
| Pass-2 research | @sources/stronghold-franchise-research-pass2-2026-06-18.md |

---

### Operator decisions — **LOCKED 2026-06-18**

| ID | Decision |
|----|----------|
| **BO1** | **Crime only** — no fear factor |
| **BO2** | **Yes** — capped emergency levy (`emergency_levy.json`), not merc post meta |
| **BO3** | **Yes** — estate production picker on capture (Legends) |
| **BO4** | **Yes** — night siege scenario flag only |
| **BO5** | **No** fantasy heroes — bounded lord abilities OK later |

Brief: gitignored `briefs/story-032-franchise-cherry-picks.md`

## Dead Ends

- "Remake Crusader in 3D" — operator favourite is SH2; Crusader features are **grafts**
- Ingesting every SH3 feature because Firefly called it "ultimate Stronghold" — launch reviews + missing skirmish prove caution
