---
title: "Gemini DR — 2026 World Cup prediction market structure & contract inventory"
type: source
tags: [source, gemini-deep-research, world-cup-2026, polymarket, kalshi, prediction-markets, k82]
keywords: [world-cup, advance-to-knockout, group-qualifiers, contract-mapping, gamma, kalshi-qualifiers, maker-rebates, liquidity-rewards]
related:
  - sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md
  - sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md
  - sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md
  - sources/world-cup-youtube-research-compilation-2026-05-29.md
  - concepts/world-cup-advance-market-bot-v1.md
  - concepts/cross-venue-arbitrage-pattern.md
  - entities/platforms/polymarket.md
  - entities/platforms/kalshi.md
maturity: validated
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @sources/gemini-polymarket-lp-rewards-world-cup-2026-05-29.md — LP economics companion
- @sources/gemini-sports-prediction-bot-pitfalls-2026-05-29.md — failure modes companion
- @sources/gemini-world-cup-squad-mispricing-analysis-2026-05-29.md — squad/divergence companion
- @concepts/world-cup-advance-market-bot-v1.md — primary consumer of contract map

## Raw Concept

| Field | Value |
|-------|-------|
| Title | 2026 World Cup Prediction Market Research |
| Author | Gemini Deep Research (user prompt) |
| Type | docx synthesis report |
| Location | `cemini-librarian:/opt/cemini-bulk/research/2026 World Cup Prediction Market Research.docx` |
| Retrieved | 2026-05-29 |
| Read status | deep-read |

## Narrative

Long-form Gemini report on **Polymarket × Kalshi** World Cup 2026 market topology as of May–June 2026 pre-tournament window. Primary value for Cemini + public OSS bot: **exact contract typology**, **cross-venue naming map**, **fee/rebate stack**, and **group-by-group advance-market inventory** (48 teams, 12 groups).

### 48-team format implications

- Top two per group + **eight best third-place** teams → Round of 32 ([CONFIRMED] FIFA 2026 rules).
- Elite teams trade **97–98¢** to advance pre-kickoff — poor directional bets, viable **LP + maker-rebate** targets if bilateral quoting is enforced above 90¢.
- Mid-tier nations cluster **20–80¢** — best band for asymmetric YES-heavy conviction LP.

### Contract map (primary series for bot)

| Polymarket | Kalshi | Notes |
|------------|--------|-------|
| `FIFA World Cup: Team to advance to Knockout Stages` | `World Cup Group [X] Qualifiers` | **Core bot target** — resolves ~group stage end (~2026-06-28 PM) |
| `FIFA World Cup Group [X] Winner` | `Group [X] Winner` | Separate series; repricing during group play |
| `2026 FIFA World Cup Winner` | `Men's World Cup Winner` | Deep liquidity; capital lockup; out of v1 directional scope |
| Match moneylines | `Games` category (fixture-named) | In-play toxic for LP v1 |
| Kalshi-only | `Group [X] Team to Finish Bottom` | Inverted short on minnows |

### Platform microstructure deltas

- **Polymarket:** hybrid CLOB on Polygon; **maker free** + **liquidity rewards** + sports **maker rebates** (25% of taker fees, Apr 2026 program [TENTATIVE single-source]); dynamic sports **taker fees** (~0.75–1.8% peak near 50¢).
- **Kalshi:** CFTC DCM; **zero maker fee** on most contracts; taker ~$0.01–0.02/contract; resolves via **ESPN/Fox/WSJ/Reuters** consensus (faster than FIFA-only PM path).
- **Resolution risk:** PM continuous elimination (team → No when impossible); Kalshi media-consensus — tail risk on post-match protests/VAR reversals [TENTATIVE].

### Advance-market depth snapshot (May 2026 — illustrative, not hardcoded)

Report includes per-group tables (Mexico ~90%+, Brazil 97%, Germany 97%, USA ~85%, Turkey 76%, etc.) with Kalshi multiplier equivalents. **Bot must fetch live** via Gamma + Kalshi API at runtime — these are research anchors only.

### Group highlights (advance series)

- **Group A:** Mexico co-host premium; SK/Czechia battle for second.
- **Group D:** USA patriotic flow vs physical group — "Group of Death-lite."
- **Group H:** Spain dominance; Uruguay/Cape Verde/Saudi tail.
- **Hosts advance macro:** PM "All hosts reach knockout" traded 55–63% band historically in report.

## Snippets

> "The defining predictive puzzle of the expanded 2026 World Cup lies in the group stage… elite nations… trade at hyper-inflated premiums — often upwards of 97 cents." [Source: 2026 World Cup Prediction Market Research.docx]

> Polymarket resolves via FIFA + credible reporting; Kalshi via ESPN, Fox Sports, WSJ, Reuters. [Source: 2026 World Cup Prediction Market Research.docx]
