---
title: Inbox arXiv reject batch — 2026-07-08 (arXiv-API fallback mis-route: RE + graphics + decomp + food + quant re-drop)
type: source
tags: [source, triage, reject, arxiv]
keywords: [arxiv, triage, reject, digest, mis-route, requirements-engineering, gaussian-splatting]
related:
  - sources/inbox-arxiv-reject-batch-2026-07-07.md
  - sources/inbox-arxiv-reject-batch-2026-07-09.md
  - sources/inbox-arxiv-reject-batch-2026-07-05.md
  - meta/cross-wiki-routing.md
  - concepts/game-dev-wiki-scope.md
  - concepts/rts-networking-deferred.md
read_status: read
source_type: operator-triage
maturity: validated
created: 2026-07-08
updated: 2026-07-08
---

## Raw Concept

Five PDFs from `2026-07-08-daily.md`. **All reject** — second consecutive day the `game-navmesh-dynamic` cluster fell back to the free arXiv API (Exa 0 hits) and fetched unrelated SE / graphics / CV / quant papers. No game-dev adoption; no Phase-0; no new brief.

## Narrative

| arXiv ID | Title (short) | Verdict | Route |
|----------|---------------|---------|-------|
| 2607.04958 | Look-Ahead-Freedom (temporal non-interference) | **Reject (re-drop)** | Quant backtesting; already rejected @sources/inbox-arxiv-reject-batch-2026-07-07.md → @osint-wiki |
| 2607.05632 | Bridging Stakeholder and Product Requirements (automotive) | **Reject** | Infineon/TUM empirical RE study on automotive SW; not castle-sim / Godot |
| 2607.05667 | Clustered Codebook Quantization for 2D Gaussian Image Compression | **Reject** | SIGGRAPH Posters 2DGS compression (NVIDIA/UCL); art-codec research — route @image-gen-wiki only if asset pipeline ever needs GaussianImage-style codecs |
| 2607.06125 | Neural Decompilation of Dart AOT Binaries | **Reject** | Softsec / reverse-engineering metrics paper; not game-dev. Softsec curiosity → @cybersecurity-wiki if wanted |
| 2607.06148 | RFHNet food image retrieval | **Reject** | Fine-grained CV hashing for food photos; out of scope |

### Notes

- **Fallback pattern (day 2):** Exa paper queries returned 0; only `game-navmesh-dynamic` used arXiv API and pulled the newest ACM/CS.SE/CV noise. Operator should treat arXiv-API-fallback rows as **guilty until abstract-verified** — same rule as 2026-07-07.
- **2607.05667** is the least-wrong graphics hit (image compression for 2D Gaussians) but castle-sim uses placeholder/isometric atlas art via @image-gen-wiki — no adoption path for a SIGGRAPH poster codec.
- News lane: 0 hits across all six clusters.

**No Phase-0 / no brief:** nothing David should adopt in castle-sim this batch.

**Action:** Archive 5 PDFs to egress; clear inbox.

## Snippets

```
python3 scripts/preingest_check.py → 5 NEW (all wiki-unknown; 04958 is re-drop of already-rejected ID)
Paper lane: game-navmesh-dynamic cluster used arXiv API fallback (Exa 0 hits) → mis-route
```

## Dead Ends

- Ingesting arXiv-API-fallback titles at face value — abstracts are automotive RE, 2DGS codecs, Dart decomp, food CV, quant SE
