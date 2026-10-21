---
title: "Unbounded Losses, Unchecked Inputs — safeguards of LLM options-trading agents"
type: source
related:
  - concepts/k293-osint-wave.md
  - concepts/options-agent-order-boundary.md
maturity: draft
read_status: read
updated: 2026-10-20
---

## Raw Concept

Title: Unbounded Losses, Unchecked Inputs: Measuring the Safeguards of LLM Options-Trading Agents
Authors: Mengxiao Wang, Nitesh Saxena (Texas A&M University)
Type: arXiv preprint (2610.24289)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2610.24289-unbounded-losses-unchecked-inputs-measuring-the.pdf`
Retrieved: 2026-10-20
Read status: read (abstract and introduction)

## Narrative

This is the first measurement the wiki has of the options agents that brokers and developers ship. Prior work scored academic equities designs by whether an attacker can flip buy versus sell. This paper scores safeguards and the worst loss on the documented order path.

The authors screened 765 GitHub repositories, broker documentation, and the literature. They found 215 eligible repositories and 8 broker-native agent interfaces, then scored 26 systems: every broker interface plus every open-source project with at least 20 stars. The screen used seven robustness safeguards and eleven security safeguards.

The ecosystem is new. **198 of 215 repositories were created in 2026. 129 (60%) appeared in the two weeks around one options-trading hackathon.** Robinhood has announced agentic options trading for all US customers, on a platform with about 27 million funded customers. Listed options averaged 72.8 million contracts a day in 2026 Q2. 0DTE contracts were 66.2% of S&P 500 index-options volume in July 2026. [TENTATIVE] those market figures are the paper's citations, not a Cemini pull.

Of the 22 systems that can place orders, **10 enforce a pre-trade limit outside the model. None of the 26 authenticate their text sources or cross-check market data. 17 can execute with no mandatory human step. 13 can reach unbounded loss, including 6 of the 8 broker interfaces.**

An attacker who writes text the agent reads can move strike, expiry, volatility, and legs while the direction stays correct. The paper's figure: a bull put spread that risks $400 per contract becomes an uncovered put that can lose $9,900 if the protective leg is dropped.

**Status: operational constraint, no trade, no wire.** See @concepts/options-agent-order-boundary.md.

## Snippets

> "Because an attacker who writes the agent's inputs can move an order's strike, expiry, volatility, and legs while its direction stays correct, options agents need loss limits enforced at the order boundary." [Source: arxiv-2610.24289 p.1]
