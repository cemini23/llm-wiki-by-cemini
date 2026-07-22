---
title: Inbox arXiv reject batch — 2026-07-22 (2 flow-field false positives; drone + medical continuum)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, flow-field, mis-route, drone, continuum-robot, medical]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-20.md
  - concepts/flow-field-pathfinding.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-22
updated: 2026-07-22
---

## Raw Concept

Two PDFs from `2026-07-22-daily.md` (arxiv-only paper lane; news disabled). **Both reject** — `rts-flow-field-game` arXiv-API fallback matched bare `continuum` + `navigation` outside game pathfinding. Preingest: 2× NEW. Prior day `2026-07-21-daily.md` had empty inbox (3 ConFlow/robot/astro re-drop skips only).

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.19213 | Computing on the Fly — vision for drone computing | **Reject** | cs.RO/cs.AI infrastructure vision — “navigating” ≠ RTS flow fields |
| 2607.19274 | Eversion robots for spinal subarachnoid endoscopy | **Reject** | Medical continuum/eversion robot (cs.RO) — bare `continuum` token false positive |

**Phase-0:** none. **Local adopt:** none.

**Briefs:** none — no poker / David / xsp / pm / castle-sim / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 2 PDFs to egress; clear inbox. Tighten `rts-flow-field-game` `arxiv_query` (drop bare `continuum` / lone `navigation`; require game/RTS/pathfinding + flow-field terms).

## Snippets

```
python3 scripts/preingest_check.py → 2 NEW, 0 LIKELY, 0 DUPLICATES
Digest cluster: rts-flow-field-game (arXiv API)
2026-07-21: 0 fetched, 3 skipped-dup (ConFlow / CR-Solver / SKA)
```

## Dead Ends

- Treating arXiv “continuum” (continuum robots) as Emerson continuum crowds / flow fields
- Treating “navigating” in drone/medical titles as game navigation mesh / flow-field research
