---
title: "pmxt — CCXT for prediction markets (unified middleware)"
type: entity
tags: [tool, prediction-markets, polymarket, kalshi, middleware, mcp, adopt, k49, k56]
keywords: [pmxt, ccxt-for-prediction-markets, unified-api, polymarket, kalshi, limitless, hyperliquid, metaculus, gnosis-safe, eip-712, pmxt-mcp, mit-license, 1tb-orderbook-dataset, utility-marketing, samuel-tinnerholm]
related:
  - sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md
  - sources/analyzing-github-projects-agentic-infra-2026-05-21.md
  - entities/tools/polyterm.md
  - concepts/cemini-license-posture.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-football-shock-recovery-trading.md
  - projects/world-cup-bot/Architecture/Architecture - match_shock_pmxt_backtest.md
  - sources/rohonchain-fifa-wc-shock-recovery-strategy-2026-06-02.md
maturity: draft
created: 2026-05-16
updated: 2026-05-21
phase_0_verdict: "CONDITIONAL-GO 2026-05-16 — MIT verified (LICENSE + SPDX in both core/python SDK); real multi-venue adapters confirmed; condition 1: exclude the `baozi` Solana adapter from any cemini-prod build (its `@solana/web3.js` chain pulls LGPL-3.0-only `rpc-websockets` — weak copyleft, dynamic-link OK but cleanest to drop since baozi is not a Cemini target venue); condition 2: vendor-pin the third-party venue SDKs (`@polymarket/clob-client-v2`, `@limitless-exchange/sdk`, etc.) and re-verify their MIT status at integration time; condition 3: single-maintainer (Samuel EF. Tinnerholm) — treat as bus-factor-1, fork-and-pin before depending on it in production"
---

## Relations

- @sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — evaluated in the v3-iteration eval (Adopt tier, Cemini-financial primary fit)
- @sources/analyzing-github-projects-agentic-infra-2026-05-21.md — K56 long-form report adds growth-story + 1TB orderbook open-source dataset
- @entities/tools/polyterm.md — sibling Polymarket tooling; PolyTerm is the terminal/analytics layer, pmxt is the execution-abstraction layer
- @concepts/cemini-license-posture.md — MIT clears the IP-sale copyleft perimeter
- @concepts/cross-venue-arbitrage-pattern.md — pmxt's growth playbook is documented as giving away Kalshi↔Polymarket arbitrage scripts to drive library installs
- @ccc-wiki/entities/mcp-servers/pmxt-mcp-pattern.md — cross-wiki stub: `@pmxt/mcp` exposes prediction-market execution to Claude Code agents

## Raw Concept

Promoted from the 2026-05-16 "Tool Evaluation and Wiki Fit v3 Iteration" 46-repo eval. Tier: **Adopt**. Primary fit: Cemini-financial. Cross-route: CCC-wiki (`@pmxt/mcp`).

- URL: https://github.com/pmxt-dev/pmxt
- License: **MIT** (per report)
- Stars / last commit / open issues: 1700 / 2026-05-15 / 8
- Stack: TypeScript / Python / Node.js

## Narrative

**pmxt** is a unified middleware layer for prediction markets — the **CCXT equivalent** for the prediction-market ecosystem. Prediction markets suffer severe API fragmentation: every platform has its own auth protocol and data schema. pmxt standardizes interactions across **Polymarket, Kalshi, Limitless, Hyperliquid, and Metaculus** into a strict **Event → Market → Outcome** hierarchy with a common Python and TypeScript interface (`create_order`, `fetch_balance`, etc.).

Its key value for the Cemini financial suite: it natively resolves exchange-specific cryptographic auth — **Gnosis Safe signatures** for Polymarket, **EIP-712 signing** for Limitless — eliminating per-platform adapter maintenance. It also ships a `dome-to-pmxt` migration tool for moving off legacy API wrappers, and native `@pmxt/mcp` support so LLM agents can transact on prediction markets directly.

**Cemini fit**: candidate execution-abstraction layer for the `/opt/cemini` trading stack, replacing custom per-venue adapters. The MIT license clears it for the IP sale. Deployment belongs on **cemini-prod**, not the laptop/librarian — staged via adoption brief, not installed from this workspace.

- `[NEEDS VERIFICATION 2026-05-16]` Compatibility of the `dome-to-pmxt` automated migration tool with Cemini's customized Redis Streams data structures. (`tools/dome-to-pmxt/` confirmed present in repo — `index.js` + `package.json` + `README.md`; functional compatibility still untested.)
- `[CONFIRMED 2026-05-16]` Phase-0 clone audit complete — see `## Phase-0 Audit` below. MIT LICENSE present; one weak-copyleft transitive dep (`rpc-websockets` LGPL-3.0-only) isolated to the non-target `baozi` adapter.

