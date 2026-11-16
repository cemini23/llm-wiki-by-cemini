---
title: "TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents (2611.18493)"
type: source
maturity: draft
related:
  - concepts/trading-agent-compliance-controls.md
updated: 2026-11-16
---

## Raw Concept

- **Title:** TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents
- **Authors:** Sandip Nandi, Aishwarya Bose, Apurba Bose, Soovadeep Bakshi (independent)
- **Type:** arXiv preprint
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2611.18493-tradegauntlet-evaluating-compliance-controls-for.pdf`
- **Retrieved:** 2026-11-16
- **arXiv:** 2611.18493
- **Read status:** skimmed (abstract)

## Narrative

The question: what controls stop an autonomous trading agent from placing problematic orders, and what do those controls cost its intended task? The authors separate detection, prevention and execution cost in a replayable limit-order-book simulator.

Findings from 1,680 simulated sessions with Claude Haiku 5.5 and Sonnet 5.5: every conduct alert observed was a self-match. Gates eliminated those alerts by rejecting self-crossing orders. An aggregate-gate condition reduced Sonnet's two-sided fills by about 15%. A conduct reminder lowered Sonnet's alert rate but cut Haiku's fills without a detectable alert benefit.

The methodological point is the strongest contribution: **zero alerts does not establish compliance.** Scripted probes and two search methods found split-order schedules that evade the implemented conduct rules. A learned baseline caught all 2,400 searched episodes but also flagged 15% of a large maker's sessions.

Also reported: aggregate caps reduce the response-dependent gain unevenly, and estimates depend on market assumptions (a response fitted to five Nasdaq stocks, plus a separate ABIDES experiment). The authors state plainly that the experiments do not establish legal compliance or real-market detection accuracy.

[Source: arxiv-2611.18493-tradegauntlet-evaluating-compliance-controls-for.pdf]

## Snippets

> "all conduct alerts were self-matches."

> "zero alerts alone do not establish an agent's compliance."
