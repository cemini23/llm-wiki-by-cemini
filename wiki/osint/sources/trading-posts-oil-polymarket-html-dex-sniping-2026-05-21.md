---
title: "Trading posts compilation — 50-repos AI cashflow, Oil-on-Polymarket settlement mechanics, HTML-as-Claude-output, +$50M DEX sniping history (May 2026)"
type: source
tags: [source, trading-posts, social-media, prediction-markets, polymarket, cme-settlement, dex-sniping, mev, html-output, claude-code, k55-2]
keywords: [ridark-eth, crpt-atlas, trq212, thariq, cbb0fe, oil-polymarket, cme-settlement-price, active-month-roll, mempool-sniping, uniswap-sniping, bsc-sniping, anti-snipe-measures, html-effectiveness, 50-github-repos-2026]
related:
  - sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md
  - sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md
  - concepts/cme-settlement-mechanics-for-prediction-markets.md
  - concepts/dex-mempool-sniping-2020-2021.md
  - concepts/polymarket-bot-architecture.md
  - concepts/perps-dex-funding-carry-strategy.md
  - entities/people/morpphhhaw.md
  - entities/people/ridark-eth.md
  - entities/people/crpt-atlas.md
  - entities/people/thariq-trq212.md
  - entities/people/cbb0fe.md
  - entities/platforms/polymarket.md
maturity: validated
read_status: deep-read
created: 2026-05-21
updated: 2026-05-21
clusters: [quant-finance, polymarket, mev]
---

## Relations

- @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — Post 1 (@morpphhhaw) is a near-duplicate of that earlier source's Post 1; refer there for canonical content. **This source covers Posts 2-5 only.**
- @sources/tool-eval-50urls-polymarket-kalshi-license-false-negative-2026-05-21.md — companion K55-2 batch (Gemini DR tool eval); @ridark_eth's 50-repo list partially overlaps the tool eval's URL set
- @concepts/cme-settlement-mechanics-for-prediction-markets.md — synthesized from Post 3 (@crptAtlas)
- @concepts/dex-mempool-sniping-2020-2021.md — synthesized from Post 5 (@Cbb0fe)
- @concepts/polymarket-bot-architecture.md — Post 3 sharpens the bot-architecture page with explicit settlement-mechanics requirements
- @concepts/perps-dex-funding-carry-strategy.md — Post 1 (duplicate ref only; canonical synthesis lives there)
- @entities/people/morpphhhaw.md — Post 1 author (duplicate)
- @entities/people/ridark-eth.md — Post 2 author (NEW)
- @entities/people/crpt-atlas.md — Post 3 author (NEW)
- @entities/people/thariq-trq212.md — Post 4 author (NEW); content cross-routed to ccc-wiki
- @entities/people/cbb0fe.md — Post 5 author (NEW)

## Raw Concept

