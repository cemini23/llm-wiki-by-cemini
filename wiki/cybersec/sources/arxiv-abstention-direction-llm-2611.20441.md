---
title: "Abstention Direction in Large Language Models — query, knowledge and value abstention share a component (2611.20441)"
type: source
maturity: draft
related:
  - concepts/refusal-and-abstention-direction-geometry.md
  - concepts/recognition-refusal-gap.md
  - concepts/low-asr-is-not-refusal.md
updated: 2026-11-22
---

## Raw Concept

- **Title:** Abstention Direction in Large Language Models: Mechanistic Interpretability of Abstention Across Query Ambiguity, Knowledge Limits, and Safety Alignment
- **Authors:** Koki Itai, Jun Hirako, Hiroaki Yamagiwa (SB Intuitions Corp.)
- **Type:** arXiv preprint (cs.CL)
- **Location:** `research to be indexed/cybersec/arxiv-2611.20441-abstention-direction-in-large-language-models-me.pdf`
- **Retrieved:** 2026-11-17
- **arXiv:** 2611.20441v1, 16 November 2026
- **Read status:** read — 8 of 26 pages extracted 2026-11-22

## Narrative

Prior refusal-direction work studied one cause of abstention: a query that conflicts with human values. This paper separates three causes and compares them.

- **Query (Q):** the query is ambiguous or incomplete.
- **Model Knowledge (MK):** the query lies beyond the model's knowledge boundary.
- **Human Values (HV):** the query may compromise safety.

For each cause the authors build counterfactual pairs. The pair shares a template and differs only in the abstention-inducing slot. For example, "When did the film Casino Royale come out?" against "When did the 2006 film Casino Royale come out?" The mean activation difference is normalized into an abstention direction.

Activation steering at middle layers raises or lowers abstention in all three perspectives. Adding the direction (m > 0) promotes abstention. Subtracting it (m < 0) suppresses abstention, so the model answers an unknown-entity question with a confident invented answer.

The cross-perspective result is the important one. Steering with the direction from one perspective also moves abstention in the other two. Cosine similarity between the directions confirms a shared directional component.

The security reading: a refusal is one output of a shared abstention mechanism. A model can suppress abstention for a knowledge gap and, in the same intervention, lower refusal for a harmful query. Measurement must separate the three causes.

[Source: arxiv-2611.20441-abstention-direction-in-large-language-models-me.pdf]

## Snippets

> "Intervening in middle layers increases or decreases abstention across all three perspectives. Moreover, steering yields cross-perspective effects, indicating that the abstention directions share a common directional component."
[Source: arXiv:2611.20441v1 abstract]

## Dead Ends

- **Partial-read note (2026-11-22):** 8 of 26 pages read. Layer sweep details and the full cosine table are in the unread pages. [Source: arxiv-2611.20441-abstention-direction-in-large-language-models-me.pdf]
