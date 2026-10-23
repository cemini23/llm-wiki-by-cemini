---
title: "Agent S4 — evolve the interface, keep the model"
type: source
related:
  - concepts/k294-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: Evolving agent interfaces (Agent S4)
Authors: Saaket Agashe, Yuzhe Yang, Xin Eric Wang
Type: arXiv preprint (2610.28601)
Inbox file: `research to be indexed/seo/arxiv-2610.28601-evolving-agent-interfaces.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.28601-evolving-agent-interfaces.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)
Code URL in the paper: https://github.com/simular-ai/agent-s

## Narrative

Agent S4 changes the interface around a fixed model. A meta-agent builds interfaces from trajectories that have no success labels. Selection uses validation tasks the meta-agent never sees.

With Qwen3.8-27B against an evolved interface repository, the binary score on OSWorld V2 is **21.3%**. That is **3.8 times** the same model with fixed interfaces.

The score is above GPT-5.5 at **13.0%** and Claude Opus 4.8 at **20.6%**. The run costs about **4.3%** and **1.5%** of those models' costs.

ScienceBoard goes from **41.4%** to **58.6%** with the same model.

The lever is the interface repository, not a larger model and not a route swap. **No clone. No route swap.**
