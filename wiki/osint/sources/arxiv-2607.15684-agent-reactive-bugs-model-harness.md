---
title: "arXiv 2607.15684 — Agent-Reactive Bugs at the Model-Harness Boundary"
type: source
tags: [source, arxiv, agent-harness, reliability, k177, ccc]
keywords: [2607.15684, agent-reactive-bugs, AR-bugs, Codex, Gemini-CLI, LangChain, CrewAI]
related:
  - concepts/agent-reactive-bugs.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-20
updated: 2026-07-20
clusters: [k177-ingest]
---

## Relations

- @concepts/agent-reactive-bugs.md — taxonomy hub
- @concepts/code-as-agent-harness.md — harness layer parent

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2607.15684 |
| **sha256** | `6a5bea273c56a0812d066c42f5d0d8b4ebfdd254aa28bd00043af04792c7ff73` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2607.15684-understanding-agent-reactive-bugs-at-the-model-h.pdf` |

## Narrative

First empirical study of **agent-reactive (AR) bugs**: failures that appear only when a particular LLM response elicits an abnormal harness reaction (not attributable to model-alone or harness-alone inspection). Manual analysis of 255 issues across Codex, Gemini-CLI, LangChain, CrewAI; AR ≈ 8.4% of actively discussed issues. Many are **silent** (weak oracles); stochasticity hurts reproduction. Users push harness guardrails; developers often blame the LLM. **Steal:** design test oracles + reproduction harnesses that pin model outputs; fault-localize at the interaction boundary. **Poker / CCC:** decide() and Cursor harnesses need AR-aware regression — silent wrong tool routing is the hazard class.
