---
title: "Polymarket sports LP — operating rules (WC bot + Cemini)"
type: concept
tags: [concept, polymarket, lp-rewards, sports, market-making, operating-rules, k82]
keywords: [max-spread, pre-match-cancel, fill-handler, queue-depletion, maker-rebates, bilateral-liquidity]
related:
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/world-cup-advance-market-bot-v1.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - entities/tools/world-cup-bot.md
  - entities/tools/openfootball-worldcup-json.md
  - sources/world-cup-github-repo-eval-2026-05-29.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
  - sources/gemini-wc-knockout-market-map-2026-05-30.md
  - sources/gemini-wc-inplay-pregame-lp-risks-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-2026-05-30.md
  - sources/gemini-wc-tournament-phase-router-architectural-spec-2026-05-31.md
  - meta/wc-lp-safety-cadence.md
maturity: validated
created: 2026-05-29
updated: 2026-05-31
---

## Relations

- @concepts/polymarket-lp-rewards-farming.md — general LP strategy; this page is **sports-specific ops**
- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — K84 extreme-bound team verdicts
- @sources/gemini-wc-tournament-phase-router-architectural-spec-2026-05-31.md — follow-up FSM hooks and transition-gating details for phase-aware risk control
- @concepts/world-cup-advance-market-bot-v1.md — primary consumer

## Raw Concept

Distilled from Gemini LP WC report + Seb Montgomery/DuneHammer podcast (`N8QP23vcXM0`) + Dextrabot automation (`pxaRX8q-e6M`) + Ali Nuraldin failure (`-_E_PLRui7c`). These are **implementation invariants** for any sports LP bot on Polymarket.

## Narrative

### Market selection

1. **Distant kickoff** — prefer >24h; hard minimum >10h before first quote.
2. Read **Rewards tab** per market: `max_spread`, `min_shares`, daily pool.
3. Prefer lower-competition books (not top of rewards leaderboard whales).
4. For WC: series = advance-to-knockout, not match props or winner futures.

### Quoting

| Rule | Detail |
|------|--------|
| Order type | **Limit only** — never market cross for exit unless emergency flatten |
| Spread placement | Within `max_spread` of midpoint; closer = more rewards, more fill risk |
| Bilateral | Both YES and NO when possible; **required** if either side <10¢ or mid >90¢ |
| Size | Respect `min_shares` (often 500–1000); cap ~$2K/market notional |
| FIFO | Cancel/replace to stay top of queue |

### Fill handler

| Event | Action |
|-------|--------|
| Any fill | Post limit exit within **60s** at break-even or small loss |
| Queue depletion | If **≥$300** notional ahead of you gets filled → cancel and re-evaluate |
| Volatility | **25%** drop from local peak → cancel + cooldown |
| Draw (football) | Do not assume two-sided hedge holds — still flatten |

**Goal:** earn rewards **without** holding directional inventory through kickoff.

### Match calendar guard

- **Cancel all orders 6–10 hours before kickoff** for affected teams (v1 default).
- **Phase-aware extensions (DR 09 — implement in v2):** final group MD3 → **12h**; knockout R32→Final → **24h**; ghost-quote rule → cancel team futures **≥5 min before** expected KO match end.
- **Never** quote during live play.
- Kill switch: live-window fill → flatten + halt bot.

### Pregame information gates (DR 09)

| Trigger | v1 action |
|---------|-----------|
| Confirmed XI / official injury at presser | Full skip; rely on T-10h cancel |
| Unverified lineup leak | `human_review`; stop queue replenish |
| Anomalous queue depletion | Pull quotes; do not replenish at prior tick |

### Extreme-bound markets (mid ≥ 90¢) — K84 team assessments

When advance markets trade at **≥90¢**, bilateral quoting is mandatory and economics shift to **rewards-only** with elevated toxic flow:

| Posture | When | Bot action |
|---------|------|------------|
| **skip** | Injury/friendly windows + skewed mid (Spain K84) | No quotes; monitor only |
| **reduce** | Confirmed squad risk but still quotable (Brazil K84) | Min size, max spread, tight cancel |
| **human_review** | Unknown depth / conflicting medical wires (Morocco K84) | Gate automation until operator OK |

All such verdicts are **`[NEEDS VERIFICATION 2026-06-06]`** pre-tournament — re-run safety DR weekly through Cup window.

### Economics reminder

- Maker rebates on filled limits **do not** justify holding through matches.
- Ali Nuraldin pattern: positive reward accrual + negative directional P&L = net loss.
- 79% of addresses never earned LP rewards [TENTATIVE — Gemini pitfalls report].

### Kalshi contrast (cross-venue leg)

- Kalshi: limit = maker, market = taker; min 1 contract; free API (@sources/world-cup-youtube-research-compilation-2026-05-29.md SharpMoney).
- Cross-venue arb: **≥2% net** minimum (wangr); verify rules text match.

## Snippets

> "Cancel all my orders at least six to 10 hours before the game." [Source: N8QP23vcXM0 via world-cup-youtube-research-compilation-2026-05-29.md]

> "If there are bids in front of me worth of $300 accepted, cancel my bid and replenish." [Source: pxaRX8q-e6M Dextrabot]
