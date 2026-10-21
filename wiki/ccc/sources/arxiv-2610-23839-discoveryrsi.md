---
title: "DiscoveryRSI — recursive hypothesis search, harness only"
type: source
related:
  - concepts/k293-ccc-wave.md
maturity: draft
read_status: skimmed
updated: 2026-10-20
---

## Raw Concept

Title: DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses
Authors: Jianyuan Zhong and colleagues (PhAI Labs and others)
Type: arXiv preprint (2610.23839)
Location: `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.23839-discoveryrsi-recursively-learning-to-discover-va.pdf`
Retrieved: 2026-10-20
Read status: skimmed (abstract only)

## Narrative

DiscoveryRSI grows a tree of hypotheses, turns a chosen investigation into an executable Harbor task, and learns from the run. Three mechanisms do the learning. Hypothesis credit assigns a scientific score to a documented contribution. Harness replay keeps the strategies that worked and the failures that recurred. Re-discovery applies an accepted change to a new investigation.

The eval domains are life-science. This page does not record those protocols. The reported scores, from the abstract: hypothesis quality moves from **4.86** for the base model to **5.39** after two rounds of self-improvement, with the gains in falsifiability and data resolvability. A 27B variant matches later published work at **6.3%**, versus **2.5%** for GPT-6 and **2.3%** for Claude Opus 5, on the authors' correspondence check. Preliminary human review rates it above GPT-6 Luna on importance and on whether claims stay inside the evidence.

The harness lesson is the credit assignment. A research loop should score the contribution that is written down, then replay the workflow, not the whole transcript. **No clone. No lab use.**

## Snippets

> "Hypothesis quality rises from 4.86 for the base model to 5.39 after two rounds of self-improvement, with the large gains in falsifiability and data resolvability." [Source: arxiv-2610.23839 abstract]
