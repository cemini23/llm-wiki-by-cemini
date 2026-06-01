---
title: Federation operator hub (stub → cemini-federation-hub repo)
type: concept
tags: [meta, federation, operator]
keywords: [federation-hub, master-wiki-ui, morning-summary, triage]
related:
  - concepts/federated-daily-research-digest.md
  - meta/daily-research-digest-cadence.md
maturity: core
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/federated-daily-research-digest.md — per-wiki digest pattern
- @meta/daily-research-digest-cadence.md — OSINT digest cadence

## Narrative

Canonical **operator control plane** lives in a separate repo (not in `wiki/`):

| Field | Value |
|-------|-------|
| Repo | `/Users/claudiobarone/Desktop/projects/cemini-federation-hub` |
| Hub page | `hub/meta/federation-operator-hub.md` |
| Dashboard | `hub/dashboard.md` |
| Morning report | `hub/sweeps/YYYY-MM-DD-federation.md` |

### Install

```bash
cd ~/Desktop/projects/cemini-federation-hub
bash scripts/install_federation_hub.sh
cemini-federation-morning-summary
bash scripts/setup_obsidian_vault.sh --open
```

Domain wikis stay separate; this repo aggregates inbox counts, daily sweeps, git dirty state, and pending `*from-osint*` briefs.

### Where to work (operator)

| Task | Workspace | Why |
|------|-----------|-----|
| **Drop new sources, K-batch ingest, cross-wiki routing** | **OSINT WORKSPACE** (always) | Canonical ingest ritual, `preingest_check`, `cross_wiki_route.py`, briefs staged here first |
| **Domain-only expansion** (CCC harness, SEO goaccess, …) | **Sibling wiki folder** in Cursor | Content lives in that wiki’s `wiki/`; open the brief listed in federation sweep |
| **Morning triage, backlog, git dirty across repos** | **cemini-federation-hub** | Read-only control plane — do **not** author long-form wiki pages here |
| **Query all wikis** | OSINT + lazy-tool `kb_search` / `conductor_query` | Librarian serves synced copies; federation hub does not replace kb-server |

**Rule:** Ingest and route **in OSINT**; execute routed briefs **in the target wiki**; use federation hub **once per day** (or when clearing `*from-osint*` backlog).

## Snippets

> "Separate wikis for schema; federation hub for operator attention." [CONFIRMED] design 2026-06-01
