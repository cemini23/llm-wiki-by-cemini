---
title: Federated daily research digest — per-wiki automated learning loop
type: concept
tags: [concept, meta, automation, federation, k93]
keywords: [federated-digest, daily-research, cross-wiki, launchagent, exa, inbox-watcher]
related:
  - meta/federation-operator-hub-stub.md
  - meta/daily-research-digest-cadence.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/monokern-compounding-research-pipeline.md
  - projects/osint-workspace/Architecture/Architecture - wiki.md
  - "@3d-printing-wiki/meta/daily-research-digest-cadence.md"
maturity: core
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @meta/federation-operator-hub-stub.md — **cemini-federation-hub** operator UI (morning summary)
- @meta/daily-research-digest-cadence.md — OSINT canonical implementation
- @concepts/cemini-wiki-ingest-workflow.md — Phases 1–4
- @concepts/monokern-compounding-research-pipeline.md — weekly deep-research overlay
- @projects/osint-workspace/Architecture/Architecture - wiki.md
- @3d-printing-wiki/meta/daily-research-digest-cadence.md — sibling cadence stub

## Raw Concept

Operator request 2026-06-01: replicate OSINT morning digest + inbox automation across all federation wikis so each domain wiki gets **automated discovery** without Tier 3 auto-ingest.

## Narrative

### OSINT reference stack (canonical)

| Piece | Path |
|-------|------|
| Config | `scripts/daily_research_config.yaml` |
| Runner | `scripts/daily_research_digest_run.py` |
| Wrapper | `~/bin/cemini-daily-research-digest` |
| Report | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| Inbox | `research to be indexed/` |
| Install | `bash scripts/install_workflow_launchagents.sh` |

### Per-wiki rollout pattern

Each sibling wiki gets a **copy of the script bundle** under its repo `scripts/` (from `scripts/federation/daily_digest/`) plus a **wiki-local** `daily_research_config.yaml` with domain `active_topics` + `paper_queries` / `queries`. Same human gates: digest does not write entity pages; Cursor ingest does.

| Wiki alias | Repo path (laptop) | Inbox folder | Sweep output |
|------------|-------------------|--------------|--------------|
| osint-wiki | OSINT WORKSPACE | `research to be indexed/` | `wiki/sweeps/` |
| ccc-wiki | `projects/Cemini claude code CCC` | `research to be indexed/` | `wiki/sweeps/` |
| seo-wiki | `projects/SEO:GEO B&M Business` | `research to be indexed/` | `wiki/sweeps/` |
| image-gen-wiki | `projects/Image gen` | `research to be indexed/` | `wiki/sweeps/` |
| gambling-wiki | `projects/Gambling wiki` | `research to be indexed/` | `wiki/sweeps/` |
| cybersecurity-wiki | `projects/Cybersecurity wiki` | `research to be indexed/` | `wiki/sweeps/` |
| 3d-printing-wiki | `projects/3d printing` | `research to be indexed/` | `wiki/sweeps/` | Brief on disk — operator install pending |

**LaunchAgent labels** must be unique per wiki (e.g. `com.cemini.daily-research-digest.seo`) — see federation `install_federated_daily_digest.sh`.

### Monokern overlay (weekly)

On top of daily Exa/inbox, run one **Monokern pipeline** session per wiki per week: structured sources → NotebookLM → markdown into that wiki's vault. Config: `monokern_pipeline` block in each wiki's `daily_research_config.yaml` (OSINT template in parent config).

### Federation operator hub (2026-06-01)

**Repo:** `~/Desktop/projects/cemini-federation-hub` — master triage panel (not a content wiki).

| Piece | Path |
|-------|------|
| Hub page | `hub/meta/federation-operator-hub.md` |
| Morning report | `hub/sweeps/YYYY-MM-DD-federation.md` |
| Script | `cemini-federation-morning-summary` @ 08:05 (before per-wiki digests) |

See @meta/federation-operator-hub-stub.md.

### Librarian

After each wiki commit, `rsync` + `kb ingest` on cemini-librarian (existing federation sync). OSINT does not modify `/opt/cemini` from here.

## Snippets

> "Tier 3 autonomous ingest remains NO-GO." [CONFIRMED] @concepts/cemini-wiki-ingest-workflow.md Phase 4
