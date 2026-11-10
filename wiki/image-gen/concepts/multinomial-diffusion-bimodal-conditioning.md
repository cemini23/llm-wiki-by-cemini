---
title: Multinomial diffusion with two condition granularities
type: concept
tags: [concept, discrete-diffusion, conditioning, technique, peripheral]
keywords: [multinomial diffusion, categorical diffusion, per-token condition, global property target, discrete data, protein design, solubility, joint training]
related:
  - sources/arxiv-diffsequence-q-protein-diffusion-2611.08434.md
  - concepts/mdlm-padding-termination-decoupling.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: how do you carry a per-token structural condition and one continuous whole-sequence target in the same discrete diffusion model? Synthesized from arXiv:2611.08434 (DiffSequence-Q). Peripheral: the data is amino acids.

## Narrative

**The pattern.** Two conditions of different granularity enter the same denoiser:

| Condition | Granularity | Example in the paper |
|---|---|---|
| Structure | one class per position | secondary-structure label per residue |
| Property | one continuous scalar for the whole sample | solubility |

The claim is that these act at different scales, and one conditional generative model can satisfy both. The denoising head receives per-position features, the diffusion step, and the projected global target, then predicts a categorical distribution over the alphabet.

**Why discretisation matters.** Continuous diffusion assumes the data is well modelled by Gaussian noise. Amino acids are categories. Multinomial diffusion uses uniform category replacement, an analytic posterior, and a neural estimate of the clean distribution. This is the same family as the MDLM and masked-diffusion work already in the wiki (`@concepts/mdlm-padding-termination-decoupling.md`).

**Transfer to image work.** The structural analogy is direct:

| Discrete-model case | Image analogue |
|---|---|
| per-residue structure label | mask, depth map, pose skeleton applied per pixel |
| whole-sequence solubility target | one global style, identity or aesthetic score |
| categorical alphabet prediction | token or index prediction in a discrete image tokenizer |

The image analogue already exists in pieces: composite conditioning adapters and per-pixel ControlNet map the first row, and preference-aligned samplers target a global score. What this paper adds is a demonstration that both can be trained jointly in one objective rather than stacked as separate guidance calls.

**The quantum part is not transferable.** The auxiliary head is a quantum neural network or a quantum Kolmogorov–Arnold network. Its stated benefit is on a predicted property score, and generation stays classical. There is no inference speedup and no sampler change. Do not read the paper's quantum label as an acceleration claim.

**Operator read.** Peripheral, wiki-only. Value is the conditioning pattern and one honest caveat: the joint objective shapes the denoiser through an auxiliary head whose benefit is reported on a predicted property, not on a downstream task metric.

## Snippets

[Source: arxiv-2611.08434 p.1 — "Secondary structure can be specified at individual residues, whereas solubility is a property of the whole sequence."]
