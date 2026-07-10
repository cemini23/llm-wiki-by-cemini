---
title: Inbox arXiv reject batch — 2026-07-10 (2 re-drops + HCI scale reject)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop, hci]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-09.md
  - sources/inbox-arxiv-reject-batch-2026-07-08.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-10
updated: 2026-07-10
---

## Raw Concept

Three PDFs from `2026-07-10-daily.md`. **All reject** — two re-drops from 2026-07-09 triage, one new HCI/XAI scale paper (lockstep-cluster false positive).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2511.17384 | IndustryNav (industrial VLLM nav) | **Reject (re-drop)** | Already rejected @sources/inbox-arxiv-reject-batch-2026-07-09.md |
| 2607.05369 | GaP robotics harness | **Reject (re-drop)** | Already rejected @sources/inbox-arxiv-reject-batch-2026-07-09.md |
| 2607.05674 | Perceived System Predictability (PSP scale) | **Reject** | HCI questionnaire for general interactive/XAI systems; lockstep cluster false positive — not RTS networking |

**No Phase-0 / no brief:** digest re-fetched already-rejected PDFs; PSP scale has no castle-sim adoption path (playtest UX metrics are operator judgment, not academic 6-item scale).

**Parallel ingest (news):** Godot 4.7.1 RC2 → @sources/godot-47-release-shelf-2026-06-25.md; SH4 review → @sources/stronghold-4-public-demo-2026-06-24.md; C&C iOS Claude Code port → @sources/claude-code-cc-ios-port-2026-07-07.md.

**Action:** Archive 3 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 3 NEW (wiki-unknown IDs; 2 already triaged 07-09)
Digest skipped MIRA dupe correctly; re-fetched IndustryNav + GaP
```
