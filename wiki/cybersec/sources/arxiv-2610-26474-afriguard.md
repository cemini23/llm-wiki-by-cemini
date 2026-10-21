---
title: "AfriGuard — safety and refusal across ten African languages"
type: source
related:
  - concepts/k293-cybersec-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: AfriGuard: Safety and Robust Refusal For African Languages
Authors: Israel Abebe Azime and colleagues (Masakhane NLP, Saarland University, Cohere Labs, and others)
Type: arXiv preprint (2610.26474)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.26474-afriguard-safety-and-robust-refusal-for-african.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

AfriGuard is a multilingual set for harmful intent, safety-category labels, and refusal behavior across **10 African languages and English**.

Guardrail models underperform both open and closed LLMs on safety-intent and safety-category classification. Models score **below 60% F1** on appropriate safety behavior. Failures are often not an explicit refusal. The model produces linguistically inadequate text, so the user gets no help by accident. That is the same shape as "ignored, not refused" in @sources/arxiv-2610-23254-ignored-not-refused.md.

Using the set, the authors train small guard models that match models up to **30×** larger, and refusal detectors that improve average performance by **43.9%** over existing detectors. Supervised fine-tuning improves overall safety scores. This page records the measurement. It does not adopt the weights. **No install.**

## Snippets

> "Models often fail to respond appropriately to unsafe prompts not because they explicitly refuse, but because they produce linguistically inadequate responses that result in incidental non-assistance rather than proper refusals." [Source: arxiv-2610.26474 abstract]
