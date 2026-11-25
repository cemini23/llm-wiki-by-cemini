---
title: "RUIBench — what makes a good robot-use interface (2611.31115)"
type: source
related:
  - concepts/agentic-robotics-harness.md
  - concepts/agent-harness-operational-definition.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | RUIBench: What Makes a Good Robot-Use Interface? |
| Author | Yanzhe Chen, Zhijun Cao, Zechen Bai, Wenzheng Zeng et al. (Show Lab, NUS) |
| Type | arXiv preprint (cs.RO) |
| ID | 2611.31115v1, 23 Nov 2026 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2611.31115-ruibench-what-makes-a-good-robot-use-interface.pdfarxiv-2611.31115-ruibench-what-makes-a-good-robot-use-interface.pdf
| Retrieved | 2026-11-25 |
| File | `arxiv-2611.31115-ruibench-what-makes-a-good-robot-use-interface.pdf` |
| Pages | unknown (read p.1 only) |
| Read status | read (abstract, intro) |

## Narrative

**Off-domain.** This is a robotics-embodied paper. It has no bearing on the `/route` lane, Claude Code, or MCP. It is ingested for one transferable result.

The paper defines the **robot-use interface** (RUI): the set of actions an agent can command, and how those actions are organized for execution. The interface decides what the agent must decide, what execution can absorb, and when control returns to the agent.

RUIBench holds 30 manipulation tasks across five suites. RUIKit crosses six action abstractions with two interaction forms, giving 13 interfaces under shared perception and control.

Headline result: changing only the RUI moves success from 45% to 81% for a frontier agent. The same change moves a fine-tuned 4B model from 13% to 47%.

The authors report a **verification gap**. Agents declare success despite visible failure. The task needs task-level verification, not just per-action success checks.

**Why it matters to this wiki.** The transferable claim is the interface lever, not the robot. A good interface cuts the number of decisions the agent must make and keeps the feedback it needs. The verification gap also recurs in coding harnesses: an agent reports "done" while the task is not done. Link this to `@concepts/agent-completion-verification-gates.md` and the shell-benchmark results. [TENTATIVE]
