---
title: "Latent Space AINews — Perplexity at a $1B run rate; Qwen4-Max ships"
type: source
related:
  - concepts/frontier-model-release-cadence.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/harness-layer-competition-cursor-claude-perplexity.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Perplexity hits a $1B revenue run rate, up 4x in 2026 |
| Author | Latent Space (AINews desk) |
| Type | Newsletter (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-17-ainews-perplexity-hits-a-1b-revenue-run-rate-up.md` |
| Retrieved | 2026-11-22 (published 2026-11-17) |
| Pages | n/a |
| Read status | read |

## Narrative

Two items matter for CCC.

**Perplexity** crossed a $1B annual revenue run rate, up from under $250M at the start of the year and over $750M by August. Its product line is agent-shaped: Computer runs recurring tasks and, in November, ongoing "Teammates"; the Monitor API watches a topic and posts a webhook on change; a new research lab has 10,000+ GPUs.

**Qwen4-Max** moved from preview to shipping. At the highest reasoning setting it scores 43 on the Intelligence Index, up from 34. Average cost per task fell from $10.02 to $3.27. Alibaba cut output price from $6 to $4.50 per million tokens, and the model writes about 39% fewer of them. Total parameters stay at 2.4T, with active parameters per token cut 25% to 71B. It has a 1M-token context window.

The cost-per-task fall is the harness-relevant number. It comes from fewer output tokens, not only a lower unit price. That is the pattern `@concepts/frontier-model-release-cadence.md` already records: compare cost per solved task, never cost per token.

A legal-benchmark caveat is also reported: Qwen4-Max gets 95.7% of checklist items right but passes only 21.3% of tasks, and output tokens rise 3.6×. Treat as [TENTATIVE]; these are third-party (HLAB) results.

## Snippets

> "At the highest reasoning setting, Qwen4-Max scored 43 on the Intelligence Index, up from 34. Average cost fell from $10.02 to $3.27 per task." [Source: newsletter-rss-latent-space-2026-11-17-ainews-perplexity-hits-a-1b-revenue-run-rate-up.md]
