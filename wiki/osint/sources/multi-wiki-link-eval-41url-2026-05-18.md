---
title: "Cemini Multi-Wiki Link Evaluation Report — 41-URL batch (v3, May 2026)"
type: source
tags: [source, tool-evaluation, multi-wiki-routing, license-audit, k53]
keywords: [multi-wiki-tool-eval, 41-url-batch, gridex, polymarket-trading-bot, poly-arbitrage-bot, graphic-walker, arcticdb, picoclaw, cc-wf-studio, grex, vanguard, hermes-desktop, no-license-epidemic, license-finding-unreliability]
related:
  - entities/tools/gridex.md
  - entities/tools/discountifu-polymarket-trading-bot.md
  - entities/tools/poly-arbitrage-bot.md
  - entities/tools/graphic-walker.md
  - entities/tools/arcticdb.md
  - concepts/cemini-license-posture.md
  - concepts/cross-venue-arbitrage-pattern.md
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - entities/tools/shadowarcanist-netviz.md
maturity: validated
read_status: deep-read
created: 2026-05-18
updated: 2026-06-01
clusters: [tool-evaluation]
---

## Relations

- @entities/tools/gridex.md — URL 29, Adopt (verified Apache-2.0); native DB IDE for the Cemini Postgres/Redis layer
- @entities/tools/discountifu-polymarket-trading-bot.md — URL 30, Adopt (verified MIT); Polymarket CLOB-V2 trading bot
- @entities/tools/poly-arbitrage-bot.md — URL 1, eval Reject **corrected** (verified MIT, not unlicensed); Polymarket↔Kalshi arb bot
- @entities/tools/graphic-walker.md — URL 11, eval Reject **corrected** (verified Apache-2.0, not unlicensed); embeddable visual analytics
- @entities/tools/arcticdb.md — URL 16, eval Reject on BSL **superseded** by the K52 license verification (BSL Additional Use Grant permits Cemini use)
- @concepts/cemini-license-posture.md — this eval is a fresh case of the "don't trust retrieval-gap no-license rejects" lesson
- @concepts/cross-venue-arbitrage-pattern.md — URL 1 (poly-arbitrage-bot) is a concrete implementation of this pattern
- @ccc-wiki/briefs/2026-05-18_k53-tool-eval-ccc-items.md — cross-routed CCC items (cc-wf-studio, picoclaw, git-truck, hermes-desktop, ai-engineer-roadmap)
- @cybersecurity-wiki/briefs/2026-05-18_k53-tool-eval-cybersec-items.md — cross-routed Cybersec items (grex, vanguard, netviz, iOS pentest list)
- @seo-wiki/briefs/2026-05-18_k53-tool-eval-seo-items.md — cross-routed SEO items (colorion, snippeteditor, svgrepo)
- @image-gen-wiki/briefs/2026-05-18_k53-tool-eval-imagegen-items.md — cross-routed Image-gen item (awesome-nano-banana-pro-prompts)
- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — K60 successor v4 20-URL batch; same license-layer failure modes

## Raw Concept