- **Title**: `Post.docx` — second compilation of trader/builder social posts (delivered 2026-05-21)
- **Type**: social-media long-form posts (Twitter/X creators) + 1 Anthropic-blog-published essay
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/trading-posts-2026-05-21.docx`
- **Retrieved**: 2026-05-21 (dropped into `research to be indexed/`)
- **Contents**: 5 posts — (1) @morpphhhaw perps funding-carry bot **[DUPLICATE — see prior source]**; (2) @ridark_eth 50 GitHub repos for AI cashflow 2026; (3) @crptAtlas Oil-on-Polymarket CME settlement mechanics; (4) @trq212 / Thariq "The Unreasonable Effectiveness of HTML" with Claude Code; (5) @Cbb0fe +$50M sniping shitcoins on DEXs 2020-2021.

## Narrative

### Post 1 — @morpphhhaw: "Building a Perps DEX Trading Bot…" — **DUPLICATE**

Word-for-word duplicate of Post 1 from @sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md. Same 4-position test (Net PnL +0.059237 USDC, Funding PnL +0.057067 USDC, ~18.9% APR). Same Telegram funnel (`t.me/morph_tg`). No new content. See canonical source.

### Post 2 — @ridark_eth: "50 GitHub Repos Save Thousands AI Cashflow 2026"

Curated list of 50 GitHub repos organized into 4 buckets, framed as "stop paying for ChatGPT/Claude/Midjourney/ElevenLabs/Cursor, start running these locally and launching micro-SaaS". Each entry: `owner/repo` + 1-2 line benefit + occasional ⚠️ Crucial Note (archived, ToS-violating, etc.).

**Bucket breakdown:**

| Bucket | Range | Repos | OSINT relevance |
|--------|-------|-------|------------------|
| Income / Traffic / Lead Gen | 1-15 | Job-applier bots, video automation, Asian-market arbitrage, **algo trading (11-15)** | 11-15 directly relevant: AlphaGPT (factor analysis), TradingAgents, **nautilus_trader** (event-driven backtest framework), go-stock, ai-goofish-monitor (product arb). #46 OpenStock (market-data API alternative) is also financial. |
| Cost Reduction / Local Inference | 16-35 | LLM routers (rtk-ai/rtk, ClawRouter), gpt4free, repomix, unsloth, flux, faster-whisper, ubicloud, firecrawl, crawl4ai, docling | Marginal financial relevance. Heavy CCC overlap (n8n-mcp, OpenHands, ida-pro-mcp) → ccc-wiki brief. |
| Vibe Coding / Micro-SaaS | 36-48 | n8n-mcp, OpenHands, SaaS-Boilerplate, ida-pro-mcp, akaunting, faveo-helpdesk, laracom, **OpenStock**, anything-llm | OpenStock is financial; ida-pro-mcp is cybersec; rest is SEO/SMB. |
| Learning | 49-50 | llm-twin-course, DevOps-Roadmap | No direct OSINT relevance. |

**OSINT-relevant repos** (subset worth follow-up Phase-0 audits):

| # | Repo | Why |
|---|------|-----|
| 11 | `imbue-bit/AlphaGPT` | Symbolic-regression factor analysis (stock+crypto); compete with @entities/tools/k48-rl-toolkit cluster |
| 12 | `TauricResearch/TradingAgents` | Multi-agent AI trading — orchestrator-style; compete with Cemini's @concepts/conductor-orchestrator.md |
| 13 | `nautechsystems/nautilus_trader` | **High-priority audit candidate** — event-driven backtest engine, Rust+Python, "real-time and precise backtesting"; potential replacement/complement for any existing Cemini backtest layer |
| 14 | `ArvinLovegood/go-stock` | Local AI stock analysis (US/HK); marginal — duplicates existing Cemini ticker workflow |
| 46 | `Open-Dev-Society/OpenStock` | Direct market-data API alternative — Phase-0 audit if Cemini needs to reduce paid-API spend |

**Cross-wiki-relevant repos** (briefs staged per K55 routing decisions):

- **CCC-wiki brief** (`../projects/Cemini claude code CCC/briefs/2026-05-21_k55-ridark-eth-ccc-relevant-repos.md`): #2 claude-code-tips, #16-20 (rtk-ai/rtk, ClawRouter, gpt4free, quota watchers, **repomix**), #21 unsloth, #36 n8n-mcp, #38 OpenHands, #41 ida-pro-mcp, #47 anything-llm.
- **Image-gen-wiki brief**: #7 PersonaLive (24/7 AI-avatar streams), #22 flux + VAR (local image gen), #24 Qwen3-TTS + VoxCPM (voice cloning).
- **SEO-wiki brief**: #40 SaaS-Boilerplate, #43 akaunting, #44 faveo-helpdesk, #45 laracom, #48 astron-rpa.

**Provenance caveat**: This is a creator-marketing post. Entries are **not Phase-0 audited** at the source. Treat as a **candidate-list filter** for future evaluations, not a recommendation. Several entries carry explicit ⚠️ flags from the post author (ToS violations, archived repos, "educational purposes only" disclaimers).

### Post 3 — @crptAtlas: "How I made more than Wall Street brokers by trading Oil on Polymarket"

The **highest-signal post in this batch** for prediction-market mechanics. Synthesizes professional understanding of **CME settlement** vs naive retail "watch the chart" trading on Polymarket oil markets. → fully synthesized into `@concepts/cme-settlement-mechanics-for-prediction-markets.md`.

**Core insights** (verifiable from CME/Polymarket public rules):

1. **Settlement Trap**: Most Polymarket oil markets resolve on the official CME **settlement price** — a volume-weighted calculation of trades near the close used by banks to mark portfolios. *Not* the last trade of the day. *Not* the intraday chart. Intraday spikes can be irrelevant.
   - Example: oil spikes to $100.05 at 10:00 AM after a geopolitical headline; CME settlement closes at $99.98 → market resolves NO. Retail buys the spike; institutions trade the closing consensus.

2. **High-vs-Settlement market types**: Two distinct resolution rules with opposite volatility profiles:
   - **Daily High**: resolves YES if CME daily-high exceeds strike. Volatility is helpful — one spike above the level is enough.
   - **Settlement**: resolves YES if CME settlement price closes ≥ strike. Volatility is dangerous — price can spike far above the level intraday and still settle below.
   - Reading which rule applies before entering is the single most important pre-trade discipline.

3. **Real-money illustration**: One trader held "Will Crude Oil hit $100 by end of March?" Oil briefly touched **$119**; unrealized PnL hit **$115,559**. After Trump comments reduced escalation fears, oil pulled back; **settlement closed at $94.77**; unrealized profit dropped to **$72,925**. **$42,634 vanished purely on settlement mechanics**.

4. **Active Month Trap**: Polymarket uses the CME **Active Month** (front-month contract). The **roll happens 2 business days before expiration**. After the roll, Polymarket switches to the next contract — which can trade at a different price. Sudden market jumps are often the roll, not news. Institutional traders expect this; retail panics.

5. **Geopolitics: Event vs Expectation**: Prediction markets price probabilities, not events. By headline-time, markets have priced in the expectation. Professionals watch **cross-asset correlations**:
   - **Supply shock**: oil spikes while gold + DXY remain flat → temporary
   - **Macro regime shift**: oil + gold rise + dollar weakens → structural fear
   - One question: *fundamentals shift, or liquidity spike from retail?*

6. **Wall Street risk management** (the author's prescriptive checklist):
   - Bookmark the CME settlement page; treat that price as authoritative
   - Scale out (e.g. sell partial at 70¢ after entry at 20¢ before settlement)
   - Watch trading calendars (CME doesn't publish settlement on weekends/holidays — Saturday news cannot move official settlement until Monday)

**Cemini relevance**: directly applies to any Polymarket bot targeting commodity markets. The existing `@concepts/polymarket-bot-architecture.md` does not currently encode settlement-mechanics constraints; this post is the trigger to add them. → new concept page + update to bot architecture concept.

### Post 4 — @trq212 (Thariq): "Using Claude Code: The Unreasonable Effectiveness of HTML"

**Cross-wiki content** — Anthropic engineer Thariq's essay (also published on the official Claude Blog) arguing **HTML beats Markdown as Claude Code's default output format**. Out-of-scope for OSINT financial research; full concept page created at `@ccc-wiki/concepts/html-as-claude-code-output-format.md`.

**One-line summary for OSINT context**: As HTML-rendered Claude Code reports become standard for engineering work (PR reviews, spec docs, design exploration), Cemini's CeminiSuite briefs and `briefs/` outputs may benefit from the same shift — particularly for distribution-to-claude.ai consumption where HTML renders inline. Out-of-scope to act on now; flagged as a future authoring-format consideration.

**Referenced URLs**:
- `https://thariqs.github.io/html-effectiveness` (examples gallery)
- `https://thariqs.github.io/html-effectiveness/` (canonical w/ trailing slash)
- `https://x.com/trq212/status/2017024445244924382` (playgrounds post — two-way interactive HTML)

