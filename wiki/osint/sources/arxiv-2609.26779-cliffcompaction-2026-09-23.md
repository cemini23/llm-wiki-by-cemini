---
title: "CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents"
type: source
tags: [arxiv, source, k270, agents, harness, coding]
keywords: [k270, compaction, context, Terminal-Bench, KernelBench]
related:
  - concepts/k270-harness-evolution-wave.md
  - entities/tools/cliffcompaction.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md
- @entities/tools/cliffcompaction.md

## Raw Concept

| Paper | arXiv:2609.26779 |
| File | `arxiv-2609.26779-cliffcompaction-cost-efficient-compaction-for-lo.pdf` |
| Location | `local inbox (archive blocked 2026-09-23): research to be indexed/arxiv-2609.26779-cliffcompaction-cost-efficient-compaction-for-lo.pdf` |
| Authors | Trang Nguyen, Eulrang Cho, Bingqing Chen, Tim Dettmers (Carnegie Mellon University; Bosch Center for AI) |
| Retrieved | 2026-09-23 |
| Pages | 25 |
| Dual-ID | **OSINT K270** |
| sha256 | `0324a6727e2fc6e515858f5131ed8f0d9a73ea4fe82c6e39444dd767b4621d6b` |

## Narrative

Agents often work on complex problems that need millions of tokens of context. Limited context windows make compaction across sessions necessary. CLIFFCOMPACTION is an **autocompaction** technique. It cuts cost by **up to 50%** under a bounded context, while maintaining or improving performance on Terminal-Bench.

**Two fidelity rules drive the result:**

1. **Truncate or drop only.** CLIFFCOMPACTION never rephrases or rewrites content. Compacted information stays faithful.
2. **Never compact a compaction.** Each pass operates only on original content. Prior compacted output is discarded. Context drift therefore cannot accumulate.

**Reported results:**

| Claim | Value |
|-------|-------|
| Cost reduction under bounded context | up to 50% |
| Terminal-Bench gain from test-time scaling | >10 percentage points, under the cost of two full-context runs |
| KernelBench CUDA kernel speedup after 200 steps | 2.23× |
| KernelBench CUDA kernel speedup after 400 steps | 3.58× |
| Parallel test-time scaling | Kimi K2.6 matches Opus 4.7, exceeds Opus 4.6 and GPT-5.3 Codex at lower cost |

The properties sustain continual learning over sessions exceeding a million tokens. On KernelBench the method surpasses specialized search algorithms and trained agents, even though it is a general-purpose compaction technique.

**Release.** The paper open-sources a **scaffold-agnostic API-proxy** implementation, reported as usable with Claude Code. See @entities/tools/cliffcompaction.md for the Phase-0 clone record.

**Cemini relevance:** context-compaction pattern for CCC long-horizon sessions. **FILE only. 0 product Integrate GO. Do not swap `/route`. Never auto-evolve `.cursor/skills`. No weight download.**
