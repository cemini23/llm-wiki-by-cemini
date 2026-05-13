---
title: "Reviewer Agent — Inference-Time Feedback for Tool-Calling"
type: concept
tags: [concept, agent-architecture, tool-calling, llm-as-judge, conductor, inference-time-feedback, helpfulness-harmfulness, conductor-relevant]
keywords: [reviewer agent, inference-time feedback, provisional tool calls, o3-mini, deepseek-r1, GEPA, helpfulness, harmfulness, conductor-v2, multi-agent gating]
related:
  - sources/reinforced-agent-tool-calling-feedback.md
  - concepts/conductor-orchestrator.md
  - concepts/agent-memory-critique.md
  - concepts/agent-trajectory-triage-signals.md
  - concepts/deepseek-models.md
  - concepts/verbalized-sampling-llm-diversity.md
  - sources/verbalized-sampling-mode-collapse.md
  - concepts/rlhf-critic-bias.md
  - sources/rlhf-critic-bias-al-zawahreh-2026.md
  - sources/llms-get-lost-multi-turn-laban-2025.md
  - concepts/llms-get-lost-mitigation-audit.md
  - sources/react-yao-2022.md
maturity: validated
created: 2026-05-11
updated: 2026-05-13
---

## Relations

- `@sources/reinforced-agent-tool-calling-feedback.md` — primary source (Apple, Apr 2026)
- `@concepts/conductor-orchestrator.md` — Cemini's MCP orchestrator is the natural insertion point for a reviewer-agent stage
- `@concepts/agent-memory-critique.md` — adjacent literature on critique-based agent improvement
- `@concepts/agent-trajectory-triage-signals.md` — complementary post-hoc layer (this concept is inference-time; signals are post-trajectory)
- `@concepts/deepseek-models.md` — DeepSeek-R1 is the candidate Cemini reviewer; DeepSeek-V3 is the candidate base agent
- `@concepts/verbalized-sampling-llm-diversity.md` — third orthogonal Conductor layer (generation-time distribution; reviewer/signals are pre/post-call gates)
- `@sources/verbalized-sampling-mode-collapse.md` — VS paper source
- `@concepts/rlhf-critic-bias.md` — **structural justification for reviewer-agent investment** (K40): reviewer-agent is a partial **Mitigation 3 + Mitigation 4 implementation in miniature** (evidence-weighted critique + audit-trail disclosure). The asymmetric-penalty framework explains *why* an evaluator-gating-an-actor architecture matters: without it, every evaluative LLM call inherits structural negativity bias.
- `@sources/rlhf-critic-bias-al-zawahreh-2026.md` — RLHF Critic Bias source (Al-Zawahreh April 2026, draft maturity, Reference/Steal-from)

## Raw Concept

Extracted from the Apple "Reinforced Agent" paper (arXiv 2604.27233v1, Apr 2026). The paper proposes a specialized **reviewer agent** that evaluates a base agent's *provisional* tool call *before* execution, shifting the paradigm from post-hoc recovery to proactive course-correction. This page captures the pattern, the empirical envelope, and Cemini-specific application notes.

## Narrative

### The pattern

Standard tool-calling agents loop on `propose_call → execute_tool → observe_result → critique`. Errors caught at the `critique` stage are already side-effecting — money spent, orders placed, irreversible state mutated. The reviewer-agent pattern interposes a second model between `propose_call` and `execute_tool`:

```
base_agent.propose_call(query, context)
  → reviewer_agent.review(provisional_call, query, context)
    → (approve | revise(new_call))
  → execute_tool(approved_call)
```

The reviewer is a **distinct model**, ideally a reasoning-class model (o3-mini-class), with a prompt rubric covering directness/parsimony, completeness across multi-step requests, argument fidelity, threshold inclusivity defaults, units/scales normalization, and explicit error criteria.

### Empirical envelope

From the source paper:

| Axis | Headline |
|------|----------|
| BFCL irrelevance detection | **+5.5%** over baseline |
| τ²-Bench (multi-turn, stateful) | **+7.1%** over baseline |
| BFCL latency (mean) | **6.2× slower** single-turn |
| τ²-Bench duration (mean) | **2.4× slower** multi-turn |
| Reviewer model selection | o3-mini → **3.0:1** benefit:risk; GPT-4o → **2.1:1** |
| GEPA prompt-opt layer | adds **+1.5–2.8%** on top of reviewer |