### Post 5 — @Cbb0fe: "How We Made +$50M Sniping Shitcoins On DEXs"

Two-brother first-person narrative of **Uniswap+BSC mempool-sniping operation, August 2020 – mid-2021**. Started with $40k portfolio and no Solidity knowledge; ended with +$50M from sniping +200 shitcoins across +10 chains. → synthesized into `@concepts/dex-mempool-sniping-2020-2021.md`.

**Operational arc**:

| Phase | Date range | Notable mechanics |
|-------|-----------|-------------------|
| Naive snipes | Aug 2020 | Watch Add-Liquidity tx hit chain, then buy → 1 block late. $YMPL +60 ETH, $VIDYA +159 ETH, $POLS 6-figs |
| Mempool sniping | Sep 2020 | Watch **pending mempool** for Add-Liquidity tx → submit buy at same gas, same block. $CHADS +675 ETH, $FRONTIER +800 ETH, $LINA, $CHARTEX |
| Smart-contract innovation | Late 2020 | Custom contract: "for 1 ETH, buy as many tokens as possible up to limit Y". Works regardless of liquidity pair (ETH/USDT/USDC). |
| AWS region optimization | Oct 2020 | Compete same-tx across multiple AWS regions; **North Virginia consistently wins** because MetaMask routes via Infura, Infura sits in NoVA. |
| Polkastarter era | Dec 2020 - Feb 2021 | UI-side buy limits bypassable via direct contract calls. SpiderDAO: bought 50% of sale + sniped listing → +$500K. |
| Anti-snipe arms race | Feb 2021 | Teams add buy-limit-per-tx → counter with **loop contract** (one tx, repeated buy-limit purchases). Buy-limit-per-wallet → counter with **"slave" contracts** (main contract spawns N sub-contracts, each below the wallet limit). |
| BSC explosion | Feb-May 2021 | Different from ETH: BSC orders transactions **randomly within a block**. Counter: **150-200 nodes globally, each sending 10 txs** in parallel. AWS bill **$40-60K/month**. $MATTER +2000 BNB, $KPAD +8300 BNB ($2M in 1 hour), $COOK +3000 BNB. |
| "Suicide snipe" | Spring 2021 | One unlimited-buy-limit tx + auto-sell 4 blocks later → catches everyone sniping after. +50-150 ETH per use. |
| Same-tx list + buy | May 2021 | BSC launchpads allow public listing-tx execution → custom contract that **lists and buys in same atomic tx**. First-mover advantage for ~1 week. |
| $EVN whitelist accident | Aug 2021 | Blacklisted wallets randomly whitelisted; dumped $1M+ supply per wallet across 20+ wallets in 15 minutes → **+$6M out of nowhere**. |

