---
title: "World Cup 2026 — group conviction matrix (research synthesis)"
type: concept
tags: [concept, world-cup-2026, conviction, group-stage, prediction-markets, k82]
keywords: [deadball-tv, b-wade-picks, turkey, colombia, usa-fade, switzerland, third-place, advance-markets]
related:
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - concepts/world-cup-advance-market-bot-v1.md
  - entities/tools/world-cup-bot.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @concepts/world-cup-advance-market-bot-v1.md — YAML conviction config consumes this matrix
- @sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md — book vs PM/Kalshi divergence column

## Raw Concept

Synthesis of **DeadBall TV** (11 group previews), **B Wade Picks**, batch-1 pundit videos, and **Gemini squad mispricing** report. All picks **[TENTATIVE]** — bot loads team list from config; **prices from Gamma at runtime**.

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

**Group B missing (DeadBall):** B Wade — Switzerland win 53% Kalshi; Canada threat; Bosnia > Qatar advance rank.

### B Wade vs DeadBall splits

| Topic | DeadBall | B Wade |
|-------|----------|--------|
| Group A winner | Mexico | SK (groups) / Mexico (depth video) |
| Group D | USA out | USA 45% win, R16+ |
| Group F | Netherlands 1st | **Japan** 1st (26% Kalshi) |
| Group K | Colombia 1st | Portugal 64% win |

### Conviction LP seeds (YAML starting point)

**YES advance — mid-tier (prefer mid 0.20–0.80):**

`turkey`, `colombia`, `morocco`, `ecuador`, `senegal`, `norway`, `paraguay`, `algeria`, `cape-verde`, `japan` (if 3rd-place math clears)

**Two-sided only (90¢+):**

`spain`, `france`, `germany`, `brazil`, `argentina`, `england`, `portugal`, `mexico`, `switzerland`

**Fade / cross-venue watch (not auto-size-up YES):**

`usa`, `mexico`, `switzerland`, `england`, `croatia` — Gemini book vs Kalshi gaps

### Cross-venue alert pairs (≥5pp research flag)

| Market | Signal |
|--------|--------|
| USA advance | PM high vs Kalshi ~44% R16 |
| Switzerland advance | Books 92% vs Kalshi 55% |
| England advance | Books 99% vs Kalshi 74% |
| Croatia advance | Books 82% vs Kalshi 35% [verify live] |
| Turkey / Colombia group winner | DeadBall 1st vs market 2nd-favorite |

### Third-place tiebreakers (48-team)

Points → GD → goals scored → H2H → fair play → lots. Bot should model **GD sensitivity** for Scotland, Iran, Panama-type 3rd-place races (@sources/world-cup-youtube-research-compilation-2026-05-29.md B Wade explainer).

## Snippets

> DeadBall Group D: "In fourth, I got the USA on three points." [Source: world-cup-youtube-research-compilation-2026-05-29.md / DeadBall 3bqj4ObETss]

> Gemini: Switzerland +37pp book vs Kalshi advance divergence. [Source: gemini-world-cup-squad-mispricing-analysis-2026-05-29.md]
