---
title: BinaryTracking (BinTrack) — open spatial QA agent (CONDITIONAL-GO)
type: entity
tags: [tool, robotics, spatial-qa, navigation, k125]
keywords: [BinTrack, BinaryTracking, GangnamLoop, open VLM]
related:
  - sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md
  - concepts/godot-pathfinding-patterns.md
  - entities/tools/godot-ai-playtest.md
maturity: draft
created: 2026-06-21
updated: 2026-06-21
phase_0_verdict: CONDITIONAL-GO
license_verified: false
repo: https://github.com/ndb796/BinaryTracking
cross-wiki-source: "@seo-wiki/sweeps/2026-06-21-daily.md"
---

## Relations

- @sources/arxiv-na-2026-binary-tracking-spatial-qa-2606.16902-2026-06-21.md
- @concepts/godot-pathfinding-patterns.md — binary segment localization steal
- @entities/tools/godot-ai-playtest.md — open-model onboard testing

## Raw Concept

Phase-0 from K125 SEO digest cross-route — arXiv 2606.16902 + GitHub `ndb796/BinaryTracking`.

## Narrative

### Phase-0 verdict: **CONDITIONAL-GO**

| Check | Result |
|-------|--------|
| License | **None** on GitHub API (2026-06-21) — block fork until SPDX confirmed |
| Maturity | 0 stars; pushed 2026-06-15; GangnamLoop + SpaceLocQA claims in paper |
| Failure mode | Real-robot outdoor benchmark — not directly game-engine integrated |
| Wiki overlap | @concepts/godot-pathfinding-patterns.md — steal algorithm pattern only |

**Steal-from:** binary search on ordered trajectory between anchor landmarks; open-VLM onboard inference discipline; multi-trip benchmark design (GangnamLoop).

**Do not adopt** runtime until license verified — use paper + repo README for pattern extraction only.

## Snippets

> "Creates a need for open-source based Spatial Question Answering approaches that can run onboard the robot." [Source: arxiv-2606.16902 Abstract]
