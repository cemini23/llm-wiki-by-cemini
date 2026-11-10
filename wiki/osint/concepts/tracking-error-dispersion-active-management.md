---
title: Tracking error and dispersion — why active managers do not beat the benchmark
type: concept
related:
  - sources/substack-rss-moontower-2026-11-08-moontower-335.md
  - sources/substack-rss-moontower-2026-11-08-your-thoughts-are-gerrymandered.md
  - concepts/dispersion-trading.md
updated: 2026-11-10
---

## Raw Concept

Why does higher cross-sectional dispersion fail to help active managers? Prompted by the Elm Wealth argument summarised in Moontower #335.

## Narrative

### The puzzle

Low correlation between stocks should give stock pickers more room. In practice, active manager underperformance does not improve in low-correlation regimes. Managers in high-correlation regimes complained that there was no opportunity; managers in low-correlation regimes do no better.

### The mechanism

Managers are judged against a benchmark and manage **tracking error** — the volatility of returns relative to that benchmark. Clients, consultants, and risk teams hold tracking error inside a narrow band.

When dispersion rises, the same positions produce more tracking error. To stay inside the band, the manager **shrinks position sizes**. The extra dispersion is spent on constraint, not on return.

### The formula

If tracking error is held constant, the share of managers who underperform is approximately:

```
Share underperforming ≈ N(costs / tracking error)
```

`N` is the standard normal CDF. `costs` include fees and trading costs.

At **1.5% cost** (1% fee, 0.5% trading) and **3% tracking error**:

```
N(1.5 / 3) = N(0.5) ≈ 0.69
```

So about **69%** of managers underperform. That matches observation. As tracking error goes to zero the formula gives 100%, which is Sharpe's arithmetic of active management. [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

**Dispersion does not appear in the formula.** A manager who holds tracking error fixed removes its effect by construction.

### The second effect

Active management is negative-sum on risk **before costs**. Active portfolios sum to the market, so the average active portfolio is riskier than the market. The extra risk is idiosyncratic and uncompensated. A manager who exactly matched the index return would still deliver a worse risk-adjusted result.

High dispersion sharpens the dilemma:

- keep position sizes → take more uncompensated risk;
- cut position sizes → give up the dispersion benefit and pay trading costs to do it.

Either way the investor loses.

### What this is good for

- **A sanity check on fund claims.** If a manager reports high tracking error in a high-dispersion period, ask whether the excess return covered the extra idiosyncratic risk.
- **A prior for strategy selection.** A discretionary equity strategy benchmarked to an index is fighting a structural headwind. A strategy with an absolute or volatility target is not.
- **A caution on "more dispersion means more alpha".** The constraint consumes it.

## Snippets

> "When dispersion rises, the same positions generate more tracking error, so managers tend to shrink their bets." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "With a cost disadvantage of 1.5% (fees of 1% and trading costs of 0.5%) and tracking error of 3%, about 69% of managers should underperform. That is close to what we observe." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

> "Active management is also a negative-sum game on risk, even before costs." [Source: substack-rss-moontower-2026-11-08-moontower-335.md]

## Dead Ends

- **Treating dispersion as a tailwind for benchmarked managers.** The tracking-error constraint neutralises it.
- **Using the formula as a performance model.** It gives the share below the benchmark, not the size of the shortfall.
