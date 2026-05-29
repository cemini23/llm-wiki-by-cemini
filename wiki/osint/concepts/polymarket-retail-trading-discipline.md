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
maturity: draft
created: 2026-05-22
updated: 2026-05-29
clusters: [polymarket, risk]
---

## Relations

- @sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md — Post 4 (@vorty2797)
- @entities/people/vorty2797.md — author
- @concepts/polymarket-copy-trading-strategy.md — copy-trading is tactic 6; must use wallet filters, not blind mirror
- @concepts/polymarket-bot-architecture.md — parent
- @entities/tools/polymarket-clob-api.md — `py-clob-client-v2` reference client
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — complementary bot-side subtractive filters

## Raw Concept

K57 Posts.docx Post 4 — @vorty2797 educational thread (referral-linked). Synthesizes **retail-survival** mechanics distinct from bot-architecture posts: the game is mispricing vs market mid, not outcome prediction.

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

### Client note [NEEDS VERIFICATION 2026-05-22]

Post claims **`py-clob-client-v2`** is the current official Python CLOB client and legacy `py-clob-client` archived May 2026. Verify against Polymarket docs before any Cemini dependency pin change.

### Cemini posture

Informational for **human operators** and **risk gates** on any future retail-facing Cemini UI — not a deployment spec. Complements `@concepts/polymarket-copy-trading-strategy.md` adversary model (informed vs uninformed flow).

## Snippets

> "You are not losing because you guessed wrong. You are losing because you did not understand what game you are playing." [Source: Posts.docx — @vorty2797 Post 4]

> "If your model says 0.75 and the mid says 0.62, you have something. If you cannot articulate why your number is different, close the tab." [Source: Posts.docx — @vorty2797 Post 4]
