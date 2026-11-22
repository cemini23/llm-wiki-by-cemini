---
title: "Refusal and abstention direction geometry — what the steering vector actually encodes"
type: concept
maturity: draft
related:
  - sources/arxiv-refusal-register-causally-steerable-2611.20405.md
  - sources/arxiv-abstention-direction-llm-2611.20441.md
  - sources/arxiv-scientific-misconduct-recognition-refusal-2611.25492.md
  - concepts/recognition-refusal-gap.md
  - concepts/low-asr-is-not-refusal.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/head-attribution-non-identifiability.md
  - concepts/machine-unlearning-privileged-context.md
  - concepts/refusal-induction-as-defense.md
updated: 2026-11-22
---

## Raw Concept

What this page answers: when a lab ablates or steers a "refusal direction", what does that vector actually control? Two November 2026 papers decompose it.

## Narrative

The early picture was one residual-stream direction that mediates refusal. Ablation bypasses safety training, and steering toward the direction induces refusal. Two papers show that the picture is more complex in two independent ways.

**Register, not only decision.** Khindkar and Povarova study Gemma-2-9B-IT at layer 20. Two SVM directions, B1 (harmful vs neutral) and B2 (self-reference vs neutral), sit about 75 degrees apart. B1 aligns with the Arditi-style difference-of-means vector at cosine 0.68. Injecting the harmful-vs-neutral vector into self-reference prompts keeps the refusal, but changes how the model refuses. Content-safety vocabulary moves 2.55 to 10.37 per 100 tokens at alpha 2.0; a random control gives 1.13 to 2.16. B1 carries both category detection and refusal vocabulary. B2 carries mostly category detection. The asymmetry holds across ablation, sufficiency, and injection.

**Cause, not only harm.** Itai, Hirako, and Yamagiwa build abstention directions for three causes: ambiguous query (Q), missing knowledge (MK), and misaligned human values (HV). Steering any one direction moves abstention in the other two, and the cosine similarities confirm a shared component. So refusal is one output of a shared abstention mechanism.

**Consequence for a lab.** Three rules follow.

1. An ablation result is not a clean "safety off" switch. It may move register, cause, or both.
2. Measure the decision and the wording. A model that still refuses but in content-style wording has changed behaviour.
3. Cross-cause steering means a test that suppresses knowledge abstention can also lower value refusal. Report the cause you tested.

The abliterated-model comparison from tl;dr sec #354 fits here. It found 26% fewer source findings and no exploit-development gain. A lab that treats a refusal vector as a capability lever should not expect an exploit gain from it.

[Source: arxiv-2611.20405-refusal-register-is-causally-steerable-decomposi.pdf, arxiv-2611.20441-abstention-direction-in-large-language-models-me.pdf]

## Snippets

> "Cosine similarity between the directions confirms a shared directional component."
[Source: arXiv:2611.20441v1]

## Dead Ends

- A single direction is not a unitary switch. Wollschlager et al. (2025) already found multi-dimensional concept cones, and orthogonality does not imply independence under intervention. [Source: arxiv-2611.20405 §1]
