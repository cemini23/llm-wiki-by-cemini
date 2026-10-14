---
title: Inbox arXiv reject batch — 2026-07-15 (5 rejects; 4 re-drops + swarm MARL)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop, marl, swarm]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-14.md
  - sources/inbox-arxiv-reject-batch-2026-07-13.md
  - sources/inbox-arxiv-reject-batch-2026-07-12.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - concepts/game-ai-rl-augmentation-shelf.md
  - sources/brickworks-godot-lego-framework-shelf-2026-07-15.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-15
updated: 2026-07-15
---

## Raw Concept

Five PDFs from `2026-07-15-daily.md`. **All reject** — four sha256/re-drop matches from 07-13/07-14 plus one new robot-swarm MARL hit from the influence-map cluster.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.07475 | Agent-exploitation affordances | **Reject (re-drop)** | Social robotics ontology — @sources/inbox-arxiv-reject-batch-2026-07-14.md |
| 2607.07820 | DeepSearch-World web agents | **Reject (re-drop)** | QA/browse self-distillation — @sources/inbox-arxiv-reject-batch-2026-07-13.md → CCC note only |
| 2607.08547 | Potential Functions as Types | **Reject (re-drop)** | PL amortized-cost theory — @sources/inbox-arxiv-reject-batch-2026-07-12.md |
| 2607.11334 | Generate–verify–repair twelve-tone | **Reject (re-drop)** | Music harness — lockstep false positive → CCC |
| 2607.12861 | Collective behaviors from simple rewards | **Reject** | IROS 2026 **robot swarm** MARL + Agent Response Map; not RTS influence maps / castle AI |

**Phase-0:** none. No adopt. 2607.12861 is robotics swarm interpretability — defer any RL swarm patterns to Phase E+ per @concepts/game-ai-rl-augmentation-shelf.md (same posture as other MARL rejects).

**Briefs:** none from this inbox (castle-sim legacy; no poker/xsp/pm/David mapping).

**Parallel ingest (news):** Brickworks Godot LEGO framework press → @sources/brickworks-godot-lego-framework-shelf-2026-07-15.md (**WATCH**, no public repo — no Phase-0). Grid placement / SH4 / Phaser / Ziva already shelved prior days.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (4 sha match prior reject batches)
Digest skipped VRExplorer wiki dupe (2607.10174)
```

## Dead Ends

- Treating swarm MARL ARM geometric fields as RTS influence-map research
- Phase-0 on Brickworks without a published license/repo
