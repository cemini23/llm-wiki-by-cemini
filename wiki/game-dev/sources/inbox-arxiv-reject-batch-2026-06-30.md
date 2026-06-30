---
title: Inbox arXiv reject batch — 2026-06-30 (4 reject + 1 ingest)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop]
related:
  - sources/inbox-arxiv-reject-batch-2026-06-29.md
  - sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-06-30
updated: 2026-06-30
---

## Raw Concept

Five arXiv PDFs from `2026-06-30-daily.md`. **Four reject**; **one ingest** (StarCraft influence-map HRL).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2606.24037 | Morality Game multiplayer platform | **Reject (re-drop)** | Behavioral economics research hub |
| 2606.24160 | Causal RL introduction survey | **Reject (new)** | Academic RL theory — not game implementation |
| 2606.24386 | Line Planning at Scale | **Reject (new)** | Public-transit line planning — mis-route from navmesh query |
| 2606.26397 | Pareto-optimal multi-objective RL | **Reject (re-drop)** | Generic MORL → @concepts/game-ai-rl-augmentation-shelf.md defer |
| 2606.30092 | HRL-IM/CBS StarCraft micromanagement | **INGEST** | @sources/arxiv-2606.30092-starcraft-hrl-influence-maps-2026-06-30.md |

**Parallel ingest (news):** @sources/pcgodot-phase-0-audit-2026-06-30.md; @sources/ramen-aura-15-commercial-shelf-2026-06-26.md; PUBG Ally beta note → @sources/krafton-pubg-ally-nvidia-ace-2026-06-25.md.

**Action:** Archive all PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (sha not in wiki index)
```
