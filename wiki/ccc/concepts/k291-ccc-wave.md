---
title: "K291 — ccc wave (2026-10-14)"
type: concept
tags: [wave, k291, ingest, hub]
keywords: [K291, tool-use supervision, reflective agents, action chunking]
related:
  - sources/arxiv-davinci-tool-agentic-tool-use-supervision-2610.16867-2026-10-14.md
  - sources/arxiv-agent-reflex-reflective-agents-2610.17953-2026-10-14.md
  - sources/arxiv-chunkact-action-chunking-agentic-robotics-2610.18874-2026-10-14.md
maturity: draft
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @sources/arxiv-davinci-tool-agentic-tool-use-supervision-2610.16867-2026-10-14.md — 30B tool-use model; +35.8 pts on τ2-bench
- @sources/arxiv-agent-reflex-reflective-agents-2610.17953-2026-10-14.md — reflection learned from matched success–failure pairs
- @sources/arxiv-chunkact-action-chunking-agentic-robotics-2610.18874-2026-10-14.md — action chunking cuts LLM calls 2.9×

## Raw Concept

The question this page answers: **what did the K291 ccc inbox contain, and what transfers to this workspace's agent lane?**

## Narrative

**Three papers, one theme: the supervision signal is the bottleneck, not the model size.**

### Davinci-Tool — scale environment coverage and verification together

A **30B** tool-use model plus an execution-grounded dataset. The argument: scaling trajectories *or* verification alone fails, because **new environments introduce states, rules, and dependencies that must also appear in the success criteria**.

Two pipelines: **EGTS** (verified demonstrations from independently authored systems) and **EES** (synthesizable environments, state-grounded tasks, executable verifiers). Result: **30,395 verified trajectories across 2,260 tool names**, used for SFT then for outcome-grounded DPO preferences.

| Benchmark | Base Qwen3-Coder-30B | Davinci-Tool |
|---|---|---|
| τ2-bench | 52.4 | **88.2** |
| BFCL v4 multi-turn | 30.4 | **62.8** |
| MCP-Atlas | 16.9 | **56.2** |

Beats Qwen3-Coder-480B-A35B **at 1/16 the parameters**.

### Agent-Reflex — learn reflection from failure pairs

Three stages: **RSD** injects grounded tool-feedback perturbations, mines **matched success–failure pairs**, and summarizes reusable **reflection meta-skills**; **ReSFT** converts each skill into supervision; **ORPO** adds on-policy distillation. On Qwen3-8B: **58.6** across five long-horizon tool-use benchmarks, **29.1** on AgentNoiseBench.

The design point: **reflection is trained from contrastive pairs, not from instructions to "think harder".**

### ChunkAct — stop re-reasoning what memory already decided

In agentic robotics every primitive costs a full LLM reasoning pass over the whole history. ChunkAct observes the reasoning is **largely redundant**: once a sub-goal is chosen, its primitives follow a routine memory already prescribes. Offline it **compiles memory into chunks**; online one call launches a chunk that runs autonomously until failure.

**+5.0 points** task success on LIBERO-Pro over SOTA, with **2.9× fewer LLM calls, 4.4× fewer input tokens, 2.3× fewer output tokens**.

### What transfers here

- **ChunkAct is the cost lesson.** Compiling a known routine into one call, instead of re-deriving it, is directly applicable to any repeated agent workflow in this workspace.
- **Davinci-Tool is the data lesson.** Verification must scale *with* environment coverage; a verifier that does not know the environment's success criteria validates the wrong thing.
- **Agent-Reflex is the training lesson.** Matched success–failure pairs, not instructions, drive reflection.

### Boundary

No install, no wire, no `/route` swap.

## Snippets

> "Scaling either trajectory coverage or verification alone is insufficient as new environments introduce distinct states, rules, and dependencies that must also be reflected in the success criteria." [Source: arxiv-2610.16867 p.1]

> "Once a sub-goal is chosen, its primitives follow a routine already prescribed by memory." [Source: arxiv-2610.18874 p.1]

> "On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art ... while requiring 2.9× fewer LLM calls, 4.4× fewer input tokens, and 2.3× fewer output tokens." [Source: arxiv-2610.18874 p.1]

## Dead Ends

- Treating Davinci-Tool's benchmark jumps as a general capability gain. The model was trained on synthesised environments with executable verifiers; the gain is tied to that supervision.
