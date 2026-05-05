---
title: Kalshi llms.txt — Official LLM-Readable API Documentation
type: entity
tags: [reference, prediction-markets, kalshi, llms-txt, documentation, adopt-tier]
keywords: [kalshi-api, llms-txt, llm-readable-docs, kalshi-developer-documentation, wiki-layer-ingest]
related:
  - sources/5-5-links-2-tool-eval.md
  - entities/platforms/kalshi.md
  - entities/tools/pykalshi.md
  - concepts/kalshi-api-reference.md
maturity: validated
created: 2026-05-05
updated: 2026-05-05
---

## Relations

- @sources/5-5-links-2-tool-eval.md — origin source: 2026-05-05 Gemini DR eval, URL 26, **Adopt** tier (ingest llms.txt into wiki for LLM-readable Kalshi reference)
- @entities/platforms/kalshi.md — Kalshi venue entity; this is its canonical developer docs in LLM-friendly form
- @entities/tools/pykalshi.md — companion Adopt-tier (the high-performance Python client uses this API)

## Raw Concept

Kalshi publishes an `llms.txt`-formatted version of their developer documentation explicitly designed for LLM consumption. K30 Gemini DR eval (URL 26) recommends ingesting it into Cemini's wiki layer.

## Narrative

- **URL**: kalshi.com/docs/llms.txt (typical convention; verify exact path)
- **License**: Proprietary (Kalshi Terms of Service / Developer Terms)
- **Format**: `llms.txt` — a markdown-with-structure format that LLMs can parse directly without HTML scraping

### Why Adopt for Cemini's wiki layer

Per K30 eval URL 26: "ingest the llms.txt." The action is clean:

1. Periodically `curl kalshi.com/docs/llms.txt > wiki/concepts/kalshi-api-reference.md` (or similar)
2. Wrap with our wiki frontmatter + attribution to Kalshi
3. kb-server indexes it; the brain can query Kalshi-specific endpoints without scraping HTML or referring to stale training data
4. Refresh monthly (or on the user's signal that Kalshi shipped new docs)

This is cheaper than scraping and more reliable than relying on the model's training cut-off. Kalshi explicitly publishes llms.txt for this purpose.

### License posture

Kalshi's Developer Terms (proprietary) govern reuse of API documentation. For internal Cemini use (wiki ingestion → kb-server retrieval → DeepSeek brain queries), the use is **internal reference**, not redistribution. Standard for any vendor docs.

If Cemini ever distributes its wiki externally, ingested Kalshi docs need to either be excluded or the relevant Kalshi terms followed. The wiki-share zip refresh from K28 already excludes anything sensitive; this would join that pattern.

### Adoption status — INGESTED 2026-05-05

Resolved questions (initial Phase 0):
- **URL**: `https://docs.kalshi.com/llms.txt` (verified, HTTP 200, 33 KB)
- **File size**: 33,256 bytes — well within kb-server's normal page-size envelope; no chunking required
- **Format**: markdown index of ~150 endpoints across 18 categories (account, api-keys, communications, events, exchange, fcm, historical, incentives, live-data, market, milestone, multivariate, etc.) + WebSocket channels + OpenAPI/AsyncAPI spec links
- **License posture**: Proprietary (Kalshi Developer Terms). Internal Cemini reference use is standard fair-use of vendor API docs; no redistribution. Wiki-share-zip pattern excludes this page if/when redistribution context emerges.

Wiki ingestion (deployed):
- Page: `@concepts/kalshi-api-reference.md` (validated maturity, ~37 KB including frontmatter + refresh procedure)
- kb-server picks up the new page on next sync cycle (hourly cron per `scripts/sync_wiki_to_librarian.sh`)
- Refresh cadence documented inline in the synthesis page (manual / on-trigger / future-monthly-cron)

Open question [NEEDS VERIFICATION 2026-05-05]:
- Whether Kalshi version-stamps the file (no version header observed in 2026-05-05 snapshot — refreshes will be by-content-hash, not by-version)

## Snippets

- **Adopt-tier framing** (K30 eval URL 26): "Ingest the llms.txt — this serves as the official developer documentation for the Kalshi Exchange API." [Source: 5_5 links 2.docx URL 26]

- **License**: "Proprietary (Terms of Service / Developer Terms)" [Source: 5_5 links 2.docx URL 26]
