---
title: Inbox arXiv reject batch — 2026-07-28 (1 lockstep false positive; neuromorphic SIMD)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, lockstep, mis-route, neuromorphic, SIMD, sparsity]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-22.md
  - sources/inbox-arxiv-reject-batch-2026-07-20.md
  - concepts/rts-networking-deferred.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-28
updated: 2026-07-28
---

## Raw Concept

One PDF from `2026-07-28-daily.md` (arxiv-only paper lane; news disabled). **Reject** — `lockstep-deterministic` arXiv-API query matched hardware **lockstep SIMD** in a neuromorphic sparsity paper (no game / multiplayer / netcode). Preingest: 1× NEW. Prior empty digests `2026-07-23`…`2026-07-27` (0 PDFs) committed with this batch.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.22790 | The Sparsity Tax — weight sparsity in event-driven SIMD/SIMT neuromorphic cores | **Reject** | Hardware architecture (cs.AR) — “lockstep SIMD” ≠ RTS lockstep netcode; GitHub `MW-SAND/neuromorphic-flos-co-processor` out of scope |

**Phase-0:** none — neuromorphic FLOS co-processor is not a castle-sim / Godot / harness adopt target.

**Local adopt:** none (<500 MB N/A).

**Briefs:** none — no poker / David (TipDrop) / xsp / pm / atto / castle-sim / prod mapping from this inbox.

**News:** lane disabled — no news rows.

**Action:** Archive 1 PDF to egress; clear inbox. Tighten `lockstep-deterministic` `arxiv_query`: drop bare `all:game` / `all:networking`; require multiplayer / RTS / netcode / `"video game"` / `"game networking"`; `ANDNOT` SIMD / neuromorphic / GPU.

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/arxiv-2607.22790-the-sparsity-tax-weight-sparsity-trade-offs-in-e.pdf`

## Snippets

```
python3 scripts/preingest_check.py → 1 NEW, 0 LIKELY, 0 DUPLICATES
Digest cluster: lockstep-deterministic (arXiv API)
sha256: 8a1ff0f9e46f6087… · 1,658,213 bytes
Abstract: “undermine lockstep Single Instruction Multiple Data (SIMD) execution”
```

## Dead Ends

- Treating silicon “lockstep SIMD” as networked-game lockstep / rollback netcode
- Phase-0 on neuromorphic accelerators for hobby RTS
- Auto-scp / local clone of `neuromorphic-flos-co-processor`
