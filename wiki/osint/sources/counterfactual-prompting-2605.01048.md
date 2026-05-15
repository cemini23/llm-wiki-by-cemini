---
title: "Compared to What? Baselines and Metrics for Counterfactual Prompting (arXiv 2605.01048, 2026)"
type: source
tags: [arxiv, llm-evaluation, counterfactual-prompting, causal-inference, bias-detection, statistical-testing, 2026]
keywords: [counterfactual-baselines, paraphrase-null-distribution, treatment-variation-irrelevance, jsd-kl-metrics, medqa-gender-swap, medperturb, bias-in-bios]
related:
  - concepts/counterfactual-prompting-baselines.md
maturity: draft
read_status: deep-read
created: 2026-05-14
updated: 2026-05-14
clusters: [llm-agents]
---

## Relations

- @concepts/counterfactual-prompting-baselines.md — concept page synthesizing the framework

## Raw Concept

- **Title:** Compared to What? Baselines and Metrics for Counterfactual Prompting
- **Authors:** Zihao Yang (Northeastern), Mosh Levy (Bar-Ilan), Yoav Goldberg (Bar-Ilan / Allen AI), Byron C. Wallace (Northeastern)
- **Type:** arXiv preprint (2605.01048v1)
- **Location:** `cemini-librarian:/opt/cemini-bulk/research/2605.01048v1.pdf`
- **Retrieved:** 2026-05-14
- **Pages:** 8 (two-column)

## Narrative

The paper argues that counterfactual prompting studies — widely used to evaluate LLM bias, CoT faithfulness, and model sensitivity — produce unreliable results without baseline comparisons against meaning-preserving paraphrases. The core problem: every counterfactual edit is a compound treatment bundling the variable of interest with incidental surface-form variation, violating treatment variation irrelevance from causal inference.

Key empirical finding: When DeepSeek-R1 is evaluated on MedQA clinical vignettes, gender-swap perturbations produce a 14.9% answer flip rate — but benign paraphrasing produces a nearly identical 14.1% flip rate. The gender effect is statistically indistinguishable from noise.

The authors propose a framework: compare target-intervention effects to a null distribution from token-count-adjusted paraphrases, using statistical testing (one-sided paired t-test for per-sample metrics; bootstrap for aggregate metrics). Six metrics are evaluated: flip rate, KL divergence, JSD, mutual information, phi coefficient, and regression coefficient.

Key findings: (1) Model sensitivity to paraphrasing scales with token-change count — magnitude-matched baselines are necessary. (2) Of 120 tests on MedPerturb (gender + style perturbations), only 5 reach significance after Bonferroni correction — all for "colorful" style on the 8B model. Gender perturbations show no significant effects. (3) On Bias-in-Bios, the framework does detect real directional gender bias, confirming it's not overly conservative. (4) Per-sample metrics (JSD, KL) are dramatically more powerful than aggregate metrics (MI, phi, flip rate).

## Snippets

> "Observed effects cannot be reliably attributed to the targeted factor without accounting for baseline 'meaning-preserving' modifications to text that establish general model sensitivity." (Abstract)

> "Gender swap: 14.9% flip rate. Benign paraphrase: 14.1% flip rate. [...] It would therefore be unwarranted to conclude that the LLM is especially sensitive to patient gender." (§1, Fig 1)

> "Per-sample metrics (JSD, KL) are dramatically more powerful than aggregate metrics (MI, phi, flip rate) and regression powerfully and uniquely characterizes effect direction and magnitude." (Abstract)
