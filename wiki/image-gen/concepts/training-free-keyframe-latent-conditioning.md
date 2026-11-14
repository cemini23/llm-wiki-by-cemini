---
title: Training-free keyframe conditioning at interior latent blocks
type: concept
tags: [concept, video-generation, keyframes, conditioning, training-free, wan]
keywords: [first-frame conditioning channel, mid-grey padding, conditioning mask, temporal block, latent block end, Wan2.2 VAE, keyframe interpolation]
related:
  - sources/arxiv-2611.17324-k2v-generative-keyframing.md
  - concepts/vlm-guided-physical-video-generation.md
  - entities/models/wan-2-2.md
  - concepts/physics-aware-orthogonal-view-video.md
  - concepts/video-generation-physical-executability.md
  - concepts/world-models-video-generation.md
updated: 2026-11-14
---

## Raw Concept

**The question this page answers:** how do you pin a frame at an arbitrary interior timestamp of a video model that only accepts a first frame?

Source: K2V (arXiv:2611.17324, Cambridge / Toyota Motor Europe), ingested 2026-11-14.

## Narrative

### The mechanism

Wan2.2 takes one conditioning image plus a caption. Under the hood it builds a padded image tensor of `N + 1` frames. Frame 0 is the real image. Frames 1..N are mid-grey, which the VAE maps to zero after normalization to `[-1, 1]`. The VAE then compresses to `N/L_T + 1` latent frames, where `L_T` is the temporal compression factor. A mask vector marks which slots are filled. Conditioning is concatenated with the noise tensor at every denoising step.

To add a keyframe, replace the grey frame at the target slot with the keyframe and set the mask at that slot.

```
I'[n] = I        if n = 0
        K_i      if n = a_i          (a keyframe timestamp slot)
        0.5      otherwise
```

The slot index is the nearest frame that falls at the **end of one latent timestep**:

```
a_i = L_T * floor(f * t_i / L_T)      a_i in {L_T, 2L_T, ..., N}
```

With the Wan2.2 VAE, `L_T = 4`, frame rate `f = 16`, and clip length `N = 80`.

### The two constraints

1. **Place keyframes at latent block ends only.** Intermediate positions inside a block do not condition correctly. The authors hypothesize that a frame at the end of a temporal block looks most like the initial conditioning frame the network was trained on.
2. **Update the mask.** An unmarked keyframe slot is treated as empty.

Both constraints follow from the same fact: the model was trained to treat frame 0 as a special one-frame latent block. The trick reuses that behaviour at interior positions.

### Why it works without training

Wan2.2 pre-training explicitly included frame interpolation as a task. Keyframe conditioning is therefore a *surviving* behaviour, not a learned adaptation. The authors report it works with default weights, no fine-tuning.

### Consequence for an operator

This is the cheapest way in the wiki to get multi-anchor control of an open-weight video model:

- No new weights.
- No adapter training.
- Works on Wan2.2 I2V-A14B and TI2V-5B.

Two practical cautions:
- **Repeat keyframes.** Two identical keyframes far apart in time make the model invent motion between them. Insert intermediate keyframes every second, and hold the last frame still once the scene comes to rest.
- **Colour drift.** An image edit model introduces small colour shifts. Apply an affine colour match to the input image before conditioning, and to the first frame after generation.

### Relationship to the rest of the wiki

This page covers the *transport* mechanism only. The *source* of the keyframes — a VLM planner, a simulator, or an artist — is separate. See @concepts/vlm-guided-physical-video-generation.md for language-model planning, and @concepts/physics-aware-orthogonal-view-video.md for a multi-view physics approach that uses an explicit training stage instead.

## Snippets

> "It is trivially possible to condition Wan2.2 for multiple frames at several points in a given video." [Source: arxiv-2611.17324 p.4]

> "This approach works with no training or fine tuning of Wan2.2, and works with the default weights. This appears to be a surviving behaviour … from its pre-training." [Source: arxiv-2611.17324 p.5]
