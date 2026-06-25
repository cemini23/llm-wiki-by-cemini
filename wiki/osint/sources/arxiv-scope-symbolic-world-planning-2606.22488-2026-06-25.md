---
title: "SCOPE — evolving symbolic world for open-ended planning (arXiv 2606.22488)"
type: source
tags: [source, arxiv, planning, symbolic-reasoning, embodied-ai, k129]
keywords: [2606.22488, SCOPE, SESim, SASMem, VLM, open-ended environments]
related:
  - concepts/active-project-research-routing.md
  - sources/arxiv-qwen-robotnav-2606.18112-2026-06-20.md
maturity: draft
read_status: read
created: 2026-06-25
updated: 2026-06-25
clusters: [llm-agents]
---

## Relations

- @concepts/active-project-research-routing.md — castle-sim / RTS planning weak hook

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SCOPE: Evolving Symbolic World for Planning in Open-Ended Environments |
| **Authors** | Yundaichuan Zhan et al. |
| **arXiv** | 2606.22488v1 (Jun 2026) |
| **sha256** | `5b7352b83dd115f6ea288f87bc1909b882a4b270be43b6fbd52039b5101d93c1` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2606.22488-2606-22488v1-scope-evolving-symbolic-world-for-p.pdf` |
| **Retrieved** | 2026-06-25 (inbox) |
| **Read status** | read (abstract + module architecture) |

## Narrative

VLM + classical planner pipelines fail when symbolic world models from perception are **incomplete** in open-ended settings.

**SCOPE** self-adaptively refines plans **and** evolves the symbolic world representation:

| Module | Role |
|--------|------|
| **SESim** | Symbolic execution simulator — validates plans, executes in real env, feedback refines plan + world model |
| **SASMem** | Self-Adaptive Symbolic Memory — distills feedback into evolving symbolic knowledge |

Improves world completeness, success under perturbations, cross-task grounding [TENTATIVE — paper experiments].

**Cemini steal:** **Symbolic world evolution loop** for castle-sim RTS — influence-map / planner state repair when perception incomplete; wiki-only until Godot slice validates.

## Snippets

> "SCOPE comprises two synergistic modules: a Symbolic Execution Simulator (SESim) … and a Self-Adaptive Symbolic Memory (SASMem)." [Source: arXiv:2606.22488 abstract (retrieved 2026-06-25)]

> "In open-ended environments, these symbolic representations obtained from perception are often incomplete, leading to suboptimal performance." [Source: arXiv:2606.22488 abstract (retrieved 2026-06-25)]

> "SCOPE significantly improves the completeness of the symbolic world, the success rate of plans under environment perturbations." [Source: arXiv:2606.22488 abstract (retrieved 2026-06-25)]

## Dead Ends

- Embodied VLM stack ≠ Godot 4 isometric slice — no install without game-dev brief GO.
