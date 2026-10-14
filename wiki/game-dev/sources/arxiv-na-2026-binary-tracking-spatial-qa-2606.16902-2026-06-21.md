---
title: "Na et al. 2026 — BinTrack spatial QA for open VLMs (arXiv 2606.16902)"
type: source
tags: [source, arxiv, robotics, spatial-qa, navigation, k125]
keywords: [2606.16902, BinTrack, BinaryTracking, GangnamLoop, SpaceLocQA, open VLM]
related:
  - entities/tools/binarytracking.md
  - concepts/godot-pathfinding-patterns.md
  - entities/tools/godot-ai-playtest.md
maturity: validated
read_status: read
created: 2026-06-21
updated: 2026-06-21
cross-wiki-source: "@seo-wiki/sweeps/2026-06-21-daily.md"
---

## Relations

- @entities/tools/binarytracking.md — BinTrack agent + GangnamLoop benchmark
- @concepts/godot-pathfinding-patterns.md — binary segment search steal for grid agents
- @entities/tools/godot-ai-playtest.md — onboard open-model agent testing analog
- @seo-wiki/sweeps/2026-06-21-daily.md — K125 SEO digest cross-route
- @seo-wiki/concepts/near-me-search.md — route-context local query analog

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Binary Tracking for Spatial QA and Navigation with Open Vision-Language Models |
| **Authors** | Dongbin Na et al. |
| **arXiv** | 2606.16902v1 |
| **Repo** | https://github.com/ndb796/BinaryTracking |
| **Retrieved** | 2026-06-21 via @seo-wiki federated digest |
| **Read status** | read (BinTrack method, GangnamLoop benchmark, SpaceLocQA gains) |

## Narrative

**BinTrack** — fully open-source spatial-localization agent for service-robot egocentric routes. Given queries like *"where can I find a dry cleaner on the way back home?"*, returns metric coordinates for downstream navigation.

**Method:** binary search over trajectory segments between two anchor landmarks parsed from the query — exploits temporal ordering of the robot path vs retrieval-heavy closed-source agents (GPT-4o RAG baselines).

**Results:** up to **+22.8%** accuracy vs other open-source stacks; matches reported closed-source result on SpaceLocQA **global** category; **>1.5×** inference speedup.

**GangnamLoop:** new multi-trip outdoor benchmark — real quadruped on public streets, anonymized, revisits under varying conditions, low robot POV + human owner POV pairs.

**Game-dev steal:** binary search over ordered path segments for "where along this route?" localization — pattern transfer to grid castle-sim patrol / landmark queries without closed API dependency.

**Phase-0:** GitHub **0 stars**, **no LICENSE** (2026-06-21) — **CONDITIONAL-GO** until SPDX confirmed.

## Snippets

> "BinTrack performs a binary search over the trajectory segments between two anchor landmarks identified from a query." [Source: arxiv-2606.16902 Abstract]

> "Improves overall accuracy by up to 22.8% over other open-source implementations." [Source: arxiv-2606.16902 Abstract]
