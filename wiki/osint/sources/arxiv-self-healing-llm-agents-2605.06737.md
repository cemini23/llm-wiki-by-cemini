---
title: "Self-healing framework for LLM agents (arXiv:2605.06737)"
type: source
tags: [source, arxiv, llm-agents, reliability, fault-tolerance, k48]
keywords: [self-healing, failure-detection, reliability-assessment, adaptive-replanning, corrective-prompting, multi-agent-workflow]
clusters: [llm-agents]
related:
  - concepts/llm-agent-systems.md
  - concepts/cemini-ai-assistant.md
  - sources/agentic-harness-engineering.md
  - concepts/code-as-agent-harness.md
  - concepts/cemini-knowledge-application-architecture.md
maturity: draft
read_status: skimmed
created: 2026-05-21
updated: 2026-05-31
---

## Relations

- @concepts/llm-agent-systems.md — reliability layer for long-horizon agents
- @concepts/cemini-ai-assistant.md — failure detection + recovery for user-facing assistant sessions
- @sources/agentic-harness-engineering.md — harness evolution vs runtime self-healing (complementary)
- @concepts/code-as-agent-harness.md — verification + feedback control in harness mechanisms

## Raw Concept

- **Title**: A Self-Healing Framework for Reliable LLM-Based Autonomous Agents
- **Authors**: Cheonsu Jeong (Samsung SDS), Younggun Shin (Yonsei University)
- **Type**: arXiv preprint — arXiv:2605.06737
- **Submitted**: 2026-05-07
- **Retrieved**: 2026-05-21 (Tier-2 sweep `@sweeps/2026-05-21.md`, Tier-B)
- **Pages**: 13
- **Read status**: skimmed (abstract + introduction)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.06737_self-healing-llm-agents.pdf`

## Narrative

Proposes a **reliability-aware self-healing** loop: failure taxonomy → quantitative reliability model → pattern-based failure detection (execution traces + output consistency) → recovery via adaptive replanning and corrective prompting. Implemented in a multi-agent workflow environment; claims higher task success, less failure propagation vs baselines.

**Distinctive claim [TENTATIVE]**: Integrates **internal reasoning traces** with **external execution results** in one monitoring system — relevant to Cemini's stash + tool-outcome logging for assistant sessions.

**Cemini relevance**: Design patterns for Cemini AI confirm-gate retries and conductor worker failures — not a drop-in library; evaluate against existing reviewer/retry loops before adoption.

## Snippets

> "The framework integrates failure detection, reliability assessment, and automated recovery mechanisms."
> — [Source: 2605.06737_self-healing-llm-agents.pdf p.1]

> "This study distinguishes itself by establishing an integrated monitoring system that combines the agent's internal reasoning process with external execution results."
> — [Source: 2605.06737_self-healing-llm-agents.pdf p.1]
