---
title: Outcome-supervised block regeneration — score the partial state, re-denoise the whole block
type: concept
tags: [concept, diffusion, decoding, verifier, inference-time, mdlm]
keywords: [DiVR, outcome supervision, block re-decoding, remasking, verifier head, LoRA adapter, best-of-k, early decision error]
related:
  - sources/arxiv-2611.17320-divr-diffusion-verifier-regeneration.md
  - concepts/mdlm-padding-termination-decoupling.md
  - concepts/decomposed-graded-verifier.md
updated: 2026-11-14
---

## Raw Concept

**The question this page answers:** when a diffusion model has already committed a bad region, what is the correct repair action?

Source: DiVR (arXiv:2611.17320, Seoul National University / KAIST), ingested 2026-11-14. The experiment is masked diffusion language model decoding. The rule is general to iterative generation.

## Narrative

### The failure it fixes

A diffusion model commits tokens or latent positions in an order. Once a position is committed, standard decoding never revisits it. A wrong commitment with high confidence therefore survives, because later positions are predicted from that context and confirm it.

The natural repair — re-sample only the wrong position — fails. The DiVR diagnosis reports that a re-masked wrong cell keeps mean probability 0.869 of the same wrong value. Only 6 of 77 failures were fixed by reopening every wrong cell at once `[TENTATIVE]`.

The reason is context support. The wrong token sits in a context that was itself built on the error. Changing one position leaves the pressure that produced it.

### The rule

Three parts, each independently useful:

1. **Regenerate a region, not an element.** Re-sample a whole block from the same prefix. The block contents then change together, which is what the diagnosis requires.
2. **Score the partial state by predicted outcome, not by confidence.** Train a small verifier head on the generator's own samples, labelled by the final quality of each sample. Correctness labels are cheap: a check on the finished output is enough.
3. **Share the backbone.** A LoRA adapter plus a small MLP head, about 1% of backbone parameters, reads the model's own hidden states. Reshaping the representation with the adapter mattered: a head-only verifier scored 74.2%, the full verifier 78.8% at lower cost.

The decision threshold is a single scalar. A score below it triggers re-generation of the block, subject to a budget.

### Why early blocks dominate

Most repairs land at the start of the trajectory. On the DiVR benchmark suite, 114 of 154 repaired problems departed in the first block. The first block fixes the interpretation of the task. Every later token confirms that interpretation.

Two consequences:
- **Sample fewer alternatives, earlier.** Spend the budget where a fresh route is still possible.
- **Late regeneration is near-useless.** A re-sample of a late block inherits the wrong setup.

### Transfer to image and video diffusion

The mapping is direct, though untested in the wiki:

| DiVR element | Image/video analogue |
|--------------|----------------------|
| Token block | Latent tile, temporal block, or frame block |
| Outcome-supervised score | A quality or instruction-following score on the partial denoise |
| Block re-sample | Re-denoise the tile from the same noisy prefix |
| Best-of-k rerank | Best-of-k on finished samples, scored by the same head |

The wiki already holds verifier work at the finished-output stage. See @concepts/decomposed-graded-verifier.md for the graded-score alternative to a binary judge. This page adds the *when to regenerate* decision, which is the part that costs compute.

### Limits

- The evidence is one paper on text reasoning benchmarks (GSM8K, MATH-500, Countdown, HumanEval, MBPP).
- The verifier must be trained per domain. A math verifier and a code verifier are separate models.
- Per-problem cost is 1.9–3.5× greedy decoding. This is an accuracy lever, not a speed lever.
- No image or video experiment exists yet. Treat the transfer as `[OPEN QUESTION 2026-11-14]`.

## Snippets

> "The criterion for revision should be learned rather than read from token confidence, and the unit of revision should be a region regenerated jointly rather than an isolated token." [Source: arxiv-2611.17320 p.3]

> "A fresh sample of the first block starts from the prompt alone and can take a different route, whereas a fresh sample of a later block inherits the mistaken setup." [Source: arxiv-2611.17320 p.7]
