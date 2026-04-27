---
title: Architectural Transformation and Scalability Roadmap for the Cemini Financial Suite
type: source
tags: [docx, rl-marl, market-microstructure, quant-finance, ml-methods, crypto, cemini-internal, infrastructure, kubernetes, litestar, redpanda, microservices]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - concepts/rl-marl-research.md
maturity: validated
created: 2026-04-23
updated: 2026-04-26
clusters:
  - rl-marl
  - market-microstructure
  - quant-finance
  - ml-methods
  - crypto
  - cemini-internal
  - infrastructure
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @concepts/rl-marl-research.md — cluster hub for RL/MARL research in the Cemini corpus

## Raw Concept

- **Original title**: Architectural Transformation and Scalability Roadmap for the Cemini Financial Suite
- **Author(s)**: Cemini internal research (no attributed author)
- **Type**: DOCX (internal roadmap)
- **Location**: research for cemini/Cemini Suites Technical Analysis.docx
- **Length**: ~4738 words, 166 paragraphs
- **Retrieved**: 2026-04-23
- **Read status**: read-skim
- **Primary cluster**: ml-methods (misclustered — this is primarily an infrastructure/scalability roadmap, see flags)
- **All clusters**: rl-marl, market-microstructure, quant-finance, ml-methods, crypto, cemini-internal, infrastructure

## Narrative

A scalability roadmap that proposes transforming Cemini from the current single-Hetzner monolith into a decoupled microservices architecture on Kubernetes (GKE/EKS), with a public web frontend and 24/7 background RL training/data harvesting. Prescribes Domain-Driven Design + Strangler Fig migration into five services: Market Data Harvester, Feature Engineering Pipeline, RL Inference Engine, Continuous Training Worker, Public Web API Gateway.

Technology selections: Kubernetes over Fargate/Cloud Run (cites Fargate costing up to 300% more for continuous workloads; Cloud Run is request-driven and unsuited for stateful background training). Litestar over FastAPI (C-based msgspec + Rust query parser; ~2x throughput in 2025 benchmarks). Redpanda over Kafka and NATS JetStream (C++/Seastar thread-per-core, Kafka-API-compatible, no JVM GC pauses, no ZooKeeper).

IMPORTANT INTERNAL CONFLICT: This roadmap directly contradicts the "Cemini stays on one Hetzner VPS, CPU-only, <$50/mo" constraints that govern the rest of the Cemini internal research corpus (see 3-19-rl-research, 3-19-signal-fusion-engine-research, cost-effective-algorithmic-trading-api-stack). The proposal advocates GPU node pools for continuous training, which is mutually exclusive with the "CPU-only, no CUDA" constraint present elsewhere. This document appears to describe a future state (post-IP-sale or scale-up phase), not the current architecture.

Relevant to Cemini as either (a) a target-state scale-up reference or (b) a candidate for retraction / explicit labeling as "future/out-of-scope" depending on whether the Hetzner constraint is a hard architectural commitment. Honest limits: document is buzzword-dense ("state-of-the-art", "ultra-low tail latency"), benchmarks are vendor-cited ("up to 300%", "approximately double"), and the GPU node pool recommendation is incompatible with other internal research.

## Key findings

- **CONFLICT FLAG**: This roadmap assumes GPU node pools + Kubernetes cloud migration, directly contradicting the CPU-only Hetzner VPS architectural invariant asserted in every other Cemini internal research doc.
- Prescribed decomposition: Market Data Harvester → Feature Engineering → RL Inference → Continuous Training Worker → Public Web API Gateway.
- Strangler Fig migration: extract Public Web API first, incrementally peel off other services from the monolith.
- Litestar over FastAPI: C-based msgspec + Rust query parser + class-based controllers; ~2x JSON throughput claim.
- Redpanda over Kafka/NATS: Kafka-API compatible, thread-per-core Seastar, no JVM GC pauses, no ZooKeeper, Raft built-in.
- Kubernetes over Fargate/Cloud Run: cites Fargate 300% cost premium for continuous workloads; explicit GPU node pool allocation for training.
- Spot Instances 55-90% discount cited as baseline cost lever for 24/7 trading.

## Snippets

- **Sec 2.1** — "the architecture must transition toward a decoupled microservices paradigm, underpinned by state-of-the-art, open-source infrastructure."
- **Sec 2.2 (CONFLICT)** — "RL training requires advanced hardware, including GPU acceleration and large shared memory spaces. Kubernetes allows the continuous training worker to be scheduled on dedicated GPU node pools" — directly contradicts CPU-only constraint in other Cemini docs.
- **Sec 2.3** — "Recent 2025 performance benchmarks comparing ASGI frameworks reveal that Litestar achieves approximately double the throughput of FastAPI in JSON serialization tasks."
- **Sec 3.1** — "Redpanda completely eliminates garbage collection pauses, delivering deterministic, ultra-low tail latencies even under extreme read/write loads."
