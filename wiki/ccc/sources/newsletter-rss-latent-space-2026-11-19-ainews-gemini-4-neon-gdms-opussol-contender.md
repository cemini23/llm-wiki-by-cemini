---
title: "Latent Space AINews — Gemini 4 Neon, a mid-tier Opus/Sol contender"
type: source
related:
  - concepts/frontier-model-release-cadence.md
  - concepts/reasoning-effort-calibration.md
  - concepts/token-economics-and-prompt-caching.md
updated: 2026-11-22
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Gemini 4 Neon: GDM's Opus/Sol Contender |
| Author | Latent Space (AINews desk) |
| Type | Newsletter (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-19-ainews-gemini-4-neon-gdms-opussol-contender.md` |
| Retrieved | 2026-11-22 (published 2026-11-19) |
| Pages | n/a |
| Read status | read |

## Narrative

Google DeepMind shipped Gemini 4 Neon, the fourth Gemini 4 model in about seven weeks. Argon is already retired. The names track atomic number: Carbon (6), Neon (10).

Pricing is $3 input, $0.15 cached input and $15 output per million tokens, with a 1M-token context window and four effort levels. Vals reports a maximum output limit of 1M tokens.

Results:

- At high effort, Neon matched Carbon's 60 on the Intelligence Index for $3.74 per task.
- On Agent Arena it debuted second with 1,336 points across about 4,200 sessions, at a $2.82 median task cost, and placed second on steerability.
- On the Vals Index it placed second at 70.9%, about 0.4 points behind Fable 5.2 at less than half the cost per task.
- On Code Migration it averaged 160 turns, fewer than Carbon's 234 or Hydrogen's 574, and scored below both.

Day-one integrations include Cursor, GitHub Copilot across app, CLI and VS Code, and LangChain Managed Deep Agents.

Two CCC lessons. Release cadence is now weeks, so a model pin ages fast. And effort levels again change the score: high matched Carbon at a fraction of the cost, while xhigh scored lower on GDP.pdf (28.0% against 33.4%). See `@concepts/reasoning-effort-calibration.md`.

## Snippets

> "At high effort, Neon matched Carbon's 60 on the Intelligence Index for $3.74 per task." [Source: newsletter-rss-latent-space-2026-11-19-ainews-gemini-4-neon-gdms-opussol-contender.md]

> "Neon placed second on the Vals Index at 70.9%, about 0.4 points behind Fable 5.2 at less than half the cost per task." [Source: newsletter-rss-latent-space-2026-11-19-ainews-gemini-4-neon-gdms-opussol-contender.md]
