---
title: "AR-Edit — training-free autoregressive video editing without inversion (arXiv:2611.09795)"
type: source
tags: [source, arxiv, video-editing, streaming, autoregressive, training-free, neurips]
keywords: [AR-Edit, inversion-free, value injection, self-attention asymmetry, DMD distillation, Reward Forcing, CausVid, Self Forcing, Wan 2.1, streaming editing]
related:
  - concepts/value-cache-streaming-video-editing.md
  - concepts/layered-diffusion-content-preserving-video-editing.md
  - concepts/agentic-video-editing-orchestration.md
read_status: read
created: 2026-11-10
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AR-Edit: Training-Free Autoregressive Video Editing without Inversion |
| Author | Hovhannes Margaryan, Quentin Bammey, Christian Sandor, Vicky Kalogeiton (Université Paris-Saclay, Télécom Paris, École Polytechnique) |
| Type | arXiv:2611.09795 [cs.CV], 31 pages; NeurIPS 2026 |
| Location | `research to be indexed/image-gen/arxiv-2611.09795-ar-edit-training-free-autoregressive-video-editi.pdf` |
| Retrieved | 2026-11-10 |
| File | `arxiv-2611.09795-ar-edit-training-free-autoregressive-video-editi.pdf` |
| Read status | read (abstract, method, ablations) |

## Narrative

A streaming video editor that needs no training, no inversion, and one forward pass of the source frame.

**The observation.** In DMD-distilled autoregressive video diffusion models, self-attention behaves asymmetrically over denoising timesteps. Queries and keys stay close to their clean-source values: mean cosine similarity 0.68 and 0.73 across 30 blocks of a Reward Forcing student. Values diverge sharply: mean 0.30. Routing is nearly invariant to the noise level; the content carried by V changes.

The asymmetry comes from the non-distilled bidirectional teacher. It is strongest at high noise, which is exactly where the few-step student operates, because its training timesteps are all at t ≥ 625.

**The method, in three steps.**

1. Run one clean forward pass of the source frame and cache the V features.
2. Denoise the edited frame from pure Gaussian noise under the target prompt.
3. Inject the cached source V during denoising. Target Q and K set the edit semantics; source V preserves identity.

Later denoising steps restrict injection to the unedited region, using a mask derived from cross-attention. Targets also raise the weight of the target text tokens.

The claim that follows: inversion is redundant in this regime. With only three or four large steps, an inverted latent falls outside the expected Gaussian noise distribution, so inversion fails anyway.

**Controls and defaults.** Full V-injection at each step trades text adherence for source adherence. Commit-then-anchor recovers the source at little text cost. Defaults are S = SCtA = 2, b_min = 22, b_cta = 19 — the knee of both trade-offs. Below b_min = 22 the source gain saturates while the text keeps degrading.

**Baselines compared.** SDEdit, FlowEdit, DynaEdit, and an inversion-plus-inversion variant. The paper reports less burning, less tonal drift, and better source appearance. StreamEdit comparisons are in the appendix.

**Why it matters here.** Real-time stream editing is the missing piece for live persona video: an operator can change the setting or an object in a face-cam stream without re-rendering or losing identity. The method adds no parameters and stays inside the AR model's native latency and memory budget.

**Caveats.** Reported results are on Reward Forcing (Wan 2.1 teacher) and a few other AR backbones. The method depends on DMD distillation, so it does not transfer to a bidirectional offline model or to a non-distilled AR model without re-checking the Q/K/V asymmetry. No code release was verified [NEEDS VERIFICATION 2026-11-10].

## Snippets

> "Q and K remain stable across noise levels while V diverges, suggesting that the identity of a video can be captured from the value features of a single forward pass." [Source: arxiv-2611.09795 p.4]

> "Caching V from a single clean forward pass of the source and injecting it during denoising from Gaussian noise reconstructs the source with fidelity meeting or surpassing inversion-based methods, while inversion itself fails under the few-step schedule." [Source: arxiv-2611.09795 p.2]

## Dead Ends

- **Inversion under a few-step schedule.** With three or four steps the reverse process cannot recover the noise that regenerates the source. The paper reports it fails.
- **SDEdit as a streaming baseline.** It cannot preserve the source even for small edits.
