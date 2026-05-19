---
title: "AI-assisted discretionary trading workflow"
type: concept
tags: [concept, discretionary-trading, trading-process, journaling, trading-psychology, ai-assisted, k49]
keywords: [ai-trading-workflow, trader-morin, market-outlook, trade-journaling, confluence-scoring, trade-plan, position-sizing-why, post-trade-review, trading-psychology, prep-layer-ai]
related:
  - sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md
  - concepts/quant-finance.md
  - entities/tools/quantdinger.md
maturity: draft
created: 2026-05-16
updated: 2026-05-19
---

## Relations

- @sources/trading-posts-ai-workflow-polymarket-markov-2026-05.md — @TraderMorin post this page synthesizes
- @entities/tools/quantdinger.md — K54 tool eval; QuantDinger's multi-agent research engine is a software instance of this AI-assisted workflow
- @concepts/quant-finance.md — corpus-index parent cluster

## Raw Concept

Synthesized from the @TraderMorin post in `posts.docx` (May 2026): a 5-stage discretionary trading process where AI assists the *preparation and review* layers rather than generating signals. Captured because it is a clean structural template for a human-in-the-loop trading process — orthogonal to Cemini's automated stack but useful as a checklist contrast.

## Narrative

### Core thesis

**AI does not fix an unprofitable trader.** It does not "magically" correct mistakes. Its leverage is in *structuring* the workflow — preparation, journaling, and review — so the trader executes process instead of emotion. Emotions are constant even for experienced traders; the difference is acting on the plan, not the feeling.

### The 5-stage process

1. **Market Outlook** — establish context before any trade:
   - *Bias*: weekly bias (HTF-trend alignment) → daily bias (trend-continuation vs fade-the-range) → pro-trend/counter-trend checklist (favour highest-probability = pro-trend setups).
   - *Setups on radar*: log price + setup type (Mean Reversion, Range Extreme).
   - *High-impact data*: an "outlook sheet" wired to a macro-data tracker that surfaces the day's key events on load — avoid opening trades into a release.
   - *Key levels*: swing highs/lows, supply/demand zones.
   - *TPO / composites*: inefficiencies on TPO charts as secondary confluence and trade-location input (not a standalone strategy).

2. **Daily Focus List** — weekly/monthly goals defined by **weaknesses, not PnL** (e.g. "lock profits sooner instead of round-tripping" → weekly: "use TP limit orders, don't adjust TP after entry"). A daily task list aimed at being "1% better." Goals are only meaningful if trades are journaled.

3. **Trade Plan** — per-setup:
   - *Trade ID* + a "Checklist Completed" gate confirming the Market Outlook sheet was reviewed and the environment (Ranging/Trending) re-confirmed.
   - *Position sizing & risk* — every number carries a mandatory **"Why?"**; risk % scales with setup tier (an A* setup has higher expectancy → larger risk than a B/C setup).
   - *Trade confluences* — secondary confluences (divergences, EMAs, composites, single prints) determine A/B/C tier. Then **actively disconfirm**: look for reasons *not* to take the trade, which often demotes a perceived A* to a B.

4. **Trade Execution** — a moment-of-execution setup checklist (split into Mean Reversion / Range Extremity playbooks); tagged **execution patterns** (some cross-playbook, some specific) so journaling reveals which patterns are most profitable; scaled entries rather than single-clip full size.

5. **Trade Closure**:
   - *Emotion journaling across the lifecycle* — rarely-discussed; logging why you froze / deviated surfaces the root cause to fix.
   - *Post-trade review* — was the execution plan followed or deviated from, and why; what worked; which mistakes occurred and **at which lifecycle stage** (so improvement effort targets the failing stage — e.g. fine execution but greedy closure → round-tripping).

### Why it's in this wiki

Cemini's stack is automated; this is a *discretionary* process. It earns a page as:

- A **structural contrast** — the checklist gates, confluence tiering, disconfirmation step, and stage-localized error attribution are patterns that translate to designing automated-strategy guardrails and post-trade attribution.
- The **"AI assists prep/review, not signals"** framing is a useful boundary marker: AI-as-preparation-scaffolding vs AI-as-alpha-source are different claims with different verification burdens.

`[TENTATIVE]` — single-source creator content; no performance claims to verify. The methodology is internally consistent and standard discretionary-trading practice.

## Snippets

> "Personally, I don't like setting PnL goals and instead focus on goals based on my weaknesses." [Source: posts.docx — Post 1, @TraderMorin]

> "While justifying why you should take a trade is good, what's better is putting yourself on the other side where you try to find reasons not to take the trade." [Source: posts.docx — Post 1, @TraderMorin]
