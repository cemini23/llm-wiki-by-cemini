---
title: "Reasoning effort calibration — a higher tier beats a higher effort setting"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md
  - sources/newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md
  - entities/models/claude-fable-5-2.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/decision-model-hybrid-agent-routing.md
updated: 2026-11-14
---

## Raw Concept

What question does this page answer: when a task needs more capability, should the harness raise the effort level or move to a stronger model? Sources: the 2026-11-12 D-Day and 2026-11-14 AINews newsletters, plus the Fable 5.2 page.

## Narrative

Effort is a dial, not a free upgrade. Reported evidence from November 2026:

| Setting | Reported result |
|---------|-----------------|
| Claude line, one tier up at lower effort | Opus 5.5 at xhigh beats Sonnet 5.5 at max, with 40% lower cost per task |
| Fable 5.2 | high is often cheaper and better than xhigh or max |
| Fable 5.2, high and xhigh | both 62 on the Intelligence Index, about 98K output tokens per task |
| DeepSeek-V4.1-Flash, high effort | 28% more expensive, no gain outside noise |
| GLM-5.3-Flash, high effort | +5.8 percentage points |

Two of the five rows show no gain, or a loss. The effect is model-specific and it is not monotonic.

The practical rules:

1. **Set a cost ceiling per task before the run**, and measure against it.
2. **Test the effort ladder once per model**, then pin the setting. Do not carry settings across model versions; both vendor and Cursor guidance say the levels behave differently from one release to the next.
3. **Prefer a tier change to an effort change** when quality is short and the budget is fixed. On the reported numbers, a tier change buys more per dollar in the Claude line.
4. **Treat max as a known cost trap** unless a measurement justifies it. Fable 5.2 at max reached $44.22 per task on the AA Coding Agent Index, against $1.51 for a cheap configuration.

Cost per task is the comparison unit. Cost per token hides the difference, because a high effort setting can emit several times more tokens for the same answer.

For Cemini: `/route` picks a lane. This page adds a second decision inside the lane: the effort level. Record both in the run log, so a later postmortem can tell a lane failure from an effort failure.

## Snippets

> "moving up a model tier beats raising effort: Opus 5.5 at xhigh outscores Sonnet 5.5 at max with 40% lower cost per task" [Source: newsletter-rss-latent-space-2026-11-12-ainews-d-day-decision-models-day.md]

> "high effort makes DeepSeek-V4.1-Flash 28% more expensive with no gain within noise" [Source: newsletter-rss-latent-space-2026-11-14-ainews-the-no-ai-slop-manifesto.md]
