---
title: "Decision-model hybrid routing — small classifiers inside the harness"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md
  - sources/newsletter-rss-latent-space-2026-11-12-the-jev-revolution-what-engineers-are-already-bu.md
  - sources/newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/reasoning-effort-calibration.md
updated: 2026-11-14
---

## Raw Concept

What question does this page answer: can a small, fast model replace a general reasoning call for closed decisions inside an agent harness? Sources: the 2026-11-12 D-Day and Jev newsletters, plus the 2026-11-14 AINews items.

## Narrative

A **decision model** returns a structured choice, score, or probability in one pass. It does not generate text token by token. Examples reported in these sources: Jev from TypeSafe AI, Gemini Decision 1, Perplexity Decider, Drex, and GLiDE.

The useful harness pattern is hybrid, not replacement. At AI Engineer, Cloudflare described a design where a fast decision model picks the tool and extracts log fields, and a larger reasoning model does diagnosis only. In the demo this cut six LLM calls to one and about 40K tokens to 1.8K. [TENTATIVE — vendor demo]

Three properties make the pattern work:

1. **Closed output space.** Tool choice, yes/no checks, rubric scores, and span extraction fit. Open-ended planning does not.
2. **Tolerance for abstention.** SubQ Snap 1.2 ties at 73 on the AA Decision Index, and its gain comes from abstention, not accuracy. A harness must handle "no decision" as a real output.
3. **A checkable result.** Glean reports zero-shot flexibility: the taxonomy can change without retraining. That is only safe when the harness validates the chosen class.

Cost is not automatically better. Gemini Decision 1 costs $345 per 1M tasks, against $103 for Drex Max and $156 for Jev, despite a low per-token price. A harness must compare cost per resolved decision, not cost per token.

Adoption is broad enough to plan for. Vercel reports that 26% of requests route through decision models, and Perplexity reports about 1B decision-model requests per month on OpenRouter. [TENTATIVE]

Cemini fit: the `/route` lane already classifies task difficulty before it spends a reasoning call. A decision model is a candidate for that classifier and for pre-tool checks. Keep the general model for open work, and keep a fallback path when the classifier abstains or returns low confidence.

## Snippets

> "Fast decision models handle tool selection and log extraction, and a large reasoning model handles diagnosis only. In its demo, this cut six LLM calls to one and about 40K tokens to 1.8K." [Source: newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md]

> "Jev is a building block that we can adjust … It might look less intelligent on its own, but with these strategies and patterns, we can get more intelligent" [Source: newsletter-rss-latent-space-2026-11-12-the-jev-revolution-what-engineers-are-already-bu.md]
