---
title: "Vision-language models on Urdu Nastaliq handwriting — a zero-shot benchmark"
type: source
tags: [source, arxiv, ocr, handwriting, vlm, benchmark, weak-fit]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Benchmarking Vision-Language Models for Urdu Nastaliq Handwriting Recognition |
| Authors | Haseeb Yaqoob, Fatima Azfar (NED University of Engineering & Technology, Karachi) |
| arXiv | 2611.01635 |
| Pages | 7 |
| Read status | skimmed (abstract) |

## Narrative

Six systems benchmarked on the Urdu Nastaliq Handwritten Dataset (UNHD): Tesseract at default, a script-specific recognizer trained on **printed** Urdu (UTRNet-Large), two open-source VLMs, and two commercial VLMs. **2,465 single-line images**, no fine-tuning, one fixed prompt.

Result: **both commercial VLMs beat** the printed-Urdu recognizer and both open-source VLMs.

The authors are careful about what that means: they do not compare against handwriting-trained recognizers, which would likely do better in-domain. They characterize **zero-shot behaviour, not state of the art**.

Three distinct failure modes are described among the ranked systems. In one, a commercial model **explicitly declines to transcribe** a few very hard-to-read images rather than guessing.

Part B tests whether VLMs can correct a separate OCR system's output given both image and noisy text. Once separated from each model's own reading ability, **the benefit is small**.

### Why it is worth keeping despite the weak fit

Two transferable observations:

1. **A refusal is a better failure than a plausible wrong transcription.** The model that declined was behaving correctly on illegible input. For any archival-digitisation work, that property matters more than raw accuracy.
2. **Correction is not separate from reading.** The Part B finding — that VLM correction adds little once you account for the VLM's own reading — is a warning against double-counting a gain.

**Relevance to this workspace.** Nastaliq is not a script this workspace handles, and Italian civil records are Latin. Filed as a method reference on zero-shot VLM OCR limits, not as a domain source.

**Caveat.** Abstract only. No accuracy figure reproduced.

## Snippets

> "In one of them, a commercial model explicitly declines to transcribe a few very hard-to-read images instead of guessing." [Source: arxiv-2611.01635 p.1]

> "Once separated from each model's own reading ability, the benefit is small." [Source: arxiv-2611.01635 p.1]

## Dead Ends

- **Reading this as a claim about Italian records.** Different script, different failure modes.
