---
title: "dsh-vision-toolkit — DeepSeek Harness vision Extract"
type: entity
tags: [tool, phase-0, k240, ccc, dsh]
keywords: [dsh-vision, Anionex, MIT, claude-ds]
related:
  - sources/eval-github-repository-stack-2026-08-16.md
  - entities/tools/dshackle.md
  - concepts/cemini-license-posture.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: draft
created: 2026-08-17
updated: 2026-08-17
harness_verb: FILE
---

## Relations

- @sources/eval-github-repository-stack-2026-08-16.md — K240 eval (MIT ✓)
- @entities/tools/dshackle.md — same-batch Extract (RPC, not dsh)
- @concepts/cemini-license-posture.md
- @concepts/llm-routing-deepseek-openrouter-failover.md — do **not** replace PATH `claude-ds`

## Raw Concept

What prompted this page: K240 GitHub-stack eval URL (Anionex/dsh-vision-toolkit). Docx license unverified; **MIT confirmed** via `gh api`.

## Narrative

| Field | Value |
|-------|--------|
| Repo | https://github.com/Anionex/dsh-vision-toolkit |
| License | **MIT** [CONFIRMED gh 2026-08-17] |
| Local | `.local/adopts/dsh-vision-toolkit` (17MB) |
| Sibling clone | `.local/adopts/dsh-agent-teams` (MIT, 3.5MB) Watch REFERENCE |
| Verdict | **GO Extract** — CCC dsh ecosystem |
| wire_status | `policy_wired` |

Vision / multimodal helpers for DeepSeek Harness. Same-batch `dsh-agent-teams` is a multi-agent Watch clone. **Do not** replace official dsh behind PATH `claude-ds` with this toolkit, a desktop wrapper, or an awesome-dsh fork.

## Snippets

> dsh-vision-toolkit + dsh-agent-teams = CCC dsh ecosystem Extract. Do not replace PATH claude-ds. [Source: `.local/reports/license-k240-2026-08-17.md`]
