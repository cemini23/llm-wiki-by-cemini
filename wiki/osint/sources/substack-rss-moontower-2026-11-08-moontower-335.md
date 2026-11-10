---
title: "Moontower #335 — commodity index construction, dispersion, and a Levine index"
type: source
related:
  - sources/substack-rss-moontower-2026-11-08-your-thoughts-are-gerrymandered.md
  - concepts/k296-feeds-wave.md
  - concepts/commodity-index-construction.md
  - concepts/tracking-error-dispersion-active-management.md
  - concepts/dispersion-trading.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Moontower #335 |
| Author | Kris Abdelmessih (Party at the Moontower) |
| Type | newsletter, RSS |
| Location | `research to be indexed/substack-rss-moontower-2026-11-08-moontower-335.md` |
| Retrieved | 2026-11-08 |
| File | substack-rss-moontower-2026-11-08-moontower-335.md |
| Read status | read |

## Narrative

The issue has three market sections and one non-market essay. The essay is filed separately as @sources/substack-rss-moontower-2026-11-08-your-thoughts-are-gerrymandered.md.

### Commodity indices are oil bets

This is the main money section. It summarises Bruno Schwalbach's critique of standard commodity indices and his alternative.

The critique:

- **GSCI is mostly energy.** Energy was over half the 2026 weight and has carried about **85% of the index's risk** over history.
- **BCOM caps sectors but not risk.** The 33% sector cap still leaves about half the risk in energy.
- **Variance drag is large.** The GSCI averaged **5.1% a year** but compounded at **2.7%**.
- **Diversification is thin.** Across 26 commodity futures, average pairwise correlation is **0.14 across sectors** and **0.53 within a sector**. [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

The proposed alternative, **Balanced Commodity**, splits risk equally across six sectors, tilts toward trending markets, and holds cash when everything trends down. It is long-only and unlevered. Backtest from **1996**, after costs:

| Metric | Balanced Commodity | GSCI |
|---|---|---|
| Annual return | 8.2% | 2.8% |
| Max drawdown | 35% | 88.5% |
| Correlation to global equities | 0.29 | — |
| 2008 return | 1.1% | — |
| 2022 return | 7.5% | — |

[Source: substack-rss-moontower-2026-11-08-moontower-335.md]

The honest failure case is stated: from January to mid-October 2026 the **GSCI returned 60%** and Balanced Commodity returned **16%**. The author's view is that this is a prior problem, not a product problem. If you want broad commodity exposure, buy a well-built index. If you want oil, buy oil. Do not mix the two motives.

He also notes that the Rogers index (RICI), built to escape these problems, is still **40% energy by weight**. Its wrinkle is that its roll dates front-run the much larger GSCI rolls.

### Dispersion does not help active managers

This section summarises an Elm Wealth note on why low correlation has not helped stock pickers.

The mechanism is **tracking-error targeting**. As dispersion rises, the same positions generate more tracking error, so managers shrink their bets. The share of managers who underperform is approximately:

```
Share underperforming ≈ N(costs / tracking error)
```

where `N` is the standard normal CDF. At 1.5% cost (1% fees, 0.5% trading) and 3% tracking error, about **69%** of managers should underperform. That matches observation. As tracking error goes to zero the formula gives 100%, which is Sharpe's arithmetic of active management. Dispersion does not appear in the formula because a manager who holds tracking error fixed removes its effect. [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

The second point is that active management is negative-sum on risk before costs. Active portfolios add up to the market, so the average active portfolio is riskier than the market, and the extra risk is uncompensated.

### The Levine index

An operational note with a reusable pattern. Abdelmessih had agents (Grok and Claude) index his Gmail archive of Matt Levine's newsletter. The pipeline read **1,533 daily columns**, split into **8,845 sections**, read **277 candidates in full**, and kept **160**. A section qualifies when a market, a mechanic, or a company story has commodities at its core.

The output is flat files in git, one file per entry, with date, column, theme tags, a short summary, and one verbatim passage. Claude adds new columns each Monday. The value is retrieval: a writer in a project folder can call the index instead of searching years of email.

### Why it matters here

- The **tracking-error formula** is a small, checkable model for the "why active managers underperform" question. It is usable as a sanity check on any fund-selection claim.
- The **commodity index critique** gives concrete numbers for a common error: treating a commodity index as broad exposure when it is an oil bet.
- The **corpus-indexing pattern** is a general recipe for a personal research index: extract sections, screen candidates, keep a verbatim quote, store flat files in git, refresh on a schedule.

## Snippets

> "Energy was over half of the S&P GSCI's weight in 2026 and has carried about 85% of its risk over history." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "The GSCI averaged 5.1% a year but compounded at 2.7%." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "Share underperforming ≈ N(Costs / Tracking Error). With a cost disadvantage of 1.5% and tracking error of 3%, about 69% of managers should underperform." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "Across 26 commodity futures, correlation averages 0.14 across sectors, 0.53 within a sector." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

## Dead Ends

- **Reading Balanced Commodity as a free lunch.** It trails the GSCI badly when energy rallies. The 2026 year-to-date gap was 60% to 16%.
- **Treating dispersion as a tailwind for discretionary managers.** The tracking-error constraint consumes the benefit.
