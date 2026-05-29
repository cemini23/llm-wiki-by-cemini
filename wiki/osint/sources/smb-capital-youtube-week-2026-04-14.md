---
title: "SMB Capital YouTube — week of 2026-04-14 (3 videos)"
type: source
tags: [source, youtube, smb-capital, claude-code, pre-market, k79]
keywords: [claude-trading-assistant, four-step-workflow, pre-market-automation, plan-mode, routines]
related:
  - entities/organizations/smb-capital.md
  - meta/smb-capital-youtube-ingest-cadence.md
  - sources/smb-capital-youtube-week-2026-04-01.md
  - sources/smb-capital-youtube-week-2026-05-05.md
  - sources/smb-capital-youtube-week-2026-05-22.md
  - concepts/claude-code-trading-assistant-workflow-smb.md
  - concepts/pre-market-ai-research-briefing-smb.md
  - concepts/claude-code-skills-md-workflow.md
maturity: validated
read_status: deep-read
created: 2026-05-29
updated: 2026-05-29
clusters: [trading-education, agent-workflows, claude-code]
---

## Relations

- @entities/organizations/smb-capital.md — channel publisher
- @meta/smb-capital-youtube-ingest-cadence.md — batch 3 checkpoint
- @sources/smb-capital-youtube-week-2026-05-05.md — prior batch
- @sources/smb-capital-youtube-week-2026-05-22.md — batch 1
- @concepts/claude-code-trading-assistant-workflow-smb.md — videos 1–2 synthesis
- @concepts/pre-market-ai-research-briefing-smb.md — video 3 synthesis
- @concepts/claude-code-skills-md-workflow.md — OSINT Skills.md parallel

## Raw Concept

| Field | Value |
|-------|-------|
| Batch window | 2026-04-14 → 2026-04-25 |
| Videos | 3 (Claude Code cluster) |
| Location | `.local/smb-capital-youtube/2026-04-14-week/` → `cemini-librarian:/opt/cemini-bulk/research/smb-capital-youtube-week-2026-04-14-transcripts.md` |
| Read | 2026-05-29 deep-read |

**Note:** Videos 1–2 are near-duplicates (4-step framework vs longer live build) — ingest once as shared workflow concept.

## Narrative

### Video index

| # | Date | ID | Title | Route |
|---|------|-----|-------|-------|
| 1 | 2026-04-25 | [45eaVU5NVi8](https://www.youtube.com/watch?v=45eaVU5NVi8) | 4-Step Process To Build AI Trading Assistant With Claude | @concepts/claude-code-trading-assistant-workflow-smb.md |
| 2 | 2026-04-18 | [mssPkDuQnmY](https://www.youtube.com/watch?v=mssPkDuQnmY) | How To Build Your Own Claude AI Trading Assistant | same (live build companion) |
| 3 | 2026-04-14 | [sh5h0GJzjNk](https://www.youtube.com/watch?v=sh5h0GJzjNk) | I Automated My Pre-Market Research With AI | @concepts/pre-market-ai-research-briefing-smb.md |

### Highlights

- **Four steps:** plan mode → build skeleton → personalize (coach layer) → scheduled routines.
- **Deliverable:** personal HTML dashboard (TraderView-style stats + custom tabs); non-coders can build in ~afternoon [TENTATIVE].
- **Pre-market:** email 5:00–8:30 → markdown rundown → HTML scan before open.
- **Key constraint:** personalization requires playbook/trade-log **inputs** — generic prompts → generic tools.

### Next batch

Resume **2026-04-01** — Steenbarger (`K2e1Sdpfv7s`), profitable-trader signs (`JddKb9XyOqk`), earnings strategy (`afDpTJ6I3gA`).

## Snippets

> "Plan mode… build mode… personalize… routines." [Source: https://www.youtube.com/watch?v=45eaVU5NVi8 (retrieved 2026-05-29)]

> "The markdown file is simply a lightweight text format… structured source document for the dashboard." [Source: https://www.youtube.com/watch?v=sh5h0GJzjNk (retrieved 2026-05-29)]
