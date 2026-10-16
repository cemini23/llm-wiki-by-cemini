---
title: Decomposed graded verifier — replace the pass/fail with a counted fraction
type: concept
tags: [verification, reward-models, image-generation, k292]
keywords: [graded verifier, decomposition, sub-questions, pairwise, pointwise, decoupled RL, reference image, over-decomposition]
related:
  - sources/arxiv-omniverifier-c1-2610.22355-2026-10-16.md
  - concepts/k292-image-gen-wave.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @sources/arxiv-omniverifier-c1-2610.22355-2026-10-16.md — the paper
- @concepts/k292-image-gen-wave.md

## Raw Concept

**The question this page answers:** what should replace a binary True/False judge in an automated pipeline?

Source: OmniVerifier-C1 (arXiv 2610.22355, Tsinghua / Amap), ingested 2026-10-16. Domain is visual generation; the pattern is general.

## Narrative

### The construction

Decompose a prompt or a rule set into **K sub-questions**. Judge each 0/1. Return **`S = (# satisfied) / K`**.

Three properties follow:

1. **Continuous, so it can train.** A fraction is a dense reward where a gate is not.
2. **Inspectable.** You can see *which* sub-question failed, not just that the whole thing failed.
3. **Ordering-preserving.** The paper proves a graded reward ranks quality better than a threshold: `Acc_rank(r_c) = 1 ≥ Acc_rank(r_d)`.

### Pairwise beats pointwise when a reference exists

With a ground-truth example `y*` the error decomposes as `ε_point = ε_reasoning + ε_judge`, but `ε_pair = ε_judge` — comparing against a reference removes the reasoning step entirely. The empirical gap is large and consistent:

| Task | Pointwise | Pairwise |
|---|---|---|
| Maze world-modeling | 67.8 | **85.3** |
| Sudoku world-modeling | 77.7 | **90.0** |

**If a harness can hold a known-good example, compare against it rather than asking a model to score in isolation.**

### Training recipe

**Decoupled RL** on Qwen3-VL-8B, 80 RL steps. From one (prompt, image) pair, build **1+K samples**: one global-score sample rewarded on `1−|Ŝ−S*|`, and K binary per-sub-question samples rewarded on the 0/1 match. Judgment and scoring stay separate reward terms instead of one blended signal — the same decomposition discipline applied to the training objective.

Generator-side results, for scale: GenEval SD3.5-medium 0.66 → **0.77** graded (discrete binary reaches 0.68), FLUX.1-dev 0.68 → **0.79**.

### The failure mode to avoid

The authors warn that **excessive decomposition adds redundant or unsupported sub-questions**. More criteria is not monotonically better: each spurious sub-question inflates K and dilutes the fraction. Decomposition quality is the constraint, not decomposition quantity.

### Where it fits here

The pattern matches three other K292 findings without being the same thing: the VEPA evidence gate decides *when* a deterministic rule may fire; the OpenGCUA `todo` state separates *claimed* from *verified*; DistressBench scores care delivered rather than refusal. All four replace a binary with a counted, inspectable signal. That convergence is the K292 theme.

**Domain caveat:** the paper's own evaluation is limited to game environments with unique ground truth. Generalisation beyond that is untested.

## Snippets

> we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores [Source: arXiv 2610.22355, abstract]

> the transition from generative models to structured world-modeling agents critically hinges on the availability of accurate pairwise graded visual verifiers. [Source: arXiv 2610.22355, abstract]
