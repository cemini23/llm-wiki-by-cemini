---
title: Market-structure efficiency and edge decay
type: concept
maturity: draft
related:
  - sources/substack-rss-moontower-2026-11-22-hillstone.md
  - sources/substack-rss-moontower-2026-11-22-moontower-337.md
  - concepts/options-derivatives.md
updated: 2026-11-22
---

## Raw Concept

Question this page answers: why does a profitable edge decay, and what should an operator do while it lasts?

Built from two Moontower posts (2026-11-22), an opinion essay with a historical example.

## Narrative

**The SIG example.** SIG tightened markets to win share. It accepted slightly worse risk-reward per trade in exchange for far more absolute dollars. It then used the cash to widen coverage, which let it price and hedge tighter, which won more share. The loop is: better product, more share, more proprietary data, repeat. [TENTATIVE: the author's account, not an audited case study]

**Why the edge was available.** Bookmakers could get rich on much less edge than SIG was taking at the time, and the wider market had not repriced that fact. The edge was a temporary information asymmetry about how lucrative market making had become.

**The decay.** As others copy the model, spreads compress. The author's comparison is Jane Street, whose balance sheet and coverage let it price risk with a near-linear utility of wealth. An edge that once paid a half-dollar pays a penny.

**The rule.** If you find an edge that others have not caught up to, and the edge can absorb capital, push it. Do not assume it persists. Efficiency is good for the market and bad for the incumbent edge.

**Operator application.** A tooling or workflow advantage is also an edge, and it also decays as it spreads. Examples: an automated ingest pipeline, a local model that removes a paid dependency, a faster research loop. Size them while the gap exists, and keep a plan for when the gap closes.

**Caution.** This is an essay, not a measurement. The SIG history is a narrative with survivorship risk, which the author acknowledges. Use it as a prior on edge durability, not as evidence about any specific market.
