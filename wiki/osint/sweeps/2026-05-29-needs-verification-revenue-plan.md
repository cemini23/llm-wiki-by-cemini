---
title: NEEDS VERIFICATION sweep — revenue-priority plan (2026-05-29)
type: brief
tags: [sweep, verification, polymarket, revenue]
updated: 2026-05-29
---

## Scope

- **Backlog:** 225 stale tags → **212** after Wave 1 → **~202** after Wave 2 → **~195** after Wave 3 → **198** after Wave 4 → **195** after Wave 5 → **~188** after Wave 6 → **~178** after Wave 7 → **~170** after Wave 8 (2026-05-29)
- **Priority rule:** revenue path first (Polymarket execution, weather alpha, cross-venue, promotion gates)
- **Verification rule:** no blind closure — every tag gets live API probe, Exa/web search, or GitHub/license check; outcome → `[CONFIRMED]` / `[TENTATIVE]` / `[RETRACTED]` / honest internal note
- **Fresh tags (7–14d):** included when revenue-relevant (K79 SMB, K77 quant, Kalshi UI bot)

## Revenue tiers

| Tier | Cluster | Tags (approx) | Revenue lever |
|------|---------|---------------|---------------|
| **R1** | pm-execution (API, bridge, CLOB, copy bots, LP) | 19 | Direct trading + treasury automation |
| **R2** | pm-weather-alpha | 6 | Directional weather edge |
| **R3** | kalshi-cross-venue | 4 | Second venue + arb |
| **R4** | perps-carry (HL funding) | — | Carry sleeve |
| **R5** | quant-promotion (Brier, MCPT, shadow→live) | 2+ | Model promotion discipline |
| **R6** | infra-blocking (deepseek, data APIs) | 9 | Unblocks dev velocity |
| **Defer** | tool-eval entities, gemini-dr wave5, harness meta | ~180 | Low/no near-term PnL |

## Wave log

### Wave 1 — DONE 2026-05-29 (13 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| Bridge API public/no-auth | `curl` live API | `[CONFIRMED]` |
| Bridge deposit flow shape | AlterEgo + curl 400-not-401 | `[CONFIRMED]` |
| Open-Meteo `bias_correction=true` | Exa + openapi.yml | `[RETRACTED]` — wrong API/param |
| Kreo = KreoPolyBot naming | Exa (docs.kreo.app, kreopoly.app) | `[CONFIRMED]` |
| Kreo "unique" stop-loss | Exa competitor docs | `[RETRACTED]` uniqueness |
| Pretracer 100ms / zero fees | Exa/web (no official docs) | `[TENTATIVE]` |
| Kreo fastest/lowest fees | Exa (PolyCop 0.5%, ~2s) | `[TENTATIVE]` |

**Pages touched:** `polymarket-bridge-api`, `polymarket-api-reference`, `alterego-eth-polymarket-bridge-api`, `open-meteo`, `polymarket-weather-trading-strategy`, `pretracer`, `kreopolybot`, `polymarket-copy-trading-strategy`, `posts-prediction-markets-*`, `theparuchh`

### Wave 2 — DONE 2026-05-29 (10 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| Data API paths public/no-auth | curl + docs.polymarket.com OpenAPI | `[CONFIRMED]` |
| polymarketanalytics public API | Web fetch + Falcon API site | Web UI free; API = paid Falcon `[CONFIRMED]` |
| polymarketanalytics funding model | Site product links (PolyGun, Falcon) | `[TENTATIVE]` freemium/referral |
| pykalshi auth format | GitHub `_base.py` read | `[CONFIRMED]` RSA-PSS |
| pykalshi endpoint coverage | Repo grep RFQ/MVE tests | `[TENTATIVE]` partial |
| pykalshi rate-limit headers | `rate_limiter.py` + `_base.py` | `[TENTATIVE]` code present; soak test pending |
| Kalshi UI bot ToS | Kalshi Data Terms PDF | `[CONFIRMED]` scrape/automation banned; API OK |
| py-clob-client-v2 official | Polymarket docs + archived V1 repo | `[CONFIRMED]` — **prod pin action** |

**Pages touched:** `polymarket-data-api`, `polymarketanalytics-com`, `pykalshi`, `kalshi-ui-automation-bot-pattern`, `polymarket-retail-trading-discipline`

