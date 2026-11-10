---
title: Value-cache streaming video editing (inversion-free, one source pass)
type: concept
tags: [concept, video-editing, streaming, autoregressive, training-free, identity-preservation]
keywords: [AR-Edit, V injection, Q/K stability, inversion, DMD distillation, Reward Forcing, CausVid, Self Forcing, commit-then-anchor, streaming latency]
related:
  - sources/arxiv-ar-edit-streaming-video-editing-2611.09795.md
  - concepts/layered-diffusion-content-preserving-video-editing.md
  - concepts/agentic-video-editing-orchestration.md
  - concepts/disentangled-context-memory-video-edits.md
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

The question this page answers: how do you edit a live video stream while keeping subject identity, without training and without inversion? Synthesized from arXiv:2611.09795 (AR-Edit) and the wiki's existing video-editing coverage.

## Narrative

**The structural fact that makes it possible.** In a DMD-distilled autoregressive video model, self-attention splits into two parts that behave differently across noise levels:

| Tensor | Behaviour across denoising timesteps | Role |
|---|---|---|
| Q, K | stable, cosine similarity about 0.68–0.73 to clean source | decides where each token attends |
| V | diverges, cosine similarity about 0.30 | carries what content is retrieved |

The asymmetry is inherited from the non-distilled bidirectional teacher. It is strongest at high noise, which is exactly where a three-to-four-step student lives (its training timesteps are all t ≥ 625).

**The consequence.** Identity is in V. Attention routing is nearly noise-invariant. So one clean forward pass of the source frame, with its V cached, is enough to carry identity into an edit that starts from pure Gaussian noise.

**The recipe.**

1. Cache V from one forward pass of the source frame. Discard the output.
2. Denoise the target frame from Gaussian noise under the target prompt.
3. Inject the cached source V at chosen self-attention blocks during the first S steps.
4. After the commit point, restrict injection to the unedited region with a cross-attention mask ("commit then anchor").
5. Raise the weight of target text tokens to hold edit adherence.

**Why inversion is not needed.** Inversion needs many small steps to recover the noise that regenerates the source. A three-to-four-step student has only large steps, so the inverted latent falls outside the expected Gaussian noise distribution. The paper reports inversion fails in this regime, while V injection reconstructs the source at matching or better fidelity.

**The trade-off is one dial.** Full injection at every block and step favours source adherence and starves text adherence. The paper's defaults (S = SCtA = 2, b_min = 22) sit at the knee of that curve. Injecting into more blocks below b_min = 22 saturates the source gain while the text keeps degrading, so pushing further buys nothing.

**How it compares to the wiki's other editing families.**

| Approach | Needs | Cost per edit | Streaming |
|---|---|---|---|
| `@concepts/layered-diffusion-content-preserving-video-editing.md` | a layered backbone and mattes | offline, many passes | no |
| `@concepts/agentic-video-editing-orchestration.md` | an agent loop and a tool set | high, planning overhead | no |
| `@concepts/disentangled-context-memory-video-edits.md` | RGB/depth memory with invalidation | offline | no |
| This page | a DMD-distilled AR backbone | one source pass plus the native few-step denoise | yes |

**Operator read.** This is the first training-free method in the wiki that edits a stream inside the AR model's own latency budget. For live persona video the useful capability is narrow and real: swap a background object or colour while the face keeps identity. The dependency is strict. It requires a distilled AR backbone, so a bidirectional offline model gains nothing.

**Open questions.**

- Does the Q/K-stability asymmetry hold for non-Wan AR backbones and for students distilled by other objectives? [OPEN QUESTION 2026-11-10]
- How does injection behave under a moving camera, where source V contains stale spatial content? [OPEN QUESTION 2026-11-10]

## Snippets

[Source: arxiv-2611.09795 p.4 — "Q and K remain stable across noise levels while V diverges from the clean anchor. The asymmetry originates in the teacher and is strongest in the high-noise regime where the distilled students operate."]
