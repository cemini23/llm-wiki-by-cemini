---
title: Tool Evaluation and Cross-Wiki Routing — 56-target batch (2026-06-13)
type: source
tags: [source, phase-0, routing, tools, stronghold, audit]
keywords: [tool-evaluation, cross-wiki, serpentai, airtest, ucp2, license]
related:
  - concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
  - concepts/stronghold-modding-ecosystem-shelf.md
  - concepts/deferred-engine-candidates.md
  - entities/tools/serpent-ai.md
  - entities/tools/unofficial-crusader-patch2.md
  - entities/tools/gamedev-resources.md
  - entities/tools/airtest.md
  - sources/serpent-ai-phase-0-audit-2026-06-13.md
  - sources/airtest-phase-0-audit-2026-06-13.md
  - sources/unofficial-crusader-patch2-phase-0-audit-2026-06-13.md
  - meta/cross-wiki-routing.md
  - concepts/ai-game-dev-tool-stack-2026.md
  - concepts/art-pipeline-v0-requirements.md
read_status: read
source_type: operator-research
source_url: ""
maturity: validated
created: 2026-06-13
updated: 2026-06-15
---

## Raw Concept

- **Original title**: Tool Evaluation and Cross-Wiki Routing Analysis Report
- **Location**: `research to be indexed/Tool Evaluation and Wiki Fit.docx`
- **SHA-256**: `763fc3e3a82c9a00…` (full hash from preingest_check)
- **Method**: Multi-wiki eval prompt v7 (surface 8 = game-dev-wiki); license lookup via LICENSE file + GitHub API where noted
- **Targets**: 56 GitHub URLs across game frameworks, Stronghold modding, agent harness, UI automation

## Narrative

Operator dropped a structured evaluation docx covering **56 repositories** with tier verdicts (Adopt / Steal-from / Defer / Reference-only / Reject / UNAVAILABLE), primary wiki fit, and cross-wiki routing stubs.

Pre-ingest flagged **DUPLICATE** on CCGS URL only — remainder is **NEW** analytical content folded into @concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md.

### Aggregate verdicts [CONFIRMED — docx aggregate summary]

| Tier | Count | Notable |
|------|-------|---------|
| **Adopt** | 1 | Airtest → @ccc-wiki primary |
| **Steal-from** | 5 | SerpentAI, CCGS (existing), GameFramework, GameDevelopmentKit, UCP2 |
| **Defer** | 2 | libGDX, Duality |
| **Reference-only** | 2 | AITradeGame → OSINT; GameDev-Resources |
| **Reject** | 37 | License gaps, scope mismatch, proprietary book code |
| **UNAVAILABLE** | 9 | Unretrievable at eval time |

### Post-ingest license corrections [CONFIRMED — gh api 2026-06-13]

| Repo | Docx verdict | Corrected |
|------|--------------|-----------|
| OpenSHC | Reject (no license) | **GPL-3.0** — reference-only for engine archaeology; no code merge into castle-sim |
| Path-Creator | Reject (no license) | **MIT** — upgrade to **Steal-from** for Unity spline math when Unity Phase-0 runs |
| AI-Aimbot | Reject (no license) | **GPL-3.0** — still **Reject** on game-dev; route @cybersecurity-wiki offensive shelf |
| SerpentAI | Steal-from MIT | Confirmed MIT; last push 2022-11 — **dormant** [NEEDS VERIFICATION 2026-09-13] |
| UCP2 | Steal-from MIT | Confirmed MIT; ~435★, active issue queue |

### License hygiene finding [TENTATIVE]

Stronghold Crusader community modding repos overwhelmingly lack SPDX licenses (~35/56 NO LICENSE in docx). **UnofficialCrusaderPatch2** is the clean MIT exception for studying AIV injection and balance patches — not for copying Firefly assets.

### Cross-wiki stubs (operator action — sibling wikis)

| Target wiki | Stub topic |
|-------------|------------|
| @ccc-wiki | SerpentAI pixel parsing for lazy-tool visual assertions |
| @ccc-wiki | AITradeGame multi-provider LLM routing (session hooks) |
| @ccc-wiki | CCGS 49-agent topology (partially done — @concepts/ccgs-workflow-extraction.md) |
| @cybersecurity-wiki | SerpentAI client automation (defensive) |
| @cybersecurity-wiki | UCP2 memory hooking case study |
| @cybersecurity-wiki | AI-Aimbot adversarial baseline |
| @image-gen-wiki | GameDev-Resources → OpenGameArt / Poly Haven links |

### world-cup-bot overlap

**None** — no prediction-market or sports-bot crossover in this batch.

## Snippets

Full per-URL table: @concepts/tool-evaluation-cross-wiki-batch-2026-06-13.md
