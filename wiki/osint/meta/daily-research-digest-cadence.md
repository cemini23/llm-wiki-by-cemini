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
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - meta/federation-operator-hub-stub.md
maturity: core
created: 2026-05-31
updated: 2026-06-04
---

## Relations

- @meta/federation-operator-hub-stub.md — operator morning summary (`cemini-federation-hub`)
- @concepts/federated-daily-research-digest.md — per-wiki install kit (K93)
- @concepts/monokern-compounding-research-pipeline.md — weekly deep-research overlay
- @meta/wiki-gap-detect-cadence.md — weekly stale-claim / thin-page report; linked from daily digest
- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — script-first automation posture
- @concepts/cemini-wiki-ingest-workflow.md — four-phase pipeline overview

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily — Exa papers (wiki-deduped) → inbox PDFs + news digest (no wiki ingest) |
| **Last run** | 2026-06-11 |
| **Script** | `cemini-daily-research-digest` (or `bash scripts/run_daily_research_digest.sh` from repo) |
| **Config** | `scripts/daily_research_config.yaml` |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |

Run manually each morning or via LaunchAgent (`com.cemini.daily-research-digest`, 08:00 local).

**Launchd / macOS privacy (2026-06-04):** morning jobs use `~/bin/cemini-*` wrappers and a synced payload under `~/.cemini/launchagent/` (not executing `.py`/`.sh` paths on Desktop). Reinstall after wrapper changes: `bash scripts/reinstall_morning_launchagents.sh`. Full Disk Access on Cursor or `/bin/bash` does **not** propagate to launchd’s Python — if jobs fail while the Mac is locked/logged out, add FDA to the interpreter shown at reinstall time (usually `/Library/Developer/CommandLineTools/usr/bin/python3`). `launchctl kickstart` tests can fail even when the 08:00 calendar run succeeds.

**Workflow:** overnight fetch lands non-duplicate arXiv PDFs in inbox → morning **full ingest** in Cursor → optional news-row picks + social pass.

Tier 2 arXiv sweep (`weekly_arxiv_sweep.sh`) remains weekly; this digest covers broader news/web + inbox triage.

**Weekly overlay:** `monokern_pipeline` in `scripts/daily_research_config.yaml` — one NotebookLM-heavy research session per top ROADMAP topic (see @concepts/monokern-compounding-research-pipeline.md).

**Federation:** sibling wikis install via `scripts/federation/daily_digest/install_federated_daily_digest.sh` — @concepts/federated-daily-research-digest.md.
