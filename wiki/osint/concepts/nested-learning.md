---
title: "Nested Learning (Behrouz et al, NeurIPS 2025) — OSINT-side stub"
type: concept
tags: [concept, stub, ml-research, nested-learning, hope-architecture, multi-timescale-memory, cross-wiki-pointer]
keywords: [nested-learning, hope-architecture, continuum-memory-system, update-frequency, stub-cross-wiki-ccc]
related:
  - sources/nl-nested-learning-behrouz-neurips2025.md
  - "@ccc-wiki/concepts/nested-learning.md"
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @sources/nl-nested-learning-behrouz-neurips2025.md — the paper source page (lives in osint-wiki)
- `@ccc-wiki/concepts/nested-learning.md` — **primary concept page** lives in ccc-wiki

## Raw Concept

What this stub does: OSINT-side cross-reference for the Nested Learning paper. The substantive concept page lives in ccc-wiki because the paper is fundamentally about agent / memory architecture (the meta-wiki domain), not financial research.

## Narrative

This stub exists for two reasons:

1. **Source page anchor** — the paper's source page (`@sources/nl-nested-learning-behrouz-neurips2025.md`) is filed under osint-wiki/sources because the raw PDF dropped into this workspace's inbox. The source page needs a concept relation for index discoverability.
2. **Cross-wiki pointer** — when an osint-wiki context (RL-for-trading, multi-timescale memory in trading agents) touches Nested Learning, the lookup path should resolve here before forwarding to ccc-wiki.

For the substantive content — Definitions of Update Frequency, Hope architecture, Continuum Memory System, M3 optimizer, empirical results — see `@ccc-wiki/concepts/nested-learning.md`.

### Brief synopsis

ML models are nested associative memory systems with per-level optimization at multi-timescale frequencies. Each level updates at a different "Update Frequency." The paper's primary architectural contribution — **Hope** — combines self-modifying Titans (DGD with weight decay) + Continuum Memory System (chain of MLPs at progressively longer chunk sizes) + M3 optimizer (Adam + Muon + CMS). Empirical wins: RULER NIAH 100% at 16K, BABILong 10M context retention, language modeling 58.04 avg vs Transformer++ 53.38.

### Why ccc-wiki, not osint-wiki

- Cemini's Conductor + librarian + memory-graph architecture is itself a multi-timescale memory system. The Hope/CMS frame is the cleanest existing-literature anchor for that pattern.
- The osint-wiki contribution from the paper is **possible-future-not-current** — RL-for-trading agents may eventually use multi-timescale memory primitives, but no current Cemini Polymarket / OSINT workflow needs Hope.

## Snippets

(See `@sources/nl-nested-learning-behrouz-neurips2025.md` for paper snippets.)
