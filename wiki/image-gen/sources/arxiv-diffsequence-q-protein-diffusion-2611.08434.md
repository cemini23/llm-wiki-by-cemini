---
title: "DiffSequence-Q — multinomial diffusion with a quantum auxiliary head for protein design (arXiv:2611.08434)"
type: source
tags: [source, arxiv, discrete-diffusion, conditioning, quantum, protein, peripheral]
keywords: [DiffSequence-Q, multinomial diffusion, discrete diffusion, per-residue conditioning, continuous property target, QNN, QKAN, solubility, CATH, peripheral]
related:
  - concepts/multinomial-diffusion-bimodal-conditioning.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | DiffSequence-Q: Diffusion Design with Quantum Assistance for Biologically Active Proteins |
| Author | Ke-Xin Tang et al. (TuringQ, Shanghai Jiao Tong University, Atomology) |
| Type | arXiv:2611.08434 [quant-ph], 29 pages |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.08434-diffsequence-q-diffusion-design-with-quantum-ass.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.08434-diffsequence-q-diffusion-design-with-quantum-ass.pdf` |
| Read status | read (abstract, method, contributions) |

## Narrative

**Peripheral to image generation.** The output is a protein sequence, not an image. The quantum head is a training aid, not a sampler. The page is short because the honest connection is narrow.

**What is genuinely relevant.** The conditioning structure. The model is a multinomial (categorical) diffusion model over amino acids with two conditions at once:

| Condition | Granularity |
|---|---|
| Secondary structure | one label per residue |
| Solubility | one continuous value for the whole sequence |

The paper's argument is that these two constraint types act at different scales, and a conditional generative model can carry both. That is the same shape as image work with a per-pixel condition plus a global property target: a mask or depth map per pixel, and a style or identity score for the whole image.

**The quantum part.** A quantum neural network (QNN) or quantum Kolmogorov–Arnold network (QKAN) serves as an auxiliary solubility prediction head over the shared Transformer representation. Its loss is optimised jointly with the diffusion loss, so the quantum head shapes the denoiser. At generation time the reverse process is fully classical.

**Reported numbers.**

| Claim | Result |
|---|---|
| Secondary-structure recovery on CATH | best of four models; +8.96 points DSSP9, +4.77 points Q3 |
| Predicted solubility vs MLP baseline | QNN +14.0%, QKAN +22.7% |
| Experimental activity | defensins inhibit *Aspergillus niger*; xylanases 1.92–2.21 U/mg; two dehydrogenases 55.25 and 53.10 U/mg |

The scaling trends with quantum-head configuration are non-monotonic, which the authors state plainly.

**Operator read.** wiki-only, no distribution. Do not read the quantum result as an acceleration claim: the sampler is classical, so there is no inference speedup. The transferable content is the two-granularity conditioning pattern, and that is one paragraph, not a method.

## Snippets

> "Secondary structure can be specified at individual residues, whereas solubility is a property of the whole sequence. Moreover, satisfying local structural constraints does not necessarily ensure favorable solubility." [Source: arxiv-2611.08434 p.1]

> "Once trained, protein sequences are generated entirely through classical reverse diffusion." [Source: arxiv-2611.08434 p.1]
