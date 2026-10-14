---
title: Inbox arXiv reject batch — 2026-06-26 (digest re-drop)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop]
related:
  - sources/inbox-arxiv-reject-batch-2026-06-25.md
  - sources/inbox-arxiv-reject-batch-2026-06-24.md
  - sources/hera-agent-godot-phase-0-audit-2026-06-26.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - sources/notnull92-hera-agent-godot-devto-2026-06-25.md
  - sources/inbox-arxiv-reject-batch-2026-06-27.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-06-26
updated: 2026-06-26
---

## Raw Concept

Five arXiv PDFs from `2026-06-26-daily.md`. **All reject/re-defer** — four re-drops from @sources/inbox-arxiv-reject-batch-2026-06-24.md; one new robotics survey.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2606.21438 | Temporal logics robot synthesis | **Reject** | cs.RO formal planning survey |
| 2606.22488 | SCOPE symbolic world planning | **Reject (re-drop)** | Embodied VLM + classical planner |
| 2606.22813 | Active Inference physical AI | **Reject (re-drop)** | Robotics test-time scaling |
| 2606.23105 | CaR video world models | **Reject (re-drop)** | Video generation / implicit memory |
| 2606.24037 | Morality Game multiplayer platform | **Reject (re-drop)** | Behavioral economics research hub |

**Digest dupes skipped:** 2606.22757 (ingested), cap-5 on 2606.24003/2606.21008.

**Parallel ingest (news):** @sources/notnull92-hera-agent-godot-devto-2026-06-25.md → Phase-0 @sources/hera-agent-godot-phase-0-audit-2026-06-26.md.

**Action:** Archive all PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (sha not in wiki index)
```
