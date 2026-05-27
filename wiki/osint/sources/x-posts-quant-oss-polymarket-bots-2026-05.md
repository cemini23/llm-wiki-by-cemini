---
title: "X-posts compilation — hedge-fund OSS, Polymarket bot taxonomy, cross-market stat-arb, Hermes weather bot, Claude arb-bot debugging (May 2026)"
type: source
tags: [source, x-posts, social-media, hedge-fund-oss, polymarket-bots, statistical-arbitrage, hermes-agent, weather-trading, latency-arbitrage, k52]
keywords: [zostaff, retrovalix, ridark-eth, 0xmovez, adiix-official, hedge-fund-open-source, arcticdb, jane-street, polymarket-updown-bots, cross-market-arbitrage, cointegration, ornstein-uhlenbeck, order-book-imbalance, micro-price, hermes-agent, nous-research, weather-trading-bot, claude-arbitrage-bot]
related:
  - concepts/hedge-fund-open-source-tooling.md
  - concepts/polymarket-updown-bot-taxonomy.md
  - concepts/prediction-market-statistical-arbitrage.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - concepts/cross-venue-arbitrage-pattern.md
  - concepts/non-latency-arbitrage-strategies.md
  - entities/tools/hermes-agent.md
  - entities/tools/arcticdb.md
  - entities/tools/prediction-market-analysis.md
  - sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md
  - concepts/polymarket-sports-microstructure-bot-taxonomy.md
maturity: validated
read_status: deep-read
created: 2026-05-18
updated: 2026-05-27
clusters: [quant-finance]
---

## Relations

- @concepts/hedge-fund-open-source-tooling.md — synthesized from Post 1 (@zostaff, 22 hedge-fund/quant-firm OSS repos)
- @concepts/polymarket-updown-bot-taxonomy.md — synthesized from Post 2 (@RetroValix, 6 bot types on Polymarket Up/Down markets)
- @concepts/polymarket-sports-microstructure-bot-taxonomy.md — K69 Post 14 (@RetroValix, 7 sports-market bot types)
- @concepts/prediction-market-statistical-arbitrage.md — synthesized from Post 4 (@ridark_eth, cross-market stat-arb quant roadmap)
- @concepts/polymarket-weather-trading-strategy.md — Post 5 (@0xMovez) adds a Hermes-Agent-driven deployment path for the @AlterEgo_eth weatherbot
- @concepts/polymarket-bot-architecture.md — Post 6 (@adiix_official) independently corroborates the @0x_Punisher / @bored2boar bot-build discipline
- @concepts/cross-venue-arbitrage-pattern.md — Post 4 supplies the quant math layer (cointegration, OU, OBI) for the cross-venue arb loop
- @concepts/non-latency-arbitrage-strategies.md — Post 2's "Arbitrage Bot" type is the latency-relaxed YES+NO<\$1 case already documented there
- @entities/tools/hermes-agent.md — Post 5 deploys on Nous Research's Hermes Agent runtime
- @entities/tools/arcticdb.md — Post 1's tick-store repo (Man Group), an adoption candidate for the Cemini market-dataset layer
- @entities/tools/prediction-market-analysis.md — the repo Post 4 advertised; verified 2026-05-18 (real + MIT, but the post misrepresents its contents)
- @sources/trading-posts-farxxxxx-hermes-koroush-2026-05-24.md — K64; Hermes use-case catalog (Post 2) extends Post 5 path
- @seo-wiki/briefs/2026-05-18_ugc-3-platform-monetization-loop.md — Post 3 (@timbidefi UGC creator monetization) routed to seo-wiki as a brief; off-topic for OSINT

## Raw Concept

