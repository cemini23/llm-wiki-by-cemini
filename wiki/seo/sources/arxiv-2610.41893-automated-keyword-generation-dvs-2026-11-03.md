---
title: "Automated keyword generation for a high-volume data virtualization service"
type: source
tags: [source, arxiv, keywords, discovery, data-catalog, llm]
related: []
maturity: draft
read_status: skimmed
created: 2026-11-03
updated: 2026-11-03
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Automated Keywords Generation Using LLMs in a High-Volume Data Virtualization Service |
| Authors | Saiful Khan, Yiwen Xing, Joyraj Chakraborty, Afrah Farea, Philip Beaucamp, Samuel Jackson, Min Chen |
| arXiv | 2610.41893 |
| Pages | 12 |
| Read status | skimmed (abstract, truncated) |

## Narrative

A data virtualization service lets users create many versions of a source dataset for different tasks, which means many near-identical virtual datasets accumulate. Users then need to discover existing ones to avoid duplicating work, and that needs a searchable catalogue with good keywords.

The paper addresses **automatically generating those keywords with an LLM** at the scale a high-volume service produces.

### Why it is a real problem and not a trivial one

The datasets are **variants of each other**. Two virtual datasets may differ only by a preprocessing step, and the keyword set has to make them distinguishable — not just describable. That is a harder task than summarising a document, because the useful keyword is often the *difference*, not the content.

**Caveat.** The abstract extract is truncated mid-sentence. No method, quality measure, or evaluation is captured here. This page records the problem framing only.

## Snippets

> "In modern data infrastructure, a data virtualization service (DVS) allows users to create many versions of source datasets for different processing tasks." [Source: arxiv-2610.41893 p.1]

## Dead Ends

- **Citing a quality result.** The abstract was truncated before the method.
