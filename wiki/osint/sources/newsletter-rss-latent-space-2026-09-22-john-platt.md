---
title: "Latent Space — An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science"
type: source
tags: [newsletter, source, k270, ood, ai-for-science]
keywords: [k270, John-Platt, ERA, Google, scoreable-task]
related:
  - concepts/k270-ood-stub-wave.md
maturity: draft
created: 2026-09-23
updated: 2026-09-23
read_status: read
---

## Relations

- @concepts/k270-ood-stub-wave.md

## Raw Concept

| File | `newsletter-rss-latent-space-2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-your.md` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-your.md` |
| Title | 🔬 An Oscar, Two Asteroids, and the Algorithm in Your sklearn: John Platt on AI for Science |
| URL | https://www.latent.space/p/john-platt |
| Feed | latent-space |
| Retrieved | 2026-09-23 (published 2026-09-22) |
| Dual-ID | **OSINT K270** |
| sha256 | `1dcfc6433ca4c84bf09f4979f50bce0634596254d88000caeef418d7f5d42013` |

## Narrative

Interview with **John Platt** (Google). Platt has an Academy Award, two named asteroids, and two textbook machine-learning algorithms. The conversation covers Google's **Empirical Research Assistance (ERA)**, AI for climate change, and the co-evolution of science and AI.

Key point: Platt's team reduces many scientific problems to a **scoreable task**. Once a score function exists, the job is to find code that maximises the score. ERA keeps a running tree of past experiment notebooks and uses an **Upper Confidence Bound** rule (a close cousin of Monte Carlo Tree Search) to pick notebooks to mutate. Gemini proposes mutations, about ten at a time, and branch histories are shared. Platt notes a step change between Gemini 2.0 and 2.5, from not working to working well. Platt warns that ERA gives predictive models; the scientist must confirm they are descriptive. His line: "It's a power tool. It can slice your fingers off."

**Cemini relevance:** OOD signal only — AI-for-science harness pattern. **FILE only. 0 product Integrate GO. Do not swap `/route`. Never auto-evolve `.cursor/skills`.**

## Snippets

> "It's almost like having a hyper-eager grad student who doesn't sleep." [Source: newsletter-rss-latent-space-2026-09-22-an-oscar-two-asteroids-and-the-algorithm-in-your.md]
