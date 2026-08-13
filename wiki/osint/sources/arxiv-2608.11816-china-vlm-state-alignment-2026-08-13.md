---
title: "China-Origin VLMs — From Refusal to Reframing in State Alignment"
type: source
tags: [arxiv, k235, vlm, state-alignment, censorship, cyber]
keywords: [2608.11816, reframing, China-VLM, Qwen, multimodal, refusal, framing, LLM-judge]
related:
  - concepts/llm-content-moderation-refusal-to-warning.md
  - sources/arxiv-2608.11806-content-moderation-restricted-books-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/llm-content-moderation-refusal-to-warning.md — shared thesis: refusal is the wrong signal
- @sources/arxiv-2608.11806-content-moderation-restricted-books-2026-08-13.md — companion paper same wave

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11816 (2026-08-12) |
| Authors | Yang, Liu, Wang, Hosseinmardi, Ghasemian (UCLA / Berkeley / Stanford) |
| sha256 | `c811b1da3fbdb7da0724dc12dcfb52f37ec0efe92c5a74902c8c9f0a73e359db` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11816-how-china-origin-vision-language-models-move-fro.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Benchmark of 200 core entries over 10 politically sensitive topics + a seven-variant visual-abstraction probe; **9 VLMs (7 China-origin) × 4 elicitation paradigms × 2 prompt languages = 21,708 trials**, each audited on six independent dimensions (explicit refusal, information integrity, visual grounding, state-aligned framing, language consistency, response length) by two frontier LLM judges, validated against 3 human experts on a 200-trial sample.

Key findings: (i) Chinese-language prompting roughly **triples** the odds of state-aligned framing within every model — a constant, origin-independent shift; (ii) China-origin models reframe 1.6–3.2× more than non-China models; (iii) strongest in text-only political commentary (36.5%), gated by **subject recognition, not pixel detail** (persists at silhouette for iconic images); (iv) across four Qwen generations, framing rises while refusal falls — **censorship migrates from visible refusal to invisible fluent reframing**, removing the signal users rely on to notice information was withheld.

Relevance: cybersec wiki brief for the local-abliterated lab — when evaluating China-origin open-weight VLMs (Qwen-family) as local vision backends, refusal-rate alone is a broken safety metric; framing bias must be probed separately, and prompt-language effects hold even for local deployments.

[Source: arXiv:2608.11816]

## Snippets

> "censorship migrates from a visible act (refusal) to an invisible one (fluent reframing)… it removes the very signal users rely on to recognize that information has been withheld" [Source: arXiv:2608.11816 p.1]
