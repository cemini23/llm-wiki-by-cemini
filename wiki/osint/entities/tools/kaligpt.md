---
title: KaliGPT — terminal offensive-security agent (custom NC license)
type: entity
tags: [entity, tool, cybersec, ollama, reject-commercial, k60]
keywords: [kaligpt, sudohopex, ollama, pentest, terminal-agent, non-commercial-license]
related:
  - sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md
  - concepts/cemini-license-posture.md
maturity: draft
created: 2026-05-23
updated: 2026-05-23
---

## Relations

- @sources/github-repo-evaluation-cemini-v4-20url-2026-05-23.md — K60 URL 1; eval Adopt **rejected after license read**

## Raw Concept

K60 v4 tool eval flagged `SudoHopeX/KaliGPT` as MIT Adopt for cybersec-wiki. GitHub API + LICENSE file audit: **custom non-commercial license**, not MIT.

## Narrative

- **Repo**: [github.com/SudoHopeX/KaliGPT](https://github.com/SudoHopeX/KaliGPT) (~246★, May 2026)
- **Stack**: Bash/Python, Ollama local models, terminal UI (`rich`, `google.genai` optional)
- **Fit**: Offensive security payload/recon assistant with local-inference OPSEC story

### Verdict: **NO-GO for Cemini commercial / IP-sale path**

LICENSE file: **SudoHopeX Non-Commercial Software License (2025)** — prohibits commercial use without separate permission. Eval prose claiming MIT is **wrong** [CONFIRMED 2026-05-23].

Reference-only for cybersec-wiki tradecraft (Ollama + terminal harness pattern). **Do not** install on prod or bundle into proprietary stack.

### Phase-0

Not required for NO-GO license gate. If license ever reverts to OSI MIT/Apache, re-run Phase-0 for Ollama dependency + tool surface.

## Snippets

> "Copyright (c) 2025 Krishna Dwivedi | SudoHopeX" — SudoHopeX Non-Commercial Software License [Source: github.com/SudoHopeX/KaliGPT LICENSE, retrieved 2026-05-23]
