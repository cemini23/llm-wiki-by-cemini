---
title: Grok Bot — persistent cloud AI teammates (SpaceXAI)
type: entity
tags: [tool, spacexai, agents, k241, operator]
keywords: [Grok Bot, cloud VM, skills, routines, templates, plugins]
related:
  - sources/xai-grok-bot-guides-index-2026-09-02.md
  - sources/x-post-mattyp-grok-bot-templates-2026-09-02.md
  - sources/x-post-irabukht-grok-bot-marketing-2026-09-02.md
  - sources/newsletter-rss-latent-space-2026-08-13-grok-46.md
  - sources/newsletter-rss-pragmatic-engineer-2026-08-14-meta-resignation-wave.md
  - sources/x-article-antpalkin-self-improving-ai-trading-machine-2026-08-06.md
  - sources/substack-rss-outlier-weekly-2026-08-18-cursor-route.md
  - concepts/grok-bot-operator-patterns.md
  - concepts/practical-loop-engineering.md
  - entities/people/antpalkin-cvxv666.md
  - sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md
  - concepts/k256-ccc-models-wave.md
maturity: validated
created: 2026-09-02
updated: 2026-09-14
harness_verb: FILE
wire_note: Operator charters in briefs/2026-09-01_grok-bot-charters.md (§1–16 plus §17–19 DFS/Parlays desks) — not prod wire
---

## Relations

- @sources/xai-grok-bot-guides-index-2026-09-02.md — official guide library
- @sources/x-post-mattyp-grok-bot-templates-2026-09-02.md — Templates launch (Matt Palmer)
- @sources/x-post-irabukht-grok-bot-marketing-2026-09-02.md — GTM/marketing community article (Ira Bodnar)
- @sources/newsletter-rss-latent-space-2026-08-13-grok-46.md — launch + Grok 4.6 training on harness trajectories
- @concepts/grok-bot-operator-patterns.md — Cemini operator synthesis
- @concepts/practical-loop-engineering.md — execution lane; not wiki author
- @entities/tools/cursor-route.md — public CLI; federation `/route` stays separate
- @sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md
- @concepts/k256-ccc-models-wave.md

## Raw Concept

SpaceXAI beta product: named persistent agents on a **user-scoped cloud VM** (browser, terminal, `/workspace`). Included on eligible SuperGrok and Cursor Pro+ plans; Bot usage meter is separate from Grok chat and Cursor Agent. Prompted operator entity from Sep 2026 guides + template-sharing launch.

## Narrative

| Field | Value |
|-------|--------|
| Product | https://x.ai/bot |
| Docs | https://docs.x.ai/grok-bot/overview |
| Guides | https://x.ai/bot/guides |
| Verdict | **Operator tool (FILE)** — Cemini charters in `briefs/2026-09-01_grok-bot-charters.md` (core + marketing + §17–19 slate/recap desks); not a CeminiSuite wire |
| Distinct from | Grok chat @ grok.com; federation `/route` + `cursor-route` CLI; `@bot` announcement account |

**Architecture (docs, retrieved 2026-09-02):** All Bots on one account share **one computer** — browser sessions, files, and CLI credentials are **not** isolated per Bot. Each Bot gets its own screen; parallel browser work is possible; security boundary is the **account**, not the Bot. Local Mac/Windows is separate unless local-computer policy is enabled.

**Primitives:** Description (profile) · **Skills** (saved task workflows) · **Routines** (scheduled or event-triggered re-runs) · **Plugins** (connectors/MCP; `@` in chat) · **Templates** (Aug 2026: share identity/skills/routines/plugins via `x.ai/bot/<id>` — recipient gets a **copy**, not creator logins or history).

**Cemini posture:** HITL on send/publish/delete/purchase; no Equifax/banks/1Password/Stripe/Discord/Atto on shared Bot VM; wiki ingest stays on laptop Cursor; Bot = discovery desk only for Drive Wiki Scout. DFS/Parlays desks (§8, §17–19) are research and recap only — no sportsbook submit, no Odds API key on the VM, no FanDuel Enter.

## Snippets

> "All of your Bots use the same persistent cloud computer. They share files, browser sessions, and app logins." [Source: https://docs.x.ai/grok-bot/overview (retrieved 2026-09-02)]

> "Adding creates a copy on their account" — templates do not give recipient your computer, logins, or conversation history. [Source: community summaries of docs.x.ai Create-and-manage-Bots; mattyp template article preview 2026-09-02]
