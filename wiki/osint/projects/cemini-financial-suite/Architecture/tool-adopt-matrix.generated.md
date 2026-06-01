---
title: CeminiSuite tool adopt matrix (generated)
type: concept
date: 2026-06-01
updated: 2026-06-01
tags: [architecture, cemini-suite, prod-handoff, wave4]
keywords: [Cemini-Financial-Suite, /opt/cemini, e8fd49f]
deploy-root: /opt/cemini
scanned-commit: e8fd49f
provenance: prod-briefs-out-architecture-2026-06-01-wave4
ai-first: true
related:
  - projects/cemini-financial-suite/Cemini Financial Suite.md
  - projects/cemini-financial-suite/Architecture/Architecture - tools.md
  - projects/cemini-financial-suite/Architecture/OPEN-GAPS.md
maturity: validated
---

## Relations

- @projects/cemini-financial-suite/Cemini Financial Suite.md
- @projects/cemini-financial-suite/Architecture/Architecture - tools.md
- @projects/cemini-financial-suite/Architecture/OPEN-GAPS.md

## For future Claude

Regenerable K71 tool manifest; scripts/export_tool_adopt_matrix.py on prod.

<!-- @generated:start tool-adopt-matrix -->
| Slug | Verdict | Batch | Repo | Reason / notes |
|------|---------|-------|------|----------------|
| `suislanchez-weather` | **STEAL_FROM** | k60 | suislanchez/polymarket-kalshi-weather-bot | No LICENSE on main — pattern extract only |
| `trademaster-ntu` | **STEAL_FROM** | k60 | TradeMaster-NTU/TradeMaster | Apache — eval/simulator patterns only; no prod install |
| `coldmath-adversary` | **STEAL_FROM** | k61 | ColdMath/polymarket-weather | Adversary model K61 — watchlist only |
| `katbrink-weather` | **—** | k63 | Katbrink/polymarket-weather-trading-bot |  |
| `openpatchlab-weather` | **—** | k63 | OpenPatchLab/polymarket-weather-trading-bot | MIT weather bot — verify LICENSE on audit |
| `pm-weather-bot-moonsat` | **REJECT** | k63 | MoonsatProtocol/Polymarket-Weather-Bot | No LICENSE; freemium |
| `tsukamg-weather-engine` | **—** | k63 | Tsukamg/polymarket-weather-trading-engine |  |
| `arcticdb` | **STEAL_FROM** | k68 | man-group/ArcticDB | Step 189 — read-only bulk bars |
| `aruneshdev-kalshi-weather` | **REJECT** | k68 | AruneshDev/Automated-Trading-System-Kalshi-Weather-Model | No LICENSE artifact (K68/K66 caution) |
| `chronos-forecasting` | **DEFER** | k68 | amazon-science/chronos-forecasting | Step 64/109 comparison |
| `dataset-viewer` | **DEFER** | k68 | cursor-dataset-viewer/dataset-viewer | Laptop Arctic UI — K59 |
| `finrl` | **DEFER** | k68 | AI4Finance-Foundation/FinRL | RL stack — license review pending |
| `flox-ws` | **GO** | k68 | flox-dev/flox | Step 197 shipped on prod |
| `graphic-walker` | **DEFER** | k68 | Kanaries/graphic-walker | UI-10 backlog |
| `hftbacktest` | **DEFER** | k68 | nkaz001/hftbacktest | Step 131 research backlog |
| `kronos` | **DEFER** | k68 | NeoQuasar/Kronos | Kronos A/B brief |
| `langextract` | **DEFER** | k68 | google/langextract | Step 108 research |
| `leann-rag` | **DEFER** | k68 | yichuan-w/LEANN | Evaluate separately from K71 scope |
| `madappgang-claudish` | **REJECT** | k68 | MadAppGang/claudish | license null / no LICENSE file (K68) |
| `octotools` | **DEFER** | k68 | octotools/octotools | Step 190 audit |
| `paradigmxyz-centaur` | **STEAL_FROM** | k68 | paradigmxyz/centaur | NOASSERTION license — patterns only until clarified |
| `polymarket-agents` | **DEFER** | k68 | Polymarket/agents | Step 127 blocked |
| `pykalshi` | **GO** | k68 | Kalshi/pykalshi | Step 129 shipped |
| `qstrader` | **STEAL_FROM** | k68 | quantstart/qstrader | Already partially adopted Step 191 |
| `automaton` | **REJECT** | k71 | 0x676/automaton | Malicious setup / wallet exfil (issue #245) |
| `bbot` | **REJECT** | k71 | blacklanternsecurity/bbot | AGPL-3.0 |
| `camofox-browser` | **LAPTOP_ONLY** | k71 | — | Laptop wiki ingest helper — not prod |
| `polyweather` | **REJECT** | k71 | yangyuan-zhen/PolyWeather | AGPL-3.0 — methodology only (K60 A8) |
| `xang1234-stock-screener` | **STEAL_FROM** | k71 | xang1234/stock-screener | Apache-2.0 — breadth + fundamental filter math only |
| `hl-funding-sniper` | **STEAL_FROM** | k72 | TheSmartApe/hl-funding-sniper | MIT — port into core/hyperliquid_funding; no upstream runtime |
| `ai-polymarket-agent` | **REJECT** | k73 | — | K73 targeted — README scaffold, no license |
| `alsk-cloddsbot` | **STEAL_FROM** | k73 | alsk1992/CloddsBot | K73 batch2 — Node runtime; pattern extraction only |
| `discountifu-websocket-client` | **STEAL_FROM** | k73 | discountifu/polymarket-websocket-client | K73 — protocol reference vs polymarket_ws_client.py |
| `mermaid-skill` | **LAPTOP_ONLY** | k73 | WH-2099/mermaid-skill | K73 audit — local diagram skill for briefs |
| `polymarket-paper-trader` | **STEAL_FROM** | k73 | agent-next/polymarket-paper-trader | K73 batch2 — MCP forward-test; Step 138 partial wrapper exists |
| `probablyprofit` | **STEAL_FROM** | k73 | randomness11/probablyprofit | K73 batch2 — gap-audit Kelly/ensemble vs shipped modules |
| `cve-mcp-server` | **GO** | k76 | mukul975/cve-mcp-server | K76-F — laptop MCP only |
| `discountifu-polymarket-trading-bot` | **STEAL_FROM** | k76 | discountifu/polymarket-trading-bot | K75/K76-A — docs/specs/discountifu-polymarket-steal-from.md |
| `ent0n29-polybot` | **STEAL_FROM** | k76 | ent0n29/polybot | K76-B research only — core/pm_replication_score.py |
| `fuzzyai` | **STEAL_FROM** | k76 | cyberark/FuzzyAI | K76-E — CCC laptop only |
| `mirage-strukto` | **STEAL_FROM** | k76 | strukto-ai/mirage | K76-G — docs/specs/mirage-steal-from.md |
| `pmxt` | **STEAL_FROM** | k76 | pmxt-dev/pmxt | K76-D — fork+pin; PM+Kalshi only |
| `zostaff-poly-arbitrage-bot` | **STEAL_FROM** | k76 | zostaff/poly-arbitrage-bot | K76-C — core/pm_kl_execution/partial_fill.py |

**Manifest entries:** 43 (DEFER=10, GO=3, LAPTOP_ONLY=2, REJECT=7, STEAL_FROM=18, —=3)
<!-- @generated:end tool-adopt-matrix -->
