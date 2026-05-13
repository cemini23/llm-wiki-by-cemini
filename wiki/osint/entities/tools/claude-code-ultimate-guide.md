---
title: "claude-code-ultimate-guide — 24k-line CC reference (Steal-from, CC-BY-SA-4.0 caveat)"
type: entity
tags: [tool, claude-code, reference-guide, cve-catalog, malicious-skill-patterns, cc-by-sa, gemini-eval-doc1]
keywords: [claude-code-ultimate-guide, FlorianBruniaux, 24000 lines, 7-module learning path, 181 templates, embedded mcp search, 28 cve catalog, 655 malicious skill patterns]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/multi-wiki-gemini-eval-prompt-2026-05-12.md
  - concepts/tool-evaluation-framework.md
  - "@cybersecurity-wiki/entities/tools/claude-code-ultimate-guide.md"
maturity: draft
created: 2026-05-12
updated: 2026-05-12
gemini_eval_doc1_url: 17
phase_0_verdict: STEAL-FROM 2026-05-12 (TDD prompts + CVE database; copy ideas, not fork — CC-BY-SA Share-Alike)
---

## Relations

- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — source eval (URL 17)
- `@cybersecurity-wiki/entities/tools/claude-code-ultimate-guide.md` — cybersec cross-route for CVE catalog + skill-pattern DB

## Raw Concept

- **Repo**: `github.com/FlorianBruniaux/claude-code-ultimate-guide`
- **License** [per Gemini eval]: CC-BY-SA-4.0
- **Stars** [per Gemini eval]: ~4,300
- **Tier**: Steal-from
- **Primary fit**: Workflow (TDD prompt templates) + Cybersec wiki (CVE catalog + malicious-skill-pattern DB)

## Narrative

24,000-line Claude Code reference with 7-module learning path, 181 prompt templates, embedded MCP search server. Substantial cybersec content: 28-CVE catalog and 655-pattern malicious-skill-detection database. Cross-routed to cybersec wiki where the security content has primary value.

### Integration vector

**Steal-from, do not fork**. CC-BY-SA-4.0 Share-Alike copyleft triggers derivation obligations on any forked work. Safe pattern: read for ideas, extract pattern names + concepts, re-implement in our own templates. NOT safe: copying full template files verbatim into our own skill library (would obligate us to publish derivative work under CC-BY-SA).

### Open questions

- Whether the MCP search server inside the guide is itself standalone-reusable (and what its license is)
