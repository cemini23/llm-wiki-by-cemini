---
title: RTS siege AI — reference shelf (Tier 2+)
type: concept
tags: [concept, siege, ai, deferred]
keywords: [siege, ai, total-war, stronghold]
related:
  - sources/gdc-total-war-warhammer-siege-ai.md
  - concepts/stronghold-systems-inventory.md
  - concepts/vertical-slice-v0.md
  - concepts/scope-tiers.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - entities/tools/unofficial-crusader-patch2.md
  - concepts/stronghold-2-siege-warfare.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/arxiv-2606.20210-augmenting-game-ai-drl-2026-06-20.md
  - concepts/stronghold-crusader-ai-modding-shelf.md
maturity: validated
created: 2026-06-13
updated: 2026-06-20
---

## Relations

- @sources/gdc-total-war-warhammer-siege-ai.md — AAA role/reserve architecture (ingested 2026-06-13)
- @concepts/game-ai-rl-augmentation-shelf.md — modular RL leaves on hand-coded siege director (EA 2026)

## Raw Concept

Enemy siege behavior research shelf when castle-sim passes v0 — Stronghold mechanics + TW GDC patterns, scaled down.

## Narrative

v0 explicitly excludes enemy raids and siege engines. When adding waves (Tier 2):

### Stronghold-first (primary)

From @concepts/stronghold-systems-inventory.md:

- Ladder / siege tower / ram counters
- Wall segment targeting, pitch, engineer units
- Popularity / fear hooks optional Tier 2.5

### AAA reference (secondary)

From @sources/gdc-total-war-warhammer-siege-ai.md [TENTATIVE — forum recap of GDC 2016]:

| TW pattern | castle-sim mini version |
|------------|-------------------------|
| Assault roles (breach, suppress, reserve) | 3 unit types max: grunt, archer, ram |
| Reserve pool / tactic fail | Second wave only if first stalls N seconds |
| Wall phase → courtyard phase | Raid ends if wall held; breach triggers courtyard spawn |
| Fast epic pacing | **Invert** — one slow raid timer, SH1 pacing |

### Minimum viable raid AI

1. **Timer spawn** + single attack vector (gate or wall segment)
2. **Direct path** on same grid as peasants (no lord AI)
3. **No withdraw** OK for wolves — TW's withdraw gap is a caution for human-like lords Tier 3+

## Snippets

Tier 2 minimum: one enemy type, one attack vector, no multi-lord skirmish.

## Dead Ends

- Grand tactical analyzer at hobby scale — start timer + path
