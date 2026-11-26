---
title: "MiniMax-H3 pose-transfer LoRA — permissive adapter, territorially restricted base (Context)"
type: entity
related:
  - "@osint-wiki/sources/2026-11-26-deep-research-batch-audit.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - entities/benchmarks/minimax-h3-reason.md
updated: 2026-11-26
---

## Raw Concept

Surfaced by
@osint-wiki/sources/2026-11-26-deep-research-batch-audit.md, URL 11, **Context** tier.
Indexed specifically to flag a licensing trap.

The question this page answers: **when an adapter says Apache-2.0, is the adapter
usable?**

## Narrative

### What it is

A community-trained pose-transfer LoRA for image generation:

- **Adapter** — 298 MB safetensors, `minimax-h3-image_pose-transfer_v2.safetensors`,
  trained with Fizgig, plus a ComfyUI workflow.
- **Task** — transfer the pose from Picture 1 onto the character in Picture 2 while
  keeping the background.
- **Base** — `MiniMaxAI/MiniMax-H3-Image`, released 2026-11-10: 33.1B DiT, native 4K in
  six distilled steps, ~135 GB BF16 including a 66.7 GB text encoder, or 11.4–21 GB
  quantised.

The author notes it was built for posing game assets and still drifts toward human
anatomical proportions.

### The trap

The adapter card lists **apache-2.0**. The base model's **Community License excludes
the United States, the European Union, the United Kingdom, and South Korea**, and
requires a manual waiver through the MiniMax console. The waiver is reportedly free
below $1M ARR, and is still non-OSI and legally encumbered.

MiniMax cites ongoing US copyright litigation as the reason for the carve-out.

[CONFIRMED — licence text in the evaluation report, 2026-11-26]

So the adapter is permissively licensed and unusable in the jurisdiction where this
workspace operates, without a separate written grant. A licence line on the small
artifact does not license the large one it depends on.

### Why it was not adopted

Beyond the licence: a 135 GB native-4K model with human-proportion bleed adds nothing
to game-time's 2D pixel sprites or Atlas101's archival prints. The capability is not
needed, and the licence is not available. Both answers are no.

### The general rule

Gate 1 must check the **whole dependency chain**. The artifact that carries the licence
line is usually the smallest piece. Read the base model card before writing an adapter
into a queue.

This is the same shape as the `wrapvm` case — a permissive-looking item with a hard
constraint behind it — and the same as a commercial add-on tier under an Apache core.

## Snippets

> Adapter card claims apache-2.0; the required base model MiniMaxAI/MiniMax-H3-Image
> Community License explicitly excludes the United States, European Union, United
> Kingdom, and South Korea.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 11]

> MiniMax explicitly cited ongoing US copyright litigation as the reason for the
> territorial exclusion.
> [Source: Cemini Multi-Wiki Batch Audit.docx, URL 11]

## Dead Ends

- **Reading the adapter licence as the model licence.** It is not.
- **Assuming a free waiver is a licence.** It is a manual grant, and it does not come
  with the weights.
