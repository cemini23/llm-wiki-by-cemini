---
title: "GraphFlow — formally verifiable visual agent workflows (arXiv:2605.14968)"
type: source
tags: [source, arxiv, agent-workflows, formal-methods, healthcare, k59, ccc-routed]
keywords: [graphflow, proof-carrying, requires-ensures, temporal, durable-execution, agentic-reliability]
related:
  - concepts/graphflow-verifiable-agent-workflows.md
  - concepts/code-as-agent-harness.md
  - sources/agentic-harness-engineering.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - concepts/llm-agent-systems.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
read_status: skimmed
---

## Relations

- @concepts/graphflow-verifiable-agent-workflows.md — stub; ccc-wiki brief carries expansion
- @concepts/code-as-agent-harness.md — diagram-as-spec vs harness evolution (AHE)
- @sources/agentic-harness-engineering.md — observability-driven harness evolution contrast

## Raw Concept

- **Title**: GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation
- **Authors**: Drewry H. Morris, Luis Valles, Reza Hosseini Ghomi (MedFlow, Inc.)
- **Type**: arXiv:2605.14968, Jan 2026
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/2605.14968_graphflow-verifiable-workflows.pdf`
- **Retrieved**: 2026-05-23 (K59 sweep Tier-B)
- **Read status**: skimmed

## Narrative

**Problem:** Multi-step agentic workflows compound errors (~35% success at 90% per-step under independence). Visual workflow tools offer durability/observability but weak **semantic** guarantees; agents plan at inference time.

**GraphFlow:** workflow **diagram = executable spec** — compile-time **verified core** (acyclic/sequential subgraphs) with **requires/ensures** contracts, proof-checked before library admission; **durable runtime** (Temporal-like event log) for full diagrams including cycles/retries.

**Pilot:** 8,728 clinical workflow runs, 97.08% completion (prototype without verified core; failures = external integrations). Formal verified core **specified, under development**.

**Cross-wiki:** ccc-wiki (OpenSpec, harness verification, LangGraph durability patterns).

## Snippets

> "A ten-step process with 90% per-step reliability completes successfully only 35% of the time." [Source: 2605.14968_graphflow-verifiable-workflows.pdf p.1]

> "Proof-carrying workflow automations … must be satisfied before admission to the automation library." [Source: 2605.14968_graphflow-verifiable-workflows.pdf p.5]
