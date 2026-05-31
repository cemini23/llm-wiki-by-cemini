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
maturity: core
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @meta/wiki-gap-detect-cadence.md — weekly stale-claim / thin-page report; linked from daily digest
- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — script-first automation posture
- @concepts/cemini-wiki-ingest-workflow.md — four-phase pipeline overview

## Narrative

| Field | Value |
|-------|-------|
| **Cadence** | Daily (discovery only — no auto-ingest) |
| **Last run** | 2026-05-31 |
| **Script** | `bash scripts/daily_research_digest.sh` |
| **Config** | `scripts/daily_research_config.yaml` |
| **Report** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Template** | `wiki/sweeps/_daily-template.md` |

Run manually each morning or via LaunchAgent (`com.cemini.daily-research-digest`, 08:00 local).

**Workflow:** review digest → check rows → optional social pass in Cursor → ingest session.

Tier 2 arXiv sweep (`weekly_arxiv_sweep.sh`) remains weekly; this digest covers broader news/web + inbox triage.
