---
title: Tunnelto — Rust public-URL tunnel for local servers
type: entity
tags: [entity, tool, tunnel, rust, mit, atto-fit, k233]
keywords: [tunnelto, ngrok-alternative, rust, tunnel, atto-vault, localhost-expose]
related:
  - sources/eval-url-revenue-opportunity-2026-08-12.md
  - concepts/atto-genealogy-agent-kit.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- @sources/eval-url-revenue-opportunity-2026-08-12.md — K233 eval, Extract tier
- @concepts/atto-genealogy-agent-kit.md

## Raw Concept

Repo `tunneltodev/tunnelto` / `agrinman/tunnelto`. MIT, ~7k★. High-performance async-io/tokio Rust tunnel exposing localhost to public URLs — open-source ngrok alternative, no account/session limits.

## Narrative

**Verdict: GO Extract (Atto).** Enables ephemeral, client-facing previews of Atto vault visualizations during sales calls (Access share tier $8–20/mo, concierge $2.5k) without deploying persistent cloud infra. **Critical requirement: enforced automated teardown** — a live tunnel pointing at sensitive Italian civil records is a PII exposure risk. Steal-from: connection-parameter control + instant-teardown pattern.

[Source: agrinman/tunnelto (retrieved 2026-08-12)]
