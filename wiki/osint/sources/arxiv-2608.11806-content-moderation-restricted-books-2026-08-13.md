---
title: "Content Moderation via Restricted Books — From Refusal to Warning"
type: source
tags: [arxiv, k235, content-moderation, llm-policy, cyber, ccc]
keywords: [2608.11806, restricted-books, ALA, zero-refusal, warning-language, hesitation, provider-styles]
related:
  - concepts/llm-content-moderation-refusal-to-warning.md
  - sources/arxiv-2608.11816-china-vlm-state-alignment-2026-08-13.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @concepts/llm-content-moderation-refusal-to-warning.md — synthesized concept + cross-wiki brief pointer
- @sources/arxiv-2608.11816-china-vlm-state-alignment-2026-08-13.md — companion paper, same wave

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11806 (2026-08-12) |
| Authors | Yu, Knox, Wang (UIUC) |
| sha256 | `bce8b8c2a4f98eb324c5f55c5bc9548d77bb5700d6d8bc048a94c7e1ba5e2532` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11806-understanding-content-moderation-in-large-langua.pdf` |
| retrieved | 2026-08-13 |

## Narrative

Controlled experiment: **40,800 query–response pairs, 400 books (ALA Most Challenged 2000–2023), 17 prompt designs, 6 frontier models across 6 providers** (Claude Sonnet 4.5, GPT-4o, Gemini 2.5 Flash, DeepSeek-V3, Qwen-Plus, Grok-4.1-Fast). Central finding: **zero-refusal phenomenon** — modern LLMs refuse to discuss restricted books in only 0.07% of cases, invalidating jailbreak research for this content class. Differentiation has migrated to *how* content is discussed: warning language (+8–15 pp, p<0.001), hesitation markers (+2–5 pp), sexual-content mention (+33–52 pp, strongest single signal).

Provider styles decompose cleanly: **Claude = direct-warning; GPT-4o = conditional hedging; Gemini/Grok = highest warning gaps with low hesitation; DeepSeek/Qwen intermediate**. Scenario-based prompts (ban-context) produce up to 19 pp warning-rate gaps; abstract controversy queries invert the effect. Content policy has shifted from binary refusal toward calibrated, context-sensitive disclosure — consistent across Western and Chinese providers.

Relevance: cyber wiki (moderation/refusal behavior of lab models) + CCC (refusal/moderation awareness in harness design). Complements 2608.11816's reframing finding — refusal is the wrong signal in both papers.

[Source: arXiv:2608.11806]

## Snippets

> "modern LLMs decline to discuss restricted books in only 0.07% of cases, effectively invalidating the premise of jailbreaking research for this content class" [Source: arXiv:2608.11806 p.1]
