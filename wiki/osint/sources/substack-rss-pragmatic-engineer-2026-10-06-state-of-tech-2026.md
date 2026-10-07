---
title: "The Pragmatic Engineer — The state of the tech industry in 2026 (2026-10-06)"
type: source
tags: [source, k284, engineering, agents, ccc, industry]
keywords: [pragmatic-engineer, agent-prs, ide-death, harness, migrations, code-review-theater, quality]
related:
  - concepts/k284-feeds-wave.md
  - concepts/ai-industry-trends-2026.md
  - concepts/agentic-code-quality-gates.md
maturity: draft
created: 2026-10-07
updated: 2026-10-07
read_status: read
---

## Relations

- @concepts/k284-feeds-wave.md
- @concepts/ai-industry-trends-2026.md
- @concepts/agentic-code-quality-gates.md

## Raw Concept

| Title | The state of the tech industry in 2026 |
| Source | The Pragmatic Engineer (Substack) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/osint/newsletter-rss-pragmatic-engineer-2026-10-06-the-state-of-the-tech-industry-in-2026.md` |
| Retrieved | 2026-10-06 |
| URL | https://newsletter.pragmaticengineer.com/p/the-state-of-the-tech-industry-in |
| Tier | free (RSS) |
| cross-wiki | ccc-wiki |
| read-status | read |

## Narrative

Gergely Orosz's LDX3 keynote, backed by unpublished data from GitHub, Factory AI, and Linear. The most useful industry snapshot of the year for the CCC lane.

### What changed

- **Nobody writes code by hand.** Most engineers have stopped.
- **5–10 parallel agents is now normal** (Claude Code's Boris Cherny runs 5 terminal tabs + 5–10 cloud Claudes).
- **Agent-authored PRs: ninefold increase in eight months.** In **August 2026, agent-authored PRs on GitHub exceeded human-authored ones.** ~75M+ AI PRs/month (vs 25M human PRs in Dec 2023).
- **Agent-generated issues exceed human ones** since July (Linear data).
- **83% of Factory AI users use skills** — up 2.5× from February.
- **The IDE is fading.** Cursor removed its IDE interface; JetBrains pivoted to Air; no major VS Code fork has shipped since Nov 2025.
- **Migrations collapse from years to weeks.** Bun Zig→Rust in 11 days; OpenAI API Python→Rust in ~5 months; Uber 600k JUnit4 tests in 4 months.
- **AI cost is a top concern.** Uber cut per-token cost 50%+ via open models + smart routing.

### What is broken

- **Human code review is dead.** "Everyone is playing the theater of doing reviews … just stamp everything with LGTM."
- **Agent-only PR reviews are trending up** (Linear data).
- **Quality and reliability are down.** "98% uptime becoming the norm instead of the exception."
- **CPU/GPU/memory shortages** — reserve capacity months ahead.

### What stays the same

Teams still matter. **Planning still matters for complex work.** **Tests and validation still matter** — "you need a way to trust your code." **Non-engineers still do not ship to production.** And old best practices return: **tracer bullets / golden path**, unit tests, upfront architecture.

### What comes next

Cloud coding agents + harnesses dominate. Engineers stop reading the code. New internal infra (agentic CI/CD, agentic observability). A golden age of refactoring/migrations. AI "positivity" screened in hiring. **Deep domain knowledge becomes more valuable** (Titus Winters: "When intelligence becomes commonplace, wisdom and charisma become much more important").

### Why it matters here

The **code-review theater** and **quality-decline** findings are the actionable ones — they justify the wiki's "audit the change set, not just the tests" doctrine, and the `agentic-code-quality-gates` thread. **No `/route` swap.** Route to CCC.

## Snippets

> "There were more agent-authored PRs in August 2026 on GitHub than human-authored ones!" [Source: newsletter-rss-pragmatic-engineer-2026-10-06-the-state-of-the-tech-industry-in-2026.md]

> "Everyone is playing the theater of doing reviews, but with the volume of changes that get thrown your way … people just find a path of least resistance: give up on reviews and just stamp everything with LGTM." [Source: newsletter-rss-pragmatic-engineer-2026-10-06-the-state-of-the-tech-industry-in-2026.md]

> "The AI writes pretty much all the code, but we have the AI write pretty much all the tests as well … You need to have a way to trust your code, and tests are probably the best way to." [Source: newsletter-rss-pragmatic-engineer-2026-10-06-the-state-of-the-tech-industry-in-2026.md]
