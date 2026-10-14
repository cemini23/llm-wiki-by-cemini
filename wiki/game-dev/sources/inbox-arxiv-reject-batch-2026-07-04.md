---
title: Inbox arXiv reject batch — 2026-07-04 (urban planning + AV re-drop)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, mis-route]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-03.md
  - sources/inbox-arxiv-reject-batch-2026-07-02.md
  - sources/36kr-ai-game-story-gameplay-guardrails-2026-06-30.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-04
updated: 2026-07-04
---

## Raw Concept

Two PDFs from `2026-07-04-daily.md`. **Both reject** — one urban-planning math mis-route, one autonomous-driving re-drop.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2408.05140 | Network model for urban planning | **Reject (new)** | Mean-field / optimal-transport urban economics; too abstract for castle-sim |
| 2607.01382 | CommonRoad-Game (AV HITL sim) | **Reject (re-drop)** | Autonomous driving / CommonRoad; already rejected @sources/inbox-arxiv-reject-batch-2026-07-03.md |

**No Phase-0:** `Yunfei-Bi8/CommonRoad-Game` is GPL-3.0 AV research (~1★) and not a game-dev tool. Urban-planning paper has no adoption path for castle-sim; Stronghold 2 estates/carters remain the concrete multi-node economy reference.

**Parallel ingest (news):** @sources/36kr-ai-game-story-gameplay-guardrails-2026-06-30.md. Other news rows were already covered (Ziva Asset Store, Phaser Game Agent, skeleton-implementation article, GameDevBench).

**Action:** Archive PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 2 NEW
```
