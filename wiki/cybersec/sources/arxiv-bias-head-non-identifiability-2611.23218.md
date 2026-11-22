---
title: "What Does a Bias Head Measure? — non-identifiability in head-level bias attribution (2611.23218)"
type: source
maturity: draft
related:
  - concepts/head-attribution-non-identifiability.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/low-asr-is-not-refusal.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution
- **Author:** S.M Seefat Alam (Bangladesh University of Engineering and Technology)
- **Type:** arXiv preprint (cs.CL)
- **Location:** `research to be indexed/cybersec/arxiv-2611.23218-what-does-a-bias-head-measure-non-identifiabilit.pdf`
- **Retrieved:** 2026-11-18
- **arXiv:** 2611.23218v1, 17 November 2026
- **Read status:** read — 8 of 18 pages extracted 2026-11-22

## Narrative

A family of methods localizes social bias to individual attention heads and removes it by ablation. The methods are validated by their effect on a fairness metric. No one checks that the statistic which selects the heads actually measures bias. This paper audits that gap.

The audit runs on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct. First result: the head map correlates at rho = -0.950 and -0.768 with a label-blind response-length map. That looks like a clean surface confound.

An intervention rejects the reading. With the prompt held fixed, response length explains 1% of the statistic's variance. What explains the score is prompt identity, at 64% of variance, in an ordering that is not monotonic in length. The pooled correlation was a between-arm artifact.

The construct itself is unidentifiable. Inside a fixed prompt, the fairness label, the response length, and the presence of a protected-group token are collinear at phi = 0.95. Part of this is the labelling rule by definition. No observational analysis can attribute the map to any one of them, and no method in this family runs an experiment that could.

The substantive claims fail separately. Bias selectivity is not late-layer-concentrated on either model. No tested head set reduces the unfairness rate when ablated against a ten-draw layer-matched null.

The positive control is the useful part. The complement of the head set, scored on the opposite label, reliably destroys refusal behaviour (p = 2.7e-5). The pipeline detects effects at this scale, so the null result is not a power failure.

The paper also reports two measurement hazards. A single random baseline sits inside a null band spanning 0.641 to 1.000. Ablation-degraded generation is scored as fair: one arm produced 31% unclassifiable output and an apparent 0.127 reduction in unfairness.

The defensive lesson is general. A causal claim about an ablation needs an intervention, not a correlation. A degraded model that stops refusing must not be scored as improved.

[Source: arxiv-2611.23218-what-does-a-bias-head-measure-non-identifiabilit.pdf]

## Snippets

> "No observational analysis can attribute the map to any of them, and no method in this family runs an experiment that could."
[Source: arXiv:2611.23218v1 abstract]

> "Its complement, scored on the opposite label, reliably destroys refusal behaviour (p = 2.7 × 10−5), demonstrating that the pipeline detects effects at this scale."
[Source: arXiv:2611.23218v1 abstract]