**Backlog after Wave 2:** ~202 stale tags (225 − 13 Wave1 − 10 Wave2)

### Wave 3 — DONE 2026-05-29 (R2 weather + R1 remainder, ~8 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| KATL station resolution (theparuchh) | Polymarket rules + WU KATL + Open-Meteo airport coords + NWS METAR | `[CONFIRMED]` |
| x2 bias_correction magnitude | Align with Wave 1 RETRACTED | `[RETRACTED]` |
| `github.com/weather_scanner` repo | GitHub search + Phase-0 on `vgjtsy/weather_scanner` | `[TENTATIVE]` — best public match; URL ambiguous; no `detect_changes()` in code |
| GraphCast supersedes regional NWP | DeepMind blog + NOAA GraphCastGFS docs | `[TENTATIVE]` — operational but experimental; not station-level substitute |
| Type-2 arb regulatory risk | Kalshi Data Terms (Wave 2) + generic ops risks | `[TENTATIVE]` |
| py-clob-client-v2 (K57 source dup) | Cross-ref Wave 2 | `[CONFIRMED]` |
| Insider-tracker DBSCAN latency | GitHub `sniper.py` code read | `[TENTATIVE]` — batch/offline path, not websocket-inline |

**Pages touched:** `x2-docx-polymarket-theparuchh`, `polymarket-weather-trading-strategy`, `nwp-model-stack-polymarket-weather`, `polymarket-weather-bot-methodology-taxonomy`, `trading-posts-llm-gustafsson-retail-weather-copy`, `polydao-mr-buzzoni`, `graphcast`, `polymarket-insider-tracker`, `wiki/index.md`

### Wave 4 — DONE 2026-05-29 (R5 quant promotion, ~3 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| MCPT "every serious quant shop" | Exa + Masters/book refs + Bailey DSR literature | `[RETRACTED]` — one valid gate, not universal |
| Brief-audit LLM-as-judge vs keywords | `scripts/skill_audit.py` read (`check_regime_disclosure`) | `[CONFIRMED]` — v1 mechanical keywords shipped; LLM is tool-adoption-only v0.5 |
| LP promotion DSR/markout numeric thresholds | SSH librarian DOCX deep-read | `[CONFIRMED]` — DSR numeric corrupted in source; markout qual thresholds intact (10–50ms non-negative median; 1–5s positive after fees) |

**Pages touched:** `monte-carlo-permutation-test-mcpt`, `regime-conditioned-evaluation`, `lp-algorithm-live-promotion-gates`, `quant-bot-lp-live-promotion-criteria`

### Wave 5 — DONE 2026-05-29 (R6 infra, ~7 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| DeepSeek vision/TVP API surface | Official api-docs sitemap + pricing | `[RETRACTED]` — text-only hosted API; no vision guide |
| Prod RAM / no local inference | `ssh cemini-prod` + `free -h` | `[CONFIRMED]` — 7.6 GiB |
| DeepSeek API key on prod | SSH grep `.env` | `[CONFIRMED]` — `DEEPSEEK_API_KEY` present |
| Prod model/base URL | SSH read client + `.env` | `[CONFIRMED]` — `api.deepseek.com/v1`, `deepseek-chat` (pin v4-flash action) |
| DeepSeek pricing/rate limits | api-docs pricing + rate_limit pages | `[CONFIRMED]` |
| Polymarket WS subscribe + deltas | Live websocket + AsyncAPI docs | `[CONFIRMED]` |
| LB-API `window` values | Live curl | `[CONFIRMED]` — `all`, `1d`, `7d`, `30d`; `1w`/`1m` → 400 |

**Pages touched:** `deepseek-api`, `polymarket-websocket-api`, `polymarket-lb-api`, `polymarket-api-reference`

### Wave 6 — DONE 2026-05-29 (defer tier batch, ~7 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| Polymarket $39.7M arb (K67) | arXiv 2508.03474 fetch | `[CONFIRMED]` — $39,587,585.02; top wallet ~$2.01M |
| zostaff reverse-quant repo | GitHub `zostaff/reverse-research-funds` | `[CONFIRMED]` — MIT, active 2026-05-27 |
| Binary quantization 32× memory | Literature standard + internal gap | `[TENTATIVE]` — technique OK; Cemini recall benchmark pending |
| Bullpen CLI Phase-0 | cli.bullpen.fi + releases repo | `[TENTATIVE]` — official alpha CLI; not open-source core |

