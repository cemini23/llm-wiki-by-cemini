---
title: "Guardrail construct validity — Invalid before policy claims (K321)"
type: concept
tags: [concept, agent-security, audit, measurement, guardrails, k321]
keywords: [construct validity, protocol isolation, incentive validity, stochastic stability, welfare accounting, agent market eval, guardrail measurement]
related:
  - sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md
  - concepts/compliance-verdict-rule-invariance.md
  - concepts/threat-preserving-representation-sensitivity.md
  - concepts/adversarial-region-estimation-vs-single-example.md
  - sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md
  - sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md
  - concepts/compliance-boundary-adjacent-pair-search.md
  - sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md
  - concepts/benchmark-shortcut-attack-pyramid-audit.md
  - sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md
  - concepts/certified-selective-prediction-guardrails.md
  - sources/arxiv-2609-22048-available-guardrails-selective-prediction.md
  - sources/arxiv-2609-01519-guardrail-construct-validity.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/ai-redteam-evidential-ceiling.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/culturally-responsive-llm-benchmark-audit.md
  - sources/arxiv-bmms-policy-conditioned-behavioral-compliance-2611.09147.md
  - concepts/policy-conditioned-compliance-measurement.md
  - sources/arxiv-jev-llm-safety-guardrail-2611.08845.md
  - concepts/external-filter-safety-utility-tradeoff.md
  - sources/arxiv-safety-as-a-budget-2611.16628.md
  - sources/arxiv-nfr-to-hyperparameter-quantum-2611.16902.md
  - sources/arxiv-parsed-plausible-wrong-output-format-2611.17169.md
  - concepts/provider-refusal-measurement-contamination.md
  - concepts/safety-budget-control-channel-calibration.md
  - concepts/silent-error-rate-structured-output.md
maturity: draft
created: 2026-09-02
updated: 2026-11-14
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc (K321)"
---

## Relations

- @sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md — K408-K417 ingest / 2026-10-09
- @concepts/compliance-verdict-rule-invariance.md — K408-K417 ingest / 2026-10-09
- @concepts/threat-preserving-representation-sensitivity.md — K408-K417 ingest / 2026-10-09
- @concepts/adversarial-region-estimation-vs-single-example.md — K408-K417 ingest / 2026-10-09
- @sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md — K403-K407 ingest source page
- @sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md — K398-K402 ingest source page
- @concepts/compliance-boundary-adjacent-pair-search.md — K398 adjacent-pair compliance boundary testing
- @sources/arxiv-2610-03585-threat-preserving-representation-sensitivity.md — K395-K397 ingest source page
- @concepts/benchmark-shortcut-attack-pyramid-audit.md — K387-K391 cross-link
- @sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md — K387-K391 ingest source page
- @sources/arxiv-2609-01519-guardrail-construct-validity.md — construct validity contract (2609.01519)
- @sources/arxiv-2609-22048-available-guardrails-selective-prediction.md — K354 certified availability (2609.22048)
- @concepts/certified-selective-prediction-guardrails.md — K354 pairs construct validity with deployment availability
- @concepts/measurement-integrity-mcp-security-eval.md — K277 labels ≠ endpoints; integrity chain

## Raw Concept

Question: **when does a guardrail eval actually measure guardrail effect, not protocol drift?**

## Narrative

Agent guardrail studies can show large welfare or safety lifts that **reverse** when the transaction **protocol** (schemas, choosers, incentives) is held fixed. **K321 (2609.01519)** proposes a **construct-validity contract** with four checks:

1. **Incentive validity** — manipulations move incentives in the expected direction.
2. **Protocol isolation** — guarded vs unguarded agents share the same offer/choice interface.
3. **Stochastic stability** — enough generations; report uncertainty (bootstrap CIs).
4. **Welfare accounting** — scripted positive controls bound interpretability.

Return **Invalid** or **Inconclusive** before licensing causal guardrail claims. Pairs K277 measurement integrity and K271 faithful ASR reporting.

### Two more validity checks (November 2026)

The three sources below add two failure modes to the contract.

**1. A budget reads a level, not a ranking.** A safety target stated as a rate budget compares the scorer mean with the budget. Rank quality does not enter that comparison. A scorer can rank well and still carry a mean bias of 0.16, which drives the controller into a saturated or inactive state. Measure the mean bias on labeled responses before you report a budget result. See @concepts/safety-budget-control-channel-calibration.md.

**2. Provider refusal is a missing data point.** When a provider filter blocks a test item, the benchmark records a failure that measures policy, not capability. Exclude the item, report the excluded count, and never compare providers on a set that one provider refuses. See @concepts/provider-refusal-measurement-contamination.md.

**3. Exact match hides silent errors.** Rank parsers and tool calls on the four-way split, and treat the silent-error rate as the deployment objective. See @concepts/silent-error-rate-structured-output.md.

## Snippets

> The case study does not establish that guardrails are ineffective; it establishes that their apparent value is unidentified until the simulated agents and protocol pass these checks. [Source: arXiv 2609.01519 abstract, paraphrase]
