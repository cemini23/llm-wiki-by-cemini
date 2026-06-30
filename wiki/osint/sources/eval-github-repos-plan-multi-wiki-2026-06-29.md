---
title: "GitHub Repository Evaluation Plan.docx — multi-wiki runtime batch (2026-06-29)"
type: source
tags: [tool-evaluation, multi-wiki, k134, license-compliance]
keywords: [deepsec, agent-reach, codebase-memory-mcp, mattpocock-skills, cybersec-skills, gemini-dr-v9]
related:
  - concepts/wiki-tooling-evaluation.md
  - concepts/cemini-license-posture.md
  - entities/tools/deepsec.md
  - entities/tools/codebase-memory-mcp.md
  - "@ccc-wiki/entities/tools/codebase-memory-mcp.md"
  - entities/tools/agent-reach.md
  - entities/tools/anthropic-cybersecurity-skills.md
  - entities/tools/stealth-browser-mcp.md
  - entities/tools/daily-stock-analysis.md
  - entities/tools/mattpocock-skills.md
  - sources/eval-multi-wiki-discord-link-2026-06-28.md
  - concepts/llm-agent-systems.md
read_status: read
created: 2026-06-29
updated: 2026-06-29
clusters: [agent-harness, wiki-tooling, osint, cybersec]
---

## Relations

- @concepts/wiki-tooling-evaluation.md — K134 wave register
- @entities/tools/deepsec.md — Adopt (Apache-2.0)
- @ccc-wiki/entities/tools/codebase-memory-mcp.md — CONDITIONAL-GO (MIT); CCC-primary deploy
- @entities/tools/agent-reach.md — CONDITIONAL-GO (MIT; ToS/cookie risk)
- @entities/tools/anthropic-cybersecurity-skills.md — Adopt (Apache-2.0)
- @entities/tools/stealth-browser-mcp.md — Steal-from (MIT; overlaps built-in browser)
- @entities/tools/daily-stock-analysis.md — Steal-from (MIT; xsp TA routing patterns)
- @entities/tools/mattpocock-skills.md — Adopt reaffirmed (K126 + K134)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v9) |
| **Type** | DOCX (`GitHub Repository Evaluation Plan.docx`) |
| **sha256** | `763c79d259573c4e3e3516bbaca911edb5b57d359a3c746caaf15dc4c9bc7d0f` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/GitHub Repository Evaluation Plan.docx` |
| **Retrieved** | 2026-06-29 (inbox) |
| **Read status** | read (tier aggregation + `gh api` spot-check on Adopt rows) |

## Narrative

K134 batch — **20 GitHub URLs** across OSINT, CCC, Cybersec, image-gen, and finance-bot surfaces. Theme: agent harness MCP, social read paths, security scanning, skill libraries.

### Tier distribution

| Tier | Count | Notes |
|------|-------|-------|
| **Adopt** | 7 | 6 new Phase-0 + mattpocock reaffirmed |
| **Steal-from** | 3 | agency-agents, ai-website-cloner, video-use |
| **Reference-only** | 3 | design.md, voicebox, free-for-dev |
| **Reject** | 6 | GPL/AGPL/CC-BY-NC poison + Metabase AGPL |
| **Defer** | 1 | penpot MPL-2.0 |
| **UNAVAILABLE** | 2 | total-recall, free-for-dev license gaps |

### Adopt — `gh api` spot-check (2026-06-29)

| Repo | Docx | Verified | Phase-0 |
|------|------|----------|---------|
| vercel-labs/deepsec | Adopt | **Apache-2.0**, 4.7k★, pushed 2026-06-22 | **GO** |
| mattpocock/skills | Adopt | **MIT**, 150k★ | **GO** (K126 entity; no re-audit) |
| DeusData/codebase-memory-mcp | Adopt | **MIT**, 20.7k★, pushed 2026-06-29 | **CONDITIONAL-GO** — trust binary + allowlist MCP tools |
| Panniantong/Agent-Reach | Adopt | **MIT**, 45k★ | **CONDITIONAL-GO** — cookie/ToS; wiki-only |
| ZhuLinsen/daily_stock_analysis | Adopt | **MIT**, 51.6k★ | **Steal-from** — GHA cron + LiteLLM routing; not prod stack |
| mukul975/Anthropic-Cybersecurity-Skills | Adopt | **Apache-2.0**, 22.9k★ | **GO** — cybersec skill corpus |
| vibheksoni/stealth-browser-mcp | Adopt | **MIT**, 807★, pushed 2026-05-24 | **Steal-from** — overlaps Cursor browser + Playwright |

### Rejects aggregated (no per-URL stubs)

**Copyleft / NC:** altic-dev/FluidVoice (GPL-3.0), simplex-chat/simplex-chat (AGPL-3.0), calesthio/OpenMontage (AGPL-3.0), metabase/metabase (AGPL-3.0), ByteByteGoHq/system-design-101 (CC-BY-NC).

**UNAVAILABLE:** dax8it/total-recall (NO LICENSE on gh), ripienaar/free-for-dev (license not found).

### Cross-wiki routing

| Repo | Target wiki |
|------|-------------|
| deepsec, Anthropic-Cybersecurity-Skills | @cybersec-wiki |
| mattpocock/skills, codebase-memory-mcp, design.md | @ccc-wiki |
| Agent-Reach, stealth-browser-mcp | osint-wiki |
| OpenMontage, voicebox | @image-gen-wiki |
| video-use | @seo-wiki |

## Snippets

> "Deepsec operates via a bifurcated pipeline: rapid heuristic scan, then LLM investigation in Vercel Sandbox microVMs." [Source: GitHub Repository Evaluation Plan.docx URL 3 (retrieved 2026-06-29)]

> "Codebase-memory-mcp reduces token consumption by over 99% via Tree-sitter AST graphs and 14 MCP tools." [Source: GitHub Repository Evaluation Plan.docx URL 6 (retrieved 2026-06-29)]

## Dead Ends

- Docx **Adopt** tier for `daily_stock_analysis` over-routes to cemini-prod — repo is GHA cron + retail data providers; downgrade to **Steal-from** for xsp-killer TA digest patterns only.
- Docx **Adopt** for `stealth-browser-mcp` duplicates OSINT built-in browser + global Playwright — no install until anti-bot claims reproduced.
