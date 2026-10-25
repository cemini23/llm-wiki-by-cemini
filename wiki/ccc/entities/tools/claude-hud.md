---
title: claude-hud — Claude Code statusline telemetry (Context)
type: entity
tags: [tool, ccc]
keywords: [claude-hud, statusline, rate limits, cve]
related:
  - @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md
maturity: draft
created: 2026-10-25
updated: 2026-10-25
phase_0_verdict: CONTEXT
wire_status: none
wire_note: Wiki reference only. No install.
---

## Raw Concept

URL row of @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.9-2026-10-25.md. Tier **Context** — reference only, no revenue path.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/jarrodwatts/claude-hud |
| **License** | MIT |
| **Maturity** | Active 2026, v0.5.0+ |
| **Verdict** | CONTEXT |

A Claude Code statusline plugin. It renders live context-window use, 5-hour and 7-day rate-limit countdowns, active tools, sub-agent progress, and todo state. It is an operator terminal HUD with no product revenue path, so it stays Context.

Versions up to 0.0.12 carry two published vulnerabilities. CVE-2026-47090 (GHSA-f378-wf84-8j5h) allows ANSI terminal injection, OSC 52 clipboard overwrite, and outbound requests via branch or directory names containing ESC sequences. CVE-2026-47092 (GHSA-p5qq-v9mc-39ff) allows arbitrary code execution on Windows via COMSPEC hijacking. Require commit 234d9aa or later, where transcript values are sanitised and capped at 80 characters.

## Dead Ends

- Installing any build before commit 234d9aa. Two published CVEs, one of them RCE on Windows.
