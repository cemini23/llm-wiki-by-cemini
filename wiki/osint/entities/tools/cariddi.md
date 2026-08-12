---
title: Cariddi — automated secret/credential scanner
type: entity
tags: [entity, tool, recon, secrets, gpl-3.0, cybersec-fit, k233]
keywords: [cariddi, secret-detection, api-key, regex, recon, crawler]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/local-abliterated-llm-pentest-stack.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @cybersecurity-wiki/concepts/local-abliterated-llm-pentest-stack.md

## Raw Concept

Repo `edoardottt/cariddi`. GPL-3.0. Crawls a domain list and scans URLs for 500+ secret types (hardcoded secrets, API keys, exposed credentials) via tuned regexes.

## Narrative

**Verdict: GO Extract (cyber lab, regex only).** Reuse the 500+ secret-detection regex signatures in internal OSINT/forensic scanning scripts; do **not** deploy the crawler against external targets (scope discipline, false-positive noise, WAF rate-limit risk). Steal-from: regex coverage for authorized lab exposure mapping.

[Source: edoardottt/cariddi (retrieved 2026-08-12)]
