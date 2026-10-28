---
title: "MiD-VLM — detecting semantic misinformation in image-caption pairs"
type: source
tags: [source, arxiv, disinformation, multimodal]
related: []
maturity: draft
read_status: skimmed
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | MiD-VLM: Detecting and Grounding Global Semantic Misinformation in Image-Caption Pairs |
| Authors | Tarunya Prasad, Bharatesh Chakravarthi — Arizona State University |
| arXiv | 2610.32967 |
| File | `arxiv-2610.32967-mid-vlm-detecting-and-grounding-global-semantic.pdf` |
| Retrieved | 2026-10-27 |
| URL | https://arxiv.org/abs/2610.32967 |
| Read status | skimmed (abstract + intro) |

## Narrative

Most image-forensics tools look for pixel-level tampering. This paper covers a different
attack. The image is authentic and untouched. Only the caption is false, so the pair reports
an event, place or action that did not happen. Pixel-artefact detectors have nothing to find.

The authors frame this as *global semantic* inconsistency, where the mismatch sits in the
relationship between image and text rather than in any local patch.

**Method.** A multimodal model fuses two visual streams: image-text representations from
SigLIP, and visual scene features from DINOv2, combined through a projection MLP. The authors
adapt Qwen2-VL-7B with LoRA. The model makes three predictions at once — is the pair
authentic, what type of manipulation is present, and which caption tokens carry the
misleading claim.

**Results.** On the DGM4+ validation split, the model reaches **F1 = 0.9679** for the binary
authenticity task. The authors report token-level grounding as the weaker half and call for
further work on precise grounding.

**Defensive implication.** A high binary F1 is useful for triage, but it is not the same as
producing evidence a reviewer can act on. For a blue team working disinformation cases, the
grounding output matters more than the label, because it names the claim to check. Treat
0.9679 as a single-source, single-dataset figure from the authors.

Routed from the image-gen inbox on 2026-10-27; the topic is disinformation detection, not generation.

## Snippets

> "Because the image itself may contain no visible signs of manipulation, methods designed to detect pixel-level artifacts can miss these misleading image-caption pairs." [Source: `arxiv-2610.32967-mid-vlm-detecting-and-grounding-global-semantic.pdf` p.1 (arXiv 2610.32967), retrieved 2026-10-27]
