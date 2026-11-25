---
title: "The Pragmatic Engineer — inference engineering for software engineers"
type: source
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/timeout-cascade-cost-aware-routing.md
  - concepts/kv-cache-working-set-serving.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Inference engineering for software engineers |
| Author | Gergely Orosz (The Pragmatic Engineer) |
| Type | Newsletter (RSS teaser, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-pragmatic-engineer-2026-11-17-inference-engineering-for-software-engineers.md` |
| Retrieved | 2026-11-22 (published 2026-11-17) |
| Pages | n/a |
| Read status | read |

## Narrative

This is a teaser for a paid post. It describes the two ways to leave a frontier-lab API for open models: run "bare metal" GPUs yourself, or use an inference provider. Interviews cover Modal, Fireworks and Baseten.

The staged path it describes is the useful part:

1. **API replacement.** Swap the frontier API for a multi-tenant inference API. Watch latency and cache hit rate at load.
2. **Dedicated GPU nodes.** Move when you hit rate limits, inconsistent performance, or overpay for usage. Then size the model, choose interactivity versus throughput, size the KV cache, and plan failover.
3. **Speculative decoding.** Use it only when decode-phase compute is idle.

Reported cost claims from other companies: Uber cut per-token costs 50%, Pinterest 90%, AT&T 56%. These are [TENTATIVE] and come from the teaser.

For Cemini the takeaway is a checklist, not an action. The lane is free or cheap models through `/route`. Cache hit rate and tail latency are the metrics that decide when a provider change pays. The teaser does not give numbers, so do not quote it as evidence. [OPEN QUESTION 2026-11-22] Read the full post before citing detail.

## Snippets

> "Onboarding to an inference provider to run LLM workloads comes with challenges, such as dealing with tail latencies, worrying about cache hit rates, rate limits, and more." [Source: newsletter-rss-pragmatic-engineer-2026-11-17-inference-engineering-for-software-engineers.md]
