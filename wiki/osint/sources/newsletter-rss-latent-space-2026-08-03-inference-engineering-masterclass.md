---
title: "Latent Space — The Inference Engineering Masterclass (Baseten) 2026-08-03"
type: source
tags: [source, newsletter-rss, latent-space, inference, k221]
keywords: [Baseten, KV-cache, prefill, decode, quantization, speculative-decoding, inference-engineering]
related:
  - sources/newsletter-rss-latent-space-2026-08-05-megakernels.md
  - sources/newsletter-rss-latent-space-2026-08-04-qwen-38.md
  - concepts/llm-agent-systems.md
  - concepts/coding-agent-substrate-steerability.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-08-03
updated: 2026-08-05
read_status: skimmed
---

## Relations

- @sources/newsletter-rss-latent-space-2026-08-05-megakernels.md

- @sources/newsletter-rss-latent-space-2026-08-04-qwen-38.md

- @concepts/llm-agent-systems.md
- @concepts/coding-agent-substrate-steerability.md
- @concepts/wiki-tooling-evaluation.md
- @ccc-wiki — primary route (agent / inference substrate)

## Raw Concept

| Field | Value |
|-------|--------|
| Title | The Inference Engineering Masterclass — Philip Kiely & Ali Taha, Baseten |
| URL | https://www.latent.space/p/inference-eng |
| sha256 | `e146f376570b062f0dfa96fdd87d7131bebf546a09555a02ab517e21a1db7434` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-03-the-inference-engineering-masterclass-philip-kie.md` |
| Feed | latent-space |
| Cross-wiki | CCC (primary) |
| read_status | skimmed |

## Narrative

Baseten / Latent Space episode on inference as its own discipline: cache-aware routing, disaggregated **prefill vs decode**, KV-cache movement, quantization (errors can cancel; throughput gains), speculative decoding, model parallelism / kernels, day-0 open-model serving. **Route → CCC** for harness/serving notes; OSINT keeps only overlap with agent-substrate / tooling eval vocabulary. No trading signal.

## Snippets

> Inference engineering inherently tackles a different question than standard model training: “How do you turn those weights from training into a product that is fast, reliable, and affordable at scale?” [Source: https://www.latent.space/p/inference-eng (retrieved 2026-08-03)]

> We go deep on cache-aware routing, disaggregated prefill and decode, quantization, speculative decoding, KV-cache movement… [Source: Latent Space 2026-08-03]
