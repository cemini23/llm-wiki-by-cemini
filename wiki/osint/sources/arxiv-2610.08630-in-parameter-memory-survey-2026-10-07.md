---
title: "In-Parameter Memory: A Survey (arXiv 2610.08630)"
type: source
tags: [source, k284, arxiv, agents, memory, survey, ccc]
keywords: [in-parameter-memory, ipm, kb-lam, titans, atlas, memgen, lora, delta-rule, rag, icl]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/agent-memory-critique.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/agent-memory-critique.md

## Raw Concept

| Title | In-Parameter Memory: A Survey — Towards In-Parameter Memory Augmentation for Large Language Models |
| Authors | Haoyu Huang et al. (HKUST; HKBU) |
| Type | arXiv preprint (cs.CL) — survey |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08630-towards-in-parameter-memory-augmentation-for-lar.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08630v1 |
| Repo | `github.com/HKUST-KnowComp/Awesome-In-Parameter-Memory` |
| read-status | read |

## Narrative

A survey of **in-parameter memory (IPM)**: reusable memory **written into model parameters or adapters**, composed into the forward pass at inference. It is the third memory axis beside **in-context learning (ICL)** and **RAG**.

### Framework

Two orthogonal axes:

- **Parameter Placement:** Embedding / Attention / FFN / Hybrid.
- **Parameter Acquisition Time:** online vs offline.

Formalised with a memory object **ϕ**, an acquisition operator **A**, and an augmentation operator **C**:

    ϕt = A(ϕt−1, zt),   yt ~ p_{C(θ, ϕt)}(yt | x≤t)

One-shot (`ϕ = A(K)`) vs stateful acquisition (delta-rule, surprise-driven updates). Audits ~100 methods: **KBLaM, Titans, ATLAS, MemGen, LoRA**, and more.

### The scope test

A paradigm qualifies as IPM **only if** it is parametric **and** independently acquired **and** augmented at deployment. That excludes plain ICL-RAG and an unmodified KV cache.

### Why it matters here

The wiki tracks agent memory across several pages. This survey gives the **taxonomy and the boundary rule** — useful for judging memory claims and for the `agent-memory-critique` thread. Conceptual (no benchmarks). **No license stated.** Route to CCC.

## Snippets

> "A paradigm qualifies only if parametric AND independently acquired AND augmented at deployment — excludes ICL-RAG and unmodified KV cache." [Source: arxiv-2610.08630-towards-in-parameter-memory-augmentation-for-lar.pdf]

> "ϕt = A(ϕt−1, zt), yt ∼ pC(θ,ϕt)(yt | x≤t)." [Source: arxiv-2610.08630-towards-in-parameter-memory-augmentation-for-lar.pdf]
