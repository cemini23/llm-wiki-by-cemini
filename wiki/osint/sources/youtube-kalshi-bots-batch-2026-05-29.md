---
title: YouTube — Kalshi bots batch (May 2026, 7 videos)
type: source
tags: [source, youtube, kalshi, trading-bot, claude-code, sports-signals, k80]
keywords: [processoverprofit, night-shark, part-time-larry, prediction-engineer, momentum-odds, beast-sports-picks, kalshi-api, ui-automation]
related:
  - sources/youtube-polymarket-bots-batch-2026-05-29.md
  - concepts/kalshi-ui-automation-bot-pattern.md
  - concepts/kalshi-api-reference.md
  - concepts/ai-assisted-trading-workflow.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/polymarket-copy-trading-strategy.md
  - entities/tools/momentum-odds.md
  - entities/platforms/kalshi.md
maturity: validated
read_status: deep-read
created: 2026-05-29
updated: 2026-05-29
clusters: [kalshi, trading-bot, sports, retail-promo]
---

## Relations

- @sources/youtube-polymarket-bots-batch-2026-05-29.md — K80 sibling batch (Polymarket bots)
- @concepts/kalshi-ui-automation-bot-pattern.md — videos 1, 6 (Night Shark OCR Kalshi crypto 15-min)
- @concepts/kalshi-api-reference.md — video 2 (Part Time Larry REST tutorial)
- @concepts/ai-assisted-trading-workflow.md — video 3 (Claude Code slippage-preview bot)
- @entities/tools/momentum-odds.md — video 4 (webhook signal → local Kalshi executor)
- @concepts/sports-prediction-consensus-agent.md — videos 4–5 (sportsbook consensus vs PM lines)
- @concepts/polymarket-copy-trading-strategy.md — video 5 (whale wallet tracker promo)
- @entities/platforms/kalshi.md — venue entity

## Raw Concept

| Field | Value |
|-------|-------|
| Batch | 7 YouTube URLs (K80 batch 2) |
| Retrieved | 2026-05-29 |
| Location | `.local/youtube-ingest/2026-05-29-batch2/` → `cemini-librarian:/opt/cemini-bulk/research/youtube-kalshi-bots-batch-2026-05-29-transcripts.md` |
| Read gap | `xp1Lpe3TTMQ` — age-restricted; yt-dlp blocked without browser cookies → **unread-stub** |

**Credibility note:** Third-party creator content — promo claims (PnL, hit rates, whale ROI) require independent verification. ProcessOverProfit stack is **UI automation (OCR)**, not Kalshi API — operational fragility vs Cemini's pykalshi path.

## Narrative

### Video index

| # | Date | ID | Channel | Title | Route |
|---|------|-----|---------|-------|-------|
| 1 | 2026-03-10 | [m9dD0XlpFF0](https://www.youtube.com/watch?v=m9dD0XlpFF0) | ProcessOverProfit | Kalshi bot 10 min v2 (stop-loss + time gate) | @concepts/kalshi-ui-automation-bot-pattern.md |
| 2 | 2024-08-24 | [E2mgWN4ReqQ](https://www.youtube.com/watch?v=E2mgWN4ReqQ) | Part Time Larry | Kalshi API Python tutorial (Colab) | @concepts/kalshi-api-reference.md |
| 3 | 2026-03-19 | [mKr_jW2tPoY](https://www.youtube.com/watch?v=mKr_jW2tPoY) | The Prediction Engineer | Claude Code Kalshi slippage-preview bot | @concepts/ai-assisted-trading-workflow.md |
| 4 | 2026-05-15 | [qPRY5ws3h60](https://www.youtube.com/watch?v=qPRY5ws3h60) | Odds | Kalshi bot + MomentumOdds signals | @entities/tools/momentum-odds.md |
| 5 | 2026-02-23 | [iF6ZWEbkxzM](https://www.youtube.com/watch?v=iF6ZWEbkxzM) | Beast Sports Picks | Sportsbook line vs Kalshi/Polymarket | @concepts/sports-prediction-consensus-agent.md |
| 6 | 2026-04-03 | [Y8tcbq1hS5o](https://www.youtube.com/watch?v=Y8tcbq1hS5o) | ProcessOverProfit | Kalshi trading bot v3 (KuCoin + Night Shark) | @concepts/kalshi-ui-automation-bot-pattern.md |
| 7 | — | [xp1Lpe3TTMQ](https://www.youtube.com/watch?v=xp1Lpe3TTMQ) | — | **Unread** (age gate) | — |

### Cross-cutting themes

1. **API vs UI automation split** — Part Time Larry + Prediction Engineer teach REST/pykalshi-style paths; ProcessOverProfit sells Night Shark screen-scraping on Kalshi crypto 15-min markets (late-session probability trigger → auto-click buy/sell).
2. **Slippage / illiquidity guard** — Prediction Engineer bot previews average fill + slippage before market order; mirrors Cemini's liquidity-first posture on short-horizon books.
3. **Sports edge = line divergence** — Beast Sports + MomentumOdds both frame edge as **sportsbook consensus vs prediction-market line** (totals, moneylines), not in-play microstructure.
4. **Vibe-coding stack** — ChatGPT/Claude Code generating local Python executors with env-var API keys + paper mode appears in videos 3–4.

## Snippets

> "Create a Kalshi bot … ask me for a market … tells me what price I would get filled at and the percent slippage … if I say yes, it market buys … include a paper mode." [Source: https://www.youtube.com/watch?v=mKr_jW2tPoY (retrieved 2026-05-29)]

> "Trigger point 90 means whenever whichever price reaches 90 first, we're going to enter … trigger minute … if you set it to five, that means whenever there's five minute left, then only … activates." [Source: https://www.youtube.com/watch?v=m9dD0XlpFF0 (retrieved 2026-05-29)]

> "Sportsbook correlation … takes our signals from momentum odds with over 60 plus sports books … tells us the directions they are hitting on certain games." [Source: https://www.youtube.com/watch?v=qPRY5ws3h60 (retrieved 2026-05-29)]
