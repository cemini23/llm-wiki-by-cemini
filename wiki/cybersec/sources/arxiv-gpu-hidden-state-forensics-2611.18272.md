---
title: "From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States (2611.18272)"
type: source
maturity: draft
related:
  - concepts/gpu-hidden-state-forensics.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** From Bytes to Behavior: Request-Level Attribution from Live GPU Hidden States
- **Authors:** Jonathan Pan, Yidi Yuan, Xin Wei Chia, Xinhui Su, Vincent Tan, Brenda Ong (HTX, Singapore)
- **Type:** arXiv preprint, digital forensics
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.18272-from-bytes-to-behavior-request-level-attribution.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18272
- **Read status:** full — 7 pages extracted 2026-11-16

## Narrative

Memory forensics for machine-learning systems usually targets static artefacts — weights, prompt logs. That misses the transient state of a live inference process, which is exactly what an examiner needs when the service cannot be restarted or modified.

The method acquires per-layer residual-stream activations from a live GPU process using a non-modifying debugger, without prior knowledge of architecture parameters or weights. A six-stage process with platform-specific adapters uses either a PyTorch allocator clock or a kernel-launch clock to locate and read tensor allocations in video memory.

Validation: 33 open-source decoder-only models across nine architecture classes, with recovered bytes byte-exact and usable downstream.

Use case: linear probes trained on standard framework activations, applied to recovered states, separate refusal from compliance at AUROC 0.88 on held-out prompts.

The operational point is that a deployed model's per-request internal state is recoverable evidence on a live system, without instrumentation the operator added.

[Source: arxiv-2611.18272-from-bytes-to-behavior-request-level-attribution.pdf]

## Snippets

> "distinguishing refusal from compliance with an AUROC of 0.88 on held-out prompts."

## Dead Ends

- **Full-read note (2026-11-16):** Stated scope bound: conclusions are limited to what live states can support, excluding any claim about semantic content or intent. [Source: arxiv-gpu-hidden-state-forensics-2611.18272.md full text, 7pp]
