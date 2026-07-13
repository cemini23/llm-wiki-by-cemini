---
title: Inbox arXiv reject batch — 2026-07-12 (4 re-drops + chemistry + PL theory)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, re-drop]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-11.md
  - sources/inbox-arxiv-reject-batch-2026-07-10.md
  - sources/inbox-arxiv-reject-batch-2026-07-13.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-12
updated: 2026-07-12
---

## Raw Concept

Five PDFs from `2026-07-12-daily.md`. **All reject** — four re-drops from 07-09–07-11 triage plus two new off-topic hits.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2606.05050 | CatDT catalyst digital twin | **Reject** | Chemistry/materials multi-agent sim; harness pattern note only → @ccc-wiki |
| 2607.04689 | RCT-AD AV planning | **Reject (re-drop)** | @sources/inbox-arxiv-reject-batch-2026-07-11.md |
| 2607.05369 | GaP robotics harness | **Reject (re-drop ×4)** | @sources/inbox-arxiv-reject-batch-2026-07-09.md |
| 2607.06269 | Structural Tension meta-architecture | **Reject (re-drop)** | @sources/inbox-arxiv-reject-batch-2026-07-11.md |
| 2607.08547 | Potential Functions as Types (Calf/Giralf) | **Reject** | PL cost verification; influence-map cluster false positive — not RTS potential fields |

**No Phase-0 / no brief:** digest re-fetch loop continues (GaP ×4); no castle-sim tool surfaced.

**Parallel ingest (news):** UGenLah Unity agentic PCG → @sources/ugenlah-unity-agentic-pcg-shelf-2026-07-10.md.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (4 sha256 matches prior reject batches)
Digest skipped MIRA wiki dupe; capped PSP re-fetch
```

## Dead Ends

- Treating "Potential Functions as Types" as RTS influence-map research
