---
title: "aulekator/Polymarket-BTC-15-Minute-Trading-Bot — 15-minute BTC algorithmic trading framework"
type: entity
category: tool
tags: [entity, tool, trading-bot, nautilustrader, polymarket, btc, prediction-markets, k44, adopt-doc-level-pending-phase-0]
keywords: [polymarket-btc-bot, nautilustrader, redis-state, binance-websocket, coinbase-rest, prometheus-grafana, 15min-bar, mit-license]
related:
  - sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-gamma-api.md
  - concepts/three-formula-system-polymarket-rare-events.md
  - concepts/cemini-license-posture.md
  - concepts/multi-wiki-eval-doc-level-vs-phase-0.md
maturity: adopt-doc-level-pending-phase-0
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

### Verdict snapshot (doc-level, K44)

| Dimension | Value | Source |
|-----------|-------|--------|
| Verdict | **Adopt** (doc-level) | K44 eval |
| License | MIT | K44 eval (UNVERIFIED at source level) |
| Stars | 274 | K44 eval (UNVERIFIED) |
| Last commit | NOT FOUND | K44 eval |
| Stack | Python 3.14+, NautilusTrader, Redis, Grafana, Prometheus | K44 eval |
| Primary fit | Cemini-financial | K44 eval |
| Cross-routes | OSINT (data ingestion schemas) | K44 eval |
| Cemini status | **doc-level-pending-phase-0-2026-05-14** | this page |

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

### Phase-0 audit gates (must clear before adoption)

| # | Gate | Method | Block |
|---|------|--------|-------|
| G1 | **Star + maturity verification** | `gh api repos/aulekator/Polymarket-BTC-15-Minute-Trading-Bot` — confirm 274 stars, last commit date, contributor count | If commit history is <30 days old or last commit >180 days stale, downgrade to Defer |
| G2 | **License verification** | `gh api repos/.../license` + read LICENSE file | If not actually MIT, escalate to Reject |
| G3 | **Polymarket adapter audit** | Read repo, identify whether Polymarket ingestion uses Gamma, CLOB, or unofficial scraping | Scraping ⇒ TOS-gate (same class as tradingview-mcp NO-GO 2026-05-13) |
| G4 | **NautilusTrader version pinning** | Check `requirements.txt` / `pyproject.toml` for NautilusTrader version | Pinning to a fork or unreleased commit ⇒ Defer |
| G5 | **Python 3.14+ requirement** | Confirm Python 3.14 actually required (3.14 is bleeding-edge for May 2026); validate /opt/cemini Python version | Incompatible ⇒ requires either downgrade-and-test or Defer |
| G6 | **Binance / Coinbase commercial-TOS audit** | Both data feeds have commercial-use clauses; confirm bot's usage pattern is compatible with Cemini's anticipated IP-sale (i.e., does the buyer inherit the API keys?) | TOS-fail ⇒ Steal-from (extract architecture only) |
| G7 | **Backtesting realism** | Read the backtest harness; confirm it uses tick or order-book data, not just bar-close (15-min bars alone are too coarse for prediction-market sentiment overlay) | Bar-close-only ⇒ adapter incomplete |

### Reconsideration / upgrade gates

Verdict upgrades to **GO** if Phase-0 audit clears **all** of: G1 + G2 + G3 (no scraping) + G6 (commercial-TOS clean for IP-sale).

Verdict downgrades to **STEAL-FROM** if any of: G3 reveals scraping; G6 reveals incompatible commercial TOS; G4 reveals unreleased-fork dependency.

Verdict downgrades to **DEFER** if G1 reveals stale repo (>180d) or unstable maturity signal.

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

- **K44 eval does not specify the Polymarket adapter's API surface.** Whether it integrates with Gamma (REST, market-discovery), CLOB (REST + WS, execution), or both is unknown from the doc-level eval. This is Phase-0 gate G3.
- **Repo URL `https://github.com/aulekator/Polymarket-BTC-15-Minute-Trading-Bot` not yet verified to exist.** K44 eval claims a 274-star MIT repo but provides no last-commit date or contributor count; standard K43-style doc-level skepticism applies. Phase-0 gate G1 covers this.
