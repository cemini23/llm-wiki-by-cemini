---
title: "SAFE-PRO — proactive inquiry for cross-modal safety"
type: source
related:
  - concepts/k293-cybersec-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: When Reasoning Is Not Enough: Proactive Inquiry for Cross-Modal Safety in Multimodal Large Language Models
Authors: Wei Cai, Jian Zhao, Yuchen Yuan, Xuelong Li
Type: arXiv preprint (2610.22068)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2610.22068-when-reasoning-is-not-enough-proactive-inquiry-f.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Two inputs can each be benign and still be unsafe together. The paper names two failure modes. Implicit reasoning risk: a long chain branches into an unsafe trajectory even when the request is fully specified. Intent-level risk: cross-modal ambiguity commits the model to a hazardous premise without saying so.

Path optimisation covers the first. Unimodal "ask a clarifying question" methods miss the second, because they trigger on entropy alone and reward short answers, and because no multimodal multi-turn training set existed for them.

SAFE-PRO has three parts. A risk-conditioned uncertainty signal mixes predictive entropy with a learned cross-modal risk score, trained on contrastive reasoning branches with no extra labels. A two-layer loop interleaves risk-guided path optimisation with a safety-grounded question. The reward puts safety above efficiency and penalises over-refusal. SSUI-Dialog is their cross-modal multi-turn set, with dual safe and unsafe intent labels.

The abstract states a variance bound on the inner-loop gradient when the risk score tracks gradient magnitude. This skim did not extract a headline accuracy. Treat the result as a method claim until a later read. **No PoC.**

## Snippets

> "Multimodal Large Language Models (MLLMs) face a subtle safety vulnerability: cross-modal inputs that are individually benign can elicit unsafe behavior once jointly interpreted." [Source: arxiv-2610.22068 abstract]
