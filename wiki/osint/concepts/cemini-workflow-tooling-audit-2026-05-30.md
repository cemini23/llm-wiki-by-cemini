---
title: Cemini workflow tooling audit (Obsidian, n8n, automation gap map)
type: concept
tags: [concept, workflow, obsidian, n8n, automation, audit, k84]
keywords: [workflow-audit, kepano-obsidian-skills, claude-obsidian, n8n-workflows, lazy-tool, stash, notebooklm]
related:
  - sources/kepano-obsidian-skills.md
  - sources/agriciDaniel-claude-obsidian.md
  - entities/tools/obsidian-llm-wiki-local.md
  - entities/tools/n8n-workflows.md
  - concepts/librarian-server-architecture.md
  - concepts/mcp-tool-marketplace.md
  - entities/tools/world-cup-bot.md
  - sources/multi-wiki-tool-eval-v4-k84-2026-05-30.md
  - entities/tools/lazy-tool.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-05-30
updated: 2026-05-30
---

## Relations

- @entities/tools/n8n-workflows.md — K42 Adopt; workflow audit recommends script-first before n8n host
- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — K84 per-team LP safety verdicts (time-volatile)
- @sources/kepano-obsidian-skills.md — Workflow-Adopt; **not installed** on laptop `.claude/skills`
- @sources/agriciDaniel-claude-obsidian.md — Steal-from visual Karpathy pattern; partial overlap with git wiki

## Raw Concept

K84 session audit: we have **deep wiki coverage** of Obsidian + n8n + MCP automation but **under-deploy** them relative to ingested knowledge. Goal: map gaps before world-cup-bot public launch (2026-06-03 Issue 3) and v5 eval prompt refresh.

## Narrative

### What we use well today [CONFIRMED]

| Layer | Tool | Role |
|-------|------|------|
| Wiki canon | Git `wiki/` + kb-server | Authoritative; hourly librarian sync |
| Agent MCP | lazy-tool → conductor/kb/prod-mcp | Default research path |
| Memory | stash (global MCP) | Episodic goals/hypotheses |
| Lint/ingest | wiki_lint, preingest_check, skill_audit | Mechanical health |
| Prod boundary | briefs → scp | No laptop→prod code edits |

### Obsidian — ingested but underused

**In wiki:** kepano/obsidian-skills (MIT), agriciDaniel/claude-obsidian (Steal-from), obsidian-llm-wiki-local (Steal-from lint patterns), Eugeniughelbur second-brain workflow.

**Gap:** Laptop authoring is **plain git + Cursor**, not an Obsidian vault overlay. Missing:

1. **kepano-obsidian-skills** install — `npx skills add git@github.com:kepano/obsidian-skills.git` → reduces frontmatter/wikilink hallucination on ingest
2. **Visual graph layer** — claude-obsidian `/wiki` `/save` for operator review (optional; kb-server remains serve path)
3. **Bidirectional wikilink UX** — we use `@path` in markdown; Obsidian graph would help orphan/backlink review pre-commit

**Recommendation:** CONDITIONAL-GO — install kepano skills on laptop only; pilot one vault mirror of `wiki/` read-only for human curation sessions (no second canonical).

### n8n / workflow automation — catalogued, not integrated

**In wiki:** `@entities/tools/n8n-workflows.md` (54k★ MIT script library + AI-BOM scanner); n8n-mcp referenced in K55 ridark brief (CCC).

**Gap:** No n8n instance in Cemini stack. Ingest still **manual**: drop → preingest → agent session → scp librarian.

**High-value automations to evaluate:**

| Workflow | Trigger | Action | Owner |
|----------|---------|--------|-------|
| Inbox watcher | File lands in `research to be indexed/` | Slack/webhook + preingest_check JSON | Laptop or librarian |
| Wiki sync verify | post-commit | ssh verify librarian mtime + kb ingest hook | librarian cron extension |
| WC safety refresh | cron weekly pre-Cup | Re-run Gemini LP safety template | world-cup-bot operator |
| License spot-check | post tool-eval docx | `gh api` batch → markdown appendix | CI script (no n8n required) |

**Recommendation:** **Script-first** (`scripts/` + LaunchAgent) before n8n — matches deployment boundary. Revisit n8n if non-dev operators need GUI workflow editing. Steal **AI-BOM scanner heuristics** from n8n-workflows for prod MCP audit without hosting n8n.

### Tooling we should use more (already available)

| Tool | Current | Should |
|------|---------|--------|
| **NotebookLM** | Skill exists; bridge skill K69 | Podcast/Q&A for large briefs pre-prod handoff |
| **stash** | Session goals | Persist WC shadow-soak hypotheses + workflow audit decisions |
| **wiki_gap_detect Tier 1** | On request | Post-K84 run for stale `[NEEDS VERIFICATION]` on WC pages |
| **Canvas** | Rules exist | LP safety verdict matrix for Issue 3 prep |
| **Built-in browser** | Default for PM/Kalshi UI | Cross-venue live checks during Cup window |
| **claude-mem / mem-search** | Available | "Did we already reject PageIndex?" before re-Adopt |

### v4 Gemini eval prompt gap (workflow-adjacent)

v4 multi-wiki eval prompt (frozen in `Cemini claude code CCC/prompts/deep-research-multi-wiki-eval-v4-2026-05-21.md`) lacks:

- **world-cup-bot** OSS module map (scanner/conviction/quoter/fill/calendar/cross-venue/ledger)
- **Shipped tools** inventory (lazy-tool, stash, ArcticDB on librarian, prod-mcp)
- **Phase-0 NO-GO registry** (PageIndex, SwarmVault, …)
- Inline **`gh api` license step**

→ Draft **v5** before next tool-eval drop (see `Cemini claude code CCC/prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md`).

## Adopted (2026-05-30 session)

| Item | Status | Notes |
|------|--------|-------|
| Inbox watcher | **Live** | `scripts/inbox_notify.sh` + LaunchAgent `com.cemini.inbox-notify` (WatchPaths on `research to be indexed/`) |
| Wiki sync verify | **Live** | `scripts/verify_wiki_sync.sh`; hourly LaunchAgent + end of `sync_wiki_to_librarian.sh` |
| License spot-check | **Script** | `scripts/license_spot_check.sh` — run post tool-eval ingest |
| kepano obsidian-skills | **Installed** | HTTPS `npx skills add https://github.com/kepano/obsidian-skills.git` → `.agents/skills/obsidian-{markdown,cli}` |
| v5 eval prompt | **Draft on disk** | CCC `prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md` |
| n8n host | **Deferred** | Script-first per recommendation |
| Obsidian vault mirror | **Deferred** | Optional human curation layer |

## Snippets

> "NPX install path is one command — npx skills add git@github.com:kepano/obsidian-skills.git" [Source: kepano-obsidian-skills.md]

> "4,343 production-ready automation scripts" + Trusera AI-BOM scanner [Source: n8n-workflows.md / K42 eval]
