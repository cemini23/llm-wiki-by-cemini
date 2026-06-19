---
title: Inbox arXiv reject batch — 2026-06-18 (digest re-drop)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest]
related:
  - sources/inbox-arxiv-reject-batch-2026-06-16.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - sources/inbox-arxiv-reject-batch-2026-06-19.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-06-18
updated: 2026-06-18
---

## Raw Concept

Five arXiv PDFs from daily digest lane (`2026-06-18-daily.md`). Pre-ingest: all **NEW** vs wiki. **Rejected** for game-dev-wiki — same mis-route class as @sources/inbox-arxiv-reject-batch-2026-06-16.md (robotics, AV, gen-video).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2606.13376 | MoVerse video world model | **Reject** | @image-gen-wiki if pursued |
| 2606.13598 | OrchRM multi-agent orchestration | **Defer @ccc-wiki** | Harness-adjacent |
| 2606.13840 | Embodied autonomous driving | **Reject** | AV research |
| 2606.16953 | SidewalkBench visual navigation | **Reject** | Robotics benchmark |
| 2606.18247 | Visual verification policy steering | **Reject** | General ML / robotics |

**Action:** Archive to `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/inbox-rejects/2026-06-18/`; clear local inbox. No concept pages.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW, 0 duplicates
```
