---
title: "Reinforced Agent — Inference-Time Feedback for Tool-Calling Agents (Apple, Apr 2026)"
type: source
tags: [source, agent-architecture, tool-calling, llm-as-judge, multi-agent, apple, conductor-relevant]
keywords: [reviewer agent, inference-time feedback, tool calling, BFCL, tau2-Bench, helpfulness-harmfulness, GEPA, o3-mini, Apple]
related:
  - concepts/reviewer-agent-inference-time-feedback.md
  - concepts/conductor-orchestrator.md
  - concepts/agent-memory-critique.md
maturity: validated
read_status: deep-read
created: 2026-05-11
updated: 2026-05-11
---

## Relations
- `@concepts/reviewer-agent-inference-time-feedback.md` — pattern extracted from this paper
- `@concepts/conductor-orchestrator.md` — Conductor is Cemini's MCP-call orchestrator; reviewer-agent pattern slots in upstream of `execute_tool()`
- `@concepts/agent-memory-critique.md` — adjacent agent-critique literature

## Raw Concept

- **Title**: Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents
- **Authors**: Anh Ta, Junjie Zhu, Shahin Shayandeh (Apple)
- **Type**: Academic paper (cs.AI)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Reinforced Agent- Inference-Time Feedback for Tool-Calling Agents.pdf`
- **arXiv**: 2604.27233v1 (29 Apr 2026)
- **sha256**: `352a4f39ae64d077…` (preingest verdict: NEW)
- **Pages**: 12
- **Read-status**: deep-read

## Narrative

A specialized **reviewer agent** evaluates **provisional tool calls** from the base agent *before* execution, shifting the paradigm from post-hoc recovery to proactive course-correction. The reviewer can revise the call or approve it; only approved calls hit the tool interface. Clear separation of concerns: base agent (GPT-4o-class executor) versus review agent (o3-mini-class reasoner).

### Headline results

| Benchmark | Baseline | + Reviewer | Δ |
|-----------|---------:|-----------:|---:|
| BFCL irrelevance detection | — | — | **+5.5%** |
| τ²-Bench (multi-turn, stateful) | — | — | **+7.1%** |
| BFCL latency (mean) | 1.27 s | 7.87 s | **6.2× slower** |
| τ²-Bench duration (mean) | 158.7 s | 384.3 s | **2.4× slower** |

The latency tradeoff differs sharply by mode: in multi-turn the reviewer overhead amortizes across ~40 turns/episode, dropping marginal cost dramatically.

### Helpfulness-Harmfulness metrics (paper's key contribution)

Reviewer agents can introduce errors while correcting others. Authors quantify both:

- **Helpfulness**: % of base-agent errors that reviewer feedback corrects
- **Harmfulness**: % of correct base responses that reviewer feedback degrades

These metrics enable systematic reviewer-design optimization. Findings:
- **o3-mini reviewer**: **3.0:1 benefit-to-risk ratio**
- **GPT-4o reviewer**: **2.1:1 benefit-to-risk ratio**
- Reasoning models materially outperform non-reasoning models in the reviewer role.

### GEPA prompt-optimization layer

Automated prompt optimization via GEPA adds an additional **+1.5–2.8%** on top of the reviewer alone. This compounds with reviewer model selection — both axes (model + prompt) can be improved without retraining the base agent.

### Cemini significance

**HIGH-fit** for Conductor + FastMCP. The architecture lines up:
- Cemini's Conductor already routes MCP tool calls through an orchestrator node
- Slot a reviewer-agent step between `provisional_tool_call` and `execute_tool` — reviewer ingests the call + relevant user-intent context, returns approve/revise
- DeepSeek-R1 (Cemini's reasoning model) is the natural reviewer; DeepSeek-V3 (fast) stays in the base-agent slot
- Latency tradeoff is workable: most Cemini calls are not single-turn (they're long-horizon trading sessions), so the 2.4× multi-turn amortization regime applies, not the 6.2× single-turn regime

**Open questions for Cemini adoption**:
1. Does the harmfulness rate hold for finance-specific tool surfaces (Kalshi/Polymarket/IBKR)? Need empirical measurement on production trajectories.
2. Can the reviewer be selectively triggered — e.g., only on high-stakes calls (`place_order`, `withdraw`) and skipped on read-only queries — to recover latency on hot paths?
3. GEPA integration: does the existing skill_audit.py LLM-as-judge prompt infrastructure provide an entry point?

### Snippets

> "We move evaluation into the execution loop at inference time: a specialized reviewer agent evaluates provisional tool calls prior to execution, shifting the paradigm from post-hoc recovery to proactive evaluation and error mitigation." [Source: Reinforced Agent.pdf p.1 (Abstract)]

> "These metrics directly inform reviewer design by revealing whether a given model or prompt provides net positive value." [Source: Reinforced Agent.pdf p.1 (Abstract)]

> "Our metrics reveal that reviewer model choice is critical: the reasoning model o3-mini achieves a 3:1 benefit-to-risk ratio versus 2.1:1 for GPT-4o." [Source: Reinforced Agent.pdf p.1 (Abstract)]

### Reviewer prompt skeleton (from supplementary materials)

The paper documents a reusable reviewer rubric covering: directness/parsimony, completeness across multi-step requests, argument fidelity, threshold inclusivity defaults, units/scales normalization, and error criteria. Worth lifting verbatim as the v0 Cemini reviewer prompt — full prompt is in the paper's supplementary materials [Source: Reinforced Agent.pdf p.10].

[Source: Reinforced Agent- Inference-Time Feedback for Tool-Calling Agents.pdf, arXiv:2604.27233v1]
