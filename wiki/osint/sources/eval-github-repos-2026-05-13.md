---
title: "Evaluating GitHub Repositories for Cemini — 14-repo audit (May 13 2026)"
type: source
tags: [source, github-audit, eval, multi-wiki-routing, license-audit, phase-0-audit, k41-adjacent]
keywords: [github-eval-2026-05-13, 14-repo-audit, spdx-license-check, adopt-steal-defer-reject, cross-wiki-routing, mit-apache-safe, agpl-poison-pill, polyform-noncommercial]
related:
  - entities/tools/bukosabino-ta.md
  - entities/tools/tradingview-mcp-atilaahmettaner.md
  - entities/tools/awesome-ai-agents-2026-zijian.md
  - entities/tools/awesome-systematic-trading-paperswithbacktest.md
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
maturity: validated
read_status: deep-read
created: 2026-05-13
updated: 2026-05-13
clusters: [eval, multi-wiki-routing]
---

## Relations
- @3d-printing-wiki/concepts/2026-05-13_gracia-ai-volumetric-3d-export.md  (cross-wiki stub)
- @image-gen-wiki/concepts/2026-05-13_gracia-ai-volumetric-video.md  (cross-wiki stub)
- @cybersecurity-wiki/concepts/2026-05-13_chekusu-mails-dual-use.md  (cross-wiki stub)
- @cybersecurity-wiki/entities/pentest-ai-agents-0xsteph.md  (cross-wiki stub)
- @cybersecurity-wiki/entities/pydns-scanner-xullexer.md  (cross-wiki stub)
- @ccc-wiki/concepts/2026-05-13_multi-codex-codex-home-isolation.md  (cross-wiki stub)
- @ccc-wiki/concepts/2026-05-13_tolaria-steal-from-patterns.md  (cross-wiki stub)

- @entities/tools/bukosabino-ta.md — ADOPT-tier (MIT, 5.1k stars, TA library)
- @entities/tools/tradingview-mcp-atilaahmettaner.md — ADOPT-tier (MIT, 30+ MCP tools)
- @entities/tools/awesome-ai-agents-2026-zijian.md — REFERENCE-ONLY (frontier-model index)
- @entities/tools/awesome-systematic-trading-paperswithbacktest.md — REFERENCE-ONLY (no license, 8.2k stars)
- @concepts/cemini-license-posture.md — IP-sale-readiness lens used in every verdict
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — K43 origin lesson powering the two-gate pattern (bukosabino + tradingview-mcp doc-level ADOPT → Phase-0 NO-GO)

## Raw Concept

- **Format**: docx (Cemini-internal eval document); ~500 substantive lines
- **Date**: May 13, 2026
- **Drop location**: `research to be indexed/Evaluating GitHub Repositories for Cemini.docx` → librarian
- **sha256**: `16464cb905cdc205...`
- **Size**: 3,056,584 bytes
- **Preingest verdict**: NEW

**What prompted this page**: a 14-URL evaluation batch — the largest cross-wiki-routing event observed so far. Touches all 6 sibling wikis (osint, image-gen, seo, 3d-printing, cybersecurity, ccc). Distinct from prior eval-source pages because the cross-routing scope means a meaningful fraction of the verdicts ship out of the OSINT wiki entirely.

## Narrative

### Verdict ladder (Cemini house convention)

- **ADOPT** — install directly, depend on upstream, pin to a known-good commit
- **STEAL-FROM** — patterns only; do not depend on upstream (license usually poison)
- **DEFER** — interesting but unverified license / unclear fit; recheck later
- **REFERENCE-ONLY** — useful as a catalog/index; never code-coupled
- **REJECT** — license-fatal or maturity-fatal; explicit dead-end

### 14 verdicts at a glance

| # | Repo | License | Stars | Verdict | Routes to |
|---|------|---------|-------|---------|-----------|
| 1 | chekusu/mails | MIT | — | ADOPT | osint + cybersec (cross-route brief) |
| 2 | bukosabino/ta | MIT | 5.1k | ADOPT | osint-wiki |
| 3 | atilaahmettaner/tradingview-mcp | MIT | — | ADOPT (30+ MCP tools) | osint-wiki |
| 4 | xullexer/PYDNS-Scanner | MIT | — | ADOPT | cybersec (cross-route stub) |
| 5 | 0xSteph/pentest-ai-agents | MIT | — | ADOPT | cybersec (cross-route stub) |
| 6 | refactoringhq/tolaria | AGPL-3.0 | — | STEAL-FROM (poison-pill) | ccc-wiki (cross-route brief) |
| 7 | Spielewoy/multi-codex | unverified | — | DEFER (CODEX_HOME trick) | ccc-wiki (cross-route brief) |
| 8 | Zijian-Ni/awesome-ai-agents-2026 | MIT | — | REFERENCE-ONLY | osint-wiki (frontier-model index) |
| 9 | gracia.ai | — | — | REFERENCE-ONLY | image-gen + 3d-printing (cross-route brief) |
| 10 | paperswithbacktest/awesome-systematic-trading | (no license) | 8.2k | REFERENCE-ONLY | osint-wiki |
| 11 | paperdraw.dev | none | — | REJECT (no license) | none |
| 12 | anysniper/Frontend | none | — | REJECT (no license) | none |
| 13 | 720kb/angular-socialshare | — | — | REJECT (archived 2022 / obsolete) | none |
| 14 | Gimanh/taskview-community | PolyForm-Noncommercial | — | REJECT (poison-pill non-commercial) | none |

Plus 12 URLs flagged **UNAVAILABLE** (404 / repo-removed / repo-renamed) — `datareaper247/*`, `gripebomb/*`, `alexxxmf/*`, `archasek/*`, etc. These are not REJECTs (no audit possible) and not deferrals (no evidence of future availability) — they're listed for provenance only.

