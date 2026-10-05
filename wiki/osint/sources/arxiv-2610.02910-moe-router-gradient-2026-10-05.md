---
title: "Frequency is Not Sensitivity — router-gradient expert suppression in sparse MoE LLMs"
type: source
tags: [arxiv, safety, mechanistic-interpretability, moe]
keywords: [2610.02910, mixture-of-experts, router-gradients, expert-suppression, refusal]
related:
  - concepts/k282-agent-eval-wave.md
maturity: draft
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- @concepts/k282-agent-eval-wave.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Frequency Is Not Sensitivity: Identifying Safety-Sensitive Experts in Sparse MoE LLMs |
| Authors | Md Nurul Absar Siddiky, Liuwan Zhu, Yingfei Dong (University of Hawaii at Manoa) |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02910-frequency-is-not-sensitivity-identifying-safety.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.02910 |
| read-status | read |

## Narrative

The paper studies how to weaken the safety behavior of a sparse
Mixture-of-Experts (MoE) model without retraining. The usual method ranks experts
by activation frequency. The authors argue that frequency measures use, not
influence. They test an alternative: router-gradient sensitivity, which measures
how much the sequence loss depends on the gate weights that select an expert.

They rank experts on 500 benign prompts (AEGIS2.0) and 500 malicious prompts
(AdvBench) across five MoE architectures. They then suppress selected experts on
100 held-out malicious prompts. Under two budgets (equal expert count, and equal
malicious routing traffic of 1%–5%), gradient selection reduces refusals more than
activation selection in 24 of 25 conditions, and more than a ten-trial random mean
in all 25. The largest effect is in OLMoE, where refusals fall from 34 to 9 of 100
prompts (73.53%). A depth-matched control keeps the gain in 23 of 25 conditions.
An exploratory link ties larger malicious-vs-benign concentration gaps to larger
peak effects (ρ = 0.90; exact p = 0.083, n = 5). Gradient expert selection costs a
one-time backward pass, but no extra cost at inference.

For this workspace: this is a direct contribution to the local abliterated LLM lab
and to agent security. It gives a measurable way to find safety-critical experts in
MoE models and shows that activation frequency is a poor proxy. The method informs
both attack (weaken refusal) and defense (harden experts). It also supports
mechanistic work on where refusal lives in a model.

[Source: arXiv:2610.02910]

## Snippets

> "Suppressing a small set of routed experts can weaken the safety behavior of a sparse Mixture-of-Experts (MoE) language model without retraining. Which experts to suppress is therefore a security question, and the usual answer is activation frequency — but frequency measures use, not influence."
[Source: arxiv-2610.02910-frequency-is-not-sensitivity-identifying-safety.pdf p.1]

> "Under each of the two budgets, router-gradient selection reduces refusals more than activation in 24 of 25 conditions, and more than a ten-trial random mean in all 25."
[Source: arxiv-2610.02910-frequency-is-not-sensitivity-identifying-safety.pdf p.1]

> "The largest effect is in OLMoE, where refusals fall from 34 to 9 of 100 prompts (73.53% relative) with no degraded outputs, indicating substantive compliance rather than broken generation."
[Source: arxiv-2610.02910-frequency-is-not-sensitivity-identifying-safety.pdf p.1]

> "This study shows that activation frequency is not a consistently reliable proxy for suppression-induced behavioral effects in sparse MoE language models."
[Source: arxiv-2610.02910-frequency-is-not-sensitivity-identifying-safety.pdf p.5]
