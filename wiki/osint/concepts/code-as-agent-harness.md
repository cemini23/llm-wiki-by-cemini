---
title: "Code as agent harness — executable, verifiable, stateful agents"
type: concept
tags: [concept, agent-harness, coding-agents, agentic-ai, survey-synthesis]
keywords: [code-as-agent-harness, harness-interface, harness-mechanisms, multi-agent-coordination, verification, stateful-agents]
related:
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md
  - entities/tools/rocketsmith.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/generator-verifier-inference-time-steering.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
  - concepts/cemini-ai-assistant.md
  - sources/arxiv-self-healing-llm-agents-2605.06737.md
  - sources/arxiv-grep-agent-harness-2605-15184.md
  - sources/arxiv-skillrae-agent-skills-2605.10114.md
  - sources/arxiv-graphflow-verifiable-workflows-2605.14968.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - sources/arxiv-weavebench-2606.09426-2026-06-11.md
  - sources/arxiv-siga-scientific-sim-adapters-2606.09774-2026-06-11.md
  - concepts/agentified-agent-assessment.md
  - sources/arxiv-agentbeats-aaa-assessment-2606.13608-2026-06-12.md
  - concepts/agents-all-the-way-down-methodology.md
  - sources/arxiv-agents-all-the-way-down-2606.11869-2026-06-16.md
  - sources/arxiv-claw-swe-bench-2606.12344-2026-06-16.md
  - concepts/claw-swe-bench-harness-evaluation.md
  - entities/tools/claw-swe-bench.md
  - sources/arxiv-harnessfix-trace-repair-2606.06324-2026-06-16.md

maturity: draft
created: 2026-05-21
updated: 2026-06-16
---

## Relations

- @sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — **physical-domain harness** (K105): skills + subagents + MCP over OpenRocket/build123d; flight-test oracle
- @entities/tools/rocketsmith.md — MIT plugin; REFERENCE-only for Cemini
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — primary synthesis source (UIUC/Meta/Stanford survey, May 2026)
- @sources/arxiv-continual-harness-self-improving-agents-2605.09998.md — online reset-free harness refinement (embodied agents; refiner loop analogue)
- @concepts/continual-harness-online-self-improvement.md — K72 synthesis
- @concepts/llm-agent-systems.md — parent cluster
- @sources/agentic-harness-engineering.md — complementary: observability-driven harness *evolution*
- @sources/arxiv-grep-agent-harness-2605-15184.md — retrieval/harness interaction (PwC, May 2026)
- @concepts/cemini-ai-assistant.md — Cemini user-facing agent should map to harness-interface + verification layers
- @sources/arxiv-self-healing-llm-agents-2605.06737.md — runtime failure detection + corrective replanning atop harness execution

## Raw Concept

Prompted by Tier-2 sweep ingest of arXiv:2605.18747 — a 102-page survey codifying the industry shift from "LLMs that write code" to "code as the infrastructure layer agents run on."

## Narrative

### Three-layer model (from survey)

| Layer | What it covers | Cemini mapping |
|-------|----------------|----------------|
| **Harness interface** | Code linking reasoning ↔ action ↔ environment | Conductor routing + MCP tool calls + kb-server reads |
| **Harness mechanisms** | Planning, memory, tools, feedback control | Stash episodic memory; lazy-tool catalog; reviewer loops |
| **Scaling the harness** | Multi-agent shared artifacts | Prod MCP + server-Claude vs laptop wiki curator |

### Design imperatives for Cemini

- **Executable** — proposed actions must compile to verifiable tool calls (Cemini AI confirm gate).
- **Verifiable** — harness changes need regression checks (skill_audit, MCPT for strategies).
- **Stateful** — shared state across turns (stash, wiki log, hot.md) without silent drift.

### Physical-domain instance (K105)

@sources/arxiv-rocketsmith-agentic-rocketry-2606.00097-2026-06-08.md — RocketSmith wraps OpenRocket (sim source of truth) → build123d (parametric STEP) → PrusaSlicer (weight oracle). Same three-layer model: harness interface = MCP tools; mechanisms = 6 subagents + 7 skills; scaling = GUI read mirror + human-in-the-loop for slicing/recovery timing. **Steal:** deterministic codegen + programmatic mass check ≈ backtest/replay gates before prod.

### Open problems called out in source (actionable)

Evaluation beyond final success; verification with partial feedback; regression-free harness edits; multi-agent state consistency; human oversight for finance actions.

## Snippets

> "Programs are increasingly used as the medium through which agents reason, act, model environments, and verify execution."
> — [Source: 2605.18747_code-as-agent-harness-survey.pdf p.1]
