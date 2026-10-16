---
title: "OmniVerifier-C1 — decomposed graded verifiers for rule-governed visual generation (arXiv 2610.22355)"
type: source
tags: [image-generation, verification, reward-models, source, k292]
keywords: [OmniVerifier, graded verifier, decomposed rubric, decoupled RL, DAPO, ViVerBench, GenEval, world modeling, pairwise]
related:
  - concepts/decomposed-graded-verifier.md
  - concepts/k292-image-gen-wave.md
maturity: draft
read_status: read
created: 2026-10-16
updated: 2026-10-16
---

## Relations

- @concepts/decomposed-graded-verifier.md — the pattern this paper establishes
- @concepts/k292-image-gen-wave.md — K292 image-gen wave hub

## Raw Concept

Title: OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling
Authors: Bowei Liu, Xinchen Zhang, Xuhuan Li et al. (Tsinghua University; Amap, Alibaba Group; Microcyto; Peking University)
Type: arXiv 2610.22355v1 [cs.CL], 32 pages, 15 Oct 2026
Location: `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2610.22355-omniverifier-c1-decomposed-graded-verifier-for-r.pdf`
Retrieved: 2026-10-16
Artifacts: code `github.com/Cominclip/OmniVerifier` (code only; no weights, no dataset link)
Read status: read

## Narrative

**A vision-generation reward model, not a coding-agent tool.** Filed here because the domain is image generation; the one idea that travels is the grading pattern, noted at the end.

**The construction.** Conventional visual verifiers answer True/False. This one **decomposes** a prompt or an environment rule set into **K sub-questions**, judges each 0/1, and returns a **continuous score `S = (# satisfied) / K`**. Two claims are attached:

- **Graded beats binary.** A fractional score preserves the true ordering of quality better than a threshold — the paper proves `Acc_rank(r_c) = 1 ≥ Acc_rank(r_d)`.
- **Pairwise beats pointwise when ground truth exists.** With a reference image `y*`, the error decomposes as `ε_point = ε_reasoning + ε_judge` but `ε_pair = ε_judge`, because the reasoning step disappears.

**Training.** **Decoupled RL** on **Qwen3-VL-8B**, 80 RL steps on 16× A800-80G. From one (prompt, image) pair it builds **1+K samples**: one global-score sample rewarded on `1−|Ŝ−S*|`, and K binary per-sub-question samples rewarded on the 0/1 match. Judgment and scoring are optimised as separate reward terms rather than one blended signal. Generator training is separate: 200 steps, DiffusionNFT, same hardware.

**Results.**

| Setting | Base | After RL |
|---|---|---|
| ViVerBench overall | 0.654 | **0.684** (graded); binary RL reaches 0.671 |
| GenEval, SD3.5-medium | 0.66 | **0.77** graded (UnifiedReward 0.73, discrete binary 0.68) |
| GenEval, FLUX.1-dev | 0.68 | **0.79** |
| CLIPScore, SD3.5 | 32.8 | **34.4** |
| Maze world-modeling | 17.3 | **85.3** pairwise (pointwise 67.8) |
| Sudoku world-modeling | 22.2 | **90.0** pairwise (pointwise 77.7) |
| RISEBench overall | 6.7 | **15.0** pairwise |

The world-modeling jumps are the largest, and the **pairwise-versus-pointwise gap is visible in every one** — Maze 67.8 → 85.3, Sudoku 77.7 → 90.0. Where a ground-truth image exists, comparing against it beats scoring the image alone.

**Limitations (the authors' own).** *"Our world-modeling evaluation is restricted to game-based environments with explicit rules, where the ground-truth image is uniquely determined"* — so it captures a fraction of real-world complexity. They also note that **excessive decomposition can add redundant or unsupported sub-questions.**

### Why it matters here

1. **The grader pattern transfers beyond vision.** Decomposing a pass/fail rubric into sub-criteria and returning a fraction is exactly what a harness-side judge should do, and it is the same shape as the K290 VEPA evidence gate and the OpenGCUA `todo` state: replace a binary with a counted, inspectable signal.
2. **Pairwise over pointwise when a reference exists.** If a harness can hold a known-good example, compare against it rather than asking a model to score in isolation.
3. **The decomposition warning is real.** More sub-questions is not monotonically better — redundant criteria inflate K and dilute the score.

**Code only, no weights. No install. No trade.**

## Snippets

> we move beyond conventional binary verifiers that produce only True/False discrete judgments and introduce a verifier that automatically decomposes complex prompts or environmental rules into fine-grained components and assigns pointwise scores to provide a continuous and more informative critique signal. [Source: arXiv 2610.22355, abstract]

> the transition from generative models to structured world-modeling agents critically hinges on the availability of accurate pairwise graded visual verifiers. [Source: arXiv 2610.22355, abstract]
