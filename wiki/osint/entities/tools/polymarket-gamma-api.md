---
title: "Polymarket Gamma API"
type: entity
tags: [tool, polymarket, api, gamma, discovery, public-endpoints]
keywords: [gamma-api, polymarket-discovery, conditionId, clobTokenIds, public-search, events-by-slug, no-auth, market-metadata]
related:
  - entities/platforms/polymarket.md
  - entities/tools/polymarket-clob-api.md
  - sources/alterego-eth-polymarket-gamma-vs-clob.md
  - concepts/polymarket-bot-architecture.md
maturity: validated
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- @entities/platforms/polymarket.md — the platform Gamma exposes
- @entities/tools/polymarket-clob-api.md — paired execution-layer API
- @sources/alterego-eth-polymarket-gamma-vs-clob.md — primary source enumerating endpoints
- @concepts/polymarket-bot-architecture.md — bot playbook that assumes correct Gamma/CLOB split

## Raw Concept

What prompted this page: the @AlterEgo_eth ingest (2026-05-13) formalized the Gamma vs CLOB distinction. Half of broken Polymarket bots fail at this boundary — devs query Gamma where CLOB is required, or vice versa. This entity page is the durable reference for "which endpoint does what on Gamma."

## Narrative

### Identity

- **Role**: Polymarket's **market-discovery** API layer
- **Base URL**: `https://gamma-api.polymarket.com`
- **Auth**: **None required** — fully public
- **Wallet**: not needed
- **Used for**: finding markets, reading metadata, getting `clobTokenIds[]` (the bridge to CLOB execution)

### Endpoints

| Method | Path | Purpose | Returns |
|--------|------|---------|---------|
| GET | `/markets?conditionId={id}` | Single market by conditionId | object (recommended) |
| GET | `/markets?ids={id}` | Same data, array form | array |
| GET | `/events?slug={slug}` | Event + nested markets | event object |
| GET | `/events/slug/{slug}` | Direct event access | event object (cleaner) |
| GET | `/markets?tag_id={id}&active=true` | Active markets by category | array |
| GET | `/public-search?q={query}` | Market search | array; use `q=` only |

### Critical response field — `clobTokenIds[]`

Every market response includes a `clobTokenIds` array of exactly two entries:

- `clobTokenIds[0]` = YES token
- `clobTokenIds[1]` = NO token

These are the bridge into the CLOB API. Any order execution requires the token_id, not the conditionId — see `@entities/tools/polymarket-clob-api.md`.

**Idiomatic helper** (Python, paraphrased from source):

```python
def get_token_ids(condition_id: str) -> tuple[str, str]:
    r = requests.get(
        f"https://gamma-api.polymarket.com/markets?conditionId={condition_id}"
    )
    data = r.json()
    return data["clobTokenIds"][0], data["clobTokenIds"][1]  # YES, NO
```

Wrap the indexing — `[0]` / `[1]` for YES / NO is exactly the off-by-one mistake that ships incorrectly.

### When to use Gamma vs CLOB

- **Use Gamma** when: finding markets, reading metadata, getting token IDs, browsing categories, searching by keyword
- **Use CLOB** when: reading order book, placing/cancelling orders, fetching prices for already-known token IDs

Gamma is the entry point; CLOB is what you reach after Gamma gives you a token_id.

### Production discipline

1. **Cache `clobTokenIds`** when first resolving a conditionId — avoid round-trips to Gamma on every order
2. **Don't poll Gamma for prices** in a hot loop — `GET /price?token_id=...` on CLOB is the canonical price read
3. **`/public-search` parameter is `q=` only** — other query parameters are silently ignored
4. **`/events/slug/{slug}`** is the cleanest event-by-slug variant; prefer over `/events?slug={slug}` for code readability

## Snippets

> "Gamma API — market discovery. Public. No auth required. No wallet needed. This is where you find markets, read prices, get metadata." [Source: 1)@AlterEgo_eth.docx]

> "Most important field in the response: clobTokenIds[] — array of two token IDs. clobTokenIds[0] = YES token. clobTokenIds[1] = NO token. These are your bridge to trading." [Source: 1)@AlterEgo_eth.docx]

## Dead Ends

- **Querying CLOB endpoints with conditionId** — CLOB does not understand conditionId. All CLOB endpoints require token_id; the only path is Gamma → `clobTokenIds[k]` → CLOB.
- **Trusting `/markets?ids=` array shape when expecting a single object** — use the `conditionId={id}` variant to get an object form directly; the `ids=` variant always returns an array even for single-item queries.
