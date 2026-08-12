---
title: "The Illusion of Cross-Lingual Safety in Low-Resource Languages"
type: source
tags: [arxiv, k233, cyber, llm-safety, multilingual]
keywords: [2608.11146, cross-lingual-safety, refusal, low-resource, lodna, latent-geometric, safety-alignment]
related:
  - concepts/cross-lingual-safety-refusal-transfer.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: skimmed
---

## Relations

- @concepts/cross-lingual-safety-refusal-transfer.md
- @cybersecurity-wiki/concepts/local-abliterated-llm-pentest-stack.md
- @cybersecurity-wiki/briefs/2026-08-12_k233-redagentbench-crosslingual-safety.md (cross-wiki brief)

## Raw Concept

| Field | Value |
|-------|--------|
| arXiv | 2608.11146 |
| sha256 | `799067a1692f614eb72de189f5ec787098cf9b959595a2dc7d13b39292962245` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/arxiv-2608.11146-the-illusion-of-cross-lingual-safety-in-low-reso.pdf` |
| retrieved | 2026-08-12 |
| authors | Abigail Oppong, P Sam Sahil, et al. (Makerere, Hamburg, Bayero Kano, Brown, Ghana, CMU, Imperial) |

## Narrative

Tests whether English-centric safety alignment generalizes to low-resource languages. Uses **LoDNA**, a new safety dataset pairing literal translations with culturally localized prompts, across four African languages: **Twi, Hausa, Amharic, Swahili**. To move past generation-based eval, the paper proposes a **Latent Geometric Framework** probing hidden-state refusal representations.

Result: cross-lingual safety transfer is **severely limited** — harmful prompts retain less than 10% of the English refusal signal across most language×model pairs. Literal and localized prompts are semantically aligned (cosine 0.95–0.996) but drift across layers, implying models **encode the concepts without routing them to safety mechanisms**. Strong evidence against a universal, language-agnostic harm manifold.

Relevance to local-abliterated-lab: the refusal-signal-weakness across low-resource languages is a *safety gap*, and also a reminder that abliterated/local models' refusal surfaces are uneven across languages — relevant when choosing which model/language combination to run for authorized assist vs. when a low-refusal surface is the point. For the operator lab, this maps to which target languages to test under an owned scope, and to a caution that "safety" is not monolithic across languages.

[Source: arXiv:2608.11146]
