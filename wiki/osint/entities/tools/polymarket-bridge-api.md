---
title: Polymarket Bridge API (bridge.polymarket.com)
type: entity
tags: [entity, tool, polymarket, bridge-api, deposits, withdrawals, funding, prediction-markets, k54]
keywords: [polymarket-bridge-api, deposit, withdraw, supported-assets, quote, status, pusd, balance-allowance-update, multi-chain-funding]
related:
  - sources/alterego-eth-polymarket-bridge-api.md
  - concepts/polymarket-api-reference.md
  - entities/tools/polymarket-clob-api.md
  - entities/platforms/polymarket.md
maturity: draft
created: 2026-05-19
updated: 2026-05-19
---

## Relations

- @sources/alterego-eth-polymarket-bridge-api.md — origin source (@AlterEgo_eth X post, K54)
- @concepts/polymarket-api-reference.md — cross-surface Polymarket endpoint index; Bridge is surface #6
- @entities/tools/polymarket-clob-api.md — the funding flow ends with a CLOB `/balance-allowance/update` call
- @entities/platforms/polymarket.md — the venue

## Raw Concept

What prompted this page: K54 ingest of @AlterEgo_eth's Bridge API post. The Bridge API is the **sixth Polymarket surface** — wallet funding (deposits/withdrawals) — not previously cataloged alongside Gamma / Data / CLOB / LB-API / WebSockets.

## Narrative

`https://bridge.polymarket.com` — the **funding layer**: converts arbitrary on-chain assets into Polymarket's collateral token (**pUSD**) and bridges pUSD back out. Reported as public, no auth required `[NEEDS VERIFICATION 2026-05-19]`.

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/deposit` | POST | Create unique deposit addresses (EVM / Solana / Bitcoin). Cacheable, reusable. |
| `/supported-assets` | GET | Supported tokens + minimum deposit amount per chain. |
| `/quote` | POST | Expected pUSD output + fees for a deposit. |
| `/status/{address}` | GET | Deposit status by deposit address — poll until confirmed. |
| `/withdraw` | POST | Create withdrawal addresses to bridge pUSD back to any supported chain/token. |

**Deposit flow**: `POST /deposit` → `GET /supported-assets` (verify token + minimum) → `POST /quote` → send funds → poll `GET /status/{address}` → **CLOB `/balance-allowance/update`** to sync the new balance into the order layer.

**pUSD** — Polymarket's Polygon-based collateral token. All deposited assets auto-convert to pUSD; every other surface (CLOB balances, order sizing) is denominated in it.

### Cemini posture

Relevant only if the deployed `/opt/cemini` bot is to manage its own treasury — auto-top-up of collateral, sweep of realised PnL. The critical integration detail: step 6 (`/balance-allowance/update`) is mandatory; a deposit that confirms on-chain but skips this call is invisible to the order layer — a silent funding failure. Multi-chain deposit addresses (BTC/SVM/EVM) give funding-source flexibility. Not currently in scope for Cemini's adapter; documented for the funding-flow note in `briefs/2026-05-19_k54-polymarket-tooling-cemini.md`.

`[NEEDS VERIFICATION 2026-05-19]` — the "no auth required" claim and the endpoint shapes are from a single X post; @AlterEgo_eth's prior cheat sheet had a wrong auth column. Reproduce against the live API before relying on this.
