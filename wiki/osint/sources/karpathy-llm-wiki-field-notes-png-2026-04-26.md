---
title: "LLM-WIKI.md Field Notes — Karpathy nine rules (PNG, v040426)"
type: source
tags: [karpathy, llm-wiki, schema-pattern, obsidian, k133]
keywords: [karpathy, llm-wiki, compile-not-retrieve, obsidian, claude-code, nine-rules]
related:
  - sources/llm-wiki.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/librarian-server-architecture.md
maturity: validated
read_status: read
created: 2026-06-28
updated: 2026-06-28
clusters: [llm-agents, wiki-tooling]
---

## Relations

- @sources/llm-wiki.md — canonical gist; this PNG is a formatted one-pager of the same thesis
- @concepts/cemini-wiki-ingest-workflow.md — Cemini implements rules II–VIII via CLAUDE.md + ingest ritual

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLM-WIKI.md: Field Notes on a Knowledge Base That Maintains Itself |
| **Author** | Andrej Karpathy |
| **Type** | PNG (working notes v040426 reformatted) |
| **sha256** | `a02bb5ead616ead99d5f1e6e90b1265585dab9f7102bb3869a8c98201a372cfa` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/llmwiki field notes.png` |
| **Retrieved** | 2026-06-28 (dropped 2026-06-27) |
| **Read status** | read (vision extract) |
| **Index terms** | LLM-maintained KB, Obsidian, Claude Code, markdown, compounding notes, retrieval vs compilation, second brain |

## Narrative

One-page distillation of Karpathy's **compile-don't-retrieve** wiki pattern — nine numbered rules. Maps 1:1 to this workspace's three-layer schema (`raw/` egress-fi → `wiki/` git → `CLAUDE.md`).

| # | Rule | Cemini mapping |
|---|------|----------------|
| I | Sources immutable | egress-fi bulk; never edit archived PDFs |
| II | Separate layers | raw / wiki / schema — CLAUDE.md |
| III | Model owns wiki | Agent writes pages; human drops sources + asks |
| IV | Compile don't retrieve | Ingest builds linked pages; not RAG-on-every-query |
| V | Ingest one source at a time | K-batch ritual; avoid dump imports |
| VI | Link everything | `@path` + `related:` bidirectional |
| VII | Navigate by index | `wiki/index.md` first |
| VIII | Lint the knowledge | `wiki_lint.py`, gap detect, claim tags |
| IX | Start small | Phase-0 before Adopt |

K132 skipped this PNG as unsupported; K133 ingests content via vision read.

## Snippets

> raw/ is source code, the model is the compiler, wiki/ is the executable, queries are the runtime. [Source: llmwiki field notes.png, Karpathy v040426]

> Ingest one source at a time — batch import creates a dump, not a linked wiki. [Source: llmwiki field notes.png, rule V]
