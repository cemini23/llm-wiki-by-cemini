---
title: "supavec — PostgreSQL+Supabase RAG backend with hybrid file_id + cosine vector search"
type: entity
category: tool
tags: [entity, tool, rag, vector-search, postgresql, supabase, kb-server, k44, steal-from-go-phase-0-2026-05-14, p95-claim-unverified]
keywords: [supavec, plpgsql, batch-embeddings, file-id-filter, redis-sliding-window, character-based-chunking, rls-file-ownership, apache-2-license, port-to-python-fastapi]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - concepts/cemini-license-posture.md
maturity: validated
created: 2026-05-14
updated: 2026-05-14
---

## Relations

- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @concepts/cemini-license-posture.md — Apache-2.0 IP-sale-safe

## Raw Concept

A TypeScript+Supabase RAG (Retrieval-Augmented Generation) backend with hybrid `file_id` + cosine-similarity vector search via PLpgSQL RPC. Claimed P95 latency 210ms (no benchmarks shipped — unverified). **Apache-2.0, 1,068 stars verified (vs claimed 1,100)**. Verdict: **STEAL-FROM-GO** — all 5 high-value patterns confirmed real and portable to Python/FastAPI in ~18–28 hours of engineering work.

## Narrative

K44 primary fit: OSINT-wiki (kb-server retrieval optimization). Cross-routes: Cybersec-wiki (Supabase RLS for multi-tenant data isolation), CCC-wiki (vector chunking patterns for local retrieval setups).

**Steal-from rationale**: Apache-2.0 is IP-sale-safe but Cemini's kb-server is Python/FastAPI-on-Hetzner, not TypeScript/Supabase-on-Vercel. The architectural patterns port cleanly into the existing kb-server stack; the runtime does not.

### Phase-0 audit verdict (2026-05-14): STEAL-FROM-GO

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `supavec/supavec` resolved; multi-author with active commits |
| G1 | Star + maturity | **PASS** | 1,068★ verified (-32 drift vs claimed 1,100, ~3% inflation — minor), Apache-2.0, actively maintained |
| G2 | License | **PASS** | Apache-2.0 verbatim; LICENSE file present; NOTICE inheritance rules apply to Python port |
| G3 | Hybrid file_id + cosine RPC | **PASS — REAL** | `match_documents` PLpgSQL function confirmed in `supabase/migrations/`; uses `pgvector` cosine similarity with `WHERE file_id IN (...)` pre-filter. Pattern portable to Python via `asyncpg` + raw SQL |
| G4 | P95 210ms claim | **UNVERIFIED** | **No benchmarks shipped.** No load-test fixtures, no corpus-size context, no concurrency parameters. Claim is anecdotal. Must benchmark on Cemini's corpus before publishing latency targets |
| G5 | Chunking algorithm | **PASS — character-based** | Fixed-character-window chunking with overlap; specific overlap math in `lib/chunking.ts`. Not token-aware (will produce mid-token splits on non-Latin scripts). Acceptable for English research corpora |
| G6 | Rate limiting | **PASS — sliding-window** | Redis-backed sliding-window limiter; portable to Python via `redis-py` + Lua script. Cleaner than current kb-server hand-rolled fixed-window |
| G7 | Batch embeddings | **PASS** | OpenAI batch API with chunked dispatch; portable directly to Python OpenAI SDK |
| G8 | RLS + file ownership | **PASS** | Supabase RLS policies enforce per-user file isolation; pattern translates to FastAPI dependency-injection + per-row `owner_id` check |
| G9 | Python port effort | **18–28 hours** | Breakdown: PLpgSQL RPC port (4–6h), character chunking (2–3h), sliding-window limiter (3–4h), batch embeddings (2–3h), RLS analog as FastAPI deps (4–6h), integration testing (3–6h) |

**Verdict: STEAL-FROM-GO.** All patterns confirmed real and portable; total estimated effort 18–28h.

### Five ranked extractable patterns

1. **Hybrid file_id + cosine RPC** (highest value) — `WHERE file_id IN (...) ORDER BY embedding <=> query` pre-filtering. Faster than pure cosine on filtered subsets. Port: PLpgSQL function callable from Python via `asyncpg`.
2. **Character-based chunking with overlap** — fixed-window chunking with explicit overlap math. Port: Python equivalent in `kb_server/chunking.py`. **Caveat**: not token-aware; mid-token splits on non-Latin scripts.
3. **Redis sliding-window rate limiter** — replaces current hand-rolled fixed-window. Port: `redis-py` + Lua script for atomic sliding-window counts.
4. **Batch embeddings dispatch** — OpenAI batch API chunked-dispatch wrapper. Port: direct Python OpenAI SDK equivalent; minimal logic to extract.
5. **RLS + file ownership** — Supabase RLS policy logic. Port: FastAPI dependency-injection enforcing per-row `owner_id` checks; not a 1:1 transfer (Postgres-level vs application-level), but the policy *logic* is portable.

### Critical caveats

1. **P95 210ms claim is unverified** — no benchmarks in repo. Do NOT cite this number in Cemini docs until reproduced on a comparable corpus. Run a benchmark on kb-server's actual data before publishing latency targets.
2. **Apache-2.0 NOTICE file inheritance** — when porting patterns, include attribution per Apache-2.0 §4.4; document the supavec source in the kb-server `NOTICE` file.
3. **Character chunking is not token-aware** — acceptable for English research corpora; if kb-server starts ingesting non-Latin scripts (Chinese, Japanese, Arabic), need to upgrade to tiktoken-aware chunking instead.

## Snippets

> "Supavec implements a remarkably efficient vector search backend capable of generating batch embeddings while achieving a P95 latency of just 210 ms using a hybrid file_id and cosine similarity filter."
[Source: K44 eval ¶133 — Phase-0 audit confirms hybrid filter is real; P95 210ms claim is unverified (no benchmarks shipped).]
