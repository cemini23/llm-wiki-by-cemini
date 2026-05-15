---
title: "OmniVoice — Zero-Shot Voice Cloning for 600+ Languages (k2-fsa)"
type: entity
tags: [voice-cloning, tts, pytorch, whisper-asr, arxiv, apache, adopted-tier]
keywords: [omnivoice, zero-shot-tts, 600-languages, diffusion-language-model, cmu-dictionary, persona-ops]
related:
  - sources/multi-wiki-tool-evaluation-v3.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/multi-wiki-tool-evaluation-v3.md — v3 batch eval: Adopt tier, Image-gen wiki primary fit

## Raw Concept

From the Cemini Multi-Wiki Link Evaluation Report v3 (May 2026). Apache-2.0 licensed, 5.9k stars, backed by a 2026 arXiv preprint. Pure Python/PyTorch voice cloning with zero-shot capability from 3-10 seconds of reference audio.

## Narrative

OmniVoice provides high-fidelity zero-shot voice cloning across 600+ languages using a diffusion language model architecture. Key features: precise pronunciation control via CMU dictionaries, expressive non-verbal tags ([laughter]), and 100% Python/PyTorch alignment with existing ComfyUI GPU hardware stacks.

**Tier: Adopt** — Apache-2.0, pure Python, compatible with existing GPU infrastructure. Critical for Image-gen wiki persona-ops voice requirements.

**NEEDS VERIFICATION:** VRAM overhead and inference Real-Time Factor (RTF) scaling when batch-processing long-form conversational content across multiple M-series GPUs.