**Key learnings encoded for Cemini's MEV/DEX concept layer**:

- **Mempool monitoring** is the foundational primitive — public mempool visible to anyone running an Ethereum node, but speed-to-block-inclusion is the actual edge.
- **Geographic / infrastructure latency** is a first-class strategic variable (NoVA for ETH mempool, Frankfurt/Tokyo as backups, dedicated $40-60K/mo AWS infra at scale).
- **Smart-contract innovation as edge** — at every anti-snipe iteration, the response was a new contract pattern (loop, slave contracts, list-and-buy atomic).
- **"Anti-snipe is good for us"**: every team-side defense creates a moat for snipers willing to engineer past it. Sophistication compounds.
- **The end-of-era signal** is exhaustion + market saturation, not regulatory action. By mid-2021, the operators had been running 6 snipes/day with no time to live; they secured profits and exited.

**Cemini relevance**: The narrative is **2020-2021 historical**, not a current strategy. Mempool sniping at this magnitude is largely a closed window (private mempools, Flashbots, MEV-share, etc.). But the **operational lessons** — geographic infrastructure, smart-contract iteration cycle, anti-defense as opportunity — generalize to any MEV / DEX-adjacent strategy Cemini might explore. Concept page records the history; **does not** trigger a Cemini build action.

### Caveats

