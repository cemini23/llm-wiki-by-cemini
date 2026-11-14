---
title: "Non-functional requirements to hyperparameter translation for quantum software via LLMs (arXiv 2611.16902)"
type: source
related:
  - concepts/provider-refusal-measurement-contamination.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/agent-safety-executable-evaluation.md
  - sources/arxiv-parsed-plausible-wrong-output-format-2611.17169.md
  - concepts/silent-error-rate-structured-output.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Non-Functional Requirements to Hyperparameter Translation for Quantum Software via LLMs |
| Author | Joseph G. Bronyah; Nasir U. Eisty (University of Tennessee, Knoxville) |
| Type | arXiv preprint, 2611.16902v1 |
| Location | `research to be indexed/cybersec/arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf` |
| URL | https://arxiv.org/abs/2611.16902 |
| Retrieved | 2026-11-13 |
| Pages | 11 |
| Read status | read |

## Narrative

Quantum software has a translation gap. A stakeholder says "respond quickly" or "protect accuracy." The framework accepts only numbers, such as circuit `shots` and transpiler `optimization_level` in Qiskit. The paper asks whether an LLM can bridge that gap better than a keyword heuristic.

### Design

Seven LLM agents compete against a deterministic keyword baseline on two tiers: **540 synthetic user stories** and **18 real-world holdout stories** written from quantum hackathon codebases. Each story is translated to a JSON configuration. A separate LLM judge scores the configuration against an intent-aware rubric. Simulation then measures the execution consequence on Qiskit/Aer, transpiled for FakeBrisbane (a 127-qubit model).

The metric design matters. The paper scores execution outcomes, not text similarity. A configuration that is well formed but wrong still passes schema validation. Only simulation shows the wasted shots or the lost sampling reliability.

### Results

Every LLM beat the heuristic on semantic pass rate.

| Target | Synthetic SPR | Real-world SPR |
|---|---|---|
| Keyword heuristic | low | 16.7% |
| Claude Sonnet 4.6 | high | **83.3%** |
| GPT 5.4 | high | 77.8% |
| GPT OSS 120B | high | 77.8% |
| All LLMs | high | 55.6–83.3% |

No LLM-to-LLM pair survived Holm correction on the real-world holdout. The paper therefore claims broad superiority over the heuristic, and no ranking among models. Only the heuristic showed detectable domain shift between the synthetic and real tiers.

Speed and cost configurations were consistently faster and cheaper. The fidelity hypothesis failed: top-state probability did not rise for accuracy-oriented stories.

### Provider refusals pollute the measurement

Error analysis found **13 Claude Sonnet 4.6 failures** that returned `Failed.` rather than a score. All 13 traced to five hazard-themed synthetic seeds: volcanic aerosol dispersion, stratospheric geoengineering, antiviral molecule generation, viral-target protein-structure retrieval, and antibody-viral-spike docking. Each seed crosses ten intent templates, so the group covers 50 of the 540 stories.

On the flagged subset, Claude passed 0/13. The heuristic passed 7/13. DeepSeek v4Pro, GPT-5.4 and Qwen 80B passed 12/13 each.

A strict protocol scores those cells as translation errors. That is wrong. A provider safety refusal is a policy outcome, not a parsing failure. The paper states the correct handling: separate the refusal effect from translation quality. No real-world story matched the hazard definition, so the exclusion set there is 0/18.

### Defensive reading

Two rules transfer to any LLM capability evaluation.

1. Score the execution consequence, not the text. A well-formed configuration can still violate the stated requirement.
2. Treat a provider refusal as a missing data point. Report it in its own column. Do not count it as a model error, and do not let it move the ranking.

The second rule is a measurement-integrity control. It applies to red-team scoring, guardrail benchmarks and agent evaluations that use hazard-themed prompts.

### Limits

The real-world holdout is 18 stories, so its confidence intervals are wide. The synthetic stories come from author templates, which may be cleaner than real stakeholder language. Gate times and the dollar rate are illustrative proxies, not a vendor quote.

## Snippets

> "A subset of apparent failures was instead traced to provider safety refusals on hazard-themed stories, conflating translation error with moderation policy." [Source: arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf p.1]

> "An LLM's structured output can be semantically plausible without its execution preserving the original requirement's intent." [Source: arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf p.3]

> "Claude passed 0/13 of this flagged synthetic subset, whereas the same stories were passed by the baseline heuristic in 7/13 cases." [Source: arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf p.6]
