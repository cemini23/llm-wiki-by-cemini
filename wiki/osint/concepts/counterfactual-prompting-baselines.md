---
title: "Counterfactual Prompting Baselines — Why Paraphrase-Null Distributions Are Necessary"
type: concept
tags: [llm-evaluation, counterfactual-prompting, causal-inference, bias-detection, statistical-methodology]
keywords: [counterfactual-baselines, paraphrase-null, treatment-variation-irrelevance, jsd-kl-metrics, token-count-adjusted, medperturb, bias-in-bios]
related:
  - sources/counterfactual-prompting-2605.01048.md
  - entities/tools/deepeval.md
  - concepts/monte-carlo-permutation-test-mcpt.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/counterfactual-prompting-2605.01048.md — source paper (Northeastern / Bar-Ilan / Allen AI, 2026)
- @entities/tools/deepeval.md — complementary: deepeval provides the metrics infrastructure; this page provides the null-distribution framework

## Raw Concept

Synthesized from "Compared to What? Baselines and Metrics for Counterfactual Prompting" (arXiv 2605.01048). The core question: when we perturb an LLM prompt and observe output changes, how do we know the change is from the factor we targeted rather than from the model being sensitive to any text change?

## Narrative

Counterfactual prompting — surgically editing a prompt to change one factor and measuring output differences — is widely used to evaluate LLM bias, CoT faithfulness, and model sensitivity. This paper demonstrates that the method produces **meaningless results without paraphrase baselines**, and provides a statistical framework to fix it.

### The problem

Every counterfactual edit is a **compound treatment**: it bundles the variable of interest with incidental surface-form variation. Causal inference calls this a violation of *treatment variation irrelevance* — the effect of "changing gender" can't be separated from the effect of "changing words." The solution: compare target-intervention effects to a **null distribution** from meaning-preserving paraphrases that change a similar number of tokens.

### Empirical findings

| Context | Target perturbation | Flip rate | Paraphrase baseline | Significant? |
|---------|-------------------|-----------|---------------------|--------------|
| MedQA + DeepSeek-R1 8B | Gender swap | 14.9% | 14.1% | **No** |
| MedPerturb (120 tests) | Gender + style | varies | varies | Only 5/120 (all "colorful" style, 8B model) |
| Bias-in-Bios | Gender swap | directional | below baseline | **Yes** — real directional bias detected |

The framework is not overly conservative — it detects real effects when they exist (Bias-in-Bios gender bias) and correctly passes null effects (gender on MedQA).

### The method

1. **Baseline construction:** Generate meaning-preserving paraphrases with token-change count matched to the target perturbation (token-count adjustment matters — flip rates scale with edit distance).
2. **Metric selection:** Per-sample distributional metrics (JSD, KL) are dramatically more powerful than aggregate metrics (MI, phi, flip rate). Regression uniquely characterizes effect direction and magnitude.
3. **Statistical testing:** One-sided paired t-test for per-sample metrics; nonparametric bootstrap for aggregate metrics. Bonferroni correction within test families.

### Relevance to OSINT workspace

This directly upgrades our claim-validation methodology:
- **`[CONFIRMED]` / `[TENTATIVE]` tags:** When evaluating LLM-based claims (e.g., "model X shows bias Y"), a paraphrase baseline is now a requirement for `[CONFIRMED]` status.
- **Tool evaluation:** When auditing tools that make claims about LLM behavior (bias detection, safety eval), check whether they use baseline-controlled counterfactuals.
- **Wiki gap detection:** The JSD/KL per-sample approach can be adapted to measure drift between wiki page versions or between source and synthesis.
