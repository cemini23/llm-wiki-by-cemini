---
title: "Trading posts compilation — Perps funding-carry bot, Polymarket LP-rewards $POLY airdrop farming, sports-consensus agent, weather-trader top-7, prediction-market Python algo, Shopify-Claude (May 2026)"
type: source
tags: [source, trading-posts, social-media, perps-funding-carry, polymarket-lp-rewards, poly-airdrop, sports-consensus-agent, weather-traders, prediction-market-algo, k55]
keywords: [morpphhhaw, matiasscalbi, zostaff, stacyonchain, polymarketsuccubus, gippp69, perps-dex-funding-carry, market-neutral-funding-bot, polymarket-liquidity-provision, lp-rewards-farming, poly-airdrop, time-weighted-open-interest, sports-consensus-firecrawl, coldmath, clawdbot, parity-polymarket, prediction-market-python-momentum-value-risk, shopify-claude-ecommerce]
related:
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/perps-dex-funding-carry-strategy.md
  - concepts/sports-prediction-consensus-agent.md
  - concepts/polymarket-weather-trading-strategy.md
  - concepts/polymarket-bot-architecture.md
  - concepts/ai-assisted-trading-workflow.md
  - entities/people/matias-scalbi.md
  - entities/people/morpphhhaw.md
  - entities/people/stacyonchain.md
  - entities/people/polymarketsuccubus.md
  - entities/tools/clawdbot.md
  - entities/tools/parity-polymarket-analytics.md
  - entities/tools/firecrawl.md
  - entities/platforms/polymarket.md
  - entities/tools/centpro.md
  - concepts/polymarket-lp-bot-phase0-spec.md
  - sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md

maturity: validated
read_status: deep-read
created: 2026-05-20
updated: 2026-05-20
clusters: [quant-finance, polymarket]
---

## Relations
- @seo-wiki/briefs/2026-05-20_2026-05-20_k55-shopify-with-claude-5-methods.md  (cross-wiki brief)

