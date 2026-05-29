---
title: Pre-market AI research briefing (SMB email workflow)
type: concept
tags: [concept, pre-market, research-ops, claude-code, automation, k79]
keywords: [pre-market-briefing, email-ingestion, market-rundown, stocks-in-play, economic-calendar]
related:
  - entities/organizations/smb-capital.md
  - sources/smb-capital-youtube-week-2026-04-14.md
  - concepts/claude-code-trading-assistant-workflow-smb.md
  - concepts/claude-ai-trading-operational-workflows-smb.md
  - concepts/prop-desk-team-trading-collaboration.md
maturity: draft
created: 2026-05-29
updated: 2026-05-29
---

## Relations

- @entities/organizations/smb-capital.md — SMB trader demo
- @sources/smb-capital-youtube-week-2026-04-14.md — `sh5h0GJzjNk` walkthrough
- @concepts/claude-code-trading-assistant-workflow-smb.md — same Claude Code stack
- @concepts/prop-desk-team-trading-collaboration.md — theme tracking + catalyst catalog parallel

## Raw Concept

What prompted this page: SMB Capital YouTube *I Automated My Pre-Market Research With AI* (2026-04-14) — weekday workflow before 8:30 a.m. ET synthesizing research emails into markdown + HTML dashboard.

## Narrative

**Problem:** ~1 hour manually reading scattered research newsletters before the open.

**SMB workflow** [TENTATIVE]:

1. **Define markdown template** — daily rundown sections (macro snapshot, macro tone, overnight developments, economic calendar w/ prior/estimate/importance, earnings, other events, top movers w/ catalyst, research themes, secondary names, week ahead).
2. **Ingest emails** — Claude reads inbox research mail **5:00–8:30 a.m.** only; summarize (no verbatim quotes); extract stocks-in-play with catalyst + volatility rationale.
3. **Generate briefing** — structured markdown file per day.
4. **Render dashboard** — convert markdown → scannable HTML for morning review.
5. **Schedule** (optional step skipped in demo) — weekday automation before 8:30.

### Overlap with prop-desk ops

Same functional job as SMB desk **theme widget + catalyst catalog** (@concepts/prop-desk-team-trading-collaboration.md) but **single-trader email-driven** instead of team shared workspace.

### Cemini relevance

- Steal-from for **prod morning intel brief** — align with existing macro/regime tools + wiki synthesis; email access is laptop-trust-boundary [NEEDS VERIFICATION 2026-05-29].
- Not a signal source — **information compression** layer before human/discretionary or analyst-agent decisions.

## Snippets

> "Every weekday morning before 8:30 a.m., an AI workflow reads my market research emails… and generates a structured trading briefing along with a full dashboard." [Source: SMB Capital YouTube sh5h0GJzjNk, 2026-04-14]

> "Only use information from those email sources… Summarize the information rather than quoting emails directly." [Source: SMB Capital YouTube sh5h0GJzjNk, 2026-04-14]
