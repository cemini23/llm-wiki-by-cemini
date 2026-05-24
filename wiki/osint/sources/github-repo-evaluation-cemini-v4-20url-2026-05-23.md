---
title: "GitHub Repo Evaluation for Cemini — 20-URL batch (v4, May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki-routing, license-audit, k60]
keywords: [github-repo-evaluation, v4, kaligpt, trademaster, pentest-ai, h4cker, weather-bot-sweep, license-corrections]
related:
  - entities/tools/kaligpt.md
  - entities/tools/trademaster.md
  - entities/tools/pentest-ai.md
  - entities/tools/suislanchez-polymarket-kalshi-weather-bot.md
  - entities/tools/polyweather.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/cemini-license-posture.md
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
  - sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md
maturity: validated
read_status: deep-read
created: 2026-05-23
updated: 2026-05-24
clusters: [tool-evaluation]
---

## Relations
- @ccc-wiki/briefs/2026-05-23_k60-ai-engineering-roadmap-from-osint.md  (cross-wiki brief)
- @cybersecurity-wiki/briefs/2026-05-23_k60-cybersec-tool-eval-from-osint.md  (cross-wiki brief)

- @entities/tools/kaligpt.md — URL 1; eval Adopt **downgraded** (custom non-commercial license, not MIT)
- @entities/tools/trademaster.md — URL 4 Steal-from (Apache-2.0 verified)
- @entities/tools/pentest-ai.md — URL 6; eval Reject on license **corrected** (MIT via GitHub API)
- @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md — URL 17; **Steal-from** on re-audit (403★, cross-venue + Brier; license pending)
- @entities/tools/polyweather.md — URL 16; **Reference-only methodology** (AGPL; EMOS/DEB/TAF patterns)
- @concepts/polymarket-weather-trading-strategy.md — URLs 11–20 weather/Kalshi bot cluster
- @concepts/cemini-license-posture.md — fifth batch reinforcing license-layer unreliability

## Raw Concept

- **Title**: GitHub Repo Evaluation for Cemini (Multi-Wiki Link Evaluation v4)
- **Type**: LLM tool-eval report (Gemini DR-style), 20 GitHub URLs
- **Location**: `research to be indexed/GitHub Repo Evaluation for Cemini.docx` → `cemini-librarian:/opt/cemini-bulk/research/GitHub Repo Evaluation for Cemini.docx`
- **Retrieved**: 2026-05-23
- **Read status**: deep-read (with GitHub API license spot-checks)

## Narrative

### Tier rollup (eval verdicts vs API-corrected)

| Tier | Eval count | Notes after verification |
|------|------------|--------------------------|
| Adopt | 1 | KaliGPT — **downgrade** (custom NC license file, not MIT) |
| Steal-from | 1 | TradeMaster — Apache-2.0 confirmed |
| Reference-only | 3 | Ai-Engineering-Roadmap, h4cker, cyber-security-llm-agents |
| Reject | 15 | incl. weather-bot cluster + domain mismatches |

### Per-URL summary

