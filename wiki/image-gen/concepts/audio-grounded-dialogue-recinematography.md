---
title: Audio-grounded dialogue re-cinematography
type: concept
tags: [concept, video-generation, audio-visual, multi-shot, cinematic, lipsync, lora]
keywords: [re-cinematography, dialogue coverage, view-invariant audio, speaker-aware audio gating, speech leakage, in-context conditioning, LTX-2.3, LoRA, over-the-shoulder shot, medium close-up, shot synthesis]
related:
  - sources/arxiv-2611-33147-one-take-many-cameras-recinematography.md
  - concepts/multi-shot-audio-video-evaluation.md
  - concepts/camera-controlled-video-generation.md
  - concepts/sync-audio-video-customization.md
  - concepts/seam-stitching-strategies.md
  - entities/models/ltx-2.md
maturity: draft
created: 2026-11-25
updated: 2026-11-25
---

## Raw Concept

The question this page answers: how do you turn one wide dialogue take into a set of cuttable cinematic shots, with lip motion that still matches the speech? Synthesized from @sources/arxiv-2611-33147-one-take-many-cameras-recinematography.md.

## Narrative

### The production gap

Cinema builds a dialogue scene from coverage: a wide master, medium close-ups, over-the-shoulder shots, and reaction shots. The editor cuts between them. Capture needs several cameras on one take, or repeated takes. Small productions and interviews often have neither.

A crop window cannot fix this. A crop enlarges pixels; it never moves the camera. Profile footage cannot become an over-the-shoulder shot.

### Why pixels alone fail

Camera-controllable generators synthesize content the source never showed. They still infer lip motion from pixels. When the source is a wide shot where the lips are a few pixels wide, they invent motion that does not match the words. Viewers notice the mismatch at once.

### The anchor: audio

Speech constrains lip motion in every viewpoint. That makes the audio a view-invariant conditioning signal. The model keeps the source video for performance and body motion, and uses the audio for articulation.

### The recipe (LTX-2.3 adaptation)

1. Render a target first frame from the source frame plus a shot prompt. This fixes framing and angle.
2. Concatenate clean source-video tokens with the target sequence. Per-token timesteps keep conditioning tokens at t=0.
3. Hold audio tokens clean at t=0. Generate only the video stream.
4. Post-train a LoRA on the video stream with flow matching, on paired synchronized views.
5. At inference, gate audio-to-video cross-attention per speaker.

### Speaker-aware gating

Audio-to-video cross-attention has no notion of who speaks. Every visible face receives the same audio, so silent listeners mouth the speaker's words. Detect the speaking face in the source (LightASD), map the label to the target view through the model's own attention, and suppress audio-to-video updates on non-speakers. Build the gate in early steps, where appearance forms, and apply it in later steps, where lip motion forms.

The gate is training-free. It cut speech leakage from 17.5% to 0.6% on the paired-view benchmark.

### Evidence

- Against Wan 3.0: perceptual error down 59%, landmark error down 56%, leakage down 97%.
- No generated clip is mistaken for the source view (0.0% source copy, against 6.8% for Wan 3.0).
- Removing the audio at inference drops Sync-C from 5.01 to 3.70. The audio is the mechanism.
- In-the-wild user study: 74.7% overall preference.

### Relation to the rest of the wiki

This is the shot-synthesis counterpart to score-level work. @concepts/multi-shot-audio-video-evaluation.md measures whether a multi-shot scene holds together; this page describes how to make the extra shots. @concepts/camera-controlled-video-generation.md covers explicit 6-DoF camera control; here the camera is implied by a single target frame. @concepts/seam-stitching-strategies.md covers the cut or blend between shots.

### Limits for persona operations

The reported target frames come from GPT-Image 2, a closed model. A local pipeline needs a local editor and a re-test. Training used research multi-view datasets with conversation and full-body motion; a single-character persona take is easier in some ways and lacks listener reactions. A closed-API baseline declined the task on content policy, so a hosted path may fail at the door.

[OPEN QUESTION 2026-11-25] No local reproduction has been attempted. The open question is whether a ComfyUI LTX-2.3 LoRA path exists that accepts a source video, a target frame, and an audio track at once.

## Snippets

> "Speech is tightly coupled to lip motion and is shared among all possible viewpoints." [Source: arxiv-2611.33147 p.2]

> "The gate is built in the first s_g steps and applied in the remaining steps, where lip motion is mainly shaped." [Source: arxiv-2611.33147 p.6]
