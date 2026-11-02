---
title: "LiquidAI/d1-2B — single-pass decision model (LFM Open License, $10M threshold)"
type: entity
tags: [tool, model, multimodal, local-inference, system-one, atto, collectibles, ceminiparlays]
keywords: [d1-2B, liquid ai, LFM3-VL, system one, single forward pass, box detection, pre-grade, jev gate]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md
  - entities/tools/jeveryword.md
maturity: draft
created: 2026-11-01
updated: 2026-11-01
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-b-2026-11-01.md, URL 6, **Integrate** tier — the only Integrate in either v10.10 batch. Routed to Collectibles, Atto, and CeminiParlays.

The question this page answers: **can a small local model replace per-decision LLM calls for scoring, span extraction, and box localisation?**

## Narrative

### What it is

A 1.92B-parameter model from Liquid AI, built on LFM3-VL-2B. It answers in a **single forward pass** instead of generating tokens. The model card states plainly that it is **not a chat model**. Its job is one pipeline step: routing, moderation, extraction, or reranking.

Question types:

| Type | Output |
|------|--------|
| `noul` | Unconstrained short answer. |
| `choice` | One label from a supplied set. |
| `score` | An ordinal value across 2–10 ordered levels. |
| span types | Text, number, or date, returned as a span of the input. |
| `box` / `boxes` | Object localisation as fractional image coordinates, up to 16 instances or a `max` you set. |

Input modalities are text, image, and video.

### Hardware

Documented inference is Transformers `trust_remote_code=True`, version 5.19 or later. Sample code runs on CUDA, Apple `mps`, or CPU in fp32.

Published latency, per decision:

| Device | Time |
|--------|------|
| NVIDIA H100 PCIe | 5.7 ms |
| AMD MI325X | 3.8 ms |
| Apple M5 Pro via `mps` | 18.6 ms |

First call includes about one minute of compilation.

**The laptop runs it.** 18.6 ms per decision on Apple Silicon is the number that matters here, because it makes the model usable inside a local pipeline rather than as a batch job.

### Licence — Phase-0 finding, 2026-11-01

LFM Open License v1.0. The report asked to "verify redistribution terms for packaged Atto kits". The verified position:

| Question | Answer |
|----------|--------|
| Can a commercial product bundle it? | **Yes**, while the entity stays below the threshold. |
| What is the threshold? | **$10 000 000** or more in annual revenue. Above it, use "is not licensed". |
| What must accompany redistribution? | The licence, marked modified files, existing notices, and any NOTICE file attributions. |
| Patent grant? | Yes, terminated if you sue alleging the work infringes a patent. |
| Trademark? | No rights granted. |

Atto is far below the threshold. Bundling is permitted **today**. Add the licence file and the NOTICE file to the kit. Re-read the licence if revenue approaches the threshold.

### The three routings

**Collectibles — visual pre-grade.** `score` over ordered condition levels, plus `box`/`boxes` for corner and centering localisation. This is the clearest fit: a bounded set of ordered labels on an image, at 18.6 ms, with no token generation and therefore no drift.

**Atto — record triage.** Short-field extraction from scanned records. The open question is accuracy on Italian handwriting and pre-war typography. The model card gives no benchmark for that.

**CeminiParlays — the jev-gate.** A local screen of a slip before it goes further. The name comes from the paired tool, @entities/tools/jeveryword.md. The gate is the right shape for this model: pick one label from a set, or produce an ordered score.

### What this does not do

- It is not a chat model. Do not route conversation to it.
- It does not generate text. If the task needs a sentence, this is the wrong tool.
- The model card documents **Transformers only**. Community MLX and GGUF builds exist — the download counts are real — but their behaviour is not verified here.

### Status

**Integrate**, gated on a local acceptance test per use case. Run each candidate task against a hand-labelled sample before wiring it in. The licence is cleared; only accuracy is open.

## Snippets

> "Any Commercial Use of the Work or a Derivative Work by a Legal Entity that exceeds the Threshold is not licensed" — LFM Open License v1.0, Threshold defined as "$10,000,000 or more" [fetched 2026-11-01]

> The card states it is "not a chat model" and is meant for pipeline steps such as routing, moderation, extraction, and reranking. [fetched 2026-11-01]

> "Apple M5 Pro via `mps` (18.6 ms)" — speed benchmark [fetched 2026-11-01]

## Dead Ends

- **Assuming the MLX or GGUF builds behave like the card.** The card documents Transformers only.
- **Treating it as a general assistant.** It answers one bounded question per pass and does not converse.
- **Citing an Atto accuracy figure.** None exists. The card gives no benchmark for historical Italian record text.
