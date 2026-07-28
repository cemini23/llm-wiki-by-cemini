---
title: Credential leak response — revoke before you clean
type: concept
tags: [concept, security, secrets, incident-response, k201]
keywords: [revoke first, IAM, CloudTrail, push protection, gitleaks]
related:
  - sources/substack-rss-seceng-weekly-2026-07-28-aws-keys-public-repo.md
  - sources/substack-rss-seceng-weekly-2026-07-13-agentic-ai-security-fundamentals.md
  - concepts/code-as-agent-harness.md
maturity: draft
created: 2026-07-28
updated: 2026-07-28
---

## Relations

- @sources/substack-rss-seceng-weekly-2026-07-28-aws-keys-public-repo.md
- @sources/substack-rss-seceng-weekly-2026-07-13-agentic-ai-security-fundamentals.md
- @concepts/code-as-agent-harness.md

## Raw Concept

What is the correct first move when secrets land in a public git repo?

## Narrative

Public credential push is a **race**, not a scolding moment. Scrapers already have the material. Sequence (AWS-shaped but generalizes to PATs, Discord webhooks, API keys):

1. **Revoke / deactivate** the live credential immediately.
2. **Assess** blast radius (scopes / IAM policies).
3. **Investigate** logs for use + persistence (second doors).
4. **Clean** history (rewrite, not delete-in-new-commit).
5. **Prevent** (gitignore, Secrets Manager, scanners, push protection).
6. **Communicate** without blame — speed of report is the win condition.

Prevention tooling (gitleaks, trufflehog, GitHub push protection, repo `detect-secrets`) complements but does not replace the revoke-first response.
