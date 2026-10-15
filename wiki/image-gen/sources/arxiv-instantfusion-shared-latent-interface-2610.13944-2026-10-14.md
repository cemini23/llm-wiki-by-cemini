---
title: "InstantFusion — A Shared Latent Interface for Heterogeneous Image Generators"
type: source
tags: [arxiv, diffusion, latent-space, model-composition]
keywords: [shared latent interface, latent autoencoder, cross-model handoff, denoising trajectory, flow models]
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

Title: InstantFusion — A Shared Latent Interface for Heterogeneous Image Generators
Authors: Xuanlang Dai, Jiazi Bu, Yujie Zhou et al. (Fudan, Shanghai AI Lab, SJTU, CUHK)
Type: arXiv preprint (2610.13944)
Location: `research to be indexed/image-gen/arxiv-2610.13944-instantfusion-a-shared-latent-interface-for-hete.pdf`
Retrieved: 2026-10-14
Read status: read

## Narrative

Independently trained diffusion/flow generators show **similar latent spatial organisation**, and handing intermediate states between *unaligned* models still preserves coarse visual content. InstantFusion exploits that: **model-specific Latent AutoEncoders** project each generator's intermediate states into a **shared latent space**, decoded into the target generator's latent space.

Two constraints define the space: aligning states from the **same image at matched noise levels**, and **synchronising local denoising velocities**.

Once trained, denoising **transitions across frozen generators** with no per-pair mapping. Demonstrated on acceleration, multi-preference composition, cross-architecture on-policy distillation, and cross-model composition.

## Snippets

> "independently trained generators exhibit similar latent spatial organization, while directly handing off intermediate states between unaligned models can still preserve coarse visual content." [Source: arxiv-2610.13944 p.1]

## Dead Ends

- Assuming a mapping is needed per model pair. The shared space is the point — one interface, many frozen generators.
