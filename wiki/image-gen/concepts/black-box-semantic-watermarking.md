---
title: Black-box semantic watermarking (distortion-free selection)
type: concept
related:
  - sources/arxiv-2611-23208-black-box-semantic-watermark.md
  - concepts/t2i-model-ownership-verification.md
  - concepts/anti-personalization-privacy.md
  - concepts/generative-ai-era-deepfake-landscape.md
  - sources/arxiv-2605-29809-cert-las-t2i-mov.md
  - entities/models/flux.md
updated: 2026-11-22
maturity: draft
---

## Raw Concept

Question this page answers: how do you mark the output of a model you cannot open, without degrading quality, and so that the mark survives edits?

From arXiv 2611.23208 (Tel Aviv University).

## Narrative

### Two properties

**Distortion-free.** Averaged over the secret key, the watermark leaves the generator's output distribution unchanged. No benchmark can show quality loss. DeepMind shipped this as SynthID-Text in Gemini; Anthropic adopted a version.

**Semantic.** Detection must survive edits that keep the meaning: compression, cropping, resizing, generative edits. A pixel-bound mark dies under these.

### Why the prior work does not generalise

Earlier semantic image watermarks need white-box access. They control the initial noise, or they need diffusion inversion for detection. Closed image APIs expose neither. They also break when the architecture changes.

### The construction

Treat the generator and the semantic encoder as oracles. The generator returns samples. The encoder maps an image to a vector.

1. Draw N candidates for the prompt.
2. Hash each embedding to an M-bit code with a fixed random hyperplane set.
3. Score each occupied code with a secret-keyed pseudorandom function.
4. Pick the code with the best score per member (Gumbel selection: maximise log F(code)/n_code).
5. Return a uniformly random candidate from the winning code.

Because the winning code is chosen with probability proportional to its member count, every candidate is returned with probability 1/N after averaging over the key. This gives distortion-freeness for **any** generator and **any** encoder (Theorem 3). A fixed key makes some codes win often, and that is the detectable signal.

Detection reads the encoder and the keyed score, and averages over a batch of images.

### The detector's fuel: semantic entropy

The encoder must be stable under content-preserving edits **and** separate independent generations from the same prompt. Standard encoders (CLIP, DINO) collapse same-prompt generations together, so they carry little signal. The paper defines **semantic entropy** as the negative log probability that two independent generations are within a semantic radius. Detection true-positive rate rises with semantic entropy (Theorem 4). The authors train an encoder for the tradeoff.

### The hard ceiling

Black-box selection has an information limit: single-image TPR ≤ N × FPR. One image cannot carry strong evidence. The method works where many images come from one source:

- One social-media profile.
- One student's submissions.
- One persona account.

Batch detection drives both error rates down exponentially with batch size.

### Measured performance

| Setting | AUROC |
|---------|-------|
| 1 image, N=32 | 0.920 |
| 10 images, N=32 | 1.000 |
| 5 images, OpenAI GPT Image API, N=8 | 0.978 |
| 1 image, OpenAI GPT Image API, N=8 | 0.815 |

Quality under a fixed key: matched-population FID 4.75–5.22 against a clean reference of 4.64, and same-prompt diversity within 1.3% of clean. Both beat the pixel-based baselines (Tree-Ring, Gaussian Shading, SEAL) on FID and diversity.

Robustness is mixed. The baselines are stronger after compression and appearance edits. This method is stronger after geometric edits (48.9% after edit, against 46.7% for Tree-Ring) and after 80 generative edits (70.0% against 60.0%).

### Use for persona provenance

Two directions.

**Prove your own output.** A persona account publishes many images. Batch detection fits. Cost is N× generation per published image.

**Check another account.** The method needs only sampling access, so a closed model's output can be tested without the model.

It is attribution, not protection. An adversary who changes the content itself removes the mark. For a persona operator it answers "did this come from that model", not "stop them copying".

## Snippets

> "Our algorithm samples several candidate outputs, maps them to semantic codes depending on their semantic embeddings, and selects one using a secret keyed function." [Source: arxiv-2611.23208 p.2]

> "Selecting among N independent candidates gives single-output detection rates satisfying TPR ≤ N FPR." [Source: arxiv-2611.23208 p.2]
