---
title: "World Cup advance-market bot — v1 specification (OSS + Cemini module)"
type: concept
tags: [concept, world-cup-2026, polymarket, kalshi, lp-bot, market-making, oss, cemini-prod, k82]
keywords: [advance-to-knockout, conviction-lp, cross-venue-scanner, fill-handler, gamma-api, clob-api, outlier-weekly]
related:
  - sources/gemini-world-cup-market-structure-research-2026-05-29.md
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - sources/gemini-wc2026-cross-venue-arbitrage-dynamics-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - concepts/world-cup-2026-group-conviction-matrix.md
  - concepts/polymarket-sports-lp-operating-rules.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/polymarket-sports-microstructure-bot-taxonomy.md
  - entities/infrastructure/cemini-egress-fi.md
  - entities/tools/polymarket-gamma-api.md
  - entities/tools/polymarket-clob-api.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - entities/tools/world-cup-bot.md
  - entities/tools/openfootball-worldcup-json.md
  - sources/world-cup-github-repo-eval-2026-05-29.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
clusters: [polymarket, world-cup, market-making, oss]
---

## Relations

- @concepts/polymarket-lp-bot-phase0-spec.md — generic LP bot architecture; **this page is the sports/WC vertical slice**
- @concepts/polymarket-sports-lp-operating-rules.md — fill/cancel/quote rules
- @concepts/world-cup-2026-group-conviction-matrix.md — YAML conviction seeds
- @entities/infrastructure/cemini-egress-fi.md — PM order POST egress (Finland)
- @concepts/cross-venue-arbitrage-pattern.md — alert-only cross-venue pattern
- @entities/tools/world-cup-bot.md — public MIT repo ([cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot))
- @sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md — K83 Group B YAML tiers
- @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md — `cross_venue.yaml` seed

## Raw Concept

K82 research wave (4× Gemini DR + 35 YouTube videos) synthesized into a **dual-deliverable** spec:

