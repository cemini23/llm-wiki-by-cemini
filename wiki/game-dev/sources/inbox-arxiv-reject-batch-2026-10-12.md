---
title: Inbox arXiv batch — 2026-10-12 (2 ingests, 0 rejects)
type: source
tags: [source, triage, arxiv, ingest, harness, memory]
keywords: [arxiv, triage, digest, spirebench, reqclarifybench, clarification, cross-run-memory]
related:
  - sources/inbox-arxiv-reject-batch-2026-10-09.md
  - sources/arxiv-2610.12596-spirebench-long-horizon-memory-2026-10-12.md
  - sources/arxiv-2610.13022-reqclarifybench-clarification-2026-10-12.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - concepts/agent-harness-castle-project.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-10-12
updated: 2026-10-25
---

## Raw Concept

Two PDFs from the `2026-10-10` and `2026-10-12` digests. **2 ingest, 0 reject** — the **third consecutive all-ingest batch**. One is a long-horizon game benchmark with a decisive memory result; the other is a requirement-clarification benchmark for repository-level work. Preingest: 2× NEW, 0 duplicates.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2610.12596 | SpireBench — long-horizon strategic play (Slay the Spire) | **Ingest** | @sources/arxiv-2610.12596-spirebench-long-horizon-memory-2026-10-12.md |
| 2610.13022 | ReqClarifyBench — interactive requirement clarification | **Ingest** | @sources/arxiv-2610.13022-reqclarifybench-clarification-2026-10-12.md |

### The two hooks

**SpireBench** closes a loop this wiki has been tracking for a week. Three separate studies now show that agent-written persistent notes fail:

1. The Mafia study (@sources/arxiv-2610.05041-mafia-communication-collective-inference-2026-10-07.md) — societies carrying sixty generations of their own notes scored **below** societies with none.
2. Learn2Play (@sources/arxiv-2610.08215-learn2play-bench-experience-2026-10-07.md) — complete raw records beat summarised ones.
3. **SpireBench** — models **did not improve from the memories they write across runs**, and those memories were **often wrong and overly cautious**.

That is three independent setups reaching the same conclusion, which is why rule **H8** now carries three citations rather than one. MEMENTO 3 (@sources/arxiv-2610.11794-memento-3-reflective-rulebooks-2026-10-09.md) is the constructive answer: a revisable rulebook admitted only on deterministic replay.

**ReqClarifyBench** is the closest match yet to the wiki's own planner→executor handoff: a vague intent handed to a model that must clarify rather than guess, because a wrong guess **propagates and causes costly rework**. It supports a new rule — surface ambiguity before writing the spec.

### Phase-0

**No resolvable repositories.** Neither paper ships a code URL that resolves in the text. Both are **STEAL-FROM (pattern only)**. SpireBench does describe a harness, but the paper is the artifact, not a repo.

**Action:** Archive 2 PDFs; clear inbox.

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/game-dev/` (per archived filename).

## Dead Ends

- Reading three negative results about agent-written notes as a reason to keep no record at all. The finding is that *derived* notes fail; the raw record is what Learn2Play found useful.
- Expecting a fourth consecutive all-ingest batch. Three good windows are a good query, not a guarantee.
