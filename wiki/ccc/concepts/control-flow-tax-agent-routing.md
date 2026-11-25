---
title: "Control-flow tax — routing decisions as a first-order agent cost"
type: concept
related:
  - sources/arxiv-control-flow-tax-decision-routing-2611.32365.md
  - concepts/decision-model-hybrid-agent-routing.md
  - concepts/timeout-cascade-cost-aware-routing.md
  - entities/skills/route.md
  - concepts/token-economics-and-prompt-caching.md
updated: 2026-11-25
maturity: draft
---

## Raw Concept

Question this page answers: how much of an agent's cost goes to deciding the next step, and what lowers that share? Synthesised from `@sources/arxiv-control-flow-tax-decision-routing-2611.32365.md` (2611.32365).

## Narrative

Every agent step is a decision plus an action. The decision is "advance, repair, backtrack, or stop". To make it, a content-aware controller may need the request, the current files, the contracts, and the execution history. The answer is short. The evidence is long. The paper calls the recurring cost of that evidence the **control-flow tax**.

In the paper's three-document workflow, control takes 42.5% of baseline cost and 66.5% of input tokens. It takes 19.4% of elapsed time. The cost share is high. The time share is not. Do not treat one as a proxy for the other.

Three design rules follow from the measurements.

**1. Specialize the chooser, keep the generator.** Replace only the decision backend with a small specialized model. Keep the expensive generator unchanged. Cost fell 40.5% to 49.6% across four tasks. This differs from a cascade: a cascade picks one model for the whole task.

**2. A partial substitution saves little.** Replacing only the Boolean existence gate cut gate cost 97.6% and workflow cost 1.8%. The expensive semantic chooser was untouched. The saving scales with the share of cost you actually replace.

**3. Cheap routers can be a false economy.** A cheap router that makes extra calls to the generator costs more than it saves. In the paper, Haiku hit the request limit on every run, and Luna used 54% more requests than its controls. Judge a router on trajectory length, not on its own token price.

The paper states two requirements: inexpensive decisions, and trajectories that preserve the savings. The second is the one a naive cost model misses.

**Status.** All figures come from one paper, one workflow, and one vendor's decision model. None are independently reproduced. [TENTATIVE]

## Snippets

> "Replacing only a small Boolean gate leaves the expensive semantic chooser untouched: a 97.6% gate-cost reduction translates into just 1.8% lower workflow cost." [Source: `arxiv-2611.32365-the-control-flow-tax-specialized-decision-routin.pdf` p.1, retrieved 2026-11-25]
