---
title: "arXiv 2608.03836 — RESUMECONTRACT checkpoint/interrupt semantics"
type: source
tags: [arxiv, agents, ccc, atto, k223]
keywords: [LangGraph, CrewAI, TLA+, exactly-once, consume-once]
related:
  - concepts/llm-agent-failure-telemetry-monitors.md
  - entities/tools/addyosmani-agent-skills.md
  - concepts/gpuology-genealogy-agent-kit.md
maturity: draft
created: 2026-08-05
updated: 2026-08-05
read_status: deep-read
---

## Relations

- @concepts/llm-agent-failure-telemetry-monitors.md
- @entities/tools/addyosmani-agent-skills.md
- @concepts/gpuology-genealogy-agent-kit.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics |
| Author | Sajjad Khan |
| arXiv | 2608.03836 |
| sha256 | `397dfcc50bbe9ba595c98ba9e1dc50165d47efdd91649d07384e6f2ce5eeb5cd` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.03836-resume-means-resume-a-machine-checked-conformanc.pdf` |
| read_status | deep-read |

## Narrative

Six persistence properties (prefix continuation, effect exactly-once, fork determinism, checkpoint validity, consume-once, recovery determinism) + TLA+ + 39-cell fault matrix. Measured: LangGraph 1.2.9 re-executes after SIGKILL / silent invalid state; CrewAI 1.15.2 re-executes completed effects; pydantic-graph cannot resume mid-node crash; concurrent consume-once fails (k racers → k effects). **CCC/Atto harness:** steal contract checklist before trusting workflow persistence; no clone (paper-only).
