---
title: "GEPA-Curator: Curated Learning for Self-Improving Agents"
type: source
tags: [source, arxiv, agents, prompt-optimization, self-improvement]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | GEPA-Curator: Curated Learning for Self-Improving Agents |
| Authors | Zack Yu et al., UC Berkeley |
| arXiv | 2610.37651 |
| File | `arxiv-2610.37651-gepa-curator-curated-learning-for-self-improving.pdf` |
| Retrieved | 2026-11-01 |
| URL | https://arxiv.org/abs/2610.37651 |
| Read status | skimmed (abstract + intro) |

## Narrative

Large language models run multi-turn agent work that needs sustained interaction with complex environments. Reflective prompt optimizers such as GEPA learn from failed rollouts. The paper says a failure can come from a weak prompt, a harness limit, stochastic execution, or a noisy judge. The authors argue that some of these failures give no useful learning signal and can be harmful. They say the optimizer must choose which tasks it uses.

GEPA-Curator adds a selection step to the prompt optimizer. The framework decides which agent experiences shape the next prompt. It has two parts. Task curation filters out tasks that are likely to give a noisy or unreliable learning signal. Prior success retrieval selects past successful trajectories for a task and gives them to the prompt optimizer as extra context.

The authors evaluate GEPA-Curator on GoBrowse, ALFWorld, AppWorld, and τ-bench. They use Gemini 3.1 Pro and Claude Opus 5 as optimizer models. The abstract says GEPA-Curator matches or exceeds the mean performance of both baselines, with gains of up to 20.7% over GEPA and 21.2% over ACE. Those two percentages are single-source claims from this abstract.

The introduction frames the same problem as attribution inside a harness. An agent acts with tools. A Reflector reads the trajectory or end state, draws lessons, and revises the prompt. Later tasks use that revised prompt. The paper says the Reflector often cannot tell whether a failure came from the prompt. A missing tool, a harness limit, execution noise, or a judge can also cause the failure. Ambiguous or infeasible tasks add more noise. The Reflector can still treat that noise as a prompt defect and write an unnecessary or harmful update.

The introduction gives a shopping example. If the agent misses a required option before it adds an item to the cart, the Reflector can revise the prompt so the agent checks required fields. If the same task fails because the purchase button malfunctions, the paper says that treating the failure as evidence about the prompt is the wrong use of the rollout. The extract ends mid-sentence on that second case.

For an agent and coding-harness practitioner, the claim is about the update loop. A harness, a missing tool, or a judge can fail a rollout that the prompt did not cause. A loop that revises the prompt from every failure can store that noise in the next prompt. The paper proposes two controls: drop unreliable tasks, and give the optimizer prior successful trajectories before it writes the prompt.

## Snippets

> "We introduce GEPA-Curator, a framework that augments the prompt optimizer to select which agent experiences should shape prompt optimization. In particular, GEPA-Curator consists of two components: task curation, which filters out tasks that are likely to provide noisy or unreliable learning signals, and prior success retrieval, which selectively retrieves past successful trajectories for a task and provides them as additional context to the prompt optimizer." [Source: `arxiv-2610.37651-gepa-curator-curated-learning-for-self-improving.pdf` p.1 (arXiv 2610.37651), retrieved 2026-11-01]

> "GEPA-Curator matches or exceeds the mean performance of both baselines, with gains of up to 20.7% over GEPA and 21.2% over ACE." [Source: `arxiv-2610.37651-gepa-curator-curated-learning-for-self-improving.pdf` p.1 (arXiv 2610.37651), retrieved 2026-11-01]
