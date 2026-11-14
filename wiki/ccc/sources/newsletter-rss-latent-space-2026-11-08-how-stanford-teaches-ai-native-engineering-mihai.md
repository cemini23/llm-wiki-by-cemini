---
title: "Latent Space — How Stanford teaches AI-native engineering (Mihail Eric, CS146S)"
type: source
related:
  - concepts/ai-native-engineering-curriculum.md
  - concepts/foundational-work-verification.md
updated: 2026-11-10
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | How Stanford Teaches AI-Native Engineering — Mihail Eric, Monaco |
| Author | Latent Space (interview with transcript) |
| Type | newsletter / podcast notes (RSS) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md` |
| Retrieved | 2026-11-10 |
| Published | 2026-11-08 |
| Read status | read (editorial section and transcript opening; full transcript sampled) |

## Narrative

Mihail Eric teaches **CS146S, The Modern Software Developer** at Stanford and leads AI at Monaco. The interview covers the course, then the parts of it that held up in a real engineering team.

The course problem is stated cleanly: a coding agent can finish last year's homework in one prompt. In the second run, part of the coursework became a contribution to an open-source project. The maintainer reviews the student patch. The student still has to learn whether the maintainer wants the change, why the code behaves as it does, and what else the patch might break.

The episode offers a transferable exercise: use an explain-diff skill on a patch your own agent just wrote, then answer its questions. The useful signal is which question forces you to reopen the code.

At Monaco, the team applies a rule about ownership:

- **Buy to learn, and build to keep.** They evaluated code-review products and kept using Devin.
- **Agent workspaces were built, not bought.** A background agent needs a place to run the product, reproduce a failure, and test a patch. That depends on the team's own cloud setup.

The result is **Hal**, one system with two readers. An engineer asks it to investigate a failure and open a pull request. A salesperson asks how the product works and needs an explanation. Both are legitimate outputs of the same investigation.

The interview cites the Faros study: teams with high AI adoption merged 98% more pull requests, while pull request review time was 91% longer. That is the bottleneck moving, not disappearing.

Related notes in the same episode: Basis's Authority Map (where an agent looks for current behaviour, earlier decisions, and intent), Stripe's Minions (background coding agents with a path to an engineer-reviewed pull request), and Boris Cherny's steps of AI adoption.

## Snippets

> "What do you assign when a coding agent can finish last year's homework in one prompt?" [Source: newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md]

> "You buy to learn, and you build to keep." [Source: newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md]

> "Teams with high AI adoption merged 98% more PRs, while their PR review time was 91% longer." [Source: newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md]