### Cross-routing matrix

| Destination wiki | Routes to it | Page type |
|------------------|--------------|-----------|
| Workflow / ccc-wiki | tolaria (STEAL-FROM), multi-codex (DEFER) | 2 briefs |
| Cybersecurity | mails (dual-use), PYDNS-Scanner (ADOPT), pentest-ai-agents (ADOPT) | 1 brief + 2 stubs |
| OSINT (this wiki) | mails (primary), ta, tradingview-mcp, awesome-ai-agents-2026, awesome-systematic-trading | 4 entity stubs |
| Image-gen | gracia.ai (volumetric video) | 1 brief |
| 3D printing | gracia.ai (Gaussian splatting) | 1 brief (cross-referenced) |
| SEO | (none) | — |

### License-posture observations

- **5 of 5 ADOPTs are MIT** — confirms Cemini's house preference for MIT-licensed third-party dependencies as the IP-sale-readiness path of least resistance.
- **AGPL-3.0** flagged as poison-pill on tolaria — code touching Cemini's distribution surface must avoid AGPL. Patterns extractable, code not.
- **PolyForm-Noncommercial** is a particularly nasty license to encounter — explicitly forbids the commercial-distribution scenario at the core of Cemini's exit thesis. Auto-REJECT on encounter.
- **No-license repos auto-REJECT** under house policy — "no license = no rights granted = legally indistinguishable from copyright-infringement on first commit." paperdraw.dev, anysniper/Frontend both fall here.

### Specific repo notes

**chekusu/mails** (ADOPT, MIT) — AI email parsing on Cloudflare Workers/D1. Dual-use: financial / regulatory mailroom intake (OSINT side) + phishing-domain enumeration (cybersec side). Cross-route brief authored to cybersec-wiki so analysts can pick up the cybersec use-case independently of the OSINT primary entity page.

**bukosabino/ta** (ADOPT, MIT, 5.1k stars) — pure-Python technical-analysis library, 43 indicators. Direct dependency candidate for any Cemini strategy that needs RSI / MACD / Bollinger / Stochastic / ATR / Aroon / etc. Note: `@concepts/polymarket-bot-architecture.md` flags layered-indicator-stack as a documented failure mode; this library is the tool, the strategy discipline is the user's responsibility.

**atilaahmettaner/tradingview-mcp** (ADOPT, MIT) — 30+ MCP tools exposing TradingView screener / indicator / chart APIs. Direct fit for Cemini's MCP-server-tooling pattern. Verify upstream is actively maintained before pinning.

**xullexer/PYDNS-Scanner** (ADOPT, MIT) — async DNS recon with two operational modes: Slipstream (single-host deep scan) and SlipNet (subnet sweep). Cross-route to cybersec-wiki as primary; OSINT-side use is shallower (entity-resolution / domain inventory).

**0xSteph/pentest-ai-agents** (ADOPT, MIT) — shell-only Claude Code subagents for pentest workflows. The "shell-only" constraint is the key insight — no Python deps, just bash + claude-code. Cross-route to cybersec-wiki for the offensive-security subagent design.

**refactoringhq/tolaria** (STEAL-FROM, AGPL-3.0) — refactoring tool with interesting patterns for incremental migrations. AGPL kills upstream-dependency path; patterns only. Cross-route to ccc-wiki for the refactoring-workflow design language.

**Spielewoy/multi-codex** (DEFER) — uses a `CODEX_HOME` env-var isolation trick to run multiple OpenAI Codex CLI instances side-by-side. License unverified; trick may still be extractable even if license is fatal. Cross-route to ccc-wiki for the isolation pattern itself.

**Zijian-Ni/awesome-ai-agents-2026** (REFERENCE-ONLY, MIT) — frontier-model index. Includes entries for **Gemini 3.1 Pro**, **Claude Opus 4.7**, **Gemma 4 31B**, **BenchClaw**. Useful as a periodic-refresh source for the model-orchestra config in `@concepts/agent-cost-routing-model-orchestra.md`.

**gracia.ai** (REFERENCE-ONLY) — Gaussian Splatting volumetric video. Genuinely interesting tech but no clean Cemini route. Cross-route as brief to image-gen-wiki (primary fit) and 3d-printing-wiki (volumetric-mesh-export angle).

**paperswithbacktest/awesome-systematic-trading** (REFERENCE-ONLY, no license but 8.2k stars curated list) — strategy + dataset + tool catalog for quant finance. Index-only — Cemini cannot depend on it (no license), but it's a high-quality discovery source for finding individual repos to audit. Re-audit any candidate from this list under the normal Phase-0 audit pattern.

## Snippets

> "5 of 5 ADOPTs are MIT-licensed. The license-posture filter eliminates most candidates before maturity even matters." [Source: eval-github-repos-2026-05-13.docx — paraphrased]

> "PolyForm-Noncommercial is auto-REJECT — explicitly forbids the commercial-distribution scenario at the core of Cemini's exit thesis." [Source: eval-github-repos-2026-05-13.docx]

## Dead Ends

- **Adopting AGPL-licensed code into Cemini's distribution surface** — re-confirms a known dead end. tolaria has good patterns but AGPL infects the consuming codebase. Patterns extractable, code not.
- **No-license repos** — paperdraw.dev and anysniper/Frontend both fall here. Pre-empts the "interesting code, ship it" reflex.
- **Archived repos** — 720kb/angular-socialshare (archived 2022) is the example. Maturity-fatal regardless of license.
- **Trying to "fix" PolyForm-Noncommercial via fork** — license terms forbid commercial use of the fork too. License is structural, not architectural.
