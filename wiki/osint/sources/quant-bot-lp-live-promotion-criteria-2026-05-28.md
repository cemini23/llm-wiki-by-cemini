---
title: Mathematical Criteria for Promoting LP Algorithms to Live Trading
type: source
tags: [source, cemini-internal, liquidity-provision, validation, markout, deflated-sharpe]
keywords: [LP-bot, DSR, deflated-sharpe, markout, MCPT, shadow-trading, kill-switch, MDD]
related:
  - concepts/lp-algorithm-live-promotion-gates.md
  - concepts/monte-carlo-permutation-test-mcpt.md
  - concepts/regime-conditioned-evaluation.md
  - concepts/polymarket-lp-rewards-farming.md
  - concepts/shadow-to-live-transition-engineering.md
  - concepts/zero-trade-edge-signal-diagnostics.md
maturity: validated
read_status: deep-read
created: 2026-05-28
updated: 2026-05-28
clusters: [cemini-internal, liquidity-provision, quant-validation]
---

## Relations

- @concepts/lp-algorithm-live-promotion-gates.md — promotion gate checklist for Cemini LP workstreams
- @concepts/monte-carlo-permutation-test-mcpt.md — MCPT section cross-validates K56 @phosphenq framework
- @concepts/regime-conditioned-evaluation.md — DSR / multiple-testing discipline
- @concepts/polymarket-lp-rewards-farming.md — Cemini PM LP bot context
- @concepts/shadow-to-live-transition-engineering.md — shadow incubation pipeline (§4)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Architecture of Trust: Mathematical Criteria for Promoting Liquidity Provision Algorithms to Live Trading |
| Author | Unspecified (Gemini DR / research synthesis) |
| Type | DOCX |
| sha256 | `611cde3b27e2845e72cb9a2d7237dd59f1dc43e6003811c992520604c2f35ba8` |
| Location | `cemini-librarian:/opt/cemini-bulk/research/quant-bot-lp-live-promotion-criteria-2026-05-28.docx` |
| Retrieved | 2026-05-28 |
| Read status | deep-read |

## Narrative

~39k-char survey of **industry-style GO criteria** for LP / market-making bots. Flash Crash (2010) and Knight (2012) as motivation. Five pillars:

1. **Deflated Sharpe Ratio (DSR)** — López de Prado / Bailey framework correcting for skew, kurtosis, and **multiple testing** (`N` trials → expected max Sharpe). Standard GO: DSR above high confidence threshold (source text truncates numeric cutoff in export — treat as **operator-defined**, not copy-paste).

2. **Monte Carlo Permutation Test (MCPT)** — shuffle session returns / gaps separately; p-value = fraction of permuted paths beating live path. Aligns with @concepts/monte-carlo-permutation-test-mcpt.md.

3. **Markout analysis** — realized spread vs effective spread; short-term (10–50ms) and mid-term (1–5s) markout floors for adverse selection detection.

4. **Shadow incubation + minimum PnL floor** — positive shadow PnL necessary but insufficient; floor must cover risk-free rate + fees + infra + capital utilization.

5. **MDD + Expected Shortfall + kill switch** — tight drawdown bounds for market-neutral LP; automated kill switch outside strategy loop (message-rate, position, loss limits).

### Cemini relevance

Before promoting `pm_lp_rewards` beyond paper/shadow: require documented DSR/MCPT evidence, markout stats from shadow window, and kill-switch fire drill. Bump `pm_lp_k69_v1` (or successor) at promotion cutover per K75 registry SOP.

## Snippets

> "A standard 'GO' condition for algorithmic promotion requires a DSR [above stringent confidence threshold]." [Source: quant-bot-lp-live-promotion-criteria-2026-05-28.docx — numeric threshold truncated in DOCX extract]

> "In shadow mode, the candidate LP algorithm consumes live, tick-level market data … but its execution commands are suppressed or routed to a simulated matching engine." [Source: quant-bot-lp-live-promotion-criteria-2026-05-28.docx]
