---
title: "supavec — PostgreSQL+Supabase RAG backend with P95 210ms hybrid vector search"
type: entity
category: tool
tags: [entity, tool, rag, vector-search, postgresql, supabase, kb-server, k44, steal-from-doc-level-pending-phase-0]
keywords: [supavec, plpgsql, batch-embeddings, file-id-filter, redis-sliding-window, chunking-overlap, apache-2-license]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - concepts/cemini-license-posture.md
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @concepts/cemini-license-posture.md — Apache-2.0 IP-sale-safe

## Raw Concept

A TypeScript+Supabase RAG (Retrieval-Augmented Generation) backend optimized for batch embeddings and hybrid `file_id` + cosine-similarity vector search. Claimed P95 latency 210ms. **Apache-2.0, 1,100 stars** per K44 doc-level eval. Verdict: **Steal-from** — extract the PLpgSQL schemas, chunking-overlap algorithms, and Redis sliding-window rate-limiting strategies for the OSINT-wiki's `kb-server` REST API; do not embed the TypeScript runtime.

## Narrative

K44 primary fit: OSINT-wiki (kb-server retrieval optimization). Cross-routes: Cybersec-wiki (Supabase RLS for multi-tenant data isolation), CCC-wiki (vector chunking patterns for local retrieval setups).

**Steal-from rationale**: Apache-2.0 is IP-sale-safe but Cemini's kb-server is Python/FastAPI-on-Hetzner, not TypeScript/Supabase-on-Vercel. The architectural patterns (PLpgSQL schemas, chunking overlap, sliding-window rate limits, file_id hybrid filtering) port cleanly into the existing kb-server stack; the runtime does not.

**Phase-0 gates** (must clear before pattern extraction):
- G1: Star + maturity verification (`gh api repos/supavec/supavec`)
- G2: License verification (LICENSE file must actually be Apache-2.0)
- G3: Read the PLpgSQL schema; confirm file_id+cosine hybrid filter is real (not just claimed) and that 210ms P95 is reproducible on a comparable corpus
- G4: Chunking-overlap algorithm — extract the specific overlap math and confirm it improves recall vs Cemini's current chunking

**Highest-value extraction targets**:
1. The hybrid `file_id` + cosine similarity filter (faster than pure cosine on filtered subsets)
2. Redis sliding-window rate-limiting (replaces hand-rolled limiters in current kb-server)
3. Chunking-overlap algorithm (currently kb-server uses fixed-window chunking)

## Snippets

> "Supavec implements a remarkably efficient vector search backend capable of generating batch embeddings while achieving a P95 latency of just 210 ms using a hybrid file_id and cosine similarity filter."
[Source: K44 eval ¶133]
