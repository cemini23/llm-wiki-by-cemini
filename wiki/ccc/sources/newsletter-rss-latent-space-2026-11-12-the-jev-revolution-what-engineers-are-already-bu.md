---
title: "The Jev Revolution — system one models inside application code"
type: source
related:
  - concepts/decision-model-hybrid-agent-routing.md
  - concepts/token-economics-and-prompt-caching.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Jev Revolution: What Engineers Are Already Building with System One Models |
| Author | Latent Space (AI Engineer Code Summit coverage) |
| Type | Newsletter (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-12-the-jev-revolution-what-engineers-are-already-bu.md` |
| Retrieved | 2026-11-14 (published 2026-11-12) |
| Pages | n/a |
| Read status | read |

## Narrative

The session theme was **system one models**: non-generative models that return structured choices, scores, or probabilities. They are faster and cheaper than reasoning models.

Diogo Almeida, co-founder of TypeSafe AI and lead creator of Jev, gave the keynote. His argument is that the core problem with LLM-driven software is reliability: "you get Einstein 95% of the time, but Mr. Bean 5% of the time." If you cannot tell which is which, automation is unsafe. His prescription is to integrate system one models with code, because code is the language of automation. The Latent Space reading: place fast model calls inside application code instead of building elaborate string assembly.

Production users described narrower uses:

- **Glean** uses Jev beside LLMs and other classifiers. The fit is zero-shot flexibility: when the decision taxonomy changes, the model does not need retraining. Customers do not need to know which model type serves a flow.
- **UiPath** ran a tournament that ranked document chunks. Jev picks the best chunk from small groups, and winners advance. The whole process took under a second, with thousands of calls. Their point: Jev is a building block to compose, not a standalone intelligence.
- **Workday** prototyped an interface that fills a time-off card while the user types. The framing is a move from predicting what you want to say to predicting what you want to do.

For Cemini the useful claim is bounded. A small, fast classifier inside a harness can replace a general LLM call for a closed decision. The decision must be checkable, and the fallback path must exist when the model is wrong. The newsletter gives no Cemini measurement.

## Snippets

> "you get Einstein 95% of the time, but Mr. Bean 5% of the time." [Source: newsletter-rss-latent-space-2026-11-12-the-jev-revolution-what-engineers-are-already-bu.md]

> "code is the language of automation, therefore you need to integrate with code." [Source: newsletter-rss-latent-space-2026-11-12-the-jev-revolution-what-engineers-are-already-bu.md]
