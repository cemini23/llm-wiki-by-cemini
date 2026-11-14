---
title: "BMMS: policy-conditioned measurement of behavioral compliance in language models (arXiv 2611.09147)"
type: source
related:
  - concepts/policy-conditioned-compliance-measurement.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/compliance-verdict-rule-invariance.md
  - sources/arxiv-safety-as-a-budget-2611.16628.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | BMMS: Policy-Conditioned Measurement of Behavioral Compliance in Language Models |
| Author | Anthony Rhodes; Gadi Singer (Confidential Core AI) |
| Type | arXiv preprint (cs.AI) — NeurIPS 2026 TAE workshop |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf` |
| Retrieved | 2026-11-09 |
| File | `arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf` |
| Pages | 21 |
| Read status | read |

## Narrative

Fixed-taxonomy benchmarks measure hallucination, sycophancy, toxicity and over-refusal. A regulated operator asks a different question: does this system do what our rulebook requires? The Behavioral Misalignment Metric Suite (BMMS) takes a **policy corpus as an argument** and returns a compliance profile over it. Customisation to a domain is a structural property, not a claim.

### The four metrics

| Metric | Question |
|---|---|
| CAS — Compliance Attainment Score | Of the obligations that bind this system, weighted by severity, what fraction does it meet? |
| CRM — Compliance Robustness Margin | How much attainment survives graded adversarial pressure? |
| BIV — Behavioral Invariance | Does a rule survive meaning-preserving rephrasing? |
| BDI — Behavioral Disposition Index | Which dispositions, such as over-refusal, move compliance without registering as it? |

CAS and CRM are measured at full scale here. BIV and BDI are specified and released with the suite.

Severity is read from the modal verb in the source span, with two classes (HARD and SOFT). Each admitted rule gets four probes in fixed order: direct request, embedded scenario, boundary case, adversarial pressure. The probe set is hashed and frozen, so every target answers the identical exam.

### The admission test

A dimension enters the suite only if it passes five criteria: construct, independence, sensitivity, discrimination, and **attribution**. Attribution is the binding criterion. A quantity that moves when the judge changes, holding the target fixed, is measuring the instrument. One of the suite's own reported quantities failed and was excluded.

### The policy corpus

Eleven public documents in five registers yield **1,003 candidate obligations**. Vendor specifications score the highest bindability. A bindability funnel runs from 1,003 extracted to 231 non-mixed obligations, and probes run on 401 majority-bindable rules.

The yield spread is itself a result. Admission rates are 68.0% for vendor specifications, 32.3% for AI-transparency statutes, 25.4% for conduct regulation, and 16.0% for analytical guidance. After per-register precision correction, the ratio widens: vendor specification rises to 82.0% and analytical guidance falls to 8.0%. The documents that govern deployed AI behaviour are written by vendors, not regulators.

### Validity against human judgement

A blinded expert annotated 60 items. Precision of the admission criterion is **94.4% on vendor specifications**, 66.7% on conduct regulation, and 50.0% on analytical guidance. Extraction fidelity is 94.6%. Extraction preserves the obligation and sheds its qualifiers, so measured violation is inflated and never suppressed.

### The judge panel

Stored records were re-scored under two further judges from two other providers. The judges disagree about level and agree about order. A single target's absolute CAS spans as much as 0.216 across the three judges. Kendall τ is +1.000 between the two swap judges and +0.905 against the primary. The paper therefore reports ordering as the quantity that carries claims, and labels every absolute level with its panel range.

The headline: GPT-4o fails 70.7% of the hard constraints binding it in OpenAI's own Model Spec, where the two Claude models fail 0.0% and 9.1%. Section 5 reports the same cell under the judge panel as 35.0%, 22.5% and 42.5% for GPT-4o. The direction holds under every judge. The magnitude varies by about a factor of two.

### Defensive reading

This is a usable audit pattern for a defensive team. Write the obligation list first. Admit only obligations that an assistant can comply with or violate in one response or one tool call. Report a profile, not a scalar. Label every absolute score with its judge panel range. A vendor specification is a better source of actionable rules than the regulation that nominally covers the same conduct.

### Limits

The absolute numbers rest on a single corpus and a single primary judge. The level criterion for attribution failed on most targets. BIV and BDI carry partial evidence only. The own-specification comparison cannot resolve a self-preference advantage from zero once document difficulty is subtracted.

## Snippets

> "We introduce the Behavioral Misalignment Metric Suite (BMMS), which measures policy-conditioned misalignment by taking a policy corpus as an argument and returning a compliance profile over it, so customizability to a regulated domain is a structural property rather than a claim." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.1]

> "BMMS shows, for example, that GPT-4o fails 70.7% of the hard constraints binding it in OpenAI's own Model Spec, where the two Claude models fail 0.0% and 9.1% of theirs." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.1]

> "A5, the criterion the suite is designed around: a quantity that moves when the judge changes, holding the agent fixed, is measuring the instrument." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.5]

> "The documents that govern AI behavior are written by vendors, not by regulators." [Source: arxiv-2611.09147-bmms-policy-conditioned-measurement-of-behaviora.pdf p.6]
