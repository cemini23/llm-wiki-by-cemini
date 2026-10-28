---
title: "Profiling a Frontier Agent with EBench: Direct Control vs Harness with Policy"
type: source
tags: [source, arxiv, agent-harness, robot-evaluation]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy |
| Authors | Yifei Yao, Yude Zou, Guanbo Jiao, Xing Gao, Ning Gao, Yukai Wang, Jiantong Chen, Zihou Zhu, Xinyu Li, Ningyu Yan, Shuai Wang, Jianming Ma, Haoyu Guo, Weinan Zhang, Chunhua Shen (Shanghai AI Laboratory; SJTU; Fudan; Zhejiang) |
| arXiv | 2610.35832 |
| File | `arxiv-2610.35832-profiling-a-frontier-agent-with-ebench-from-dire.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.35832 |
| Read status | skimmed (abstract + intro) |

## Narrative

The paper evaluates GPT-6-Astra as a robot controller on EBench. It compares two configurations:

- **Direct control** — the agent emits waypoint commands itself.
- **Harness with policy** — the agent may also call a post-trained VLA or WAM policy to execute actions.

Results under direct control:

- Overall performance is competitive with post-trained policies.
- The agent leads on short-horizon tasks.
- It shows the least variation across generalization dimensions.
- It underperforms on long-horizon tasks, tabletop manipulation, and high-precision contact-rich tasks.

Under harness with policy, invoking a post-trained policy combines the strengths of both parts. Overall success rises to the level of the strongest post-trained policy, and token cost falls substantially. Performance still stays below the per-task upper bound.

**Why it matters.** This is the clearest demonstration in the wave of a design principle: a general model plus a specialist tool beats either alone. The general model wins on breadth and variance; the specialist wins on precision. The harness decides when to call which. The same shape applies outside robotics — a general agent with a precise, narrow tool.

## Snippets

> "In the harness with policy, invoking a post-trained VLA or WAM combines the complementary strengths of both components, raising overall task success to the level of the strongest compared post-trained policies while substantially reducing token cost." [Source: `arxiv-2610.35832-profiling-a-frontier-agent-with-ebench-from-dire.pdf` p.1 (arXiv 2610.35832), retrieved 2026-10-27]
