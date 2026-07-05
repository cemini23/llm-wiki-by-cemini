---
title: snyk studio-mcp — Snyk MCP for agent codegen security
type: entity
tags: [entity, tool, mcp, security, tipdrop, k146]
keywords: [snyk, studio-mcp, CVE, dependency scan, Apache-2.0]
related:
  - sources/eval-github-repo-mcp-plan-2026-07-05.md
  - concepts/openclaw-security-taxonomy.md
  - concepts/wiki-tooling-evaluation.md
maturity: draft
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @sources/eval-github-repo-mcp-plan-2026-07-05.md — K146 Adopt
- @concepts/openclaw-security-taxonomy.md — MCP hardening cluster

## Raw Concept

K146 Phase-0 on [snyk/studio-mcp](https://github.com/snyk/studio-mcp).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `snyk/studio-mcp` |
| **License** | **Apache-2.0** |
| **Stars / pushed** | ~51★; pushed 2026-06-26 |
| **Verdict** | **Adopt** — TipDrop/CCC agent PR CVE gate (requires Snyk account) |
| **Ops** | Run on agent-generated diffs before merge; not a substitute for iFixAi M2 diagnostics |

Wiki + TipDrop kit optional adopt; no prod scp unless David enables Snyk org.

## Snippets

> "Guarantees that known CVEs, malicious dependency chains, and basic prompt injection vectors are caught instantly at the inception of the code generation loop." [Source: eval-github-repo-mcp-plan-2026-07-05.md aggregate summary]
