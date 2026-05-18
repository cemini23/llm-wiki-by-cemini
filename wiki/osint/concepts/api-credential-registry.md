---
title: API Credential Registry — Cemini Key Inventory
type: concept
tags: [concept, infrastructure, api, credentials, registry, operations]
keywords: [api keys, credential inventory, free tier, rate limits, key rotation, signup urls, secrets management, dotenv]
related:
  - entities/tools/public-apis-list.md
maturity: draft
created: 2026-05-18
updated: 2026-05-18
---

## Relations

- @entities/tools/public-apis-list.md — the *discovery* directory (find a NEW candidate API); this page is the *inventory* (APIs Cemini has committed to / holds keys for)

## Raw Concept

Prompted by an operator request to "track API keys in the wiki so the bot can find a key it needs." This page answers that need **safely**: it is a credential *inventory*, not a credential *store*.

**Hard rule — no key values in the wiki, ever.** This page records, for each API: what it's for, the free-tier limits, the official signup/console URL, whether Cemini holds a key, and *where the secret physically lives* (the `.env` file + variable name). It never records the secret string itself.

Why: the wiki is a git repo, synced to `cemini-librarian` and (via briefs) to `cemini-prod`. A key pasted here is a key leaked to every machine in that path and every clone of the repo. The repo's `detect-secrets` pre-commit hook will reject a commit containing a key — that rejection is the system working as designed, not an obstacle to route around.

**Out of scope — deliberately.** This registry does *not* catalog third-party "free key" / leaked-credential dumps. Keys harvested from such repos belong to other accounts; using them is unauthorized access and theft of service, and many are honeypots or already burned. Cemini uses keys it has legitimately registered for, tracked below. If a needed key is missing, the fix is the **Signup URL** column, not a leak repo.

## Narrative

### How the bot uses this page

1. Bot needs to call service X → searches the wiki → lands here.
2. Reads the row for X: is a key held (`Key?` column)? If yes, which `.env` variable holds it (`Stored at`)? What are the limits?
3. At runtime the bot reads the *actual* secret from that `.env` variable — **not from the wiki**.
4. If `Key? = ❌`, the row's **Signup URL** tells the operator where to register one. Obtaining the key is a human action; the bot surfaces the gap, it does not self-provision.

So the chain the operator described — "search wiki → find source → get the key" — terminates at *the location of a key we own* (`.env` variable name), never at someone else's leaked credential.

### Where keys physically live

Cemini keeps API credentials in `.env` files. The wiki references them by **variable name only**:

| Environment | `.env` location | `Stored at` convention |
|---|---|---|
| `cemini-prod` (trading stack) | `/opt/cemini/.env` | `prod .env: SERVICE_API_KEY` |
| Laptop workspace | `~/Desktop/OSINT WORKSPACE/.env` (gitignored) | `laptop .env: SERVICE_API_KEY` |
| MCP servers (Exa, Brave…) | MCP client config, not `.env` | `MCP config: <server>` |

Both `.env` files are gitignored and untracked — verified 2026-05-18. They must stay that way; if either ever appears in `git status` as tracked, rotate every key in it.

### Rotation discipline

- Record a `Rotated` date when a key is issued or rotated (use the log or a per-row note).
- Rotate immediately on any suspected exposure (accidental commit, shared log, machine compromise).
- Free-tier keys are low-stakes but still rotate-on-exposure: a burned key on a shared free tier can get the *whole tier* rate-limited or banned.
- `wiki_gap_detect.py` does not yet scan this page for stale rotations — treat rotation as a manual audit aid for now.

### Free-tier limits — point-in-time

Every limit and signup URL below is `[NEEDS VERIFICATION 2026-05-18]` as a class: providers change free-tier quotas and console URLs without notice. Verify against the provider's current pricing page before depending on a limit for capacity planning. The structure is stable; the numbers drift.

---

## Registry

Populated 2026-05-18 from `.env` variable names on `cemini-prod:/opt/cemini/.env` (28 keys) and the laptop workspace `.env` (2 LLM keys). Legend — `Key?`: ✅ held · ❌ not held · ❓ unknown / lives outside `.env`. `Stored at` records the `.env` variable name, never the value.

