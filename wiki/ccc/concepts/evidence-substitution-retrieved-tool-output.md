---
title: Evidence substitution — retrieved tool output can be the wrong file
type: concept
related:
  - concepts/k293-ccc-wave.md
  - sources/arxiv-2610-26836-evidence-substitution.md
maturity: draft
updated: 2026-10-20
---

## Raw Concept

What this page answers: when a harness parks a long tool report in a file, where does accuracy go? From arXiv 2610.26836.

## Narrative

The agent can compute the right value and still answer with the wrong one. Harnesses that keep long tool output out of the window ask the agent to search or read a file later. On a deterministic USGS simulator (PHREEQC), reports reach 846,800 characters. With the simulation held fixed, the loss is in which text the model treats as the answer.

| Setup | Result |
|---|---|
| Section index instead of in-context report | GPT-5.1 loses 11.3 points. GPT-5.2 loses 7.9. Claude Opus 4.6 and Sonnet 4.6 show no detectable cost. |
| Same simulation, retrieval still on | GPT-5.2 still loses 9.4 points. |
| GPT-5.4 | More correct simulations hide an evidence-use loss of about ten points. Net change is about zero. |
| Name the authoritative output | +6.3 to +7.9 points over plain retrieval for the three GPT models. |

The failure mode is evidence substitution. Under retrieval the GPT models often skip the report, answer from their own higher-precision output files, and mis-round to a neighboring option. Re-running all 11,007 logged simulator calls shows the keyed value was computed about as often as before.

For this workspace: if a tool writes several files, the harness must name the file that is allowed to decide the answer. Retrieval is not a neutral compression step.