## Phase-0 Audit (2026-05-16)

Clone audit per CLAUDE.md § "Phase-0 audit pattern". Repo cloned to `/tmp/pmxt-audit/` (shallow, depth 50). Inspect-only — tools not executed.

### License verification — PASS

- Root `LICENSE`: MIT License, "Copyright (c) 2026 pmxt.dev". Standard unmodified MIT text.
- GitHub `licenseInfo`: `mit` / "MIT License".
- SPDX `"license": "MIT"` declared in `core/package.json` and `license = {text = "MIT"}` in `sdks/python/pyproject.toml`. Python SDK also carries the `License :: OSI Approved :: MIT License` classifier.
- Verdict: MIT confirmed at repo level and in both publishable SDK manifests. Clears the IP-sale copyleft perimeter for pmxt's own code.

### Maturity signals — eval claim vs observed

| Metric | Eval claim | Observed (2026-05-16) | Note |
|--------|-----------|----------------------|------|
| Stars | ~1700 | 1731 | Confirmed |
| Last commit | 2026-05-15 | 2026-05-16 (`pushedAt`) | Confirmed — actively pushing |
| Open issues | 8 | 8 | Exact match |
| Stack | TS/Python | TS (2.46 MB primary) + Python (290 KB SDK) + JS | Confirmed |
| Forks | — | 193 | Healthy ecosystem interest |
| Created | — | 2026-01-08 | ~4-month-old project — young |

### Failure-mode probe (financial execution middleware → cemini-prod, IP-sale-bound stack)

(a) **Real LICENSE = MIT + SPDX** — PASS. See above.

(b) **Dependency license scan** — CONDITIONAL. Scanned `package-lock.json` + `core/package-lock.json` (~1400 resolved deps). License distribution: 1172 MIT, 98 ISC, 30 BSD-3, 21 Apache-2.0, 16 BlueOak-1.0.0, 14 BSD-2, plus a few permissive dual-licenses. **One copyleft hit: `rpc-websockets@9.3.3` declared `LGPL-3.0-only`.** It is a *transitive* dep pulled only via `@solana/web3.js`. `@solana/web3.js` is imported **only** by the `baozi` exchange adapter (`core/src/exchanges/baozi/*`) — none of the Cemini-target venues (Polymarket/Kalshi/Limitless/Hyperliquid/Metaculus are EVM- or REST-based) touch it. LGPL is weak copyleft (dynamic linking via npm does not force relicensing of the consuming app), so it is not an automatic disqualifier — but for an IP-sale-bound proprietary stack the clean move is to exclude `baozi` from the cemini-prod build entirely, which removes the `@solana/web3.js` → `rpc-websockets` chain. No GPL/AGPL/SSPL anywhere; no unlicensed deps found.

(c) **Real adapters vs stub** — PASS. `core/src/exchanges/` contains 15 venue directories, each with its own `auth.ts`, `api*.ts`, order/market modules. Substance check (line counts): polymarket 5034 lines / 10 files, kalshi 4775 / 10, limitless 3151 / 9, metaculus 2024 / 8, hyperliquid 1415 / 7. `polymarket/auth.ts` implements the four real CLOB signature types (EOA / Poly-Proxy / **Gnosis Safe** / ERC-1271) against `@polymarket/clob-client-v2` + `viem`; Limitless/Hyperliquid carry their own `auth.ts` with EIP-712 signing. This is a genuine multi-venue implementation, not a thin wrapper. `@pmxt/mcp` is real but lives in a **separate repo** (`pmxt-dev/pmxt-mcp`, invoked via `npx -y @pmxt/mcp`) — not vendored here, so it needs its own Phase-0 pass before CCC-side adoption.

(d) **Maintenance health** — WEAK. Of the last 50 commits, 33 are by a single human author (Samuel EF. Tinnerholm) and 17 by `github-actions[bot]` (auto-docs/changelog). Effectively a **bus-factor-1 single-maintainer project**, ~4 months old. Commit cadence is high (multiple commits/day through early-mid May) and the version is advancing fast (changelog shows v2.41.6) — active but fragile. For a production execution dependency, fork-and-pin is mandatory.

### Comparison vs existing Cemini coverage

Cemini's `/opt/cemini` stack currently uses custom per-venue adapters. pmxt is a *consolidation* play, not a duplicate: it would replace hand-maintained adapter code with one upstream interface plus the `dome-to-pmxt` migration path. No existing Cemini component overlaps. Sibling tool @entities/tools/polyterm.md is complementary (analytics/view-only layer, not execution).

