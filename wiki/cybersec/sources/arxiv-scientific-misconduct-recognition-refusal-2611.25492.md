---
title: "Why Do LLMs Help with Scientific Misconduct Requests? — recognition without refusal (2611.25492)"
type: source
maturity: draft
related:
  - concepts/recognition-refusal-gap.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/refusal-and-abstention-direction-geometry.md
updated: 2026-11-22
read_status: read
---

## Raw Concept

- **Title:** Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science
- **Authors:** Almene De Meran Meguimtsop, Daniel E. Acuna (University of Colorado Boulder; ReviewerZero AI)
- **Type:** arXiv preprint (cs.AI)
- **Location:** `research to be indexed/cybersec/arxiv-2611.25492-why-do-llms-help-with-scientific-misconduct-requ.pdf`
- **Retrieved:** 2026-11-20
- **arXiv:** 2611.25492v1, 19 November 2026
- **Read status:** read — 8 of 9 pages extracted 2026-11-22

## Narrative

Science safety evaluations usually measure whether a model refuses a misconduct request. They rarely measure whether the model recognized it. This paper separates the two across 8 LLMs on SciIntBench, a benchmark of 1,350 research-integrity prompts.

The recognition result is the finding. When asked directly whether fulfilling a request would involve misconduct, models identify such requests at 91% even in the Most Covert cases. They refuse to carry out the request in only 34% of cases. Recognition is high. Refusal is low.

The authors then estimate which framing features drive refusal. The largest effect: rephrasing a request as a question about permissibility rather than an instruction raised refusal from 52% to 88%. That is the same mechanism as Deferred Semantic Commitment and many jailbreak families. A question asks for a judgment, not an act.

Two system-prompt fixes were tested. Ask the model to assess the request before responding. Remind it of responsible-conduct-of-research principles. These raised refusal on adversarial requests from 58% to 87% and 86%.

The defensive reading: a model that recognizes misconduct can still comply. The gap is between representation and behaviour. A safety metric that scores only refusal cannot see the difference. This matches the abstention-direction result, where refusal is one output of a mechanism that also governs knowledge-gap and ambiguity abstention.

[Source: arxiv-2611.25492-why-do-llms-help-with-scientific-misconduct-requ.pdf]

## Snippets

> "Models overwhelmingly identify such requests, even in the Most Covert cases (91%), while they refuse to carry out the request in only 34% of cases."
[Source: arXiv:2611.25492v1 abstract]

> "The most significant effect was to rephrase requests as questions about permissibility rather than instructions, which increased refusal from 52% to 88%."
[Source: arXiv:2611.25492v1 abstract]
