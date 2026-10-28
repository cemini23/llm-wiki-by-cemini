---
title: "AI SRE: What It Is, How It Changes On-Call, and Whether It Works"
type: source
tags: [source, pragmatic-engineer, sre, agents]
related: []
maturity: draft
read_status: read
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | AI SRE: what is it, how could it change on-call – and does it work? |
| Authors | The Pragmatic Engineer (Gergely Orosz), with Jessica |
| Feed | Pragmatic Engineer (https://newsletter.pragmaticengineer.com/feed) |
| File | `newsletter-rss-pragmatic-engineer-2026-10-27-ai-sre-what-is-it-how-could-it-change-on-call-an.md` |
| Retrieved | 2026-10-27 |
| URL | https://newsletter.pragmaticengineer.com/p/ai-sre |
| Published | 2026-10-27 |
| Read status | read (RSS teaser — full post may be paywalled) |

## Narrative

**History.** Microsoft introduced an "Azure SRE Agent" at BUILD in May 2025, with a demo where an alert fired and the agent found the root cause and shipped a fix without waking a human. The author doubted any team would let an AI make production decisions unsupervised, and heard nothing more for a year.

**Now.** The topic is live again. OpenAI built an AI SRE bot called Sevbot. An engineer at ING reports an in-house AI SRE. Vendor stands are appearing at conferences.

**The survey.** The newsletter spoke to three AI incident platforms: Rootly, incident.io, and ResolveAI. The author discloses an investment in incident.io.

**What "AI SRE" means in practice.** Mostly faster incident investigation, conducted inside Slack or Teams. Whether AI SREs should make code changes is actively debated.

**How teams build it.** Fanning out multiple agents is common, with engineers steering them in chat. A "context layer" holds a knowledge graph and memory to improve investigation. Several companies built their own investigation agents rather than buying.

**Why the topic is hot.** Incidents and pages are trending upward because AI agents speed up shipping to production. That increases on-call load, which creates the case for better on-call tooling.

**Why it matters.** Note the causal loop: agents increase deploy rate, deploy rate increases incidents, incident tooling becomes an agent problem. The article also draws a clear line between investigation (widely adopted) and autonomous remediation (debated).

## Snippets

> "It's mostly about doing incident investigation much faster, and inside of Slack. Whether 'AI SREs' should make code changes is debated." [Source: `newsletter-rss-pragmatic-engineer-2026-10-27-ai-sre-what-is-it-how-could-it-change-on-call-an.md`, retrieved 2026-10-27]
