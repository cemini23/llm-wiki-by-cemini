---
title: "An external safety filter has two error rates, not one"
type: concept
related:
  - sources/arxiv-jev-llm-safety-guardrail-2611.08845.md
  - concepts/calibrated-decision-models-pentest-harness-jev.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/certified-selective-prediction-guardrails.md
  - concepts/guardrail-construct-validity-agent-eval.md
updated: 2026-11-10
---

## Raw Concept

Question: **what does it cost to put a classifier in front of a model, and which number should an operator quote?** From arXiv 2611.08845, an end-to-end evaluation of the Jev decision model as an external guardrail.

## Narrative

A guardrail is a decision system with two error rates. It can pass a harmful prompt, and it can block a benign one. A single "safety score" hides both. The evaluation puts Jev in front of Qwen2.5-1.5B and measures both on 970 prompts.

| Configuration | Harmful prompts answered | Benign prompts refused |
|---|---|---|
| Model alone | 73.2% | 1.2% |
| Input gate at 0.50 | 2.4% | 10.8% |
| Tiered gate, input + selective output review | 5.6% | 4.0% |

The input gate removes almost all harmful answers and multiplies benign refusals by about nine. The tiered gate buys back benign refusals and gives back harmful answers. Neither dominates.

### Four things an operator should take

**A threshold tuned on one benchmark does not generalise across harm types.** AdvBench prompts score a mean harmfulness of 0.98, so their answer rate stays near zero across a wide threshold range. XSTest-unsafe scores 0.87 and is very sensitive to the threshold. A filter that looks excellent on AdvBench can be mediocre on a different harm distribution.

**Input harmfulness is not answer harmfulness.** The tiered configuration blocked 13 responses at the output stage. Seven were harmful and six were safe. Some unsafe prompts passed because the generated response scored low. Input and output review measure different objects.

**Output review has a measurable cost.** Removing it raised harmful answers by 0.97 points and lowered benign refusals by 2.4 points. It is a trade, not a free improvement.

**Matched-budget comparison removes most of the gain.** At a common 4% benign-refusal budget, a retuned single gate answered 14.5% of XSTest-unsafe prompts and a jointly tuned tiered gate answered 12.5%. On a held-out split, both selected policies produced the same result and the tiered policy used no output review.

### Reporting pattern to copy

1. Report the harmful-answer rate and the benign-refusal rate together, never one alone.
2. Report the review call volume, because it is a real cost.
3. Do not tune thresholds and evaluate on the same prompts.
4. State the target model and the guard model version.
5. Report a manual audit of the automated outcome labels.

### Where this connects

This is the concrete instance of the measurement discipline in `@concepts/guardrail-construct-validity-agent-eval.md`: an invalid protocol produces a policy claim that does not hold. It also extends `@concepts/low-asr-is-not-refusal.md`, because a blocked prompt and a refused answer are different outcomes, and the guardrail decides which one you count. The decision-model framing matches `@concepts/calibrated-decision-models-pentest-harness-jev.md`, which uses Jev as a calibrated gate at pentest decision points.

Confidence: the in-sample numbers are `[TENTATIVE]` — one target model, one guard version, one dataset set. The held-out result is a single 40% split.

## Snippets

> "A threshold optimized for prompt-classification F1 need not minimize end-to-end harmful answers at an acceptable benign-refusal rate." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.5]

> "Of the 79 outputs reviewed, seven responses to harmful-labeled prompts and six responses to benign prompts were blocked. Thus, the second-stage check provides a modest reduction in harmful-prompt answering at a measurable cost in over-refusal and additional computation." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.6]

> "At a 10% benign-refusal budget, optimized C2 and C3 yield pooled unsafe-answer rates of 2.4% and 2.1%, respectively, with C3 reviewing 0.7% of requests. These results demonstrate modest gains from joint threshold optimization on the evaluation dataset." [Source: arxiv-2611.08845-jev-as-an-llm-safety-guardrail-an-empirical-stud.pdf p.7]
