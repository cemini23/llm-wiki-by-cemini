---
title: discountifu/polymarket-trading-bot — async Python Polymarket trading bot
type: entity
tags: [entity, tool, polymarket, trading-bot, prediction-markets, clob-v2, adopt-eligible, k53]
keywords: [polymarket-trading-bot, discountifu, clob-v2, websocket-orderbook, pbkdf2-fernet, gasless-relayer, builder-attribution, mit-license, polymarket-adapter]
related:
  - sources/multi-wiki-link-eval-41url-2026-05-18.md
  - concepts/polymarket-bot-architecture.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @sources/multi-wiki-link-eval-41url-2026-05-18.md — K53 eval URL 30, Adopt tier; the source that surfaced this bot
- @concepts/polymarket-bot-architecture.md — the bot-architecture playbook this codebase is a concrete, MIT-licensed instance of

## Raw Concept

What prompted this page: K53 multi-wiki tool-eval URL 30, tier Adopt, primary fit Cemini-financial. A directly drop-in-relevant Polymarket trading codebase for the `/opt/cemini` adapters.

## Narrative

`discountifu/polymarket-trading-bot` — an **async Python algorithmic trading bot for Polymarket**. Verified 2026-05-18 (GitHub API): **MIT**, ~67★, pushed 2026-04-23, not archived.

Documented features (per the eval):
- **CLOB-V2 order formatting** — builder attribution baked into every order.
- **Real-time WebSocket order-book ingestion**.
- Built-in handling for **ultra-volatile 15-minute crypto markets** (BTC / ETH / SOL).
- **Relayer-backed gasless transaction execution**.
- **PBKDF2 + Fernet** local private-key encryption — no third-party custody.
- **103 unit tests** (pytest) — unusually rigorous coverage for a repo this size.

### Sibling repos (same author)

`discountifu` ships two related repos, both surfaced in the K53 eval:
- `discountifu/polymarket-websocket-client` (URL 31) — zero-dependency TypeScript client for Polymarket CLOB + RTDS, heartbeat + auto-reconnect. Eval marked it "no license / Reject"; **verified MIT** (2026-05-18) — the reject was a retrieval-gap error.
- `discountifu/polymarket-orderbook-watcher` (URL 32) — eval marked UNAVAILABLE; the repo exists (~10★) but **genuinely has no license file** — not adoptable as-is.

### Cemini fit

The CLOB-V2 builder-attribution formatting, WebSocket order-book layer, and 15-minute crypto-market handling map directly onto the Cemini Polymarket adapters and the @concepts/polymarket-bot-architecture.md playbook. The PBKDF2+Fernet local-key pattern is a reusable security primitive. MIT license is IP-sale-clean.

### Verdict

**Adopt-eligible** — license-clean (MIT, verified), high test coverage, directly aligned with the Cemini Polymarket workstream. Server-side adoption (it belongs in the `/opt/cemini` trading stack), so it routes through a `cemini-prod` brief, not a laptop install. Phase-0 follow-up the eval flagged: review the pytest suite for failure-state handling under extreme WebSocket latency before relying on it in production.

## Snippets

> "Features exceptionally rigorous full test coverage (103 discrete unit tests), Relayer-backed gasless transaction execution, and explicit Central Limit Order Book (CLOB) V2 formatting integration." [Source: Multi-Wiki Tool Evaluation.docx — URL 30]
