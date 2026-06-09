---
title: "Polymarket retail trading discipline — edge framing, sizing, fades, and resolution hygiene"
type: concept
tags: [concept, polymarket, risk-management, retail-trading, k57]
keywords: [vorty2797, quarter-kelly, overreaction-fade, scale-out-ladder, resolution-red-flags, py-clob-client-v2, slippage-simulator]
related:
  - sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md
  - entities/people/vorty2797.md
  - concepts/polymarket-copy-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - entities/tools/polymarket-clob-api.md
  - concepts/trading-account-blowup-red-flags-smb.md
  - entities/tools/polysniper.md
  - projects/world-cup-bot/Architecture/Architecture - Pre-live POST checklist.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - sources/trading-posts-compilation-19-2026-06-07.md
  - concepts/retail-pm-edge-myth-debunk.md
  - concepts/market-informedness-market-making.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - "@gambling-wiki/briefs/2026-06-09_k108-gambling-wc-retail-hygiene-from-osint.md"
maturity: draft
created: 2026-05-22
updated: 2026-06-09
clusters: [polymarket, risk]
---

## Relations

- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — Post 4 (@vorty2797)
- @entities/people/vorty2797.md — author
- @concepts/polymarket-copy-trading-strategy.md — copy-trading is tactic 6; must use wallet filters, not blind mirror
- @concepts/polymarket-bot-architecture.md — parent
- @entities/tools/polymarket-clob-api.md — `py-clob-client-v2` reference client
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — complementary bot-side subtractive filters
- @sources/trading-posts-compilation-8-2026-06-09.md — K108 Post 0 (@GodEyeDotFun WC 2026 ten mistakes)
- @gambling-wiki/briefs/2026-06-09_k108-gambling-wc-retail-hygiene-from-osint.md — operator checklist handoff

## Raw Concept

K57 Posts.docx Post 4 — @vorty2797 educational thread (referral-linked). Synthesizes **retail-survival** mechanics distinct from bot-architecture posts: the game is mispricing vs market mid, not outcome prediction. **K108 extension:** @GodEyeDotFun WC 2026 hygiene list (rules/fees/UMA/cross-venue/format) — tournament-specific overlay on tactics 1–7.

## Narrative

### Core framing

- Trade when **your model probability − market mid** is explainable; otherwise you are liquidity for informed flow.
- 2026 Polymarket ≠ 2023: naive YES-on-news and blind consensus fades are largely arbed; bots compress information quickly.

### Seven tactics (with code patterns)

| # | Tactic | Mechanism |
|---|--------|-----------|
| 1 | Cap size | Max 2–5% bankroll/trade; quarter-Kelly with hard cap |
| 2 | Fade news overreaction | 2h window, ≥15% move → fade after exhaustion |
| 3 | Scale out | 33/33/34 at +40%/+80%/+150% style ladder; never average down |
| 4 | Specialize | 2–3 categories via Gamma `tag_slug` filter |
| 5 | Depth check | Slippage simulator on order book before market orders |
| 6 | Copy smart wallets | Filter: ≥100 trades, ≥55% WR, PF≥1.5, DD≤40%, ≥6mo — **not** blind copy |
| 7 | Resolution hygiene | Keyword red flags: discretion, widely reported, concede, etc. |

### Client note — CLOB Python SDK

Post claims **`py-clob-client-v2`** is the current official Python CLOB client and legacy `py-clob-client` archived May 2026. **`[CONFIRMED 2026-05-29]`** — Polymarket docs list `py-clob-client-v2` as the official Python SDK; legacy `py-clob-client` GitHub repo is **archived** and explicitly states V1 no longer works against production CLOB V2 [Sources: https://docs.polymarket.com/api-reference/clients-sdks, https://docs.polymarket.com/v2-migration, https://github.com/Polymarket/py-clob-client (retrieved 2026-05-29)]. **Cemini action:** pin `py-clob-client-v2` for any new Polymarket order-path work; do not install `py-clob-client`.

### WC 2026 overlay (K108 Post 0)

| # | Mistake | Tie to existing tactics |
|---|---------|-------------------------|
| 1 | Trade title not rules | Extends tactic 7 (resolution hygiene) — ET/penalties/abandonment |
| 2 | Ignore fees + spread | Sports taker ~0.75% peak at 50¢; maker rebates; round-trip 1–2% on liquid books |
| 3 | Longshot festival | Favorite-longshot bias; needs concrete mispricing thesis |
| 4 | Outright winner lockup | Prefer stage markets (group, R16) for capital velocity |
| 5 | Thin niche books | Extends tactic 5 (depth/slippage) |
| 6 | Gut sizing | Reinforces tactic 1; pre-commit drawdown brakes (20/40/50%) |
| 7 | Revenge trading | Daily trade cap during group-stage density |
| 8 | UMA dispute latency | 2h challenge → 48–96h DVM; favor templated sports rules |
| 9 | Single-venue anchor | Cross-venue de-vig vs Kalshi/books; stale PM liquidity |
| 10 | 48-team format drift | Third-place math, extra knockout round, heat/fatigue |

### Cemini posture

Informational for **human operators** and **risk gates** on any future retail-facing Cemini UI — not a deployment spec. Complements `@concepts/polymarket-copy-trading-strategy.md` adversary model (informed vs uninformed flow). WC overlay feeds `@gambling-wiki` operator checklist and WC LP safety DR — not bot deployment.

## Snippets

> "You are not losing because you guessed wrong. You are losing because you did not understand what game you are playing." [Source: Posts.docx — @vorty2797 Post 4]

> "If your model says 0.75 and the mid says 0.62, you have something. If you cannot articulate why your number is different, close the tab." [Source: Posts.docx — @vorty2797 Post 4]

> "Always price the trade after costs, and consider posting limit orders instead of crossing the spread." [Source: Posts.docx K108, @GodEyeDotFun Post 0]
