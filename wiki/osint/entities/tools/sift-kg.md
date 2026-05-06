---
title: sift-kg — Knowledge-Graph Builder for Document Collections (Python)
type: entity
tags: [tool, knowledge-graph, llm-extraction, osint, python, candidate-audit, kggen-derived]
keywords: [sift-kg, knowledge-graph, networkx, kggen, neurips-2025, entity-resolution, schema-discovery, kreuzberg, osint-domain-schema, librarian-alternative]
related:
  - sources/5-6-links-eval-batch.md
  - concepts/cemini-license-posture.md
  - concepts/librarian-server-architecture.md
  - entities/tools/curl-md.md
maturity: draft
created: 2026-05-06
updated: 2026-05-06
---

## Relations

- @sources/5-6-links-eval-batch.md — origin source: K32 Gemini DR eval URL 1, originally marked **UNAVAILABLE** at eval time, Exa-resolved 2026-05-06 with high-signal output
- @concepts/cemini-license-posture.md — license [TBV — likely MIT/Apache, requires verification before any adoption decision]
- @concepts/librarian-server-architecture.md — sift-kg's KG output may complement OR compete with the Karpathy LLM Wiki pattern Cemini already uses; Phase-0 audit needed
- (kb-server is the wiki serving layer per `@concepts/librarian-server-architecture.md`; sift-kg is NOT an MCP server and would not replace that role)
- @entities/tools/curl-md.md — companion ingest-pipeline candidate from same K32 batch

## Raw Concept

Python CLI tool that turns arbitrary document collections into NetworkX knowledge graphs via LLM-driven entity/relation extraction. Inspired by **KGGen** (NeurIPS 2025) by `@stochastic-sisyphus` for the pre-dedup + LLM-batching technique; sift-kg adapts these into a **human-in-the-loop** review workflow.

Originally marked **UNAVAILABLE** in K32 Gemini DR eval (HTTP error at retrieval time). Exa-rescued 2026-05-06: repo is alive at `github.com/juanceresa/sift-kg` with **453 stars** and active README. This is a meaningful project, not a phantom URL.

## Narrative

- **URL**: `https://github.com/juanceresa/sift-kg` ✓ verified via Exa 2026-05-06
- **License**: [NEEDS VERIFICATION 2026-05-06] — not stated in scraped README excerpts; must check `LICENSE` file before any adoption decision
- **Stars**: 453 (substantial; bus factor concern less acute than typical 1-maintainer K-series finds)
- **Stack**: Python CLI; NetworkX for graph data structure; Kreuzberg for text extraction (local, supports PDF/DOCX/HTML + 75 formats + optional OCR via Tesseract/EasyOCR/PaddleOCR/Google Cloud Vision)
- **LLM integration**: schema discovery + entity/relation extraction + entity-resolution proposals — provider not specified in scraped excerpts (likely OpenAI-compatible based on conventions)
- **Maturity**: 1 published HTML demos page (`https://juanceresa.github.io/sift-kg/`) + active GitHub repo

### Pipeline architecture

```
Documents (PDF, DOCX, text, HTML, 75+ formats)
       ↓
  Text Extraction (Kreuzberg, local) — with optional OCR
       ↓
  Schema Discovery (LLM designs entity/relation types from your data — or use a predefined domain)
       ↓
  Entity & Relation Extraction (LLM, using discovered or predefined schema)
       ↓
  Knowledge Graph (NetworkX, JSON)
       ↓
  Entity Resolution (LLM proposes → you review)
       ↓
  Narrative Generation (LLM)
       ↓
  Interactive Viewer (browser) / Export (GraphML, GEXF, CSV, SQLite)
```

Critical user-control feature: **"sift-kg never merges anything without your approval"** — entity-resolution outputs `merge_proposals.yaml` + `relation_review.yaml` as DRAFT, user upgrades to FINAL. Human-in-the-loop is the design.

### OSINT domain preset

Notably, sift-kg ships with three predefined domain schemas: `general`, **`osint`**, `academic`. The `osint` preset is directly aligned with this workspace's primary purpose (per `@concepts/librarian-server-architecture.md`). Users can also define custom YAML schemas.

This is the strongest fit signal in the K32 batch. Most KG-builder tools assume domain-agnostic OR academic-only scope; an OSINT-tuned schema is rare and operationally relevant.

### Architectural fit question — complement or compete?

Cemini's wiki uses the Karpathy LLM Wiki pattern: prose pages with YAML frontmatter, manual `@path` cross-links, kb-server REST API for serving. sift-kg generates a structured graph layer that:

