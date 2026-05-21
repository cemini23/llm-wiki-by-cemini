---
title: "Inference scaling for reasoning LLMs (arXiv:2605.19775)"
type: source
tags: [source, arxiv, llm-inference, reasoning-models, systems, k48]
keywords: [inference-scaling, chain-of-thought, kv-cache, data-parallelism, tensor-parallelism, pipeline-parallelism, capacity-bound, deepseek-r1, llama-405b]
clusters: [llm-agents, infrastructure]
related:
  - concepts/mcp-context-optimization.md
  - concepts/librarian-server-architecture.md
  - entities/tools/lazy-tool.md
  - entities/infrastructure/cemini-egress-fi.md
maturity: draft
read_status: skimmed
created: 2026-05-21
updated: 2026-05-21
---

## Relations

- @concepts/mcp-context-optimization.md — orthogonal axis: MCP reduces tool/context bloat; this paper addresses KV **capacity wall** on long CoT reasoning
- @entities/tools/lazy-tool.md — tool-schema compression (orthogonal to KV capacity wall)
- @concepts/librarian-server-architecture.md — deployment sizing for librarian Ollama / future reasoning workloads on Hetzner
- @entities/infrastructure/cemini-egress-fi.md — K48 adoption posture: API-only gateway on 4 GB Helsinki box; no local long-CoT weights

## Raw Concept

- **Title**: Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles
- **Authors**: Moiz Arif (Micron), Avinash Maurya, Sudharshan Vazhkudai (Micron), Bogdan Nicolae (Argonne)
- **Type**: arXiv preprint — arXiv:2605.19775
- **Submitted**: 2026-05-21 (per sweep)
- **Retrieved**: 2026-05-21 (Tier-2 sweep `@sweeps/2026-05-21.md`, Tier-B)
- **Pages**: 14
- **Read status**: skimmed (abstract + introduction)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.19775_inference-scaling-reasoning-llms.pdf`

## Narrative

System characterization of **reasoning-centric LLMs** (long CoT traces) vs standard generative workloads. Reasoning shifts inference into a **capacity-bound** regime (KV-cache fragmentation, early throttling). Evaluates 8B–671B models on GPU clusters across data/tensor/pipeline parallelism.

**Findings [TENTATIVE — skim]**: Data parallelism throughput-efficient for small models but hits a **capacity trap** on reasoning workloads; tensor parallelism unlocks stranded memory (~32B crossover); frontier dense (Llama-405B) interconnect/memory-bandwidth bound (favor high TP); sparse MoE (DeepSeek-R1) routing/sync limited (hybrid strategies).

**Cemini relevance**: Informs whether to host long-horizon reasoning on `cemini-egress-fi` vs API-only — pairs with MCP context optimization, not a substitute.

## Snippets

> "Unlike traditional workloads dominated by compute-bound prefill, reasoning workloads generate long chains of reasoning tokens that shift inference into a Capacity-Bound regime."
> — [Source: 2605.19775_inference-scaling-reasoning-llms.pdf p.1]

> "Data parallelism is throughput efficient for small models but hits a capacity trap on reasoning workloads as KV-cache fragmentation forces early throttling."
> — [Source: 2605.19775_inference-scaling-reasoning-llms.pdf p.1]
