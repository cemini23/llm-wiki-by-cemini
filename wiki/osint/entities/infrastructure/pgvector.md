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
  - sources/platonic-representation-hypothesis-huh-2024.md
  - sources/alash3al-stash.md
  - sources/gemini-dr-wave5a-cemini-stack-2026-04-30.md
maturity: validated
created: 2026-04-23
updated: 2026-04-30
---

## Relations

- @sources/3-19-ip-sale-research.md
- @sources/3-19-telegram-discord-research.md
- @sources/3-9-pm-research.md
- @entities/infrastructure/timescaledb.md
- @entities/frameworks/finbert.md
- @sources/platonic-representation-hypothesis-huh-2024.md — 2026-04-30 — Huh/Cheung/Wang/Isola MIT ICML 2024 — theoretical claim that representations across competent models converge to a shared statistical model of reality (P(Z)). Operational read for this entity: **embedding-space portability** across model swaps is bounded above by a linear projection in the limit. Cemini's pgvector indexes are therefore more durable across LLM-vendor changes than naive intuition suggests; re-indexing on a model-swap may be a "thin re-tune" rather than a full rebuild. Caveat: PRH's strict math assumes bijective projections; lossy/stochastic data (financial series, OSINT sentiment) attenuate the guarantee but don't void it
- @sources/alash3al-stash.md — 2026-04-30 — Wave 5A Adopt for the Wiki/Librarian server. Stash uses pgvector for fact-recall queries inside its 8-stage consolidation pipeline. Cemini's existing pgvector competency directly transfers; same vector-recall pattern Cemini uses for semantic search applies to stash's persistent-memory queries. Operational disposition: deploy stash on a **dedicated PostgreSQL instance** (separate from Cemini's existing pgvector) to avoid upgrade-coupling risk.

## Raw Concept

Synthesized from 3 source(s) referencing this entity across the Cemini research corpus. Category: infrastructure.

## Narrative

pgvector is the PostgreSQL extension for vector similarity search. Co-
tenant with TimescaleDB in the same Postgres instance, which keeps the
stack footprint small (no separate vector database to operate or hand
over to the acquirer).

Primary uses (deployment status calibrated 2026-04-26 K5):

- **Research-corpus retrieval** — `pgvector` is in postgres extensions and the `cemini_mcp` service uses RAG-style retrieval against the embedded research corpus. *(Earlier bullet specified "with FinBERT or an open sentence-encoder" + "Telegram message" — both are post-K3 corrections: FinBERT is `[RETRACTED 2026-04-26 K3 deep-read]` per @entities/data-sources/telethon.md (the source explicitly rejects FinBERT-class transformers as too CPU-expensive for real-time stream processing); Telegram message embedding is moot because the Telegram ingester is not deployed. The actual deployed encoder is undetermined from the outside but is **not** FinBERT.)*
- **Event deduplication** — GDELT events ingested via `gdelt_harvester` container can be embedded and compared by cosine distance to suppress duplicate-story flooding of strategy inputs. (Pattern is implementable on the deployed stack; specific dedup-by-cosine usage not directly verified at K5 server probe level.)
- **Ticker-description similarity** — company-profile embeddings feed cluster-aware basket construction in dispersion-trading strategies. (Implementable; specific deployment status not verified.)

## Snippets

*(populate as source stubs are deep-read.)*
