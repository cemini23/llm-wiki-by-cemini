---
title: "Hetty — HTTP toolkit for security research (Steal-from-tier)"
type: entity
tags: [tool, offensive-security, pentesting, mitm-proxy, cybersec-wiki, steal-from-tier, go]
keywords: [hetty, HTTP toolkit, MITM proxy, Burp Suite alternative, Go, security research, bug bounty]
related:
  - sources/tool-evaluation-multi-wiki-audit-may-2026.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
---

## Relations

- `@sources/tool-evaluation-multi-wiki-audit-may-2026.md` — source evaluation that classified this as Steal-from-tier

## Raw Concept

Identified in the May 2026 44-tool multi-wiki audit. MIT-licensed HTTP toolkit for security research — an open-source Burp Suite alternative written in Go. Primary fit: Cybersec wiki.

## Narrative

Hetty is a comprehensive HTTP toolkit for security research and penetration testing. Features: advanced MITM proxy, project-based database storage, scope management. Written in Go.

**Steal-from rationale**: Full integration into Cemini's stack is unnecessary, but specific Go-based proxy implementation patterns are worth extracting for internal traffic inspection tools. These tools would monitor API behavioral anomalies on `/opt/cemini` without requiring the full Hetty deployment.

**License**: MIT — permits extracting and adapting specific code patterns without copyleft risk.

**Primary wiki**: Cybersec wiki — reference architecture for offensive security operations and bug bounty auditing methodology.

**Open question** [NEEDS VERIFICATION 2026-05-16]: Go proxy performance stability under high-throughput real-time REST API stream interception needs stress testing.
