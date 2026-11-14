---
title: "Signals, evidence, and context: user scrutiny in real-world LLM conversations (arXiv 2611.08232)"
type: source
related:
  - concepts/verification-environment-user-scrutiny.md
  - concepts/citation-is-not-consultation.md
  - concepts/verification-generation-gap.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Signals, Evidence, and Context: User Scrutiny in Real-World LLM Conversations |
| Author | Ahana Biswas; Yu-Ru Lin (University of Pittsburgh) |
| Type | arXiv preprint (cs.AI) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf` |
| Retrieved | 2026-11-06 |
| File | `arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf` |
| Pages | 38 |
| Read status | read |

## Narrative

The study asks a simple question with a large dataset. When an assistant answer claims evidence, does the answer also give the user something to inspect? And what do users do next?

The corpus holds 489,283 assistant–user response pairs from ShareChat and WildChat, across 98,007 conversations. A qualifying pair is an assistant answer joined to the next user message on a checkable claim. There are 368,644 qualifying pairs. Next-turn behaviour gets one of three labels: accepting, checking, or challenging. Checking and challenging together make **scrutiny**.

### Finding 1 — grounding language outnumbers inspectable evidence

Broad attribution language appears in **31.9%** of qualifying responses (117,715). Explicit URLs appear in **1.33%** (4,889). Any inspectable evidence indicator appears in **1.46%** (5,372). The attribution-to-URL ratio is about **24:1**. After an estimated detector precision of 0.67, the ratio falls to roughly 10:1 to 20:1.

Attribution language and explicit URLs are almost uncorrelated (φ = 0.03). Naming an authority and showing a source are different features in practice.

In Perplexity's released records, citation-like attribution appears in 10.3% of assistant turns. Of those turns, **39.8% have no preserved URL or source object**. That is 4.1% of all turns.

### Finding 2 — cues accompany both checking and challenging

Every measured cue accompanies both checking and challenging relative to acceptance. Only uncertainty shows a small pooled difference that favours checking. Its relative risk ratios are 1.10 for checking and 1.04 for challenging; the direct ratio is 1.06 (95% CI [1.02, 1.10], q = 0.018).

The lesson is negative. The wording of an answer gives limited information about whether a user will ask for support or dispute the claim.

### Finding 3 — task context changes the association

In Technical Help, uncertainty favours checking (check/challenge ratio 1.26, q < 0.001). In Seeking Information, refusals favour challenging (0.62, q = 0.015), and reasoning traces also favour challenging (0.89, q = 0.010). Reasoning traces reverse direction between the two corpora.

Opening topic, intent and position predict next-turn behaviour better than response features do: macro AUC 0.592 against 0.551.

### Finding 4 — scrutiny clusters in conversations

Scrutiny is concentrated in some conversations. The apparent turn-to-turn persistence becomes much smaller when conversation-level differences and response ordering are separated.

### Defensive reading

The paper gives a usable metric for transparency claims. A count of "citations" is not a count of inspectable support. A vendor that reports a grounding rate should report the share of claims with a preserved, inspectable source, and the share of those that resolve.

The second use is for human verification in a SOC. An analyst reading an AI summary sees attribution language far more often than a link. The paper measures how often that language sits alone.

### Limits

The labels are model-assigned, with estimated precision 0.89 for checking and 0.92 for challenging on positive cases. There is no double-coded human sample and no recall estimate. The corpora are public share collections, so the mix of models and users is not a production sample.

## Snippets

> "Broad attribution language appears in 31.9% of qualifying responses, compared with explicit URLs in 1.33%, revealing a gap between claims of grounding and preserved inspectable support." [Source: arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf p.1]

> "The attribution-to-URL ratio is about 24:1. Broad attribution and explicit URLs are almost uncorrelated (φ = 0.03). Mentioning an authority and exposing a source are empirically distinct features in these records." [Source: arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf p.8]

> "Uncertainty is the only feature with a statistically distinguishable pooled checking-versus-challenging association after nine-test correction." [Source: arxiv-2611.08232-signals-evidence-and-context-user-scrutiny-in-re.pdf p.10]
