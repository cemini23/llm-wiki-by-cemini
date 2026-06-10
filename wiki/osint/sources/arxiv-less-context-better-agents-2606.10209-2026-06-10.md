---
title: Less Context, Better Agents — efficient context engineering (arXiv 2606.10209)
type: source
tags: [source, arxiv, llm-agents, context-engineering, mcp, enterprise-automation]
keywords: [2606.10209, context-pruning, conversation-summarization, MCP, D365, token-efficiency, GPT-5]
related:
  - concepts/context-compression-resume-pattern.md
  - concepts/llm-agent-systems.md
  - concepts/librarian-server-architecture.md
  - concepts/conductor-orchestrator.md
maturity: validated
read_status: deep-read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- @concepts/context-compression-resume-pattern.md — empirical validation of prune + summarize stack
- @concepts/llm-agent-systems.md — cluster hub
- @concepts/librarian-server-architecture.md — kb-server / conductor long-horizon tool loops
- @concepts/conductor-orchestrator.md — orchestration target for context budget policy

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents |
| **Authors** | Abhilasha Lodha et al. (Microsoft) |
| **arXiv** | 2606.10209 (cs.AI) |
| **Pages** | 17 |
| **sha256** | `31aa21cfc78d1528d07752527b6039720bc8b31eb82906a6c55a40e41fe98a5d` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.10209-less-context-better-agents-efficient-context-eng.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | deep-read — abstract, C1–C4 configs, headline metrics, discussion |

## Narrative

Controlled study of **context engineering** for MCP-connected agents automating hotel expense itemization in **Microsoft Dynamics 365 F&O**. Four configurations on GPT-5 (50-task benchmark, 5 runs, user model held constant C2–C4):

| Config | Description | Complete itemization | Tokens | Wall time |
|--------|-------------|---------------------|--------|-----------|
| C1 | No user model (ablation) | 8.0% | — | — |
| C2 | Full conversation history | 71.0% | 1,480,996 | 14.56 h |
| C3 | Prune to last **5** tool call/response pairs | 79.0% | 535,274 (−63.9%) | 5.39 h |
| C4 | C3 + automated summarization (window **3**) | **91.6%** | 553,374 | 5.79 h |

**Key finding:** selective retention of recent tool interactions beats full history on **both** accuracy and cost. Summarization closes the gap on tasks requiring long-range dependencies (C3→C4: +12.6 pp complete itemization for +3.4% tokens vs C3 alone).

Extended analyses: 95% CIs, sensitivity over pruning window N and summary window W, per-category failure taxonomy, generalization across five expense types and **Claude Sonnet 4.5** `[TENTATIVE — paper claims cross-model; not independently verified here]`.

**Scope limits (authors explicit):** one enterprise ERP workflow class; not proof of universal generalization.

**Cemini implications:**

| Takeaway | Stack target |
|----------|--------------|
| Full MCP tool history is suboptimal | Conductor / kb-server multi-hop sessions |
| Last-N tool pairs + rolling summary | `@concepts/context-compression-resume-pattern.md` prescribed-not-built gap |
| C3 as cost-sensitive operating point | 79% at ~same tokens as full context but 2.77× cheaper than C2 |

**Posture:** REFERENCE — steal the **N=5 / W=3** starting hyperparameters for conductor context budget experiments; pair with existing CPR pattern page. Brief staged for prod evaluation (not auto-scp).

## Snippets

> "Context pruning to the last 5 tool calls achieved 79.0% complete itemization with 535,274 tokens—a 63.9% reduction—in 5.39 hours. Adding automated summarization achieved 91.6% complete itemization and 99.64% average amount itemized with 553,374 tokens in 5.79 hours."

> — [Source: arxiv-2606.10209-less-context-better-agents-efficient-context-eng.pdf Abstract, retrieved 2026-06-10]

> "Selective retention of recent tool interactions is more decision-relevant than full history while dramatically reducing token consumption."

> — [Source: arxiv-2606.10209 Abstract, retrieved 2026-06-10]

> "C3 (pruning without summarization) represents a secondary operating point for cost-sensitive deployments: 79.0% task completion at baseline-equivalent token cost, compared to 71.0% for full context at 2.77× the cost."

> — [Source: arxiv-2606.10209 Discussion, retrieved 2026-06-10]
