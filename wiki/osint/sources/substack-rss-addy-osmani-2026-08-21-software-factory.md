---
title: "Osmani — human judgment relocates in the software factory"
type: source
tags: [ccc, factory, verification, harness]
keywords: [software-factory, Warp-labels, Vercel-taxonomy, verification-budget, comprehension-debt]
related:
  - concepts/wayfinder-fog-of-war-planning.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
read_status: skimmed
---

## Relations
- @concepts/wayfinder-fog-of-war-planning.md
- @concepts/skill-misevolution.md
- @concepts/agent-toolkit-routing-research-backlog.md

## Raw Concept
- **title:** Human judgment doesn't leave the software factory. It relocates.
- **author:** Addy Osmani
- **type:** Substack essay
- **location:** research to be indexed/substack-rss-addy-osmani-2026-08-21-human-judgment-doesnt-leave-the-software-factory.md
- **retrieved:** 2026-08-21
- **pages:** full essay
- **read-status:** skimmed

## Narrative
A software factory is a repeatable, event-driven loop (issues → isolated run → implement/test → human gate). Stock Claude/Codex + SPECs is enough until you need a queue, locks, and consistent runs.

**Warp labels as queue+lock:** ready-to-implement / ready-to-spec / needs-info / wait-to-implement. Only `ready` is picked up. Label is queue, lock, and human parking.

Human stays in steering, blocked notifications, handoff (state+evidence), and merge. Encode taste in the environment (types, tests, mutation tests, scanners, architecture lints). Number of checks ≠ quality — tune signal/noise.

**Verification budget** like a perf budget: cheap lint/types early; heavy tests/mutation/browser/security near draft PR. Green can lie (agents edit tests or drop auth providers to pass).

**Vercel taxonomy:** success / flawed / blocked / manual; only success ships. Pair with per-stage timing: Osmani movies-app 82-minute sample run; favorites with two rejections 56 min vs 7 min with no rejections.

**Comprehension debt:** parallel sessions go cold; he merged a favorites feature he could not later explain. Persist trajectory/lessons, not just the diff. Autonomy is earned per project via verification, not a global slider. Untrusted GitHub/Slack input → sandbox + least-privilege secrets.

Steal: issue-label state machine; Vercel run taxonomy + draft PRs; persist run trajectory so review does not depend on compacted chat. Complements wayfinder map/ticket.

## Snippets
> Warp mention triaging every incoming issue into one of four states — ready-to-implement, ready-to-spec, needs-info, wait-to-implement — and the label is what fires the next agent. This label does a few jobs in one go: it’s the queue, the lock … [Source: https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software (retrieved 2026-08-21)]

> In their software factory, Vercel marks every agent run as “success”, “flawed”, “blocked” or “manual” and only “success” ships to production. [Source: https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software (retrieved 2026-08-21)]

> I returned to the code, and I couldn’t explain to you how the feature worked. … my understanding hadn’t kept up pace with all of the code that had been building up. [Source: https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software (retrieved 2026-08-21)]
