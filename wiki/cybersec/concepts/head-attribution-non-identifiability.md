---
title: "Head-level attribution is non-identifiable — correlation is not a mechanism"
type: concept
maturity: draft
related:
  - sources/arxiv-bias-head-non-identifiability-2611.23218.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/refusal-and-abstention-direction-geometry.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: when a paper says "these attention heads encode bias", what did it measure? From 2611.23218.

## Narrative

A family of methods ranks attention heads by a per-head statistic, selects a set, and ablates it. Validation is the change in a fairness metric. The audit asks whether the statistic measures bias at all.

The first correlation looks decisive. The fairness head map correlates with a label-blind response-length map at rho = -0.950 on Qwen-2.5-7B and -0.768 on Llama-3.1-8B. A surface confound seems proven.

An intervention rejects it. With the prompt fixed, response length explains 1% of the statistic's variance. Prompt identity explains 64%, in an ordering not monotonic in length. The pooled correlation was a between-arm artifact.

The construct is unidentifiable. Inside a fixed prompt, the fairness label, the response length, and the protected-group token are collinear at phi = 0.95. The labelling rule entails part of that. No observational analysis can separate them, and the family runs no experiment that could.

The substantive claims fail separately. Bias selectivity is not late-layer-concentrated on either model. No tested head set lowers the unfairness rate when ablated against a layer-matched null.

The positive control is what makes the null credible. Ablating the complement of the head set, scored on the opposite label, destroys refusal behaviour (p = 2.7e-5). The pipeline can detect effects at this scale.

**Two measurement hazards.**

- A single random baseline can sit inside a null band from 0.641 to 1.000. Use many draws.
- Ablation-degraded generation gets scored as fair. One arm produced 31% unclassifiable output and an apparent 0.127 reduction. Score refusal loss and unclassifiable output as separate outcomes.

**General rule for interpretability audits.** A causal claim needs an intervention with a matched null, not a correlation with a plausible confound. A degraded model that stops refusing is not an improved model.

[Source: arxiv-2611.23218-what-does-a-bias-head-measure-non-identifiabilit.pdf]

## Snippets

> "Every piece of that evidence is correlational, and it is wrong."
[Source: arXiv:2611.23218v1 §1]
