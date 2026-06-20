---
title: Monokern compounding research pipeline — Claude + NotebookLM + Obsidian
type: concept
tags: [concept, workflow, notebooklm, obsidian, ingest, k93]
keywords: [monokern-pipeline, yt-search, notebooklm-py, skill-creator, federated-digest, compounding-memory]
related:
  - sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
  - concepts/cemini-wiki-ingest-workflow.md
  - concepts/federated-daily-research-digest.md
  - entities/tools/scholarquest.md
  - sources/arxiv-scholarquest-agentic-academic-search-2606.20235-2026-06-19.md
  - meta/daily-research-digest-cadence.md
  - entities/tools/revfactory-harness.md
  - entities/tools/world-cup-bot.md
  - concepts/autosci-research-lifecycle-memory.md
  - "@ccc-wiki/concepts/autosci-memory-centric-research-agents.md"
  - concepts/agent-memory-pipeline-eval-rubric.md
  - sources/trading-posts-compilation-17-2026-06-03.md
  - sources/arxiv-metaresearcher-deep-research-2606.19893-2026-06-20.md
  - entities/tools/metaresearcher.md
maturity: validated
created: 2026-06-01
updated: 2026-06-20
---

## Relations

- @sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md
- @concepts/cemini-wiki-ingest-workflow.md
- @concepts/federated-daily-research-digest.md
- @meta/daily-research-digest-cadence.md
- @entities/tools/scholarquest.md — K123 literature eval benchmark
- @entities/tools/metaresearcher.md — K124 adversarial deep-research eval steal

## Raw Concept

Synthesized from @monokern inbox drop (2026-06-01); operator requested inclusion in daily/weekly ingest cadence.

## Narrative

Four-layer research loop distinct from Hermes/OpenClaw parallel runtimes:

| Layer | Role | Cemini mapping |
|-------|------|----------------|
| Execution | Claude Code + skills | OSINT workspace + `.cursor/skills/` |
| Customization | Skill Creator plugin | CCC-wiki harness patterns |
| Analysis | NotebookLM via `notebooklm-py` | `.cursor/skills/notebooklm-osint-bridge/SKILL.md` |
| Memory | Obsidian vault markdown | `wiki/` git canon + optional `setup_obsidian_vault.sh` |

**Pipeline skill pattern:** one invocable command runs (1) structured source harvest, (2) NotebookLM notebook + sources, (3) analysis + optional deliverable (infographic, mindmap, audio), (4) markdown artifact to vault. Modular inputs: YouTube (`yt-dlp`), PDFs, URLs, local drops — same as inbox → librarian → ingest.

### Cadence integration

| Cadence | Use |
|---------|-----|
| **Daily** | `run_daily_research_digest.sh` — Exa papers/news → inbox; morning Cursor full ingest |
| **Weekly** | Monokern-style **deep pipeline** on 1 ROADMAP topic (10 sources → NotebookLM → 1 concept page refresh) |
| **Per-ingest** | Posts.docx / tool eval — existing cemini-wiki-ingest skill; no NotebookLM required |

Config hook: `scripts/daily_research_config.yaml` → `monokern_pipeline` block (weekly topic + deliverable default).

### Operator constraints

- NotebookLM auth is laptop-only (`notebooklm login`); never upload prod secrets.
- Human gates unchanged: takeaways discussion, license verify, prod brief GO (@concepts/cemini-wiki-ingest-workflow.md Phase 4).
- Tier 3 autonomous ingest remains **NO-GO**.

## Snippets

> "Obsidian is what turns it into something that compounds." [Source: monokern.docx via @sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01.md]
