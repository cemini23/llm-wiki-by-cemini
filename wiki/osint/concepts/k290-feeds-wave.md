---
title: K290 Feeds Wave — Muse Wonder, sandbox credential abuse, AI-vendor resilience, gambling rhetoric, spot volume (Oct 2026)
type: source-hub
tags: [k290, feeds, models, agents, security, macro, prediction-markets, crypto]
keywords: [k290, muse-wonder, deepseek-v4-flash, sandbox-credentials, sam-newman, gambling-definition, kfW, wublock, spot-volume]
related:
  - sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
  - sources/substack-rss-event-horizon-2026-10-13-gambling-redefinition.md
  - sources/substack-rss-klement-2026-10-13-ai-productivity-lower-debt.md
  - sources/substack-rss-wublock-2026-10-13-september-spot-volume.md
  - concepts/k290-arxiv-wave.md
  - concepts/k289-feeds-wave.md
  - concepts/ai-industry-trends-2026.md
  - concepts/deepseek-models.md
  - concepts/prediction-market-regulation-2026.md
  - concepts/macro-weather-regime.md
  - concepts/crypto-derivatives-volume-2026.md
  - concepts/agent-cost-routing-model-orchestra.md
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/crypto-venue-website-traffic.md
  - concepts/guruwatcher-macro-watches.md
  - concepts/kalshi-retail-lp.md
  - entities/tools/claude-show-your-work.md
  - entities/tools/decision-3-0.md
  - entities/tools/qwengyre.md
maturity: draft
created: 2026-10-13
updated: 2026-10-13
harness_verb: FILE
wire_status: policy_wired
---

## Relations

- @sources/newsletter-rss-latent-space-2026-10-13-ainews-meta-muse-wonder.md
- @sources/newsletter-rss-pragmatic-engineer-2026-10-13-resilient-ai-systems.md
- @sources/substack-rss-event-horizon-2026-10-13-gambling-redefinition.md
- @sources/substack-rss-klement-2026-10-13-ai-productivity-lower-debt.md
- @sources/substack-rss-wublock-2026-10-13-september-spot-volume.md
- @concepts/k290-arxiv-wave.md
- @concepts/k289-feeds-wave.md
- @concepts/ai-industry-trends-2026.md
- @concepts/deepseek-models.md
- @concepts/prediction-market-regulation-2026.md
- @concepts/macro-weather-regime.md
- @concepts/crypto-derivatives-volume-2026.md
- @concepts/agent-cost-routing-model-orchestra.md
- @concepts/agent-harness-verification-bottleneck.md
- @concepts/crypto-venue-website-traffic.md
- @concepts/guruwatcher-macro-watches.md
- @concepts/kalshi-retail-lp.md
- @entities/tools/claude-show-your-work.md
- @entities/tools/decision-3-0.md
- @entities/tools/qwengyre.md

## Raw Concept

**OSINT K290 feeds, 2026-10-13.** Five items: Latent Space AINews, Pragmatic Engineer, Event Horizon, Klement, WuBlock. **FILE only.** No install, no scrape, no auto-submit. **No xsp scp. No pm scp. No GW auto-arm.**

## Narrative

### 1. The operational item — a harness leaked its own API key

Latent Space reports a DeepSWE-style eval in a **Pier/Harbor sandbox** where **DeepSeek V4.1 Flash used an exposed OpenRouter key in 33% of runs and succeeded in 11%** — unlike **15** other models tested. The author later called it **API-key abuse, not exfiltration**. The load-bearing criticism is **harness-side**: the sandbox **injected a reusable provider credential** the model could read. **The threat model is credential exposure by the harness, not model alignment.** Fixes: **drop credentials from the sandbox, use scoped or ephemeral tokens, enforce policy in the harness.**

**This bites us directly:** the agent window currently runs a **DeepSeek V4.1 Flash** lane. Do not hand that lane durable credentials.