- **Title**: `posts.docx` — compilation of six X (Twitter) creator posts/articles, separated in-file by `Next post:` markers
- **Type**: social-media long-form posts (X/Twitter creators)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/posts-2026-05-18.docx` (renamed on transfer — a prior posts.docx batch already occupies `posts.docx`; see @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md)
- **Retrieved**: 2026-05-18 (dropped into `research to be indexed/`)
- **Contents**: 6 posts — (1) @zostaff hedge-fund/quant-firm OSS repos; (2) @RetroValix 6-type Polymarket Up/Down bot taxonomy; (3) @timbidefi UGC creator monetization loop *(off-topic → routed to seo-wiki)*; (4) @ridark_eth cross-market statistical-arbitrage roadmap; (5) @0xMovez Hermes-Agent weather-trading bot; (6) @adiix_official Claude latency-arbitrage bot debugging guide (part 2).

## Narrative

### Post 1 — @zostaff: "22 Open Source Repos from Hedge Funds and Quant Firms"

A catalog of 22 public GitHub repos from 7 firms that open-source part of their stack — Two Sigma, Man Group/AHL, Jane Street, D.E. Shaw, Hudson River Trading, Optiver, WorldQuant — contrasted with firms that publish nothing (Renaissance, Citadel, Bridgewater, Millennium, Point72, AQR). Almost all repos are MIT/Apache-2.0/BSD; the one exception is **ArcticDB** (Man Group), under the Business Source License (BSL — free non-production, paid for commercial deployment).

Thesis: the open/closed split maps onto each firm's competitive moat — *if your edge is the people you hire*, open-source the code as a recruiting brand (Two Sigma, D.E. Shaw, Jane Street, HRT); *if your edge is the alpha you discover*, lock everything down (Renaissance, Citadel, Bridgewater). → synthesized into @concepts/hedge-fund-open-source-tooling.md, which carries the full 22-repo table.

Cemini-relevant standouts: **ArcticDB** (server-less S3-backed time-series store — direct adoption candidate for the market-dataset layer), **twosigma/flint** (temporal as-of joins on Spark), and the community **WorldQuant alpha101** implementation (101 formulaic alphas).

### Post 2 — @RetroValix: "6 Main Types of Trading Bots on Up/Down Markets on Polymarket"

Claims to have analyzed 1,000 profitable bots on short crypto Up/Down markets and grouped them into 6 microstructure-trading types: (1) **Arbitrage** (buy Up+Down when sum < \$1.00), (2) **Directional Arbitrage** (arb base, then tilt toward the stronger side), (3) **Repricing / Fair-Value Model** (own fair-value estimate vs lagging Polymarket price), (4) **Cross-Timeframe / Multi-Market** (lag between 5-min and 15-min contracts on the same underlying), (5) **Order-Book Imbalance** (skew/structure trading), (6) **Near-Resolution** (buy the ~0.99 almost-settled side for residual yield, tail-risk exposed). Common DNA across all 6: **limit orders + small repeatable edge + precise execution + hedging + speed**; they trade *structure*, not direction, exploiting the lag between underlying price moving and Polymarket repricing. → synthesized into @concepts/polymarket-updown-bot-taxonomy.md.

### Post 3 — @timbidefi: "Most UGC Creators are wrong. The 3-Platform \$17,000/month loop"

A UGC-creator monetization workflow: reverse-engineer viral TikTok hooks with Claude, build a visual identity from Pinterest references, generate faceless videos with Higgsfield, distribute on TikTok + Instagram + (the under-served) Pinterest, and sell 3-platform retainers instead of per-video. **Off-topic for OSINT/financial research** — creator marketing / social-media operations. Routed to **seo-wiki** as a brief — @seo-wiki/briefs/2026-05-18_ugc-3-platform-monetization-loop.md — and not given an OSINT wiki page. See cross-wiki routing note in `## Snippets`.

### Post 4 — @ridark_eth: "How To Trade Cross-Market Statistical Arbitrage On Prediction Markets"

A quant roadmap for trading the spread between the *same* event listed on Polymarket and Kalshi, plus a claimed public repo + L2 order-book dataset. Two methodologies:

- **Method 1 — Cointegration + Ornstein-Uhlenbeck mean reversion.** Build the spread `S_t = P_Poly − β·P_Kalshi − μ`; test stationarity (ADF / Johansen); model `S_t` as an OU process `dS = θ(μ−S)dt + σ dW`; calibrate θ/μ/σ by MLE on historical data (Euler–Maruyama discretization); enter/exit at thresholds derived from an optimal-stopping problem. Tradeable only if mean-reversion time `τ = 1/θ` beats execution latency.
- **Method 2 — Order-Book Imbalance + micro-price.** `I_t = (V_bid − V_ask)/(V_bid + V_ask) ∈ [−1,1]`; micro-price `P_micro = P_mid + I_t·(spread/2)`; cross-venue, a large imbalance on the faster venue predicts the slower venue's book clearing within a ~200ms window via a rolling Markov transition matrix.

→ synthesized into @concepts/prediction-market-statistical-arbitrage.md. **Caveat — verified 2026-05-18**: the math is standard pairs-trading theory and is correct. The advertised repo `github.com/Jon-Becker/prediction-market-analysis` **is real** (MIT, ~3,378★, active — @entities/tools/prediction-market-analysis.md), but Post 4 **misrepresents it**: the actual dataset is **trades + market metadata** (36 GiB compressed), `[RETRACTED]` *not* the "L2 order-book snapshots, 20 levels, 100ms, 850M state updates" the post claimed, and every setup command in the post is wrong (`cd prediction-market-arbitrage` 404s; `make download-ob` / `orderbooks_l2.tar.zst` / `data/snapshots/` do not exist). Net: Method 1 (cointegration/OU) is backtestable from the real dataset; Method 2 (OBI/micro-price) is not — that needs L2 data the dataset lacks.

