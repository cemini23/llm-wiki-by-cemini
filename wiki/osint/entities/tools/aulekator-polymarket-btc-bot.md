---
title: "aulekator/Polymarket-BTC-15-Minute-Trading-Bot — 15-minute BTC algorithmic trading framework"
type: entity
category: tool
tags: [entity, tool, trading-bot, nautilustrader, polymarket, btc, prediction-markets, k44, no-go-phase-0-2026-05-14, steal-from-adapter-only, abandoned-after-pump, missing-license]
keywords: [polymarket-btc-bot, nautilustrader, redis-state, binance-websocket, coinbase-rest, prometheus-grafana, 15min-bar, mit-license-unverified, py-clob-client-sdk, gamma-api-monkey-patch, abandoned-after-pump]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
maturity: validated
created: 2026-05-14
updated: 2026-05-14
---

## Relations
- @sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — source of this verdict (K44)
- @entities/tools/polymarket-clob-api.md — execution path overlaps; bot may complement K43 Gamma+CLOB integration brief
- @entities/tools/polymarket-gamma-api.md — market-discovery layer; bot's Polymarket dependency points to either Gamma or CLOB
- @concepts/three-formula-system-polymarket-rare-events.md — bot is a 15-min bar pipeline; rare-event system operates on different timescale, complementary rather than competing
- @concepts/cemini-license-posture.md — MIT clean, IP-sale-safe (doc-level)
- @concepts/multi-wiki-eval-doc-level-vs-phase-0.md — gate that must clear before Cemini adoption

## Raw Concept

A 15-minute BTC trading framework wrapping the NautilusTrader open-source quant core, with Binance WebSocket + Coinbase REST data ingestion, Redis state management, Prometheus/Grafana observability, and **a Polymarket adapter** of unspecified depth. From K44 doc-level eval (May 14, 2026): MIT license, 274 stars, claimed "highly functional algorithmic framework integrating professional-grade backtesting and real-time observability telemetry."

**What prompted this page**: K44 eval positioned this as the single Adopt-tier item with **Cemini-financial as primary fit** — the only K44 candidate that directly augments `/opt/cemini` rather than CCC/Cybersec/SEO. Also lands as the most direct follow-up to the K43 Gamma+CLOB integration brief (shipped to cemini-prod 2026-05-13).

## Narrative

### Verdict snapshot (post-Phase-0, 2026-05-14)

| Dimension | Value | Status |
|-----------|-------|--------|
| Verdict | **Adopt** (doc-level) → **NO-GO** (Phase-0 2026-05-14) | Phase-0 audit |
| Adapter sub-verdict | **STEAL-FROM** (Polymarket adapter code is reusable) | Phase-0 G3 PASS |
| License | **NO LICENSE FILE** (MIT claim unverified) | **Phase-0 G2 FAIL** |
| Stars | 281 (vs claimed 274) | Phase-0 G1 OK |
| Last code commit | **2026-02-22 (78d stale; metadata-only push 2026-05-14)** | **Phase-0 G1 abandoned-after-pump** |
| Contributors | 1 (single-maintainer) | Phase-0 G1 single-bus-factor |
| Project age | Created 2026-02-15 (~90d) | Phase-0 G1 OK |
| Stack | Python 3.14+, NautilusTrader 1.222.0, Redis 7.1.1, Prometheus, Grafana | **VERIFIED** |
| Polymarket adapter | **py-clob-client 0.34.5 SDK + Gamma API monkey-patch** (TOS-compliant) | Phase-0 G3 PASS |
| Primary fit | Cemini-financial | K44 eval |
| Cross-routes | OSINT (data ingestion schemas), CCC (skeleton patterns) | K44 eval |
| Cemini status | **NO-GO** for bot adoption; **STEAL-FROM** for adapter code only | Phase-0 verdict |

### What the doc-level eval claims

- **7-Phase architecture** built on NautilusTrader core
- **Binance WebSocket** + **Coinbase REST** data ingestion
- **Redis backend** for configuration + state management
- **Prometheus metrics + Grafana dashboards** for live strategy monitoring
- **Optional Solana RPC support** for multi-chain blockchain data (flagged as needs-verification in K44 itself)
- Polymarket dependency exists but **the eval does not specify which API surface (Gamma vs CLOB) it depends on**

### Why this matters for K44

This is the **single most operationally aligned K44 candidate** for the existing Cemini trading stack:

1. NautilusTrader is the same quant core Cemini has been evaluating (per ROADMAP nautilus-trader thread) — convergent dependency choice reduces integration risk.
2. The Polymarket adapter is **the missing link in the K43 Gamma+CLOB integration**: K43 shipped infrastructure for market discovery + execution; this bot provides a working strategy template that exercises both.
3. The Prometheus+Grafana stack aligns with the existing Cemini observability posture.

### Phase-0 audit verdict (2026-05-14)

