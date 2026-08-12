---
title: Pragmatic Engineer — Stop being skeptical about AI for development (Charity Majors)
type: source
tags: [newsletter, k234, ccc, harness, observability]
keywords: [pragmatic-engineer, charity-majors, honeycomb, claude-code, harness, verification, code-review]
related:
  - concepts/agent-harness-verification-bottleneck.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-12
updated: 2026-08-12
read_status: read
---

## Relations

- @concepts/agent-harness-verification-bottleneck.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept

| Field | Value |
|-------|--------|
| Title | Stop being skeptical about AI for development with Charity Majors |
| Author | Gergely Orosz / Charity Majors (Honeycomb) |
| URL | https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for |
| sha256 | `e56bda950d3b7fc26aa568cbe6dec8bc92d7d8c15bffa2072bcf67742f15008e` |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-08-12-stop-being-skeptical-about-ai-for-development-wi.md` |
| retrieved | 2026-08-12 |
| type | RSS teaser + episode takeaways (paywall may gate full post) |

## Narrative

Charity Majors (Honeycomb CTO) on why 2026 skepticism about AI for development is less tenable. Steals for Cemini harness / `/route`:

1. **Harness > model for the generational shift** — Opus 4.5 mattered, but Claude Code turning harnesses from shell-script wrappers into serious infrastructure was the turning point (Nov 2025).
2. **Verification is the bottleneck** — once generation is cheap, trust moves to tests, evals, conformance; shipping unread code becomes a "when not if" for professionals.
3. **Pets → cattle for code** — regenerate verifyably-correct variants instead of hand-nursing individual functions (infra analogy from 2010s servers).
4. **Code review overrated** for correctness/syntax — humans better at deciding *what* to build; correctness belongs in automated validation.
5. **Non-deterministic systems need more discipline**, not less — reduce trust in authored code → increase trust in validation layers.
6. **AI fatigue counter** — Honeycomb's "no AI on Wednesdays"; small acts of agency.

Route: **CCC primary** (`/route` verify gate, SIP Plan quality, harness evolution backlog). Wiki concept `@concepts/agent-harness-verification-bottleneck.md`. No Atto/GW/poker steal.

[Source: Pragmatic Engineer 2026-08-12 (retrieved 2026-08-12)]
