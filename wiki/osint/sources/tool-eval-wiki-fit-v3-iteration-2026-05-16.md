---
title: "Cemini Infrastructure & Ecosystem Tooling Evaluation — v3 Iteration (46-repo batch, May 2026)"
type: source
tags: [source, tool-evaluation, phase-0-audit, multi-wiki-routing, license-audit, adopt-stealfrom-reject, k49]
keywords: [tool-eval-v3-iteration, 46-repo-batch, 12-detailed, license-poison-pill, cross-wiki-routing, ip-sale-perimeter, mcp-convergence, prediction-market-tooling, polymarket-kalshi, llm-generated-eval]
related:
  - entities/tools/pmxt.md
  - entities/tools/polyterm.md
  - entities/tools/polymarket-insider-tracker.md
  - entities/tools/socid-extractor.md
  - concepts/cemini-license-posture.md
  - sources/tool-evaluation-wiki-fit-2026-05-15.md
maturity: validated
read_status: deep-read
created: 2026-05-16
updated: 2026-05-16
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/pmxt.md — Adopt-tier; CCXT-for-prediction-markets middleware (financial primary fit)
- @entities/tools/polyterm.md — Adopt-tier; terminal-native Polymarket analytics (financial primary fit)
- @entities/tools/polymarket-insider-tracker.md — Adopt-tier; on-chain "informed money" surveillance (financial primary fit)
- @entities/tools/socid-extractor.md — Adopt-tier; cross-platform social-account identifier extraction (OSINT primary fit)
- @concepts/cemini-license-posture.md — the IP-sale copyleft posture this eval enforces
- @sources/tool-evaluation-wiki-fit-2026-05-15.md — prior 52-URL eval batch (K48); this v3 iteration is the successor batch
- @cybersecurity-wiki/entities/tools/jadx-mcp-server.md — Adopt-tier, cybersec primary fit (cross-routed)
- @cybersecurity-wiki/entities/tools/osmedeus.md — Adopt-tier, cybersec primary fit (cross-routed)
- @ccc-wiki/entities/tools/claude-for-legal.md — Steal-from tier, CCC primary fit (cross-routed)
- @ccc-wiki/entities/tools/skillkit.md — Adopt-tier, CCC primary fit (cross-routed)
- @3d-printing-wiki/entities/tools/rebot-devarm.md — Steal-from tier, 3D-printing primary fit (cross-routed)

## Raw Concept

