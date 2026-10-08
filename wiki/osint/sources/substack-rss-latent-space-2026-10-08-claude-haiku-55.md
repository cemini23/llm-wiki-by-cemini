---
title: "Latent Space — Claude Haiku 5.5: the cheap worker tier (2026-10-08)"
type: source
tags: [source, k285, llm, anthropic, ccc, model-pricing]
keywords: [haiku-5-5, gpt-6-luna, sonnet-5-5, tiered-pricing, subagent, effort-settings, terminal-bench, osworld]
related:
  - concepts/k285-feeds-wave.md
  - concepts/agent-cost-routing-model-orchestra.md
maturity: draft
created: 2026-10-08
updated: 2026-10-08
read_status: read
---

## Relations

- @concepts/k285-feeds-wave.md
- @concepts/agent-cost-routing-model-orchestra.md

## Raw Concept

| Title | [AINews] Claude Haiku 5.5 — better than GPT-6 Luna at the same pricing |
| Source | Latent Space (AINews), Substack |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-10-08-ainews-claude-haiku-55-better-than-gpt-6-luna-at.md` |
| Retrieved | 2026-10-08 |
| URL | https://www.latent.space/p/ainews-claude-haiku-55-better-than |
| Tier | free (RSS teaser) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

**Claude Haiku 5.5** — Anthropic's first Haiku-tier update in about a year, priced to match **GPT-6 Luna**. Anthropic called it "the cheapest, fastest, and most capable small model we've ever released," ~**75% cheaper to run on average** than Haiku 4.5.

### Position and pricing

Anthropic positions it as a **subagent** under Opus 5.5 or Sonnet 5.5 — "Opus does the heavy thinking, Haiku does the high-volume work." **Tiered pricing:** under 100K tokens **$0.10 / $0.50** per M (cache reads $0.01); over 100K **$0.50 / $2.50** (cache reads $0.05). Sonnet 5.5 cache reads were halved ($0.20 → $0.10) the same day.

### First Haiku with effort control

- **Effort settings + adaptive thinking** (first Haiku).
- **1M-token context** (up from 200K for 4.5).
- Artificial Analysis **Intelligence Index 43** at max effort (**+26**); ahead of GLM-5.3 Flash (42), Gemini 3.8 Flash (41), GPT-6 Luna (38); trails Sonnet 5.5 (56) by 13.
- **Terminal-Bench 4.0: 33%** (up from **0%** for Haiku 4.5). Vendor claims **OSWorld 15% → 72%**; independently **33%** on Terminal-Bench.

### The caveats (the useful part)

- **Token usage offsets the price cut:** ~**162k output tokens** per Index task at max effort — roughly **3× GPT-6 Luna** at max (~50k). Going xhigh→max adds 2 points for ~1.8× tokens.
- **Prompts over 100K tokens pay 5× more** — a real cost for long-context agent loops. That gap explains why Cursor's "10× cheaper on short requests" differs from Anthropic's "75% cheaper on average."
- Weaker **factual recall** than Gemini 3.8 Flash and Luna; a **pre-release over-refusal bug** depresses the automation score.

### Why it matters here

The **cheap-worker tier** in a multi-model harness is now explicit and priced — the same shape the wiki's `/route` and cost-routing thread assumes. The **tiered pricing and 3× token caveat** are the numbers to keep when sizing a route. **No `/route` swap** — the policy stands.

## Snippets

> "Opus does the heavy thinking, Haiku does the high-volume work." [Source: substack-rss-latent-space-2026-10-08-claude-haiku-55.md]

> "At max effort it uses about 162k output tokens per Index task, roughly 3x GPT-6 Luna at max (~50k)." [Source: substack-rss-latent-space-2026-10-08-claude-haiku-55.md]
