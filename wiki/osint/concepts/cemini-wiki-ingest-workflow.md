---
title: Cemini wiki ingest workflow — four-phase discovery-to-commit pipeline
type: concept
tags: [concept, workflow, automation, ingest, wiki, k90]
keywords: [wiki-ingest, daily-digest, inbox-watcher, ingest-gates, tier-2, autoresearch]
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-07-29-formal-methods-hillel-wayne.md
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
  - sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md
  - entities/tools/metaresearcher.md
  - projects/osint-workspace/Architecture/Architecture - wiki.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/file-keep-wire-harness.md
  - entities/tools/deptry.md
  - entities/tools/typst.md
  - sources/arxiv-harness-updating-not-benefit-2605.30621.md
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - concepts/autosci-research-lifecycle-memory.md
  - sources/arxiv-neurolog-osint-handoff-2606.00669-2026-06-06.md
  - concepts/scientific-conclusion-synthesis-eval.md
  - sources/arxiv-2606-11337-sciconbench-scientific-synthesis-agents-2026-06-13.md
  - meta/macro-charts-email-ingest-cadence.md
  - concepts/computational-genealogy-archival-automation.md
  - sources/substack-rss-outlier-weekly-2026-07-14-llm-wiki-lint.md
  - sources/newsletter-rss-pragmatic-engineer-2026-07-14-what-is-loop-engineering.md
  - sources/arxiv-2607.15715-behavioral-controllability-agentic-ie.md
  - concepts/skill-regression-tax.md
  - sources/arxiv-2607.22520-regression-tax-llm-skills.md
  - sources/substack-rss-moontower-2026-07-26-slopcounterslop.md
  - entities/tools/langchain-openwiki.md
  - sources/arxiv-2607.23791-brw-cover-times.md
  - sources/newsletter-rss-sparktoro-2026-07-28-brand-affinity.md
  - sources/arxiv-2607.24663-aps-rag.md
  - sources/arxiv-2607.25620-epistemic-schizologia-llms.md
  - entities/tools/claude-real-video.md
  - entities/tools/crawl4ai.md
  - entities/tools/olmocr.md
  - entities/tools/unlimited-ocr.md
  - meta/substack-rss-ingest-cadence.md
  - sources/karpathy-llm-wiki-field-notes-png-2026-04-26.md
  - sources/llm-wiki.md
  - sources/multi-wiki-url-evaluation-2026-07-03.md
  - sources/super-audit-ai-harness-2026-09-02.md
maturity: core
created: 2026-05-31
updated: 2026-10-25
---

## Relations

- @sources/newsletter-rss-pragmatic-engineer-2026-07-29-formal-methods-hillel-wayne.md — formal methods / property-based testing note
- @sources/arxiv-2607.24663-aps-rag.md — K198 backlink

- @sources/newsletter-rss-sparktoro-2026-07-28-brand-affinity.md — K198 → seo brief

- @sources/arxiv-2607.23791-brw-cover-times.md — K198 digest false-positive

- @entities/tools/langchain-openwiki.md — K197

- @concepts/skill-regression-tax.md — K196 evaluate Cursor/MCP skill adds with before/after matrices
- @sources/arxiv-2607.22520-regression-tax-llm-skills.md — K196
- @sources/substack-rss-moontower-2026-07-26-slopcounterslop.md — K196 Pangram / counterslop publishing hygiene
- @sources/arxiv-2607.15715-behavioral-controllability-agentic-ie.md — K177 process-trace IE eval for ingest agents
- @concepts/computational-genealogy-archival-automation.md — parallel “sources before automation / no Tier-3 invention” discipline for archival digs
- @sources/substack-rss-outlier-weekly-2026-07-14-llm-wiki-lint.md — K165: contribution rate + wikilint-on-PR framing
- @sources/newsletter-rss-pragmatic-engineer-2026-07-14-what-is-loop-engineering.md — K165: loop engineering (CCC primary)
- @concepts/federated-daily-research-digest.md — K93 per-wiki digest rollout
- @concepts/monokern-compounding-research-pipeline.md — weekly NotebookLM overlay
- @meta/daily-research-digest-cadence.md — Phase 1 schedule + report path
- @meta/wiki-gap-detect-cadence.md — weekly Tier 1 gap report (linked from daily digest)
- @meta/macro-charts-email-ingest-cadence.md — Macro Charts RSS + Vincent Gmail auto-drop (Phase 2)
- @concepts/cemini-workflow-tooling-audit-2026-05-30.md — K84 gap map; Phase 1–4 closes inbox/n8n automation row
- @concepts/cemini-knowledge-application-architecture.md — wiki→prod loop after ingest
- @entities/tools/scholarquest.md — K123 agentic paper-search eval steal
- @sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md — K123 cross-wiki source
- @entities/tools/metaresearcher.md — K124 adversarial deep-research eval steal
- @sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md — K124 SEO cross-wiki source
- @projects/osint-workspace/Architecture/Architecture - wiki.md — `wiki/` module map (catalog, lint, librarian sync)
- @sources/arxiv-2607.25620-epistemic-schizologia-llms.md — epistemic practice / human gates


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
