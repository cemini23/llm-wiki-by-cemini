---
title: Polymarket API Reference (six-surface endpoint inventory)
type: concept
tags: [reference, prediction-markets, polymarket, api, endpoint-inventory, cemini-internal-reference]
keywords: [polymarket-api, gamma-api, data-api, clob-api, lb-api, websockets, bridge-api, endpoint-cheatsheet, keyset-pagination, market-positions, leaderboard-pnl, geo-block, pusd]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-data-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-lb-api.md
  - entities/tools/polymarket-websocket-api.md
  - entities/tools/polymarket-bridge-api.md
  - sources/alterego-eth-polymarket-endpoint-cheatsheet.md
  - sources/alterego-eth-polymarket-bridge-api.md
  - concepts/polymarket-bot-architecture.md
  - concepts/kalshi-api-reference.md
maturity: validated
created: 2026-05-18
updated: 2026-05-19
---

## Relations

- @entities/platforms/polymarket.md — the venue this reference documents
- @entities/tools/polymarket-gamma-api.md — Gamma (discovery) entity page; this concept page is the cross-surface index
- @entities/tools/polymarket-data-api.md — Data API (trader/market analytics) entity page
- @entities/tools/polymarket-clob-api.md — CLOB (execution + market data) entity page
- @entities/tools/polymarket-lb-api.md — LB-API (leaderboard/PnL) entity page
- @entities/tools/polymarket-websocket-api.md — WebSocket channels entity page
- @entities/tools/polymarket-bridge-api.md — Bridge API (deposits/withdrawals/pUSD) entity page
- @sources/alterego-eth-polymarket-endpoint-cheatsheet.md — origin source for surfaces 1-5 (@AlterEgo_eth X post, May 2026)
- @sources/alterego-eth-polymarket-bridge-api.md — origin source for surface 6, the Bridge API (@AlterEgo_eth X post, K54)
- @concepts/polymarket-bot-architecture.md — downstream consumer; the 6-layer websocket bot is built on these endpoints
- @concepts/kalshi-api-reference.md — sibling reference for the other prediction-market venue Cemini trades

## Raw Concept

**The question this page answers**: "which Polymarket endpoint does what, and which need auth / are geo-blocked?" — the canonical Cemini-side cross-surface index so the brain and any bot code can be audited against a single source of truth instead of guessing.

**Provenance**: synthesized from `@sources/alterego-eth-polymarket-endpoint-cheatsheet.md` (@AlterEgo_eth X post, "tested and up to date as of May 2026"), cross-checked against the earlier K43 @AlterEgo_eth post and Cemini's own 2026-05-18 geo-profiling test from cemini-prod. Where the source and the empirical test disagree, the test wins and the discrepancy is flagged.

**License posture**: Polymarket's API is publicly documented; this is internal-reference synthesis, not redistribution. Same posture as `@concepts/kalshi-api-reference.md`.

## Narrative

Polymarket exposes **six surfaces**. Five are public-facing read/funding layers; only order *writes* require auth. A separate axis is **geography**: per Cemini's 2026-05-18 profiling, all reads succeed from a US IP and only `POST /order` is geo-blocked (HTTP 403, Cloudflare-enforced).

### 1. Gamma API — `https://gamma-api.polymarket.com` (public, no auth)

Market catalog + discovery. See `@entities/tools/polymarket-gamma-api.md`.

| Endpoint | Purpose |
|----------|---------|
| `GET /markets?limit=100&offset=0` | Market catalog (classic offset pagination) |
| `GET /markets/keyset?next_cursor=&limit=100` | Market catalog, cursor pagination — faster for bulk |
| `GET /markets?ids={conditionId}` | Market details, array form |
| `GET /markets?conditionId={conditionId}` | Market details, single object — preferred |
| `GET /markets?active=true&closed=false` | Active markets only |
| `GET /markets?tag_id={id}&closed=false` | Open markets by tag |
| `GET /public-search?q={query}` | Search — `q=` only; `term=` returns HTTP 422 |
| `GET /events?slug={slug}` | Event + all its markets |
| `GET /events/slug/{slug}` | Direct event access (cleaner) |
| `GET /events?tag_id={id}` | Events by tag |
| `GET /tags` | Full tag list |

### 2. Data API — `https://data-api.polymarket.com` (public, no auth)

Per-trader and per-market analytics. See `@entities/tools/polymarket-data-api.md`.

| Endpoint | Purpose |
|----------|---------|
| `GET /v1/market-positions?market={conditionId}` | All trader positions in a market |
| `GET /positions?user={address}&limit=500` | Open positions (max 500) |
| `GET /closed-positions?user={address}&limit=50` | Closed positions + PnL history |
| `GET /activity?user={address}&limit=500` | User transactions (TRADE/REDEEM/YIELD) |
| `GET /trades?user={address}&limit=100` | Trade history by wallet |
| `GET /trades?market={conditionId}&limit=100` | Trade history by market |
| `GET /oi?market={conditionId}` | Open interest in USD |
| `GET /holders?market={conditionId}&limit=50` | Top holders |
| `GET /value?user={address}` | Portfolio value |

