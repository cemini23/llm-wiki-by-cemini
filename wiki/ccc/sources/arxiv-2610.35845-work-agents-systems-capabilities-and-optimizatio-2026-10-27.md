---
title: "Work Agents: Systems, Capabilities, and Optimization"
type: source
tags: [source, arxiv, agent-taxonomy, work-agents]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Work Agents: Systems, Capabilities, and Optimization |
| Authors | Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, Zirong Chen, Zhiyuan Yao, Yifu Guo, Yuquan Lu, Jinyang Huang, Zhengxi Lu, Siyi Liu, Ziyu Zheng, Yongqi Zhang, Difan Zou, Weiwen Liu (SJTU; HKU; HKUST-GZ; Tsinghua; CUHK; Zhejiang; Sun Yat-sen; Central South) |
| arXiv | 2610.35845 |
| File | `arxiv-2610.35845-work-agents-systems-capabilities-and-optimizatio.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35845 |
| Read status | skimmed (abstract + intro) |

## Narrative

A survey that gives structure to "work agents" — systems that execute delegated digital work rather than generate text. The paper treats an agent as a system of foundation model plus runtime harness, working in a stateful workspace and delivering verifiable outcomes.

Two dimensions describe the working conditions:

- **Work persistence** — how long the state must survive across steps and sessions.
- **Work openness** — how far the environment can change outside the agent's control.

Digital work is classified into **five forms** by task scope and organisation. The paper's figure maps scope at four levels — conversation, atomic action, multi-step, workflow, and workspace — from "interpret evidence and produce answers" up to "track dependencies across related objects".

**Why it matters.** This is a usable reference frame for scoping an agent project. The persistence and openness axes predict which harness features are needed: a long-persistent open workspace needs checkpointing and dependency tracking, while a short closed one does not.

## Snippets

> "We present a work-centric, system-level perspective that views work agents as systems combining foundation models and runtime harnesses to execute tasks in stateful workspaces and deliver verifiable outcomes." [Source: `arxiv-2610.35845-work-agents-systems-capabilities-and-optimizatio.pdf` p.1 (arXiv 2610.35845), retrieved 2026-10-27]
