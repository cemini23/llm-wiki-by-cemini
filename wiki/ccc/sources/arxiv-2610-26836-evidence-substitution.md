---
title: "Same Simulation, Different Evidence — retrieved tool output costs accuracy"
type: source
related:
  - concepts/k293-ccc-wave.md
  - concepts/evidence-substitution-retrieved-tool-output.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy
Authors: Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu, Mohammad Javad Abdolhosseini Qomi, Maziar Raissi (UC Riverside; UC Irvine)
Type: arXiv preprint (2610.26836)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.26836-same-simulation-different-evidence-where-retriev.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract)

## Narrative

Agents use PHREEQC, a deterministic geochemistry simulator, to answer 158 execution-checked multiple-choice items. Reports reach 846.8k characters, so a harness may keep the report out of context and let the agent read it through a section index.

GPT-5.1 and GPT-5.2 then lose **11.3** and **7.9** points. Claude Opus 4.6 and Sonnet 4.6 show no detectable cost. Both GPT models still compute the keyed value about as often. What changes is the evidence they answer from. They skip the report, answer from their own higher-precision files, and mis-round. The authors call this evidence substitution. With the simulation held fixed, retrieval still costs GPT-5.2 **9.4** points. For GPT-5.4, more frequent correct simulations mask an evidence-use loss of about ten points, so the net change is indistinguishable from zero.

Naming the authoritative output raises accuracy by **6.3–7.9** points over plain retrieval for the three GPT models. The domain is geochemistry. The harness lesson is not. See @concepts/evidence-substitution-retrieved-tool-output.md and @osint-wiki/concepts/agent-tool-use-verification.md. **No install.**

## Snippets

> "With the simulation held fixed, retrieval still costs GPT-5.2 9.4 points." [Source: arxiv-2610.26836 abstract]
