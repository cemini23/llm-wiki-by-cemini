---
title: "PolyTerm — terminal-native, zero-custody Polymarket analytics"
type: entity
tags: [tool, prediction-markets, polymarket, terminal-ui, analytics, zero-custody, adopt, k49]
keywords: [polyterm, terminal-native, polymarket-analytics, zero-custody, view-only, sqlite, websocket, ascii-charts, arbitrage-scanner, whale-tracking, mit-license]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - entities/tools/pmxt.md
  - entities/tools/polymarket-insider-tracker.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
phase_0_verdict: GO 2026-05-16 — MIT verified (LICENSE + OSI classifier); zero-custody claim CONFIRMED in source (CLOB client is GET-only, no web3/eth_account import, no order-submission or wallet-signing path anywhere; only "key" handled is a read-only Gamma data-API key); dependency tree fully permissive (no copyleft). Single-maintainer (NYTEMODEONLY) — minor bus-factor note, but as a view-only reference tool the risk is low; fork-and-pin still advised for cemini-prod.
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, Cemini-financial primary fit)
- @entities/tools/pmxt.md — sibling Polymarket tooling; pmxt is execution-abstraction, PolyTerm is analytics/journaling
- @entities/tools/polymarket-insider-tracker.md — sibling surveillance tooling; PolyTerm does whale-tracking from order flow, the Insider Tracker does it from on-chain forensics
- @ccc-wiki/entities/tools/polyterm-tui-pattern.md — cross-wiki stub: ASCII depth-chart + TUI navigation as a Claude Code tool-UI template

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: Cemini-financial. Cross-route: CCC-wiki (terminal-UI patterns).

- URL: https://github.com/NYTEMODEONLY/polyterm
- License: **MIT** (per report)
- Stars / last commit / open issues: 256 / 2026-04-28 / 1
- Stack: Python / SQLite / WebSockets

## Narrative

**PolyTerm** is a terminal-native analytics and intelligence layer for Polymarket, built around **deep situational awareness and zero-custody security**. It runs entirely from the command line: a local SQLite database holds trade journals, bookmarks, and market snapshots; WebSockets drive real-time depth displays and ASCII charts. The 73 interactive screens use keyboard navigation shortcuts (e.g. `c15` for crypto markets, `mw`).

Analytics include volume-based **whale tracking**, an internal **Arbitrage Scanner** for intra-market discrepancies (where YES + NO prices sum below $1.00), and multi-factor forecasting (RSI + smart-money positioning + UMA dispute tracking). Its **view-only architecture** means no private keys ever touch the terminal — aligning with institutional opsec.

**Cemini fit**: strategy-backtesting and real-time risk-assessment reference for the `/opt/cemini` stack; the Arbitrage Scanner and forecasting logic are reusable. The TUI/ASCII-chart patterns are a UI template for laptop-side Claude Code tools (cross-routed to CCC). MIT clears the IP sale. Deployment belongs on **cemini-prod** — staged via adoption brief.

- `[NEEDS VERIFICATION 2026-05-16]` WebSocket stability + SQLite write-lock thresholds under extreme-volume events (resolution spikes). (Not testable in a Phase-0 inspect-only audit — requires runtime load testing.)
- `[CONFIRMED 2026-05-16]` Phase-0 clone audit complete — see `## Phase-0 Audit` below. MIT LICENSE present; all dependencies permissive; **zero-custody claim verified in source**.

## Phase-0 Audit (2026-05-16)

Clone audit per CLAUDE.md § "Phase-0 audit pattern". Repo cloned to `/tmp/polyterm-audit/` (shallow, depth 50). Inspect-only — tool not executed.

### License verification — PASS

- `LICENSE`: MIT License, "Copyright (c) 2025 PolyTerm Contributors". Standard unmodified MIT text.
- GitHub `licenseInfo`: `mit` / "MIT License".
- `setup.py` carries the `License :: OSI Approved :: MIT License` classifier. (No SPDX `license=` field in `setup.py`, but the classifier + LICENSE file are unambiguous.)
- Verdict: MIT confirmed. Clears the IP-sale copyleft perimeter.

### Maturity signals — eval claim vs observed

