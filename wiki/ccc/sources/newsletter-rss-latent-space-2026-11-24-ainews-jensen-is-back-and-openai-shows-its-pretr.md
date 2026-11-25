---
title: "Latent Space AINews 2026-11-24 — Jensen returns, OpenAI pretraining curve, Claude Ship"
type: source
related:
  - entities/tools/claude-code.md
  - concepts/frontier-model-release-cadence.md
  - concepts/model-vs-harness-performance-variance.md
updated: 2026-11-25
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Jensen Is Back! and OpenAI Shows Its Pretraining Curve, joined by Microsoft |
| Author | Latent Space (AINews) |
| Type | Newsletter (RSS, free tier) |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-24-ainews-jensen-is-back-and-openai-shows-its-pretr.mdnewsletter-rss-latent-space-2026-11-24-ainews-jensen-is-back-and-openai-shows-its-pretr.md
| Retrieved | 2026-11-24 |
| File | `newsletter-rss-latent-space-2026-11-24-ainews-jensen-is-back-and-openai-shows-its-pretr.md` |
| URL | https://latent.space/p/ainews-jensen-is-back-and-openai-shows-its-pretraining-curve-joined-by-microsoft/ |
| Read status | read |

## Narrative

An AI-news digest. Most items are model releases and policy. The items that touch this wiki concern harnesses.

**Claude Ship (beta).** Running `/ship` in Claude Code opens the PR, reviews it, and works through feedback and failing checks. Branch rules and permissions still decide what merges. Admins can enable it repo-wide. The approval policy is stored in the repo, described as a smarter CODEOWNERS file.

**Harness adapters.** Adapting Qwen3.8-27B to the Pi harness raised Terminal-Bench 2.1 from 39% to 55%, while using half the tokens. Reported on X, not a paper. [TENTATIVE]

**CoEvoBench (Alibaba).** Agents that improve model-harness pairs drew most of their gains from harness edits, not from training. This is the strongest pro-harness item in the digest. [TENTATIVE]

**Model releases.** Gemini 4 Neon sits between Carbon and Hydrogen. LiveBench 2.0 gives Neon 87.4, against 84.9 for Claude Fable 5.2 and GPT-6.2 Astra, at about a quarter of Fable's cost per task. Hydrogen costs $1.50 per million input tokens. OpenAI published a base-model log-perplexity curve back to GPT-3.5, with caveats on tokenizer bias and post-training compute share.

**Why it matters.** The `/ship` item is a direct change to the Claude Code harness this workspace uses. The CoEvoBench result argues that harness edits carry most of the gain in a model-harness co-evolution loop. That supports the harness-editing lane. All digest items are single-source and unverified. [TENTATIVE]

## Snippets

> "Claude Ship (beta): Running /ship in Claude Code opens the PR, reviews it, and works through feedback and failing checks." [Source: `newsletter-rss-latent-space-2026-11-24-ainews-jensen-is-back-and-openai-shows-its-pretr.md`, retrieved 2026-11-24]
