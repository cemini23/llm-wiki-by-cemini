---
title: "@AlterEgo_eth — Every Polymarket API Endpoint Cheat Sheet (X post, May 2026)"
type: source
tags: [source, x-post, polymarket, api-reference, gamma-api, data-api, clob-api, lb-api, websockets]
keywords: [alterego_eth, polymarket-api, gamma-api, data-api, clob-api, lb-api, websockets, endpoint-cheatsheet, keyset-pagination, market-positions, leaderboard-pnl]
related:
  - entities/people/alteregoeth.md
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/tools/polymarket-data-api.md
  - entities/tools/polymarket-lb-api.md
  - entities/tools/polymarket-websocket-api.md
  - concepts/polymarket-api-reference.md
  - concepts/polymarket-bot-architecture.md
  - sources/alterego-eth-polymarket-gamma-vs-clob.md
maturity: validated
read_status: deep-read
created: 2026-05-18
updated: 2026-05-18
clusters: [api-tradecraft, polymarket]
---

## Relations

- @entities/people/alteregoeth.md — author; second technical artifact from this handle ingested into the wiki
- @entities/platforms/polymarket.md — primary platform reference
- @entities/tools/polymarket-gamma-api.md — discovery layer; this post adds keyset pagination + `/tags`
- @entities/tools/polymarket-clob-api.md — execution layer; this post adds `/markets/{conditionId}`, `/orders`, batch + cancel
- @entities/tools/polymarket-data-api.md — Data API layer, first documented from this source
- @entities/tools/polymarket-lb-api.md — LB-API leaderboard/PnL layer, first documented from this source
- @entities/tools/polymarket-websocket-api.md — WebSocket layer, first documented from this source
- @concepts/polymarket-api-reference.md — the canonical Cemini-side reference page this source feeds
- @concepts/polymarket-bot-architecture.md — bot playbook (@0x_Punisher); this cheat sheet is the API surface that bot consumes
- @sources/alterego-eth-polymarket-gamma-vs-clob.md — earlier @AlterEgo_eth post (K43); this cheat sheet supersedes its endpoint enumeration with a fuller surface

## Raw Concept

- **Author**: @AlterEgo_eth (X handle)
- **Format**: X post — "Every Polymarket API Endpoint Your Bot Will Ever Need (One Cheat Sheet)"
- **Date**: post dated May 2026; drop date 2026-05-18
- **Drop location**: `research to be indexed/@AlterEgo_eth.docx` → librarian as `alterego-eth-polymarket-endpoint-cheatsheet.docx`
- **sha256**: `a3ef77c3e4a4766e...`
- **Size**: 564,628 bytes
- **Preingest verdict**: NEW (distinct sha from the K43 `1)@AlterEgo_eth.docx`)

**What prompted this page**: a second @AlterEgo_eth artifact, this time a full five-surface endpoint inventory ("tested and up to date as of May 2026"). The K43 post covered the Gamma/CLOB split conceptually; this one enumerates the complete API surface — including two layers Cemini had not catalogued (Data API, LB-API) and the WebSocket channels. Ingested as the substrate for the canonical `polymarket-api-reference.md` concept page.

## Narrative

The post claims to collect "every single working endpoint across Gamma, Data, CLOB, LB-API and WebSockets." Five surfaces:

### 1. Gamma API — `http://gamma-api.polymarket.com` (public, no auth)

Market catalog + discovery. New vs the K43 enumeration: **keyset pagination** (`/markets/keyset?next_cursor=`), `closed=false` filters, `/events/slug/{slug}`, `/events?tag_id=`, and `GET /tags` (full tag list). `/public-search` takes `q=` only — `term=` returns HTTP 422.

### 2. Data API — `http://data-api.polymarket.com` (public, no auth) — NEW to Cemini

Per-trader and per-market analytics. Positions, closed-positions (with PnL), activity (TRADE/REDEEM/YIELD), trades by wallet or market, open interest, top holders, portfolio value. This is the layer that answers "who is in this market and what are they doing" — directly relevant to the informed-minority signal (`@concepts/insider-detection-entropy-collapse.md`, `@sources/polymarket-informed-minority-gomezcram-2026.md`).

### 3. CLOB API — `http://clob.polymarket.com`

Order book + execution. New vs K43: `GET /markets/{conditionId}` (CLOB-side conditionId→token_id mapping — so token resolution is not Gamma-exclusive), `GET /orders` (your open orders), `POST /orders` (batch), `DELETE /order` (cancel).

**Contradiction flagged** — the post groups `GET /book` and `GET /midpoint` under "Auth required". This conflicts with (a) the K43 @AlterEgo_eth post, which lists both as public reads, and (b) Cemini's own geo-profiling test on 2026-05-18 (~12:30pm EDT from cemini-prod), which observed `/book` and `/midpoint` returning HTTP 200 with no auth header. Empirical test wins for now: treat `/book` + `/midpoint` as public reads. `[NEEDS VERIFICATION 2026-05-18]` — re-test whether Polymarket has begun (or announced) gating these.

### 4. LB-API — `http://lb-api.polymarket.com` (public, no auth) — NEW to Cemini

Leaderboard / PnL history. `GET /profit?window={all|1d}&address={address}`.

### 5. WebSockets — `wss://ws-subscriptions-clob.polymarket.com/ws`

`/market` — public stream: orderbook snapshots + real-time price-change deltas. `/user` — authenticated stream: personal fills, cancellations, order updates. This is the realtime substrate the `@concepts/polymarket-bot-architecture.md` 6-layer websocket bot assumes.

### Cemini relevance

1. **Data API closes a real gap** — Cemini had Gamma (discovery) + CLOB (execution) catalogued but nothing for per-trader position/PnL analytics. `/v1/market-positions`, `/holders`, `/oi` are direct inputs to the informed-minority / whale-flow analyst surface.
2. **`/markets/{conditionId}` on CLOB** nuances the K43 "CLOB only understands token_id" rule — CLOB *does* expose a conditionId→token_id lookup. Order *placement* still requires token_id, but discovery has a CLOB-side path.
3. **Geo note** — all five surfaces are read-public; per the 2026-05-18 geo-profiling, all reads work from a US IP and only `POST /order` is geo-blocked (HTTP 403). See `@concepts/polymarket-api-reference.md` and hot.md geo-profiling findings.

## Snippets

> "I collected every single working endpoint across Gamma, Data, CLOB, LB-API and WebSockets - no more guessing, no more 404s, no more outdated docs. Everything is tested and up to date as of May 2026." [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

> "GET /public-search?q={query} - search (use only q=, term= returns 422)" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

> "GET /markets/keyset?next_cursor=&limit=100 - market catalog with cursor (faster for bulk)" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

> "GET /v1/market-positions?market={conditionId} - all trader positions" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

> "wss://ws-subscriptions-clob.polymarket.com/ws — /market public stream, orderbook snapshots + real-time price change deltas; /user authenticated stream, your personal fills, cancellations and order updates" [Source: alterego-eth-polymarket-endpoint-cheatsheet.docx]

## Dead Ends

- **`term=` on `/public-search`** — returns HTTP 422. The search parameter is `q=` only.
- **Trusting the post's CLOB auth grouping verbatim** — `/book` and `/midpoint` are listed as auth-required but empirically return 200 unauthenticated (Cemini geo-test 2026-05-18). The cheat sheet's auth column is not reliable for those two rows.
