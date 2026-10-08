---
title: "Moontower — vibey vs discrete trades: options as surgical tools (2026-10-07)"
type: source
tags: [source, k285, options, trading, quant, kelly]
keywords: [moontower, options, vertical-spread, kelly, straddle, nike, earnings, discrete-thesis]
related:
  - concepts/k285-feeds-wave.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-feeds-wave.md

## Raw Concept

| Title | vibey vs discrete trades |
| Source | Moontower Meta (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-moontower-2026-10-07-vibey-vs-discrete-trades.md` |
| Retrieved | 2026-10-07 |
| URL | https://moontowermeta.com/vibey-vs-discrete-trades/ |
| Tier | free (RSS) |
| read-status | read |

## Narrative

Kris Abdelmessih's worked example of **when options are the right tool**. The thesis: options are surgical — use them only for a *specific, terminal-value* view. A vague view ("I want to be long") belongs in stock, where delta is 1.00 and constant; an option forces a **series of future decisions** as time passes and the thesis must be re-tightened.

### The worked trade (NKE, 2026-09-30)

Setup: Nike reports after the close on Oct 1. Stock ~$36; the Oct 2 **36-straddle ≈ $3 (8%)** — a big expected move.

- **Vague expression:** buy the 36 call for ~$1.50. If NKE moves +8%, the call doubles — **1-to-1**. You also keep paying for upside beyond 8%.
- **Discrete expression:** the **38.5/39 call spread at ~$0.12** pays $0.50 if NKE ≥ $39 — **just over 3-to-1** on the same outcome.

The point: a **tighter thesis buys more leverage on being right** and less margin of error. The cost is a binary-ish outcome — wrong most scenarios → total loss.

### Sizing — Kelly

Because the vertical is a near-total-loss bet, it suits Kelly: `f* = p − q/b`. With p = 0.40 and b = 3, `f* = 0.20` → $1,000 of $5,000. Each spread ~$12 → ~83 contracts; sized to **half-Kelly** (overbetting risk if p is overestimated) → **40 contracts**.

### The heuristic worth keeping

The straddle ≈ **80% of one standard deviation**, so the upper tail (a move > $3) is ~**21%** under normality. To make a **3-to-1** bet positive-EV you need **p > 25%**. Normality is doing a lot of work there — earnings are closer to binary. So the "cheap" spread is only cheap if your p beats 25%.

### Postscript (the honest part)

NKE *fell*. The symmetric put spread would have been the 33.50/33. NKE touched $32.09 intraday but closed at $33.90 — the put spread expired worthless, though a quick flip could have tripled it. The rival short-spread side collected the full premium but "the path would have greyed your hair."

### Why it matters here

A **concrete Kelly-sizing worked example for a discrete options thesis** — the xsp lane's method, written out. It reinforces: **buy the specific expression, budget for total loss, let sizing do the risk management.** The wiki already tracks Kelly discipline; this is a desk-grade illustration. **No trade, no scp.**

## Snippets

> "The more tightly you can wrap an option expression around a terminal value thesis, the easier the risk management is because you can budget for total loss and let sizing do the heavy work." [Source: substack-rss-moontower-2026-10-07-vibey-vs-discrete-trades.md]

> "We know from the derivation of the straddle approximation, that the straddle is 80% of 1 standard deviation … To get 3-1 odds would require a minimum probability of 25% to be a positive EV bet." [Source: substack-rss-moontower-2026-10-07-vibey-vs-discrete-trades.md]
