---
title: 'An Update of "Loosening Your Collar: Alternative Implementations of QQQ Collars"'
type: source
tags: [pdf, portfolio-strategy, options-derivatives, k49]
keywords: [collar strategy, QQQ, protective put, covered call, passive collar, active collar, momentum signal, volatility signal, VIX, out-of-sample, drawdown, Szado, Schneeweis]
related:
  - concepts/portfolio-strategy.md
  - concepts/options-derivatives.md
clusters: [options-derivatives]
maturity: validated
read_status: deep-read
created: 2026-04-27
updated: 2026-05-16
---

## Relations

- @concepts/options-derivatives.md — options & derivatives cluster hub
- @concepts/portfolio-strategy.md — Portfolio Strategy corpus-index hub

## Raw Concept

- **Original title**: An Update of "Loosening Your Collar: Alternative Implementations of QQQ Collars" — Credit Crisis and Out-of-Sample Performance
- **Author(s)**: Edward Szado (Isenberg School of Management, UMass Amherst / INGARM) and Thomas Schneeweis (Michael & Cheryl Philipp Professor of Finance, Director of CISDM, UMass Amherst). Research support from the Options Industry Council. Original Aug 2009; this update Jan 2011.
- **Type**: PDF — academic working paper / journal article update
- **Location**: research for cemini/Loosening Your Collar- Alternative Implementations of QQQ Collars.pdf
- **Retrieved**: 2026-04-27
- **Length**: 50p
- **Read status**: deep-read
- **Cluster**: options-derivatives

## Narrative

An update to Szado & Schneeweis [2010] extending the analysis from the March 1999 / May 2009 window through September 2010, and adding **out-of-sample** results (June 2009 – Sept 2010) for the active strategies. A **collar** is long underlying + long protective put + short covered call, bounding returns within a chosen range; a tight collar (ATM strikes) immunizes the position, a loose (far-OTM) collar approaches a plain long index. The paper compares **passive collars** (fixed rules: 1-month written call, 1/3/6-month purchased put, ATM–5% OTM moneyness) against an **active "collar adjustment"** strategy that varies strikes and the calls-written ratio using three lagged signals: a NDX moving-average crossover (momentum), a VIX-based volatility band (0.75–1.25 calls per put, after Renicker & Mallick), and a compound macro factor (unemployment claims + NBER business cycle).

Headline results for the 2% OTM passive 1-month-call / 6-month-put collar on QQQ: over the full 138-month period it lifts annualized return from −0.3% (QQQ long) to 9.6%, cuts stdev from ~29.6% to 10.7% (≈⅔ reduction), raises the Stutzer index from 0.05 to 0.67, and slashes maximum drawdown from −81.1% to −17.6%. The collar shines in falling/volatile markets: in the Apr 1999–Sept 2002 tech-bubble sub-period it turned QQQ's −23.3% annualized loss (42.4% vol) into a +21.6% gain at 13.6% vol, with drawdown cut from −81.1% to −7.5%. It lags in the calm Oct 2002–Sept 2007 bull run (the "worst" environment for a collar). Active collars outperformed comparable passive collars both in-sample and **out-of-sample**, and the same strategy wrapped via QQQ options around an optionless small-cap mutual fund produced similar results. The authors caution against Sharpe ratios on skewed option payoffs, preferring the Stutzer index and Leland's alpha.

**Cemini relevance**: a rigorous, multi-decade empirical benchmark for QQQ collar hedging — passive vs. signal-driven active implementations, with concrete drawdown/return/vol numbers — directly useful for CeminiSuite's downside-protection and tactical-overlay research. Set `maturity: validated` (peer-reviewed authors, OIC-supported, multi-period out-of-sample).

## Snippets

> "Over the 138 months of the study, the 2% OTM collar significantly reduces risk and improves realized returns. The returns are improved from a -0.3% annualized loss to a 9.6% gain, meanwhile standard deviation is reduced by about 2/3 from 29.6% to 10.7%... a reduction of the maximum drawdown from -81.1% to -17.6%."
> — [Source: Loosening Your Collar- Alternative Implementations of QQQ Collars.pdf p.24]

> "In this volatile market, the 2% OTM passive collar strategy generated an annualized return of 21.6% at a volatility of only 13.6%. Thus the collar was able to turn a sizeable loss into a significant gain... The maximum drawdown of the QQQ is reduced significantly from -81.1% to -7.5%."
> — [Source: Loosening Your Collar- Alternative Implementations of QQQ Collars.pdf p.25]

> "For the period of analysis, the active collar adjustment strategy tends to outperform the passive collar both in-sample as well as out-of-sample."
> — [Source: Loosening Your Collar- Alternative Implementations of QQQ Collars.pdf p.1 (Abstract)]
