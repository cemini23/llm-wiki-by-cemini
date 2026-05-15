---
title: "kb-server retrieval scaling — when (not) to add a vector index"
type: concept
tags: [concept, kb-server, librarian, vector-search, ann, benchmark, infrastructure, k47]
keywords: [kb-server, brute-force-cosine, turbovec, leann, sqlite-vss, ann-index, vector-search-scaling, 2000-note-threshold, premature-optimization]
related:
  - entities/infrastructure/conductor-librarian-architecture.md
  - entities/tools/turbovec.md
  - entities/tools/leann.md
  - sources/tool-evaluation-wiki-fit-2026-05-15.md
maturity: validated
created: 2026-05-15
updated: 2026-05-15
---

## Relations

- @entities/infrastructure/conductor-librarian-architecture.md — kb-server is the librarian's retrieval layer; this page sets its scaling policy
- @entities/tools/turbovec.md — benchmarked here as a candidate ANN index; staged on the librarian, not wired
- @entities/tools/leann.md — benchmarked here as a candidate ANN index; staged on the librarian, not wired
- @sources/tool-evaluation-wiki-fit-2026-05-15.md — the eval that surfaced turbovec/LEANN as Adopt-tier

## Raw Concept

The question: should kb-server's retrieval (brute-force cosine similarity) be replaced by an ANN vector index — specifically `turbovec` or `LEANN`, both Adopt-tier from the 2026-05-15 tool eval? Answered with a benchmark on the live corpus, 2026-05-15 (K47).

## Narrative

### How kb-server retrieval works today

kb-server (`cemini-librarian:/opt/kb-server`, Node.js) embeds documents with `Xenova/all-MiniLM-L6-v2` (384-dim, quantized, in-process via `@huggingface/transformers`), stores them as BLOBs in SQLite (`/root/.knowledge-base/kb.db`), and searches by **brute-force cosine similarity**. `search.js` carries an explicit author note:

> "Brute-force cosine similarity — works for <2000 notes. If vault exceeds 2000 notes, consider sqlite-vss extension for ANN search."

Current corpus: **943 vectors** — one embedding per document, no chunking. That is **~2× under** the author's own threshold.

### Benchmark (librarian, 943 real vectors, K47)

| Engine | Build | Search latency | Recall@10 | Extra footprint |
|--------|-------|----------------|-----------|-----------------|
| **brute-force** (current) | n/a | 23 µs/query | 1.000 (exact) | 0 — already in kb-server |
| turbovec bw=4 | 150 ms | 16 µs/query | 0.922 | 180 KB index; 570 MB build tree + 111 MB venv |
| turbovec bw=3 | 127 ms | 19 µs/query | 0.876 | 136 KB index |
| turbovec bw=2 | 101 ms | 25 µs/query | 0.814 | 92 KB index |
| LEANN (hnsw) | **19 min 23 s** | unstable* | — | 1.2 MB index; **5.6 GB venv**, 1.5 GB RAM peak |

\* LEANN search on the librarian was unstable — one run core-dumped (`Aborted (core dumped)`), another exited 0 with no results. Not reliably benchmarkable on a 3.7 GB-RAM host.

### Conclusion — NO-GO on wiring either into kb-server (2026-05-15)

1. **Scale doesn't justify it.** At 943 vectors brute-force is 23 µs/query — already instant. turbovec's best case saves ~7 µs while *losing 8 % recall*; turbovec bw=2 is slower than brute-force. The whole embedding set is 1.4 MB — there is no memory pressure to relieve.
2. **ANN indexes are a large-corpus tool.** turbovec ("31 GB → 4 GB") and LEANN ("60 M chunks in 6 GB") pay off at 10⁵–10⁷ vectors. A sub-1 000-page wiki is 2–4 orders of magnitude below that.
3. **Architecture mismatch.** kb-server is Node; turbovec is Rust, LEANN is Python. Wiring either in requires a separate sidecar service + IPC — added moving parts and failure modes, for negative benefit at current scale.
4. **The right upgrade is already named.** When the corpus crosses ~2 000 chunks, `sqlite-vss` (a SQLite extension — stays in-process, in-Node, in the existing DB) is the low-risk path kb-server's own author flagged. ANN-via-sidecar is not.

### Trigger condition for revisiting

Re-evaluate an ANN index **only** when kb-server's `embeddings` table exceeds **~2 000 rows** — which first requires kb-server to start chunking documents (today it stores one embedding per whole document). At that point evaluate `sqlite-vss` first; turbovec/LEANN only if the corpus reaches genuinely large scale.

### Deployment-boundary note

`turbovec` and `LEANN` are installed on `cemini-librarian` (the 24/7 kb-server host), not wired into anything — staged per the rule that any wiki-serving component must live on the librarian, never the laptop (which is not always on). The laptop installs of both remain benchmark/workflow tools only.

## Snippets

```
# kb-server/src/embeddings/search.js
// Brute-force cosine similarity — works for <2000 notes.
// If vault exceeds 2000 notes, consider sqlite-vss extension for ANN search.
```

[Source: cemini-librarian:/opt/kb-server/src/embeddings/search.js, retrieved 2026-05-15]

## Dead Ends

- **LEANN as a kb-server backend** — beyond the scale mismatch, LEANN's recompute-on-search design needs the embedding model resident; on the librarian's 3.7 GB RAM its search core-dumped. Wrong tool for a small, latency-sensitive corpus.
- **turbovec as a kb-server backend** — technically clean (fast, stable, tiny index) but solves a problem kb-server does not have; wiring it in would trade exact recall for quantized recall to save microseconds.
