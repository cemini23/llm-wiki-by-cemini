---
title: "MasRouter: Learning to Route LLMs for Multi-Agent Systems"
type: source
tags: [source, llm-agents, multi-agent-routing, model-selection, role-allocation, collaboration-mode, conductor-relevant]
keywords: [masrouter, multi-agent-system, llm-router, cascaded-controller, role-allocation, collaboration-mode, acl-2025]
related:
  - concepts/llm-agent-systems.md
  - concepts/conductor-orchestrator.md
  - concepts/scatter-gather-topology.md
  - sources/toolorchestra-2511.21689.md
  - sources/select-then-route-emnlp-2025.md
  - sources/meta-router-2509.25535.md
maturity: validated
created: 2026-05-01
updated: 2026-05-01
---

## Relations

- @concepts/llm-agent-systems.md — MasRouter extends routing from single-agent to multi-agent orchestration decisions.
- @sources/toolorchestra-2511.21689.md — ToolOrchestra trains orchestrators; MasRouter provides the multi-agent routing framework they can control.
- @concepts/conductor-orchestrator.md — Conductor is the synthesis concept; MasRouter provides the multi-agent routing extension.
- @concepts/scatter-gather-topology.md — MasRouter selects collaboration modes for scatter-gather agent topologies.
- @sources/select-then-route-emnlp-2025.md — StR routes single queries to models; MasRouter routes tasks to agent collaboration topologies.
- @sources/meta-router-2509.25535.md — Meta-Router's evaluation framework applies to multi-agent routing evaluation.
- @concepts/scatter-gather-topology.md — MasRouter's collaboration mode determination is a learned version of scatter-gather topology selection.

## Raw Concept

- Original title: MasRouter: Learning to Route LLMs for Multi-Agent Systems
- Author(s): Yanwei Yue, Guibin Zhang, Boyang Liu (Tongji Univ), Guancheng Wan (UCLA), Kun Wang (NTU), Dawei Cheng, Yiyan Qi (IDEA)
- Type: ACL 2025
- Location: https://aclanthology.org/2025.acl-long.757.pdf
- Retrieved: 2026-05-01 (K25 Conductor sweep)
- Read status: deep-read

## Narrative

MasRouter introduces the problem of Multi-Agent System Routing (MASR): jointly deciding collaboration mode, agent roles, AND which LLM backs each agent — all within a single routing framework. Previous routing work only handled single-agent LLM selection. MasRouter is the first to tackle the full multi-agent orchestration decision.

### Architecture

A cascaded controller network makes three decisions in sequence:

1. **Collaboration mode determination** — should agents work solo, in parallel, or with critic feedback?
2. **Role allocation** — which agent handles which sub-task?
3. **LLM routing** — which specific model backs each agent?

The cascade is inductive: it can handle new models and new collaboration modes not seen during training.

### Results

- **1.8–8.2% improvement** over SOTA on MBPP and other benchmarks
- **Up to 52.07% cost reduction** vs. always using the strongest model for every agent
- MMLU: 84.25% → 85.40%
- HumanEval: 90.62% → 91.41%
- GSM8K + MATH tested as well
- Inductive: when a new, stronger model is added to the pool, MasRouter routes to it without retraining

### Why this matters for Conductor

MasRouter extends the Conductor concept from single-query routing to full multi-agent orchestration. Cemini already uses a scatter-gather topology with multiple analysts — MasRouter provides the learned equivalent of manual topology selection.

Key design elements:
1. **Cascaded decisions** — collaboration mode → role allocation → LLM selection. Each decision constrains the next.
2. **Inductive routing** — works with unseen models. Critical for Cemini as new DeepSeek models release.
3. **52% cost reduction** — the "don't use GPT-5 for every sub-agent" argument in hard numbers.

## Snippets

**S1 — MASR definition**:
> "We first introduce the problem of Multi-Agent System Routing (MASR), which integrates all components of MAS into a unified routing framework."

**S2 — Cascaded controller**:
> "MasRouter employs collaboration mode determination, role allocation, and LLM routing through a cascaded controller network, progressively constructing a MAS that balances effectiveness and efficiency."

**S3 — Inductive property**:
> "When adding the new, stronger model, MasRouter improved the accuracy on MMLU from 84.25% to 85.40%."

**S4 — Cost reduction**:
> "Reducing overhead by up to 52.07% compared to baseline approaches."
