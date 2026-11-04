---
title: "Ask, Don't Equip — direction as a hypothesis beats more tooling"
type: source
tags: [source, arxiv, agents, kernel-optimization, hypothesis, search]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Ask, Don't Equip: Question-Driven Coding Agents for Deep Kernel Optimization |
| Authors | Gabriele Oliaro, Jaeseong Lee, Zhaoyuan Su, Sreeram Vennam, Zhihao Jia, Samyam Rajbhandari |
| arXiv | 2611.03517 |
| Pages | 29 |
| Read status | skimmed (abstract) |

## Narrative

The setting is GPU kernel optimisation, where agents sit on a structure-versus-freedom tradeoff:

- **Scripted agents** fix what the model does at each step — a learned policy, an optimisation menu, fixed roles. Sample-efficient where the recipe applies, stalled where it does not.
- **Open-ended agents** let the model mutate a population of kernels. They pay for the freedom in thousands of evaluations, repeated edits, and wrong candidates.

The paper's argument is that both respond to a hard target by **adding equipment**: parsed profiler output, disassembly, documentation retrieval, lesson stores. And that both are missing **direction** — a hypothesis about where the remaining performance gap actually is.

"Ask, don't equip": interrogate the model about what it believes the bottleneck is, and use that to direct the search, rather than handing it more instruments.

### Why the idea is general

This is a critique of tool accumulation as a substitute for diagnosis. Every mature agent stack drifts toward more tools, more context, more retrieval. The paper's claim is that this raises the cost of search without narrowing it, because nothing in the added surface says *where to look*.

The testable form: **does asking the agent for a hypothesis before each attempt beat giving it more information?** If yes, the direction is worth more than the equipment — which is the same conclusion as CLEO, reached from a third angle.

### Caveat

Abstract only. No result, speedup, or evaluation count is reproduced here.

## Snippets

> "Both respond to hard targets by equipping the agent with more: parsed profiler output, disassembly analysis, retrieval over documentation and libraries, and stores of lessons. We argue that both lack direction, a hypothesis about where the remaining gap is…" [Source: arxiv-2611.03517 p.1]

## Dead Ends

- **Citing a speedup.** Abstract only.
