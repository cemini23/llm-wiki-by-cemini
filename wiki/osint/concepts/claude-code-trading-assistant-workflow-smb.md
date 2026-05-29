---
title: Claude Code trading assistant workflow (SMB four-step)
type: concept
tags: [concept, claude-code, trading-workflow, dashboard, agentic-ai, k79]
keywords: [claude-code, plan-mode, build-mode, routines, html-dashboard, performance-coach, trade-journal]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-04-14.md
  - sources/smb-capital-youtube-week-2026-04-01.md
  - concepts/claude-code-skills-md-workflow.md
  - concepts/claude-ai-trading-operational-workflows-smb.md
  - concepts/pre-market-ai-research-briefing-smb.md
  - concepts/prop-desk-team-trading-collaboration.md
  - ccc-wiki/concepts/claude-code-skills-md-institutional-memory.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB trader (Garrett/Tim) walkthrough
- @sources/smb-capital-youtube-week-2026-04-14.md — primary source (Apr 2026 videos)
- @concepts/claude-ai-trading-operational-workflows-smb.md — five-practice operational layer (Mar 2026 video)
- @concepts/pre-market-ai-research-briefing-smb.md — morning briefing use case
- @concepts/prop-desk-team-trading-collaboration.md — playbook/personalization emphasis
- @ccc-wiki/concepts/claude-code-skills-md-institutional-memory.md — deeper Claude Code workflow home

## Raw Concept

What prompted this page: SMB Capital YouTube pair *4-Step Claude AI Trading Assistant* (2026-04-25) + *Build Your Own Claude AI Trading Assistant* (2026-04-18) — non-coder trader builds personal HTML performance dashboard in one afternoon.

## Narrative

SMB teaches **Claude Code desktop** (not chat-only Claude) for trader-built tooling. Output is typically a **local HTML dashboard** — custom TraderView-style stats, tagged setups, P&amp;L, mistake/tendency coach — updated by talking to the agent.

### Four-step workflow [TENTATIVE — SMB]

| Step | Mode | Action |
|------|------|--------|
| **1. Plan** | Plan mode (no file edits) | Brainstorm → concrete implementation plan (`.md` project brief) |
| **2. Build** | Build mode (accept edits) | Feed plan to Claude Code → skeleton dashboard / scripts |
| **3. Personalize** | Build + iterate | Custom tabs, stats, **coach layer** (mine trade write-ups for repeating mistakes) |
| **4. Routine** | Claude **Routines** (scheduled) | Daily prompts (e.g. 4:15 p.m. — "what trades today?") auto-update dashboard |

### Design principles (SMB)

- **Workflow > shiny dashboard** — same four steps apply to any trading tool; swap keywords in step-1 prompt.
- **Personalization requires trader context** — playbook, grading rules, checks-in-favor; generic builds stay generic.
- **Output quality = input quality** — coach/backtest layer only as good as trade logs, tags, and playbook data fed in [TENTATIVE].
- **Plan before build** — spend time in plan mode; prompting discipline matters more than model choice.

### Example coach use case [TENTATIVE]

At decision time (e.g. breakout close below level): agent queries tagged history — "70% of my breakout trends that closed above level worked; none below worked" → downgrade setup grade.

### Cemini relevance

- **Laptop / workflow only** — mirrors OSINT wiki + Claude Code curation pattern; not prod trading path.
- Steal-from for **analyst morning brief HTML** + **post-close review routine** — Conductor owns prod orchestration.
- Complements @concepts/claude-code-skills-md-workflow.md (Skills.md persistence) vs SMB's project/routine pattern.
- API/data wiring for live stats = `[NEEDS VERIFICATION 2026-05-29]` before prod-adjacent use.

## Snippets

> "These four steps, all you would replace is pretty much keywords in that first prompt." [Source: SMB Capital YouTube 45eaVU5NVi8, 2026-04-25]

> "It's all about the inputs, the quality of the data… that's going to then give it the power." [Source: SMB Capital YouTube 45eaVU5NVi8, 2026-04-25]
