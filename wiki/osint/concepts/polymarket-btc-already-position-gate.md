---
title: Polymarket BTC already-position gate — ask where price is, not where it goes
type: concept
tags: [concept, polymarket, btc-updown, bot-architecture, microstructure, k62]
keywords: [position-already, dynamic-threshold, direction-efficiency, tape-speed, gustafssonkotte, env-flag, quadrant-deprecation]
related:
  - sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md
  - sources/trading-posts-compilation-38-2026-05-26.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - entities/people/gustafssonkotte.md
  - concepts/polymarket-three-quadrant-blacklist-microtrend.md
  - concepts/multi-module-bot-conflict-detector-pattern.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/polymarket-updown-indicator-stack.md
  - concepts/polymarket-bot-architecture.md
  - concepts/polymarket-updown-15min-execution-latency.md
maturity: draft
created: 2026-05-24
updated: 2026-05-27
---

## Relations

- @sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md — K62 primary source
- @sources/trading-posts-compilation-38-2026-05-26.md — K67 Post 32 FOK execution fix
- @sources/trading-posts-compilation-20-2026-05-27.md — K69 Post 5 decimal-format silent reject + reversal guard sweep
- @entities/people/gustafssonkotte.md — operator
- @concepts/polymarket-three-quadrant-blacklist-microtrend.md — prior Q1/Q2/Q3 direction stack; demoted after K62
- @concepts/multi-module-bot-conflict-detector-pattern.md — K55 lineage (conflict skip vs new first-branch gate)
- @concepts/polymarket-updown-bot-taxonomy.md — 5-min BTC UpDown markets
- @concepts/polymarket-bot-architecture.md — execution-plumbing / guard-stripping lesson

## Raw Concept

K62 @Gustafssonkotte essay: after 330-trade study, **direction prediction ≈ coin flip** on Polymarket 5-min BTC; edge shifts to detecting **where spot already sits relative to strike** with a **volatility-scaled margin**, run **before** legacy multi-module direction voters.

## Narrative

### Problem statement

Short-horizon Up/Down markets price **binary strike distance**. If trend/momentum/book/regime all predict direction at ~50% on 330 labeled trades [TENTATIVE single-operator], adding more directional modules is negative EV.

### Core pattern — “already position” gate

| Step | Behavior |
|------|----------|
| 1 | Measure whether current BTC is **already** on one side of the strike by a **dynamic margin** |
| 2 | Margin scales with **tape speed** — small move sufficient in quiet tape; large move required when violent |
| 3 | If gate passes → allow entry logic; **legacy quadrants do not vote** on direction (author: they were the coin flip) |
| 4 | Feature gated by **one ENV flag**; operator runs day session on, overnight off (thin liquidity) |

This is structurally different from @concepts/multi-module-bot-conflict-detector-pattern.md (internal disagreement skip) — it **replaces** the primary question rather than filtering conflicting answers.

### Plumbing prerequisite

Author reports prior strategy failed despite “correct brain” because **four legacy guards** blocked entries: entry-price cap, pocket guard, slippage check, dropped inter-stage flag. Fix: strip guards + **one line** to persist carry flag. Aligns with @concepts/polymarket-bot-architecture.md “execution > strategy.”

### Early results [TENTATIVE n=9]

7W / 2L; first session with **both UP and DOWN** fills; losses at window edge → threshold tuning, not architecture rejection.

### Cemini application sketch

- For Cemini UpDown or similar: compute **strike distance / realized micro-vol** before ensemble direction models
- Log **direction-module accuracy** separately — if ≈50%, demote or zero-weight per K62 evidence
- Keep **ENV kill-switch** + session liquidity schedule as operational defaults
- Do not treat 9-trade day as validated edge — require export-verified sample (Polymarket CSV rule from K55/K57). **2026-05-24 check:** no public `polymarket.com/@gustafssonkotte` profile; wallet unpublished — K62 n=330 / n=9 remain author-only.

### K67 execution addendum — FOK vs resting limit (Post 32)

@Gustafssonkotte reports **96% backtest vs ~60% live** on export — not logic failure but **12s resting limit** orders that chase price. Fix: **fill-or-kill / immediate** with small cushion; env flag toggles behavior. Reinforces @concepts/polymarket-bot-architecture.md: measured edge on snapshots ≠ live fills.

### K69 silent-reject addendum (Post 5, 2026-05-27)

New failure mode worse than loud crashes: **brain fired 10 entries, order layer placed zero** — exchange rejected **order size decimal precision** (too many decimals). One rounding fix restored flow. Same post: **verify settled outcomes**, not pre-close snapshots (2/4 "obvious" wins were wrong); **last-30s reversal** can flip apparent winners; reversal-guard margin swept on history with one-notch safety buffer.

### Relation to K57 quadrant/blacklist

| Layer | K57 | K62 |
|-------|-----|-----|
| Direction | Q1/Q2/Q3 + micro override | Quadrants **no vote** |
| Filters | Pattern blacklist (subtractive) | Still compatible — blacklist after gate |
| Lesson | Fix one-sided stream | Abandon direction question |

## Snippets

> "Not where is the price going, but where is it already." [Source: @sources/gustafssonkotte-cheat-code-position-already-2026-05-24.md]

> "Nine trades is a signal, not a victory." [Source: same]