The Helpfulness-Harmfulness framing is the paper's key methodological contribution:
- **Helpfulness**: fraction of base-agent errors that the reviewer corrects
- **Harmfulness**: fraction of *correct* base outputs that the reviewer degrades

A reviewer is net-positive iff helpfulness > harmfulness, but the *ratio* lets you tune the system (reviewer strictness, model class, prompt) against a single scalar.

### Architectural axes for tuning

Three orthogonal axes, all tunable without retraining the base agent:

1. **Reviewer model class** (reasoning vs non-reasoning). Reasoning models win materially.
2. **Reviewer prompt** (manual rubric vs GEPA-optimized). GEPA compounds on top of model selection.
3. **Reviewer trigger policy** (review every call vs selective gating on high-stakes calls). Paper reviews every call; production deployment will want a trigger filter to avoid the 6.2× single-turn latency hit.

### Cemini application

**Insertion point**: Conductor (Cemini's MCP orchestrator, see `@concepts/conductor-orchestrator.md`) already routes tool calls through an orchestrator node. Slot a reviewer stage between `provisional_tool_call` and `execute_tool`.

**Model assignment**:
- **Reviewer**: DeepSeek-R1 (reasoning-class, already in Cemini's pool) — natural o3-mini analogue
- **Base agent**: DeepSeek-V3 (fast, non-reasoning) — natural GPT-4o analogue

**Latency tolerability**: Cemini trading sessions are predominantly *multi-turn long-horizon* (a Polymarket weather thesis can run 40+ tool calls across 10+ minutes). The paper's 2.4× multi-turn amortization regime applies, not the 6.2× single-turn regime. For single-turn lookups (e.g., one-shot price quote), the reviewer should be **trigger-gated off** — only review on calls with side effects.

**Trigger policy (Cemini-specific)**:
- **Always review**: `place_order`, `withdraw`, `close_position`, `cancel_order`, anything mutating account state
- **Review on uncertainty**: tool calls where the base agent's confidence score is below a configurable threshold
- **Skip review**: read-only queries (`get_price`, `get_orderbook`, `get_news`)

This selective-trigger design recovers most of the single-turn latency floor while preserving the reviewer's gating benefit on the high-stakes minority of calls.

### Open questions

1. **Domain transfer**: does the o3-mini 3:1 benefit:risk hold on Cemini's finance-specific tool surfaces (Kalshi, Polymarket, IBKR)? Needs empirical measurement on Conductor production trajectories before broad rollout.
2. **GEPA fit**: Cemini's `skill_audit.py` v0.5 already uses LLM-as-judge for brief auditing. Can the same infrastructure be reused as the prompt-optimization layer for the reviewer? Reduces engineering surface.
3. **Reviewer cost ceiling**: if the reviewer runs at every high-stakes call, what's the total monthly DeepSeek-R1 cost on a typical Cemini trading load? Need a cost model before commit.
4. **Failure mode**: paper measures harmfulness as % of correct outputs degraded, but doesn't characterize *what kind* of degradation (false negatives vs over-cautious refusals). For finance, over-cautious refusals are particularly costly (missed trades). Need an audit pass on harmful-class trajectories specifically.

### Why this matters for the IP-sale-readiness thesis

Cemini's defensibility is the **stack architecture**, not any individual model. A reviewer-agent layer is exactly the kind of architecturally-distinctive component that strengthens the moat: it produces measurable benefit:risk ratios that are quotable in a sale prospectus, it composes with the existing Conductor design, and it's tunable along three axes without retraining a base model. Phase-0 prototype is ~200-400 LOC.

### Pairing with trajectory triage

This concept is the **inference-time** half of a complete agent-quality stack. Its complement is `@concepts/agent-trajectory-triage-signals.md` — cheap non-LLM signals computed *after* trajectory close-out to triage which trajectories are worth human review or RLHF preference data. Reviewer agent improves trajectories while they happen; signals select which trajectories matter for downstream learning.

## Snippets

> "We move evaluation into the execution loop at inference time: a specialized reviewer agent evaluates provisional tool calls prior to execution, shifting the paradigm from post-hoc recovery to proactive evaluation and error mitigation." [Source: Reinforced Agent.pdf p.1]

> "Our metrics reveal that reviewer model choice is critical: the reasoning model o3-mini achieves a 3:1 benefit-to-risk ratio versus 2.1:1 for GPT-4o." [Source: Reinforced Agent.pdf p.1]

[Sources: @sources/reinforced-agent-tool-calling-feedback.md (arXiv 2604.27233v1)]
