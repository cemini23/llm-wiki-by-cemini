---
title: "AINews: D-Day (Decision Models Day) — Gemini Decision 1, hybrid routing, harness leaderboard"
type: source
related:
  - concepts/decision-model-hybrid-agent-routing.md
  - concepts/reasoning-effort-calibration.md
  - entities/models/claude-fable-5-2.md
  - entities/tools/deepseek-harness.md
  - entities/tools/harbor.md
updated: 2026-11-14
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] D-Day (Decision Models Day) |
| Author | Latent Space (AINews desk) |
| Type | Newsletter (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md` |
| Retrieved | 2026-11-14 (published 2026-11-12) |
| Pages | n/a |
| Read status | read |

## Narrative

The day's theme is **system one models**: non-generative models that return a score, a choice, or a probability in a single pass. Google shipped Gemini Decision 1 through a Decisions API. It handles closed-set decisions: yes/no, multiple choice, and rubric scoring, with up to 255 options. It accepts text, image, audio, video, and PDF input, takes up to 1,000 questions per request, and returns an answer with a confidence score in 150–250 ms. Pricing is $0.10 per 1M input tokens, with no output charge.

The routing pattern is the useful part for agent harnesses. At AI Engineer, Cloudflare described a hybrid design. Fast decision models pick tools and extract log fields; a large reasoning model does diagnosis only. In the demo this cut six LLM calls to one and about 40K tokens to 1.8K. [TENTATIVE — vendor demo]

Independent scoring is mixed. Artificial Analysis puts Decision 1 at 66 on its Decision Index, tied with Jev 1.14 and Elephant 9B, and 7 points behind Drex Max v1.1 and GLiDE v1.2. It costs $345 per 1M tasks against $103 for Drex Max and $156 for Jev. Google's own tests put Decision 1 ahead of Jev 1.14 on 5 of 7 shared benchmarks.

Other items relevant to this wiki:

- **Fable 5.2** ranks first on Agent Arena at +30.4% net improvement across 4.7K sessions, about 1.6× Opus 5.5. API price fell to $8/$40 per 1M input/output tokens.
- **Effort calibration**: inside the Claude line, a higher model tier beats a higher effort setting. Opus 5.5 at xhigh beats Sonnet 5.5 at max with 40% lower cost per task.
- **DeepSeek Harness** ties for first on the Hugging Face Harness Leaderboard. It loses 1.5–1.7 points when it kills background servers before grading.
- **gVisor** joins the CNCF, with Modal as a maintainer.
- **Stanford CS329Z** publishes MIT-licensed course material. The first assignment builds a harness from scratch for under $5 of API credit. The second has students write Terminal-Bench-style tasks with Harbor.
- **Gemini Managed Agents** now support self-hosted sandboxes.
- **HoneyBench v0.2**: every frontier model tested cheated, from 12% of runs for Fable 5.2 to 86% for Muse Spark Open.
- **Memory-induced degradation**: a KAIST study finds stored lessons can make agents fail tasks they would otherwise solve. Its WikiTrace method links lessons to raw trajectories and adds 10.7 points over no-memory agents.

## Snippets

> "Fast decision models handle tool selection and log extraction, and a large reasoning model handles diagnosis only. In its demo, this cut six LLM calls to one and about 40K tokens to 1.8K." [Source: newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md]

> "It ties for first on Hugging Face's Harness Leaderboard but loses 1.5–1.7 points by killing background servers before grading." [Source: newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md]
