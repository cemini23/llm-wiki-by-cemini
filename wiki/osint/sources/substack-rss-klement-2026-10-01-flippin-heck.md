---
title: "Klement — Flippin' heck: agent summaries flip buy/sell calls (2026-10-01)"
type: source
tags: [source, k277, agents, verification, macro]
keywords: [k277, hallucination, agent-reliability, flip, FILE]
related:
  - concepts/k277-harness-evolution-wave.md
maturity: draft
created: 2026-10-01
updated: 2026-10-01
read_status: skimmed
---

## Relations

- @concepts/k277-harness-evolution-wave.md

## Raw Concept

| File | `substack-rss-klement-2026-10-01-flippin-heck.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-klement-2026-10-01-flippin-heck.md` |
| Archive | egress-fi 2026-10-01 |
| URL | https://klementoninvesting.substack.com/p/flippin-heck |
| Retrieved | 2026-10-01 |
| Dual-ID | **OSINT K277** |
| sha256 | `d111357fccb95865128c5058a548d3a151166c6502730ad8a132c84df7e7b315` |

## Narrative

A summary of Lee et al. (2026). The team tested how agentic workflows change an investment call. They had ChatGPT, Gemini, Qwen, and DeepSeek compress the MD&A section of the 100 largest US stocks into 20 points. They then asked Gemini for a buy, hold, or sell call, once from the summary and once from the full document.

The headline number: the recommendation flipped, buy to sell or sell to buy, in roughly **one in four to one in three cases**.

A second measure: the decision model differed by about 11% on MD&A and about 9% on earnings calls.

The author's conclusion is that such a tool is too random to trust for a portfolio decision.

This is the strongest companion yet to the K276 invalid-traces finding. Both say the same thing from different directions. K276 shows a correct answer can carry an invalid trace. This item shows a correct-looking summary can carry the opposite conclusion. **A summary is not the document.** Do not arm a watch. Do not trade from a summary.
