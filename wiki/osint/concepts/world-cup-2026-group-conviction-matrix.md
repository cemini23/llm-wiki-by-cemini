---
title: "World Cup 2026 — group conviction matrix (research synthesis)"
type: concept
tags: [concept, world-cup-2026, conviction, group-stage, prediction-markets, k82]
keywords: [deadball-tv, b-wade-picks, turkey, colombia, usa-fade, switzerland, third-place, advance-markets]
related:
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md
  - sources/gemini-wc2026-third-place-advancement-2026-05-29.md
  - sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md
  - sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md
  - sources/gemini-wc-conviction-config-audit-2026-05-31.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
  - concepts/world-cup-tournament-phases-lp-strategy.md
maturity: validated
created: 2026-05-29
updated: 2026-05-31
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — YAML conviction config consumes this matrix
- @sources/gemini-wc2026-group-b-lp-analysis-2026-05-29.md — Group B LP tiers (K83)
- @sources/gemini-wc2026-third-place-advancement-2026-05-29.md — third-place caps/skips
- @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md — live cross-venue verification
- @sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md — K84 per-team LP safety verdicts (time-volatile)
- @sources/gemini-wc-conviction-config-audit-2026-05-31.md — full 43-team stale-config pass; urgent downgrade candidates before kickoff

## Raw Concept

Synthesis of **DeadBall TV** (11 group previews), **B Wade Picks**, batch-1 pundit videos, and **Gemini DR** reports (K82 + **K83 May 29 batch** + **K84 May 30 LP safety**). All picks **[TENTATIVE]** except K83 Group B / live gap rows marked validated — bot loads team list from config; **prices from Gamma at runtime**. **LP safety verdicts `[NEEDS VERIFICATION 2026-06-06]`** — re-run before Group C/H kickoff (~Jun 13).

## Narrative

### DeadBall predicted standings (single source — DeadBall)

| Grp | 1st | 2nd | 3rd | 4th | Notes |
|-----|-----|-----|-----|-----|-------|
| A | Mexico (5) | S. Korea (5) | Czechia (4) | S. Africa (1) | Mexico floor 3rd possible |
| C | Brazil (9) | Morocco (6) | Scotland (3) | Haiti (0) | Scotland best-3rd on 3 pts |
| D | **Turkey (6)** | Australia (4) | Paraguay (4) | **USA (3) OUT** | Max research/market split |
| E | GER (5) | CIV (5) | Ecuador (5) | Curaçao (0) | 3-way tie 5 pts |
| F | Netherlands (7) | Sweden (6) | Japan (4) | Tunisia (0) | Japan 4 pts — 3rd-place math |
| G | Belgium (7) | Egypt (4) | Iran (3) | NZ (2) | Iran may miss best-3rd |
| H | Spain (7) | Uruguay (5) | **Cape Verde (4)** | Saudi (0) | CV 3rd advances |
| I | France (7) | Senegal (6) | Norway (4) | Iraq (0) | |
| J | Argentina (6) | Austria (6) | Algeria (4) | Jordan (1) | Austria GD over ARG |
| K | **Colombia (7)** | Portugal (6) | DR Congo (2) | Uzbek (1) | |
| L | England (9) | Croatia (6) | Panama (3) | Ghana (0) | |

**Group B (Gemini DR K83 — DeadBall video still useful but tiers from DR):**

| Team | Tier | Cap | Notes |
|------|------|-----|-------|
| Switzerland | bilateral / fade_watch | $2000 | Whale book ~87¢; bilateral only |
| Canada | yes_conviction | **$2500** | Host edge; monitor Davies |
| Bosnia | fade_watch | alert | 8–11pp PM vs Kalshi — no auto YES |
| Qatar | skip + fade_watch | — | 11–14pp divergence |

### Conviction LP seeds (YAML v4 — `world-cup-bot/config/conviction.yaml`)

**YES advance — mid-tier (prefer mid 0.20–0.80):**

`canada`, `turkey`, `colombia`, `morocco`, `ecuador`, `senegal`, `norway`, `paraguay`, `algeria`, `cape-verde`, `japan`, `scotland`, **`ivory-coast`** (cap $2500 — +51pp mispricing K83)

**Two-sided only (90¢+):**

`spain`, `france`, `germany`, `brazil`, `argentina`, `england`, `portugal`, `mexico`, `switzerland`

**Fade / cross-venue watch (not auto-size-up YES):**

`usa`, `mexico`, `switzerland`, `england`, `croatia`, **`bosnia`**, **`qatar`**

**Skip (per_team):**

`usa`, `qatar`, **`dr-congo`**, `ghana`, `haiti`, … (see YAML)

### Cross-venue alert pairs

**Live May 29 [CONFIRMED]:** group-winner pairs only; all gaps **<5pp** — no alerts fired. PM advance slugs **TBD** — see @sources/gemini-wc2026-market-gap-live-verification-2026-05-29.md.

**Prior book-vs-Kalshi advance gaps [TENTATIVE — not reproduced on live group-winner mids]:**

| Market | Signal |
|--------|--------|
| USA advance | PM high vs Kalshi ~44% R16 (K82) |
| Switzerland advance | Books 92% vs Kalshi 55% (K82) |
| England advance | Books 99% vs Kalshi 74% (K82) |
| Croatia advance | Books 82% vs Kalshi 35% [verify live] |

### B Wade vs DeadBall splits

| Topic | DeadBall | B Wade |
|-------|----------|--------|
| Group A winner | Mexico | SK (groups) / Mexico (depth video) |
| Group B | (video exists — DR tiers above) | Switzerland win 53% Kalshi; Canada threat |
| Group D | USA out | USA 45% win, R16+ |
| Group F | Netherlands 1st | **Japan** 1st (26% Kalshi) |
| Group K | Colombia 1st | Portugal 64% win |

### K84 LP safety verdicts (May 30 snapshot — not prices)

| Team | LP safety | Notes |
|------|-----------|-------|
| Spain | **skip** | Yamal injury + Jun 4/8 friendlies |
| Brazil | **reduce** | Neymar calf; widen spreads / cut size |
| Morocco | **human_review** | Aguerd injuries; depth unknown |

**Shipped in repo (2026-05-30):** Spain skip, Brazil $500 cap, Morocco human_review — **do not** publish static mids in Issue 3.

### Third-place tiebreakers (48-team)

Points → GD → goals scored → H2H → fair play → lots. Bot should model **GD sensitivity** for Scotland, Iran, Panama-type 3rd-place races (@sources/world-cup-youtube-research-compilation-2026-05-29.md B Wade explainer).

## Snippets

> DeadBall Group D: "In fourth, I got the USA on three points." [Source: world-cup-youtube-research-compilation-2026-05-29.md / DeadBall 3bqj4ObETss]

> K83 live gap sweep: group-winner PM↔Kalshi gaps all <5pp May 29; advance pairs blocked. [Source: gemini-wc2026-market-gap-live-verification-2026-05-29.md]
