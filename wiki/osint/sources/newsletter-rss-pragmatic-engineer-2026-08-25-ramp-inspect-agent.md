---
title: "Pragmatic Engineer — Ramp Inspect in-house coding agent (2026-08-25)"
type: source
tags: [newsletter, harness, ccc, k247]
keywords: [Ramp, Inspect, remote-sandbox, Cloudflare, Modal, background-agent]
related:
  - concepts/k247-agent-harness-wave.md
  - concepts/practical-loop-engineering.md
  - sources/newsletter-rss-pragmatic-engineer-2026-08-19-osmani-ai-engineering.md
maturity: draft
created: 2026-08-26
updated: 2026-08-26
read_status: read
---

## Relations

- @concepts/k247-agent-harness-wave.md — enterprise custom harness case study
- @concepts/practical-loop-engineering.md — buy-vs-build harness economics
- @sources/newsletter-rss-pragmatic-engineer-2026-08-19-osmani-ai-engineering.md — PE harness discourse sibling

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Why Ramp built its own in-house coding agent, Inspect |
| URL | https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect |
| Retrieved | 2026-08-25 |
| File | `newsletter-rss-pragmatic-engineer-2026-08-25-why-ramp-built-its-own-in-house-coding-agent-ins.md` |
| sha256 | `8ca0ef16fdf190839adaa7ddc87f626bd19ada269114cdc120ca94a43378091d` |
| Dual-ID | **OSINT K247**. CCC awareness — do not swap `/route`. |

## Narrative

Ramp's **Inspect** internal background coding agent (Nov 2025 internal ship): ~75% of merged PRs now from Inspect vs third-party harnesses. Differentiators: **remote Modal sandboxes** (unlimited concurrency, centralized dev env), internal data/MCP integrations, public collaborative sessions (150+ contributors), sub-5s sandbox spin-up tricks.

Stack: React/Vite, Cloudflare Durable Objects, SQLite, Cloudflare Agents SDK, Modal. In-sandbox: OpenCode, Postgres/Redis/RabbitMQ/Temporal, Chromium, VS Code Server. Use cases: coding, Slack bugfix, code review, incident agents.

CCC steal: enterprise harness when parallel remote sandboxes + internal MCP beat laptop-bound Cursor/Claude Code. **No prod wire** — pattern reference only.

## Snippets

> "75% of merged PRs are now raised by Inspect; a clear indication that many engineers prefer the tool over others." [Source: newsletter-rss-pragmatic-engineer-2026-08-25-why-ramp-built-its-own-in-house-coding-agent-ins.md]

> "Inspect spins up a sandboxed remote development environment which unlocks unlimited session concurrency, centralized setup configuration, and cross-functional session collaboration." [Source: same]
