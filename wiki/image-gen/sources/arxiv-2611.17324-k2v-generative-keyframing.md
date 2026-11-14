---
title: "K2V: generative keyframing for physically plausible video (arXiv:2611.17324)"
type: source
tags: [paper, video-generation, physics, keyframes, training-free, vlm, agentic]
keywords: [K2V, keyframes to video, Wan2.2, Gemini 3.8 Flash, Physics-IQ Verified, PhyGenBench, first-frame conditioning, keyframe interpolation, NEWTON]
related:
  - concepts/vlm-guided-physical-video-generation.md
  - concepts/training-free-keyframe-latent-conditioning.md
  - concepts/video-generation-physical-executability.md
  - concepts/world-models-video-generation.md
  - entities/models/wan-2-2.md
  - concepts/physics-aware-orthogonal-view-video.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | K2V: Generative Keyframing For Physically Plausible Video Generation |
| Authors | Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla, Ayush Tewari (University of Cambridge, Toyota Motor Europe) |
| Type | arXiv preprint, cs.CV |
| arXiv | 2611.17324v1, 12 Nov 2026 |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2611.17324-k2v-generative-keyframing-for-physically-plausib.pdf` |
| URL | https://arxiv.org/abs/2611.17324 |
| Retrieved | 2026-11-14 |
| Pages | 16 |
| Read status | read |
| Domain fit | **On-topic.** Video diffusion, physical plausibility, inference-time conditioning for open-weight Wan2.2. |

## Narrative

### The argument

Video diffusion models produce high appearance quality but large physical errors. K2V removes most of the physical reasoning from the video model. A language-model planning agent predicts the physically important states of a scene as **keyframes**. The video model then interpolates between them.

The authors state the core claim directly: a video model reconstructs the motion between two explicit keyframes better than it infers plausible motion from one frame in diffusion space `[TENTATIVE]` — single paper, but supported by a controlled keyframe experiment.

### Pipeline

**Keyframe module (agentic).**
1. A planning agent, Gemini 3.8 Flash, receives the caption and optionally an input image.
2. The agent imagines five seconds of evolution and divides it into phases.
3. For each phase the agent writes an editing instruction.
4. Gemini 3.1 Flash Image applies the instruction to the previous keyframe.
5. The agent reviews the result, adds a timestamp, or repeats.
6. The module returns a keyframe stack plus an **expanded caption** that describes the motion.

No physics simulator is used at any stage. Each keyframe conditions on the previous one, so the causal chain resolves serially before any video exists.

**Video model (training-free).** Wan2.2 accepts only a first frame plus caption. K2V writes keyframes into the existing first-frame conditioning channel. It pads the image tensor with mid-grey frames and then replaces specific slots with keyframes.

Two constraints make this work:
- Keyframes must land at the **end of a temporal latent block** (every `L_T = 4` frames for the Wan2.2 VAE). Intermediate conditioning fails otherwise.
- The mask vector must mark those slots as filled.

No fine-tuning and no weight change are needed. The authors attribute this to Wan2.2 pre-training that included frame interpolation as an explicit task.

**Post-processing.** An affine colour match aligns each keyframe to the input image, and each video frame to the first frame. This removes small colour drift from the image edit model.

### Results

| Benchmark | Setting | Score |
|-----------|---------|-------|
| Physics-IQ Verified (I2V) | K2V + Wan2.2-14B | 55.0 ± 0.8 |
| Physics-IQ Verified (I2V) | K2V + Wan2.2-5B | 50.0 ± 1.3 |
| Physics-IQ Verified (I2V) | best prior (Cosmos3-Super) | 42.7 |
| Physics-IQ Verified (I2V) | Wan2.2-14B alone | 32.2 |
| PhyGenBench (T2V) | K2V | 0.63 (prior state of the art 0.56) |

The 5B backbone with K2V beats the unmodified 14B backbone at about one third of the parameters. This is the strongest single number in the paper for an operator.

**Cost.** $0.47 per video on Physics-IQ Verified and $0.59 on PhyGenBench, including planning. Planning is the larger share ($0.30 and $0.42). Wan2.2-14B generation is $0.165. Both K2V configurations sit on the leaderboard cost-score frontier.

**Error does not drift.** Wan2.2-14B error grows over the five-second clip. K2V error stays near constant, because each keyframe re-anchors the scene.

**Effort scales with difficulty.** A motionless duck needs under ten seconds of planning. A domino row with a gap needs more than five minutes.

### Ablation signal

Conditioning Wan2.2-5B on evenly spaced **ground-truth** keyframes raises the Physics-IQ score monotonically with keyframe count, then plateaus. The conditioning structure is therefore the cause of the gain, independent of keyframe quality. A small number of well-placed keyframes beats many naive ones.

### Workspace relevance

This is the strongest training-free physical-plausibility lever in the wiki so far. It needs no training, no simulator, and no new weights — only an image edit model and a current VL model for planning. Both cost money per clip, so it suits a batch job, not a real-time persona pipeline.

Relevant for persona clips only where physical interaction matters: pouring, contact, falling objects, cloth. It is not a talking-head tool.

## Snippets

> "Video models are more successful at reconstructing the physical motion connecting two explicit keyframes than at inferring plausible physical motion from a starting state entirely in diffusion space." [Source: arxiv-2611.17324 p.1]

> "Keyframing raises Wan2.2-14B from 32.2 to 55.0 on the Physics-IQ Verified image-to-video track." [Source: arxiv-2611.17324 p.2]

> "Intermediate conditioning only works if the conditioning is applied at the end of a temporal block of L_T frames." [Source: arxiv-2611.17324 p.5]

## Dead Ends

Closed commercial image and language models (Gemini 3.8 Flash, Gemini 3.1 Flash Image) sit in the loop. A local-only reproduction needs substitute models, and the substitution is untested. No code release is stated in the paper.
