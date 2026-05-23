---
title: "GraphFlow — proof-carrying visual workflows for agentic automation"
type: concept
tags: [concept, agent-workflows, formal-verification, ccc-routed, k59]
keywords: [graphflow, requires-ensures, proof-carrying, durable-execution, swimlanes]
related:
  - sources/arxiv-graphflow-verifiable-workflows-2605.14968.md
  - concepts/code-as-agent-harness.md
  - sources/agentic-harness-engineering.md
  - sources/arxiv-code-as-agent-harness-survey-2605.18747.md
  - concepts/llm-agent-systems.md
  - ccc-wiki/concepts/graphflow-verifiable-agent-workflows.md
  - ccc-wiki/sources/arxiv-graphflow-2605.14968.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
---

## Relations

- @sources/arxiv-graphflow-verifiable-workflows-2605.14968.md — K59 source
- @concepts/code-as-agent-harness.md — complementary: harness evolution vs compile-time proofs
- @sources/agentic-harness-engineering.md — observability-driven harness tuning
- @sources/arxiv-code-as-agent-harness-survey-2605.18747.md — executable harness survey
- @ccc-wiki/concepts/graphflow-verifiable-agent-workflows.md — OpenSpec / LangGraph / Glasswing contrast
- @ccc-wiki/sources/arxiv-graphflow-2605.14968.md — CCC source provenance page

## Raw Concept

K59 stub for GraphFlow (2605.14968). Expanded in **ccc-wiki** — see `@ccc-wiki/briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md`.

## Narrative

Two-mode architecture:
- **Verified core** — restricted diagrams → reusable automations with machine-checked contracts.
- **Durable runtime** — full production graphs, append-only event log, replay.

**Cemini relevance:** design pattern reference for **high-stakes agent workflows** (conductor side-effecting tools), not near-term prod port. Contrast with @sources/agentic-harness-engineering.md (empirical harness search) vs **proof-before-admission**.

## Snippets

> "GraphFlow shifts planning into diagrams and contracts, then executes those diagrams under durable semantics with auditable traces." [Source: 2605.14968_graphflow-verifiable-workflows.pdf p.2]