1. **Public MIT repo — [World Cup Bot](https://github.com/cemini23/world-cup-bot)** (`@entities/tools/world-cup-bot.md`). Product name **World Cup Bot**; GitHub slug `world-cup-bot`. **Shipped 2026-05-30** (main @ `17708e1`, 128 pytest). Outlier Weekly Issue 3 marketing **2026-06-03**.
2. **CeminiSuite module** — same codebase, private env on `cemini-prod` / egress path; **never** committed to the public repo.

**No hardcoded prices** — all mids, spreads, reward params, and kickoff times fetched at runtime from **Gamma + CLOB**. Prod uses server credentials; public OSS uses `.env` only (see repo `SETUP.md`).

### Public vs private boundary

| Layer | Public repo | Private (Cemini / prod) |
|-------|-------------|-------------------------|
| Source code | MIT on GitHub | Same tree; merge via server-Claude after brief |
| API keys / wallet | `.env.example` placeholders | Real keys on prod only |
| Egress / relay | Documented as "your egress IP" | `cemini-egress-fi` for PM POST |
| Conviction YAML | Example teams + caps in docs | Full matrix from `@concepts/world-cup-2026-group-conviction-matrix.md` |
| Issue 3 / marketing | Behavior + setup | No prod hostnames or internal paths |

Nothing published publicly **connects to** operator prod unless an operator clones the repo and supplies their own credentials.

## Narrative

### Strategy stack (three layers)

| Layer | v1 scope | Mechanism |
|-------|----------|-----------|
| **1. Conviction LP** | **IN** | Resting YES-heavy limits on `advance to knockout` for research-backed mid-tier teams; mandatory NO side when mid >90¢ |
| **2. Repricing** | Manual/alert | Sell-before-resolution as group results land — bot exits fills; optional human directional adds |
| **3. Cross-venue arb** | **Alert-only** | PM vs Kalshi advance/qualifier gaps ≥5pp after fees; semantic contract match required |

### Out of v1 (v2 roadmap — @concepts/world-cup-tournament-phases-lp-strategy.md)

**Out of v1:** match-level markets, in-play microstructure, auto Kalshi execution, winner futures bankroll, `$POLY` airdrop farming, Kalshi parlays.

**v2 (post-group):** reach-final LP, knockout match markets (after DR 08–10), phase router, in-play hard halt + lineup gates.

### Timeline

| Date | Event |
|------|-------|
| 2026-05-29 | **Repo reserved** — [github.com/cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot) (README, SETUP, SECURITY; no secrets) |
| 2026-05-30 | **v1 shipped** — modules 1–7, liquidity gate, shadow automation, systemd monitor profile |
| 2026-06-03 | Outlier Weekly Issue 3 + public launch narrative |
| 2026-06-11 | Group stage kickoff |
| ~2026-06-28 | Advance markets resolve (PM) |

### Architecture

```
┌──────────────────────────────────────────────────────────────┐
│ 1. SCANNER (Gamma)                                           │
│    Filter: "advance to knockout" × FIFA WC 2026              │
│    Fetch: reward_pool, max_spread, min_shares, midpoint      │
│    Filter: kickoff_hours > 10 (prefer > 24)                  │
│    Flag: bilateral_mode if mid > 0.90 or side < 0.10         │
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. CONVICTION FILTER (YAML config)                           │
│    Team list + max notional; human_review injury gates         │
│    Optional: CLOB /book liquidity gate (operating.yaml)       │
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. QUOTER (CLOB via egress-fi for POST)                      │
│    YES-heavy + NO hedge leg; limit orders only               │
│    Cancel/replace for FIFO; cap ~$2K/market                  │
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 4. FILL HANDLER (WS user channel)                            │
│    Fill → limit exit ≤60s (break-even / small loss)          │
│    Queue depletion: $150 ahead filled → pull quotes (WC tune)│
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 5. MATCH CALENDAR GUARD                                      │
│    Fixture kickoffs from data/worldcup2026-fixtures.json     │
│    (CC0 @entities/tools/openfootball-worldcup-json.md)       │
│    T-10h to T-6h: cancel ALL orders for teams playing today  │
│    Kill switch on any live-window fill                       │
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 6. CROSS-VENUE SCANNER (alert-only)                          │
│    Kalshi qualifiers API + PM gamma; rules hash match        │
│    Alert if ≥5pp after fees; no auto hedge                   │
└────────────────────────────┬─────────────────────────────────┘
                             ▼
┌──────────────────────────────────────────────────────────────┐
│ 7. DAILY P&L LEDGER                                          │
│    JSONL + logic_version; pnl-daily vs rewards-sync split     │
└──────────────────────────────────────────────────────────────┘
```

### Deployment

| Component | Where |
|-----------|-------|
| PM order **POST** | `cemini-egress-fi` (Finnish IP) — see `@entities/infrastructure/cemini-egress-fi.md` |
| PM read / Gamma | prod or laptop (public endpoints) |
| Kalshi | US-eligible operator credentials; separate from PM egress |
| Preflight | `GET https://polymarket.com/api/geoblock` from deploy host |

Public **SETUP.md** ([repo](https://github.com/cemini23/world-cup-bot/blob/main/SETUP.md)) documents server region requirement — **not VPN bypass language**.

### Capital tiers (WC advance markets)

| Tier | Notional | Use |
|------|----------|-----|
| Pilot | $500–1K | Single-market learning — structurally weak per Gemini |
| **Standard** | **$2–3K** | **Recommended sweet spot** |
| Scale | $5–10K | Diminishing reward share; needs faster cancel/replace |

### Contract targets (runtime discovery)

- PM: `FIFA World Cup: Team to advance to Knockout Stages` (per team slug)
- Kalshi: `World Cup Group [X] Qualifiers` — map in config when Gemini report #5 / Kalshi API catalog lands

### Risk register

| Risk | Mitigation |
|------|------------|
| Live-match adverse selection | T-6h cancel; kill switch |
| Fill on news | 60s limit exit; queue depletion pull |
| 90¢+ bilateral trap | Mandatory NO leg + size cap |
| Oracle mismatch PM↔Kalshi | Alert-only; rules parser |
| USA/Mexico home-nation flow | Cross-venue fade signals; size limits |
| Reward formula change | Daily Gamma diff; halt if params missing |

### Cemini integration boundary

- Module lives under CeminiSuite Polymarket stack — **reuse CLOB auth**, do not duplicate wallet logic.
- Public canonical repo: `@entities/tools/world-cup-bot.md` — Cemini imports/forks from `cemini23/world-cup-bot`, not a separate internal-only tree.
- This workspace: wiki + briefs + OSS repo authoring (`~/Desktop/projects/world-cup-bot`); prod code merge via server-Claude after brief review.
- Read-only prod verification (`ssh cemini-prod` ls/grep) OK; no `/opt/cemini` edits from here.

### Open items

1. **SHADOW Phase 1 soak** — ≥3 days `plan --record --liquidity-gate` on prod shadow ledger
2. **LP safety DR re-run** — **2026-06-06** per `@meta/wc-lp-safety-cadence.md`
3. Gemini report **#5** — full cross-venue ticker map (optional)
4. CeminiSuite module import — post shadow gate
5. ~~Calendar fixture data~~ — **done** 2026-05-29 via `@entities/tools/openfootball-worldcup-json.md`
6. ~~Module 6 scanner~~ — **done** 2026-05-30 in public repo in public repo

## Snippets

> "The edge is in the plumbing, not the algorithm." — extends @concepts/polymarket-lp-bot-phase0-spec.md MatiasScalbi line to WC vertical.

> LP rewards without fill discipline → net loss (Ali Nuraldin bot season, @sources/world-cup-youtube-research-compilation-2026-05-29.md).
