---
title: Inbox arXiv reject batch — 2026-07-16 (1 ingest + 4 rejects; arXiv-API false positives)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, astronomy, robotics, antenna, ocean]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-15.md
  - sources/inbox-arxiv-reject-batch-2026-07-17.md
  - sources/arxiv-2607.02222-cofl-s-sector-flow-fields-2026-07-16.md
  - concepts/flow-field-pathfinding.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-16
updated: 2026-07-16
---

## Raw Concept

Five PDFs from `2026-07-16-daily.md` (arxiv-only paper lane; news disabled). **One ingest** (CoFL-S flow fields), **four reject** — astronomy, continuum robots, wireless antennas, ocean wave drawing — keyword collisions on “flow field” / pathfinding clusters.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.02222 | CoFL-S sector flow fields (VLN) | **Ingest** | @sources/arxiv-2607.02222-cofl-s-sector-flow-fields-2026-07-16.md — STEAL-FROM research |
| 2607.06315 | Low-frequency recombination lines (galaxies/AGN) | **Reject** | Radio astronomy / SKA chapter |
| 2607.11340 | CR-Solver continuum robot kinematics | **Reject** | Tendon-driven robot IK — not RTS pathfinding |
| 2607.13582 | Pinching-antenna LoS blockage (PASS) | **Reject** | Wireless communications / stochastic geometry |
| 2607.13691 | Drawing with water waves | **Reject** | Ocean engineering focused-wave fields |

**Phase-0:** none — CoFL-S has no public adoptable package found; robotics/Habitat domain → **NO-GO adopt**.

**Briefs:** castle-sim research shelf only (`briefs/research/cofl-s-sector-flow-field-shelf.md`). No poker / David / prod mapping from this inbox.

**News:** lane disabled in digest config — no news rows.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW
Paper lane: arxiv-only API (exa.paper_mode=arxiv-only); heavy false-positive rate on "flow field"
```

## Dead Ends

- Treating radio-astronomy “recombination lines” or ocean wave focusing as game flow-field research
- Phase-0 on CR-Solver for castle-sim pathfinding
