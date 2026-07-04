---
title: Inbox arXiv reject batch — 2026-07-03 (autonomous-driving mis-route)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, mis-route]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-04.md
  - sources/inbox-arxiv-reject-batch-2026-07-02.md
  - sources/inbox-arxiv-reject-batch-2026-07-01.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-03
updated: 2026-07-03
---

## Raw Concept

One arXiv PDF from `2026-07-03-daily.md`. **Reject** — autonomous-driving HITL simulator mis-routed from lockstep/deterministic query.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.01382 | CommonRoad-Game (AV HITL sim) | **Reject (new)** | Autonomous driving / CommonRoad — GPL-3.0 repo out of scope |

GitHub: `Yunfei-Bi8/CommonRoad-Game` (~1★, Jul 2026). **No Phase-0** — not game-dev; human-in-the-loop pattern only loosely parallels playtest gates.

**Digest dupes skipped:** 2606.30092 (ingested).

**Parallel ingest (news):** @sources/godot-engine-ai-contribution-policy-2026-07-01.md.

**Action:** Archive PDF to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 1 NEW
preingest URLs: https://github.com/Yunfei-Bi8/CommonRoad-Game
```
