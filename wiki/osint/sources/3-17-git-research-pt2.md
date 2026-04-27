---
title: "Targeted Technical Research Audit: Cemini Financial Suite (3/17 Part 2)"
type: source
tags: [docx, cemini-internal, llm-agents, prediction-markets, infrastructure, alt-data]
clusters: [llm-agents, prediction-markets, cemini-internal, infrastructure, alt-data]
related:
  - entities/data-sources/gdelt.md
  - entities/infrastructure/hetzner.md
  - entities/frameworks/finbert.md
maturity: validated
read_status: deep-read
created: 2026-04-23
updated: 2026-04-23
---

## Relations

- @entities/data-sources/gdelt.md
- @entities/infrastructure/hetzner.md
- @entities/frameworks/finbert.md

## Raw Concept

- Original title: Targeted Technical Research Audit: Cemini Financial Suite (Part 2)
- Authors: Cemini internal authoring team (unsigned)
- Affiliation: Cemini internal
- Type: DOCX, internal technical research audit
- Location: research for cemini/3_17 git research pt2.docx
- Length: long-form
- Retrieved: 2026-04-23
- Publication date: 2026-03-17
- Read status: deep-read
- Primary cluster: alt-data
- All clusters: llm-agents, prediction-markets, cemini-internal, infrastructure, alt-data
- Flag: **cemini-internal** — evaluation document, not external research.

## Narrative

Part 2 of a GitHub/tech research audit series. Three main integration threads: (1) **BitNet 1.58-bit ternary quantization** from Microsoft as a CPU-only inference unlock for the Hetzner 128GB VPS — the suite is CPU-only so ternary-quantized LLMs are evaluated for inference latency and memory; (2) a **Code Review Graph** tool proposal that treats code reviews as a graph over files/PRs/authors to surface review patterns and risk clusters; (3) **GDELT integration** for geopolitical event-driven signals feeding the alt-data layer.

Each thread comes with implementation notes (licenses, integration path, likely engineering time) and explicit fit/no-fit judgments against the Cemini architecture. The document does its own due-diligence work — flagging licensing concerns for BitNet, noting Code Review Graph is early-stage with limited adoption, and marking GDELT as high-priority but requiring FinBERT or similar for sentiment scoring.

Value: a useful curated scan of GitHub-level tooling for a CPU-only fintech stack. Treat as an **internal architect's memo**, not research. The items it recommends (BitNet, GDELT) are externally verifiable and the document flags its own uncertainty levels honestly.

## Key findings

- BitNet 1.58-bit ternary quantization evaluated for CPU-only LLM inference on Hetzner.
- Code Review Graph proposed for risk-clustering reviews (early-stage tool).
- GDELT integration recommended for geopolitical event signals with FinBERT sentiment layer.
- Each item has explicit fit judgment, license notes, engineering-time estimate.
- Internal audit document, not external research.

## Snippets

- **BitNet** — "Microsoft BitNet 1.58-bit gives credible CPU inference for 7B–13B models on Hetzner 128GB" — the unlock.
- **Code Review Graph** — Noted as early-stage; adoption risk flagged.
- **GDELT** — "High-priority alt-data source; pair with FinBERT for sentiment scoring" — the recommended stack.
