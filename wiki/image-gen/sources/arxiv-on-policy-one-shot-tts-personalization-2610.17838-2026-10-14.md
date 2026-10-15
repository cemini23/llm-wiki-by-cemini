---
title: "Beyond Fixed Targets — On-Policy One-Shot Speaker Personalization for Autoregressive TTS"
type: source
tags: [arxiv, tts, voice-cloning, reinforcement-learning, personalization]
keywords: [one-shot personalization, AR TTS, GRPO, on-policy self-distillation, speaker similarity, WER]
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

Title: Beyond Fixed Targets — On-Policy One-Shot Speaker Personalization for Autoregressive Text-to-Speech Models
Authors: Sangkwon Park, Che Hyun Lee, Heeseung Kim, Sungroh Yoon (Seoul National University, University of Seoul)
Type: arXiv preprint (2610.17838)
Location: `research to be indexed/image-gen/arxiv-2610.17838-beyond-fixed-targets-on-policy-one-shot-speaker.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

**The diagnosis:** supervised fine-tuning on a single reference pair **degrades** autoregressive TTS — it produces **blank or near-empty outputs** at inference. The named cause is **fixed, off-policy supervision**.

**The near-miss:** diversifying the data with zero-shot pseudo-pairs removes the blank-output failure, but adds **little speaker similarity** and **raises word error rate**, because the targets remain **fixed and teacher-forced**.

**The fix:** two **on-policy** methods —
- **GRPO** with a speaker-similarity reward — strongest overall,
- **On-Policy Self-Distillation** with soft supervision from a reference-conditioned teacher — **substantially faster adaptation**, no external reward evaluation.

Both improve similarity while preserving intelligibility. Analysis confirms the gains come from **on-policy supervision, not target diversity**.

**Why it is filed here:** it is the wave's clearest statement that **frozen targets are the problem**. Relevant to this wiki's persona and character lanes, where one-shot voice or style adaptation is the aim.

## Snippets

> "We identify fixed, off-policy supervision as a key cause of failure in one-shot SFT for AR TTS, leading to blank or near-empty outputs at inference." [Source: arxiv-2610.17838 p.1]

> "Further analysis confirms that these gains stem from on-policy supervision rather than target diversity." [Source: arxiv-2610.17838 p.1]

## Dead Ends

- Adding training data while keeping targets fixed. The paper tries exactly that and reports little similarity gain plus higher WER.
