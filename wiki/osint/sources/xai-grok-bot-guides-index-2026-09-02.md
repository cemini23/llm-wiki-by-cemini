---
title: "xAI Grok Bot Guides — index + deep-read summaries (Sep 2026)"
type: source
tags: [source, grok-bot, spacexai, operator]
keywords: [guides, multi-team, GTM, design, templates]
related:
  - entities/tools/grok-bot.md
  - concepts/grok-bot-operator-patterns.md
  - sources/x-post-mattyp-grok-bot-templates-2026-09-02.md
  - sources/x-post-irabukht-grok-bot-marketing-2026-09-02.md
maturity: validated
created: 2026-09-02
updated: 2026-09-02
read_status: deep-read
---

## Relations

- @entities/tools/grok-bot.md
- @concepts/grok-bot-operator-patterns.md
- @sources/x-post-mattyp-grok-bot-templates-2026-09-02.md
- @sources/x-post-irabukht-grok-bot-marketing-2026-09-02.md

## Raw Concept

| Field | Value |
|-------|--------|
| URL | https://x.ai/bot/guides |
| Type | Official operator guide library |
| Retrieved | 2026-09-02 |
| read_status | deep-read (index + three guides full text; two others title-only) |

## Narrative

Hub lists practical playbooks (Aug 2026–Sep 2026): mobile app dev (Aug 25), designing with Grok Bot (Aug 24), GTM (Aug 16), multi-team coordination (Aug 27). Complements `docs.x.ai/grok-bot/*` (overview, computer-and-apps).

**Multi-team (Aug 27)** — Author pattern: Notion **Projects** + **Tasks** DBs; **Projects Manager** bot with "Project Ops" skill creates project → sidebar channel → staffs roster. Rules: reuse bench bots first; ≤5 specialists + PM (6 cap); new bot only with human yes. PM watches; tasks move Blocked → ping human. [Source: how-i-run-multiple-teams-of-grok-bots]

**GTM (Aug 16)** — Enterprise stack: Salesforce, Gmail, Calendar, Slack, Notion, Granola, Gong, Figma, X, LinkedIn, warehouse. Bot roster: Chief of Staff, prospecting (overnight), per-account customer expert, data analysis, product/10x engineer, 1:1, forecasting, slides (Figma + live Granola update), sales coach. Skills: record demo → skill; anti-slop skill; parallel cloud agents; group chat delegation (CoS → slides bot). Includes paste-ready **weekly media rundown** prompt with state file for dedupe. [Source: grok-bot-for-gtm]

**Design (Aug 24)** — Figma MCP for exact layout; specialized bots (Figma Bro, Motion God, Experiments, Devbot) delegate subtasks; judgment stays human; prototypes need not ship. [Source: designing-grok-bot-with-grok-bot]

**Docs cross-cut (retrieved 2026-09-02):** Persistent VM; `/workspace` for durable files; connectors = Plugins account-wide; take over for password/2FA/CAPTCHA/payment; template sharing documented separately (see mattyp source).

## Snippets

> "Each project gets a Grok Bot channel and an entry in a Notion database." [Source: https://x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots (retrieved 2026-09-02)]

> "Onboard Grok Bot like a new teammate… ask the agent to record, take over the computer and demonstrate, then have it turn the recording into a skill." [Source: https://x.ai/bot/guides/grok-bot-for-gtm (retrieved 2026-09-02)]