**Complement scenario**: run sift-kg over `wiki/sources/` to extract a graph view (e.g., `output/graph_data.json`). Use it for queries Cemini's manual structure can't easily answer:
- "show all sources citing Person X across all wiki pages"
- "which entities are cited together most often"
- "find isolated subgraphs (potential domain gaps)"

**Compete scenario**: replace the manual frontmatter+`@path` cross-link convention with sift-kg's auto-extracted graph. **Risk**: lose authorial control over which entities/relations exist; LLM extraction errors propagate through the graph; no human-readable prose layer.

Recommendation if Phase-0 audit passes license check: **complement, not compete.** Run sift-kg as a parallel layer over `wiki/`; treat its `graph_data.json` as a derived analytical artifact, not a source of truth. Manual prose pages remain primary.

### Phase-0 audit checklist (per @concepts/cemini-license-posture.md)

Before any deeper integration:

1. ✅ Clone `github.com/juanceresa/sift-kg` to `/tmp/sift-kg-audit/`
2. ✅ Verify license matches the eval claim (DR didn't even reach the repo; Exa-pulled README was license-silent)
3. ✅ Check maturity signals (★/commits/last push/issues)
4. **Audit failure mode for KG-builder tool class**: hardcoded directory layout? (would kill nested `wiki/entities/<category>/` layout — see SwarmVault NO-GO + PageIndex NO-GO precedents)
5. Compare against existing Cemini coverage (kb-server REST API + manual frontmatter cross-links)
6. Decide GO / CONDITIONAL-GO / NO-GO; record in this entity page

### Open questions — to resolve via Phase-0 audit

- ⚠ License: TBV. CRITICAL prerequisite.
- ⚠ Hardcoded directory layout? (KG-builder failure mode per Cemini Phase-0 audit doctrine)
- ⚠ LLM provider compatibility: OpenAI API? DeepSeek (via `OPENAI_API_BASE` override)? Custom?
- ⚠ Cost profile: how many LLM calls per document? Schema discovery is 1 call per corpus; entity/relation extraction is N calls per chunk; entity resolution is M batched calls. Estimating costs for a 350+ page Cemini wiki corpus needs measurement.
- ⚠ Output stability: does re-running `sift extract` over the same input produce deterministic output? Or does LLM nondeterminism produce graph drift between runs?
- ⚠ Incremental ingest: README claims "graph persists across sessions and grows incrementally" — verify this works without re-extracting the whole corpus on every new document.

### Adoption status — NOT ADOPTED

Phase-0 audit deferred until either:
- Monetization-relevant signal materializes (e.g., a buyer/research outreach asks for KG-style output of the Cemini wiki), OR
- A specific OSINT-research question surfaces that the current Karpathy structure can't answer cleanly.

Until then, this entity page documents the candidacy without committing audit time.

## Snippets

### sift-kg core value proposition

> "Turn any collection of documents into a knowledge graph. Extract entities and relationships via LLM, deduplicate with your approval. Map domains, find hidden connections, spot patterns across documents — knowledge that persists and compounds, for you and your AI agents. All from the CLI." [Source: https://github.com/juanceresa/sift-kg/blob/main/README.md (retrieved 2026-05-06)]

### Human-in-the-loop entity resolution

> "When you're building a knowledge graph from family records, legal filings, or any documents where accuracy matters, you want full control over which entities get merged. sift-kg never merges anything without your approval. ... The LLM sees batches of entities (all types except DOCUMENT) and identifies ones that likely refer to the same real-world thing. ... Results go to merge_proposals.yaml (entity merges) and relation_review.yaml (variant relations), all starting as DRAFT." [Source: https://github.com/juanceresa/sift-kg/blob/main/README.md (retrieved 2026-05-06)]

### KGGen attribution (NeurIPS 2025 lineage)

> "The pre-dedup and LLM batching techniques are inspired by KGGen (NeurIPS 2025) by @stochastic-sisyphus. KGGen uses SemHash for deterministic entity deduplication and embedding-based clustering for grouping entities before LLM comparison. sift-kg adapts these into its human-in-the-loop review workflow." [Source: https://github.com/juanceresa/sift-kg/blob/main/README.md (retrieved 2026-05-06)]

## Dead Ends

- **DR eval marked sift-kg as UNAVAILABLE** — eval-time HTTP error caused complete skip. This is exactly the scenario the post-ingest Exa fallback was designed to catch. Lesson: HIGH-VALUE finds can hide behind transient eval errors; never default-trust "skipped" verdicts.
