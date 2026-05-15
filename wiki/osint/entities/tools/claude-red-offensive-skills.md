---
title: "Claude-Red — Offensive Security Skills Library for Claude Code"
type: entity
tags: [tool, offensive-security, claude-code, skill-library, pentest, web-application-security]
keywords: [claude-red, snailsploit, offensive-security, skill-md, claude-code, pentest, web-vulnerabilities, sqli, ssrf, mit-license, adopt]
related:
  - sources/multi-wiki-link-eval-v4-2026-05-15.md
  - concepts/ip-sale-readiness.md
maturity: draft
created: 2026-05-15
updated: 2026-05-15
---

## Relations
- @cybersecurity-wiki/entities/claude-red-offensive-skills.md  (cross-wiki stub)

- @sources/multi-wiki-link-eval-v4-2026-05-15.md — evaluated in v4 link-eval (Adopt tier)
- @concepts/ip-sale-readiness.md — MIT license clean for IP-sale portfolio

## Raw Concept

Promoted from the v4 multi-wiki link evaluation (2026-05-15). Tier: **Adopt**. Primary fit: Cybersec-wiki.

URL: https://github.com/SnailSploit/Claude-Red
License: MIT
Stars: 1.3k | Last commit: 2026-03-08 | Open issues: 0
Stack: Python / Shell / Markdown

## Narrative

Claude-Red is a curated offensive security skills library that maps 16 web application methodologies (offensive-sqli, offensive-ssrf, offensive-xss, etc.) directly into the SKILL.md paradigm used by Claude Code. Each skill loads on conversational trigger, eliminating context-window bloat — only the relevant methodology is loaded when the user invokes a specific attack vector.

Phase structure: V.2 release with structured phases covering reconnaissance, vulnerability discovery, exploitation, and reporting. The repository uses sparse git checkout patterns for modular installation.

Key architectural insight: SKILL.md contextual loading — skills are loaded only when triggered by conversation cues rather than pre-loaded into context. This token-economic pattern is directly reusable across all Cemini laptop-side Claude Code deployments.

Wireless phase (Phase 3) splits into 802.11 and WPA3 sub-modules — requires physical network validation for compatibility with internal auditing scopes.

## Cross-wiki routing

- **@cybersec-wiki** — primary destination. Full tool entity page for offensive security operations (pentest/bug bounty).
- **@ccc-wiki** — stub documenting the on-demand conversational trigger architecture and SKILL.md contextual loading pattern for token optimization.
