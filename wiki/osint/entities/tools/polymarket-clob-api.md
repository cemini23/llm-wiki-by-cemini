---
title: "Polymarket CLOB API"
type: entity
tags: [tool, polymarket, api, clob, execution, order-book, hmac, public-reads]
keywords: [clob-api, polymarket-execution, token_id, order-book, midpoint, spread, fee-rate, tick-size, server-time, nonce, hmac-auth, post-order]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-python-order-utils.md
  - entities/tools/aulekator-polymarket-btc-bot.md
  - entities/tools/awesome-polymarket-tools-harish-garg.md
  - sources/alterego-eth-polymarket-gamma-vs-clob.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
  - entities/tools/polymarket-data-api.md
  - entities/tools/polymarket-websocket-api.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-api-reference.md
maturity: validated
created: 2026-05-13
updated: 2026-05-18
---

## Relations

- @entities/platforms/polymarket.md — execution venue
- @entities/tools/polymarket-gamma-api.md — paired discovery-layer API (Gamma → token_id → CLOB)
- @entities/tools/polymarket-python-order-utils.md — official client; canonical signer for POST /order
- @entities/tools/aulekator-polymarket-btc-bot.md — K44 NautilusTrader-based bot; Polymarket adapter path TBD (Phase-0 G3)
- @entities/tools/awesome-polymarket-tools-harish-garg.md — K44 CC0 directory referencing CLOB tooling
- @sources/alterego-eth-polymarket-gamma-vs-clob.md — primary source for the public-vs-auth endpoint split
- @sources/alterego-eth-polymarket-endpoint-cheatsheet.md — K51 @AlterEgo_eth cheat sheet; added `/markets/{conditionId}`, `/orders`, batch + cancel
- @entities/tools/polymarket-data-api.md — sibling analytics layer (post-trade positions/PnL)
- @entities/tools/polymarket-websocket-api.md — realtime push layer over the same CLOB order book
- @concepts/polymarket-bot-architecture.md — bot playbook; 6-layer websocket system applies on top of CLOB reads
- @concepts/polymarket-api-reference.md — canonical five-surface endpoint index CLOB is part of

## Raw Concept

What prompted this page: the @AlterEgo_eth ingest (2026-05-13) clarified that **CLOB read endpoints are public** (no auth) — only trading endpoints (POST /order, cancels) require HMAC. This corrects a common assumption that the entire CLOB surface is auth-gated.

## Narrative

### Identity

- **Role**: Polymarket's **trade-execution + market-data** API layer
- **Base URL**: `https://clob.polymarket.com`
- **Auth**: public for reads, **HMAC required** for writes (POST /order, cancels, order management)
- **Wallet**: needed for writes only

### Public read endpoints

| Method | Path | Returns |
|--------|------|---------|
| GET | `/book?token_id={id}` | Live order book |
| GET | `/price?token_id={id}&side=buy` | Best available price |
| GET | `/midpoint?token_id={id}` | Midpoint price |
| GET | `/spread?token_id={id}` | Spread |
| GET | `/last-trade-price?token_id={id}` | Last trade price |
| GET | `/fee-rate?token_id={id}` | Fee rate |
| GET | `/tick-size?token_id={id}` | Tick size |
| GET | `/markets/{conditionId}` | conditionId → token_ids mapping |
| GET | `/time` | Server time (for nonce generation) |

**These require zero auth.** A wrapper that gates them behind wallet init / HMAC setup is wasting bytes and creating failure surface.

> **Auth discrepancy `[NEEDS VERIFICATION 2026-05-18]`** — the K51 @AlterEgo_eth cheat sheet groups `GET /book` and `GET /midpoint` under "Auth required". This conflicts with the earlier K43 @AlterEgo_eth post AND with Cemini's own 2026-05-18 geo-profiling test (cemini-prod, no auth header) which observed both returning HTTP 200. Empirical test takes precedence — `/book` and `/midpoint` are treated as public reads. Re-test if Polymarket announces a gating change.

### Authenticated write endpoints

- `GET /orders` — read your own open orders (auth required, vs. anonymous book reads)
- `POST /order` — place single order (HMAC signature + server-time nonce). **Geo-blocked outside permitted regions: HTTP 403, Cloudflare-enforced** (Cemini geo-test 2026-05-18).
- `POST /orders` — batch order placement (same auth + geo profile)
- `DELETE /order` — cancel order (same auth profile)

### Critical input — `token_id`

Order *placement* accepts only `token_id`, not `conditionId`. The classic resolution path is Gamma's `clobTokenIds[]` field (see `@entities/tools/polymarket-gamma-api.md`). **K51 nuance**: CLOB also exposes `GET /markets/{conditionId}`, which returns the conditionId → token_ids mapping — so token resolution is not Gamma-exclusive. Discovery can happen CLOB-side; only the order body still requires `token_id`.

### Canonical two-step flow

```python
import requests

# Step 1: Gamma → token_id
gamma = requests.get(
    f"https://gamma-api.polymarket.com/markets?conditionId={cid}"
).json()
token_id_yes = gamma["clobTokenIds"][0]

# Step 2: CLOB → public read, no auth needed
price = float(
    requests.get(
        f"https://clob.polymarket.com/price?token_id={token_id_yes}&side=buy"
    ).json()["price"]
)
```

### Production discipline

1. **Nonce from `/time`, not local clock**. Local clock drift between bot host and Polymarket servers is a documented order-rejection cause.
2. **Pre-build HMAC + headers + bodies** in the hot path — see `@concepts/polymarket-bot-architecture.md` <0.5ms internal-hot-path target.
3. **Public reads do not authenticate** — do not retry public read 401s as if they were transient; they're code bugs (something wrapping auth around a public endpoint).
4. **Full reconciliation every 30s** — silent fill bug post-V2 means API exceptions alone don't confirm fills. Poll order-status manually, full reconcile pass minimum every 30s. (See bot-architecture concept page.)
5. **`?side=buy` vs `?side=sell`** on `/price` — these are different reads. Best-available-buy price ≠ best-available-sell price; the spread between them is `/spread`'s output.

## Snippets

> "CLOB API — trade execution. Only trading endpoints require auth (POST /order, cancels, etc.)." [Source: 1)@AlterEgo_eth.docx]

> "GET /time — server time (for nonce)." [Source: 1)@AlterEgo_eth.docx]

> "You cannot place orders with conditionId. CLOB only understands token_id." [Source: 1)@AlterEgo_eth.docx]

## Dead Ends

- **Treating all CLOB endpoints as auth-required** — common but wrong. Nine read endpoints are public (incl. `/markets/{conditionId}`).
- **Using local clock for nonce** — `/time` exists specifically to avoid clock-drift order rejections.
- **Sending `conditionId` in an order body** — order *placement* accepts only `token_id`. CLOB *does* accept conditionId for the `GET /markets/{conditionId}` lookup, but never as an order parameter — resolve to `token_id` first (Gamma `clobTokenIds[]` or CLOB `/markets/{conditionId}`).
