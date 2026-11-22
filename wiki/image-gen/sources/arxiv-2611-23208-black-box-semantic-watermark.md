---
title: "Distortion-free semantic watermarks for black-box models (arXiv:2611.23208)"
type: source
related:
  - concepts/black-box-semantic-watermarking.md
  - concepts/t2i-model-ownership-verification.md
  - concepts/anti-personalization-privacy.md
  - sources/arxiv-2605-29809-cert-las-t2i-mov.md
  - entities/models/flux.md
  - concepts/generative-ai-era-deepfake-landscape.md
updated: 2026-11-22
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Distortion-Free Semantic Watermarks for Black-Box Generative Models |
| Authors | Aviv Yossef, Or Patashnik, Or Zamir (Tel Aviv University) |
| Type | arXiv preprint, cs.LG |
| arXiv | 2611.23208v1, 17 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.23208-distortion-free-semantic-watermarks-for-black-bo.pdf` |
| URL | https://arxiv.org/abs/2611.23208 |
| Code | https://github.com/avivyossef/distortion-free-semantic-watermark |
| Retrieved | 2026-11-22 |
| Pages | 59 |
| Read status | read |
| Domain fit | **On-topic.** Watermarking of generated images, black-box APIs, provenance for persona work. |

## Narrative

### The problem

A watermark should not change output quality. A **distortion-free** watermark leaves the generator's output distribution unchanged when you average over the secret key. DeepMind deployed this idea as SynthID-Text in Gemini, and Anthropic adopted a version for Claude.

Distortion-free is not enough for images. A watermark tied to pixel values dies under JPEG compression, cropping, or resizing. **Semantic watermarking** moves the signal to content. Detection should survive any edit that keeps the meaning of the image.

Prior semantic image methods need white-box access: control of the initial noise, or diffusion inversion. Closed image APIs do not expose these. They also break when the architecture changes.

### The method

The framework treats both the generator and the semantic encoder as black boxes. It needs only two oracles: one that returns samples, one that maps an image to a vector.

1. Sample N candidate images for the prompt (for example N = 32).
2. Hash each image's semantic embedding into an M-bit code.
3. Give every occupied code a pseudorandom score F from a secret key.
4. Select from the code with the best keyed score, weighted by how many candidates share that code (a Gumbel-style rule).
5. Return one candidate uniformly from the winning code.

Averaged over the key, every candidate returns with probability 1/N. The output distribution therefore equals the generator's own distribution. This holds for any generator and any encoder (Theorem 3). A fixed key makes some codes win more often, and this supplies the detection signal.

Detection needs only the encoder and the keyed score. A batch of images is scored together. The authors also add a boundary-aware detector for images near a code boundary.

### Semantic entropy

The encoder must do two opposite things. It must stay stable under content-preserving edits, and it must tell apart independent generations from the same prompt. The paper calls the second quantity **semantic entropy** and proves a lower bound on true-positive rate that grows with it. A standard CLIP or DINO encoder is bad at this: it treats same-prompt generations as similar. The authors train an image encoder for this tradeoff on SDXL images, then test transfer to other generators.

### Results

| Setting | Metric | Value |
|---------|--------|-------|
| N=32, M=12, 1 image | AUROC | 0.920 |
| N=32, M=12, 5 images | AUROC | 0.998 |
| N=32, M=12, 10 images | AUROC | 1.000 |
| OpenAI GPT Image API, 8 candidates, 5 images | AUROC | 0.978 |
| OpenAI GPT Image API, 8 candidates, 1 image | AUROC | 0.815 |

The closed GPT Image API run uses only sampling access. This is the strongest workspace result: you can watermark the output of a closed model you cannot open.

**Quality under fixed-key reuse.** Matched-population FID is 4.75 to 5.22, against a clean-versus-clean reference of 4.64. The three diffusion baselines score 5.42 to 6.88. Same-prompt diversity stays within 1.3% of clean output. Gaussian Shading loses 9.1% of diversity and SEAL loses 13.2%.

**Robustness.** The picture is mixed. The baselines are stronger after compression and appearance changes. The proposed method is stronger after geometric edits and generative edits:

| Edit type | Ours (N=16, M=8) | Tree-Ring | Gaussian Shading | SEAL |
|-----------|------------------|-----------|------------------|------|
| Geometric (detection after edit) | 48.9% | 46.7% | 27.4% | 14.5% |
| 80 generative edits (TPR after) | 70.0% | 60.0% | 37.5% | 10.0% |

### The ceiling

Black-box selection has a hard limit. Single-image true-positive rate cannot exceed N × false-positive rate. A single image therefore cannot carry strong evidence. The method works where many outputs trace to one source: one social profile, one student's submissions, one persona account.

### Workspace relevance

This is directly useful for persona provenance. A persona account publishes many images from one source. Batch detection fits that shape. The framework also works on a closed API, so a competitor's account can be tested without access to their model. The trade is compute: N candidates per published image. At N = 32, generation cost rises 32×.

It is not a defence against a determined adversary who edits content itself. It is attribution, not protection. For an operator, it is the reverse tool: a way to prove your own outputs came from you, or to check whether someone else's did.

## Snippets

> "A watermark is called distortion-free if, averaged over its secret detection key, it leaves the generator's output distribution unchanged." [Source: arxiv-2611.23208 p.1]

> "Selecting among N independent candidates gives single-output detection rates satisfying TPR ≤ N FPR." [Source: arxiv-2611.23208 p.2]

> "We also apply our framework to OpenAI's closed GPT Image API, using only sampling access, and obtain an AUROC of 0.978 for batches of five images with eight candidates per output." [Source: arxiv-2611.23208 p.3]

## Dead Ends

A single linear projection of latents into semantic space is not enough. Standard encoders (DINOv2, CLIP, DINOv3, TPIPS) treat same-prompt generations as similar, so they yield low semantic entropy and weak detection. A trained encoder is required.
