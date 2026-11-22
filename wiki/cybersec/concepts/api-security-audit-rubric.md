---
title: "API security audit rubric — inventory auth before hunting BOLA/BFLA"
type: concept
related:
  - "@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
maturity: draft
created: 2026-11-22
updated: 2026-11-22
---

## Raw Concept

Routed from
@osint-wiki/sources/2026-11-22-deep-research-link-eval-abliterated-harness.md, URL 16,
during the 2026-11-22 ingest. Graded **Context**.

The question this page answers: **what makes an automated API audit report worth
reading?**

## Narrative

A 2.8 KB Claude Code subagent prompt distributed through `claude-code-templates`. Blocked
from installation by the Workstation Harness Freeze. The prompt is the artifact; the
rubric is the extract.

### The rubric

1. **Read-only tool allowlist** — Read, Grep, Glob, Bash. An audit agent must not be able
   to change the target.
2. **Endpoint-to-auth mapping first** — inventory every endpoint and its authentication
   and authorization rule *before* looking for a bug. Most broken-object-level (BOLA)
   and broken-function-level (BFLA) findings are invisible until the access matrix is
   explicit.
3. **OWASP API Security Top 10 (2023)** as the checklist, not the goal.
4. **80% exploitability confidence bar** — report only what the agent believes is
   exploitable with that confidence.
5. **An explicit "do not report" list** — boilerplate headers, WAF fingerprints, and
   missing-header findings are excluded.

### Why steps 2 and 5 carry the value

Step 2 turns an unstructured scan into a comparison against a declared expectation — the
same principle as the pre-read expectation model used in code review.

Step 5 is rarer and more useful. Most automated auditing fails on volume: a report of
four hundred findings is read by nobody. Stating in advance what will **not** be
reported is what makes the remaining findings credible.

Both are reimplementable as prose in an `AGENTS.md`, with no installation.

### Licence

The report records **NOT FOUND** for the component licence. It is a published prompt on
a template site, not a repository. Treat it as reading material; do not copy and
redistribute it without checking the site's terms.

## Snippets

> Endpoint-to-auth mapping prior to bug hunting, OWASP API Security Top 10 (2023)
> checks, an 80% exploitability confidence bar, and an explicit "do not report"
> anti-noise list.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 16, retrieved 2026-11-22]

## Dead Ends

- **Reporting missing security headers.** They are on the do-not-report list for a
  reason: they are noise in an exploitability review.
