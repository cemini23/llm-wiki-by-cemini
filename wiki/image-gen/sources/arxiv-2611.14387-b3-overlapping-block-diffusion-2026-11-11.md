---
title: "B3 — overlapping blocks let the next block start early"
type: source
tags: [source, arxiv, diffusion, language-models, latency, training-free]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Blurring the Block Boundaries: Overlapping Block Denoising for Efficient Diffusion Language Models |
| Authors | Amir Mann, Jonathan Fhima, Shaked Brody, Or Avivit and others |
| arXiv | 2611.14387 |
| Pages | 22 |
| Read status | skimmed (abstract) |

## Narrative

Diffusion language models generate tokens faster than autoregressive ones by denoising **blocks** in parallel. Recent work adds self-editing: each block refines its tokens iteratively before the next begins.

The bottleneck the paper names is precise: **each block is only as fast as its slowest token, and the next block cannot start before it.**

**B3** refines **two blocks in parallel within a shared forward pass**, and **calibrates itself on the fly** — opening the next block only once the model is ready to generate it.

It is **training-free and hyperparameter-free**, and integrates into any self-editing block diffusion model.

### Why "calibrates itself on the fly" is the interesting part

The obvious version of this is a fixed overlap: start block N+1 when block N is 70% done. That requires choosing 70%, which then has to be tuned per model.

Deciding **when the model is ready** from the model's own state removes the hyperparameter and produces a rule that transfers across models.

That is the same reason the eval corrections in this workspace keep landing: a fixed rule chosen in advance does not survive a change of subject, and a rule read off the current state does.

**Caveat.** Abstract only. No latency or quality figures reproduced.

## Snippets

> "Each block is only as fast as its slowest token, and the next block cannot start before it." [Source: arxiv-2611.14387 p.1]

> "B3 calibrates itself on the fly, opening the next block only once the model is ready to start generating it. It is a training-free and hyperparameter-free acceleration method." [Source: arxiv-2611.14387 p.1]

## Dead Ends

- **Citing a speedup.** Abstract only.
