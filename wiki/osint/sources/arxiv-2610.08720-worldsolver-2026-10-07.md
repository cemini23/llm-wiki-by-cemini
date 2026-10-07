---
title: "WorldSolver: can LLM agents simulate physical dynamics via solver generation? (arXiv 2610.08720)"
type: source
tags: [source, k284, arxiv, game-dev, agents, physics, eval]
keywords: [worldsolver, physics-solver, simulation, benchmark, gpt-5.6-sol, claude-opus-5, visual-fidelity]
related:
  - concepts/k284-arxiv-wave.md
  - concepts/agent-tool-use-verification.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-arxiv-wave.md
- @concepts/agent-tool-use-verification.md

## Raw Concept

| Title | WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation? |
| Authors | Siru Jiang et al. (NLPR & MAIS, CASIA; PKU; Huawei Noah's Ark Lab) |
| Type | arXiv preprint (cs.AI) — benchmark |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.08720-worldsolver-can-llm-agents-simulate-the-physical.pdf` |
| Retrieved | 2026-10-07 |
| arXiv | 2610.08720v1 |
| Code | `github.com/sirujiang/WorldSolver` |
| read-status | read |

## Narrative

The first benchmark that frames **physics-solver generation as an agentic coding task** — physical understanding + mathematical formalisation + software engineering.

### Method

**168 tasks from 61 classic computer-graphics papers across 7 physical domains.** Each task gives a natural-language description `d` and a fixed code scaffold `S = (G, P, E, R)` (geometry, physics params, execution protocol, rendering). The agent implements a solver `Φ = A(d, S)`; then `s_{t+1} = Φ(s_t)` yields a trajectory `τ` and a rendered video `v = R(τ)`. Three evaluation axes: **Execution Checks**, **Visual Fidelity** (VLM-scored, 4 dims), **Physical Plausibility** (violation functions on physical laws).

### Results — frontier agents struggle

| Agent | Overall |
|-------|---------|
| GPT-5.6-Sol | **48.7%** |
| Claude-Opus-5 | **46.7%** |
| Gemini-3.7-Flash | 29.3% |
| most others | ~20–25% |

Producing *executable* solvers is hard; **visual and physical correctness is harder**.

### Why it matters here

A concrete **eval for coding agents on simulation/physics** — cloth, fluid, rigid-body solvers. Relevant to the Game-dev wiki (procedural effects) and to the agent-eval lane. Code at `sirujiang/WorldSolver`. **No license stated.**

## Snippets

> "Frontier agents struggle. GPT-5.6-Sol 48.7% overall, Claude-Opus-5 46.7%." [Source: arxiv-2610.08720-worldsolver-can-llm-agents-simulate-the-physical.pdf]

> "Producing executable solvers is hard; visual/physical correctness harder." [Source: arxiv-2610.08720-worldsolver-can-llm-agents-simulate-the-physical.pdf]