- **Post 1 (@morpphhhaw) is a duplicate** — same content was ingested in K55-1 (`@sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md`). The Telegram channel (`t.me/morph_tg`) appears to recycle the same long-form post across distributions.
- **Post 2 (@ridark_eth)** is creator-marketing content with affiliate framing ("stop paying for AI subs, start running micro-SaaS"). The 50-repo list is **unaudited** — entries include ToS-violating tools (mass job-applying, gpt4free) and archived repos. Use as **candidate list**, not endorsement.
- **Post 3 (@crptAtlas)** PnL number ($115K → $72.9K example) is **uncited** — no trader handle, no on-chain reference. Treat the mechanics as well-documented (CME settlement is public knowledge), the specific dollar example as illustrative.
- **Post 4 (@trq212)** is Anthropic-engineer first-party content — high credibility but reflects one engineer's preference, not Anthropic product position. Marked `validated` because the Claude Blog publication adds independent corroboration.
- **Post 5 (@Cbb0fe)** is self-published memoir; PnL claims are **not independently verifiable**. The mechanics are corroborated by the broader 2020-2021 MEV literature (Flashbots research, Daian et al. "Flash Boys 2.0"). Treat individual ETH/BNB figures as `[TENTATIVE]`; treat architecture descriptions as `[CONFIRMED]` against the public MEV record.

## Snippets

### Post 3 — @crptAtlas

> "Most oil markets on Polymarket resolve using the official CME settlement price. This is not simply the last trade of the day. It is a volume-weighted calculation of trades near the close, used by banks and clearinghouses to mark portfolios. That means intraday spikes often do not matter." [Source: Post.docx — @crptAtlas]

> "During a recent oil spike tied to Middle East tensions, one trader held a large position in: 'Will Crude Oil hit $100 by end of March?' At the peak of the rally, oil briefly touched $119. His unrealized PnL showed $115,559 profit. But the market used settlement price, not intraday highs. After political comments from Donald Trump reduced escalation fears, oil pulled back. The official settlement finished at $94.77. His unrealized profit dropped to $72,925. Still profitable, but $42,634 vanished purely because settlement mechanics matter." [Source: Post.docx — @crptAtlas]

> "Polymarket uses the CME Active Month, also called the front-month contract. The key rule: The active month rolls two business days before expiration. When the roll happens, Polymarket switches to the next contract. If the next month trades at a different price, the market can suddenly jump." [Source: Post.docx — @crptAtlas]

### Post 4 — @trq212 (Thariq)

> "I've started preferring HTML as an output format instead of Markdown and increasingly see this being used by others on the Claude Code team … The chance of someone actually reading your spec, report or PR writeup is much much higher if it's in HTML." [Source: Post.docx — @trq212; published on Claude Blog]

> "HTML can take 2-4x longer than Markdown, but I've found the results are worth it." [Source: Post.docx — @trq212]

### Post 5 — @Cbb0fe

> "After some research, we realize that with an Ethereum node we can monitor the public mempool to see pending transactions before they hit the chain. Starting from September, this is how sniping works for us: Watch the mempool for a pending Add Liquidity TX. Immediately send a buy TX with the same gas price. Aim to be included in the same block right after the liquidity add." [Source: Post.docx — @Cbb0fe]

> "It quickly becomes clear that nodes hosted in North Virginia are consistently faster. This leads us to believe that North Virginia is the best place to run our sniping servers. After conducting further research, our assumptions are confirmed: At the time, nearly all users are transacting through MetaMask, which route every Add Liquidity transaction via Infura's public RPC endpoint and Infura's servers are located in North Virginia." [Source: Post.docx — @Cbb0fe]

> "We setup 10 nodes on AWS all around the world and each node sends 50 txs trying to snipe a random test transaction … For the next snipes, we build an infrastructure of 150-200 nodes on BSC. Every node sends 10 transactions. The AWS invoices to run such infrastructure are between $40k and $60k monthly." [Source: Post.docx — @Cbb0fe]

> "In total, we sniped +200 shitcoins on +10 different chains." [Source: Post.docx — @Cbb0fe]
