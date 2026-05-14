---
title: "@AlterEgo_eth — Polymarket Gamma vs CLOB API tradecraft (X thread, May 2026)"
type: source
tags: [source, x-thread, polymarket, gamma-api, clob-api, api-tradecraft, bot-architecture]
keywords: [alterego_eth, polymarket-api, gamma-api, clob-api, conditionId, clobTokenIds, two-step-flow, market-discovery, order-execution, public-endpoints]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - concepts/polymarket-bot-architecture.md
maturity: validated
read_status: deep-read
created: 2026-05-13
updated: 2026-05-13
clusters: [api-tradecraft, polymarket]
---

## Relations

- @entities/platforms/polymarket.md — primary platform reference
- @entities/tools/polymarket-gamma-api.md — derived entity page enumerating Gamma endpoints
- @entities/tools/polymarket-clob-api.md — derived entity page enumerating CLOB endpoints
- @concepts/polymarket-bot-architecture.md — complementary bot-architecture playbook from @0x_Punisher; this AlterEgo source covers the API-surface side that Punisher's playbook assumes as prerequisite

## Raw Concept

- **Author**: @AlterEgo_eth (X handle)
- **Format**: X thread (~64 substantive lines)
- **Date**: May 2026 (drop date 2026-05-13)
- **Drop location**: `research to be indexed/1)@AlterEgo_eth.docx` → librarian
- **sha256**: `a8312520c375e809...`
- **Size**: 725,656 bytes
- **Preingest verdict**: NEW

**What prompted this page**: a meaningful fraction of broken Polymarket bots fail because the operator confuses Gamma API (discovery, public) with CLOB API (execution). This source distills the two-layer architecture into a step-by-step reference so Cemini's polymarket_client wrapper can be audited against it.

## Narrative

### The two-layer model

**Gamma API** = market discovery layer. Public. No auth required. No wallet needed. Used to find markets, read prices, get metadata.

**CLOB API** = trade execution layer. Read endpoints (book, price, midpoint, spread, fee-rate, tick-size, time) are public; only trading endpoints (POST /order, cancels) require auth.

The bridge between the two: every Gamma market response contains `clobTokenIds[]` — an array of two token IDs.

- `clobTokenIds[0]` = YES token
- `clobTokenIds[1]` = NO token

These token IDs are the only thing CLOB understands. **You cannot place an order with a `conditionId`** — CLOB only understands `token_id`.

### Gamma endpoints (discovery)

Base: `https://gamma-api.polymarket.com`

| Endpoint | Purpose |
|----------|---------|
| `GET /markets?conditionId={conditionId}` | Single market details — returns object (recommended) |
| `GET /markets?ids={conditionId}` | Same data, returns array |
| `GET /events?slug={slug}` | Event by slug + all markets inside |
| `GET /events/slug/{slug}` | Direct event access (cleaner) |
| `GET /markets?tag_id={id}&active=true` | Active markets by category |
| `GET /public-search?q={query}` | Market search (use `q=` only) |

Most-important response field: `clobTokenIds[]` — see above.

### CLOB endpoints (execution + public reads)

Base: `https://clob.polymarket.com`

| Endpoint | Purpose | Auth? |
|----------|---------|-------|
| `GET /book?token_id={id}` | Live order book | public |
| `GET /price?token_id={id}&side=buy` | Best available price | public |
| `GET /midpoint?token_id={id}` | Midpoint price | public |
| `GET /spread?token_id={id}` | Spread | public |
| `GET /last-trade-price?token_id={id}` | Last trade price | public |
| `GET /fee-rate?token_id={id}` | Fee rate | public |
| `GET /tick-size?token_id={id}` | Tick size | public |
| `GET /time` | Server time (for nonce) | public |
| `POST /order` | Place order | **auth required** |
| Cancel/manage | Order lifecycle | **auth required** |

### Correct two-step flow (canonical example)

```python
import requests

# Step 1: Gamma — get metadata + token IDs
r = requests.get(
    f"https://gamma-api.polymarket.com/markets?conditionId={market_condition_id}"
)
data = r.json()
token_id_yes = data["clobTokenIds"][0]
token_id_no  = data["clobTokenIds"][1]

# Step 2: CLOB — read endpoints work without auth
price_resp = requests.get(
    f"https://clob.polymarket.com/price?token_id={token_id_yes}&side=buy"
)
price = float(price_resp.json()["price"])
```

### Bot-architecture corollary

> "Gamma for discovery → CLOB for execution (and now all market data reads are public)"

> "If your bot is broken = 90% of the time you're either hitting the wrong endpoint on Gamma or using outdated assumptions about CLOB auth"

### Cemini relevance

1. **Audit `/opt/cemini/conductor/tools.py` polymarket_client** against this two-layer pattern. Specifically: does the wrapper carry a `conditionId` field anywhere into a CLOB call? If yes → bug (the K30 polymarket-stack adoption brief should already have closed this hole, but worth verifying).
2. **Public CLOB reads** (book/price/midpoint/spread/fee-rate/tick-size/time) require **no auth**. Any internal code path that gates these behind wallet/HMAC initialization is wasted complexity and unnecessary failure surface.
3. **`clobTokenIds[0] = YES`, `[1] = NO`** — the index convention. Wrap this in a helper rather than indexing raw arrays (off-by-one in a YES/NO context is a critical bug).
4. **`/time` endpoint** is canonical nonce source for signed-request flows — use server time, not local clock.

## Snippets

> "Half the broken Polymarket bots I've seen fail because the dev used the wrong API for the wrong job. Gamma API and CLOB API are two completely different layers." [Source: 1)@AlterEgo_eth.docx]

> "clobTokenIds[] - array of two token IDs. clobTokenIds[0] = YES token. clobTokenIds[1] = NO token. These are your bridge to trading." [Source: 1)@AlterEgo_eth.docx]

> "You cannot place orders with conditionId. CLOB only understands token_id." [Source: 1)@AlterEgo_eth.docx]

> "Right bot architecture: Gamma for discovery → CLOB for execution (and now all market data reads are public)." [Source: 1)@AlterEgo_eth.docx]

## Dead Ends

- **Passing `conditionId` to CLOB endpoints** — explicitly flagged as common failure mode. CLOB has no concept of conditionId; it's purely a Gamma-layer construct that maps to two token IDs.
- **Authenticating CLOB read endpoints** — read endpoints (book/price/midpoint/spread/fee-rate/tick-size/time) are public. Adding auth wastes setup time and creates failure modes that don't exist in the canonical flow.
- **Using local clock for nonce** — `/time` endpoint exists explicitly for nonce generation. Local-clock drift between bot host and Polymarket servers is a documented order-rejection cause.
