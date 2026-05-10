---
title: "public-apis — Curated Free API Directory"
type: entity
tags: [tool, api, data, discovery, reference-only, community]
keywords: [public-apis, free APIs, data discovery, API directory, community curated]
related:
  - sources/evaluating-links-trading-wiki-stacks.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-10
updated: 2026-05-10
---

## Relations
- `@sources/evaluating-links-trading-wiki-stacks.md` — source evaluation brief (URL 23)

## Raw Concept

An exhaustive, meticulously curated markdown database of free APIs across the internet. Community-maintained, categorized into Finance, Weather, Government, etc.

- **Repo**: `github.com/public-apis/public-apis`
- **License**: MIT
- **Stack**: Markdown

## Narrative

**Verdict: Reference-only.** The repository serves as a discovery mechanism for expanding Cemini's data ingestion pipelines. When the current ingestion layer (Polygon, CCXT, GDELT) needs novel alternative data feeds, cross-referencing public-apis can surface obscure but valuable sources. However, free public APIs suffer from catastrophic rate limits, unannounced downtime, and sudden deprecation — they cannot be load-bearing dependencies in 24/7 trading systems.

[Source: Evaluating Links for Trading and Wiki Stacks.docx, URL 23]
