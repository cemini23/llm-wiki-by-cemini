---
title: "TiDAR: Think in Diffusion, Talk in Autoregression (NVIDIA, arXiv 2511.08923, Nov 2025)"
type: source
tags: [arxiv, llm-architecture, diffusion-language-models, speculative-decoding, hybrid-architecture, nvidia, 2025]
keywords: [tidar, diffusion-ar-hybrid, parallel-decoding, structured-attention-mask, kv-cache, throughput-speedup, free-token-slots]
related:
  - concepts/tidar-hybrid-diffusion-ar.md
maturity: draft
read_status: deep-read
created: 2026-05-14
updated: 2026-05-14
clusters: [llm-agents, ml-systems]
---

## Relations

- @concepts/tidar-hybrid-diffusion-ar.md — concept page synthesizing the architecture

## Raw Concept

- **Title:** TiDAR: Think in Diffusion, Talk in Autoregression
- **Authors:** Jingyu Liu, Xin Dong, Zhifan Ye, Rishabh Mehta, Yonggan Fu, Vartika Singh, Jan Kautz, Ce Zhang, Pavlo Molchanov (NVIDIA)
- **Type:** arXiv preprint (2511.08923v1)
- **Location:** `cemini-librarian:/opt/cemini-bulk/research/2511.08923v1.pdf`
- **Retrieved:** 2026-05-14
- **Pages:** 8 (two-column)

## Narrative

TiDAR proposes a sequence-level hybrid architecture that combines diffusion language models (dLMs) for parallel token drafting with autoregressive (AR) sampling for final output — all within a single forward pass using specially designed structured attention masks.

The core insight exploits GPU compute density: at small batch sizes, AR decoding is memory-bound and leaves GPU compute idle. TiDAR fills these "free token slots" with parallel diffusion drafting, achieving 4.71× (1.5B) to 5.91× (8B) tokens-per-second throughput gains while closing the quality gap with pure AR models.

Architecture (single forward pass): tokens are partitioned into three sections — (1) prefix tokens with exact KV cache reuse, (2) tokens proposed from the last step autoregressively sampled via rejection sampling guided by p_AR, and (3) tokens pre-drafted via p_Diff for the next step. A structured attention mask switches between causal (AR) and block-causal (diffusion) patterns across these sections.

Training is data-efficient: a single model learns both distributions via combined AR and diffusion losses on the same sample, using structured causal-bidirectional hybrid attention.

Key comparisons: TiDAR outperforms speculative decoding (separate drafter + verifier) and diffusion variants (Dream, Llada) in both efficiency and quality. It is the first architecture to close the AR quality gap while delivering >4× throughput.

## Snippets

> "TiDAR is the first architecture to close the quality gap with AR models while delivering 4.71× to 5.91× more tokens per second." (Abstract)

> "We leverage [free token slots] to achieve almost free paralleled drafting and sampling for TiDAR." (§1, Fig 1 caption)
