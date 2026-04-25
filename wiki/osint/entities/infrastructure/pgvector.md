---
title: pgvector
type: entity
tags: [infrastructure, database, vector-db, postgres-extension]
keywords: []
related:
  - sources/3-19-ip-sale-research.md
  - sources/3-19-telegram-discord-research.md
  - sources/3-9-pm-research.md
  - entities/infrastructure/timescaledb.md
  - entities/frameworks/finbert.md
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @sources/3-19-ip-sale-research.md
- @sources/3-19-telegram-discord-research.md
- @sources/3-9-pm-research.md
- @entities/infrastructure/timescaledb.md
- @entities/frameworks/finbert.md

## Raw Concept

Synthesized from 3 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

pgvector is the PostgreSQL extension for vector similarity search. Co-
tenant with TimescaleDB in the same Postgres instance, which keeps the
stack footprint small (no separate vector database to operate or hand
over to the acquirer).

Primary uses in Cemini:
- **Research-corpus retrieval** — embed every source paper + transcript
  + Telegram message with FinBERT or an open sentence-encoder; query
  by HNSW index for relevant-context retrieval in LangGraph planning.
- **Event deduplication** — GDELT events embedded and compared by
  cosine distance to suppress duplicate-story flooding of strategy
  inputs.
- **Ticker-description similarity** — company-profile embeddings feed
  cluster-aware basket construction in dispersion-trading strategies.

## Snippets

*(populate as source stubs are deep-read.)*
