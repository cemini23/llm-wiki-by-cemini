---
title: "SpecCloak — Probing Harmful Code Generation through Engineering Specifications"
type: source
tags: [arxiv, red-team, code-generation, refusal, defense]
keywords: [PseudoSpec, engineering specification, refusal bypass, RedCode-Gen, SpecReveal, harmful code]
related:
  - concepts/k291-cybersec-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-cybersec-wave.md — K291 cybersecurity wave hub

## Raw Concept

Title: SpecCloak — Probing Harmful Code Generation through Engineering Specifications
Authors: Wenbin Chen, Jiexin Wang, Guanting Wu, Jiaxi Liang, Yi Cai
Type: arXiv preprint (2610.17907)
Location: `research to be indexed/cybersec/arxiv-2610.17907-speccloak-probing-harmful-code-generation-throug.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The finding:** refusal in code generation **does not track the request's keywords**. Across five open-weight models, removing explicit risk keywords only *partially* reduces refusal — but **restating the same requirements as an engineering specification lowers refusal substantially, even when the risk keywords are kept**.

**PseudoSpec** is the template that organises functional requirements as an engineering specification. The effect is accompanied by consistent shifts toward code-output representations, and **activation interventions along condition-difference directions alter refusal behaviour** — so the shift is not merely surface phrasing.

**SpecCloak** pairs PseudoSpec with discriminator-guided optimisation: **28.91% average execution-verified attack success** across eight target models on RedCode-Gen.

**SpecReveal** is the defence prototype — natural-language **intent reconstruction** plus **dual-view detection**, needing no target-model fine-tuning: **96.88%** attack detection in a separate prompt-detection evaluation, with false positives assessed on benign programming and specification-style inputs.

**Why it is filed here:** it belongs with the wiki's existing finding that an eval which measures the wrong artefact is unsound. **Keyword-based refusal filtering measures phrasing, not intent.** The defence works by reconstructing intent, not by matching banned tokens.

## Snippets

> "removing explicit risk keywords only partially reduces refusal, whereas specification prompting substantially lowers refusal even when these keywords are retained." [Source: arxiv-2610.17907 p.1]

> "SpecCloak ... achieving an average execution-verified attack success rate of 28.91% across eight target models on RedCode-Gen." [Source: arxiv-2610.17907 p.1]

> "SpecReveal ... achieves a 96.88% attack detection rate in a separate prompt-detection evaluation." [Source: arxiv-2610.17907 p.1]

## Dead Ends

- Treating keyword filters as a refusal boundary. The same request restated as a specification moves refusal while the keywords stay in place.