### Market data & trading venues

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| Polygon.io | US stocks/options/crypto/forex data | 5 req/min, EOD, 2yr history | https://polygon.io/dashboard/signup | ✅ | `prod .env: POLYGON_API_KEY` |
| Finnhub | Stocks/forex/crypto, fundamentals, news | 60 req/min | https://finnhub.io/register | ✅ | `prod .env: FINNHUB_API_KEY` |
| Alpaca | Brokerage + market data; paper trading | Paper trading free; data tiers vary | https://alpaca.markets/ | ✅ | `prod .env: ALPACA_API_KEY` / `ALPACA_API_SECRET` / `ALPACA_SECRET_KEY` |
| Kalshi | Prediction-market trading API | Account-based | https://kalshi.com/account | ✅ | `prod .env: KALSHI_API_KEY` (+ `KALSHI_EMAIL` / `KALSHI_PASSWORD` / `KALSHI_SENDER_ID` / `KALSHI_TARGET_ID`) |
| OANDA | Forex data + execution | Practice account free API token | https://www.oanda.com/ | ✅ | `prod .env: OANDA_API_KEY` (+ `OANDA_ACCOUNT_ID`) |
| Coinbase | Crypto exchange — data + execution | Free, account-based | https://www.coinbase.com/developer-platform | ✅ | `prod .env: COINBASE_API_KEY` / `COINBASE_API_SECRET` |
| Robinhood | Equities/crypto broker (unofficial API) | No official API/free tier — login-based | https://robinhood.com/ | ✅ | `prod .env: RH_USERNAME` / `RH_PASSWORD` |
| Polymarket | CLOB API (prediction markets) | Public reads free; orders need wallet-derived API creds | https://docs.polymarket.com/ | ❓ | wallet-derived — see @concepts/polymarket-api-reference.md (`.env` holds RPC/CLOB URLs, not a key) |
| Hyperliquid | Perp DEX | Wallet-signed; no central key | https://hyperliquid.xyz/ | ❓ | wallet-derived (`prod .env: HYPERLIQUID_PROXY` is routing config) |
| Interactive Brokers | Brokerage (TWS/Gateway) | No API key — authenticated session | https://www.interactivebrokers.com/ | n/a | session-based — n/a |

> CCXT is a *library*, not an API — each exchange wired through it carries its own key pair (Coinbase above is one). Add a row per live exchange.

### Crypto / economic / fundamental data

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| FRED (St. Louis Fed) | Macro / economic time series | Free, key required, ~120 req/min | https://fred.stlouisfed.org/docs/api/api_key.html | ✅ | `prod .env: FRED_API_KEY` |
| Google BigQuery | Data warehouse (market dataset) | Free tier ~1TB queries/month | https://console.cloud.google.com/ | ✅ | `prod .env: GOOGLE_APPLICATION_CREDENTIALS` (service-account JSON path) |
| SEC EDGAR | Filings / financial statements | Free, **no key** — descriptive `User-Agent` header required | https://www.sec.gov/os/accessing-edgar-data | n/a | no key needed |
| Federal Register API | US regulatory notices | Free, **no key** | https://www.federalregister.gov/developers/api/v1 | n/a | no key needed |
| CoinGecko | Crypto prices, market cap, metadata | Demo plan ~30 calls/min, demo key | https://www.coingecko.com/en/developers/dashboard | ❌ | not in `.env` — register if needed |
| NASDAQ Data Link | Curated financial/economic datasets | Free key; anonymous heavily limited | https://data.nasdaq.com/ | ❌ | not in `.env` — register if needed |
| OpenFIGI | Security identifier mapping | No key: 25 req/min · with key: higher | https://www.openfigi.com/api | ❌ | not in `.env` — register if needed |

### News, events & OSINT

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| GNews | News headlines + articles API | ~100 req/day | https://gnews.io/ | ✅ | `prod .env: GNEWS_KEY` |
| NewsAPI | News aggregation API | ~100 req/day (developer plan) | https://newsapi.org/register | ✅ | `prod .env: NEWSAPI_KEY` |
| GDELT | Global news / events feed | Free, **no key** | https://www.gdeltproject.org/ | n/a | no key needed |
| Brave Search API | Web/news search (wired as MCP) | Free tier ~2,000 queries/month | https://brave.com/search/api/ | ❓ | MCP config: brave-search (not in `.env`) |
| Marketaux | Financial news + sentiment | ~100 req/day | https://www.marketaux.com/ | ❌ | not in `.env` — GNews/NewsAPI cover this need |
| OpenSanctions | Sanctions / PEP screening | Free for non-commercial, key required | https://www.opensanctions.org/api/ | ❌ | not in `.env` — register if needed |

### Social

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| X / Twitter API | Social posts, sentiment harvesting | Free tier highly restricted (read very limited) | https://developer.x.com/ | ✅ | `prod .env: X_API_KEY` / `X_API_SECRET` / `X_BEARER_TOKEN` |
| Telegram Bot API | Bot messaging / alerts | Free `bot token` | https://core.telegram.org/bots | ✅ | `prod .env: TELEGRAM_BOT_TOKEN` |
| Telegram (Telethon) | Channel/group *reading* (user API) | Free `api_id` + `api_hash` (distinct from bot token) | https://my.telegram.org/apps | ❌ | not in `.env` — only the bot token is held |

