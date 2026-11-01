---
title: "Task Advancement Memory for GUI Agents"
type: source
tags: [source, arxiv, gui-agents, agent-memory, task-advancement]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents |
| Authors | Ziyang Chen et al., The Hong Kong University of Science and Technology (Guangzhou); Qian Li, Joint SDU-NTU Centre for Artificial Intelligence Research (C-FAIR), Shandong University |
| arXiv | 2610.37482 |
| File | `arxiv-2610.37482-from-interaction-to-capability-task-advancement.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37482 |
| Read status | skimmed (abstract + intro) |

## Narrative

GUI memory should preserve the results of past actions and learn reusable operations. The paper says this is difficult in long-horizon workflows. The agent must use information across applications. Useful operations are interleaved with failed attempts.

The authors introduce Task Advancement Memory (TAM). TAM defines task advancement as verified task progress. TAM supports ongoing task execution and learns reusable operations. During execution, Task Advancement State represents how verified task progress changes the remaining goals. The agent can build on earlier achievements across applications.

After each task, advancement supervision identifies and abstracts the interactions that produced a verified local result. The learned operations preserve the relation between required inputs, expected outcomes, and verification conditions. TAM retains locally successful operations from both successful and failed tasks.

The paper reports these results. Each number comes from this paper alone. On MobileWorld GUI-only tasks, Advancement State alone raises success from 12.0% to 28.2%. Full TAM achieves a 17.6% relative gain in task success over the strongest evaluated baseline and reduces lifecycle tokens per solved task by 38.7%. On SPA-Bench, TAM achieves state-of-the-art task success in the single-app English Level 3 setting.

For an AI-agent and coding-harness practitioner, the paper claims a concrete memory split. During a run, store verified task progress and the remaining goals, so later steps can use results from earlier applications. After a run, keep operations that produced a verified local result, including operations taken from tasks that failed. The paper also claims a lower lifecycle-token cost per solved task under full TAM.

## Snippets

> "On MobileWorld GUI-only tasks, Advancement State alone raises success from 12.0% to 28.2%. Full TAM achieves a 17.6% relative gain in task success over the strongest evaluated baseline and reduces lifecycle tokens per solved task by 38.7%." [Source: `arxiv-2610.37482-from-interaction-to-capability-task-advancement.pdf` p.1 (arXiv 2610.37482), retrieved 2026-11-01]
