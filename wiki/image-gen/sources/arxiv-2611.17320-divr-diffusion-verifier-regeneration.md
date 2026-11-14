---
title: "DiVR: learning when diffusion language models should regenerate (arXiv:2611.17320)"
type: source
tags: [paper, diffusion-language-model, mdlm, decoding, verifier, inference-time]
keywords: [DiVR, LLaDA-8B, Dream, remasking, block re-decoding, outcome-supervised verifier, LoRA adapter, Sudoku diagnosis, Countdown]
related:
  - concepts/outcome-supervised-block-regeneration.md
  - concepts/mdlm-padding-termination-decoupling.md
  - concepts/decomposed-graded-verifier.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Learning When Diffusion Language Models Should Regenerate |
| Authors | Minhae Oh, Jeonghye Kim, Jinwoo Koo, Yeongoon Kim, Jimin Seo, Minsik Seol, Jungwoo Lee (Seoul National University, KAIST) |
| Type | arXiv preprint, cs.CL |
| arXiv | 2611.17320v1, 12 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.17320-learning-when-diffusion-language-models-should-r.pdf` |
| URL | https://arxiv.org/abs/2611.17320 |
| Code | https://github.com/minhaeoh/DiVR |
| Retrieved | 2026-11-14 |
| Pages | 22 |
| Read status | read |
| Domain fit | **Adjacent, not image generation.** Masked diffusion language model (MDLM) decoding for text reasoning. |

## Narrative

### The problem

Masked diffusion language models generate text by filling masked positions on a fixed canvas. Standard decoding never revisits a committed token. A wrong token placed early with high confidence therefore stays. Remasking samplers and search methods add revision, but they decide what to revise by schedule, confidence, or likelihood. None of them is trained to predict whether the final answer is correct.

### Two diagnostic findings (Sudoku, LLaDA-8B)

**Finding 1 — hidden states expose errors better than confidence.** A linear probe on answer-position hidden states separates wrong cells from correct cells with AUROC 0.838, against 0.685 for confidence. The separation is already present at the first forward pass that fills a cell (0.866 vs 0.732) `[TENTATIVE]` — single paper, one task.

**Finding 2 — locating an error does not repair it.** Re-mask one committed wrong cell and keep the rest of the canvas. The original wrong digit keeps mean probability 0.869, rising to 0.962 when the re-mask happens sixteen steps later. On 77 failed puzzles, a gold oracle that reopens every wrong answer cell repairs only 6. Reopening the following reasoning as well raises this to 13, and 15 with the best per-puzzle depth.

### Method

**DiVR** (Diffusion Verifier for Regeneration) is an outcome-supervised verifier. It shares the generator's backbone weights. A small MLP head plus a low-rank adapter (about 1% of backbone parameters) map a masked-suffix canvas to a correctness score.

Training labels are the final correctness of the generator's own sampled trajectories. This needs an answer check only, not gold reasoning steps or token-level labels.

At inference, DiVR scores the canvas after each 32-token block. A score below 0.5 triggers a whole-block re-sample of 4 alternatives from the same prefix. The best-scoring alternative replaces the original. Three regenerations per problem is the cap.

### Results

| Setting | Greedy | + DiVR-guided | Cost |
|---------|--------|---------------|------|
| LLaDA-8B-Base + SFT, 5-benchmark avg | 35.3 | 43.4 | 1.9–3.5× |
| LLaDA-8B-Instruct, 5-benchmark avg | 39.4 | 44.8 | 1.6–2.7× |
| Dream-v0-Instruct-7B, 5-benchmark avg | 45.0 | 54.8 | 1.7–2.9× |

The two search baselines reach 39.1% at 3.8–4.0× (SR-SMC) and 37.3% at 5.2–7.4× (Prism) on the SFT generator. DiVR is more accurate at lower cost `[TENTATIVE]`.

**Most repairs start in the first block.** On GSM8K, 114 of 154 repaired problems depart at block 0. On Countdown, 58 of 59 do. The first block fixes the problem interpretation, and later tokens confirm that interpretation.

**Ablation.** With the same block re-decoding procedure, commit confidence scores 72.2%, a prompted Yes/No self-judgment scores 67.9%, a head-only verifier scores 74.2%, and full DiVR scores 78.8% at the lowest cost. The gain comes from the learned criterion, not from extra sampling.

### Workspace relevance

This paper is **not** an image-generation result. It is logged because the design rule transfers to image and video diffusion:

1. **Do not repair an isolated latent element.** Re-denoise a region and let the region's contents change together.
2. **Judge a partial state by its predicted outcome, not by confidence.** Train a cheap head on the generator's own samples and their final quality.
3. **Concentrate compute where the early decision was made.** Errors are cheap to fix near the start of the trajectory and expensive near the end.

See @concepts/outcome-supervised-block-regeneration.md.

## Snippets

> "Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed." [Source: arxiv-2611.17320 p.1]

> "Re-predicting exactly the wrong cells fixes only 6 of 77 failures because the retained context keeps supporting the mistake." [Source: arxiv-2611.17320 p.2]

> "The first block fixes the interpretation of the problem … and later tokens are predicted from that context and tend to confirm it." [Source: arxiv-2611.17320 p.7]

## Dead Ends

No image-model experiment. The paper reports text reasoning benchmarks only. Cost figures rule out casual local use on 8B generators for a persona pipeline.
