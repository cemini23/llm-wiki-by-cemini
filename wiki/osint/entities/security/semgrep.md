---
title: Semgrep
type: entity
tags: [security, sast, static-analysis]
keywords: []
related:
  - sources/3-19-compliance-research.md
  - sources/3-19-ip-sale-research.md
  - sources/github-action-and-workflow-research.md
  - entities/security/trivy.md
maturity: validated
created: 2026-04-23
updated: 2026-04-24
---

## Relations

- @sources/3-19-compliance-research.md — defensive-coding gate cited alongside Trivy + pip-audit in the deal-killer mitigation roadmap
- @sources/3-19-ip-sale-research.md
- @sources/github-action-and-workflow-research.md
- @entities/security/trivy.md

## Raw Concept

Synthesized from 2 source(s) referencing this entity across the Cemini research corpus. Category: security.

## Narrative

Semgrep is the rule-based SAST tool running on every Cemini pull
request. Rule packs used: OWASP Top Ten, Python secrets detection,
SQL-injection patterns, and a custom Cemini ruleset covering
venue-credential-handling antipatterns (no hardcoded keys; AES-GCM
vault for any private-key material; no eval on LLM output).

Cited in the IP-sale and compliance research as the primary
defensive-coding signal Cemini can show institutional buyers without
compromising on velocity — Semgrep rules run in ~30 seconds so PRs
aren't blocked on slow scanners.

## Snippets

*(populate as source stubs are deep-read.)*