- **Title**: Cemini Infrastructure and Ecosystem Tooling Evaluation Report: v3 Iteration
- **Type**: LLM-generated multi-wiki link-evaluation report (Gemini Deep Research style)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Tool Evaluation and Wiki Fit Analysis.docx`
- **Retrieved**: 2026-05-16 (dropped into `research to be indexed/`)
- **Scope**: 46 repositories / articles / toolkits curated against Cemini's operational, legal, and architectural requirements. 12 were available for detailed evaluation; 34 returned UNAVAILABLE (link-resolution failures or unreachable repos).
- **Verdict basis**: license verification, maturity signals (stars / last commit / open issues), stack fit, cross-wiki routing, IP-sale copyleft contamination risk.

This is the successor to the K48 52-URL "Tool Evaluation and Wiki Fit" eval (`@sources/tool-evaluation-wiki-fit-2026-05-15.md`). It is a **doc-level evaluation** — verdicts derive from the report's research, not from a Cemini Phase-0 source audit. Phase-0 audits remain pending for adopted tools per CLAUDE.md.

## Narrative

### Strategic synthesis

Two ecosystem trends dominate the batch:

1. **MCP convergence** — the Model Context Protocol is being pushed into traditionally human-driven, specialized domains: Android reverse-engineering decompilers (`jadx-mcp-server`), offensive-security orchestration (`osmedeus`), prediction-market CLOBs (`pmxt`'s `@pmxt/mcp`), and skill-management bridges (`skillkit`). LLM agents are shifting from passive code generators to **state-aware operators** of live trading, security, and analysis environments.
2. **Prediction-market institutionalization** — tooling around Polymarket/Kalshi has matured from browser interfaces toward microsecond-sensitive arbitrage, zero-custody terminals, and on-chain whale-surveillance using statistical clustering (DBSCAN). Informational asymmetry in prediction markets is now an engineering target.

Against this, the eval enforces Cemini's **zero-tolerance copyleft posture** for the impending IP sale: GPL-3.0 on production-bearing code and absent SPDX declarations are treated as toxic-acquisition risks regardless of technical merit. See `@concepts/cemini-license-posture.md`.

### Verdict ledger (12 detailed)

| # | Tool | License | Tier | Primary fit | Cross-route |
|---|------|---------|------|-------------|-------------|
| 1 | Remote Process Write Primitive via APC Routines (Medium article) | NO LICENSE | Reference-only | Cybersec | OSINT |
| 2 | claude-for-legal | Apache-2.0 | Steal-from | CCC | OSINT |
| 3 | Polymarket-Kalshi Arbitrage Bot | NO LICENSE | **Reject** | Cemini-financial | CCC |
| 4 | pmxt | MIT | **Adopt** | Cemini-financial | CCC |
| 5 | OctoBot-Prediction-Market | GPL-3.0 | **Reject** | None | None |
| 6 | Polymarket Insider Tracker | MIT | **Adopt** | Cemini-financial | OSINT |
| 7 | jadx-mcp-server | Apache-2.0 | **Adopt** | Cybersec | CCC |
| 8 | PolyTerm | MIT | **Adopt** | Cemini-financial | CCC |
| 9 | Osmedeus | MIT | **Adopt** | Cybersec | CCC |
| 10 | socid-extractor | MIT | **Adopt** | OSINT | Cybersec |
| 11 | SkillKit | Apache-2.0 | **Adopt** | CCC | None |
| 12 | reBot-DevArm | CERN-OHL-W-2.0 / Apache-2.0 | Steal-from | 3D-printing | None |

**Aggregate**: Adopt 7 · Steal-from 2 · Reference-only 1 · Reject 2 · UNAVAILABLE 34.

### Rejections (copyleft / no-license poison pills)

- **Polymarket-Kalshi Arbitrage Bot** (`Composio-HQ/polymarket-kalshi-arbitrage-bot`) — operationally on-target (15-minute-market latency arbitrage; late-resolution arb between settled Kalshi and still-open Polymarket), but **no LICENSE file** → defaults to full copyright → automatic Reject for IP-sale surfaces. Re-check trigger: if maintainers later add MIT/Apache-2.0, tier upgrades to Adopt.
- **OctoBot-Prediction-Market** (`Drakkar-Software/OctoBot-Prediction-Market`) — Polymarket copy-trading + risk-free-arb on a clean Python/Docker stack, but **GPL-3.0** on production financial code = hard reject. Evaluation pipeline terminated; no cross-wiki documentation (copyleft negates pattern reuse).

### Financial-fit adopts (→ cemini-prod)

- **pmxt** — "CCXT for prediction markets"; unifies Polymarket/Kalshi/Limitless/Hyperliquid/Metaculus into one Event/Market/Outcome interface; natively handles Gnosis Safe + EIP-712 signing. MIT. See `@entities/tools/pmxt.md`.
- **PolyTerm** — terminal-native, zero-custody Polymarket analytics; SQLite-backed journal, WebSocket depth, ASCII charts, intra-market arb scanner (YES+NO < $1.00). MIT. See `@entities/tools/polyterm.md`.
- **Polymarket Insider Tracker** — PostgreSQL/Redis surveillance engine; detects "Fresh Wallets" (<5 lifetime txns, >$1k position) and DBSCAN "Sniper Clusters"; funding-chain analysis traces capital to CEX hot wallets. MIT. See `@entities/tools/polymarket-insider-tracker.md`.

### OSINT-fit adopt (→ laptop + librarian)

- **socid-extractor** — Python library parsing stable internal identifiers (Google GAIA IDs, Facebook UIDs, Instagram `pk`) across 130+ platforms via plain HTTP (no headless browser). MIT. Adopted locally (laptop `~/tools/` + librarian) this ingest. See `@entities/tools/socid-extractor.md`.

### Cross-routed (cybersec / CCC / 3D-printing)

- **jadx-mcp-server**, **Osmedeus** → cybersec-wiki (Android RE automation; security orchestration with ACP subprocess agents). Apache-2.0 / MIT.
- **claude-for-legal**, **SkillKit** → CCC-wiki (managed-agent cookbooks + Trust Layer; cross-agent skill translation + MCP discovery). Apache-2.0.
- **reBot-DevArm** → 3D-printing-wiki (6-DOF arm BOM, infill profiles, hybrid CNC/3D-print methodology). CERN-OHL-W-2.0 hardware / Apache-2.0 software.

### Caveats

- **Doc-level only**: stars/commit counts and feature claims come from the report's research, not independent verification. Phase-0 audits (clone, license-verify, failure-mode probe) still owed before any code lands on cemini-prod.
- **34 UNAVAILABLE**: the bulk of the 46-repo batch did not resolve — many are awesome-lists and prior-batch duplicates (e.g. `awesome-polymarket-tools-harish-garg`, `awesome-prediction-market-tools-aarora4` already have wiki pages). No action; not re-evaluated.
- **NEEDS VERIFICATION** items flagged per-tool on the entity pages (DBSCAN latency, dome→pmxt migration, etc.).

## Snippets

> "Tools historically constrained to localized, human-driven execution — such as Android reverse-engineering debuggers, prediction market central limit order books (CLOBs), and offensive security orchestration engines — are systematically exposing state boundaries to Large Language Models (LLMs) via standardized interfaces." [Source: Tool Evaluation and Wiki Fit Analysis.docx — Strategic Synthesis]

> "Repositories utilizing the GNU General Public License v3.0 (GPL-3.0) for production-bearing code, or those lacking explicit SPDX license declarations entirely, present toxic acquisition risks and mandate immediate architectural rejection regardless of their technical merit or operational utility." [Source: Tool Evaluation and Wiki Fit Analysis.docx — Strategic Synthesis]

> Aggregate: "Adopt: 7 · Steal-from: 2 · Defer: 0 · Reference-only: 1 · Reject: 2 · UNAVAILABLE: 34." [Source: Tool Evaluation and Wiki Fit Analysis.docx — Aggregate summary]
