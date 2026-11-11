---
title: "Latent Space — why agents pick Resend: AEO measured"
type: source
tags: [source, newsletter, aeo, agent-discoverability, developer-tools]
related:
  - "@osint-wiki/entities/tools/agentdiscoverability-track.md"
maturity: draft
read_status: skimmed
created: 2026-11-11
updated: 2026-11-11
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Designing for Agents — Zeno Rocha, Resend |
| Source | latent-space (podcast) |
| Published | 2026-11-10 |
| Read status | skimmed (opening) |

## Narrative

**The concrete numbers behind "agents recommend what they read", which is the first time this workspace has seen them.**

The setup is a real puzzle: the hosts use Cloudflare Email — their domains are already on Cloudflare, so there is a home bias — and **agents keep suggesting Resend instead.**

### The study

In one AEO study, **Claude Code picked Resend first in 64 of the 102 email recommendations** the researchers could extract. **SendGrid came first seven times, but appeared as an alternative 55 times.**

Then the question that matters: **if a developer asks an agent to implement email and accepts the patch, how often does anyone try the second choice?**

That is the whole economics of agent discoverability in one sentence. A second-place recommendation is worth almost nothing, because the first answer is the one that gets implemented.

A more recent, comprehensive study was **more competitive — Postmark came top for most models** — which is itself informative: the ranking is not a fixed property of a vendor, it moves.

### Why it is filed here

This is the same thread as `agentdiscoverability-track` from the 2026-11-02 batch, now with measurements instead of a framework. Found → Picked → Positioned, with numbers: found often, picked 63% of the time, and a rival positioned second 55 times and almost never chosen.

For Atto's portal work, the implication is blunt: **being listed is not being used.** The first recommendation wins, and the second is a footnote.

**Caveat.** Newsletter summary of two studies, neither read here. Numbers are as quoted.

## Snippets

> "Claude Code picked Resend first in 64 of the 102 email recommendations the researchers could extract. SendGrid came first seven times, yet showed up 55 times as an alternative." [retrieved 2026-11-11]

> "If the developer asks an agent to implement email and accepts the patch, how often does anyone get around to trying the second choice?" [retrieved 2026-11-11]

## Dead Ends

- **Citing a fixed ranking.** The follow-up study put Postmark on top for most models.
