---
title: "Self-Compacting Language Model Agents — SelfCompact (arXiv 2606.23525)"
type: source
tags: [source, arxiv, agent-harness, context-compression, k129]
keywords: [2606.23525, SelfCompact, context compaction, meta-cognitive gap, agentic search]
related:
  - concepts/context-compression-resume-pattern.md
  - sources/arxiv-less-context-better-agents-2606.10209-2026-06-10.md
  - sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md
  - concepts/devfun-poker-agent-challenge-2026.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [llm-agents]
---

## Relations

- @concepts/context-compression-resume-pattern.md — Cemini context hygiene cluster
- @sources/arxiv-aohp-os-agent-harness-2606.23449-2026-06-23.md — agent harness papers (K128)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Self-Compacting Language Model Agents |
| **Authors** | Tianjian Li et al. |
| **arXiv** | 2606.23525v1 (Jun 2026) |
| **sha256** | `85209056d1b7ef74a1aca448a16902b5126ae0a9c7214d59a845aa78c4e3ebce` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.23525-2606-23525v1-self-compacting-language-model-agen.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + scaffold design) |

## Narrative

Long agent traces (CoT + tool calls) accumulate stale content and overflow context. Fixed-interval compaction at token thresholds ignores trajectory structure — risks discarding mid-derivation state.

**SelfCompact scaffold:**

1. **Compaction tool** — model invokes to summarize accumulated context
2. **Lightweight rubric** — when to fire (sub-task resolved, converging) vs suppress (mid-derivation, stuck)

Tool alone → uneven use; rubric alone → cannot act; together → adaptive compaction without fine-tuning [TENTATIVE].

**Results (6 benchmarks, 7 models):** matches/exceeds fixed-interval summarization at **30–70% lower token cost**; up to **+18.1** math points, **+5–9** agentic search vs no-summarization baseline [TENTATIVE].

**Meta-cognitive gap:** unprompted models poor at detecting context rot; rubric closes gap — "when to compact" as scaffold-supplied capability.

**Cemini steal:** Rubric-gated compaction for poker-arena + long ingest sessions — complements `@concepts/context-compression-resume-pattern.md` and headroom proxy (K129 tool eval).

## Snippets

> "SelfCompact, a scaffold that allows the model itself to decide when and how to compact." [Source: arXiv:2606.23525 abstract (retrieved 2026-06-25)]

> "The tool alone is unevenly used … the rubric alone cannot act. Together, they elicit effective adaptive compaction without any fine-tuning." [Source: arXiv:2606.23525 abstract (retrieved 2026-06-25)]

> "A lightweight rubric closes this gap, reframing when to compact as a capability that scaffolds can supply without training." [Source: arXiv:2606.23525 abstract (retrieved 2026-06-25)]

## Dead Ends

- Benchmark math/search ≠ prod conductor Redis streams — steal is rubric pattern, not drop-in middleware.
