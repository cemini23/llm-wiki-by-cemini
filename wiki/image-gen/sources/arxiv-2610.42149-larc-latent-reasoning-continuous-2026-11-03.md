---
title: "LARC — latent reasoning in continuous space for unified multimodal models"
type: source
tags: [source, arxiv, multimodal, reasoning, diffusion, text-to-image]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Latent Reasoning in Continuous Space for Unified Multimodal Models |
| Authors | Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin (KAIST, POSTECH, RLWRLD) |
| arXiv | 2610.42149 |
| Pages | 22 |
| Read status | skimmed (abstract) |

## Narrative

Unified multimodal models handle understanding and generation together, but **language-based chain-of-thought does not transfer to image generation**. Reasoning happens in discrete token space while generation happens in continuous space, and the mismatch is why reasoning-augmented models fail to inherit the test-time scaling seen in LLMs.

LARC reasons over **continuous hidden states** instead of tokens. Two training stages:

1. **Curriculum supervised fine-tuning** — gradually converts token-level reasoning into latent reasoning.
2. **Information-gain reinforcement learning** — self-evolves the latent reasoning **without ground-truth supervision**.

Results across text-to-image benchmarks: improved generation quality, prompt following, and compositional fidelity, with a state-of-the-art claim in the abstract.

### The idea

The paper's framing — a **modality mismatch between the reasoning space and the generation space** — is the useful part. It explains why "just add chain-of-thought" does not improve image models: the reasoning is being done in a different substrate than the output.

The curriculum is the mechanism for moving reasoning into that substrate rather than translating across it each time.

**Caveat.** Abstract only. No benchmark numbers reproduced.

## Snippets

> "We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space, whereas image generation operates in a continuous space." [Source: arxiv-2610.42149 p.1]

## Dead Ends

- **Citing the state-of-the-art claim.** Abstract only; no benchmark figures here.
