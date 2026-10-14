---
title: GDC — Total War Warhammer siege AI (reference)
type: source
tags: [source, gdc, siege, ai, total-war]
keywords: [gdc, siege, ai, total-war, castle, grand-tactical]
related:
  - concepts/rts-siege-ai-reference.md
  - concepts/stronghold-systems-inventory.md
  - sources/gdc-kingdoms-and-castles-postmortem-2019.md
read_status: read
source_type: conference-talk
source_url: https://gdcvault.com/play/1023038/Have-Fun-Storming-the-Castle
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/rts-siege-ai-reference.md — distilled Tier 2 shelf

## Raw Concept

GDC 2016: **"Have Fun Storming the Castle! Siege Battle AI in Total War: Warhammer"** (Creative Assembly) — high-level siege AI for hundreds vs hundreds on walled settlements.

## Narrative

### Provenance

- GDC Vault: play/1023038 (slides free; video members)
- EGX Rezzed 2016 recap video cited on Total War forums
- Community deep-dive: [TW Center AI presentation thread](https://www.twcenter.net/threads/ai-presentation-issues.726953/) [TENTATIVE — secondary, not official transcript]

### Problem statement [CONFIRMED — GDC blurb]

Field-battle AI does not scale to **massive siege**: attackers/defenders need **roles, responsibilities, reactions** at fortification scale — "complex machine" not single blob charge.

### CA design goals (siege) [TENTATIVE — forum recap of talk]

Five stated project goals for Warhammer sieges:

1. Fast, high-intensity battles
2. Single primary attack direction (focused assault)
3. Battle centered on **walls**
4. Quick resolution once breach achieved
5. Press defender quickly and broadly

**Design tradeoff:** pacing/fantasy over simulation depth — informs what **not** to copy for Stronghold-like slow economy sieges.

### Architecture notes [TENTATIVE — forum recap]

| System | Role |
|--------|------|
| **Grand tactical analyzer** | Field battles — assigns detachment objectives |
| **Siege-specific planner** | Simpler pipeline: breach walls → take victory point (no full GTA in sieges per recap) |
| **Reserve pool** | Failed assault routes recycle units to new tactics (tower destroyed → reassign) |
| **Perimeter map** | 2D wall perimeter for defender containment |
| **Tactic options (attacker)** | Assault walls, assault gates, breach walls; **no** long "hold back and bombard" in recap |

Known limitations discussed by community: AI cannot **withdraw** from unwinnable assault; artillery/melee timing issues; repetitive patterns at Normal difficulty.

### Relevance to castle-sim

| TW lesson | castle-sim Tier 2+ |
|-----------|-------------------|
| Role-based squads (ladders, ram, archers) | Wolf raid: ladder grunts + archer suppress |
| Reserve / reassign | Don't spawn infinite stream — recycle raid waves |
| Wall-centric phases | Phase 1 wall fight → Phase 2 courtyard only if breach |
| Fast epic pacing | **Reject** for SH1 vibe — prefer slow buildup + one raid timer |
| Grand tactical layer | Overkill for v0; start **timer + single vector** (@concepts/rts-siege-ai-reference.md) |

### v0 cut

Not applicable — no enemy siege AI in vertical slice v0.

## Snippets

> "A proper siege is a complex machine of roles, responsibilities, and reactions on a large scale." — GDC session description

## Dead Ends

- Porting TW wall assault script to 2D isometric peasants — scale and unit count differ by 100×