| # | Repo | Eval tier | License (API 2026-05-23) | Primary fit | Corrected posture |
|---|------|-----------|---------------------------|-------------|-------------------|
| 1 | [KaliGPT](https://github.com/SudoHopeX/KaliGPT) | Adopt | **Custom NC** (not MIT) | Cybersec | **Reject** commercial / IP-sale |
| 2 | [Ai-Engineering-Roadmap](https://github.com/AgenticAiLabs/Ai-Engineering-Roadmap) | Reference | MIT | CCC | Reference-only |
| 3 | [h4cker](https://github.com/The-Art-of-Hacking/h4cker) | Reference | MIT | Cybersec | Reference-only; OSINT osint/ subtree |
| 4 | [TradeMaster](https://github.com/TradeMaster-NTU/TradeMaster) | Steal-from | Apache-2.0 | Cemini financial | Steal-from RL/backtest patterns |
| 5 | [Windows-MCP](https://github.com/CursorTouch/Windows-MCP) | Reject | **MIT** (eval wrong) | None | Reject domain (Windows GUI) |
| 6 | [pentest-ai](https://github.com/0xSteph/pentest-ai) | Reject | **MIT** (eval wrong) | Cybersec | CONDITIONAL-GO Phase-0; distinct from pentest-ai-agents |
| 7 | [grace-marketplace](https://github.com/osovv/grace-marketplace) | Reject | **MIT** (eval wrong) | CCC | Reject scope; reference GRACE pattern only |
| 8 | [frigate](https://github.com/blakeblackshear/frigate) | Reject | MIT | None | Reject domain (NVR/home) |
| 9 | [cyber-security-llm-agents](https://github.com/NVISOsecurity/cyber-security-llm-agents) | Reference | **NONE** | Cybersec | Reference-only until license filed |
| 10 | [COG-second-brain](https://github.com/huytieu/COG-second-brain) | Reject | **MIT** (eval wrong) | CCC | Reject — PKM overlap with existing stack |
| 11–20 | Weather / Kalshi bots | Reject (batch) | Mixed — see per-URL table | Cemini | **Re-audit 2026-05-24:** 2 steal-from tiers + 1 canonical MIT |

### Weather / Kalshi cluster — per-URL (re-audit 2026-05-24)

| # | Repo | Stars | License | Corrected posture |
|---|------|-------|---------|-------------------|
| 11 | [MoonsatProtocol/Polymarket-Weather-Bot](https://github.com/MoonsatProtocol/Polymarket-Weather-Bot) | ~99 | NONE | Reject adopt — TS Kelly + sim dashboard **patterns only**; freemium/paid edition |
| 12 | [MusicBoiyzzz/Polymarket-Weather-Bot](https://github.com/MusicBoiyzzz/Polymarket-Weather-Bot) | ~0 | NONE | **Skip** — Windows `.exe` zip funnel |
| 13 | [hcharper/polyBot-Weather](https://github.com/hcharper/polyBot-Weather) | ~35 | NONE | Reject — stale, no license |
| 14 | [alteregoeth-ai/weatherbot](https://github.com/alteregoeth-ai/weatherbot) | ~306 | **MIT** | **Steal-from (canonical)** — already on @concepts/polymarket-weather-trading-strategy.md |
| 15 | [AadiXD200/polymarket-weather-bot](https://github.com/AadiXD200/polymarket-weather-bot) | ~5 | NONE | Reject — thin, no license |
| 16 | [yangyuan-zhen/PolyWeather](https://github.com/yangyuan-zhen/PolyWeather) | ~69 | **AGPL-3.0** | **Reference-only** — DEB/EMOS/TAF/bucket methodology → @entities/tools/polyweather.md |
| 17 | [suislanchez/polymarket-kalshi-weather-bot](https://github.com/suislanchez/polymarket-kalshi-weather-bot) | ~403 | **NONE** (README falsely badges MIT) | **Steal-from CONDITIONAL-GO** → @entities/tools/suislanchez-polymarket-kalshi-weather-bot.md |
| 18 | [kylecwalden/polymarket-sniper-bot](https://github.com/kylecwalden/polymarket-sniper-bot) | ~20 | NONE | Reject — generic sniper, not weather |
| 19 | [AruneshDev/Automated-Trading-System-Kalshi-Weather-Model](https://github.com/AruneshDev/Automated-Trading-System-Kalshi-Weather-Model) | ~4 | NONE | Reject — stale 2025 |
| 20 | [cpratim/Kalshi-Weather-Trading](https://github.com/cpratim/Kalshi-Weather-Trading) | ~5 | MIT | Reject — empty README; no auditable code surface |

First-pass aggregate reject still valid for **Adopt** (no new installs without Phase-0). Re-audit adds explicit **Steal-from** rows for suislanchez + PolyWeather methodology + reaffirms weatherbot as MIT canonical.

### License corrections (GitHub API spot-check)

| Repo | Eval claimed | API / file |
|------|--------------|------------|
| KaliGPT | MIT | **SudoHopeX Non-Commercial Software License (2025)** |
| Windows-MCP | NO LICENSE | MIT |
| pentest-ai | NO LICENSE | MIT |
| grace-marketplace | NO LICENSE | MIT |
| COG-second-brain | NO LICENSE | MIT |

Reinforces @concepts/cemini-license-posture.md: read LICENSE file + `gh api`, not eval prose.

### Cross-wiki routing (executed via briefs)

- **cybersecurity-wiki** — KaliGPT (NC caveat), pentest-ai MCP, h4cker reference, NVISO catalog
- **ccc-wiki** — Ai-Engineering-Roadmap reference

## Snippets

> "TradeMaster provides an exhaustive pipeline for RL-based algorithmic trading… PRUDEX-Compass benchmark… classification restricted to Steal-from." [Source: GitHub Repo Evaluation for Cemini.docx, URL 4]

> "KaliGPT… terminal-native agentic AI… local Ollama… OPSEC value." [Source: same, URL 1 — license claim MIT **not confirmed**]