- **Title**: "Cemini Multi-Wiki Link Evaluation Report (v3, May 2026)" — `Multi-Wiki Tool Evaluation.docx`
- **Type**: LLM-generated tool-evaluation report (Gemini DR-style), 41 URLs across 7 wiki surfaces
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Multi-Wiki Tool Evaluation.docx`
- **Retrieved**: 2026-05-18 (dropped into `research to be indexed/`)
- **Structure**: per-URL — URL / license / stars-commits-issues / stack / maturity / tier / primary-fit / 7-wiki routing matrix / cross-wiki routing / reasoning / license risk / NEEDS VERIFICATION. Plus an aggregate summary, primary-fit distribution, cross-routing batch, and a license-pattern summary.

This is K53 — the fourth multi-wiki tool-eval batch in a month (K49 46-repo, K50 56-repo, K51 36-repo, K53 41-URL). Ingested **with verification corrections**: the eval's license layer was spot-checked against the GitHub API and found systematically unreliable on no-license findings (see Narrative).

## Narrative

### Tier rollup (eval's own verdicts)

| Tier | Count | Items |
|---|---|---|
| Adopt | 8 | cc-wf-studio, picoclaw, git-truck, grex, gridex, polymarket-trading-bot, hermes-desktop, vanguard |
| Steal-from | 1 | netviz |
| Defer | 0 | — |
| Reference-only | 6 | awesome-nano-banana-pro-prompts, colorion, snippeteditor, svgrepo, ai-engineer-roadmap, iOS (pentest list) |
| Reject | 22 | (incl. poly-arbitrage-bot, ArcticDB, graphic-walker, polymarket-websocket-client — see corrections) |
| UNAVAILABLE | 4 | obsidian-digital-garden, xpmetric, polymarket-orderbook-watcher, xiaomi-tproxy |

Primary-fit: CCC 12, None 12, Cybersec 6, Cemini-financial 5, SEO 3, OSINT 2, Image-gen 1. ~71% non-OSINT — heavy cross-routing batch.

### Verification corrections — the eval's license layer is unreliable

Spot-checking the eval's license findings against the GitHub API (2026-05-18) exposed a **systematic false-negative**: repos the eval marked "NO LICENSE FOUND" (and Rejected on that basis) are in fact cleanly licensed. The eval reported 17 no-license repos; of the OSINT/Cemini-relevant ones checked, **at least three were wrong**:

| Repo | Eval verdict | GitHub API (verified 2026-05-18) | Corrected |
|---|---|---|---|
| `zostaff/poly-arbitrage-bot` (URL 1) | Reject — "NO LICENSE FOUND" | **MIT**, 20★, active | License-clean → Reference/Steal-from |
| `discountifu/polymarket-websocket-client` (URL 31) | Reject — "NO LICENSE FOUND" | **MIT**, 10★ | License-clean → Reference |
| `Kanaries/graphic-walker` (URL 11) | Reject — "NO LICENSE FOUND" | **Apache-2.0**, 3,137★ | License-clean → Reference |
| `man-group/ArcticDB` (URL 16) | Reject — "BSL poison-pill, paid license required" | BSL 1.1 — Additional Use Grant permits Cemini's internal use (K52 verification) | Reject **superseded** → Adopt-eligible |
| `ridgelinecyberdefence/vanguard` (URL 40) | Adopt — "Apache-2.0" | **MIT** (not Apache) | Tier unaffected; license name corrected |

The eval's *clean-license* claims, by contrast, mostly held (picoclaw MIT/29k★, git-truck MIT, grex Apache-2.0, hermes-desktop MIT, netviz MIT all confirmed). The asymmetry is diagnostic: **the eval finds a LICENSE file reliably but reports a retrieval gap as "no license"** — the exact failure mode already recorded in @concepts/cemini-license-posture.md (the K51 `fd` lesson). Net rule for this batch: trust the eval's tiers as a *starting* shortlist, but treat every "NO LICENSE FOUND → Reject" as unverified — re-check the GitHub API before accepting the rejection.

### OSINT / Cemini-financial items (5)

- **URL 29 `gridex/gridex`** — Adopt. Native macOS/Win/Linux database IDE (Swift/AppKit), connects to PostgreSQL/MySQL/SQLite/Redis; local-first, no Electron, no telemetry. Apache-2.0, 509★ (verified). A laptop-side monitoring tool for the Cemini Postgres backtest DBs + Redis Streams order-book feed. → @entities/tools/gridex.md.
- **URL 30 `discountifu/polymarket-trading-bot`** — Adopt. Async Python Polymarket trading bot: CLOB-V2 order formatting (builder attribution baked in), real-time WebSocket orderbook, 15-min BTC/ETH/SOL handling, PBKDF2+Fernet local key encryption, 103 unit tests. MIT, 67★ (verified). Drop-in-relevant to the `/opt/cemini` Polymarket adapters. → @entities/tools/discountifu-polymarket-trading-bot.md.
- **URL 1 `zostaff/poly-arbitrage-bot`** — eval Reject (no-license) **corrected to MIT**. Cross-exchange Polymarket↔Kalshi arbitrage bot: py-clob-client + EIP-712 signing + Kalshi RSA-PSS auth, SQLite simulated-fill paper-trading, sanity caps + gated live-trading env vars. A concrete implementation of @concepts/cross-venue-arbitrage-pattern.md. → @entities/tools/poly-arbitrage-bot.md.
- **URL 11 `Kanaries/graphic-walker`** — eval Reject (no-license) **corrected to Apache-2.0**. Embeddable visual-analytics web component ("open-source Tableau alternative"), DuckDB-backed, grammar-of-graphics UI, warehouse pushdown (ClickHouse/Snowflake). OSINT-primary: a candidate dashboard layer for the librarian interface and the Cemini backtesting dashboard. → @entities/tools/graphic-walker.md.
- **URL 31 `discountifu/polymarket-websocket-client`** + **URL 32 `discountifu/polymarket-orderbook-watcher`** — same author as URL 30. The websocket-client (eval Reject/no-license → **corrected MIT**, zero-dependency TypeScript CLOB/RTDS client) and the orderbook-watcher (eval UNAVAILABLE → repo exists, genuinely no license, 10★) are documented as sibling repos on the @entities/tools/discountifu-polymarket-trading-bot.md page rather than getting their own pages.

### Cross-routed items (non-OSINT)

Routed to sibling wikis as destination briefs (`scripts/cross_wiki_route.py`):

- **CCC-wiki** — cc-wf-studio (Adopt; Claude Code visual workflow editor; license NOASSERTION/AGPL-or-later, CCC accepts AGPL for laptop-side-only tools), picoclaw (Adopt; sipeed ultra-light local AI framework, MIT, 29k★), git-truck (Adopt; local-first Git visualization, MIT), hermes-desktop (Adopt; Tauri/React GUI for Hermes Agent, MIT — ties to @entities/tools/hermes-agent.md), ai-engineer-roadmap (Reference).
- **Cybersec-wiki** — grex (Adopt; regex-from-examples generator, Apache-2.0), vanguard (Adopt; single-binary DFIR toolkit bundling Velociraptor/Volatility/KAPE/YARA, MIT), netviz (Steal-from; D3 network-graph visualizer, MIT), iOS (Reference; iOS pentest tool list).
- **SEO-wiki** — colorion mobile-palette, snippeteditor, svgrepo (all Reference-only design/asset tools).
- **Image-gen-wiki** — awesome-nano-banana-pro-prompts (Reference; 10k+ Gemini image-gen prompts).

### Caveats

- LLM-generated eval (Gemini DR-style); reasoning is verbose and over-emphatic ("catastrophic," "paradigm-shifting"). Treat tiers as a shortlist, not a verdict.
- License layer verified unreliable on no-license findings (above). Any destination-wiki curator accepting a cross-routed item should re-verify its license via the GitHub API first.
- Star/commit/issue metadata is mostly "NOT FOUND" in the eval — filled in here from the GitHub API where it mattered.

## Snippets

> "Adopt: 8 ... Steal-from: 1 ... Reference-only: 6 ... Reject: 22 ... UNAVAILABLE: 4." [Source: Multi-Wiki Tool Evaluation.docx — Aggregate summary]

> "NO LICENSE FOUND: 17 ... Poison-pill licenses caught: 4 (PHPMailer LGPL-2.1, technomancy-dev/00 AGPL-3.0, man-group/ArcticDB BSL 1.1, pi-hole EUPL-1.2) ... Clean MIT/Apache/BSD: 8." [Source: Multi-Wiki Tool Evaluation.docx — License pattern summary] — note: the "17 NO LICENSE" figure is unreliable; ≥3 verified to be cleanly licensed.

## Dead Ends

- **Do not transcribe this eval's no-license rejections verbatim.** Verified 2026-05-18 that the eval reports retrieval gaps as "NO LICENSE FOUND" — poly-arbitrage-bot, polymarket-websocket-client, and graphic-walker are all cleanly licensed despite the eval's claim. Same failure mode as the K51 `fd` data artifact. Always re-check the GitHub API before accepting a no-license reject.
