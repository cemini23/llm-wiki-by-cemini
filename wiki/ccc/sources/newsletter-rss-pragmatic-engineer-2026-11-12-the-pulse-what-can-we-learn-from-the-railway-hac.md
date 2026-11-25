---
title: "The Pragmatic Engineer — Railway hack postmortem teaser (abliterated models)"
type: source
maturity: draft
related:
  - concepts/model-is-not-a-security-boundary.md
  - concepts/tools-we-dont-use.md
  - sources/newsletter-rss-pragmatic-engineer-2026-06-30-impressions-from-visiting-openai-anthropic-curso.md
  - sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md
  - sources/newsletter-rss-pragmatic-engineer-2026-07-28-inside-anthropic.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-27-ai-sre-what-is-it-how-could-it-change-on-call-an.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-29-software-engineering-at-google-cs-education-with.md
  - sources/newsletter-rss-pragmatic-engineer-2026-10-30-the-pulse-anthropic-kills-the-coding-interview.md
  - sources/newsletter-rss-pragmatic-engineer-2026-11-03-tenfold-prs-2026-11-03.md
  - sources/newsletter-rss-pragmatic-engineer-2026-11-10-correctness-supply-chain-2026-11-11.md
updated: 2026-11-14
read_status: read
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | The Pulse: What can we learn from the Railway hack? |
| Author | The Pragmatic Engineer |
| Type | Newsletter (RSS teaser; full post may be paywalled) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-pragmatic-engineer-2026-11-12-the-pulse-what-can-we-learn-from-the-railway-hac.md` |
| Retrieved | 2026-11-14 (published 2026-11-12) |
| Pages | n/a |
| Read status | read (teaser only) |

## Narrative

The teaser only reports one item. Cloud platform Railway published a detailed postmortem of a recent hack. The attacker likely used **abliterated** AI models, meaning models with safety training removed. Railway hardened its systems in response. The full post is behind the Substack paywall, so this page holds the claim without the technical detail. [TENTATIVE]

The relevance to this wiki is narrow and it is a policy point, not a harness point. An abliterated model is not a boundary. A security control that depends on model refusal fails when the model has no refusal. Cemini already treats the model as outside the security boundary; this incident is a public example of that rule.

Do not cite the postmortem detail from this page. Read the Railway postmortem directly before using any specific claim about access path, timing, or remediation. [OPEN QUESTION 2026-11-14 — needs the primary postmortem]

## Snippets

> "the attacker likely used 'abliterated' AI models (those with no safeguards). Railway has hardened its syst…" [Source: newsletter-rss-pragmatic-engineer-2026-11-12-the-pulse-what-can-we-learn-from-the-railway-hac.md — teaser text, truncated in the feed]
