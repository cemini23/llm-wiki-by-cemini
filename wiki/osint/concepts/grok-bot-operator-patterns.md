---
title: Grok Bot operator patterns (Cemini + official guides)
type: concept
tags: [concept, grok-bot, operator, harness, hitl]
keywords: [templates, shared computer, project channel, routines, approvals]
related:
  - entities/tools/grok-bot.md
  - sources/xai-grok-bot-guides-index-2026-09-02.md
  - sources/x-post-mattyp-grok-bot-templates-2026-09-02.md
  - sources/x-post-irabukht-grok-bot-marketing-2026-09-02.md
  - concepts/practical-loop-engineering.md
  - sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md
maturity: draft
created: 2026-09-02
updated: 2026-09-14
---

## Relations

- @entities/tools/grok-bot.md
- @sources/xai-grok-bot-guides-index-2026-09-02.md
- @concepts/practical-loop-engineering.md — loop/harness discipline; Grok Bot is execution lane not wiki author
- @seo-wiki/concepts/generative-engine-optimization.md — GEO Audit Collector bot aligns here
- @seo-wiki/concepts/x-account-voice-and-format.md — X Account Eval / X Desk scoring contract
- @sources/newsletter-rss-latent-space-2026-09-05-grok-bot-openclaw-2026-09-07.md

## Raw Concept

Synthesis of xAI Grok Bot guides (Aug–Sep 2026), template-sharing launch, and Cemini `briefs/2026-09-01_grok-bot-charters.md` (8 core bots + optional §9 Project Ops + §10–16 marketing suite + §17–19 DFS/Parlays slate and recap desks).

## Narrative

### Pattern map (official → Cemini)

| Official pattern | Guide / source | Cemini charter alignment |
|------------------|----------------|---------------------------|
| One shared cloud computer per account | docs overview, computer-and-apps | **Risk:** File desk + Inbox Cut + GEO share cookies — enforce login denylist on VM |
| Skills from demonstration | GTM guide, designing guide | Matches pasted **First skill** blocks; UI "record workflow" is equivalent |
| Routines after proven manual run | Nate Herk / godofprompt community; our brief | **Keep:** no routine until one clean manual run |
| Templates (share link) | @bot Aug 2026; mattyp Sep 2026 | **New path:** publish sanitized charters as templates vs copy-paste only |
| Project channel + roster | Eric Zakariasson multi-team guide | **Brief §9 Project Ops** — Notion meta; max ~6 bots per channel |
| Chief of Staff orchestrator | GTM guide | We use **separate** narrow bots instead — OK; consider CoS for mention+desk only |
| Plugin `@` attach | docs; X integration Aug 29 | X Account Eval / X Desk already specify `@` X |
| Blocked task → ping human | multi-team Notion pattern | Same as "hand me the computer" in charters |
| Evidence / deliverable to disk | GTM weekly media rundown | Matches `/workspace/<bot>/YYYY-MM-DD.md` convention. Slate/recap desks write `environment.csv`, `ledger.csv`, `tool-gaps.md` — laptop CLI still owns fetch/compose/grade |

### Template hygiene (Sep 2026 launch)

Templates bundle **instructions, skills, routines, plugins** (and optionally selected memories per product walkthrough). They **exclude** cloud computer, logins, and chat history. Treat third-party templates like untrusted skills: strip API keys, internal URLs, customer PII before publish; one safe test run before enabling routines that send/publish/pay. [TENTATIVE] Community guidance: 0–2 routines, event trigger over polling, weekday daytime default.

### Multi-bot coordination options

1. **Separate chats (current Cemini default)** — core + marketing + DFS/Parlays desks; operator routes manually. Slate desks before lock; recap desks after.
2. **Group channel** — GTM pattern: X Desk + X Account Eval + CoS in one thread for one account week.
3. **Notion Projects/Tasks + PM bot** — experimental (Zakariasson); overkill unless running client GEO projects at scale.

### What not to wire

- No autonomous wiki write from Bot (Drive Wiki Scout → laptop `preingest_check.py` only).
- No trading egress, Discord LIVE, prod `/opt/cemini`, or GuruWatcher from Bot VM.
- No replacement of federation `/route` or `cursor-route` for code implementation.
- No Odds API key, sportsbook submit, or FanDuel Enter from DFS/Parlays desks. Recap writes `tool-gaps.md`; laptop applies CLI/repo changes.

## Snippets

> "Reuse existing bots first… Create a new bot only when nothing on the bench fits, and only after I say yes." [Source: x.ai/bot/guides/how-i-run-multiple-teams-of-grok-bots (retrieved 2026-09-02)]

> "Templates contain the skills, memories, and official @bot plugins from your bots. When you use a template, you get a copy" [Source: X Article preview, mattyp 2094833468400447618 (retrieved 2026-09-02)]
