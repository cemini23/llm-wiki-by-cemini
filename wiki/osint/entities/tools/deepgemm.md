---
title: "deepseek-ai/DeepGEMM — FP8 GEMM/MoE kernels (Watch)"
type: entity
tags: [tool, gpu, fp8, kernels, cuda, watch, k283]
keywords: [deepgemm, fp8, gemm, moe, cuda, cutlass, hopper, blackwell, watch, k283]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: **Watch**)
- @concepts/k283-eval-wave.md — K283 cluster hub

## Raw Concept

- **Repo:** `github.com/deepseek-ai/DeepGEMM`
- **Tier (K283):** **Watch**
- **License:** NOT FOUND (docx)
- **Stack:** CUDA, C++, CUTLASS, PyTorch, FP8

## Narrative

Clean, highly optimised **FP8 GEMM kernels** — dense and Mixture-of-Experts (MoE) grouped GEMMs — for modern GPUs.

### Why it is only Watch

The kernels **require NVIDIA Hopper (H100/H800) or Blackwell**. The operator's local abliterated lab runs Apple Silicon or an RTX 4090, which cannot execute them. The row holds until accessible FP8-Hopper-native hardware exists. **Not a rejection — a hardware gate.**

### Would wire

If a Hopper/Blackwell host appears, this is an offline-inference acceleration candidate for the local abliterated lab. Route: Cybersec wiki / local-abliterated-lab awareness.

## Snippets

> "These custom kernels require NVIDIA Hopper (H100/H800) or Blackwell hardware architectures, rendering them unusable on typical operator consumer hardware." [Source: eval-github-repos-dev-tools-2026-10-06.md]
