---
title: "Claude Fable 5.2 — effort levels, cost per task, and lane fit"
type: entity
related:
  - concepts/frontier-model-release-cadence.md
  - concepts/token-economics-and-prompt-caching.md
  - sources/newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md
  - entities/skills/route.md
  - sources/newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md
  - sources/newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md
  - concepts/reasoning-effort-calibration.md
updated: 2026-11-14
---

## Raw Concept

Prompted by the 2026-11-10 AINews ingest. The page exists so `/route` lane decisions cite a page, not a newsletter paragraph. All figures are vendor or third-party reported, not measured on this machine.

## Narrative

Released 2026-11-10 with Claude Mythos 5.2, on the same day Anthropic's IPO roadshow opened. Anthropic describes both as "a step above Opus 5.5 in almost all the capabilities we evaluated". The system card phrasing, "the model that underlies Claude Fable 5.2 and Claude Mythos 5.2", implies one shared base model. [TENTATIVE]

| Field | Value |
|-------|-------|
| Price | $8 / $40 per 1M input / output tokens |
| Cache | writes $10 (5-min TTL) or $16 (1-hour TTL); reads $0.20 |
| Context | 1M tokens, text and image input |
| Effort levels | low, medium (default), high, xhigh, max |
| Default in apps and Claude Code | medium |

### Independent scores

- Artificial Analysis Intelligence Index v5: first at 65.
- HLE-Diamond 80%, AA-Omniscience 67, Terminal-Bench-Science 73%, CritPt v2 hard 77%, FrontierCode 2.0 49%.
- Epoch Capabilities Index 174.
- ARC-AGI-3: 81.2% under the standard harness, 97.7% under the provider adapter harness.
- Weaker areas: AA-Briefcase 1785 Elo, GDP.pdf 24% all-pass (Opus 5.5: 26%), Terminal-Bench 4.0 60% (behind Kimi K3.1 Pro at 67%).

### Cost behaviour

Cheaper per token, more expensive per task. SemiAnalysis measured $88.15 per task on GDPx against $67.16 for Fable 5.1, a 31% rise, because the model wrote far more test cases and spawned verification subagents. At max effort, about $26.5 per task, roughly 2.6 times Opus 5.5.

At high and xhigh it scores 62 on the Intelligence Index using about 98K output tokens per task, against 173K for Opus 5.5 at max. High is the efficiency point.

### Agent Arena and pricing (reported 2026-11-12 to 2026-11-14)

Fable 5.2 ranks first on Agent Arena with a +30.4% net improvement across 4.7K sessions. That is about 1.6× Opus 5.5 at +19.5%. The lead grows on long tasks: 93% against 85% no-correction responses at 16 or more turns. [TENTATIVE — vendor leaderboard]

API price fell from $10/$50 to $8/$40 per 1M input/output tokens. Median cost per task is $7.3, against $5.5 for Opus 5.5, $1.5 for Gemini 4 Carbon at high, and $6.0 for GPT-6 Astra.

On the AA Coding Agent Index v2.1, Fable 5.2 and Opus 5.5 tie at 58. Fable at max costs $44.22 per task, while a cheap configuration costs $1.51. Medium, high, and xhigh all sit on the Pareto frontier.

### Route fit

- **Architect lane** — a candidate when Fable is available on plan. High effort is the sane default; max is a known cost trap.
- **Implementer lane** — no. The implementer lanes are Grok and Codex for cost and vendor diversity.
- **Do not carry old effort settings forward.** Vendor and Cursor guidance both say effort levels behave differently from 5.1. Start at default and measure.

Access limits matter for planning: Fable may consume at most 50% of a weekly limit, and data retention is on by default so safety classifiers can run, with zero retention only for eligible enterprise accounts.

## Snippets

> "Fable at High matched Opus 5.5 at Max for about half the cost per task." [Source: newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md]

> "don't talk about Fable at Max." [Source: newsletter-rss-latent-space-2026-11-10-ainews-fable-52-retakes-world-1-llm-spot-as-ant.md]
