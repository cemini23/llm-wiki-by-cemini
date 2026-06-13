---
title: Medieval sim — fun vs historical accuracy
type: concept
tags: [concept, medieval, design, accuracy, stronghold]
keywords: [medieval, accuracy, city-builder, fantasy, scope]
related:
  - sources/leiden-medieval-city-builder-accuracy-2020.md
  - concepts/scope-tiers.md
  - entities/games/stronghold-series.md
maturity: validated
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- @concepts/indie-kingdom-builder-lessons.md — scope framing

## Raw Concept

Why Stronghold-like games are **romantic simulators**, not history sims — and why that's fine for Tier 1.

## Narrative

### Stronghold is already fantasy

Instant wall draw, invisible gold treasury, peasants without feudal obligations, archers on demand — all gameplay abstractions. Firefly prioritized **castle fantasy** over manor economics [CONFIRMED Bradbury interviews].

### Leiden blog tensions (city-builder lens)

| Historical reality | Typical builder game | Stronghold |
|--------------------|---------------------|------------|
| Planned village layouts | Organic sprawl from center | Player-drawn walls |
| Tithes & feudal labor | Abstract tax slider | Popularity + tax |
| Subsistence stability | Linear growth | Campaign progression |
| Grid for pathfinding | Off-grid pretty towns | Grid walls |

### Design stance for castle-sim

- **Embrace** readable grid + instant feedback (pathfinding + UX)
- **Defer** tithe collectors, crop rotation, plague — Tier 2+ if ever
- **Optional flavor** later: bad harvest event, raid burn animation — not v0

### Art implication

Pre-rendered isometric Stronghold look ≠ historical reconstruction — placeholder art OK (@concepts/art-pipeline-v0-requirements.md).

## Snippets

> Gridlike roads simplify pathfinding — Leiden 2020; aligns with our `AStarGrid2D` choice.
