---
title: "Structured memory folding — shrink record count and context length together"
type: concept
related:
  - sources/arxiv-memfolder-structure-guided-memory-folding-2611.26427.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/hierarchical-bounded-agent-memory.md
  - entities/tools/claude-mem.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: what is the right unit to compress in an agent memory store?

Synthesised from one source: `@sources/arxiv-memfolder-structure-guided-memory-folding-2611.26427.md` (MemFolder, 2611.26427).

## Narrative

Agent memory cost has two coupled axes. More records means a bigger index, a wider search space and slower retrieval. Longer retrieved context means more prefill and more decoding attention. A method that fixes one axis can make the other worse: pruning loses evidence, consolidation yields fewer but longer units.

MemFolder folds both, using the same memory groups for both steps.

- **RecordFolder** grounds entity mentions, selects representative and complementary anchors, and merges compatible records. It combines semantic affinity, entity affinity and temporal chaining. Target is N → N/2.
- **ContextFolder** encodes the records in a group into compact text, then revises the encoding when verification feedback shows a missing key fact.

On Mem0 across three text benchmarks, RecordFolder keeps 99.0% of average performance with 50% fewer records, 1.9 points above the strongest baseline on retention. Benchmarks: LoCoMo, PersonaMem, LongMemEval, M3-Bench-web, M3-Bench-robot.

### Operating rule

Measure both axes. A memory change that halves record count but doubles tokens per record has moved the cost, not cut it. For Cemini, this applies to `hot.md` and to claude-mem observations: record count and total retrieved tokens belong in the same table.

Code is published at github.com/xuyang-liu16/MemFolder. [TENTATIVE] single source.

## Snippets

> "RecordFolder retains 99.0% of the original average performance across the three text-based benchmarks with 50% fewer records." [Source: arxiv-2611.26427-memfolder-structure-guided-memory-folding-for-ef.pdf p.1]

> "Pruning can discard useful evidence, whereas consolidation may produce fewer yet longer retrieval units." [Source: arxiv-2611.26427-memfolder-structure-guided-memory-folding-for-ef.pdf p.1]
