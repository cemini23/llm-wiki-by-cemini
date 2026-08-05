---
title: reverse-skill — security research skill router pack
type: entity
tags: [entity, tool, cybersecurity, pentest, skills, k129]
keywords: [reverse-skill, zhaoxuya520, MIT, penetration testing, skill router, Cursor, Claude Code]
related:
  - sources/eval-url-batch-agentic-edge-security-2026-08-05.md
  - entities/tools/ai-surface.md
  - sources/eval-url-cemini-research-2026-06-25.md
  - concepts/wiki-tooling-evaluation.md
  - concepts/mcp-tool-calling-eval-scaffold.md
  - @cybersecurity-wiki/entities/tools/reverse-skill.md
maturity: draft
created: 2026-06-25
updated: 2026-08-05
wire_status: policy_wired
wire_target: .cursor/rules/osint-phase1-adopt-wires.mdc
---

## Relations

- @sources/eval-url-batch-agentic-edge-security-2026-08-05.md — K224 Integrate refresh + local clone
- @entities/tools/ai-surface.md
- @sources/eval-url-cemini-research-2026-06-25.md — K129 Adopt row (URL 5)
- @concepts/wiki-tooling-evaluation.md — Phase-0 registry; prior K93 **Defer** row superseded after license verify
- @cybersecurity-wiki/entities/tools/reverse-skill.md — primary wiki home (cross-route stub)

## Raw Concept

Phase-0 prompted by K129 **Cemini URL Evaluation Research.docx** URL 5 — `zhaoxuya520/reverse-skill`.

## Narrative

**reverse-skill** is an MIT-licensed **skill router pack** for authorized penetration testing and reverse-engineering workflows. AI-powered routing + on-demand toolchain bootstrapping + self-evolving knowledge base; supports Claude Code, Cursor, Cline, Kiro.

**Phase-0 (2026-06-25):**

| Check | Result |
|-------|--------|
| License | **MIT** (`gh api` — SPDX MIT) |
| Hardcoded wiki layout | N/A — SKILL.md router pack |
| Maturity | **6194★**, pushed 2026-06-12, 0 open issues |
| Cybersec-wiki fit | **Adopt** — primary home for pentest skill routing |
| CCC-wiki fit | **Adopt** — SKILL.md + routing.md methodology reference |
| OSINT fit | Secondary — tradecraft overlap only |

**Posture:** **Adopt** for @cybersecurity-wiki (primary) + @ccc-wiki (harness pattern). Cross-route stub on OSINT entity page; detailed ops live in cybersec wiki. **Authorized use only** — no prod trading integration.

**K224:** eval Integrate → local-abliterated-lab. Clone `.local/adopts/reverse-skill` (~12MB). Scope-lock to owned lab; no crimeware.

## Snippets

> "Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack" [Source: https://github.com/zhaoxuya520/reverse-skill README (retrieved 2026-06-25)]

## Dead Ends

- K93 `@sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` **Defer** — superseded after MIT confirm; was pre-license-audit posture.
