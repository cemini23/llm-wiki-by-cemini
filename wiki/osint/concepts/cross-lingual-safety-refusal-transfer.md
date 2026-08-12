---
title: Cross-Lingual Safety Refusal Transfer — the low-resource safety gap
type: concept
tags: [concept, llm-safety, multilingual, refusal, k233, cyber]
keywords: [cross-lingual-safety, refusal-transfer, low-resource, lodna, latent-geometric]
related:
  - sources/arxiv-2608.11146-cross-lingual-safety-2026-08-12.md
  - concepts/reasoning-trace-exfiltration.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/arxiv-2608.11146-cross-lingual-safety-2026-08-12.md
- @concepts/reasoning-trace-exfiltration.md

## Raw Concept

What this page answers: does English-centric safety alignment transfer to low-resource languages? From arXiv 2608.11146 (Twi, Hausa, Amharic, Swahili).

## Narrative

Safety alignment is largely English-trained, but cross-lingual transfer is severely limited: harmful prompts retain **<10% of the English refusal signal** across most language×model pairs. Literal vs localized prompts are semantically aligned (cosine 0.95–0.996) yet drift across layers — models encode concepts without routing them to safety mechanisms. Implication for the abliterated lab: refusal surfaces are uneven across languages; "safety" is not monolithic. Relevant to owned-scope testing of which language/model combinations refuse.

[Source: arXiv:2608.11146]
