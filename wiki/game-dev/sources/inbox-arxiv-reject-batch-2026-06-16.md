---
title: Inbox arXiv reject batch — 2026-06-16 (out of game-dev scope)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, routing]
related:
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-06-16
updated: 2026-06-16
---

## Raw Concept

Seven arXiv PDFs dropped in `research to be indexed/` 2026-06-14–16. Pre-ingest check: all **NEW** vs wiki. **Rejected** for game-dev-wiki — robotics, sports analytics, autonomous driving; no castle/RTS/game-design hook.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2606.09289 | Football in-possession phase ID | **Reject** | Sports analytics — not game-dev |
| 2606.12281 | CCKS multi-agent consensus | **Reject** | General ML — @ccc-wiki if pursued |
| 2606.12306 | UGV/UAV informative planning | **Reject** | Robotics — mis-drop |
| 2606.13376 | MoVerse video world model | **Reject** | Gen video — @image-gen-wiki if pursued |
| 2606.13598 | OrchRM multi-agent orchestration | **Defer @ccc-wiki** | Harness-adjacent; not castle-sim |
| 2606.13840 | Embodied autonomous driving | **Reject** | AV research |
| 2606.16953 | SidewalkBench visual navigation | **Reject** | Robotics benchmark |

**Action:** Archive PDFs to `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/inbox-rejects/2026-06-16/`; clear local inbox. No concept pages created.

**Duplicate skipped:** `Tool Evaluation and Wiki Fit.docx` — already ingested @sources/tool-evaluation-cross-wiki-routing-2026-06-13.md.

## Snippets

Pre-ingest: `python3 scripts/preingest_check.py` — 7 NEW, 1 DUPLICATE (docx).
