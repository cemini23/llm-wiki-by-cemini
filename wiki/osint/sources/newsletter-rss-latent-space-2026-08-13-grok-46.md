---
title: "Latent Space AINews — Grok 4.6 / Grok @Bot / Claude watermark rollout"
type: source
tags: [source, newsletter-rss, grok, models, ccc, k235]
keywords: [Grok 4.6, Grok Bot, SpaceXAI, SFT-trajectories, agentic-RL, Claude-watermark, Qwen3.8-Max, DeepSeek-V4-Pro]
related:
  - sources/newsletter-rss-latent-space-2026-07-09-grok-45-cursor.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
read_status: skimmed
---

## Relations

- @sources/newsletter-rss-latent-space-2026-07-09-grok-45-cursor.md — prior Grok 4.5 AINews issue (preingest LIKELY verdict resolved: different dated issue, proceed)
- @concepts/agent-toolkit-routing-research-backlog.md — K235 bump: Grok 4.6 harness training notes

## Raw Concept

| Field | Value |
|-------|--------|
| URL | https://www.latent.space/p/ainews-spacexai-grok-46-and-grok |
| Published | 2026-08-13 |
| sha256 | `c93a30ac41ad6cf7961c46644bb3b9ed8de85e90874992baa03b4eb699b5fd50` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-latent-space-2026-08-13-ainews-spacexai-grok-46-and-grok-bot.md` |
| retrieved | 2026-08-13 |

## Narrative

**Grok 4.6** (SpaceXAI) — confirmed 1.5T model, same price as 4.5, "second-best knowledge work model" by some rankings; AA Intelligence Index 61 (≈ GPT-5.6 Sol Max, behind Claude Opus/Fable), 88.4% Terminal-Bench v2.1, 1753 GDPval-AA v2 Elo; $2/$6 per 1M tokens. Training disclosure (quoted in full in the newsletter): longer supplemental run with curated model-generated data; **Grok 4.5 regenerated SFT trajectories across reasoning efforts, agent harnesses, STEM/SE/knowledge-work domains**, problematic traces filtered with model-based checks; **agentic RL on knowledge work, coding, kernel optimization, webdev, CAD**. Grok 4.7 already in flight (SpaceX internal data supplemental). Cursor→SpaceX team shipped Grok @Bot (AI teammate space; Claude Tag mixed reviews).

Same issue: **Claude text watermarking rollout** — models launched ≥ 2026-08-02 embed imperceptible model-level text watermarks intended to survive copy-paste; .png/.jpg/.svg carry signed C2PA provenance; robustness degrades under paraphrasing/local-LLM rewrite (SynthID-Text-style keyed sampling bias, z-score detection). Directly relevant to the watermarks-remover eval in this batch's docx. Frontier model wave: Qwen3.8-Max open weights (2.4T/95B MoE, text-only), DeepSeek V4 Pro GA ($0.435/$0.87 per M), MAI-Thinking-1 (Microsoft). Harness-over-model theme recurs (Scott Stevenson: RAG + harness engineering beat training).

Routing: CCC /route brief (long-running agents, SFT-from-harness-trajectories recipe); no prod brief.

## Snippets

> "We then used Grok 4.5 to regenerate the SFT trajectories across reasoning efforts, agent harnesses, and domains such as STEM, software engineering, and knowledge work, and filtered out problematic traces with model-based checks." [Source: xAI via Latent Space AINews 2026-08-13]
