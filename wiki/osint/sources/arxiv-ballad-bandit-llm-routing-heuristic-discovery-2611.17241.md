---
title: "BALLAD: bandit-based LLM routing for automated heuristic discovery (arXiv 2611.17241)"
type: source
related:
  - concepts/bandit-llm-routing-heuristic-search.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/heuristic-portfolio-optimization-hpo.md
  - concepts/osint-inbox-wave-2026-11-14.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | BALLAD: Bandit-Based LLM Routing for Automated Heuristic Discovery |
| Author | Samidha Verma (IIT Delhi), Ankit Anand (Google DeepMind), Sayan Ranu (IIT Delhi) |
| Type | arXiv preprint, cs.AI; NeurIPS 2026 |
| arXiv | 2611.17241v1, 12 Nov 2026 |
| Pages | 48 |
| Location | `research to be indexed/osint/arxiv-2611.17241-ballad-bandit-based-llm-routing-for-automated-he.pdf` |
| Retrieved | 2026-11-14 |
| Read status | read |

## Narrative

### The empirical claim

Automated heuristic discovery (AHD) systems such as FunSearch, EoH and AlphaEvolve prompt a language model to mutate and refine code heuristics. The common assumption is that a stronger, costlier model yields better heuristics.

The authors test that assumption on five NP-hard combinatorial optimisation problems with four models. They find **no consistent advantage** for larger or more expensive models. In several cases a smaller or free model wins. [TENTATIVE: one paper, five benchmarks, four models]

### The routing problem

AHD needs thousands of model calls per run, so the model choice is a cost problem. The paper formalises the choice as an online bandit and identifies three properties that break classical bandits:

| Property | Meaning | Consequence |
|---|---|---|
| P1 extreme-value objective | The run wants the single best heuristic, not the best average | Rank arms by an upper-tail quantile, not the mean |
| P2 cross-arm coupling | One model's output seeds the prompt for later calls | Credit must propagate through the mutation genealogy |
| P3 non-stationary reward | A model's usefulness shifts as the population evolves | Discount stale observations |

### The three components

BALLAD combines three ideas into a single per-arm index:

1. **Bootstrapped quantile-of-maxima estimator.** It favours rare, high-scoring heuristics over stable averages.
2. **DAG credit propagation.** Each heuristic has parent edges to the heuristics in its prompt context. A model earns partial credit when its output appears as a parent of another model's later success.
3. **Sliding-window normalisation.** Keeps the index sensitive to current rather than historical fertility.

### Reported results

Across the five problems, BALLAD matches the best single model and in several cases beats every individual model. The authors argue the result is not explainable by selection alone. API cost falls by up to **65.6%** against always calling the strongest model. [TENTATIVE: one paper]

### Why it matters here

Cemini already runs a multi-model estate: a fable-advisor orchestration lane, a Grok implementation lane, a Codex lane, and a DeepSeek proxy. Today the lane choice is a static policy. BALLAD supplies a template for a learned policy where the reward is measurable.

The transfer is partial. BALLAD needs a cheap, automatic evaluator score after every call. A code heuristic has a test suite. Wiki prose and brief quality do not, so the credit signal would have to come from a judge model, which reintroduces the cost the method tries to remove.

[OPEN QUESTION 2026-11-14] Whether a judge-scored reward keeps the 65.6% cost saving is unmeasured here. No Cemini harness was run.

## Snippets

> "Across five NP-hard combinatorial optimization problems and a pool of four models of varying capability and cost, BALLAD not only matches the best individual LLM, but in several cases surpasses every individual model, while reducing API cost by up to 65.6% relative to always using the strongest model." [Source: arxiv-2611.17241-ballad-bandit-based-llm-routing-for-automated-he.pdf p.1]

> "Because each LLM's output seeds the shared program population that conditions future prompts, routing decisions are causally coupled across steps and models." [Source: arxiv-2611.17241-ballad-bandit-based-llm-routing-for-automated-he.pdf p.2]
