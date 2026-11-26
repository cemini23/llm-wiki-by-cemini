---
title: "The Pragmatic Engineer — How Anthropic builds software in 2026 (Katelyn Lesse)"
type: source
related:
  - concepts/claude-code-software-factory.md
  - concepts/agent-pr-volume-exceeds-human.md
  - concepts/agent-completion-verification-gates.md
  - concepts/progressive-autonomy-incident-resolution.md
  - concepts/coordination-cost-invariant.md
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Anthropic builds software in 2026 with Katelyn Lesse |
| Author | Gergely Orosz (The Pragmatic Engineer), with Katelyn Lesse |
| Type | Newsletter podcast recap (RSS, free tier) — body present |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-pragmatic-engineer-2026-11-25-how-anthropic-builds-software-in-2026-with-katel.md` |
| Retrieved | 2026-11-26 (published 2026-11-25) |
| File | `newsletter-rss-pragmatic-engineer-2026-11-25-how-anthropic-builds-software-in-2026-with-katel.md` |
| Pages | n/a |
| Read status | read — 12 numbered learnings present in the body |

## Narrative

This episode is not paywalled. The body carries twelve numbered takeaways from Katelyn Lesse, who
leads platform engineering at Anthropic and owns the Claude API, Claude Code and Claude Desktop
infrastructure. Her account is one senior engineer describing her own team. Tag claims as
`[TENTATIVE]`.

### 1. The Python to Rust rewrite

The Messages API serves every Claude token, including Claude Code and Claude Desktop. It does
authentication, tokenisation, billing and safety checks, then calls the GPU stack. It was a Python
monolith. The team optimised Python first, then rebuilt in Rust. The work took a few engineers about
five months. None of them were Rust experts.

The reason it worked is the verification shape, not the language. The existing Python service became
the test harness. The Rust service shadowed it, and the team iterated until responses matched. Lesse
estimates engineers read closely about **20%** of the generated Rust. Her rule:

> "As long as you can really boil something down to make it verifiable in some way, then you don't
> have to look at every single line of Rust code that's getting written."

That is the `@concepts/agent-completion-verification-gates.md` thesis in a production migration:
shadow traffic is the gate, and close reading is not. The same migration appears in the AINews digest
in this batch, with a detail this page lacks — agent teams reconciled the non-deterministic
differences. Two independent recaps raise confidence in the migration itself.

### 2. Claude reviews every pull request

A Claude code review classifier runs on all pull requests. It answers three questions: does this need
a human at all, how many human reviews does it need, and which team reviews it. Mechanical and
low-risk changes, such as an SDK version bump or a newer model id, can merge with no human. Flaky-test
fixes are reviewed by another Claude and then merged and deployed.

This is the direct answer to the review-capacity gap in `@concepts/agent-pr-volume-exceeds-human.md`.
Anthropic does not review harder. It routes, scores risk, and lets a deterministic class of change
pass without a human.

### 3. An agent is paged before a human

A Claude agent shadowed the API on-call rotation for months as training. The team now lets the agent
categorise an incoming alert first, before a human is paged. The stated long-term goal is for Claude
to handle incidents without waking a human. Lesse says they are not there yet.

This is staged promotion of autonomy on live operational data. See
`@concepts/progressive-autonomy-incident-resolution.md`.

### 4. Onboarding is "talk to Claude"

Claude is connected to the codebase and internal systems. New engineers ask it to explain how systems
work. It can generate interactive tutorials and visualisations. Orosz notes that OpenAI engineers use
Codex for the same job, citing an earlier episode.

### 5. Planning and coordination did not shrink

Lesse's team works with Inference, Research, Safety and App teams. Project kickoff still costs a lot
of alignment work. She says planning time has not changed much from pre-AI, and the average engineer
now spends **more time coordinating than implementing**. Filed to
`@concepts/coordination-cost-invariant.md`, because it qualifies the "code is cheap so engineering is
cheap" story.

### 6. Teams did not change shape

Teams remain two-pizza teams of about 5–8 people. Lesse gives two reasons: that size can hold a
complex system in view, and that size can staff an on-call rotation. Teams own systems and get paged.
The unit of ownership is the team, not the individual.

### 7. Engineers build more tooling

Product engineers now spend much more time building tools for their own work. One example: an engineer
built a Slack channel that runs a multi-agent team toward a single goal. It was not an assigned task.

### 8. Language knowledge matters less

Lesse invested heavily in learning languages before AI. Asked whether that now hurts, she says some
engineers never cared much about languages, and that engineers who do care still have work to do on
languages and frameworks themselves.

### 9. The coding interview is gone

Strong candidates were failing the coding interview because they no longer write code by hand. The
team phased it out. It is experimenting with interviews run together with coding agents. The design
and project-deepdive interviews are unchanged.

### 10. Promotions no longer use time to complete

Levels and the promotion process remain. Time to complete a project is meaningless when a year-long
project can take days. The replacement is measured impact: CPU saved, latency cut, incidents avoided.

### 11. The software factory

The episode names Anthropic's "software factory" and covers a product manager shipping a feature to
production. Filed to `@concepts/claude-code-software-factory.md`.

### 12. Company size

The post says Anthropic is publicly traded at a market capitalisation of about **$1 trillion**, with
about one tenth of the headcount of comparable companies. `[NEEDS VERIFICATION 2026-11-26]` — this is
a published number that nobody in this workspace has checked.

## Snippets

> "As long as you can really boil something down to make it verifiable in some way, then you don't
> have to look at every single line of Rust code that's getting written." [Source: `newsletter-rss-pragmatic-engineer-2026-11-25-how-anthropic-builds-software-in-2026-with-katel.md`]

> "Katelyn says that planning time has not changed much from 'pre-AI'. The average engineer actually
> spends more time coordinating than on implementation!" [Source: same]

> "Candidates who crushed other interviews were starting to fail the coding one because they no longer
> write code by hand." [Source: same]
