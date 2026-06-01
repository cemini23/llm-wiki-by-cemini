---
title: Monokern — Claude Code + NotebookLM + Obsidian compounding research pipeline
type: source
tags: [source, workflow, notebooklm, obsidian, claude-code, monokern, k93]
keywords: [monokern, yt-pipeline, notebooklm-py, skill-creator, obsidian-vault, compounding-research]
related:
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/cemini-wiki-ingest-workflow.md
  - meta/daily-research-digest-cadence.md
  - entities/people/matias-scalbi.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
clusters: [agent-tooling, research-pipeline]
---

## Relations

- @concepts/monokern-compounding-research-pipeline.md — synthesized workflow
- @concepts/cemini-wiki-ingest-workflow.md — daily digest + inbox + ingest phases
- @meta/daily-research-digest-cadence.md — schedule for overnight fetch
- @entities/people/matias-scalbi.md — cites @monokern in Polymarket creator cluster

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Monokern post — research monster workflow |
| Author | @monokern (X) |
| Type | Social long-form / operator guide |
| Location | `research to be indexed/monokern.docx` → `cemini-librarian:/opt/cemini-bulk/research/monokern.docx` |
| sha256 | `4f3959c64b144c82…` (11,641 bytes; preingest 2026-06-01) |
| Retrieved | 2026-06-01 |
| Read | deep-read |

## Narrative

Operator-facing stack: **Claude Code** (execution) + **Skill Creator** (natural-language skill install) + **notebooklm-py** (Google-side analysis, token offload) + **Obsidian** (markdown memory that compounds). Core pattern is a **single pipeline skill** that chains source discovery → NotebookLM notebook → analysis/deliverables → vault markdown.

**Modular source layer:** YouTube via `yt-dlp` is the exemplar, not the constraint — PDFs, web pages, local files, and Drive exports swap in while the pipeline skeleton stays fixed. [CONFIRMED] aligns with Cemini's existing `notebooklm-osint-bridge` skill and wiki-as-memory doctrine.

**Compounding mechanism:** weekly `CLAUDE.md` / vault instruction updates from session patterns so outputs converge on operator style without re-prompting. [TENTATIVE] cadence claim ("once a week") is single-source.

**Fit for Cemini ingest loop:** add as optional **weekly** deep-research pass after daily Exa/inbox fetch — not a replacement for `wiki_lint` / human gates.

## Snippets

> "Combined: a research system that executes on command, analyzes at scale, and improves with use." [Source: monokern.docx]

> "The YouTube source is not the point. The pipeline structure is the point." [Source: monokern.docx]

> "Offloads heavy analysis to Google's infrastructure via NotebookLM — not your Claude tokens." [Source: monokern.docx]
