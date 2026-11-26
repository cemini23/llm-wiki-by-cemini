---
title: "Coordination cost does not fall with implementation cost"
type: concept
related:
  - sources/newsletter-rss-pragmatic-engineer-2026-11-25-how-anthropic-builds-software-in-2026-with-katel.md
  - concepts/claude-code-software-factory.md
  - concepts/agent-pr-volume-exceeds-human.md
  - concepts/agent-completion-verification-gates.md
  - concepts/progressive-autonomy-incident-resolution.md
updated: 2026-11-26
maturity: draft
---

## Raw Concept

Question this page answers: if an agent can write the code in days, what part of engineering stays
expensive?

Synthesised from one interview: Katelyn Lesse, who leads platform engineering at Anthropic, on The
Pragmatic Engineer (2026-11-25). One senior engineer describing her own team, so tag `[TENTATIVE]`.

## Narrative

**The observation.** Implementation got cheap. Coordination did not. Lesse says planning time has not
changed much from pre-AI. Her team works across Inference, Research, Safety and App teams, and a
project kickoff still costs a lot of alignment work. Her summary: the average engineer now spends
more time coordinating than implementing.

**What did not change either.** Teams are still two-pizza teams of about 5–8 people. Lesse gives two
reasons that are about the work, not about habit: that size can hold a complex system in view, and
that size can staff an on-call rotation. Ownership is team-level and the team gets paged.

**Why this matters for the harness claim.** The workspace holds a "harness over model" position and a
large body of work on making the implementer cheaper. This source says the expensive part moved, not
that it disappeared. A faster implementer makes the coordination step more frequent, because more
projects start and fewer stall on code. Cheaper generation raises the cost of agreeing on what to
generate.

**Where the cost shows up.** Three places in the same interview:

- The Rust migration needed a shadow-traffic gate, because nobody could read all the generated code.
- A code review classifier now decides how many human reviews a change needs, because review capacity
  did not grow with change volume.
- Promotions dropped time-to-complete, because a long project can finish in days and the duration
  says nothing about impact.

**Practical rule.** Do not budget an agentic project as if the code were the only cost. Budget the
alignment, the review routing and the on-call ownership. See
`@concepts/agent-pr-volume-exceeds-human.md` for the review side and
`@concepts/claude-code-software-factory.md` for the production side.

**Status.** Single account, from a company that sells agent tooling. The direction matches the
review-capacity evidence already held in the workspace. The size of the effect is not measured here.

## Snippets

> "Katelyn says that planning time has not changed much from 'pre-AI'. The average engineer actually
> spends more time coordinating than on implementation!" [Source: `newsletter-rss-pragmatic-engineer-2026-11-25-how-anthropic-builds-software-in-2026-with-katel.md`]

> "Teams at Anthropic are still two-pizza teams of around 5-8 people. Katelyn says it's because this is
> the right size for understanding a complex system and staffing an oncall rotation." [Source: same]