This surface is the substrate for whale-flow / informed-minority analysis — see `@sources/polymarket-informed-minority-gomezcram-2026.md` and `@concepts/insider-detection-entropy-collapse.md`.

### 3. CLOB API — `https://clob.polymarket.com`

Order book + execution + market data. See `@entities/tools/polymarket-clob-api.md`.

**Public reads (no auth):**

| Endpoint | Purpose |
|----------|---------|
| `GET /time` | Server time — nonce source |
| `GET /markets/{conditionId}` | conditionId → token_ids mapping |
| `GET /last-trade-price?token_id={id}` | Last trade price |
| `GET /fee-rate?token_id={id}` | Fee rate |
| `GET /tick-size?token_id={id}` | Price tick size |
| `GET /book?token_id={id}` | Order book — see auth note below |
| `GET /midpoint?token_id={id}` | Midpoint price — see auth note below |
| `GET /price?token_id={id}&side=buy` | Best available price |
| `GET /spread?token_id={id}` | Spread |

**Auth required (HMAC + server-time nonce):**

| Endpoint | Purpose |
|----------|---------|
| `GET /orders` | Your open orders |
| `POST /order` | Place single order — **geo-blocked outside permitted regions (HTTP 403)** |
| `POST /orders` | Batch orders |
| `DELETE /order` | Cancel order |

> **Auth discrepancy — RESOLVED 2026-05-18.** The @AlterEgo_eth May-2026 cheat sheet groups `GET /book` and `GET /midpoint` under "Auth required" — **incorrect** `[RETRACTED]`. Cemini direct test 2026-05-18: unauthenticated GETs against a live active-market `token_id` returned HTTP 200 from both. They are public reads, consistent with the earlier K43 @AlterEgo_eth post. Treat the cheat sheet's auth column as unreliable for those two rows.

### 4. LB-API — `https://lb-api.polymarket.com` (public, no auth)

Leaderboard / PnL. See `@entities/tools/polymarket-lb-api.md`.

| Endpoint | Purpose |
|----------|---------|
| `GET /profit?window=all&address={address}` | Full PnL history |
| `GET /profit?window=1d&address={address}` | PnL, last 24h |

### 5. WebSockets — `wss://ws-subscriptions-clob.polymarket.com/ws`

See `@entities/tools/polymarket-websocket-api.md`.

| Channel | Auth | Payload |
|---------|------|---------|
| `/market` | public | Orderbook snapshots + real-time price-change deltas |
| `/user` | authenticated | Personal fills, cancellations, order updates |

### 6. Bridge API — `https://bridge.polymarket.com` (public, no auth — provisional)

Wallet funding: converts arbitrary on-chain assets into Polymarket's collateral token (**pUSD**) and bridges pUSD back out. See `@entities/tools/polymarket-bridge-api.md`. Source: K54 @AlterEgo_eth post.

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/deposit` | POST | Create deposit addresses (EVM / Solana / Bitcoin). Cacheable, reusable. |
| `/supported-assets` | GET | Supported tokens + minimum deposit amount per chain. |
| `/quote` | POST | Expected pUSD output + fees for a deposit. |
| `/status/{address}` | GET | Deposit status by deposit address — poll until confirmed. |
| `/withdraw` | POST | Create withdrawal addresses to bridge pUSD back out. |

Deposit flow: `POST /deposit` → `GET /supported-assets` → `POST /quote` → send funds → poll `GET /status/{address}` → **CLOB `/balance-allowance/update`** (mandatory — syncs the new balance into the order layer; skipping it leaves the deposit invisible to trading). All deposited assets auto-convert to **pUSD** on Polygon — the unit every other surface is denominated in. The "no auth required" claim is `[NEEDS VERIFICATION 2026-05-19]` — single-source, and the cheat sheet's auth column has been wrong before.

### Cemini posture

- **Geo split** — all reads (Gamma, Data, CLOB reads, LB-API, `/market` WS) work from Cemini's US-based cemini-prod. Only `POST /order` is geo-blocked. The order-submission path needs a non-US egress; the read path does not. See hot.md geo-profiling findings + `@concepts/cross-venue-arbitrage-pattern.md`.
- **conditionId vs token_id** — Gamma's `clobTokenIds[0/1]` (YES/NO) is the classic bridge, but CLOB's `GET /markets/{conditionId}` also resolves the mapping. Order *placement* still requires token_id.
- **Bulk catalog** — use Gamma `/markets/keyset` (cursor) over `/markets?offset=` for full-catalog pulls.
- **Reliability caveat** — the source's auth column is demonstrably not fully reliable: it mis-classified `/book` + `/midpoint` as auth-required (disproven by direct test 2026-05-18). Treat any auth/geo claim from the cheat sheet as provisional until reproduced against the live API.

## Snippets

> "I collected every single working endpoint across Gamma, Data, CLOB, LB-API and WebSockets - no more guessing, no more 404s, no more outdated docs." [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

> "GET /public-search?q={query} - search (use only q=, term= returns 422)" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

## Dead Ends

- **`term=` on Gamma `/public-search`** — HTTP 422; the parameter is `q=` only.
- **Taking the cheat sheet's CLOB auth column at face value** — `/book` and `/midpoint` are listed auth-required but empirically return 200 unauthenticated (Cemini geo-test 2026-05-18).
