---
title: Bandit LLM routing for heuristic search — BALLAD and the multi-model cost question
type: concept
related:
  - sources/arxiv-ballad-bandit-llm-routing-heuristic-discovery-2611.17241.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/heuristic-portfolio-optimization-hpo.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

Cemini already routes work across several model families. The current policy is static: a lane is chosen by hand. Can a learned policy pick the model per step and cut cost without losing quality?

Source: @sources/arxiv-ballad-bandit-llm-routing-heuristic-discovery-2611.17241.md (Verma, Anand, Ranu; NeurIPS 2026).

## Narrative

### The finding that motivates it

Automated heuristic discovery prompts a model thousands of times to mutate and refine code. The natural assumption is that a stronger, costlier model wins.

On five NP-hard combinatorial problems with four models, the paper finds **no consistent advantage** for larger or more expensive models. In several cases a smaller or free model wins. [TENTATIVE: one paper]

### Why classical bandits fail here

| Property | Statement | Breaks |
|---|---|---|
| P1 | The run wants the single best artefact, not a good average | Mean-reward bandits |
| P2 | One model's output seeds later prompts | Independent-arm assumption |
| P3 | A model's usefulness shifts during the run | Stationary-reward assumption |

### The three fixes

1. **Quantile-of-maxima index.** Rank each model by an upper-tail quantile of its scores, not the mean. This targets the extreme-value objective.
2. **DAG credit propagation.** Build the mutation genealogy: a node is a heuristic, an edge means "was in the prompt context". A model earns partial credit when its output is an ancestor of another model's later success.
3. **Sliding-window normalisation.** Discount stale observations so the index tracks current fertility.

The result is a single per-arm index, and a drop-in replacement for the fixed-model generator in a FunSearch- or AlphaEvolve-style pipeline.

### Reported results

- Matches the best single model on the five problems.
- Beats every individual model on several.
- Cuts API cost by up to **65.6%** against always using the strongest model.

The authors argue the win is not pure selection, because a selection rule over fixed model behaviour cannot exceed the best arm. The gain comes from the collaborative dynamic the credit signal creates.

### Transfer to this workspace

The estate already has four distinct lanes: a fable-advisor orchestrator, Grok for bulk implementation, Codex for cross-vendor correctness, and a DeepSeek proxy. The lane choice is currently a rule in a prompt.

Three conditions must hold before a learned router is worth building:

| Condition | Status here |
|---|---|
| A cheap, automatic score after every call | Missing for prose. Available for code with tests |
| Thousands of calls per run | Only true for large ingest waves |
| A stable reward definition | Missing: a judge model reintroduces cost and drift |

The honest conclusion is that BALLAD is a design reference, not a build order. The code-verification lane is the only place with a cheap score. A wiki or brief lane would need a judge, and the judge cost erodes the saving.

[OPEN QUESTION 2026-11-14] Whether a judge-scored reward retains the cost advantage is untested. No harness was run.

### What to steal

Even without a bandit, two ideas transfer today:

- **Credit through lineage.** When a reviewer output improves a later artefact, record which lane produced the parent. The audit trail already exists in the eval pages.
- **Tail scoring, not mean scoring.** Judge a lane on its best outputs, not its average, because the deliverable is one good artefact.

## Snippets

> "A natural assumption is that more powerful and more expensive models consistently yield better heuristics. We challenge this empirically: across multiple NP-hard combinatorial optimization problems, we find no consistent advantage for larger, costlier models." [Source: arxiv-2611.17241-ballad-bandit-based-llm-routing-for-automated-he.pdf p.1]
