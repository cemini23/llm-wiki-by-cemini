---
title: frona — Rootless OCI sandbox for AI agents (Reject — BSL 1.1)
type: entity
tags: [tool, oci-sandbox, rootless, surrealdb, rust, bsl-1-1, business-source-license, reject-tier, license-quarantine, cybersec-cross-route]
keywords: [frona, fronalabs, rootless oci, surrealdb, policy-driven syscall filtering, axum, business source license, 2029 apache conversion]
related:
  - sources/tool-evaluation-wiki-fit-2026-05-13.md
  - concepts/tool-evaluation-framework.md
  - concepts/cemini-license-posture.md
  - concepts/paradigm-vs-license-inverse-correlation.md
maturity: draft
created: 2026-05-13
updated: 2026-05-13
---

## Relations

- `@sources/tool-evaluation-wiki-fit-2026-05-13.md` — origin source (Doc 3, K42), Reject (BSL 1.1)
- `@concepts/tool-evaluation-framework.md` — methodology
- `@concepts/cemini-license-posture.md` — BSL-1.1 quarantine policy
- `@concepts/paradigm-vs-license-inverse-correlation.md` — exemplar of "novel paradigm + poison license" pattern

## Raw Concept

- **URL**: `https://github.com/fronalabs/frona`
- **License**: BSL (Business Source License) 1.1 — converts to Apache-2.0 in February 2029
- **Stars**: 133 / 2 open issues
- **Stack**: Rust (76.1%), TypeScript (22.7%), Axum, SurrealDB, Next.js
- **Tier**: Reject (until 2029 license conversion)
- **Primary fit**: Workflow

## Narrative

Rootless OCI containers wrapping tool calls in isolated Linux processes with policy-driven syscall filtering. SurrealDB-backed memory compaction + per-principal scoping. Architecturally significant: prevents arbitrary code execution during autonomous red-teaming / web scraping.

### Why Reject (BSL 1.1)

BSL prohibits third-party PaaS distribution until 2029 conversion to Apache-2.0. Direct conflict with Cemini IP-sale posture. Re-evaluate February 2029.

### Cross-routing

- **Cybersec-wiki**: policy-driven syscall filtering documentation for defensive ops sandbox research (methodology only)

[Source: Tool Evaluation and Wiki Fit.docx URL 26 (retrieved 2026-05-13)]