### Decision — CONDITIONAL-GO

MIT clean for pmxt's own code; real, substantial adapters; the venue + auth claims (Gnosis Safe, EIP-712, five-venue coverage) all verified in source. Three conditions before cemini-prod integration: (1) **exclude the `baozi` Solana adapter** to drop the LGPL-3.0-only `rpc-websockets` transitive dep — trivial since baozi is not a Cemini target; (2) **vendor-pin the third-party venue SDKs** and re-verify their MIT status at integration time (they are upstream-controlled, currently all MIT); (3) **fork-and-pin** — single-maintainer bus-factor-1 means Cemini must not depend on a live upstream. `@pmxt/mcp` is a separate repo and needs its own Phase-0 audit before CCC adoption.

## K56 update (2026-05-21) — growth playbook + 1TB orderbook open-source

The K56 long-form GitHub-projects report adds two material data points not present in the K49 eval source:

### Utility-marketing growth playbook

pmxt grew from zero to 1.8k stars (~500 in 30 days) by **giving away alpha**: the maintainers wrote risk-free Kalshi ↔ Polymarket arbitrage scripts using their own library and published the code freely on `r/algotrading` and similar forums. Users had to install pmxt to run the arbitrage code. The pattern hit GitHub Trending and earned endorsements from Limitless.Exchange + the original founder of CCXT. The library now has ~30,000+ downloads.

This is structurally relevant to Cemini in two ways:
1. **Adoption-funnel pattern**: pmxt's playbook (open-source the execution + give away the strategy to drive installs) is the inverse of what a closed Cemini IP-sale stack does. Useful as adversary-modeling for anyone competing on prediction-market middleware.
2. **The given-away arb itself is documented**: K56 references Reddit threads where the Kalshi↔Polymarket arbitrage opportunities were spelled out. If we need a cross-venue arb baseline for `@concepts/cross-venue-arbitrage-pattern.md`, these public threads are the starting point.

### 1TB orderbook open-source dataset

After saturating the retail-algo demographic, pmxt pivoted to **data democratization**:
- Scraped, archived, and normalized the complete Polymarket orderbook history using their own library
- Open-sourced the dataset starting at **1 TB initial release**, growing by **~0.25 TB/day**
- Goal: destroy the data-vendor paywall for prediction-market history; lock pmxt in as the foundational standard

For Cemini, this is **enormously consequential**. We currently don't have a comprehensive Polymarket orderbook history dataset; this is the canonical free source. Adoption considerations:
- License of the dataset itself: `[NEEDS VERIFICATION 2026-05-21]` — the library is MIT but the dataset distribution may be different. Verify before any commercial use.
- Distribution channel: per K56, the release is on a mirror at `sourceforge.net/projects/pmxt.mirror/` plus the main GitHub. Storage scale (1TB+ growing) makes direct download impractical — likely staged via S3 or torrents.
- Operational fit: a continuously-growing dataset of this scale belongs on **cemini-librarian** (`/opt/cemini-bulk/market-dataset/polymarket-orderbook/`) once we decide to ingest. Not laptop, not cemini-prod. Subsetting + selective sync recommended over full mirror.
- **Action item**: a Phase-0 audit of the dataset's license, format, and update cadence would be valuable. Not blocking any current Cemini workstream.

### Maintainer attribution

K56 also surfaces the maintainer's first-name attribution: **Samuel EF. Tinnerholm** authored the public "How I grew my open-source project from 0 to 500 stars in 30 days" Medium post that documents the utility-marketing playbook. Consistent with the K49 Phase-0 audit observation of single-maintainer bus-factor-1.

## Snippets

> "It standardizes interactions across platforms including Polymarket, Kalshi, Limitless, Hyperliquid, and Metaculus into a strict Event, Market, and Outcome hierarchy ... it natively handles complex, exchange-specific cryptographic requirements, such as Gnosis Safe signatures for Polymarket and EIP-712 signing for Limitless." [Source: Tool Evaluation and Wiki Fit Analysis.docx — URL 4]

> "By effectively giving away pure 'alpha' alongside visual proofs of price discrepancies, they forced users to download the PMXT library to run the code, rapidly boosting their repository from zero to 500 stars within 30 days." [Source: K56 Analyzing GitHub Projects report, PMXT Ecosystem section]

> "The PMXT team utilized their own library to scrape, archive, and normalize the complete Polymarket orderbook. They subsequently open-sourced this massive dataset—starting with an initial 1 Terabyte release that continues to grow by roughly 0.25TB daily." [Source: K56 Analyzing GitHub Projects report, PMXT Ecosystem section]
