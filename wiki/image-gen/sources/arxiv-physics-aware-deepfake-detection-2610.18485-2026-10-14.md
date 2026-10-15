---
title: "Physics-Aware Deepfake Detection via Distance–Speech Consistency"
type: source
tags: [arxiv, deepfake-detection, audio-visual, forensics]
keywords: [deepfake detection, speaker distance, speech energy, lip-sync complement, in-the-wild video]
related:
  - concepts/k291-image-gen-wave.md
maturity: draft
read_status: read
created: 2026-10-14
updated: 2026-10-14
---

## Relations

- @concepts/k291-image-gen-wave.md — K291 image-gen wave hub

## Raw Concept

Title: Physics-Aware Deepfake Detection via Distance–Speech Consistency
Authors: Kyeongrae Kim, Kim Sung-Bin, Oh Hyun-Bin, Tae-Hyun Oh (KAIST, POSTECH)
Type: arXiv preprint (2610.18485). Code: `byulharang.github.io/PADD/`
Location: `research to be indexed/image-gen/arxiv-2610.18485-physics-aware-deepfake-detection-via-distance-sp.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The gap:** most audio-visual deepfake detectors rely on **lip–speech synchronisation** and assume static frontal video. On dynamic, in-the-wild recordings where the speaker moves, lip cues are degraded or absent.

**The cue:** an acoustic constraint. In real recordings, **speech energy varies predictably with speaker-to-camera distance**; generation can break that coupling. The detector combines **distance estimates from video** with **distance-dependent acoustic measures** from speech.

**The result:** effective in dynamic scenarios, and it **complements** lip-sync detectors — a simple ensemble gives consistent gains across datasets.

**Why it is filed here:** it is a **physical-consistency** check, not a learned artefact detector. The audio-visual coupling is a property of the world the generator must reproduce, and generators neglect it.

## Snippets

> "in real recordings, speech energy varies predictably with speaker-to-camera distance, whereas deepfake generation can break this coupling." [Source: arxiv-2610.18485 p.1]

> "the proposed physical cue is effective in dynamic scenarios, and that it complements lip-sync-based detectors, with a simple ensemble achieving consistent gains across datasets." [Source: arxiv-2610.18485 p.1]

## Dead Ends

- Treating this as a replacement for lip-sync detection. The paper positions it as complementary, with the gain coming from an ensemble.
