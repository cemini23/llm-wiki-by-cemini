---
title: "SecEng Weekly — Respond when AWS keys hit a public repo (2026-07-28)"
type: source
tags: [source, security, seceng-weekly, secrets, k201, cybersec]
keywords: [AWS keys, IAM, CloudTrail, revoke first, gitleaks, push protection]
related:
  - concepts/credential-leak-revoke-first-response.md
  - concepts/code-as-agent-harness.md
  - sources/substack-rss-seceng-weekly-2026-07-13-agentic-ai-security-fundamentals.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k201-ingest, cybersec]
---

## Relations
- @cybersecurity-wiki/briefs/2026-07-28_k201-seceng-aws-keys-public-repo.md  (cross-wiki brief)

- @concepts/credential-leak-revoke-first-response.md
- @concepts/code-as-agent-harness.md — agent/CI secret hygiene adjacency
- @sources/substack-rss-seceng-weekly-2026-07-13-agentic-ai-security-fundamentals.md — prior SecEng Weekly
- Cross-wiki: cybersecurity-wiki brief (primary home)

## Raw Concept

| Field | Value |
|-------|-------|
| **URL** | https://secengweekly.substack.com/p/how-id-respond-when-a-developer-pushes |
| **Published** | 2026-07-28 |
| **Filename** | `substack-rss-seceng-weekly-2026-07-28-how-id-respond-when-a-developer-pushes-aws-keys.md` |
| **sha256** | `a496948f975b0515433b1bd5cac5077589f84092067c8c15d67e60e80b6bda8e` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-seceng-weekly-2026-07-28-how-id-respond-when-a-developer-pushes-aws-keys.md` |

## Narrative

Incident playbook for AWS access keys pushed to a public GitHub repo. Core order: **REVOKE → ASSESS → INVESTIGATE → CLEAN → PREVENT → COMMUNICATE**. Automated scrapers pick honeypot keys in minutes — cleaning the repo first is the wrong instinct.

Hour shape: (0–2) IAM deactivate then delete; (2–10) blast radius via attached policies; (10–25) CloudTrail by access-key-id — watch CreateUser/CreateAccessKey, GetObject, RunInstances, foreign IPs; hunt persistence before declaring win; (25–35) purge git history (filter-repo/BFG), not just new commit; (35–50) rotate, gitleaks/trufflehog, enable GitHub secret scanning + push protection; (50–60) thank reporter, no blame.

**OSINT/CCC steal:** same sequence for any Cemini API key / Discord webhook / PAT leak; pre-commit detect-secrets is prevention, not response. Primary deep home → cybersecurity-wiki.

## Snippets

> "revoke before you clean. The repo can wait. The key cannot."

> "REVOKE → ASSESS → INVESTIGATE → CLEAN → PREVENT → COMMUNICATE"
