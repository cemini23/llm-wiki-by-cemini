---
title: "ID-WM — hierarchical world models with implicit dynamics"
type: source
tags: [source, arxiv, world-models, planning, embodied, hierarchy]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Hierarchical World Models with Implicit Dynamics |
| Authors | Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun (NYU Courant, Meta-FAIR, AMI Labs) |
| arXiv | 2610.42146 |
| Pages | 26 |
| Read status | skimmed (abstract) |

## Narrative

Planning with world models generalises better than direct policy learning, but long horizons suffer from **cumulative error and search complexity**. Existing hierarchical methods use rigid macro-actions or latent skills, which produces brittle representations and limited fine-grained control.

**ID-WM** decouples **state-space reachability** from **local control**:

- A **high-level model** samples feasible transitions across the state manifold.
- A **low-level world model**, acting as an inverse dynamics solver, grounds those transitions into precise actions.

The planner can then identify reachable subgoals without being constrained by low-level execution detail.

Reported result: **38.5% improvement** over state-of-the-art policy and diffusion-based planners across three navigation and manipulation suites, with compounding errors mitigated by the hierarchy.

### The idea worth keeping

The high level answers **"where can I get to"**, the low level answers **"what actions get me there"**, and the split stops a long plan from being a very long sequence of exact actions.

That is the same decomposition that makes a multi-stage agent project survivable — DeliverBench in this batch measures what happens without it, where every stage inherits the previous stage's errors.

**Caveat.** Abstract only. The 38.5% is their benchmark suite.

## Snippets

> "Our framework utilizes a high-level model to sample feasible transitions across the state manifold and a low-level world model as an inverse dynamics solver to ground these transitions into precise actions." [Source: arxiv-2610.42146 p.1]

## Dead Ends

- **Citing 38.5% outside their suites.** Their benchmarks.
