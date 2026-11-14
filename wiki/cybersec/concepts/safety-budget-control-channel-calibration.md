---
title: "Safety-budget control-channel calibration"
type: concept
related:
  - sources/arxiv-safety-as-a-budget-2611.16628.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/calibrated-decision-models-pentest-harness-jev.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-jev-llm-safety-guardrail-2611.08845.md
updated: 2026-11-14
---

## Raw Concept

Question: **when a safety target is stated as a rate budget, what can stop the controller from reaching it?** From arXiv 2611.16628 (Bo Han, Lanzhou University).

## Narrative

An operator wants a concrete outcome: assist at most a few percent of harmful requests, and refuse at most a few percent of legitimate ones. These are rates. Constrained optimisation handles rates directly. The standard form is to maximise helpfulness subject to two budgets, with one Lagrange multiplier per constraint.

The mechanism is sound. The failure is in the measurement that feeds it.

### A budget reads a level, not a ranking

A judge or scorer enters a constrained run twice:

| Channel | What it needs | What it is usually built for |
|---|---|---|
| Learning (gradient) | Correct ranking within a group | Ranking |
| Control (dual update) | Mean equals the true rate | Not measured |

Scorers are trained and evaluated for ranking. Their mean level is often biased. When the bias is large, the controller cannot reach the budget, because the dual update compares the biased mean with the budget.

### Three controller states

At a fixed point, the mean bias `b` selects one of three states:

| State | Signature | Meaning |
|---|---|---|
| Interior | `0 < λ < λmax`, `h = ε − b` | Enforces the budget minus the bias |
| Inactive | `λ = 0` | Constraint off, no protection |
| Saturated | `λ = λmax` | The cap decides the outcome |

A monotone transform of the scores changes `b` and leaves AUROC unchanged. A ranker can therefore look excellent and still drive the controller into the wrong state.

### The second failure: the multiplier must reach the gradient

GRPO standardises the penalised reward within each group. That division cancels the factor `(1 + λ)`. The multiplier grows and the policy does not move. A budget can therefore be enforced in the controller and absent from the gradient at the same time.

### The repair

| Element | Choice | Reason |
|---|---|---|
| Base reward | Raw score | Keeps the fine-grained order for the group comparison |
| Penalty and constraint estimate | Monotone isotonic map fitted on judge labels | Corrects the level without flattening the order |
| Advantages | Unscaled, or each objective standardised before weighting | Keeps the multiplier in the gradient |

Fit the map on responses sampled along an unconstrained run. The harm bias moves with the policy, so an initial-policy fit under-covers the run. About 200 labels per question bring an open readout bias from 0.16 to about 0.01.

### Measured effect

On a Qwen3-VL-2B policy, held-out harm moves from 8.9% to 4.8% with the same reward, optimizer and budget. The gain holds in every seed and is largest when the intent sits in the image. Over-refusal stays at or below 2% on 400 benign queries.

### Operator rules

1. Measure the scorer mean bias `b` on labeled responses before you trust a budget.
2. Calibrate the control channel. Do not calibrate the signal that drives the ranking.
3. Check that the multiplier reaches the gradient. Group standardisation silently removes it.
4. Read the controller state from the data: an inactive or saturated multiplier means the budget is not doing what the operator asked.

### Outside training

The same fixed point appears in any dual controller that compares a model score with a target rate. Alert throttles, review quotas, admission control and sampling budgets all have this shape. A biased scorer makes the control loop settle at the wrong operating point, and the loop reports success.

### Limits

One policy family and two scorers. The benign set is small. The paper does not test an adversary who knows the calibration map.

## Snippets

> "A fixed-point analysis shows that the mean bias, not the budget, then decides whether the multiplier settles, saturates or switches off." [Source: arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf p.1]

> "A monotone transform such as p ↦ pγ leaves every AUROC unchanged and moves b at will." [Source: arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf p.3]
