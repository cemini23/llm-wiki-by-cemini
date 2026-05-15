---
title: "TiDAR — Hybrid Diffusion-AR Language Model Architecture"
type: concept
tags: [llm-architecture, diffusion-language-models, speculative-decoding, throughput-optimization, nvidia]
keywords: [tidar, hybrid-diffusion-ar, free-token-slots, structured-attention-mask, kv-cache-reuse, parallel-drafting, rejection-sampling]
related:
  - sources/tidar-2511.08923.md
maturity: draft
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/tidar-2511.08923.md — source paper (NVIDIA, Nov 2025)

## Raw Concept

Synthesized from the TiDAR arXiv preprint (2511.08923). What question does this architecture answer: can we get AR-quality text generation at diffusion-level throughput, in a single model, without the drafter/verifier split of speculative decoding?

## Narrative

TiDAR (Think in Diffusion, Talk in Autoregression) is a hybrid LLM architecture from NVIDIA that runs diffusion-based parallel token drafting and autoregressive verification sampling in a single forward pass. It is the first architecture to close the quality gap with pure AR models while delivering 4.71–5.91× higher tokens-per-second throughput.

**How it works.** Each forward pass partitions tokens into three sections with different attention patterns:
1. **Prefix tokens** — exact KV cache from prior steps (causal attention)
2. **Proposed tokens** — drafted last step, now verified via AR rejection sampling against p_AR (causal)
3. **Pre-drafted tokens** — drafted this step via p_Diff for use next step (block-causal / bidirectional within block)

The key insight exploits GPU "free token slots": at small batch sizes, AR decoding is memory-bound and leaves GPU compute idle. TiDAR fills these idle cycles with parallel diffusion drafting at near-zero marginal latency cost.

**Training.** A single model learns both distributions via combined AR and diffusion losses on the same data, using structured hybrid attention masks. This is data-efficient — no separate drafter model, no extra training phases.

**Vs. speculative decoding.** Unlike classic speculative decoding (separate small drafter + large verifier), TiDAR uses a single model for both roles, giving the drafter the full model capacity. Unlike Medusa/EAGLE (extra heads on base model), TiDAR's drafting is parallel rather than sequential to verification. This yields both higher drafting quality (higher acceptance rate) and higher throughput.

**Limitations.** The architecture assumes GPU compute density headroom — benefits diminish at large batch sizes where AR decoding already saturates compute. The paper evaluates at 1.5B and 8B scales; scaling laws to 70B+ are unexplored.

**Relevance to Cemini.** TiDAR's free-token-slot insight is relevant to Claude Code context economics — if local models adopt this architecture, inference throughput per GPU-dollar improves 4–6×. The hybrid attention mask design also informs understanding of modern LLM serving systems.
