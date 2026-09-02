---
title: Daily research digest cadence
type: concept
tags: [meta, wiki, automation, discovery, k90]
keywords: [daily-research-digest, exa, sweep, discovery, ingest-pipeline]
related:
  - meta/wiki-gap-detect-cadence.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - concepts/high-signal-paper-patterns.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/active-project-research-routing.md
  - entities/tools/wc-ticket-monitor.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - meta/federation-operator-hub-stub.md
  - meta/launchagent-health.md
maturity: core
created: 2026-05-31
updated: 2026-09-02
---

## Relations

- @meta/federation-operator-hub-stub.md — operator morning summary (`cemini-federation-hub`)
- @concepts/federated-daily-research-digest.md — per-wiki install kit (K93)
- @concepts/monokern-compounding-research-pipeline.md — weekly deep-research overlay
  - @concepts/active-project-research-routing.md — brief targets: **Atto** #1 · **GuruWatcher** #2 · behind: poker, ceminidfs, xsp-killer, family-tree dogfood, **local-abliterated-lab**; TipDrop retired 2026-08-05
- @entities/tools/wc-ticket-monitor.md — portfolio repo (knockout ticket resale alerts)
- @meta/wiki-gap-detect-cadence.md — weekly stale-claim / thin-page report; linked from daily digest
- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — script-first automation posture
- @concepts/cemini-wiki-ingest-workflow.md — four-phase pipeline overview

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily — **free arXiv** paper lane (wiki-deduped) → inbox PDFs; Exa news **off** by default |
| **Last run** | 2026-09-02 |
| **Script** | `cemini-daily-research-digest` (or `bash scripts/run_daily_research_digest.sh` from repo) |
| **Config** | `scripts/daily_research_config.yaml` (`exa.paper_mode`, `exa.news_enabled`) |
| **LaunchAgents** | OSINT `@08:00`; sibling wikis `@08:10+` (+3min stagger); federation summary after last sibling (`reinstall_morning_launchagents.sh`). Wrappers prefer `${WIKI_ROOT}/scripts/daily_research_digest_run.py`; frozen `~/.cemini/launchagent/osint/` is fallback. |
| **wiki-sync-verify** | **Disabled** (cemini-librarian decommissioned 2026-06-14) |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |

Run manually each morning or via LaunchAgent (`com.cemini.daily-research-digest`, 08:00 local).

### Exa cost control (2026-07-15)

Exa search is pay-per-use (~$7/1k requests). Federation default after free credits:

| Knob | Default | Effect |
|------|---------|--------|
| `exa.paper_mode` | `arxiv-only` | Paper discovery via free Atom API — **0 Exa paper calls** |
| `exa.news_enabled` | `false` | Skip digest-only news Exa (news never auto-fetches PDFs) |
| `exa.include_domains` | `[arxiv.org]` | When Exa is re-enabled for papers, only bill for arXiv hits |
| `exa.search_type` | `auto` | Never `deep` / `deep-reasoning` for digest |
| `loop.recency_window_days` | `14` | Lookback for discovery; fetch still wiki-dedupes (3d starved Atom keyword search) |
| `fetch.max_results_per_paper_query` | `3` | Fewer candidates per cluster |
| `paper_queries[].arxiv_query` | Atom syntax | **Required for reliable free mornings** — NL `query` alone is too AND-heavy |

To spend Exa again on papers: set `paper_mode: arxiv-first` (Exa only when arXiv empty) or `exa-first` (legacy). To resume news: `news_enabled: true`.

**Why free failed before (2026-07):** Exa NL queries were AND-mapped into 6 Atom terms inside a short window → 0 hits most mornings. Fix: explicit `arxiv_query` + looser NL mapper + 14d window + over-fetch-then-date-filter.
**Launchd / macOS privacy (2026-06-04):** morning jobs use `~/bin/cemini-*` wrappers and a synced payload under `~/.cemini/launchagent/` (not executing `.py`/`.sh` paths on Desktop). Reinstall after wrapper changes: `bash scripts/reinstall_morning_launchagents.sh`. Full Disk Access on Cursor or `/bin/bash` does **not** propagate to launchd’s Python — if jobs fail while the Mac is locked/logged out, add FDA to the interpreter shown at reinstall time (usually `/Library/Developer/CommandLineTools/usr/bin/python3`). `launchctl kickstart` tests can fail even when the 08:00 calendar run succeeds.

**Workflow:** overnight fetch lands non-duplicate arXiv PDFs in inbox → morning **full ingest** in Cursor → briefs route per `scripts/active_project_brief_targets.yaml` (not default legacy CeminiSuite prod).

Tier 2 arXiv sweep (`weekly_arxiv_sweep.sh`) remains weekly; this digest covers paper inbox triage (Exa news optional).

**Weekly overlay:** `monokern_pipeline` in `scripts/daily_research_config.yaml` — one NotebookLM-heavy research session per top ROADMAP topic (see @concepts/monokern-compounding-research-pipeline.md).

**Federation:** sibling wikis install via `scripts/federation/daily_digest/install_federated_daily_digest.sh` — @concepts/federated-daily-research-digest.md.
