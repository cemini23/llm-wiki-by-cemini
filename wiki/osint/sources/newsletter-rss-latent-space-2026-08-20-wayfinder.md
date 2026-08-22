---
title: "Latent Space — Matt Pocock /wayfinder skill (map, ticket, session, fog of war)"
type: source
tags: [ccc, skills, planning, harness]
keywords: [wayfinder, grill-me, fog-of-war, map, ticket, session, Pocock, AFK]
related:
  - concepts/wayfinder-fog-of-war-planning.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/wayfinder-fog-of-war-planning.md
- @concepts/skill-misevolution.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept
- **title:** The /wayfinder Skill: Navigating the “Fog of War” of Planning
- **author:** Latent Space interview with Matt Pocock (AI Skills for Real Engineers)
- **type:** newsletter / interview
- **location:** research to be indexed/newsletter-rss-latent-space-2026-08-20-the-wayfinder-skill-navigating-the-fog-of-war-of.md
- **retrieved:** 2026-08-20
- **pages:** full interview
- **read-status:** skimmed

## Narrative
Pocock’s pain: AFK/overnight agents need specs→tickets, but the planning session itself burns context. `/wayfinder` is an orchestrator that splits planning into child sessions (prototype, research, grill, human-only task) and merges them into a richer spec for an AFK run.

Named artifacts (leading words): **map** (decisions already made + overview), **ticket** (the child session’s task), **session**. Inconsistent labels confuse the agent. He is building a shared AI-coding dictionary so skills share the same leading words — ubiquitous language as context management.

**Fog of war:** you cannot specify everything at t=0. A few decisions reveal the next ring of the map (Warcraft III). Gate: `/grill-me` when the path fits in one session (most small features); `/wayfinder` when unknown unknowns are ahead.

Steal for CCC: copy map/ticket/session split and the grill-me vs wayfinder gate so AFK runs get a mergeable map instead of one giant spec. Propose-only this wave (no skill file edit). Complements Osmani’s label state machine (queue+lock) and BPS (set-level skill select).

## Snippets
> /wayfinder helps you navigate “the fog of war,” where you have a project but “you can’t quite decide everything right at the start.” [Source: https://www.latent.space/p/wayfinder-skill (retrieved 2026-08-20)]

> You’ve got the map, and you’ve got the ticket, and you’ve got the session. … if you just call everything a ticket, or if you just refer to it in different ways in different places, then [the agent is] going to be really confused. [Source: https://www.latent.space/p/wayfinder-skill (retrieved 2026-08-20)]

> Use ‘grill me’ in cases where you feel like you can plan the whole thing in a single session … Use /wayfinder when you can feel unknown unknowns ahead. [Source: https://www.latent.space/p/wayfinder-skill (retrieved 2026-08-20)]
