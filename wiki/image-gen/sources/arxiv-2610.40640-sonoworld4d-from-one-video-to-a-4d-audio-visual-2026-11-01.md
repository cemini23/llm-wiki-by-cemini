---
title: "SonoWorld4D: from one video to a 4D audio-visual scene via diffusion synchronization"
type: source
tags: [source, arxiv, video, 4d-scene, spatial-audio, diffusion]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization |
| Authors | Derong Jin, Xiyi Chen, Ming C. Lin, Ruohan Gao |
| Affiliation | University of Maryland, College Park |
| arXiv | 2610.40640 |
| Pages | 24 |
| File | `arxiv-2610.40640-sonoworld4d-from-one-video-to-a-4d-audio-visual.pdf` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/image-gen/arxiv-2610.40640-sonoworld4d-from-one-video-to-a-4d-audio-visual.pdf` |
| Retrieved | 2026-11-01 |
| Project | https://humathe.github.io/sonoworld4d |
| Read status | skimmed (abstract and first page) |

## Narrative

The paper defines a new task, `VIDEO-TO-4DAVSCENE`, and presents SonoWorld4D for it.

The input is one monocular video. The output is an explorable, time-varying 4D scene with sound. Sound is the part prior work leaves out, even though sound is coupled to the dynamic objects and events in a scene.

The method does three things from the single video:

1. Generates a 360° static background.
2. Reconstructs explicit motion trajectories for the dynamic foreground objects that emit sound.
3. Synthesises a dynamic sound field that stays consistent across multiple sources, using **dual-space diffusion synchronisation**.

The produced scene supports real-time novel-view rendering with spatial audio. Evaluation covers real-world dynamic scenes plus a user study. The paper claims perceptually realistic spatial audio that is consistent with the scene geometry and the visual content.

**Why this matters for a generation pipeline.** The contribution is joint generation of visuals and spatial audio from one clip. A clip-generation workflow that wants a usable result for a viewer needs both tracks aligned from the start, rather than dubbed afterwards. The dual-space synchronisation is the mechanism to note.

**Caveat.** Only the abstract and first page were read. No quantitative metric is reproduced here. The user study is mentioned but not summarised.

## Snippets

> "However, sound, despite being intrinsically coupled with dynamic objects and events, remains largely unmodeled in prior work. We introduce VIDEO-TO-4DAVSCENE, a new task that turns a video into an explorable, time-varying 4D audio-visual scene." [Source: arxiv-2610.40640 p.1]

> "Given a monocular video, our method generates a 360° static background, reconstructs explicit motion trajectories of dynamic, sound-emitting foreground objects, and synthesizes a dynamic sound field consistent across multiple sources through dual-space diffusion synchronization." [Source: arxiv-2610.40640 p.1]

## Dead Ends

- **Citing the user-study result.** The abstract mentions a user study and gives no figure. Only two pages were read.
