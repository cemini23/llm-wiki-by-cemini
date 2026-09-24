---
title: "Agensh: Scaling Organizational Intelligence to 1,024 Agents"
type: source
tags: [arxiv, source, k270, agents, harness, multi-agent]
keywords: [k270, Agensh, multi-agent, ProgramBench, self-organized]
related:
  - concepts/k270-harness-evolution-wave.md
  - entities/tools/agensh.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: skimmed
---

## Relations

- @concepts/k270-harness-evolution-wave.md
- @entities/tools/agensh.md

## Raw Concept

| Paper | arXiv:2609.26781 |
| File | `arxiv-2609.26781-agensh-scaling-organizational-intelligence-to-1.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2609.26781-agensh-scaling-organizational-intelligence-to-1.pdf` |
| Authors | Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei (Microsoft Research) |
| Retrieved | 2026-09-23 |
| Pages | 13 |
| Dual-ID | **OSINT K270** |
| sha256 | `b355896c23cc3a8535127d4a6f65671bd78f02366b3386c03e6af61524ade82a` |

## Narrative

A multi-agent system can cut latency on complex tasks by running work concurrently. Current multi-agent harnesses are constrained by a central orchestrator's capacity to allocate tasks and coordinate workers.

**Agensh** is a scalable **self-organized** multi-agent harness with **no central orchestrator**. Concurrent workers run a cooperation loop: gather context, claim and self-assign sub-tasks, take action and share findings, verify results, and merge progress asynchronously.

Three infrastructure components support the loop:

| Component | Function |
|-----------|----------|
| Shared workspace | Holds proposed, ongoing, and completed work |
| Message interface | Lets workers communicate |
| Shared context | Retains reusable findings and work intentions |

**Reported scaling results** on the five hardest ProgramBench tasks with GPT-5.6-sol (high):

| Setting | From | To | Result |
|---------|------|----|--------|
| Mean final test-pass rate, 1 → 128 agents | 19.31% | 28.78% | ~49% relative improvement |
| pandoc, 1 → 1,024 agents | 33.89% | 55.06% | final test-pass rate |

Larger organizations reach comparable test-pass rates earlier. Worker trajectories show that different forms of self-organized cooperation emerge and standardize as the organization grows. The paper names the number of agents as a **new scaling dimension** for multi-agent organizations.

**Release status.** GitHub returned **404 on 2026-09-23**. No clone. See @entities/tools/agensh.md.

**Cemini relevance:** multi-agent scaling pattern only. **FILE only. 0 product Integrate GO. No clone. No weight download.**
