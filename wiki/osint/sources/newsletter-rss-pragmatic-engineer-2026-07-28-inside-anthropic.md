---
title: "Pragmatic Engineer — How building software is changing at Anthropic — 2026-07-28"
type: source
tags: [source, newsletter-rss, inbox-auto, pragmatic-engineer, k202]
keywords: [Anthropic, Claude Managed Agents, Bun Rust rewrite, verification, Fable]
related:
  - sources/newsletter-rss-latent-space-2026-07-28-codex-chatgpt-work.md
  - concepts/code-as-agent-harness.md
maturity: draft
read_status: read
created: 2026-07-28
updated: 2026-07-28
clusters: [k202-ingest]
---

## Relations

- @sources/newsletter-rss-latent-space-2026-07-28-codex-chatgpt-work.md — same-day OpenAI Work harness
- @concepts/code-as-agent-harness.md — Managed Agents / verification-heavy loops
- @ccc-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-28-inside-anthropic.md — cross-wiki stub

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | How building software is changing at Anthropic |
| **URL** | https://newsletter.pragmaticengineer.com/p/inside-anthropic |
| **Feed** | pragmatic-engineer |
| **Inbox** | `newsletter-rss-pragmatic-engineer-2026-07-28-how-building-software-is-changing-at-anthropic.md` |
| **sha256** | `15acd089d08b5485d8e12e4270e7a41dfe5e2d2b493fdfa328cd81dc655d96f5` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-07-28-how-building-software-is-changing-at-anthropic.md` |

## Narrative

Gergely Orosz inside Anthropic: Claude Managed Agents (~6mo; brain/hands/session split; credentials via vault proxy never seen by agent). Bun Zig→Rust rewrite: **11 days**, 64 parallel agents, ~$165K tokens — ~15% implement / 85% verify. Practices: 3–10 parallel agents; verification > implementation; ≤2 engineers/project; PRDs still matter for complex. Archetype shifts to deep understanding + coordination. Primary routing: **CCC wiki**.

## Snippets

> Implementation of the Rust rewrite took far less time than fixing it up, then validating… ~15% implement / 85% verify. [Source: https://newsletter.pragmaticengineer.com/p/inside-anthropic (retrieved 2026-07-28)]
