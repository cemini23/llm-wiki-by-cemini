---
title: "MemFolder — structure-guided memory folding for agent memory management"
type: source
related:
  - concepts/structured-memory-folding.md
  - concepts/storage-budgeted-agent-memory-compression.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/claude-mem.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MemFolder: Structure-Guided Memory Folding for Efficient Agent Memory Management |
| Author | Xuyang Liu, Chenwen Lu et al. (Sichuan, Fudan, SYSU, ZJU, SJTU) |
| Type | arXiv paper (cs.CL), 2611.26427 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.26427-memfolder-structure-guided-memory-folding-for-ef.pdf` |
| Retrieved | 2026-11-22 |
| Pages | 24 |
| Read status | read |

## Narrative

Long-term agents accumulate memory stores that grow on two axes at once: the number of records, and the length of the retrieved context. Pruning cuts records but discards evidence. Consolidation cuts records but makes each one longer. MemFolder folds both.

Two components share the same memory groups:

- **RecordFolder** grounds entity mentions, selects representative and complementary anchors, and merges compatible records. It combines semantic affinity, entity affinity and temporal chaining. Target: N → K = N/2.
- **ContextFolder** encodes the original records in a group into compact text, then revises the encoding when verification feedback shows a key fact is missing.

On Mem0 across three text benchmarks, RecordFolder keeps 99.0% of original average performance with 50% fewer records. That is 1.9 points better retention than the strongest baseline. Reported benchmarks are LoCoMo, PersonaMem, LongMemEval, M3-Bench-web and M3-Bench-robot. Code is at github.com/xuyang-liu16/MemFolder. [TENTATIVE] single source.

The useful idea for Cemini is the two-axis framing. A memory layer that shrinks record count but lengthens each record has not solved the cost problem. `hot.md` and claude-mem should be measured on both axes.

## Snippets

> "On Mem0, RecordFolder retains 99.0% of the original average performance across the three text-based benchmarks with 50% fewer records." [Source: arxiv-2611.26427-memfolder-structure-guided-memory-folding-for-ef.pdf p.1]
