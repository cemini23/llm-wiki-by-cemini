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
  - concepts/polymarket-bot-architecture.md
maturity: validated
created: 2026-05-13
updated: 2026-05-14
---

## Relations

- @entities/platforms/polymarket.md — execution venue
- @entities/tools/polymarket-gamma-api.md — paired discovery-layer API (Gamma → token_id → CLOB)
- @entities/tools/polymarket-python-order-utils.md — official client; canonical signer for POST /order
- @entities/tools/aulekator-polymarket-btc-bot.md — K44 NautilusTrader-based bot; Polymarket adapter path TBD (Phase-0 G3)
- @entities/tools/awesome-polymarket-tools-harish-garg.md — K44 CC0 directory referencing CLOB tooling
- @sources/alterego-eth-polymarket-gamma-vs-clob.md — primary source for the public-vs-auth endpoint split
- @concepts/polymarket-bot-architecture.md — bot playbook; 6-layer websocket system applies on top of CLOB reads

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
| GET | `/time` | Server time (for nonce generation) |

**All eight require zero auth.** A wrapper that gates these behind wallet init / HMAC setup is wasting bytes and creating failure surface.

### Authenticated write endpoints

- `POST /order` — place order (requires HMAC signature, server-time nonce)
- Order cancel / modify endpoints — same auth profile
- Order-status polling endpoints — auth required to read your own orders (vs. anonymous book reads)

### Critical input — `token_id`

CLOB does not understand `conditionId`. The only identifier CLOB accepts is `token_id`, which comes from Gamma's `clobTokenIds[]` field. See `@entities/tools/polymarket-gamma-api.md`.

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

- **Treating all CLOB endpoints as auth-required** — common but wrong. Eight read endpoints are public.
- **Using local clock for nonce** — `/time` exists specifically to avoid clock-drift order rejections.
- **Querying CLOB with conditionId** — CLOB has no notion of conditionId. Always resolve via Gamma first.