**Pages touched:** `polymarket-marginal-polytope-arbitrage`, `trading-posts-compilation-38`, `reverse-quant-engineering-public-filings`, `rag-binary-quantization-at-scale`, `trading-posts-compilation-6`, `bullpen-cli`, `polymarket-copy-trading-strategy`

**Backlog after Wave 6:** ~188 stale tags (195 − 7)

### Wave 7 — DONE 2026-05-29 (gemini-dr + WW179 + PTA, ~10 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| poly_data MIT vs GPL-3.0 | GitHub API + `pyproject.toml` read | `[CONFIRMED]` — LICENSE canonical; Reject stands |
| Kronos pyqlib transitive | GitHub code search + requirements.txt | `[CONFIRMED]` — not in default deps |
| stash go.mod transitive | GitHub API (pgx, mcp-go MIT) | `[TENTATIVE]` — root Apache-2.0; formal go-licenses pending |
| firnflow Cargo.lock copyleft | Cargo.lock spot-check (705 crates) | `[TENTATIVE]` — no GPL/AGPL/SSPL fields; cargo-deny still advised |
| PTA SSRN formulation | SSRN 4549819 abstract + JBF 2026 | `[CONFIRMED]` — price-to-52-week-anchor; bond leg confirmed |
| RHEA NEAR micro-cap | CoinGecko/CMC/Kraken | `[TENTATIVE]` — Rhea Finance token; mcap ~$1.8–8M dispersed |
| LIF Android MAU glitch | SEC Q1 letter + AFR + Motley Fool | `[CONFIRMED]` — multi-source, not WW-only |
| ZeroCortex 7-agent pipeline | Vendor post; no public repo | `[TENTATIVE]` — marketing only; pattern steal-from |

**Pages touched:** `gemini-dr-wave5a/b`, `alash3al-stash`, `pta-metric-anchoring-ssrn`, `ww-issue-179`, `lif`, `warproxxx-poly-data`, `polymarket-research-throughput-bottleneck`, `zerocortex-ai`

**Backlog after Wave 7:** ~178 open tags (~188 − 10)

### Wave 8 — DONE 2026-05-29 (gemini-dr wave5b engineering, ~8 tags closed)

| Claim | Method | Verdict |
|-------|--------|---------|
| poly-maker JS→Python | GitHub `poly_merger/` read (~140 LOC) | `[TENTATIVE]` — clean-room port feasible |
| BTC bot Python 3.14+ exclusivity | Source scan `bot.py` | `[RETRACTED]` — badge only; no exclusive syntax |
| Substreams remote (Pinax) | spkg.io + Pinax polygon endpoint docs | `[CONFIRMED]` — no local indexer required |
| MCP rate-limiter under load | `rate_limiter.py` + perf tests | `[TENTATIVE]` — unit harness exists; prod soak pending |
| MCP secret management | `.env.example` + docker-compose | `[CONFIRMED]` — solo-dev OK; vault for prod |
| GPL backtest subset salvage | LICENSE file read (LGPL+MIT mix) | `[RETRACTED]` — no safe extract |
| 5 unavailable URLs re-fetch | HTTP/GitHub/HF probes | `[CONFIRMED]` reachable; CoMeT Noncommercial Reject |

**Pages touched:** `gemini-dr-wave5b`, `caiovicentino-polymarket-mcp-server`, `aulekator-polymarket-btc-bot`

**Backlog after Wave 8:** ~170 open tags (~178 − 8)

### Steady state

- Target: **≤30** open dated tags (internal benchmarks only)
- Cadence: quarterly sweep prompt (proposed meta page)
- Ingest gate: max 3 new `[NEEDS VERIFICATION]` per source unless user approves

## Commands

```bash
# Full stale list
python3 scripts/wiki_lint.py 2>&1 | tee .local/reports/needs-verification-$(date +%Y-%m-%d).txt

# Revenue-priority recount (after manifest script lands)
python3 scripts/wiki_gap_detect.py   # Type D candidates
```
