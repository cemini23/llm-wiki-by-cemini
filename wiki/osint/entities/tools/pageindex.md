---
title: PageIndex — Vectorless Reasoning-Based RAG (MIT)
type: entity
tags: [tool, rag, knowledge-base, mit, adopt-tier, librarian-candidate, vectorless-retrieval]
keywords: [pageindex, vectorless-rag, reasoning-based-retrieval, kb-server-alternative, librarian-supplement]
related:
  - sources/5-5-links-tool-eval.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/librarian-server-architecture.md
  - entities/tools/swarmvault.md
maturity: draft
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 13, **Adopt** tier
- @concepts/wiki-tooling-evaluation.md — PageIndex joins the candidate list for the wiki retrieval layer alongside kb-server (current production), llm-wiki-compiler (deployment-blocked at v0.4.0), and SwarmVault (NO-GO per K28)
- @concepts/librarian-server-architecture.md — librarian server hosts the retrieval layer; PageIndex would be a Phase-N extension or replacement candidate
- @entities/tools/swarmvault.md — prior K28 candidate with NO-GO verdict; the lesson (audit path-resolution before adopting) applies to PageIndex too

## Raw Concept

Vectorless reasoning-based Retrieval-Augmented Generation system. MIT-licensed. Adopt-tier verdict in K30 5_5-links batch — most architecturally interesting Adopt of that batch.

## Narrative

- **URL**: per K30 eval URL 13 (verify exact GitHub path)
- **License**: MIT
- **Stack**: per eval, "vectorless" implies no embeddings layer
- **Maturity**: needs Phase 0 audit

### Why interesting for Cemini

Cemini's deployed retrieval is kb-server (REST + FTS) + Ollama nomic-embed-text (embedding similarity for semantic search) on the librarian server (CPX21, ~2.6 GB headroom). PageIndex's vectorless approach would, if it works, **eliminate the embedding-store overhead** while still delivering retrieval quality via reasoning.

Possible roles:
1. **Replace kb-server** — too aggressive; kb-server works and is stable
2. **Supplement kb-server for reasoning queries** — when a query benefits from reasoning over the wiki structure (vs flat keyword/embedding matches), route through PageIndex; route simpler queries through kb-server
3. **Standalone evaluation** — set up PageIndex on the librarian as a parallel retrieval surface, A/B vs kb-server on the same wiki content

### Phase 0 audit (gates everything)

Per K28 SwarmVault lessons, the highest-priority audit question is:

**Does PageIndex assume a specific directory layout?**

Cemini's wiki has nested entity subdirectories (`entities/tools/`, `entities/tickers/`, etc. — 99 nested files across 10 subdirs per K28 audit). If PageIndex hardcodes a flat layout the way SwarmVault and llm-wiki-compiler do, the same NO-GO verdict applies.

Other Phase 0 questions:
- Does it parse our `@path/to/page.md` cross-link syntax?
- Does it respect frontmatter `related:` semantics?
- What's the runtime cost on the CPX21 RAM envelope?
- License: confirm MIT in the LICENSE file (eval claim)
- Maturity: stars, commits, version

### Adoption path

1. Phase 0 — Source audit (Explore agent, ~30 min): clone repo, inspect path-resolution + frontmatter + cross-link semantics. Same template as K28 SwarmVault audit.
2. Phase 1 — Smoke test on a copy of the wiki (laptop side)
3. Phase 2 — Side-by-side deployment on librarian, compare retrieval quality vs kb-server
4. Phase 3 — Promote (replace kb-server, supplement, or shelve)

### Open questions [NEEDS VERIFICATION 2026-05-05]

- All Phase 0 questions above
- "Vectorless" specifics: how does it handle semantic-similarity queries without embeddings? What's the reasoning mechanism?
- Token cost per query (if it uses an LLM at retrieval time, this is now an expensive component vs static FTS)
- Whether the reasoning-based approach scales to the wiki's ~510 pages

## Snippets

- **Vectorless framing** (K30 eval): "vectorless, reasoning-based Retrieval-Augmented Generation (RAG) system developed explicitly to circumvent the standard pgvector/embeddings layer." [Source: 5_5 links.docx URL 13]

- **Recommendation tier**: "Adopt. PageIndex should b[e adopted]." [Source: 5_5 links.docx URL 13]

## Dead Ends

*(none yet — Phase 0 audit pending.)*
