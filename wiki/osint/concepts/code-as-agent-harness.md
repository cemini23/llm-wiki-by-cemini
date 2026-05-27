---
title: "Code as agent harness — executable, verifiable, stateful agents"
type: concept
tags: [concept, agent-harness, coding-agents, agentic-ai, survey-synthesis]
keywords: [code-as-agent-harness, harness-interface, harness-mechanisms, multi-agent-coordination, verification, stateful-agents]
related:
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/llm-agent-systems.md
  - sources/agentic-harness-engineering.md
  - concepts/cemini-ai-assistant.md
  - sources/arxiv-self-healing-llm-agents-2605.06737.md
  - sources/arxiv-grep-agent-harness-2605-15184.md
  - sources/arxiv-skillrae-agent-skills-2605.10114.md
  - sources/arxiv-graphflow-verifiable-workflows-2605.14968.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/graphflow-verifiable-agent-workflows.md

maturity: draft
created: 2026-05-21
updated: 2026-05-27
---

## Relations

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

### Open problems called out in source (actionable)

Evaluation beyond final success; verification with partial feedback; regression-free harness edits; multi-agent state consistency; human oversight for finance actions.

## Snippets

> "Programs are increasingly used as the medium through which agents reason, act, model environments, and verify execution."
> — [Source: 2605.18747_code-as-agent-harness-survey.pdf p.1]
