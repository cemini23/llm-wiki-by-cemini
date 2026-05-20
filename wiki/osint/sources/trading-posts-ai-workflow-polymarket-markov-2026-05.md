---
title: "Trading posts compilation — AI trading workflow, Polymarket bot mistakes, Markov-chain regime models (May 2026)"
type: source
tags: [source, trading-posts, social-media, discretionary-trading, polymarket-bots, markov-chains, regime-switching, k49]
keywords: [trader-morin, bored2boar, rohonchain, ai-trading-workflow, trade-journaling, polymarket-bot-mistakes, markov-chain, hidden-markov-model, regime-switching, transition-matrix, baum-welch, viterbi]
related:
  - concepts/markov-regime-switching-models.md
  - concepts/ai-assisted-trading-workflow.md
  - concepts/polymarket-bot-architecture.md
  - concepts/quant-finance.md
  - entities/people/rohonchain.md
maturity: validated
read_status: deep-read
created: 2026-05-16
updated: 2026-05-20
clusters: [quant-finance]
---

## Relations

- @concepts/markov-regime-switching-models.md — synthesized from Post 3 (@RohOnChain Markov/HMM framework)
- @concepts/ai-assisted-trading-workflow.md — synthesized from Post 1 (@TraderMorin discretionary AI workflow)
- @concepts/polymarket-bot-architecture.md — Post 2 (@bored2boar) corroborates the existing @0x_Punisher bot playbook
- @concepts/quant-finance.md — corpus-index home for the regime-switching material

## Raw Concept

- **Title**: `posts.docx` — compilation of three trader social-media posts/articles
- **Type**: social-media long-form posts (Twitter/X creators)
- **Location**: `cemini-librarian:/opt/cemini-bulk/research/posts.docx`
- **Retrieved**: 2026-05-16 (dropped into `research to be indexed/`)
- **Contents**: 3 posts — (1) @TraderMorin AI-assisted discretionary trading workflow; (2) @bored2boar Polymarket bot-building mistakes; (3) @RohOnChain Markov-chain / HMM regime-switching framework with full Python implementation.

## Narrative

### Post 1 — @TraderMorin: "The First AI Workflow Every Trader Should Build"

A 5-stage **discretionary** trading process, AI-assisted at the prep layer (not signal generation):

1. **Market Outlook** — weekly/daily bias + pro-trend/counter-trend checklist; setups on radar; high-impact macro data (an "outlook sheet" wired to a macro tracker); key levels (swing highs/lows, supply/demand zones); TPO/composite charts for trade location.
2. **Daily Focus List** — weekly/monthly goals defined by *weaknesses*, not PnL; daily improvement task list.
3. **Trade Plan** — per-setup trade ID + "Checklist Completed" gate; position sizing with a mandatory "Why?" justification on every number; confluence-based A/B/C tier scoring; deliberate disconfirmation ("find reasons not to take the trade").
4. **Trade Execution** — moment-of-execution setup checklist (Mean Reversion / Range Extremity playbooks); tagged execution patterns; scaled entries.
5. **Trade Closure** — emotion journaling across the trade lifecycle; post-trade review identifying *which lifecycle stage* mistakes occur in.

Core thesis: **AI does not fix an unprofitable trader** — it structures preparation, journaling, and review. Emotions are constant; the edge is acting on process not emotion. → synthesized into `@concepts/ai-assisted-trading-workflow.md`.

### Post 2 — @bored2boar: "I built 1,500+ bots. Now I make $12k weekly"

A Polymarket bot operator's seven failure modes (public profile claimed at `$12,784` weekly):

1. **Dirty data** — late/out-of-order ticks, reconnect gaps, stale snapshots. Fix is *infrastructure* not logic: reject abnormal jumps, discard first ticks after reconnect, monitor latency + respawn slow connections, run parallel feeds.
2. **Fictional backtests** — backtests ignore fill probability, depth, latency, slippage, competition. Record own tick data, rebuild the order book, simulate real fills → "your 70% strategy usually becomes 53–56%."
3. **Starting too complex** — begin with one market / one timeframe / one signal (e.g. 15-min BTC window, one external signal, hold to resolution).
4. **Optimizing win rate over profit** — 90% WR entering at 85–90¢ risks $1 to make 5–10¢; one reversal wipes multiple wins. Ask "how much per trade," compute breakeven WR.
5. **Untested execution** — paper trading hides failed/delayed/rejected orders; run a real wallet (even zero-balance), let orders fail, feed failures back.
6. **Weak infrastructure** — dedicated low-latency server; FIFO markets punish second-in-line.
7. **Rushing** — manual test → backtest → execution sim → live dry test → only then deploy.

This **independently corroborates** the @0x_Punisher playbook in `@concepts/polymarket-bot-architecture.md` — same lessons (dirty-data filtering, fill-realistic backtests, win-rate-vs-entry-price, latency, NSF-as-data) from a separate operator. Several claims on that page can move toward `[CONFIRMED]`.

### Post 3 — @RohOnChain: "How To Use Markov Chains To Win Every Single Trade"

A complete **regime-switching** framework with runnable Python: market states (Bull/Bear/Sideways via 20-day rolling return thresholds); maximum-likelihood transition matrix; Chapman-Kolmogorov n-step forecasts (`Pⁿ`); stationary distribution; walk-forward backtest converting `bull_prob − bear_prob` into positions. Part 6 extends to **Hidden Markov Models** (Baum-Welch parameter estimation, Viterbi decoding via `hmmlearn`), where the regime is latent and inferred from returns. Documents the three breaking assumptions: Markov property, time homogeneity, estimation-data sufficiency. → synthesized into `@concepts/markov-regime-switching-models.md`.

### Caveats

- All three are **social-media creator content** — promotional components (TG channels, public profiles, "win every trade" framing). Treat methodology as plausible-and-corroborated; treat specific PnL/win-rate numbers as `[TENTATIVE]` single-source.
- The Markov post's code is standard and correct (yfinance + numpy + hmmlearn); the *framing* ("win every trade") is marketing — Markov models quantify transition probabilities, they do not predict.

## Snippets

> "The biggest trap that new traders fall into when trying to implement AI is thinking that it will magically fix their mistakes ... if you are not a profitable trader then AI doesn't suddenly change that." [Source: posts.docx — Post 1, @TraderMorin]

> "Because most backtests ignore fill probability, order book depth, latency, slippage and competition ... Once you do that, your 70% strategy usually becomes 53-56%. And that's actually usable." [Source: posts.docx — Post 2, @bored2boar]

> "P(Xₙ₊₁ = s | X₀, X₁, ..., Xₙ) = P(Xₙ₊₁ = s | Xₙ) — The probability of the next state depends only on the current state, not on the entire history." [Source: posts.docx — Post 3, @RohOnChain]
