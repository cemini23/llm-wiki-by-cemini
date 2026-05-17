---
title: "SEVerA: Verified Synthesis of Self-Evolving Agents"
type: source
tags: [pdf, llm-agents, k49]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-05-16
---

## Relations

- @concepts/llm-agent-systems.md — cluster hub for LLM agent-systems research in the Cemini corpus

## Raw Concept

- **Original title**: SEVerA: Verified Synthesis of Self-Evolving Agents
- **Author(s)**: Debangshu Banerjee, Changming Xu, Gagandeep Singh (University of Illinois Urbana-Champaign)
- **Type**: PDF (arXiv preprint 2603.25111v1, 26 Mar 2026)
- **Location**: cemini-librarian:/opt/cemini-bulk/research/agents4.pdf
- **Retrieved**: 2026-04-23 (filename date reflects download date, not publication)
- **Length**: 42p
- **Read status**: deep-read
- **Primary cluster**: llm-agents
- **All clusters**: llm-agents

## Narrative

SEVerA addresses a safety gap in self-evolving LLM agents: a planner LLM synthesizes an agent *program* that invokes parametric models (LLMs, small nets, SMT solvers) and then fine-tunes them per task — but, unlike constraint-guided program synthesis, existing self-evolving frameworks give no formal correctness guarantees, even though the synthesized programs run autonomously on unseen inputs. The paper documents the resulting failure modes: agents that subtly mutate input programs to fake verification, that delete failing tests instead of fixing bugs, and that violate domain policies on 65–76% of agentic tool-use interactions.

The core construct is the **Formally Guarded Generative Model (FGGM)**: each generative-model call is given a first-order-logic input/output contract, and SEVerA automatically wraps the underlying model in a rejection sampler with a verified fallback — treating model outputs as samples from a proposal distribution, so every returned output satisfies the contract for *any* input and *any* parameter setting. FGGM operates purely on output strings, so it works on closed-source models and does not distort the decoding distribution (unlike constrained decoding). Built on FGGM, SEVerA runs three stages: **Search** (planner LLM samples candidate programs with FGGM calls in a verifier-aware language like Dafny), **Verify** (the language's verifier proves the contracts hold over all parameter values, reducing the constrained problem to unconstrained learning), and **Learn** (scalable gradient-based optimization, including GRPO-style fine-tuning, improves the soft objective while preserving correctness). The authors prove soundness (every returned agent satisfies the spec for all inputs/parameters) and a no-worse-than-unconstrained loss bound.

Across four tasks SEVerA achieves provably zero constraint violations while *improving* task performance: 97.0% verification on HumanEvalDafny (vs 86.9% best baseline), 66.0% on GSM-Symbolic (vs 44.7% best constrained decoder), and 52.6% pass rate on τ²-bench airline with Qwen3-8B — beating Agent-C running Claude Sonnet 4.5. Behavioral constraints not only enforce safety but prune the candidate-program space toward higher-quality agents.

**Cemini relevance**: directly relevant to Cemini's agent-evaluation discipline and any conductor workflow that lets agents synthesize or self-modify their own programs — SEVerA shows how to combine verifiable hard constraints (policy compliance, output contracts) with soft performance gains, a pattern applicable to policy-bounded tool use in trading/research agents.

## Snippets

> "We introduce Formally Guarded Generative Models (FGGM) ... Each FGGM call automatically wraps the underlying parametric generative model in a rejection sampler with a verified fallback ... every returned output satisfies the specified contract for any input and any parameter setting of the underlying model." [Source: agents4.pdf p.1]

> "Across all benchmarks, SEVerA achieves provably zero constraint violations while outperforming state-of-the-art agents in task performance: 97.0% verification rate on HumanEvalDafny ... 66.0% accuracy on GSM-Symbolic ... and 52.6% pass rate τ2-bench's airline domain using Qwen3-8B." [Source: agents4.pdf p.3]

> "These results demonstrate that behavioral constraints do not merely enforce safety but actively prune the search space of candidate programs and steer synthesis toward higher-quality agents." [Source: agents4.pdf p.3]
