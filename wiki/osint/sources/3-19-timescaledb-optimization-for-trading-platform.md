---
title: Optimal Database Architecture for High-Frequency Multi-Asset Trading Systems (TimescaleDB)
type: source
tags: [docx, cemini-internal, rl-marl, llm-agents, market-microstructure, quant-finance, crypto, data-engineering]
related:
  - concepts/market-microstructure.md
  - concepts/quant-finance.md
  - entities/infrastructure/timescaledb.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
clusters:
  - rl-marl
  - llm-agents
  - market-microstructure
  - quant-finance
  - crypto
  - cemini-internal
  - data-engineering
---

## Relations

- @concepts/market-microstructure.md — Market Microstructure corpus-index hub (Q 2026-04-27)
- @concepts/quant-finance.md — Quantitative Finance corpus-index hub (Q 2026-04-27)
- @entities/infrastructure/timescaledb.md

## Raw Concept

- Original title: Optimal Database Architecture for High-Frequency Multi-Asset Trading Systems
- Authors: Cemini internal authoring team (unsigned)
- Affiliation: Cemini internal
- Type: DOCX, internal technical specification
- Location: research for cemini/3_19 TimescaleDB Optimization for Trading Platform.docx
- Length: long-form
- Retrieved: 2026-04-23
- Publication date: 2026-03-19
- Read status: deep-read
- Primary cluster: data-engineering
- All clusters: rl-marl, llm-agents, market-microstructure, quant-finance, crypto, cemini-internal, data-engineering
- Flag: **cemini-internal, technical spec.**

## Narrative

A TimescaleDB-focused architectural brief for Cemini's trading data layer. Recommendations: **1-day chunk sizing** on tick hypertables (balancing insert throughput vs. query selectivity for intraday queries), **Gorilla compression** on older chunks to compact historical tick data, **continuous aggregates** pre-computing 1m/5m/1h OHLCV so strategy code doesn't rebuild bars from ticks each query, **pgvectorscale StreamingDiskANN** for approximate nearest-neighbor search on embedding columns (pattern search, similar-regime retrieval), and **hypercore** (row+columnar hybrid) for blended workloads.

The document is technically specific — actual SQL snippets for hypertable creation, compression policies, continuous aggregate refresh policies, and StreamingDiskANN index construction. Not research but a production-oriented engineering guide. Value for Cemini: a ready-to-apply TimescaleDB playbook for the tick data layer. All primitives recommended are real TimescaleDB features with documented performance characteristics.

Concerns not directly addressed: multi-tenancy isolation, replication failover strategy, retention vs. compliance trade-off. Focus is on single-node performance, which fits the Hetzner VPS deployment.

## Key findings

- 1-day chunk sizing on tick hypertables for balanced insert/query performance.
- Gorilla compression on older chunks for historical tick compaction.
- Continuous aggregates pre-computing 1m/5m/1h OHLCV bars.
- pgvectorscale StreamingDiskANN for embedding ANN search.
- Hypercore (row+columnar hybrid) for mixed workloads.

## Snippets

- **chunking** — "1-day chunks on tick hypertables balance insert throughput and intraday query selectivity" — the chunking recommendation.
- **compression** — Gorilla compression is the default recommendation for historical chunks.
- **vector search** — pgvectorscale StreamingDiskANN for embedding ANN — supports pattern/regime retrieval on embedded windows.
