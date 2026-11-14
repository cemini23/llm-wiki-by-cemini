---
title: "Safety as a Budget: calibrating the control channel of constrained GRPO (arXiv 2611.16628)"
type: source
related:
  - concepts/safety-budget-control-channel-calibration.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/calibrated-decision-models-pentest-harness-jev.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-jev-llm-safety-guardrail-2611.08845.md
  - sources/arxiv-bmms-policy-conditioned-behavioral-compliance-2611.09147.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models |
| Author | Bo Han (Lanzhou University) |
| Type | arXiv preprint (cs.AI), 2611.16628v1 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf` |
| URL | https://arxiv.org/abs/2611.16628 |
| Retrieved | 2026-11-13 |
| Pages | 10 |
| Read status | read |

## Narrative

Safety tuning usually sets the outcome through reward weights. An operator tries a weight, measures the result, and retries. The paper replaces the weight with two rate budgets: the rate of harmful assistance and the rate of over-refusal. A Lagrange multiplier enforces each budget inside GRPO. The paper shows that this natural design fails twice, and it repairs both failures.

### The two channels

A scorer enters constrained GRPO at two points. In the learning channel, the reward compares responses to one prompt, so the scorer must rank them. In the control channel, the dual update compares the scorer mean with the budget, so the mean must equal the rate. Ranking quality and level accuracy are separate properties. Only the level decides what a budget means.

### Failure one: the mean bias sets the controller state

Scorers are built and evaluated for ranking. Their mean is often wrong. Proposition 1 of the paper gives three fixed-point states of the dual update, and the mean bias `b` selects the state:

| State | Condition | Effect |
|---|---|---|
| Interior | `h(π*) = ε - b` | Enforces the budget minus the bias |
| Inactive | `λ = 0` | Constraint switches off |
| Saturated | `λ = λmax` | The cap decides the outcome, not the budget |

A training-free readout of a frozen 4B model overstates refusal by **0.16**. It reports a mean refusal probability of 0.18 where the labeled rate is 0.02. The refusal multiplier then rises to 1.5–3.0 while judged over-refusal is about 2%. The harm budget barely moves the policy.

### Failure two: group standardization cancels the multiplier

Standard GRPO standardizes the penalized reward within each group. With group scale, the factor `(1 + λh)` cancels. The multiplier climbs to 3.2–4.7 and never reaches the gradient. The budget then does not lower harm.

### The repair: two-channel constrained GRPO

The fix keeps each property in the place that uses it.

1. The base reward keeps the **raw score**, because the fine-grained order drives the within-group comparison.
2. The penalty and the constraint estimate pass through a **monotone isotonic map** fitted on judge-labeled training responses. The map corrects the level without flattening the order.
3. Advantages stay **unscaled**, or each objective is standardized before weighting. The multiplier then scales the gradient.

Calibration data comes from responses sampled along an unconstrained run, because the harm bias moves with the policy. About 200 labels per question bring the bias of an open readout to about 0.01.

### Results

The policy is Qwen3-VL-2B-Instruct with LoRA. The held-out set has 1,037 adversarial prompts and 400 benign queries. Results hold across three seeds.

| Condition | Held-out harm | Over-refusal |
|---|---|---|
| Standard GRPO, no budget | 8.9% | 1.3% |
| Raw control, CGRPO advantages | 7.6% | 2.7% |
| Calibrated control, CGRPO advantages | **4.8%** | 4.0% |
| Raw control, unscaled advantages | 11.9% | 1.3% |
| Calibrated control, unscaled advantages | **6.1%** | 4.0% |

The calibrated gap against standard GRPO is −4.2 points, 95% CI [−5.1, −3.2]. The gain is largest when the intent sits in the image (10.1% to 5.1%) and on the unseen HADES benchmark (28.9% to 12.8%). MMBench stays unchanged. The unscaled form reaches 6.1% at a KL of 0.02–0.04, against 0.04–0.07 for the baseline. That matches a dedicated decision model (Jev, 5.8%) while running locally.

### Defensive reading

A budget is only as good as the level it reads. Before you trust a safety budget, measure the scorer mean bias `b` on labeled responses. If the bias is large, the constraint will saturate or switch off. Calibrate the control channel and leave the learning channel alone. A monotone map that preserves order is enough, and it costs one fitting run.

The result also applies outside training. Any dual controller that compares a model score with a target rate inherits the same fixed point. Admission control, alert throttles and review quotas are controllers of this shape.

### Limits

The evaluation covers one policy family, one benchmark cluster and two scorers. The benign set is 400 queries, so the over-refusal estimate is coarse. The paper does not test an adaptive adversary who knows the calibration map.

## Snippets

> "Stating safety as budgets on the rate of harmful assistance and the rate of over-refusal, enforced by Lagrange multipliers inside GRPO with an off-the-shelf scorer as the cost, is the natural fix, and it fails twice." [Source: arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf p.1]

> "A budget also reads their level." [Source: arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf p.3]

> "On a Qwen3-VL-2B policy with a training-free readout of an open 4B model as the scorer, held-out harm on 1,037 adversarial prompts falls from 8.9% under standard GRPO to 4.8%." [Source: arxiv-2611.16628-safety-as-a-budget-calibrating-the-control-chann.pdf p.1]