| # | Gate | Status | Finding |
|---|------|--------|---------|
| G0 | Repo discovery | **PASS** | `aulekator/Polymarket-BTC-15-Minute-Trading-Bot` exists with exact name |
| G1 | Star + maturity | **CONDITIONAL FAIL** | 281 stars verified, BUT single-maintainer + monolithic single-commit (2026-02-22) + zero commits in 78 days = textbook abandoned-after-pump |
| G2 | License verification | **FAIL** | **No LICENSE file in repo**; MIT claim from K44 eval is unverified — auto-reject under Cemini house policy |
| G3 | Polymarket adapter | **PASS** (TOS-safe) | py-clob-client 0.34.5 SDK for CLOB execution + Gamma API monkey-patch for market discovery. No scraping. Env-var credentials only. Architecture is **production-grade** even though bot is abandoned |
| G4 | NautilusTrader version | **PASS** | Pinned to 1.222.0 release tag, not forked, upstream-trackable |
| G5 | Python 3.14+ requirement | **PASS-burdensome** | Hard-required (3.14 confirmed via .pyc). Cemini-prod on 3.12/3.13 = upgrade burden |
| G6 | Binance/Coinbase TOS | **PASS** | Public WebSocket/REST endpoints only; no API keys in code/config; env-var pattern correct |
| G7 | Backtesting harness | **FAIL** | No BacktestEngine usage; live-trading-only; 15-min bar strategy unvalidated against history; only unit tests, no historical replay |
| G8 | Failure modes / credential hygiene | **MEDIUM-RISK** | No hardcoded keys, env-vars only, no `.env` in git ✓. BUT: single-thread async with no documented crash recovery |
| G9 | "7-Phase architecture" claim | **UNSUPPORTED** | README diagram only; never enumerates the 7 phases. Marketing language, not engineering spec |
| G10 | Solana RPC support | **VAPORWARE** | `data_sources/solana/rpc.py` (280 LOC Pyth stub) exists but never integrated into `bot.py`; no test coverage |

**Verdict: NO-GO for bot adoption** (license + abandoned-codebase blockers).
**Sub-verdict: STEAL-FROM for Polymarket adapter** (py-clob-client integration + Gamma monkey-patch are clean and reusable).

### Polymarket adapter — what to steal (the only Adopt-tier signal in this repo)

If Phase-0 has cleared the adapter even though the bot fails, the load-bearing code paths worth extracting are:

1. **`execution/polymarket_client.py`** — direct py-clob-client SDK wrapper. EOA signature-based auth. Order lifecycle: `create_order()` → sign → `post_order()` → `get_orders()` → `cancel_order()`. Drop-in for Cemini's K43 CLOB execution layer.

2. **`patch_gamma_markets.py`** — monkey-patch for NautilusTrader's `PolymarketInstrumentProvider`. Fixes array-parameter handling for slug-based filtering. Critical if Cemini uses NautilusTrader as the strategy host. Otherwise, the underlying Gamma API call pattern is the part worth copying.

3. **`nautilus_polymarket_integration.py`** — config-driven integration glue. Shows the env-var contract (`POLYMARKET_PK`, `POLYMARKET_API_KEY`, `POLYMARKET_API_SECRET`, `POLYMARKET_PASSPHRASE`, `POLYMARKET_FUNDER`).

4. **Signal processors** (spike_detector, sentiment, divergence) — multi-signal fusion patterns. Less directly applicable than the adapter, but reusable as a reference for combining bar-close BTC signals with prediction-market sentiment.

**What NOT to steal**:

- The monolithic `bot.py` (1,463 LOC, 36 classes/functions in one file) — abandoned, no modular phase decomposition
- The Solana RPC code — unused, untested, integration path unclear
- The strategy logic itself — never backtested; cannot trust without independent validation

### Relationship to existing K43 Polymarket work

- **K43 Gamma+CLOB integration brief** (shipped to cemini-prod 2026-05-13): provided the read/discovery + execution endpoint reference. This bot, if it clears Phase-0, would consume those same endpoints from a NautilusTrader strategy module.
- **Three-formula synthesis system** (`@concepts/three-formula-system-polymarket-rare-events.md`): operates on **per-market rare-event sizing** with quarter-Kelly. This bot is a **15-min bar-frequency strategy** — different timescale, different signal source. Complementary, not competing.
- **K43 follow-up `three-formula synthesis backtest`** (PENDING per hot.md): if this bot uses hftbacktest or has its own backtest harness, may serve as the backtest substrate, partially unblocking that follow-up.

## Snippets

> "This asset is a flawless match for the Cemini financial suite. It deploys a 7-Phase architecture utilizing the NautilusTrader core, powered by a localized Redis backend for configuration and state management."
[Source: Tool Evaluation for Cemini Wiki Integration.docx ¶61]

> "NEEDS VERIFICATION: Confirm the stability of the optional Solana RPC support within the blockchain data ingestion module before authorizing multi-chain live trading."
[Source: ibid ¶63]

## Dead Ends

- **K44 doc-level Adopt verdict failed at Phase-0** — this is the 3rd K43/K44-class doc-level→Phase-0 failure (joining bukosabino/ta + tradingview-mcp). The pattern is now thoroughly established: doc-level eval is **necessary but never sufficient**. The K44 eval correctly identified an interesting Polymarket-NautilusTrader integration but missed the abandoned-after-pump signals + missing LICENSE.
- **No-license repo is auto-Reject under house policy** ("no license = no rights granted"). Even with a TOS-clean Polymarket adapter, the surrounding code cannot be redistributed or relicensed without owner consent. STEAL-FROM the adapter via clean-room reimplementation, do not vendor or fork.
- **Abandoned-after-pump pattern** — 281 stars accumulated in 3 months on a project with **a single commit and zero post-launch maintenance** is the textbook HN-spike-then-silence signal. Trust the maturity signal, not the star count. Phase-0 G1 caught this where a doc-level eval would not have.
- **The Polymarket adapter being clean does NOT save the bot.** Adopt-tier requires the whole package (license + maintenance + tests). Adapter-only quality is a STEAL-FROM result, not an Adopt rescue.
- **"7-Phase architecture" was marketing language** — the README diagram never enumerates the 7 phases. When eval docs use suspiciously specific N-phase numbering with no formal spec, treat as evidence-of-LLM-hallucination-or-author-marketing.
- **Solana RPC was correctly flagged in the K44 eval itself** as needs-verification — Phase-0 confirmed it as vaporware. When the eval doc itself raises a flag, take it seriously.
