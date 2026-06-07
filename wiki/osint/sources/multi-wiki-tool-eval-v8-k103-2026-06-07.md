---
title: "Tool Evaluation and Wiki Fit — 63-URL Multi-Wiki Batch (K103)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, polymarket-profiles, k103]
keywords: [tool-evaluation, asm, pydantic-ai, pmxt, polymarket-data, cloddsbot, polyweather-agpl]
related:
  - sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md
  - entities/tools/agent-skill-manager.md
  - entities/tools/polymarket-data-sii.md
  - entities/tools/pydantic-ai.md
  - entities/tools/pmxt.md
  - entities/tools/application-skills.md
  - entities/tools/deep-scientist.md
  - entities/tools/autoresearch-claw.md
  - entities/tools/poker-query-language.md
  - entities/tools/cloddsbot.md
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
  - sources/tradingagents.md
maturity: validated
read_status: deep-read
created: 2026-06-07
updated: 2026-06-07
clusters: [cemini-internal]
---

## Relations

- @sources/multi-wiki-tool-eval-50url-k102-2026-06-06.md — prior 50-URL batch (different sha256)
- @entities/tools/agent-skill-manager.md — Adopt (Phase-0 CONDITIONAL-GO)
- @entities/tools/pydantic-ai.md — Adopt (Phase-0 GO)
- @entities/tools/pmxt.md — Adopt reaffirmed (Phase-0 CONDITIONAL-GO)
- @entities/tools/application-skills.md — Eval Adopt overturned → NO-GO
- @concepts/cemini-license-posture.md — license batch via `post_tool_eval_license.sh`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report — *Tool Evaluation and Wiki Fit* (Batch K85 header in doc) |
| **Type** | Internal evaluation document (.docx) |
| **sha256** | `6ebbacb83f2980fe042c464d7c029ae86b4d6817a33798e6fb118f71d7331d4a` |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit.docx` |
| **Retrieved** | 2026-06-07 |
| **URLs** | 63 |
| **Read status** | deep-read + `gh api` license spot-check + Phase-0 clones |

## Narrative

Sixty-three-URL Gemini DR eval (June 2026). Mix of **Polymarket whale profiles** (Reference-only), **prediction-market bots**, **poker/gambling playgrounds**, and **agent harness** repos. License spot-check saved: `.local/reports/license-spot-check-2026-06-07-0835.txt`.

### Tier rollup (post-verify)

| Tier | Count (eval) | Post-Phase-0 notes |
|------|--------------|-------------------|
| **Adopt** | 5 | asm, Polymarket_data, pydantic-ai, pmxt, application-skills → **application-skills demoted NO-GO** (null repo license + Membrane lock-in) |
| **Steal-from** | 5 | DeepScientist, CloddsBot, TradingAgents, AutoResearchClaw, Poker-Query-Language → **PQL NO-GO** (immature) |
| **Reference-only** | 15 | PM profiles (gopfan2, 1pixel, …), polybot, etc. |
| **Reject** | 8+ | PolyWeather AGPL, polymarket_lp_tool no license, LGPL forks, poker playgrounds |

### License corrections (eval → `gh api`)

| Repo | Eval | Verified |
|------|------|----------|
| membranedev/application-skills | MIT | **null** (no root LICENSE) → NO-GO |
| lihanyu81/polymarket_lp_tool | Reject | **null** — keep Reject |
| yangyuan-zhen/PolyWeather | Reject AGPL | **AGPL-3.0** confirmed |
| pydantic/pydantic-ai-gateway | — | **AGPL-3.0** — do not adopt; core `pydantic-ai` is MIT |
| luongnv89/asm | MIT | **MIT** confirmed |
| SII-WANGZJ/Polymarket_data | MIT | **MIT** confirmed |

### Phase-0 verdicts (2026-06-07 clones → `/tmp/k103-phase0-audit/`)

| Repo | Verdict | Install action |
|------|---------|----------------|
| pydantic-ai | **GO** | Laptop prototypes → prod brief for targeted modules |
| asm | CONDITIONAL-GO | Laptop skill-dir isolation only |
| Polymarket_data | CONDITIONAL-GO | Sample dataset on laptop; prod via brief |
| pmxt | CONDITIONAL-GO | Prod brief only; fork+pin; drop `baozi` adapter |
| application-skills | **NO-GO** | Wiki reference only |
| CloddsBot | CONDITIONAL-GO steal | Pattern extraction only |
| Poker-Query-Language | **NO-GO** | Wiki watchlist |

### World-cup-bot / gambling lines

| URL | Verdict | Notes |
|-----|---------|-------|
| pmxt-dev/pmxt | Adopt CONDITIONAL-GO | Modules 1, 3, 4 — existing entity; no new greenfield |
| alsk1992/CloddsBot | Steal-from | Module 4 M2M patterns — no Node install |
| solve-poker/Poker-Query-Language | NO-GO | 4★ WIP — gambling brief documents reject |
| ToNiePiter/casinogame + poker playgrounds | Reject | No license / domain mismatch |

### Cross-wiki routing

| Wiki | Brief on disk |
|------|---------------|
| **CCC** | asm + pydantic-ai + AutoResearchClaw + DeepScientist + backpressure/RL posts |
| **gambling** | poker/casino reject cluster + PQL NO-GO |
| **prod (staged, not scp)** | pmxt + pydantic-ai typed-agent modules — after Phase-0 |

## Snippets

> "AGPL-3.0 Open Core Policy" — PolyWeather March 2026 pivot; strict Reject for `/opt/cemini`. [Source: Tool Evaluation and Wiki Fit.docx URL 25; `gh api` confirms AGPL-3.0]

> "pydantic-ai-gateway is AGPL-3.0; core pydantic-ai is MIT" — adopt core only. [Source: K103 license spot-check]
