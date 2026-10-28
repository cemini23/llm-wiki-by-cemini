---
title: "Supabase's Plan for a Billion AI-Built Apps"
type: source
tags: [source, latent-space, backend, agents]
related: []
maturity: draft
read_status: read
created: 2026-10-27
updated: 2026-10-27
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Supabase's Plan for a Billion AI-Built Apps |
| Authors | Paul Copplestone and Ant Wilson (Supabase co-founders), interviewed by swyx |
| Feed | Latent Space (https://www.latent.space/feed) |
| File | `newsletter-rss-latent-space-2026-10-26-supabases-plan-for-a-billion-ai-built-apps.md` |
| Retrieved | 2026-10-27 |
| URL | https://latent.space/p/supabase_s_plan_for_a_billion_ai-built_apps/ |
| Published | 2026-10-26 |
| Read status | read |

## Narrative

The interview's premise is that AI agents write more software, and that changes what a backend must do.

Three themes:

- **Long-lived workloads beside the database.** Supabase Compute runs workloads next to the database instead of beside it.
- **Schemas that agents can understand.** The founders discuss making schemas easier for agents to read, which matters when an agent inspects a database to write a query.
- **Infrastructure for many more applications.** If one agent can produce a hundred apps, the per-app fixed cost has to fall.

Other topics: Postgres reliability and scaling, the acquisition of Turso as a scale-out opportunity, open source and community-led distribution, and how Supabase uses AI internally. Multigres, a highly available Postgres infrastructure product, is in private alpha.

Recorded ahead of Supabase Select 2026.

**Why it matters.** The agent-readable-schema point is the transferable one. An agent that cannot infer the data model from the schema will guess, and a guess against a production database is expensive. Schema design becomes an agent-interface design problem.

## Snippets

> "AI agents are creating more software—and that changes what a backend needs to do." [Source: `newsletter-rss-latent-space-2026-10-26-supabases-plan-for-a-billion-ai-built-apps.md`, retrieved 2026-10-27]
