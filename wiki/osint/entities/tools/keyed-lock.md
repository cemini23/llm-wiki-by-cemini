---
title: "ldm0/keyed-lock — per-key mutex for concurrent claim ingestion"
type: entity
tags: [tool, concurrency, rust, guruwatcher, k283]
keywords: [keyed-lock, per-key-mutex, rust, concurrency, guruwatcher, race-condition, k283]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
  - entities/tools/guruwatcher.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub
- @entities/tools/guruwatcher.md — target project

## Raw Concept

- **Repo:** `github.com/ldm0/keyed-lock`
- **Tier (K283):** **Extract** (route: GuruWatcher)
- **License:** NOT FOUND (docx)
- **Stack:** Rust
- **Docx metadata:** NOT FOUND

## Narrative

A fine-grained concurrency primitive: **lock distinct keys independently** instead of one monolithic process mutex. Two writers touching different keys never block each other.

### Why it matters here

GuruWatcher runs **parallel ingestion** across multiple newsletters. Per-ticker or per-watch-ID locks prevent race conditions when updating the claim ledger, while still allowing high-throughput concurrent reconciliation. Pairs with @entities/tools/background-agents.md.

### Boundary

Synchronisation must not interfere with alert-only operation and must never clobber existing `watches.json` trigger state. **Deadlock-avoidance across multi-key acquisitions is the thing to verify** before wiring.

## Snippets

> "Applying keyed locks per ticker or watch ID prevents race conditions when updating ledger records while allowing high-throughput concurrent reconciliation." [Source: eval-github-repos-dev-tools-2026-10-06.md]
