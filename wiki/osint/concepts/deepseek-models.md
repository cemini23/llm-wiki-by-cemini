---
title: DeepSeek model family
type: concept
tags: [concept, llm-models, deepseek, model-selection, cemini-brain]
keywords: [deepseek, v3, v3.1, v4, r1, model-versions, performance-benchmarks, tool-use, financial-qa, cemini-brain]
related:
  - entities/infrastructure/deepseek-api.md
  - sources/tsag-2604.19633.md
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - entities/infrastructure/deepseek-r1-14b.md
maturity: draft
created: 2026-05-02
updated: 2026-05-02
---

## Relations

- @entities/infrastructure/deepseek-api.md — API infrastructure page; this page covers model capabilities and version lineage.
- @sources/tsag-2604.19633.md — TSAG evaluated DeepSeek-V3 alongside GPT-4o, Qwen2, Llama 3 on financial tool-use benchmarks.
- @concepts/llm-agent-systems.md — cluster hub; DeepSeek is Cemini's intended brain for agent orchestration.
- @concepts/conductor-orchestrator.md — Conductor orchestrator; model selection directly impacts routing and tool-use accuracy.
- @entities/infrastructure/deepseek-r1-14b.md — Local R1-14B attempt (retracted); cloud API is the operative path.

## Raw Concept

Catalog of DeepSeek model versions referenced across the wiki, their known capabilities, and their relevance to Cemini's tool-augmented agent architecture. Distinct from @entities/infrastructure/deepseek-api.md which covers connection details and API infrastructure.

## Narrative

### Known versions

| Model | Role | Cemini relevance |
|-------|------|-----------------|
| **DeepSeek-V3** | General-purpose LLM | Evaluated in TSAG benchmark for financial tool-use; baseline reference |
| **DeepSeek-V3.1** | Improved V3 | Referenced in training-free GRPO papers (Cai 2025, ICLR 2026) |
| **DeepSeek-V4-Pro** | Frontier model | Cemini's intended brain (Fireworks-hosted); referenced in Wave 5.1 link eval |
| **DeepSeek-V4-flash** | Fast inference variant | Polymarket MCP trading; latency-sensitive agent loops |
| **DeepSeek-R1-14B** | Reasoning model (small) | Local deployment attempted, retracted (7 GB RAM constraint) |
| **DeepSeek-R1-671B** | Reasoning model (large) | Referenced in ReaLM-Retrieve paper; completion-only API proxy pattern |

### Key performance signals

- **TSAG tool-use**: DeepSeek-V3 evaluated on financial tool-augmented QA; results alongside GPT-4o (MA 1.00) and Qwen2 7B (MA 1.00) per @sources/tsag-2604.19633.md.
- **Training-free GRPO**: DeepSeek-V3.1 used as base model for token-prior optimization — achieves GRPO-level output shifts without parameter updates per @sources/training-free-grpo-cai-2025.md and @sources/training-free-grpo-iclr-2026.md.
- **MoE architecture**: DeepSeek-V4-flash benefits from Mixture-of-Experts efficiency validated by @sources/moe-surpass-dense-equal-resource-li-2026.md (ICLR 2026 Oral) and @sources/moe-efficiency-leverage-tian-2026.md.

## Snippets

(Stub — populate as additional DeepSeek model evaluations are ingested.)
