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
  - sources/blade-bayesian-listwise-alignment.md
  - concepts/llm-listwise-alignment.md
  - entities/tools/adala.md
  - concepts/reviewer-agent-inference-time-feedback.md
maturity: draft
created: 2026-05-02
updated: 2026-05-11
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

### Model family lineage (research / product history)

`api.deepseek.com` only exposes the V4 lineup as live model IDs. Earlier releases (V3, V3.1) and the R1 series are research artifacts or weight-only releases — referenced across the wiki for benchmarks and academic context but **not callable** via the production API. Audit verified 2026-05-04 against `api-docs.deepseek.com/quick_start/pricing`.

| Model | Role | API ID exposed? | Cemini relevance |
|-------|------|------------------|-----------------|
| **DeepSeek-V4-Pro** | Frontier model | ✅ `deepseek-v4-pro` | Cemini's intended frontier brain; final-decision synthesizer; referenced in Wave 5.1 link eval |
| **DeepSeek-V4-flash** | Fast inference variant; thinking-mode toggle via parameters (not separate model ID) | ✅ `deepseek-v4-flash` | Cemini analyst-node default; latency-sensitive agent loops; Polymarket MCP trading |
| **`deepseek-chat`** (legacy alias) | Legacy general-purpose alias | ⚠️ Functional but **deprecated** (will be removed in future API versions) | Avoid in new code; existing references being migrated |
| **`deepseek-reasoner`** (legacy alias) | Legacy reasoning alias | ⚠️ Functional but **deprecated** | Avoid in new code; reasoning is now parameter-toggled on `deepseek-v4-flash` |
| **DeepSeek-V3** | General-purpose LLM | ❌ Not on production API | Research reference: TSAG benchmark for financial tool-use; baseline |
| **DeepSeek-V3.1** | Improved V3 | ❌ Not on production API | Research reference: training-free GRPO papers (Cai 2025, ICLR 2026) |
| **DeepSeek-R1-14B** | Reasoning model (small, weights released) | ❌ Local-deployment-only; retracted from Cemini per `@retracted_deepseek_ollama` memory (7 GB RAM constraint) | Research reference |
| **DeepSeek-R1-671B** | Reasoning model (large, weights released) | ❌ Not on production API | Research reference: ReaLM-Retrieve paper; completion-only API proxy pattern |

### Key performance signals

- **TSAG tool-use**: DeepSeek-V3 evaluated on financial tool-augmented QA; results alongside GPT-4o (MA 1.00) and Qwen2 7B (MA 1.00) per @sources/tsag-2604.19633.md.
- **Training-free GRPO**: DeepSeek-V3.1 used as base model for token-prior optimization — achieves GRPO-level output shifts without parameter updates per @sources/training-free-grpo-cai-2025.md and @sources/training-free-grpo-iclr-2026.md.
- **MoE architecture**: DeepSeek-V4-flash benefits from Mixture-of-Experts efficiency validated by @sources/moe-surpass-dense-equal-resource-li-2026.md (ICLR 2026 Oral) and @sources/moe-efficiency-leverage-tian-2026.md.

## Snippets

(Stub — populate as additional DeepSeek model evaluations are ingested.)