- @concepts/polymarket-lp-rewards-farming.md — synthesized from Post 2 (@MatiasScalbi LP-rewards + $POLY airdrop thesis)
- @concepts/perps-dex-funding-carry-strategy.md — synthesized from Post 1 (@morpphhhaw market-neutral funding-carry bot)
- @concepts/sports-prediction-consensus-agent.md — synthesized from Post 4 (@stacyonchain Firecrawl + Claude consensus agent)
- @concepts/polymarket-weather-trading-strategy.md — updated with Post 5 (@polysuccubus Top-7 weather traders + ColdMath/Clawdbot)
- @concepts/polymarket-bot-architecture.md — corroborated by Post 1 + Post 2 (operator-tactical layer for LP bots)
- @concepts/ai-assisted-trading-workflow.md — Post 4 extends the AI-assisted workflow into a research/consensus agent
- @entities/people/matias-scalbi.md — author of Post 2 (and Post 4 of Posts-2)
- @entities/people/morpphhhaw.md — author of Post 1
- @entities/people/stacyonchain.md — author of Post 4
- @entities/people/polymarketsuccubus.md — author of Post 5
- @entities/tools/clawdbot.md — Claude-powered AI agent framework, used by ColdMath (#1 weather trader)
- @entities/tools/parity-polymarket-analytics.md — counterparty-intelligence + orderbook insights platform behind the @polysuccubus rankings
- @entities/tools/firecrawl.md — JS-rendering scraper used by the @stacyonchain sports-consensus agent

## Raw Concept

- **Title**: `Posts.docx` — compilation of six trader social-media posts/articles
- **Type**: social-media long-form posts (Twitter/X creators)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/posts-lp-rewards-perps-funding-2026-05-20.docx`
- **Retrieved**: 2026-05-20 (dropped into `research to be indexed/`)
- **Contents**: 6 posts — (1) @morpphhhaw perps DEX market-neutral funding-carry bot; (2) @MatiasScalbi Polymarket LP-rewards farming + $POLY airdrop guide (Spanish); (3) @zostaff Python algo trading on prediction markets — momentum, value, risk, backtest; (4) @stacyonchain Claude agent for sports prediction (Firecrawl + 5-source consensus); (5) @polysuccubus Top-7 most-profitable weather traders on Polymarket; (6) @gippp69 Shopify-Claude e-commerce methods (off-topic for OSINT — routed to seo-wiki as a brief).

## Narrative

### Post 1 — @morpphhhaw: "Building a Perps DEX Trading Bot — From Funding Noise to a Semi-Automated Market-Neutral Strategy"

A perpetual-futures **funding carry** bot. The thesis: even when price does not move, a perp position pays or receives funding to keep contract price close to spot; for **automated** strategies, funding is the main signal, not directional price.

**Strategy** ("volatility-adjusted funding carry"): for each candidate market, rank by funding spread between two venues; penalize regimes that appear and disappear within minutes (stability filter); ignore thin books (liquidity + min-size filter); enforce position symmetry between long + short legs (hedge integrity); only rotate when the new opportunity is meaningfully better (rotation threshold). The result behaves "less like a high-frequency arb bot and more like a slow allocator between funding regimes."

**Infrastructure-first build**: before strategy, the bot needed reliable handling of balances, positions, market/asset alias mappings, leverage settings, min order sizes, funding data, live execution, **emergency position flattening**, local state, and post-trade reporting. Quote: *"A trading bot with a clever strategy and weak execution is just a complicated way to lose money."*

**Safety gates**: explicit live-confirmation phrase before real orders; reduce-only close commands; leverage cap; min balance + min hold period; local DB of active positions; event log per allocator cycle; emergency-flatten command. The dominant failure mode: **one leg opens, the other doesn't** → the strategy is no longer market-neutral, it's a naked directional position. Execution errors are treated as **first-class events** requiring reconciliation.

**Early live test results** (small dollar size; goal was capturing the *composition* of PnL, not the absolute):
```
Closed positions: 4
Net PnL: +0.059237 USDC
Funding PnL: +0.057067 USDC      ← ~96% of net
Price PnL:   +0.002170 USDC
Return on quote size: ~0.0370%
Approx. annualized run-rate: ~18.9% APR
```
The point of the run was that **funding PnL dominated price PnL** — the strategy is capturing funding as intended, not getting lucky on basis. Annualized 19% is treated as a **point estimate from a small sample**, explicitly not a stable expected return.

**Failure-mode log** from the test: positions with positive funding still closed negative when price/basis movement outweighed funding; API session token expired mid-loop and broke read/order paths; some on-exchange positions appeared in raw fetch but weren't picked up by the normal close command → had to add an explicit reduce-only close-by-symbol+size command.

### Post 2 — @MatiasScalbi: "Polymarket va a lanzar su cripto — cómo llegar al Top 10% y prepararte para el airdrop"

The **liquidity-provision-as-airdrop-farming** thesis on Polymarket — the centerpiece of this batch. → synthesized into `@concepts/polymarket-lp-rewards-farming.md`.

**Author claim**: two accounts in the Top of Polymarket — manual at Top 2.8%, bot at Top 6.8% — both generating LP rewards daily, both from zero, in 6 days. Built with Claude Code + Antigravity ("3 months ago I didn't know how to write a line of code"). [TENTATIVE — single source, screenshots only.]

**Core mechanics** (verifiable from `docs.polymarket.com` and existing wiki):
- Polymarket has two roles: **bet** (buy YES/NO and hope for resolution) vs **provide liquidity** (post YES + NO limit orders near the midpoint). LPs earn rewards in USDC paid daily from a published pool; the post's argument is that the rewards alone justify the position regardless of any airdrop.
- **$15.86M** total LP-rewards distributed historically; Top-10% barrier is **~$48** accumulated, Top-1% is ~$1,576. Both are within reach of small capital in 1-2 weeks of consistent placement.
- **April 2026 sports liquidity incentive**: $5M+ for sports markets alone (announced by @mustafap0ly). Per-match payouts: Champions League up to $24K/match, Premier League $10K, Liga Argentina $550 — split among LPs by participation share.
- **Reward mechanics**: orders close to midpoint score higher; one-sided liquidity is divided by 3 (penalty); $1/day minimum to claim that day's reward. **Time-Weighted Open Interest** — holding a position 72h+ activates a points multiplier.

**Airdrop thesis** (the speculative-but-plausible layer):
- Shayne Coplan (founder) tweet 2025-10-08 listing `$BTC $ETH $BNB $SOL $POLY 🤔` next to the four largest cryptos. Mustafa (Polymarket team) tweet 2026-02-11: "1m markets and $POLY next." Matthew Modabber (CMO) on Degenz Live podcast: confirmed token + airdrop coming, post US-relaunch.
- **NYSE / ICE investment**: 2025-10-07 announcement of $2B strategic investment by Intercontinental Exchange at $9B post-money valuation. Polymarket is #4 daily-revenue project in crypto: $1.95M/day, $7.55M/30d.
- **CFTC**: 2022 settlement ($1.4M fine, US users blocked); November 2025 approved as a regulated exchange. State-level restrictions persist (France, Belgium, Switzerland blocked).
- Independent estimator (community-built airdrop checker): one of the author's accounts → 1,754 $POLY × 1.20× multiplier ≈ **$35,080 at $20B FDV**. **[TENTATIVE]** — unofficial estimator, no published criteria, no snapshot date, FDV is a guess. **The rewards are concrete; the airdrop is upside.**

**Risk register** (the author's own):
- Phishing pages claim "$POLY token claim" — no claim mechanism exists, do not click.
- Airdrop date, criteria, snapshot all unannounced.
- Thin markets with deep one-side fills can take real losses; gas market expired while sleeping → -$200 loss recorded.
- VPN/IP geofencing — Polymarket blocks datacenter ranges; sudden policy change could lock out non-US users without notice.

**Cemini relevance**: directly inverts the existing Cemini Polymarket build orientation, which has so far been **directional/bot-taker** (@0x_Punisher playbook, @AlterEgo_eth weather bot, @adiix_official latency arb). LP-rewards farming is a **maker** strategy with a fundamentally different risk/reward profile — the edge is in fee capture + LP scoring algorithm, not in directional prediction. Calls for its own concept page + cemini-prod brief.

### Post 3 — @zostaff: "Alpha on Prediction Markets — Momentum, Value, Risk. The Complete Python Guide."

A Python educational walkthrough of algo trading concepts applied to prediction markets:
- **Data + returns**: load market price history (Polymarket Gamma API); compute simple returns + log returns; explain why log returns are necessary (-50% then +100% on simple returns says "+25%" but you're at zero).
- **Momentum**: 7/14/30-day rolling momentum across contracts; flag those gaining on all three.
- **Value**: compute your own probability estimate, compare to market price, define edge = my_est − market_price.
- **Risk metrics**: annualized return, vol, Sharpe (>1 worth it, >2 excellent), max drawdown.
- **Correlation**: cross-contract correlation matrix — < 0.3 is good for portfolio, > 0.7 means no diversification.
- **Backtest**: simple momentum class (buy if 14-day pct_change > 0, hold otherwise); cumulative_strat vs cumulative_hold.

**Verdict**: standard quant introduction adapted to binary contracts; nothing novel. Use as a teaching reference; folded into the broader `@concepts/quant-finance.md` cluster but does not warrant its own concept page.

### Post 4 — @stacyonchain: "How to Build a Claude Agent for Sport Predictions"

**Consensus-as-signal** architecture for sports betting on Polymarket. The agent's job is to find consensus automatically across multiple sports-analytics platforms, score how strong and aligned that consensus is, and flag only entries where it crosses an actionable threshold. → synthesized into `@concepts/sports-prediction-consensus-agent.md`.

**4-step build**:
1. **Data layer (Firecrawl)**: scrape pre-match analysis from a curated, tier-weighted source list (Tier-1: WhoScored, FBref, Understat, OptaAnalytics; Tier-2: SofaScore). Trim content to 2,000 chars per article for token efficiency.
2. **Signal extraction (Claude Sonnet 4.5)**: per-article prompt extracts favored team, expressed confidence (0-1), primary factors (max 3), risk factors, stated probability (or null). **Critical constraint**: "Do not add your own analysis. Extract only what is written." Output JSON.
3. **Consensus synthesis**: per-match prompt synthesizes N individual signals into `{consensus_team, consensus_strength, weighted_probability, source_count, dissenting_count, shared_risks, signal_quality}`. Signal-quality rules: `strong` requires strength ≥ 0.72 + ≥5 sources + ≤1 dissent.
4. **Entry sizing (Kelly)**: edge gate at 7pp between agent probability and Polymarket price; Kelly fraction × strategy-conservatism multiplier (0.20 for strong, 0.12 for moderate); **6% hard cap per position** regardless of Kelly output.

**Author's headline findings**:
- Strong consensus signals (strength ≥ 0.72, ≥6 sources) appear on **~15-20%** of analyzed matches. The remaining 80-85% are weak consensus or disagreement → filter, don't enter.
- **Consensus strength predicts better than consensus direction** — 6 sources at 0.78 strength favoring the underdog outperforms 4 sources at 0.61 strength favoring the favorite.
- Limitation: the agent works on *publicly published* analysis only. It is a **systematic research layer**, not an information-edge advantage over participants with insider data.
- Cost: <$30/month in API + scraping credits for the entire system.

**Promotion caveat**: post promotes `centpro.bot` — see Post 4 of the K55 multi-wiki tool eval, CentPRO is **closed-source Windows binary** sold via Telegram at $49/mo. The architecture in this post is the open recipe; CentPRO is the gated commercial implementation. The recipe is useful regardless. → bot itself flagged as Reject in `@entities/tools/centpro.md`.

### Post 5 — @polysuccubus: "Top 7 Most Profitable Weather Market Traders on Polymarket"

A ranking of weather-market specialists, presented via **Parity** (parity.io-style counterparty-intel platform — affiliate funnel for the post). Updates the existing weather-trading concept page with operator-level evidence of who actually makes money on the strategy.

**The Top 7** (PnL, win-rate, biggest single win, n predictions):

| # | Handle | PnL | WR | Largest single win | Specialty |
|---|---|---|---|---|---|
| 1 | **ColdMath** | +$124,896 | 81.7% | $12,400 (1,941 trades) | **Bot on Clawdbot framework**; pilot aviation reports as feed; entries at 0.01-0.02¢ |
| 2 | VibeTrader | +$132,854 | 37.7% | $21.3K (5,114 trades) | NYC/Miami daily-high + Musk-tweet-count |
| 3 | BeefSlayer | +$62,064 | 68.2% | $4,103 (1,585 trades) | US city daily-highs (Seattle, Atlanta, NYC, Chicago, Austin) |
| 4 | HenryTheAtmoPhD | +$55,838 | 36.5% | $4,944 (3,472 trades) | Retired atmospheric-science professor; Seoul/NYC/London |
| 5 | HondaCivic | +$55,408 | 84.2% | $15,144 (3,828 trades) | City-specific precision entries; HK/NYC/London/BA/Seoul |
| 6 | russell110320 | +$43,936 | 64.3% | $10,300 (150 trades) | Global temperature anomaly + "Nth hottest on record" markets |
| 7 | Maskache2 | +$34,106 | 33.5% | $7,638 (1,941 trades) | Seoul/HK/Wellington/NYC daily-highs |

**Key observation**: the #1 and #5 traders run very different patterns — ColdMath at 81.7% via automation buying 0.01-0.02¢ deep-OOM contracts, HondaCivic at 84.2% via patient manual entries at very low prices. **Low entry price is the dominant feature** across both — buying the tails when the market mis-implies probability. Win-rate alone is uninformative without entry price (HenryTheAtmoPhD at 36.5% WR still cleared +$55K).

**Cemini relevance**: the existing weather-trading concept (`@concepts/polymarket-weather-trading-strategy.md` from K41) is now corroborated by **7 independent operator profiles** — confirms the strategy is real, scalable, and primarily an **execution-edge game** (data → entry-price discipline → patience) rather than a forecasting-edge game. ColdMath/Clawdbot warrants a new entity page.

### Post 6 — @gippp69: "$8,400 Last Month With Shopify — The 5 Claude Methods Nobody Is Talking About"

Shopify dropshipping store using Claude for 5 workflows: competitor autopsy, mining negative reviews, 5-email post-purchase sequence, UGC ad scripts, weekly Sunday diagnostic. Reported $8,400/mo revenue, $3,485 net profit (Month 3).

**Off-topic for OSINT financial research** → routed to seo-wiki as a brief (creator marketing / e-commerce ops / AI-assisted retail). Not folded into any OSINT concept page.

### Caveats

- All authors are **social-media creator content** with monetization layers (Telegram channels, affiliate links, paid products). Treat methodology as plausible and corroborated where multiple operators agree; treat specific PnL/win-rate numbers as `[TENTATIVE]` unless verifiable on-chain.
- Post 2's airdrop FDV math is openly speculative — the author is honest about it but it spreads.
- Post 4's promotion of CentPRO is a conflict-of-interest signal: the architecture described is the open recipe, the bot for sale is the gated implementation.
- Post 5's Parity links are an affiliate funnel; the trader profiles themselves are public on Polymarket and verifiable.

## Snippets

> "Most traders look at funding as a small operational detail. For automated strategies, though, funding can become the main signal." [Source: Posts.docx — Post 1, @morpphhhaw]

> "Polymarket no es un proyecto más por la escala que tiene. Esto no es un experimento. Estamos hablando de: más de 1.35 millones de traders activos, más de $3.6 billones de volumen solo en las elecciones de EEUU de 2024 ... Polymarket es hoy el proyecto #4 en revenue diario de todo crypto. $1.95M por día, $7.55M en 30 días." [Source: Posts.docx — Post 2, @MatiasScalbi]

> "Polymarket está regalando plata. Literalmente. ... Mustafa acaba de anunciar $5 millones de dólares en incentivos de liquidez solo para mercados de deportes en abril. Cinco millones. Para un solo mes. Para una sola categoría." [Source: Posts.docx — Post 2, @MatiasScalbi]

> "A single analyst saying 'Team A wins this 65-35' means relatively little. Five independent sources — different platforms, different methodologies, no financial relationship to each other — all converging on the same directional view? That's signal worth acting on." [Source: Posts.docx — Post 4, @stacyonchain]

> "The most useful thing I learned: consensus strength predicts better than consensus direction. Six sources aligned at 0.78 strength favoring the underdog outperforms four sources at 0.61 strength favoring the favorite." [Source: Posts.docx — Post 4, @stacyonchain]

> "Will the highest temperature in Hong Kong be 15°C or below? Invested: $37 → Payout: $15,182 → Profit +$15,144 +40,511% (his record single win)" [Source: Posts.docx — Post 5, @polysuccubus on HondaCivic — Polymarket trade]
