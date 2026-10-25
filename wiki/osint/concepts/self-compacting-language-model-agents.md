---
title: SelfCompact — model-invoked context compaction for long agent traces
type: concept
tags: [concept, agent-harness, context-management, llm-agents, k129]
keywords: [SelfCompact, SELFCOMPACT, compaction tool, rubric, fixed-interval summarization, agent traces]
related:
  - sources/arxiv-selfcompact-lm-agents-2606.23525-2026-06-25.md
  - concepts/code-as-agent-harness.md
  - concepts/context-compression-resume-pattern.md
  - concepts/aohp-os-level-agent-harness.md
  - concepts/mcp-context-optimization.md
  - entities/tools/headroom.md
maturity: draft
created: 2026-06-25
updated: 2026-10-25
---

## Relations

- @sources/arxiv-selfcompact-lm-agents-2606.23525-2026-06-25.md — primary source (arXiv 2606.23525)
- @concepts/code-as-agent-harness.md — harness scaffold taxonomy
- @concepts/context-compression-resume-pattern.md — prescribed CPR pattern (checkpoint vs in-trace compaction)

## Raw Concept

Prompted by arXiv **2606.23525** (K129). Long agent traces (CoT + tool calls) **anchor** later generations and exceed context windows. Fixed token-threshold compaction discards mid-derivation state.

## Narrative

**SelfCompact (SELFCOMPACT) scaffold — two coupled inference-time elements:**

1. **Compaction tool** — model invokes to summarize accumulated context
2. **Lightweight rubric** — when to fire (sub-task resolved, trajectory converging) vs suppress (mid-derivation, stuck loops)

Neither alone suffices: tool-only models compact at bad moments; rubric-only cannot act. No fine-tuning required [TENTATIVE — JHU/Apple paper, seven open-weight models].

**Results (paper claims):** matches or beats fixed-interval summarization at 30–70% lower token cost; +18.1 pts math, +5–9 pts agentic search vs no-summarization baseline.

**Agent harness steal:**

| Cemini surface | Application |
|----------------|-------------|
| poker-arena Cursor sessions | Compact replay analysis traces before LLM Level-5 `decide()` audits |
| castle-sim Stagehand harness | Rubric-gated compaction on multi-turn playtest logs |
| OSINT ingest sessions | Replace blind 50k-token context dumps with sub-task-boundary compaction |

Pairs with @concepts/mcp-context-optimization.md (tool-output compression) and @entities/tools/headroom.md (proxy-level compression).

## Snippets

> "We propose SELFCOMPACT, a scaffold that allows the model itself to decide when and how to compact." [Source: arXiv:2606.23525 abstract (retrieved 2026-06-25)]

> "A lightweight rubric closes this gap, reframing when to compact as a capability that scaffolds can supply without training." [Source: arXiv:2606.23525 abstract (retrieved 2026-06-25)]
