---
title: "Provider refusal as a measurement contaminant"
type: concept
related:
  - sources/arxiv-nfr-to-hyperparameter-quantum-2611.16902.md
  - concepts/guardrail-construct-validity-agent-eval.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/silent-error-rate-structured-output.md
updated: 2026-11-14
---

## Raw Concept

Question: **when a model refuses a test item, what did the benchmark actually measure?** From arXiv 2611.16902 (University of Tennessee).

## Narrative

A benchmark run returns a failure. The analyst records a model error. In some cases the model did not answer at all, because a provider safety filter blocked the request or the response. The score then measures moderation policy, not capability.

### The observed case

A study of natural-language requirement translation ran 540 synthetic stories. Thirteen failures for one model returned `Failed.` instead of a score. All thirteen came from five hazard-themed seed families: aerosol dispersion, geoengineering, antiviral molecule generation, viral protein-structure retrieval, and antibody docking. Each seed crossed ten intents, so the group covers 50 stories.

On that subset the same model passed 0 of 13. Other models passed 7 to 12 of 13. Under the strict protocol, those cells count as translation errors. Under the correct reading, the model was never asked.

### Why the distinction matters

Three different events produce a blank result:

| Event | Cause | Owned by |
|---|---|---|
| Model error | Wrong output | Model |
| Parse failure | Unusable format | Harness |
| Provider refusal | Policy filter | Provider policy |

Only the first is a capability signal. The second is a harness defect. The third is a policy property that can change without notice, per provider and per version.

Mixing them has two effects. It understates capability on hazard-adjacent tasks. It also gives a false sense of safety, because a refusal is counted as a wrong answer rather than a blocked request.

### Handling rule

1. Log the refusal separately. Detect it by an error object or a sentinel, not by string matching on polite text.
2. Exclude refused items from the capability denominator, and report the excluded count.
3. Re-run the excluded items on a local open-weight model if the question is still open.
4. Never compare two providers on a set that one provider refuses. Compare on the intersection, and state the intersection size.

### Scope

The effect is largest on hazard-themed prompts. These are exactly the prompts in red-team, guardrail and CBRN-adjacent evaluations. Any benchmark with provocation content can carry this contaminant, and the contamination is invisible in an aggregate score.

### Related measurement controls

- Exclude items blocked by the judge provider, and report the count. The source paper does this: 11–12 of 1,137 items were blocked and excluded.
- Report the judge identity with every absolute number, because level shifts with the judge.
- Keep the pre-registered protocol and report both the strict and the corrected result.

## Snippets

> "A subset of apparent failures was instead traced to provider safety refusals on hazard-themed stories, conflating translation error with moderation policy." [Source: arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf p.1]

> "Refusal effects should be disentangled from translation quality." [Source: arxiv-2611.16902-non-functional-requirements-to-hyperparameter-tr.pdf p.1]
