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
maturity: validated
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

### Phase 0 audit — completed 2026-05-05, verdict NO-GO

Cloned `https://github.com/VectifyAI/PageIndex` to `/tmp/pageindex-audit/`. Eval claim accurate: MIT licensed, vectorless reasoning-based RAG. Eight load-bearing questions answered:

| # | Question | Verdict | Evidence |
|---|----------|---------|----------|
| Q1 | Supports nested wiki directory layout? | **FAIL** | PageIndex operates on **single files only**. `pageindex/page_index.py:1113` accepts a single `pdf_path` or `md_path`. `PageIndexClient.index(file_path)` (`client.py:55-130`) takes one file. **No directory walking, glob, or batch API**. Cemini's 530+ wiki pages + 99 nested entity files would require 600+ separate index instances + a registry layer to track them. The K28 SwarmVault failure mode (hardcoded dir names) doesn't apply here — the use-case mismatch is *worse*: PageIndex is designed for individual long-form documents (financial PDFs, legal docs), not flat knowledge-base wikis. |
| Q2 | Retrieval cost profile | **EXPENSIVE** | **Agentic reasoning at query time**, not FTS or embedding similarity. Per query: agent uses `get_document_structure()` to reason over the index tree, then auto-calls `get_page_content(pages="N-M")`. 2-4 LLM calls per query. Estimate: **~$0.001-0.005/query at GPT-4o mini rates, multi-second latency**. Cemini's kb-server is sub-100ms FTS at zero LLM cost — PageIndex inverts that economics. Provider-agnostic via `litellm==1.83.7`; no vector-DB/embedding overhead, but trades that for agent-reasoning cost. |
| Q3 | License + maturity | **MIT confirmed; bus-factor concerns** | LICENSE is MIT ✓. Single commit (`dcda565`) in shallow clone — shallow git history suggests recent repo OR force-pushed main. No release tags visible. Backed by VectifyAI commercial vendor (pageindex.ai SaaS), but the OSS repo itself looks early-stage. Production-ready claim ("98.7% on FinanceBench") refers to VectifyAI's Mafin 2.5 *product*, not the open-source library directly. |
| Q4 | Integration interface | **Python library only** | No REST API in OSS repo. Integration via `from pageindex import PageIndexClient`. Cemini would need a Flask-style wrapper service (similar shape to kb-server). VectifyAI offers a hosted API + MCP via their CloudService, but that's out-of-scope for this audit (separate licensing + dependency on third-party SaaS). |
| Q5 | Cross-link syntax (`@path`) | **NO SUPPORT** | Markdown indexing (`page_index_md.py:32-43`) treats markdown as pure hierarchical heading-based text. No special handling for `@path/to/page.md`, `[[wikilinks]]`, or `[text](path)` graph edges. **Cemini's 3,400+ `@path` cross-links would be indexed as plain text, not traversable relationships**. The wiki graph topology is lost. |
| Q6 | Frontmatter handling | **NO PARSING** | YAML frontmatter not parsed as metadata. Title extracted from H1; doc_name/doc_description generated. **Cemini's `type`/`tags`/`keywords`/`related[]`/`maturity`/`created`/`updated` fields would be indexed as plain text** within document body, not exposed as filterable metadata. Queries can't filter by `type: entity` or `maturity: draft`. |
| Q7 | Resource envelope | **Fits CPX21 RAM but expensive runtime** | LiteLLM + PyPDF2 + pyyaml deps; low RAM at idle. Tree-structure JSON in memory at index time. Fits Cemini's CPX21 envelope BUT operational cost is the binding constraint, not RAM — see Q2. |
| Q8 | Marginal value vs kb-server | **NEGATIVE** | kb-server: sub-100ms FTS, zero LLM cost, REST API, flat directory walking, integrated. PageIndex: better for long-form professional documents (long PDFs, legal docs); breaks Cemini's fast-cheap-flat constraint. Wiki articles average 2-10 KB / 100-500 tokens — exactly the size class where FTS wins and reasoning-based retrieval is overkill. |

### NO-GO reasoning

Four disqualifying findings, any one of which would alone be sufficient:

1. **Q1 (single-file API)** — PageIndex requires 600+ separate index instances for Cemini's wiki, with a custom registry layer to map queries to instances. kb-server handles all 530+ pages with one flat index.
2. **Q2 (agentic cost per query)** — kb-server queries are sub-100ms / $0. PageIndex queries are ~2-4s / ~$0.001-0.005. At Cemini's expected query volume (100s/day), the operational-cost story changes fundamentally without proportional retrieval-quality gain on the wiki's content type.
3. **Q5 + Q6 (lost graph + lost metadata)** — Cemini's wiki **is** a graph (3,400+ cross-links) and **uses** structured metadata (`type`, `maturity`, etc. for filter queries). PageIndex throws both away.
4. **Q8 (use-case mismatch)** — PageIndex is built for long-form professional document QA. Cemini's wiki is a flat knowledge base of small articles. Wrong tool for the job.

### When PageIndex re-enters consideration

PageIndex is **not generically rejected**; it's rejected for *Cemini's wiki layer*. The pattern is:

> **PageIndex becomes a candidate ONLY IF Cemini begins indexing long-form professional documents (financial filings, legal PDFs, multi-hundred-page research papers) as a *separate* retrieval tier alongside the wiki.**

Specific re-evaluation triggers:
- If Cemini ingests SEC EDGAR 10-K/10-Q filings as a queryable corpus (the FinanceBench use case)
- If Cemini ingests legal documents (CFTC ANPRM filings, court orders, etc.) as a queryable corpus distinct from wiki concept pages
- If Cemini's research-corpus PDFs (`cemini-librarian:/opt/cemini-bulk/research/`) move from "occasionally read" to "frequently queried"

Until one of those triggers, PageIndex stays shelved.

### Adoption path (DEFERRED — see above)

If a future re-evaluation triggers:

1. Phase 0+ — re-clone, check for OSS API additions, retry above questions in the new context (long-form docs, NOT wiki)
2. Phase 1 — Pilot on 5-10 representative long-form documents
3. Phase 2 — Side-by-side cost/quality vs alternatives (Anthropic Files API, RAGFlow, LightRAG, etc.)
4. Phase 3 — Decision

### What we keep from this audit

- This entity page documents the verdict so future Gemini DR sweeps don't re-evaluate PageIndex for the wiki layer (at the entity-page granularity)
- The ROADMAP item #11 closes with explicit reasoning — the same as how K28 SwarmVault closed
- `concepts/wiki-tooling-evaluation.md` candidate landscape table now has PageIndex marked NO-GO alongside SwarmVault NO-GO (added in K30 batch 2)
- Cleanup: `/tmp/pageindex-audit/` left intact for user inspection

## Snippets

- **Vectorless framing** (K30 eval): "vectorless, reasoning-based Retrieval-Augmented Generation (RAG) system developed explicitly to circumvent the standard pgvector/embeddings layer." [Source: 5_5 links.docx URL 13]

- **Recommendation tier**: "Adopt. PageIndex should b[e adopted]." [Source: 5_5 links.docx URL 13]

## Dead Ends

*(none yet — Phase 0 audit pending.)*
