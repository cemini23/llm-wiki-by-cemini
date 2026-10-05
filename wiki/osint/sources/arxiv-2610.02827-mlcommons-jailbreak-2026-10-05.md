---
title: "MLCommons Jailbreak Benchmark v1.0 — Resilience Gap for text-to-text LLMs"
type: source
tags: [arxiv, safety, jailbreak, evaluation]
keywords: [2610.02827, resilience-gap, adversarial-testing, mlcommons, ailuminate]
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
| Title | MLCommons Jailbreak Benchmark v1.0 |
| Authors | Carsten Maple (corresponding), Cagatay Yucel, Isaac Holeman, Chris Knotz, Peter Mattson, and others (MLCommons and partners) |
| Type | arXiv paper |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.02827-mlcommons-jailbreak-benchmark-v1-0.pdf` |
| Retrieved | 2026-10-05 |
| arXiv | 2610.02827 |
| read-status | read |

## Narrative

This is the first complete end-to-end run of the MLCommons Jailbreak
methodology. The benchmark covers text-to-text, single-turn, prompt-level jailbreak
attacks in a black-box setting. It compares paired baseline and attacked prompts
across eight open-weight systems and eleven hazard categories. It reports two
scores: the baseline unsafe-response rate and the attacked rate. The difference is
the Resilience Gap.

The authors measure across all systems, hazards, and attacks. The unsafe-response
rate rises from 11.08% at baseline to 18.65% under attack. The average Resilience
Gap is 7.57 percentage points. This is lower than the 19.8 points in Jailbreak
v0.5, but the two releases differ in systems, seeds, attacks, and evaluator. Three
systems (Gemma 4 31B Instruct, DeepSeek-V4-Pro, and Kimi K2.6) show negative gaps.
Role-Play/Template and Wrappers/Schemas attacks are the most effective. The
evaluator ensemble has a 16.4% false non-violating rate and a 37.9% false violating
rate. The exact attacks are withheld under a risk-calibrated disclosure policy.

For this workspace: the paper gives a governance-grade jailbreak evaluation with a
paired metric that separates attack effect from baseline refusal. That matters to
agent security and red-teaming, and to any local model robustness test. The
Resilience Gap framing is a clean model for measuring harness and guardrail
changes. The disclosure policy is a useful template for dual-use release decisions.

[Source: arXiv:2610.02827]

## Snippets

> "Across all evaluated SUTs, hazard categories, and included jailbreak attacks, the unsafe-response rate increased from 11.08% under baseline conditions to 18.65% under jailbreak conditions. This corresponds to an average Resilience Gap of 7.57 percentage points."
[Source: arxiv-2610.02827-mlcommons-jailbreak-benchmark-v1-0.pdf p.30]

> "Three systems; Gemma 4 31B Instruct, DeepSeek-V4-Pro, and Kimi K2.6, showed negative Resilience Gaps. This indicates that their measured unsafe-response rates were lower for attack prompts than for the corresponding baseline prompts."
[Source: arxiv-2610.02827-mlcommons-jailbreak-benchmark-v1-0.pdf p.30]

> "The exact attack prompts, reusable templates, transformation procedures, implementation code, and detailed attack configurations are intentionally withheld."
[Source: arxiv-2610.02827-mlcommons-jailbreak-benchmark-v1-0.pdf p.8]

> "Role-Play and Template Jailbreaks at 35.7% and Wrappers and Schemas at 32.8% produce the highest mean unsafe-response rates, while Encoding and Unicode Tricks, Direct Override Patterns, and both Perturbation categories fall between 12.0% and 14.9%."
[Source: arxiv-2610.02827-mlcommons-jailbreak-benchmark-v1-0.pdf p.33]
