---
title: Stigmergic Graph Memory MAPD — goal instantiation before MAPF — 2026-08-15
type: source
tags: [source, arxiv, pathfinding, mapf, mapd, stigmergy, rts]
keywords: [sgm, stigmergy, mapd, mapf, endpoint, congestion, 2607.15182]
related:
  - concepts/rts-pathfinding-approaches.md
  - concepts/godot-pathfinding-patterns.md
  - concepts/flow-field-pathfinding.md
  - sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md
  - entities/projects/castle-sim.md
read_status: read
source_type: arxiv-paper
source_url: https://arxiv.org/abs/2607.15182
maturity: validated
created: 2026-08-15
updated: 2026-08-15
cross-wiki-source: seo-wiki/sources/arxiv-dutta-2026-stigmergic-graph-memory-mapd-2607.15182-2026-07-17.md
---

## Relations

- @concepts/rts-pathfinding-approaches.md — SGM sits **before** A*/flow/ORCA (which jobs enter the planner)
- @sources/arxiv-2606.22757-cooperative-orca-mapf-2026-06-24.md — ORCA is local steer after goals are fixed
- @seo-wiki/sources/arxiv-dutta-2026-stigmergic-graph-memory-mapd-2607.15182-2026-07-17.md — SEO overflow archive (OOD for GEO)
- Gitignored brief: `briefs/research/stigmergic-graph-memory-mapd-shelf.md`

## Raw Concept

**arXiv:2607.15182** — Dutta & Kim (Emory), *Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery*. Bounded decaying memory on graph **nodes/edges** ranks **which feasible endpoints** enter the MAPF planner. Warehouse many-to-many MAPD. Throughput **+20.5–36.7%** vs reconstructed M2M baselines across 15 map–load conditions; endpoint-steering ablation is the main gain. No public code at SEO ingest (2026-07-17). PDF archived under SEO egress.

Routed here via gitignored `briefs/2026-07-17_k141-stigmergic-graph-memory-mapd-from-seo.md` (never wiki-ingested until this page).

## Narrative

### Split [CONFIRMED — paper framing]

| Layer | What it chooses | castle-sim analog |
|-------|-----------------|-------------------|
| **SGM (this paper)** | Which stockpile / job / estate **endpoint** is eligible *now* | Job dispatcher / cart destination pick |
| **Global planner** | Path to that endpoint | `AStarGrid2D` / Tier 2 flow field |
| **Local steer** | Collision in chokes | Godot avoidance / ORCA shelf |

Typed decaying channels (waiting, endpoint pressure, edge delay/blocking) beat a single congestion scalar.

### castle-sim mapping [TENTATIVE — Phase E+ / estates]

- Peasant unique trees (v0): **skip** — one agent, one cell, no MAPD
- Estate carters + multi-granary (story-025/026): **STEAL-FROM** — decaying “this granary is slammed” memory before assigning the next cart
- Kingmaker multi-lord logistics: same pattern, not a new pathfinder

**Verdict:** **STEAL-FROM (dispatcher memory)** — do not vendor warehouse MAPD code (none linked). Do not replace `AStarGrid2D`.

## Snippets

> recent execution memory can improve warehouse throughput by shaping which feasible goals enter the planner, not only how agents travel to already fixed goals. [Source: arXiv 2607.15182 Abstract]

## Dead Ends

- Porting warehouse MAPD / PBS / RHCR into Godot v0
- Treating SGM as a flow-field or ORCA replacement
- SEO/GEO adopt (sibling correctly marked OOD)
