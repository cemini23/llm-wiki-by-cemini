---
title: "@AlterEgo_eth — Polymarket Bridge API: 5 deposit/withdrawal endpoints"
type: source
tags: [source, x-post, polymarket, bridge-api, deposits, withdrawals, prediction-markets, k54]
keywords: [polymarket-bridge-api, deposit-endpoints, withdraw, pusd, supported-assets, quote, status, balance-allowance-update, alteregoeth]
related:
  - entities/people/alteregoeth.md
  - entities/tools/polymarket-bridge-api.md
  - concepts/polymarket-api-reference.md
maturity: validated
read_status: read
created: 2026-05-19
updated: 2026-05-19
---

## Relations

- @entities/people/alteregoeth.md — author; this is the fourth ingested @AlterEgo_eth artifact
- @entities/tools/polymarket-bridge-api.md — the API surface this post documents (entity stub)
- @concepts/polymarket-api-reference.md — cross-surface Polymarket endpoint index; this post adds the sixth surface

## Raw Concept

- **Title**: "@AlterEgo_eth — Bridge API: The 5 Endpoints That Handle Deposits in Your Bot"
- **Type**: single X (Twitter) post, technical breakdown
- **Author**: @AlterEgo_eth
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/Post.docx`
- **Retrieved**: 2026-05-19 (dropped into `research to be indexed/`)
- **Read status**: read — short post, fully covered. The doc ends with a "Next Post:" delimiter but contains no second post.

What prompted this page: K54 inbox item. @AlterEgo_eth's earlier cheat sheet (K51, @sources/alterego-eth-polymarket-endpoint-cheatsheet.md) inventoried five Polymarket surfaces — Gamma, Data, CLOB, LB-API, WebSockets. This post documents a **sixth**: the Bridge API, which handles wallet *funding* (deposits and withdrawals) rather than market data or order execution.

## Narrative

The **Bridge API** — `https://bridge.polymarket.com` — is the funding layer: it converts arbitrary on-chain assets into Polymarket's collateral token and back out. The post frames it as essential for any bot that "manages its own funding, not just trading."

### The five endpoints

| Endpoint | Auth | Purpose |
|----------|------|---------|
| `POST /deposit` | public | Create unique deposit addresses for the Polymarket wallet. Returns separate addresses for **EVM, Solana (SVM), and Bitcoin (BTC)**. Addresses are safe to cache and reuse. |
| `GET /supported-assets` | public | Full list of supported tokens with **minimum deposit amounts per chain**. Check before sending funds. |
| `POST /quote` | public | Expected **pUSD output and fees** before making a deposit. |
| `GET /status/{address}` | public | Monitor deposit status by deposit address — poll until confirmed. |
| `POST /withdraw` | public | Create withdrawal addresses to bridge pUSD back to any supported chain/token. |

The post states the whole Bridge API is **public, no auth required**. `[NEEDS VERIFICATION 2026-05-19]` — not yet reproduced against the live API; @AlterEgo_eth's earlier cheat sheet had a demonstrably wrong auth column (it mis-classed CLOB `/book` + `/midpoint` as auth-required), so treat the "no auth" claim as provisional until tested.

### The deposit flow

1. `POST /deposit` → get deposit addresses (EVM / SVM / BTC).
2. `GET /supported-assets` → verify the token and its minimum amount.
3. `POST /quote` → check expected pUSD output and fees.
4. Send funds to the correct address.
5. Poll `GET /status/{address}` until confirmed.
6. Call **CLOB `/balance-allowance/update`** to sync the new funds — the post flags this step as easy to miss; without it the new balance is not visible to the order layer.

### pUSD — the collateral token

Polymarket uses **pUSD (Polymarket USD)** as collateral. All deposited assets are automatically converted to pUSD on Polygon. This is the unit every other Polymarket surface (CLOB balances, order sizing) is denominated in — the Bridge API is the only on-ramp/off-ramp.

### Cemini relevance

Cemini's `/opt/cemini` Polymarket adapter currently handles market data and order execution; if the deployed bot is ever to manage its own treasury (auto-top-up of trading collateral, sweep of realised PnL), this is the surface it would use. The step-6 `/balance-allowance/update` requirement is the kind of integration detail worth recording before it bites — a deposit that "succeeds" but is invisible to the order layer is a silent failure mode. The multi-chain deposit addresses (BTC/SVM/EVM) also matter for funding-source flexibility. Captured as an entity stub (@entities/tools/polymarket-bridge-api.md) and folded into @concepts/polymarket-api-reference.md as surface #6; a funding-flow note is staged for cemini-prod in `briefs/2026-05-19_k54-polymarket-tooling-cemini.md`.

## Snippets

> "If your bot manages its own funding - not just trading, you need Polymarket's Bridge API ... Bridge API - http://bridge.polymarket.com (public, no auth required)." [Source: Post.docx — @AlterEgo_eth]

> "POST /deposit - Create unique deposit addresses for your Polymarket wallet. Returns separate addresses for EVM, Solana (SVM), and Bitcoin (BTC). Safe to cache and reuse." [Source: Post.docx — @AlterEgo_eth]

> "Call CLOB /balance-allowance/update to sync new funds (important!)" [Source: Post.docx — @AlterEgo_eth]

> "Polymarket uses pUSD (Polymarket USD) as collateral. All deposited assets are automatically converted to pUSD on Polygon." [Source: Post.docx — @AlterEgo_eth]
