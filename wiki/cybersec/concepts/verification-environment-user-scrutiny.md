---
title: "The verification environment: signifier is not inspectable evidence"
type: concept
related:
  - sources/arxiv-user-scrutiny-llm-conversations-2611.08232.md
  - concepts/citation-is-not-consultation.md
  - concepts/verification-generation-gap.md
updated: 2026-11-10
---

## Raw Concept

Question: **when an assistant answer claims evidence, what can the user actually inspect, and what do users do next?** From arXiv 2611.08232, an observational study of 368,644 qualifying assistant–user response pairs.

## Narrative

The paper separates four things that a transparency score often merges.

| Component | Definition | Example |
|---|---|---|
| Verification signifier | language that invokes authority without exposing a source | "According to the agency's official notice" |
| Material verification support | an object the user can inspect | an explicit URL, a markdown link, a preserved source object |
| Epistemic cue | how the assistant presents its own certainty | uncertainty, confidence, disclaimer, refusal |
| Verification pathway | an action offered or taken | "Shall I check the notice?" — or the user's next message |

A signifier can suggest that evidence exists while giving the user nothing to open.

### The measured gap

In the released records, broad attribution appears in **31.9%** of qualifying responses. Explicit URLs appear in **1.33%**. Any inspectable evidence appears in **1.46%**. The ratio is about 24:1, or 10:1 to 20:1 after an estimated detector precision of 0.67.

Attribution and URLs are almost uncorrelated (φ = 0.03). Naming an authority and showing a source are empirically distinct behaviours.

### What predicts user scrutiny

Scrutiny means checking or challenging. It covers **28.7%** of qualifying pairs. Almost every measured cue accompanies both checking and challenging. Only uncertainty shows a small pooled difference that favours checking, and it is 6% in ratio terms.

Task context matters more than response wording. In Technical Help, uncertainty favours checking. In Seeking Information, refusals and reasoning traces favour challenging. Opening topic, intent and position predict next-turn behaviour better than response features do.

Scrutiny clusters in conversations. The apparent turn-to-turn persistence shrinks once conversation-level differences are removed.

### Why this belongs in a security wiki

Three uses.

**Transparency claims.** A vendor that reports "grounding" should report the share of claims with a preserved, inspectable source and the share of those that resolve. A signifier rate is not a transparency metric.

**Human verification inside a SOC.** An analyst reading an AI summary sees authority language far more often than a link. The measured ratio tells the analyst how often the language stands alone.

**Covert-channel and leakage work.** A model that describes its own evidence without exposing it produces a plausible-looking answer that an auditor cannot test. That is the same shape as a leakage finding where the output looks benign but the grounding is unverifiable.

### Limits

The labels are model-assigned, with no double-coded human sample and no recall estimate. The corpora are public share collections, so the mix of models and users is not production traffic. The authors state the study measures visible acts, not private trust or successful verification.

Confidence: the prevalence figures are `[TENTATIVE]` — one corpus pair, model-labelled outcomes.

## Snippets

> "Broad attribution and explicit URLs are almost uncorrelated (φ = 0.03). Mentioning an authority and exposing a source are empirically distinct features in these records." [Source: arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf p.8]

> "A transparency measure that treats the two as equivalent would reward how convincingly an answer sounds sourced, even where little evidence is provided to examine." [Source: arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf p.9]