| Metric | Eval claim | Observed (2026-05-16) | Note |
|--------|-----------|----------------------|------|
| Stars | ~256 | 257 | Confirmed |
| Last commit | 2026-04-28 | 2026-04-28 (`pushedAt`) | Exact match |
| Open issues | 1 | 1 | Exact match |
| Stack | Python/SQLite/WebSockets | Python (2.26 MB, 100% of code) | Confirmed; SQLite via `polyterm/db/`, WS via `websockets`/`aiohttp` |
| Forks | — | 51 | Healthy |
| Created | — | 2025-10-14 | ~7-month-old project |
| Version | — | 0.9.1, "Development Status :: 3 - Alpha" | Pre-1.0 / alpha — expect API churn |

### Failure-mode probe (zero-custody / view-only claim is the critical risk)

(a) **LICENSE = MIT + classifier** — PASS. See above.

(b) **Dependency license scan** — PASS. `requirements.txt` lists 13 runtime/test deps: requests (Apache-2.0), aiohttp (Apache-2.0), websockets (BSD-3), gql (MIT), click (BSD-3), rich (MIT), toml (MIT), pandas (BSD-3), python-dateutil (Apache/BSD dual), packaging (Apache/BSD dual), plyer (MIT), plus pytest/pytest-asyncio/pytest-mock/responses (MIT/Apache, test-only). **All permissive — no GPL/AGPL/LGPL/MPL/SSPL.** No copyleft contamination risk.

(c) **Zero-custody / view-only verification — CONFIRMED.** This was the make-or-break probe. Findings:
   - `polyterm/api/clob.py` `CLOBClient` exposes 27 methods — all read-side (`get_price`, `get_order_book`, `get_recent_trades`, `get_ticker`, `get_market_depth`, WebSocket subscribe/listen). The single underlying `_request()` helper is a generic GET/retry wrapper; **no method posts orders.**
   - Repo-wide grep for `requests.post` / `requests.put` / `requests.delete` / `.sign(` / `signTypedData` / `eth_account` / `import web3` / `PRIVATE_KEY` / `getpass`: **the only POST calls in the entire codebase are in `core/notifications.py`** — and they POST to Telegram bot API and Discord webhook URLs (alert delivery), not to any exchange order endpoint.
   - **No `web3`, `eth_account`, or any EVM-signing library is imported anywhere.** It is not even in `requirements.txt`.
   - The only "key" the tool handles is a **Gamma data-API key** (`config.gamma_api_key`), entered via `tui/screens/settings.py` — a read-only market-data credential, not a wallet private key.
   - The many `wallet` / `wallet_address` references are analytics over *other* traders' on-chain addresses (whale tracking, cluster detection, wash-trade detection) — reading public chain data, never holding keys.
   - Conclusion: the "no private keys ever touch the terminal" claim is **literally true in the code**. PolyTerm structurally cannot place a trade or sign a transaction. Risk profile is genuinely view-only.

(d) **Maintenance health** — adequate for tool class. All ~79 commits (shallow window) by a single author (`NYTEMODEONLY` / `nytemodeonly` / `nytemode` — same person, casing variants). Single-maintainer, but as a non-execution, view-only analytics tool the bus-factor risk is low-stakes. Last commit 2026-04-28 ("Release CLOB V2 support for Polymarket cutover") shows it tracked Polymarket's recent CLOB migration — maintainer is responsive to upstream changes. Alpha-stage (v0.9.1) so expect interface churn.

### Comparison vs existing Cemini coverage

Complementary to @entities/tools/pmxt.md (execution-abstraction) and @entities/tools/polymarket-insider-tracker.md (on-chain forensics). PolyTerm's distinct value: terminal-native analytics, the intra-market Arbitrage Scanner (`polyterm/core/arbitrage.py` + `scanner.py` confirmed present), and forecasting logic. No existing Cemini component duplicates it. As a view-only tool it can also run laptop-side safely (its TUI patterns cross-route to CCC), unlike execution tooling which is cemini-prod-only.

### Decision — GO

MIT clean, dependency tree fully permissive, and the critical zero-custody claim is verified in source — PolyTerm has no order-submission or key-handling path and structurally cannot trade. As a view-only analytics/reference tool the single-maintainer and alpha-stage factors are low-risk. Recommend fork-and-pin for any cemini-prod deployment (standard hygiene), and treat the Arbitrage Scanner / forecasting code as reusable reference logic per the original eval.

## Snippets

> "By adopting a view-only architecture, PolyTerm ensures that no private keys ever touch the terminal environment ... an internal Arbitrage Scanner capable of identifying intra-market discrepancies (where YES + NO prices fall below $1.00)." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 8]
