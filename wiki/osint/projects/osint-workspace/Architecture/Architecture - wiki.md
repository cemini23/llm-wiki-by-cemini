---
title: Architecture — wiki module
type: architecture-module
date: 2026-06-01
updated: 2026-06-01
project: "[[projects/osint-workspace/OSINT Workspace]]"
module: wiki
path: wiki/
scanned-commit: b960aae
tags: [architecture, wiki, knowledge-base]
ai-first: true
related:
  - projects/osint-workspace/Architecture/Architecture - Overview.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/librarian-server-architecture.md
  - concepts/federated-daily-research-digest.md
maturity: core
---

## Relations

- @projects/osint-workspace/Architecture/Architecture - Overview.md
- @concepts/cemini-wiki-ingest-workflow.md — ingest ritual
- @concepts/librarian-server-architecture.md — serving copy + kb-server

## For future Claude

The **`wiki/`** tree is the **canonical git knowledge library** (~1.3k pages): YAML frontmatter, `@path` cross-links, `index.md` catalog, `log.md` chronology. Obsidian vault root (`wiki/.obsidian/`). Synced hourly to librarian for MCP RAG. Scan counted 3 “source files” under `wiki/` (automation/metadata only); body is almost entirely Markdown pages.

<!-- @generated:start -->

## Responsibility

**Curated, interlinked research memory** for OSINT + quant finance + Cemini internal ops. Humans and agents read/write here; raw PDFs remain on librarian bulk storage with **source pages** pointing at canonical filenames.

## Layout (top-level)

| Directory | Purpose |
| --- | --- |
| `sources/` | One page per ingested source |
| `entities/` | Tickers, companies, people, tools, infrastructure |
| `concepts/` | Topics, methodologies, theses |
| `sweeps/` | Tier-2 arXiv / daily digest outputs |
| `meta/` | Cadence docs, backtest schedules |
| `projects/` | Codebase hubs + architecture (this tree) |
| `index.md` | Content catalog — read first on query |
| `log.md` | Append-only ingest/query log |
| `_CLAUDE.md` | Vault operating manual (Cemini overrides for obsidian-second-brain) |

## Page contract

Defined in repo root `CLAUDE.md`: frontmatter (`type`, `maturity`, `related`, dates), sections (`## Relations`, `## Raw Concept`, `## Narrative`, …), citation tags, confidence tags. **Bidirectional `related:`** required.

## Serving path

1. Author on laptop `wiki/`
2. `scripts/sync_wiki_to_librarian.sh` → `cemini-librarian:/opt/cemini-wiki/wiki/`
3. kb-server reindex → MCP tools (`kb_search`, lazy-tool proxy)

Laptop powered off does **not** stop serving; last sync remains live.

## Tooling

- `scripts/wiki_lint.py` — orphans, bidirectional gaps, dangling `@path`, stale verification tags
- `scripts/wiki_gap_detect.py` — Tier-1 gap candidates (user-gated Exa)
- Obsidian graph ritual: `.cursor/skills/cemini-wiki-graph/SKILL.md`

## Role in the whole

Central **librarian layer** between immutable bulk sources and prod **briefs**. Federation with sibling wikis via `@wiki-alias/path` (image-gen, seo, gambling, ccc, etc.).

<!-- @generated:end -->
