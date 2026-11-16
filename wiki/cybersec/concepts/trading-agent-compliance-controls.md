---
title: Compliance controls for autonomous trading agents
type: concept
maturity: draft
related:
  - sources/arxiv-tradegauntlet-2611.18493.md
updated: 2026-11-16
---

## Raw Concept

Question this page answers: which controls around a trading agent actually prevent bad orders, and how do you test them?

From TradeGauntlet (arXiv 2611.18493).

## Narrative

Two distinct control types. A **gate** checks an order before it reaches the market and may reject it. A **detector** inspects the order stream afterwards and raises an alert. Conflating them makes a compliance result unreadable, because a quiet detector and an effective gate look the same if you only count alerts.

What the simulator found. Every alert observed in 1,680 sessions was a self-match; gating self-crossing orders removed them. An aggregate cap cut two-sided fills by about 15% — a real cost to the intended task, not a free control. A conduct reminder helped one model and hurt another.

Why zero alerts is not compliance. Scripted probes and two search methods found split-order schedules that evade the implemented rules. That is the test any claim must survive: not "no alerts fired" but "an adversarial search could not construct an evading schedule."

False positives are a control cost too. The learned baseline caught all 2,400 searched episodes but flagged 15% of a large maker's sessions.

[OPEN QUESTION 2026-11-16] Real-market detection accuracy and legal compliance are explicitly outside what the paper measured. Any production claim needs venue-level evidence.

## Snippets

> "zero alerts alone do not establish an agent's compliance."
