---
title: Live GPU hidden-state acquisition for model forensics
type: concept
maturity: draft
related:
  - sources/arxiv-gpu-hidden-state-forensics-2611.18272.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: can an examiner recover what a running model computed for a specific request, without modifying it?

From arXiv 2611.18272 (HTX Singapore).

## Narrative

The object of interest is the residual stream: for every token and layer, the running vector that each layer adds to. Weights describe what a model is; hidden states describe what it did on one request.

The acquisition is non-modifying. A debugger reads tensor allocations from video memory, keyed either on a PyTorch allocator clock or a kernel-launch clock, with no prior knowledge of the architecture parameters or weights. Validated byte-exact across 33 decoder-only models in nine architecture classes.

The demonstrated use is classification of behaviour: linear probes trained on ordinary framework activations, applied to recovered states, separate refusal from compliance at AUROC 0.88.

Why it matters operationally: this is evidence a live, unmodified inference service produces as it runs, so a forensic case no longer depends on the operator having enabled logging.

[OPEN QUESTION 2026-11-16] Whether the method survives adversarial conditions (encrypted or paged memory, non-PyTorch runtimes, multi-tenant batching) is not addressed in the abstract.

## Snippets

> "Unlike weights, which define what a model is, these hidden states capture what the model did."
