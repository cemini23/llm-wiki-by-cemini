---
title: "Pragmatic Engineer — Scaling Slack and GitHub with Maude Lemaire"
type: source
related:
  - concepts/foundational-work-verification.md
  - concepts/ai-native-engineering-curriculum.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Scaling Slack and GitHub with Maude Lemaire |
| Author | The Pragmatic Engineer (Gergely Orosz, interview) |
| Type | newsletter / podcast notes (RSS) |
| Location | `research to be indexed/newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-05 |
| Read status | read |

## Narrative

Maude Lemaire is a principal engineer and author of *Refactoring at Scale*. She led backend performance infrastructure at Slack for nearly eight years, worked on database scaling at GitHub, and most recently worked on Cursor performance, including time to first token.

The ccc-relevant item is her rule for AI use. For platform work she personally verifies everything an LLM gives her, because ambitious structures need stable foundations. She separates **foundational** work from **non-foundational** work, and gives the first much more attention.

Other items in the episode are general engineering lessons, recorded here for completeness:

- Slack limits custom emojis to 23 to avoid thundering-herd fan-out costs.
- Event floods overwhelm power users whose single WebSocket carries many busy channels.
- The Koi Pond load test replaced headless-Chrome sessions with slim Go clients. The naive approach would have cost about $150,000 per run.
- GitHub could not exceed 16 database shards because Active Record produced scatter queries without a primary key.
- Platform and product engineers should rotate, so platform work stays connected to product experience.

One harness-adjacent observation: Cursor hires engineers who work on time to first token. Prefill latency is a product feature, not only an infrastructure metric — the same conclusion the Visual Token Routing paper reaches from the model side.

## Snippets

> "When doing foundational work, Maude pays close attention to verifying the output of LLMs because she believes that ambitious structures can only be built on stable foundations." [Source: newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md]

> "It's an interesting approach to separate 'foundational' and 'non-foundational' work in order to give more attention to the former, most critical, type." [Source: newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md]
