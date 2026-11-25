---
title: "One Take, Many Cameras: audio-grounded dialogue re-cinematography (arXiv:2611.33147)"
type: source
tags: [paper, video-generation, audio-visual, multi-shot, cinematic, lora, ltx, lipsync]
keywords: [One Take Many Cameras, dialogue re-cinematography, audio-grounded shot synthesis, speaker-aware audio gating, speech leakage, LTX-2.3, LoRA, in-context conditioning, over-the-shoulder, medium close-up, paired-view benchmark, Wan 3.0]
related:
  - concepts/audio-grounded-dialogue-recinematography.md
  - concepts/multi-shot-audio-video-evaluation.md
  - concepts/camera-controlled-video-generation.md
  - concepts/sync-audio-video-customization.md
  - concepts/seam-stitching-strategies.md
  - entities/models/ltx-2.md
updated: 2026-11-25
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | One Take, Many Cameras: Audio-Grounded Shot Synthesis for Dialogue Re-Cinematography |
| Authors | Anthony Chen (Stanford, LTX), Naomi Ken Korem, Matan Ben-Yosef, Tavi Halperin, Urska Jelercic, Ofir Bibi (LTX), Daniel Cohen-Or, Or Patashnik (Tel Aviv University), Maneesh Agrawala (Stanford) |
| Type | arXiv preprint, cs.CV (film and graphics framing) |
| arXiv | 2611.33147v1, 24 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.33147-one-take-many-cameras-audio-grounded-shot-synthe.pdf` |
| URL | https://arxiv.org/abs/2611.33147 |
| Project page | https://recinematography.github.io/ |
| Retrieved | 2026-11-25 |
| Pages | 15 |
| Read status | read |
| Domain fit | **On-topic.** Audio-visual diffusion, LoRA post-training on LTX-2.3, multi-shot cinematics, and lipsync accuracy. Production relevance for dialogue coverage without a multi-camera shoot. |

## Narrative

### Problem

A dialogue scene needs coverage: wide master, close-ups, over-the-shoulder, and reaction shots. Multi-camera capture is expensive and often unavailable to small productions.

A crop from the wide shot cannot create a new camera angle. An over-the-shoulder shot is impossible when the source shows the actors in profile. Existing video generators can move the camera, but they see only pixels. When the source barely shows the lips, the generated lip motion does not match the speech.

### Key observation

**Speech is view-invariant.** The audio constrains lip motion in every view. An actor closes the lips on /m/ whether the camera sees the face or the back of the head. Audio therefore supplies what the pixels lack.

### Pipeline

1. **Target frame.** An image editor, GPT-Image 2 in practice, renders the first frame of the new shot from the source first frame plus a cinematic prompt ("a medium close-up of the woman, at eye level").
2. **Visual conditioning.** The target frame becomes the clean first-frame latent. The source video is encoded to clean tokens and concatenated with the target sequence. LTX-2.3 gives each token its own timestep, so conditioning tokens sit at timestep 0 and every noisy target token attends to clean source tokens.
3. **Audio conditioning.** The speech is encoded by the audio VAE and held clean at timestep 0. Only the video stream is generated. The original audio is reused, so the new shot cuts against the same track with no post-processing.
4. **LoRA training.** LoRA adapters on the video stream, trained with a flow-matching objective on the target video tokens only. Training pairs are two synchronized views of one scene, cropped to different shot sizes and types, from CMU Panoptic, PKU-DyMVHumans, SynCamVideo, MEAD, Replay, and DnD Group Gesture.
5. **Speaker-aware audio gating (training-free).** Audio-to-video cross-attention updates every face with the same audio, so silent listeners mouth the speaker's words. LightASD detects who speaks in the source; the labels map to the target view through attention. The gate is built in the first steps, where coarse appearance is set, and applied in later steps, where lip motion forms `[TENTATIVE]` — single paper.

### Results — paired-view benchmark

100 cross-camera Replay pairs plus 196 pairs from real productions. Source is wide; target is cropped to cinematic framings.

| Method | LPIPS ↓ | Landmark dist. ↓ | Leakage % ↓ | Sync-C ↑ | PCK % ↑ | Source copy % ↓ |
|--------|---------|------------------|-------------|----------|---------|-----------------|
| MiniMax H3 | 0.290 | 0.174 | 47.3 | 5.29 | 29.3 | 26.4 |
| Wan 3.0 | 0.235 | 0.142 | 17.5 | 5.07 | 41.8 | 6.8 |
| Ours | 0.097 | 0.062 | 0.6 | 5.47 | 53.4 | 0.0 |

The abstract states a 59% drop in perceptual error, a 56% drop in landmark error, and a 97% drop in speech leakage against Wan 3.0. "Source copy" is the share of clips that look more like the source view than the target view; the method reaches zero.

### Results — in-the-wild and ablation

On 98 edited dialogue videos from the internet: speaker-attribution mAP 90.3 against 78.1 for Wan 3.0, leakage 11.9% against 27.5%. A user study prefers the method in 74.7% of overall judgments.

Removing the audio at inference drops Sync-C from 5.01 to 3.70 on paired-view and from 5.68 to 3.35 in the wild. The audio is the load-bearing input, not a decoration.

### Workspace relevance

This is the clearest published recipe for **one performance, many framings**. For persona operations it applies when a single wide take must yield close-ups and reaction shots without a re-shoot. The LoRA is small and the conditioning path is training-free at inference, so the cost is one generation per requested shot.

Two limits matter. The target frame comes from a closed image editor in the reported setup, so a local reproduction needs a substitute. The base model and training data also sit in the LTX family, which narrows portability.

## Snippets

> "Our key observation is that the speech audio is view-invariant: it constrains lip motion in any target view." [Source: arxiv-2611.33147 p.1]

> "In multi-person scenes, however, pretrained audio-visual models drive every visible face with the same speech, causing speech leakage, where silent listeners mouth the speaker's words." [Source: arxiv-2611.33147 p.1]

> "Our method lowers perceptual error by 59%, landmark error by 56%, and speech leakage by 97% relative to the strongest baseline, Wan 3.0." [Source: arxiv-2611.33147 p.1]

## Dead Ends

Seedance and Gemini Omni reject the model's inputs under their content policies, so the authors drop them as baselines. A local reproduction must accept that a closed API may refuse this task class. No code release is stated in the main text `[NEEDS VERIFICATION 2026-11-25]`.
