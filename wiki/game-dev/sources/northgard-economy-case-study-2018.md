---
title: Northgard core loop — economy case study (2018)
type: source
tags: [source, northgard, economy, rts, case-study]
keywords: [northgard, economy, core-loop, indie-rts, shirogames]
related:
  - concepts/indie-kingdom-builder-lessons.md
  - concepts/stronghold-deconstruction.md
  - concepts/scope-tiers.md
read_status: read
source_type: blog-analysis
source_url: https://denistodorovhonours.wordpress.com/2018/03/24/northgard-breakdow-a-case-study/
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/indie-kingdom-builder-lessons.md — patterns extracted

## Raw Concept

Honours-level breakdown of **Northgard** (Shirogames) territory-based RTS economy and anti-snowball design.

## Narrative

### Core loop (summary) [CONFIRMED — Denis Todorov 2018]

1. **Territory expansion** as reward — scouts colonize tiles for resources, worker caps, building caps, happiness
2. **Villagers** as bottleneck — every job requires a villager; population gated by houses + territories
3. **Scouts** embedded in loop — only unit that colonizes; also loot ruins
4. **Drains** — firewood per territory, scaling food consumption, winter multipliers, colonization costs
5. **Winter** — harsh periodic drain forcing stockpiles; blizzard months worse

### Design patterns named

- Static engine (passive Krown)
- Dynamic engines (food, wood production)
- Dynamic friction (consumption, colonization cost scaling)

### Relevance to castle-sim

Not Stronghold, but best Exa hit for **indie RTS economy that avoids snowball**. Tier 2 ideas: territory caps, seasonal drain, villager-as-resource. **v0 cut:** all of this — keep wood-only without happiness/territory.

## Snippets

Food consumption scales super-linearly with population — intentional anti-snowball friction.
