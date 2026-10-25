---
title: "Optimal any-angle path planning — arXiv 2607.00065"
type: source
tags: [arxiv, pathfinding, robotics, game-dev, castle-sim, k140, pdf]
keywords: [Zeta star, Zeta-SIPP, any-angle, Anya, Theta star, elliptical expansion, field of view, dynamic obstacles, Delft]
related:
  - concepts/castle-sim-pathfinding-steals.md
  - concepts/castle-sim-rts-micromanagement-steals.md
  - sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md
maturity: draft
read_status: read
created: 2026-07-02
updated: 2026-07-02
clusters: [game-dev, pathfinding]
---

## Relations

- @concepts/castle-sim-pathfinding-steals.md — K140 Zeta* steal extends K126 multi-criteria routing cluster
- @sources/arxiv-continuum-robots-resilience-2606.20495-2026-06-22.md — prior castle-sim path steal source (K126)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Optimal any-angle path planning in static and dynamic environments |
| **Authors** | Yiyuan Zou, Clark Borst (TU Delft) |
| **arXiv** | 2607.00065v1 |
| **Type** | PDF |
| **sha256** | `9019af97697a6a7947f0e69d02a6fb78516bea55c5af61353295299be036c5db` |
| **Demo** | dronectr.tudelft.nl pathfinder (Zou and Borst, 2025) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.00065-optimal-any-angle-path-planning-in-static-and-dy.pdf` |
| **Retrieved** | 2026-07-02 |
| **Read status** | read (abstract + intro + algorithm overview) |

## Narrative

Extends grid any-angle planning (Theta*, Anya) with **optimal** shortest paths on uniform costmaps. Introduces:

1. **Elliptical forward expansion** — restricts search via ellipse neighborhoods
2. **Field of view (FoV)** — faster visibility checks vs line-of-sight
3. **Inverted vs forward scanning** — open-node vs closed-node visibility propagation

**Algorithms:** **Zeta*** (static) — performance comparable to state-of-the-art **Anya**; **Zeta*-SIPP** (dynamic) — **>20× faster** than optimal TO-AA-SIPP baseline.

**Limitation:** Anya/Polyanya hard to extend to 3D or dynamic envs; Zeta* family targets unified static+dynamic optimality on grids.

**Cemini relevance:** castle-sim Godot siege routing — optimal any-angle paths on navigation grids with moving defenders (dynamic obstacles). REFERENCE only — no public code repo at ingest `[OPEN QUESTION 2026-07-02]`.

## Snippets

> "Zeta*-SIPP, with either scanning method, is more than 20 times faster than the corresponding state-of-the-art optimal planner TO-AA-SIPP." [Source: arxiv-2607.00065 abstract (retrieved 2026-07-02)]
