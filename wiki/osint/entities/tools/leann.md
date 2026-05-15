---
title: "LEANN — storage-efficient local vector index (RAG on everything)"
type: entity
tags: [tool, vector-search, rag, vector-index, local-first, mcp, memory, adopt]
keywords: [leann, yichuan-w, vector-index, selective-recomputation, graph-index, rag, mcp, storage-compression, mit-license, adopt]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-15.md
  - entities/tools/turbovec.md
  - entities/infrastructure/conductor-librarian-architecture.md
  - concepts/kb-server-retrieval-scaling.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
phase_0_verdict: ADOPT 2026-05-15 (MIT verified, locally installed)
---

## Relations

- @sources/tool-evaluation-wiki-fit-2026-05-15.md — evaluated in the 52-URL eval (Adopt tier, CCC primary, cross-routed to OSINT)
- @entities/tools/turbovec.md — sibling vector-index tool; turbovec compresses via SIMD quantization, LEANN via graph-based selective recomputation — overlapping problem space, worth a head-to-head before committing the librarian to either
- @entities/infrastructure/conductor-librarian-architecture.md — LEANN's storage profile is directly relevant to kb-server's embedding store
- @concepts/kb-server-retrieval-scaling.md — the K47 benchmark + NO-GO decision: LEANN not wired into kb-server

## Raw Concept

Promoted from the 2026-05-15 "Tool Evaluation and Wiki Fit" 52-URL eval. Tier: **Adopt**. Primary fit: CCC-wiki. Cross-route: **OSINT-wiki** (indexing large intelligence corpora locally).

- URL: https://github.com/yichuan-w/LEANN
- License: **MIT** — verified via GitHub API 2026-05-15 (matches report)
- Stars: 11,031 | Last push: 2026-05-15 | Open issues: 38 | Stack: Python / C++

## Narrative

LEANN ("Low-storage Embedding-based Approximate Nearest Neighbor") is a local-first vector index that trades storage for compute: instead of persisting every embedding, it stores a pruned graph and **recomputes embeddings on-the-fly during search**. The result is an index roughly **97% smaller** than a conventional one — the project cites 60M text chunks indexed in ~6GB — without meaningfully degrading approximate-nearest-neighbor recall.

It ships native **MCP** integration and a `skills/leann-memory` directory, and targets personal-AI-memory corpora (ChatGPT / Claude / WeChat exports, local documents).

**OSINT relevance (why cross-routed in)**: the librarian's kb-server currently indexes ~860+ wiki pages; LEANN's storage profile makes semantic search over much larger ephemeral intelligence corpora tractable. It overlaps with `turbovec` (also Adopt, also a compact local index) — the two solve the same problem by different means (graph selective-recomputation vs. SIMD scalar quantization). Decision deferred: do not wire either into kb-server before a direct benchmark on the actual wiki corpus.

**Deployment boundary** — the laptop install (below) is a **benchmark / interactive-workflow tool only**. If LEANN wins the benchmark and gets wired into kb-server to serve the wiki, that deployment **must run on `cemini-librarian`** — kb-server needs 24/7 uptime and this laptop is not always on. Anything serving the wiki belongs on the librarian server, never the laptop.

## Local adoption (2026-05-15)

Installed laptop-side via pip (`leann` 0.3.5, with backends `leann-backend-hnsw` + `leann-backend-diskann`). Status: **working** — `build` / `search` / `list` all verified. Scope: **benchmark + interactive workflow only** — this is not a wiki-serving deployment (see Deployment boundary above).

**Python 3.9 incompatibility (resolved).** The laptop only has system Python 3.9. LEANN's CLI pulls `llama-index-core`, whose current 0.14.x line uses `X | None` annotations evaluated at class-body time — a syntax error on Python 3.9. Fix: pin the llama-index trio down to the 0.12.x line, which LEANN's own floor (`llama-index-core>=0.12.0`) still permits:

- `llama-index-core==0.12.52.post1`
- `llama-index-readers-file<0.5` → 0.4.11
- `llama-index-embeddings-huggingface<0.6` → 0.5.5

Smoke test (3-doc corpus): index built, `leann search "what is LEANN"` correctly ranked the LEANN sentence #1 (score 1.127). The graph-based recompute path (`is_recompute=true`, NULL embedding storage marker) is exercised by this build.

**Recommendation**: the pinned Python 3.9 laptop install is sufficient for benchmarking against `turbovec`. A production wiki-serving role does **not** get set up here — it gets set up on `cemini-librarian` (Python 3.10+ available there, so no version pins needed) so kb-server keeps 24/7 uptime. The laptop install never serves the wiki.

## Librarian deployment (2026-05-15)

Installed on `cemini-librarian` (the 24/7 kb-server host) per the deployment-boundary rule — any wiki-serving component lives on the librarian, not the laptop.

- Installed clean into `/opt/leann-venv` (Python 3.12 — **no version pins needed**, unlike the laptop's 3.9). venv footprint: **5.6 GB** (torch + transformers + backends).
- Import + CLI verified.

**Benchmark vs kb-server's brute-force search** (943-doc live corpus):

- `leann build`: **19 min 23 s**, 1.5 GB RAM peak. Index: 1.2 MB.
- `leann search`: **unstable** on the 3.7 GB-RAM host — one run core-dumped (`Aborted (core dumped)`), another exited 0 with no output. Not reliably benchmarkable here.

**Verdict: NOT wired into kb-server.** LEANN's recompute-on-search design is built for huge corpora; on a 943-vector corpus it is slower to build, heavier in RAM, and unstable — strictly worse than the existing 23 µs/query brute-force. Full reasoning: `@concepts/kb-server-retrieval-scaling.md`. The librarian install stays as a staged/benchmark tool.

## Snippets

```bash
# Install (2026-05-15, Python 3.9)
pip3 install --user leann
# Python 3.9 fix — pin llama-index to the 0.12.x line:
pip3 install --user 'llama-index-core==0.12.52.post1' \
  'llama-index-readers-file<0.5' 'llama-index-embeddings-huggingface<0.6'

# Smoke test
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
leann build leann-smoke --docs ./docs
leann search leann-smoke "what is LEANN"
# → 1. Score: 1.127  "LEANN is a storage-efficient vector index ..."
```

