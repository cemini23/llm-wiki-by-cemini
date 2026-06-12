---
title: SIGA — self-evolving coding-agent adapters for scientific simulation (arXiv 2606.09774)
type: source
tags: [source, arxiv, coding-agents, scientific-simulation, adapter, grounding]
keywords: [2606.09774, SIGA, GEOS, simulator-interface-grounding, procedural-memory, validation]
related:
  - concepts/llm-agent-systems.md
  - concepts/code-as-agent-harness.md
maturity: validated
read_status: skimmed
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- @concepts/llm-agent-systems.md — adapter-over-reimplementation pattern
- @concepts/code-as-agent-harness.md — thin wrapper on frontier coding agents

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation |
| **arXiv** | 2606.09774 |
| **sha256** | `2499663106a94f9792b11573df096c657e4b9c2b3ffd3004e08f81c1d111c9a7` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/arxiv-2606.09774-siga-self-evolving-coding-agent-adapters-for-sci.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | skimmed — abstract, four-component decomposition |

## Narrative

**SIGA** (Simulator-Interface Grounding Adapter) wraps an off-the-shelf coding agent with four slots: **retrieval** (docs/schemas/examples), **procedural memory** (vocabulary always visible), **in-trajectory validator**, and **validation-enforced termination** (stop-hook). Primary eval on **GEOS** multiphysics XML decks; transfers to OpenFOAM and LAMMPS.

Headline: ~5 min agent setup vs ~3 h human expert on representative GEOS task (~36× wall-clock); held-out TreeSim +10% relative vs bare agent; self-evolution rewrites adapter contents from prior trajectories.

**Cemini mapping:** STEAL-FROM pattern for **domain DSL grounding** (conviction.yaml, cross_venue.yaml, poker arena config) — adapt native Claude Code/Cursor harness instead of bespoke agent loops. REFERENCE only; no GEOS install. Pair with WeaveBench (2606.09426) for eval discipline.

## Snippets

> "Coding agents already know how to navigate files, edit code, run commands, and repair outputs, but they lack the simulator's executable contract."

> — [Source: arxiv-2606.09774-siga-self-evolving-coding-agent-adapters-for-sci.pdf Abstract, retrieved 2026-06-11]
