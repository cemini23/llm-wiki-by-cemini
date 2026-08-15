---
title: Inbox arXiv reject batch — 2026-08-15 (1 UAV wind flow-field false positive)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, flow-field, mis-route, UAV, drone, wind, flight-planning, CFD]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-28.md
  - sources/inbox-arxiv-reject-batch-2026-07-22.md
  - concepts/flow-field-pathfinding.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-08-15
updated: 2026-08-15
---

## Raw Concept

One PDF from `2026-08-12-daily.md` … `2026-08-15-daily.md` (arxiv-only paper lane; news disabled). **Reject** — `rts-flow-field-game` arXiv-API fallback matched urban **wind flow fields** (CFD / advanced air mobility) outside game pathfinding. Preingest: 1× NEW. Prior empty digests `2026-07-29`…`2026-08-11` (0 PDFs each) committed with this batch.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2608.10309 | Wind-Informed Rapid Flight-Planning in Complex Urban Topologies via Machine Learning and Experimental Validation | **Reject** | physics.flu-dyn / advanced air mobility (Caltech, Renn/Gharib) — urban wind–building CFD flow fields ≠ Emerson/RTS integration-field pathfinding |

**Phase-0:** none — UAV urban-wind surrogate is not a castle-sim / Godot / harness adopt target.

**Local adopt:** none (<500 MB N/A).

**Briefs:** none — no atto / poker / ceminidfs / xsp / family-tree / wc-ticket / pm-kalshi / castle-sim / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 1 PDF to egress; clear inbox. Tighten `rts-flow-field-game` `arxiv_query`: keep existing flow-field + pathfinding/RTS/game/crowd/Emerson clause; add `ANDNOT` UAV / drone / aerial / air-mobility / flight-planning (do **not** ANDNOT bare `wind`/`urban`/`game` — too broad).

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/arxiv-2608.10309-wind-informed-rapid-flight-planning-in-complex-u.pdf`

## Snippets

```
python3 scripts/preingest_check.py → 1 NEW, 0 LIKELY, 0 DUPLICATES
Digest cluster: rts-flow-field-game (arXiv API; fetched 2026-08-12, sat 08-13…15)
sha256: 4614956bc07d516f… · 9,049,574 bytes
Abstract cue: “hazardous urban wind–building interactions; surrogate predicts flow fields … flight planning for aerial vehicles”
```

## Dead Ends

- Treating CFD/UAV urban wind “flow fields” as Emerson/RTS integration-field pathfinding
- Phase-0 on UAV flight planners / air-mobility surrogates for hobby RTS
- Auto-scp / local clone of the Caltech wind surrogate repo
