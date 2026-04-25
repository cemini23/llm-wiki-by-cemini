---
title: "Options Trading and Firm Investment Efficiency"
type: source
tags: [pdf, options-derivatives, corporate-finance, investment-efficiency, optionmetrics, crsp, compustat, granger, managerial-learning]
clusters: [options-derivatives]
related: []
maturity: validated
created: 2026-04-23
updated: 2026-04-23
---

## Relations

*(Cross-references will be added in Phase 2.)*

## Raw Concept

- **Original title**: Options Trading and Firm Investment Efficiency
- **Author(s)**: Charles Hsu (HKUST), Junqiang Ke (Central U of Finance and Economics), Zhiming Ma (Peking/Guanghua), Lufei Ruan (SFSU, corresponding)
- **Type**: PDF (SSRN working paper / accounting-finance journal submission, abstract id 4689559)
- **Location**: research for cemini/options 4:5.pdf
- **Length**: 63p
- **Retrieved**: 2026-04-23
- **Read status**: read-skim (abstract + data-availability only)
- **Primary cluster**: options-derivatives
- **All clusters**: options-derivatives

## Narrative

**Accounting/corporate-finance paper** — not a quantitative options-pricing or trading-strategy paper. Examines whether the presence of active options trading on a firm's stock causally improves that firm's **investment efficiency** (defined via Richardson-style abnormal-investment models). Data: OptionMetrics for options, CRSP for prices, Compustat for financials, I/B/E/S for analysts, Thomson Reuters for institutional ownership.

**Identification strategy stack** (strong for an accounting paper):
- Firm and year fixed effects
- PSM / coarsened-exact matching
- Instrumental variable approach
- Granger causality test
- Quasi-natural experiment on options-exchange listing decisions

**Findings:**
- Active options trading → higher investment efficiency (less overinvestment AND less underinvestment).
- Mechanisms: (1) **information asymmetry reduction** — options traders bring private info into prices; external monitors read it; (2) **uncertainty resolution** — managers learn about future uncertainty from options-market signals (implied vol, smile).
- Cross-sectional heterogeneity: effect stronger for firms with higher baseline over/under-investment, higher managerial risk-taking, and stronger learning incentives.
- Effect is **distinct from the stock-market-informational-efficiency effect** — options add information beyond what stock prices carry.

Relevant to Cemini only marginally. This paper has almost nothing to do with the Cemini stack: it is a corporate-finance/accounting empirical study of how options listings affect the firms on whose stock the options are written. It will not produce features for the MAPPO observation space or signals for the options feature layer. The filename clustered it to `options-derivatives` only because of the keyword "options" — this is a weak classification. Indirect relevance: (a) could motivate watching for firms that have just had options listed as a structural-regime-change feature for the universe-screening agent, (b) reinforces (from an orthogonal literature) that implied-vol and options-trading signals carry information beyond stock returns — aligns with Cemini's options-layer thesis in `3-19-trading-options-data-research.md`. Honest limits: (1) accounting journal, so externally-pretty identification strategy but internally-heavy reliance on Compustat's investment-efficiency proxies (Richardson-residual-based) which are noisy; (2) cross-sectional effects are consistent with the mechanism but do not rule out unobserved-heterogeneity stories; (3) the paper is about *listed* equity options on US firms — crypto/perpetual/prediction-market options are entirely outside scope.

## Key findings

- Causal finding (across multiple IV, matching, Granger, quasi-natural-experiment strategies): active options trading improves optioned-firm investment efficiency.
- Mechanisms: reduced info asymmetry (external monitoring) + managerial learning from option-implied uncertainty signals.
- Cross-sectional heterogeneity: effect stronger for firms with higher over/underinvest tendency, higher managerial risk-taking, higher learning incentives.
- Effect is distinct from stock-market informational-efficiency contribution — options add marginal info.
- Data stack: OptionMetrics + CRSP + Compustat + I/B/E/S + Thomson Reuters.
- Relevance to Cemini is weak; closest application is as a structural-regime-change feature (firm recently had options listed) for universe screening.
- Supports the options-layer thesis in `3-19-trading-options-data-research.md` from an orthogonal (corporate-finance) direction.

## Snippets

- **Abstract** — "active options trading improves an optioned firm's investment efficiency, and that this effect holds under several alternative empirical specifications and identification strategies, including fixed-effects models, different matching methods, an instrumental variable approach, a Granger causality test, and a quasi-natural experiment based on the listing decisions of the options exchanges."
- **Abstract** — "This relation is mediated by two factors, namely information asymmetry and uncertainty, consistent with the notion that options trading improves investment efficiency by providing information that facilitates external monitoring and helps managers learn about future uncertainty."
- **Data availability** — "We obtain options trading data from OptionMetrics, stock price data from CRSP, company financial data from Compustat, analyst data from I/B/E/S, and institutional ownership data from Thomson Reuters."
