---
title: Stronghold 2 — castle structures (walls, towers, gatehouses)
type: concept
tags: [concept, stronghold-2, castle, buildings, siege]
keywords: [walls, gatehouse, tower, hoarding, sally-port]
related:
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/stronghold-2-architect-controls.md
  - concepts/stronghold-2-systems-inventory.md
  - concepts/godot-3d-sh2-architect-spike-plan.md
  - sources/sh2-exa-youtube-deep-research-2026-06-17.md
  - sources/sh2-heaven-kingmaker-ranks-2026-06-18.md
  - sources/sh2-heaven-castle-structures-2026-06-18.md
  - sources/sh2-heaven-pow-missions-2026-06-18.md
  - sources/sh2-heaven-campaign-walkthroughs-2026-06-17.md
  - entities/projects/castle-sim.md
  - concepts/stronghold-2-production-buildings.md
  - sources/stronghold-2-heaven-gameinfo-2026-06-13.md
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Relations

- @sources/sh2-heaven-castle-structures-2026-06-18.md — raw Heaven ingest
- @sources/sh2-heaven-kingmaker-ranks-2026-06-18.md — rank gates for stone walls/towers

## Raw Concept

Qualitative + **material cost** reference for SH2 defensive structures. Use for castle-sim wall/tower placement rules and siege damage tiers — numeric HP not published by Firefly.

## Narrative

### Material tiers [CONFIRMED — Heaven cstructures]

| Tier | Unlock (Kingmaker) | Infantry | Siege |
|------|-------------------|----------|-------|
| Wood wall + platform | Freeman | Breakable by foot | Burns easily |
| Single stone | Knight | Blocks infantry | Falls to engines |
| Double stone | Manual stack | Crenellated | Standard siege target |
| Moat + killing pits | Earl | Slows assault | Engineer fill |

### Gatehouse progression

Wood (20 wood) → Small (15 stone) → Medium (30) → Large (50). Larger gates = harder choke but higher stone budget.

### Tower roles

| Tower | Role in clone |
|-------|---------------|
| Lookout | Early vision; no slits — avoid for defense |
| Bastion | Cheap filler |
| Square/Round | Standard archer + siege platform |
| Hoarded variants | + melee protection on parapet; **no treb/cat on top**; fire → downgrade |
| Great | Duke anchor; 4 slits + tower ballista slot |

### Sally port [CONFIRMED]

Disguised wall section (20 stone). Counter-attack or lord escape — castle-sim Phase D+ optional.

### Architect / 3D spike mapping

- **Wall thickness** = stacked segments (auto 3 max + manual)
- **Staircase adjacency rule** — must touch wall for access
- Hoarding = separate mesh state with fire revert

### AI lord castle patterns [TENTATIVE — Nation]

- Barclay: economy fully inside; joined inner/outer wall exploit
- Seren: single-thickness stone gaps
- King: northeast gap until great tower completes

## Dead Ends

- `/gameinfo/castle/*` numbered pages — 404; buildings index is canonical
