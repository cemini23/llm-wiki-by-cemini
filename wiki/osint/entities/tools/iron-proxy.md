---
title: Iron Proxy — policy egress proxy and request firewall
type: entity
tags: [entity, tool, proxy, egress-control, apache-2.0, cybersec-fit, k68]
keywords: [iron-proxy, egress, oauth, jwt, request firewall, policy enforcement]
related:
  - sources/multi-wiki-tool-eval-22url-2026-05-26.md
maturity: draft
created: 2026-05-26
updated: 2026-05-26
---

## Relations

- @sources/multi-wiki-tool-eval-22url-2026-05-26.md — K68 source

## Raw Concept

Repository: `ironsh/iron-proxy` (Apache-2.0, ~421★, active 2026-05-25). Surfaced as cybersec-primary Adopt due to request filtering, OAuth/JWT handling, and egress-policy control.

## Narrative

**Verdict: Adopt-eligible (cybersec), not yet adopted in OSINT workspace.**

Primary relevance is pattern extraction for controlled egress and request sanitization around relay nodes. For Cemini, this is a **steal-from candidate** unless server-side team explicitly scopes proxy replacement.
