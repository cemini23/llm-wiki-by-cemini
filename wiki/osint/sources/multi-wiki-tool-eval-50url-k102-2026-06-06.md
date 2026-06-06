---
title: "Tool Evaluation Prompt Analysis — 50-URL Multi-Wiki Batch (K102)"
type: source
tags: [docx, tool-evaluation, multi-wiki, license-audit, world-cup, k102]
keywords: [tool-evaluation, polymarket-bot, typst, harness, deptry, openfootball, defending-code, wc-repos]
related:
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
  - entities/tools/mrfadi-polymarket-bot.md
  - entities/tools/revfactory-harness.md
  - entities/tools/typst.md
  - entities/tools/deptry.md
  - entities/tools/defending-code-reference-harness.md
  - entities/tools/ai-text-humanizer-app.md
  - entities/tools/flowforge-skill.md
  - entities/tools/openfootball-worldcup-json.md
  - entities/tools/world-cup-bot.md
  - concepts/world-cup-advance-market-bot-v1.md
maturity: validated
read_status: deep-read
created: 2026-06-06
updated: 2026-06-06
clusters: [cemini-internal]
---

## Relations

- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 sibling file (same filename, different sha256)
- @entities/tools/mrfadi-polymarket-bot.md — Steal-from (Module 7 streak sizing)
- @entities/tools/revfactory-harness.md — Adopt (Phase-0 CONDITIONAL-GO)
- @entities/tools/typst.md — Adopt (Phase-0 CONDITIONAL-GO)
- @entities/tools/deptry.md — Adopt (Phase-0 GO)
- @entities/tools/defending-code-reference-harness.md — Adopt cybersec (Phase-0 CONDITIONAL-GO)
- @entities/tools/openfootball-worldcup-json.md — Adopt (already vendored K82)
- @entities/tools/world-cup-bot.md — WC brief target

## Raw Concept

- **Title**: Cemini Multi-Wiki Link Evaluation Report — *Tool Evaluation Prompt Analysis*
- **Type**: Internal evaluation document (.docx)
- **Retrieved**: 2026-06-06
- **sha256**: `18d1a10195a02196…` (NEW vs K68 `multi-wiki-tool-eval-22url`)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation Prompt Analysis.docx` (post-ingest)
- **URLs**: 50
- **Read status**: deep-read + `gh api` license batch + unavailable-repo resolution

## Narrative

Fifty-repository Gemini DR eval (June 2026 refresh). **License spot-check overturned 12 eval claims**; **28 repos marked UNAVAILABLE in the doc are reachable** — most are zero-star, no-LICENSE WC spam repos pushed 2026-06-06 (not integration candidates).

### Tier rollup (post-verify)

| Tier | Count | Notes |
|------|-------|-------|
| **Adopt** | 6 | harness, typst, deptry, defending-code (Apache LICENSE file), openfootball/worldcup, AI-Text-Humanizer (SEO) |
| **Steal-from** | 8 | Polymarket-bot sizing, flowforge, multiagent-coaching, academic-research-skills, Auto-Empirical-Research-Skills, awesome-rag (CC0 not MIT) |
| **Reference-only** | 4 | awesome-rag, a-list-of-claude-code-agents, WC ML sim (MIT), ScoutFootball |
| **Defer** | 2 | Auto-Company, deptry was Defer in eval → **MIT confirmed** → promoted Adopt |
| **Reject** | 7 | GHOST (PolyForm-NC), gate12 (GPL-3.0), crocoddyl (domain), + domain mismatches |
| **UNAVAILABLE (eval)** → resolved | 28 | **All exist** on GitHub 2026-06-06; 25 have `license: null`, 2 MIT, 1 CC0 calendar |
| **WC junk cluster** | ~20 | Same-day empty repos — **no Phase-0** |

### License corrections (eval → `gh api` / LICENSE file)

| Repo | Eval | Verified |
|------|------|----------|
| MrFadiAi/Polymarket-bot | NO LICENSE | **MIT** |
| osprey-oss/deptry | NO LICENSE | **MIT** |
| wentong2022-arch/flowforge-skill | NO LICENSE | **MIT** |
| ltjed/multiagent-coaching | NO LICENSE | **MIT** |
| coree/awesome-rag | MIT | **CC0-1.0** |
| tiagolr/gate12 | NO LICENSE | **GPL-3.0** |
| anthropics/defending-code-reference-harness | Apache-2.0 | **Apache-2.0** (LICENSE file; API `NOASSERTION`) |
| devfun-org/poker-arena-starter-kit | UNAVAILABLE | **MIT**, exists |
| IoakeimKyrgiafinis/WorldCup2026ML-MCsimulationPrediction | UNAVAILABLE | **MIT**, exists |

### World-cup-bot research lines

| URL | Verdict | WC module |
|-----|---------|-----------|
| MrFadiAi/Polymarket-bot | Steal-from | **Module 7** — 4-layer PnL gates + streak sizing |
| openfootball/worldcup | Adopt (sibling) | Module 5 — CC0 schedule (`.json` already vendored K82) |
| debatepro/world-cup-2026-calendar | Reference | CC0 calendar alt |
| ono/clean-match-schedule | Reference | MIT schedule helper |
| bernhard-pfann/soccer-predictions | Defer | Probabilistic model, no LICENSE |
| authenticarc/polymarket-soccer-tracker | Defer | PM soccer, no LICENSE |
| URLs 19–26, 28–50 (no-license spam) | Reject | Same-day junk — do not ingest |

### Cross-wiki routing

| Wiki | Brief |
|------|-------|
| **world-cup-bot / prod** | Streak sizing + multi-layer PnL gates |
| **CCC** | harness + typst + flowforge |
| **cybersec** | defending-code-reference-harness |
| **SEO** | AI-Text-Humanizer |
| **gambling** | poker-arena-starter-kit (MIT, dev.fun) |

## Snippets

> "Four-layer protection: daily 5%, monthly 15%, drawdown 25% from peak, total 40% permanent halt; dynamic sizing −20% per loss after 2 consecutive, +10% per win after 3." [Source: MrFadiAi/Polymarket-bot `bot-config.ts` v3.1; K102 Phase-0 clone]

> "Twenty-eight repository endpoints marked UNAVAILABLE in eval — all resolved reachable 2026-06-06; majority are zero-star no-LICENSE repos pushed same day." [Source: K102 `gh api` batch]