### Post 5 — @0xMovez: "Hermes Agent + Polymarket — self-learning weather trading bot \$100 → \$5,000"

A copy-paste deployment guide for a Polymarket weather-trading bot running on **Hermes Agent** — an open-source self-hosted agent by Nous Research (released 2026-02-25; multi-level memory, self-writing skills, 24/7 cron + messaging gateway). Positioned as the successor to OpenClaw (formerly Clawdbot/Moltbot). The bot itself reuses **@AlterEgo_eth's weatherbot** (`github.com/alteregoeth-ai/weatherbot.git`, py-clob-client stack) — 7 prompts walk through: clone+venv, generate a Polygon wallet, fund it, ERC-20-approve the 3 Polymarket exchange contracts + Conditional Tokens, wire a Visual Crossing weather key, paper-then-live scan with EV + Kelly sizing. → adds a deployment path to @concepts/polymarket-weather-trading-strategy.md; Hermes Agent gets its own entity page @entities/tools/hermes-agent.md.

### Post 6 — @adiix_official: "Why your Claude bot doesn't work" (latency-arbitrage bot, part 2)

Follow-up to a 12M-view part-1 article ("How Claude turned \$300 into \$2,382,780"). Diagnoses why reader-built Polymarket latency-arbitrage bots fail and ships a hardened build. The bot class: Binance WebSocket BTC/ETH ticker feed → Polymarket 5/15-min crypto contracts, edge detection (5% detect / 8% execute), half-Kelly sizing (8% portfolio cap), risk halts, paper-mode-first. The article's centerpiece is an updated **"battle-tested" Claude prompt** — a full production-bot spec — plus a setup checklist with explicit go-live gates (≥200 paper trades, >75% paper win rate, ≥7 crash-free days, then VPS deploy). It also restates that **Polymarket is geo-blocked to US residents** — independent corroboration of the Cemini geo-routing findings. → corroboration folded into @concepts/polymarket-bot-architecture.md (the 9-mistake list itself did not survive the docx→text extraction — likely an embedded image/table).

### Caveats

- All six are **social-media creator content** with promotional components (referral links, Telegram/X follows, paid courses). Treat methodology as plausible; treat specific PnL/win-rate numbers (`$300→$2.38M`, `ColdMath $300→$219K`, `Sharky6999 99.3% WR`, `RN1 $1.2K→$7.3M`, `$17k/month`) as `[TENTATIVE]` single-source marketing.
- Posts 2, 4, and 6 converge on the same core claim — short-crypto Polymarket markets reprice with a lag, and the edge is acting on structure before the correction. That triangulation is the genuinely high-signal extract.
- Post 4's quant math is textbook-correct; its repo is real (MIT) but the post misrepresents the dataset (verified 2026-05-18 — trades/markets, not L2). Post 1's repos are real and verifiable; ArcticDB's BSL was verified to permit Cemini's intended use (the post's "paid license" framing is an oversimplification). Post 5's Hermes Agent is a real Nous Research release (ties to the existing @entities/tools/hermes-lcm.md plugin).

## Snippets

> "If your edge is the people you hire: open up the code, attract more PhDs. If your edge is the alpha you discover: close everything, keep the signals proprietary." [Source: posts-2026-05-18.docx — Post 1, @zostaff]

> "Profitable bots trade market microstructure: repricing delays, order book imbalance, arbitrage between Up and Down, lag between 5 minute and 15 minute contracts, and the final seconds before resolution." [Source: posts-2026-05-18.docx — Post 2, @RetroValix]

> "Hedge funds don't care who wins an election... They treat prediction markets as a network of fragmented order books. They exploit mathematical cointegration and order flow imbalances to trade the spread between platforms, delta-hedging their inventory to zero." [Source: posts-2026-05-18.docx — Post 4, @ridark_eth]

> "After completing a complex task (roughly 5+ tool calls), Hermes automatically creates a 'skill' — a structured markdown file that captures the procedure, known pitfalls, and verification steps." [Source: posts-2026-05-18.docx — Post 5, @0xMovez]

> "Your paper trading must hit all three before you go live: at least 200 completed paper trades, paper win rate above 75%, at least 7 consecutive days of running without crashes." [Source: posts-2026-05-18.docx — Post 6, @adiix_official]

> "Polymarket is not available to US residents. If you're in the US, you cannot legally access the platform." [Source: posts-2026-05-18.docx — Post 6, @adiix_official] — corroborates the Cemini geo-routing work.

- **Cross-wiki routing** (2026-05-18): Post 3 (@timbidefi UGC 3-platform monetization loop) is off-topic for OSINT/financial research — creator marketing and social-media operations. Routed to **seo-wiki** as a brief via `scripts/cross_wiki_route.py`. No OSINT wiki page created for it.
