---
title: Multi-Wiki Link Revenue Evaluation v10.9 (20 URLs, 2026-10-25)
type: source
tags: [source, eval, tool-evaluation, revenue-lens]
keywords: [multi-wiki link evaluation, runtime v10.9, phase-0, tool triage]
related:
  - entities/tools/hallmark.md
  - entities/tools/security-audit-skill.md
  - entities/tools/jiangshan-map.md
  - entities/tools/firecrawl-gov-index.md
  - entities/tools/experiential-labs.md
  - concepts/historical-jurisdiction-atlas.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Cemini Multi-Wiki Link Evaluation and Revenue Opportunity Analysis (Runtime v10.9) |
| Type | Generated evaluation report (agent-authored, cited) |
| Author | Cemini eval pipeline |
| Received | 2026-10-25 |
| Inbox | `research to be indexed/osint/Multi-Wiki Link Revenue Evaluation.docx` |
| Duplicate | `Multi-Wiki Link Revenue Evaluation (1).docx` — byte-identical text (md5 `3404b6b5...`), one source |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/Multi-Wiki Link Revenue Evaluation 2026-10-25.docx` — dated to avoid clobbering the 2026-10-15 revision of the same name |
| Batch | 20 URLs, none deferred |
| Lens | revenue + project fit. Priority #1 Atto, #2 GuruWatcher + Basgiath, #3 CeminiDFS, #4 CeminiParlays, then wikis |

## Narrative

One batch of 20 URLs, scored on a revenue lens and routed to a wiki. Tiers: 3 Integrate, 5 Extract, 2 Watch, 6 Context, 4 Pass, 0 unavailable.

Batch themes: agentic coding harnesses, frontend anti-slop design, SEO/GEO conversion skills, local full-duplex speech, self-hosted PaaS and LLM routing, historical cartography deep-linking, US primary-law OSINT indexing.

### Tier table

| # | Tool | Tier | Primary wiki | Project fit | License (verified) |
|---|------|------|--------------|-------------|--------------------|
| 2 | Nutlope/hallmark | **Integrate** | CCC → SEO, Game-dev | atto high, basgiath med | MIT |
| 6 | cloudflare/security-audit-skill | **Integrate** | Cybersec → CCC | atto high, lab high | MIT |
| 7 | AgriciDaniel/claude-seo | **Integrate** | SEO → CCC, Game-dev | atto high, basgiath med | MIT |
| 3 | debpalash/VoiceStudio | **Extract** | Game-dev → Image-gen, OSINT, CCC | basgiath high, atto med | **AGPL-3.0** |
| 5 | JetBrains/thinkrail | **Extract** | CCC | atto med, guruwatcher med | Apache-2.0 |
| 10 | DeanChensj/jiangshan-map | **Extract** | OSINT → CCC | atto high, genealogy high | **GPL-3.0** |
| 15 | experientiallabs.ai | **Extract** | Cybersec → CCC, OSINT | lab high, guruwatcher high, atto med | Apache-2.0 (gateway) |
| 17 | firecrawl.dev/gov-index | **Extract** | OSINT → CCC | atto high, pm-canary med | Proprietary service, free tier |
| 14 | pausevfx.com | Watch | Game-dev | basgiath med | Proprietary SaaS |
| 18 | block.xyz/dessa | Watch | Game-dev | atto low, basgiath low | Unreleased |
| 1 | makecindy/cindy | Context | CCC | atto low | Apache-2.0 |
| 8 | coollabsio/coolify | Context | CCC → Cybersec | low across | Apache-2.0 |
| 9 | max-sixty/worktrunk | Context | CCC | atto low | NOT FOUND in index |
| 11 | jarrodwatts/claude-hud | Context | CCC → Cybersec | none | MIT |
| 13 | 777genius/agent-teams-ai | Context | CCC | none | NOT FOUND in index |
| 19 | deepseek-ai/DeepInfer | Context | CCC → Cybersec | low | Apache-2.0 |
| 4 | Renhuai123/ziwei-doushu | Pass | (OSINT, nominal) | none | NOT FOUND |
| 12 | Calcium-Ion/moejs | Pass | CCC | none | NOT FOUND |
| 16 | reasonmachines.com | Pass | — | none | N/A (domain listing) |
| 20 | kernel.org | Pass | Cybersec (nominal) | none | GPL-2.0 |

### Phase-0 audit — 2026-10-25

Per `CLAUDE.md` Phase-0 pattern. Each Integrate/Extract tool was shallow-cloned to `/tmp/phase0-audit/` and inspected. Seven of eight clones succeeded; `firecrawl/firecrawl-js` failed as a repo name — the CLI lives at `firecrawl/cli`.

| Tool | Clone | License | Last commit | Size | Structural claims checked | Verdict |
|------|-------|---------|-------------|------|---------------------------|---------|
| hallmark | OK | MIT | 2026-10-22 | 122 MB / 820 files | 755 photo entries ✓. `skills/hallmark/scripts/sloplint.mjs` exists ✓ but the report's `scripts/sloplint.mjs` path is wrong. | **GO** |
| security-audit-skill | OK | MIT | **2026-09-14** | 588 KB / 22 files | 11 domain docs, not the 5 the report names. Report's "Oct 17" commit date is wrong. Tiny = cheap to vendor. | **GO** |
| claude-seo | OK | MIT | 2026-10-22 | 11 MB / 467 files | 26 skills ✓, 19 agents ✓. No `commands/` dir — the report's "34 slash commands" are the skills themselves. | **GO** |
| VoiceStudio | OK | **AGPL-3.0** | 2026-10-25 | 139 MB / 4072 files | MCP server tests present ✓. AGPL confirmed — never vendor into Atto. | **CONDITIONAL-GO (isolate only)** |
| thinkrail | OK | Apache-2.0 | 2026-10-25 | 30 MB / 1928 files | `packages/spec-graph/tools/` has get/grep/graph/delete/create/update/validate ✓. **But `package.json` has no `bin` and no `main`**, and no `mcp/server.mjs` exists. The report's portability claim is unverified. | **CONDITIONAL-GO** |
| jiangshan-map | OK | **GPL-3.0** | 2026-10-25 | 43 MB / 82 files | `?year=` / `?place=` semantic router confirmed in README_ZH ✓. Report said license NOT FOUND — it is **GPL-3.0**, so no code or asset copying. | **CONDITIONAL-GO (pattern only)** |
| experiential | OK | Apache-2.0 | 2026-10-09 | 35 MB / 1536 files | `exp` CLI present ✓. Hosted tier is commercial, separate terms. | **CONDITIONAL-GO** |
| firecrawl (CLI) | OK (`firecrawl/cli`) | NOT FOUND (proprietary service) | — | 80 KB | `src/types/gov.ts`, `alexandria-beta.test.ts`, `skills/firecrawl-alexandria` ✓. Gov index confirmed in the client. | **GO (client only)** |

Three corrections to the report that change decisions:

1. **jiangshan-map is GPL-3.0, not unlicensed.** The report's "do not copy raw map code" caution is not a preference — it is a legal requirement. Re-implement the URL contract from scratch over ISTAT data.
2. **thinkrail has no shipped MCP stdio server.** The report claims it was "already proven portable" via `mcp/server.mjs`. That file does not exist in the public repo, and `pi-spec-graph` declares no entrypoint. Extract the tool source and wrap it; do not assume a server ships.
3. **security-audit-skill has 11 domain docs, not 5.** Coverage is broader than the report implies. Its last commit is 2026-09-14, so the "Oct 17" date in the report is stale.

### Atlas for Atto

URL 10 (jiangshan-map) is the pattern source for the in-flight Atlas work on Atto. The reusable idea is narrow and valuable: **the agent emits `?year=YYYY&place=Name` and never emits coordinates.** The client resolves jurisdiction boundaries. This removes LLM coordinate hallucination from FIND deep-links. See @concepts/historical-jurisdiction-atlas.md.

The GPL-3.0 licence means Atto takes the *contract*, not the code.

### Genuine gaps the batch identified

Eight, per the report: anti-slop conversion floor, multi-phase adversarial security verification, automated GEO/SEO audit, local voice/ASR, persistent spec graph, zero-coordinate jurisdiction mapping, zero-retention large-context uncensored routing, and zero-credit US primary-law lookup.

## Snippets

> "Extracting this semantic URL deep-link and place-genealogy pattern into an Atto Access share (20/mo) and Concierge (>=$2.5k) visualization brief creates compelling visual differentiation for paying genealogy customers (Extract)." — report, URL 10

> "the high-leverage play is classifying DeepInfer as Context in CCC wiki and consuming DeepSeek-V4.1-Flash at $0/token via experientiallabs.ai." — report, URL 19

> "AGPL-3.0 — strict copyleft network license. Must NEVER be linked, vendored, or bundled inside /Users/claudiobarone/Projects/atto." — report, URL 3

## Dead Ends

- **`firecrawl/firecrawl-js`** does not exist. The CLI repo is `firecrawl/cli`. A guessed repo name wastes a clone.
- **Report row 9 (worktrunk) carries no telemetry** — stars, commits, issues, and licence are all "NOT FOUND". It stays Context and unverified until someone checks.
