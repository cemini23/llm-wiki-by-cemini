---
title: "pawurb/hotpath-rs — Rust hot-path profiler for copula latency"
type: entity
tags: [tool, profiling, rust, gambling, ceminiparlays, k283]
keywords: [hotpath-rs, rust, profiler, hot-path, copula, ceminiparlays, k283]
related:
  - sources/eval-github-repos-dev-tools-2026-10-06.md
  - concepts/k283-eval-wave.md
maturity: draft
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- @sources/eval-github-repos-dev-tools-2026-10-06.md — K283 eval (tier: Extract)
- @concepts/k283-eval-wave.md — K283 cluster hub

## Raw Concept

- **Repo:** `github.com/pawurb/hotpath-rs`
- **Tier (K283):** **Extract** (route: CeminiParlays)
- **License:** NOT FOUND (docx)
- **Stack:** Rust
- **Docx metadata:** NOT FOUND

## Narrative

Lightweight **hot-path profiling** for Rust binaries and extension modules — find execution bottlenecks without a heavy tracing harness.

### Why it matters here

CeminiParlays computes joint probability distributions across many sportsbook legs. Ranked-EV tickets must recompute **instantly when book lines move**. Profiling the copula correlation engine keeps that latency low. Route: Gambling wiki / CeminiParlays brief (Priority #4).

### Boundary

**CeminiParlays compliance mandate unchanged:** never scrape bookmaker boards, never auto-submit bets, always require the operator to type posted American lines. Output must state "do not submit."

## Snippets

> "Extracting hot-path profiling mechanics allows fine-tuning numerical routines in CeminiParlays to ensure instant recalculations when book lines move." [Source: eval-github-repos-dev-tools-2026-10-06.md]
