---
title: "kornia — batched differentiable CV operators (Apache-2.0); speedup is GPU-batch only"
type: entity
tags: [tool, computer-vision, collectibles, pre-grade, pytorch]
keywords: [kornia, ransac homography, warp perspective, clahe, lightglue, card rectification, centering]
related:
  - sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 7, **Integrate** tier. Routed to Collectibles pre-grade and cataloguing.

The question this page answers: **what does kornia add to a single-card imaging pipeline that OpenCV does not already do?**

## Narrative

### What it is

A PyTorch computer-vision library, **Apache-2.0**, with 1 200+ operators. Its emphasis is at least as much on **differentiable geometry** — cameras, epipolar geometry, solvers, Lie groups — as on image processing.

The operators the report names for Collectibles:

| Operator | Use on a card scan |
|----------|--------------------|
| `warp_perspective` + RANSAC homography | Rectify a photographed card back to a true rectangle |
| Canny / Sobel | Locate card edges and measure left/right and top/bottom borders |
| CLAHE, Lab colour conversion | Normalise lighting and lift surface defects before scoring |
| LightGlue matching | Match a card against a reference image |

### Phase-0, 2026-11-02 — the speed claim does not transfer

The report claims "10x–70x faster eager, >100x with torch.compile" against single-image CPU OpenCV preprocessing.

The README says two things that change that reading:

1. The speed advantage is for **batched tensors on a GPU**.
2. **"OpenCV outperforms Kornia for single-image `uint8` CPU work."** — stated directly.

Card scanning processes **one image at a time**. At batch size 1 on a laptop, the throughput case disappears, and the README says the incumbent wins.

There is a second caveat: **no CI job covers CUDA or MPS half precision.** Full-precision `mps` appears supported; fp16 on Apple Silicon is untested.

### What the Integrate actually buys

Not speed. **Composability.**

The value is that rectification, edge detection, colour normalisation, and feature matching all live in one tensor graph, in one dtype, on one device. In OpenCV they are separate calls on numpy arrays with implicit conversions between them, and each conversion is a place a bug hides.

For a pre-grade pipeline that will grow — more measurements, more defect classes — one consistent pipeline is worth more than a per-stage benchmark win that does not apply at batch size 1.

### When the speed claim would apply

If Collectibles ever pre-processes a **batch** — a whole submission of 50 cards at once, or a bulk re-scan of a collection — the batched path returns and the GPU advantage is real. That is a reason to have it already in place, not a reason to adopt it for speed today.

### Status

Integrate, **for operator composition, not throughput**. Confirm `mps` full precision on the target machine before committing.

## Snippets

> "OpenCV outperforms Kornia for single-image `uint8` CPU work." — README [fetched 2026-11-02]

> "Kornia is released under the Apache 2.0 license." — README [fetched 2026-11-02]

> "No CI job covers CUDA or MPS half precision." — README [fetched 2026-11-02]

## Dead Ends

- **Expecting a 10x–70x speedup on a one-card-at-a-time pipeline.** The claim is batched-GPU, and the README hands the single-image CPU case to OpenCV.
- **Assuming fp16 on Apple Silicon is safe.** No CI covers it.
