---
title: "HGM-Dual — keep a lineage of what each ancestor changed"
type: source
related:
  - concepts/k294-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-23
---

## Raw Concept

Title: HGM-Dual — lineage-aware guided agent-harness optimization
Authors: Sudipta Paul and coauthors, Samsung Research America
Type: arXiv preprint (2610.30042)
Inbox file: `research to be indexed/seo/arxiv-2610.30042-hgm-dual-lineage-aware-guided-agent-harness-opti.pdf`
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.30042-hgm-dual-lineage-aware-guided-agent-harness-opti.pdf`
Retrieved: 2026-10-23
Read status: skimmed (abstract)

## Narrative

For planning agents, open-ended self-modification wastes evaluations.

HGM-Dual keeps a lineage of what each ancestor changed and whether it helped. Each parent grows one general child and specialized children aimed at the worst constraint violations.

It gains up to **14.45%** relative case accuracy over the strongest baseline. It matches HGM variants' final performance with **2x-4x** fewer evaluations.

The method buys the same result with less search. **No install. No route swap.**