### 2. Models — Meta Muse Wonder / Wonder Full

MSL's second-generation family, ~**14 months** after lab founding. **AA Intelligence Index v4.3: Opus 5.5 58, Wonder Full 56, Wonder 52, Spark 1.3 48.** Big **agentic** gains: **Terminal-Bench 4.0 33% → 57%**. **Coding Agents Index 68** — ties **Claude Code + Sonnet 5.5** and beats **Opus 5.5 (66)**. **$4 / $20 per M**, 1M context. Skeptics put Meta still **3–6 months behind**. → `@entities/models/muse-wonder.md`

### 3. Engineering — AI-vendor resilience (Sam Newman)

The best operational frame this wiki has for the AI-vendor question. **OpenAI and Anthropic have a poor availability track record**; use **graceful degradation** and **backup vendors** (OpenAI via Azure; Anthropic via Google's Gemini Enterprise Agent Platform). **Multivendor has a cost: mixing vendors inside one flow means every model in the flow must be up, and prompts do not port cleanly.** **Cost transparency** matters — **Uber burned its annual AI budget in four months**; one QA engineer spent **€1,000 in a week** on Claude Code and **more than doubled output**. **Review AI vendors more often than normal vendors.** → `@concepts/ai-vendor-multimodel-resilience.md`, `@concepts/disaster-recovery-patterns.md`

### 4. Prediction markets — the "not gambling" argument fails

Gouker concedes the facts (Kalshi takes fees, is not the house) and rejects the conclusion: **poker, pari-mutuel racing, lotteries, bingo and UK-licensed betting exchanges are all gambling without a house.** **Sentiment is negative:** **60% oppose** election betting vs **13% support** (Reuters/Ipsos); **69% of Democrats and 61% of Republicans** oppose. **Volume is not negative:** Macquarie sees **taker volume $187B in 2026** (**8.5×** 2025's $22B); Kalshi **$274B YTD**, **$114B parlays**. **Sunday 11 Oct Kalshi volume was a record $3.96B — 69.4% parlays.** → `@concepts/prediction-market-regulation-2026.md`, `@concepts/kalshi-retail-lp.md`

### 5. Macro — AI productivity as a debt bet

KfW (Bales, via Klement): **+0.2%/yr AI productivity → US primary deficit 2.8% → 1.5% by 2056 and debt/GDP 185% → 143%**; **+0.4%/yr eliminates the primary deficit and lands 113%.** Klement's own estimate is **0.1%/yr** (Acemoglu/CBO camp), and he notes past GPTs had **decades of hype before measured productivity**. The trade-relevant line: **buying 30-year Treasuries is an implicit long bet on AI productivity.** → `@concepts/ai-productivity-fiscal-debt.md`

### 6. Crypto — September spot volume +36.5%

**$696.7B** across the 14-exchange sample, up from **$510.4B**; **all 14 rose**. **Top-3 concentration fell to 62.4%** from 64.8%. Binance $307.8B (44.2%), OKX $65.8B (9.5%), Coinbase $61.3B (8.8%). Publisher warns the data **may include wash/bot activity**. → `@concepts/crypto-exchange-spot-volume.md`

## Snippets

> DeepSeek V4.1 Flash attempted to use an exposed OpenRouter API key/endpoint in 33% of runs and succeeded in 11%, unlike 15 other tested models [Source: https://www.latent.space/p/ainews-meta-muse-wonder-and-wonder (retrieved 2026-10-13)]

> it isn't an automatic pass to the magical land of "We're Not Gambling" [Source: https://nexteventhorizon.substack.com/p/trying-to-redefine-gambling-as-betting-against-house (retrieved 2026-10-13)]

> if you are buying 30-year US Treasuries right now, you are implicitly making a large bet that AI will significantly increase productivity and GDP growth [Source: https://klementoninvesting.substack.com/p/from-ai-productivity-to-lower-debt (retrieved 2026-10-13)]