### Weather (weather-trading bot)

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| OpenWeather | Global weather | Free ~60 calls/min, 1M/month | https://openweathermap.org/api | ✅ | `prod .env: OPENWEATHER_API_KEY` |
| NWS / weather.gov | US forecasts + observations | Free, **no key** — `User-Agent` required | https://www.weather.gov/documentation/services-web-api | n/a | no key needed |
| Open-Meteo | Global forecast / historical weather | Free, **no key** for non-commercial | https://open-meteo.com/ | n/a | no key needed |
| WeatherAPI.com | Global weather + forecast | Free ~1M calls/month | https://www.weatherapi.com/ | ❌ | not in `.env` — register if needed |
| Visual Crossing | Weather + historical | Free ~1,000 records/day | https://www.visualcrossing.com/weather-api | ❌ | not in `.env` — register if needed |
| Windy | Point forecast / model data | Limited free key | https://api.windy.com/ | ❌ | not in `.env` — register if needed |

### LLM / AI services

| Service | Purpose | Free tier (verify) | Signup / console URL | Key? | Stored at |
|---|---|---|---|---|---|
| DeepSeek API | LLM inference | Paid (no free tier) | https://platform.deepseek.com/ | ✅ | `prod .env: DEEPSEEK_API_KEY` · also `laptop .env: DEEPSEEK_API_KEY` |
| OpenRouter | Multi-model LLM gateway | Pay-per-use; some free models | https://openrouter.ai/keys | ✅ | `prod .env: OPENROUTER_API_KEY` |
| Google Gemini | LLM inference | Free tier via AI Studio (rate-limited) | https://aistudio.google.com/apikey | ✅ | `laptop .env: GEMINI_API_KEY` |
| Grok (xAI) | LLM inference | Paid, usage-billed | https://console.x.ai/ | ✅ | `laptop .env: GROK_API_KEY` |
| Exa | Neural web search (research MCP) | Paid, usage-billed | https://dashboard.exa.ai/ | ❓ | MCP config: exa (not in `.env`) |
| Anthropic | Claude API | Paid, usage-billed | https://console.anthropic.com/ | ✅ | Claude Code config (`~/.claude/`) — not in `.env` |

### Dev / infrastructure tokens (not data APIs — listed for completeness)

| Token | Purpose | `.env` variable |
|---|---|---|
| GitHub PAT | Repo access, code-context tooling | `prod .env: GITHUB_PERSONAL_ACCESS_TOKEN` |
| Cloudflare Tunnel | Network tunnel for the prod stack | `prod .env: CLOUDFLARE_TUNNEL_TOKEN` |
| Librarian API key | Internal Cemini kb-server auth | `prod .env` + `laptop .env: LIBRARIAN_API_KEY` |

---

## Maintenance

- When a new API is adopted, add a row here and flip `Key?` to ✅ once the variable is added to the relevant `.env`.
- When a key is rotated, add a `Rotated` note (row or log).
- To re-sync this page with reality, re-run a names-only extract (never values): `ssh cemini-prod "grep -hoE '^[A-Za-z_]+=' /opt/cemini/.env | tr -d '='"`.
- To find a *new* candidate API, go through @entities/tools/public-apis-list.md (the discovery directory), evaluate, then add a committed row here.
- Append registry changes to `wiki/log.md`.

## Snippets

- **Operator request that prompted this page** (2026-05-18): "track api keys in one of my wikis ... that way if it finds an api key in the wiki it needs it can use it." — Implemented as an inventory (service/limits/`.env` variable), not a value store; the leaked-key-repo portion of the request was declined as unauthorized-access infrastructure. [Source: operator session 2026-05-18]
- **Storage location** (2026-05-18): "the keys live in the .env" — confirmed `cemini-prod:/opt/cemini/.env` (28 keys) + laptop workspace `.env` (DeepSeek/Gemini/Grok/Librarian); both gitignored and untracked. [Source: operator session 2026-05-18]

## Dead Ends

- **Storing key values in the wiki — rejected.** The wiki is git-tracked and synced across three machines; a pasted key is a key leaked everywhere, and the `detect-secrets` pre-commit hook blocks it anyway. The inventory pattern (this page) gives the bot everything it needs — *which* keys exist and *which `.env` variable* holds them — without the secret leaving its `.env`.
- **Cataloging third-party "thousands of free keys" leak repos — rejected.** Those are credential dumps belonging to other accounts; using them is unauthorized access / theft of service, exposes Cemini IPs to honeypot keys, and fights the repo's own secret-scanning. The legitimate path for a missing key is the **Signup URL** column.
