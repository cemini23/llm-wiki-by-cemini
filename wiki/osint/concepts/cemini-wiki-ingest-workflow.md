---
title: Cemini wiki ingest workflow — four-phase discovery-to-commit pipeline
type: concept
tags: [concept, workflow, automation, ingest, wiki, k90]
keywords: [wiki-ingest, daily-digest, inbox-watcher, ingest-gates, tier-2, autoresearch]
related:
  - concepts/federated-daily-research-digest.md
  - concepts/monokern-compounding-research-pipeline.md
  - concepts/active-project-research-routing.md
  - meta/daily-research-digest-cadence.md
  - meta/wiki-gap-detect-cadence.md
  - concepts/cemini-workflow-tooling-audit-2026-05-30.md
  - concepts/cemini-knowledge-application-architecture.md
  - concepts/high-signal-paper-patterns.md
  - entities/tools/scholarquest.md
  - sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md
  - projects/osint-workspace/Architecture/Architecture - wiki.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - entities/tools/deptry.md
  - entities/tools/typst.md
  - sources/arxiv-harness-updating-not-benefit-2605.30621.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - concepts/autosci-research-lifecycle-memory.md
  - sources/arxiv-neurolog-osint-handoff-2606.00669-2026-06-06.md
  - concepts/scientific-conclusion-synthesis-eval.md
  - sources/arxiv-2606-11337-sciconbench-scientific-synthesis-agents-2026-06-13.md
maturity: core
created: 2026-05-31
updated: 2026-06-13
---

## Relations

- @concepts/federated-daily-research-digest.md — K93 per-wiki digest rollout
- @concepts/monokern-compounding-research-pipeline.md — weekly NotebookLM overlay
- @meta/daily-research-digest-cadence.md — Phase 1 schedule + report path
- @meta/wiki-gap-detect-cadence.md — weekly Tier 1 gap report (linked from daily digest)
- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — K84 gap map; Phase 1–4 closes inbox/n8n automation row
- @concepts/cemini-knowledge-application-architecture.md — wiki→prod loop after ingest
- @entities/tools/scholarquest.md — K123 agentic paper-search eval steal
- @projects/osint-workspace/Architecture/Architecture - wiki.md — `wiki/` module map (catalog, lint, librarian sync)

## Raw Concept

Operator request (2026-05-31): automate the daily loop — search social/web → analyze → ingest wiki — without adopting Hermes/OpenClaw parallel runtimes. Implemented as four phases on existing Conductor/librarian/Cursor stack.

## Narrative

### Phase 1 — Morning digest (automated discovery)

**Scripts:** `run_daily_research_digest.sh` · `check_daily_research_digest_due.sh` · LaunchAgent `com.cemini.daily-research-digest` @ 08:00.

Exa paper queries (7d, wiki-deduped) download new arXiv PDFs to `research to be indexed/`; news queries fill `wiki/sweeps/YYYY-MM-DD-daily.md`. Does **not** write wiki pages — morning **full ingest** does.

### Phase 2 — Inbox watcher

**Scripts:** `inbox_notify.sh` · `append_inbox_to_daily_sweep.py` · LaunchAgent WatchPaths on `research to be indexed/`.

On drop: preingest → update today's sweep → tool-eval license spot-check → macOS notification.

### Phase 3 — Ingest assistant (Cursor skill)

**Skill:** `.cursor/skills/cemini-wiki-ingest/SKILL.md` — Posts.docx, tool eval v5, daily sweep rows, K-batch checklist.

Ends with `wiki_lint.py` + `ingest_session_gate.py` before commit.

### Phase 4 — Human gates (never automate)

**Rule:** `.cursor/rules/osint-ingest-gates.mdc` — takeaways discussion, license re-verify, cross-wiki routing, prod brief GO, no Tier 3 autonomous ingest.

**Mechanical helper:** `scripts/ingest_session_gate.py` — log.md date, index rows, stale NEEDS VERIFICATION, tool license anchors.

### Daily operator loop

1. Review `wiki/sweeps/YYYY-MM-DD-daily.md` (or run digest if missing)
2. Pick rows + optional social pass (twitter/opencli in Cursor)
3. Ingest session with cemini-wiki-ingest skill
4. `ingest_session_gate.py` → commit → librarian sync → ROADMAP + briefs

### Weekly Monokern pass (optional)

After daily digest + inbox ingests, one session on `monokern_pipeline.active_topic` — YouTube/PDF/URL → NotebookLM → markdown into wiki/Obsidian. See @concepts/monokern-compounding-research-pipeline.md. **Not** a substitute for Phase 4 human gates.
