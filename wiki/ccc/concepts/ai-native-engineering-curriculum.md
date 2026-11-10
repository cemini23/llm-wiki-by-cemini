---
title: "AI-native engineering curriculum — what to teach when the agent writes the code"
type: concept
related:
  - sources/newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md
  - sources/newsletter-rss-latent-space-2026-11-08-one-million-ai-engineer-special-how-stanford-tea.md
  - sources/newsletter-rss-pragmatic-engineer-2026-11-05-scaling-slack-and-github-with-maude-lemaire.md
  - sources/newsletter-rss-pragmatic-engineer-2026-11-06-the-pragmatic-summit-2027.md
  - concepts/foundational-work-verification.md
  - concepts/subagent-orchestration.md
updated: 2026-11-10
---

## Raw Concept

Question this page answers: which engineering skills survive when a coding agent can finish the previous year's assignment in one prompt?

Synthesised from the Stanford CS146S interview, the Pragmatic Engineer Slack/GitHub episode, and the Pragmatic Summit teaser.

## Narrative

Mihail Eric teaches CS146S, *The Modern Software Developer*, at Stanford, and leads AI at Monaco. The course question is blunt: a coding agent finishes last year's homework in one prompt.

The redesign changed three things:

1. **The assignment moved to open source.** Students contribute a patch to a real project. The maintainer reviews it. The student must learn whether the maintainer wants the change, why the code behaves as it does, and what else the patch breaks.
2. **Understanding the diff became the graded skill.** Geoffrey Litt's explain-diff approach turns a change into a visual walkthrough and then quizzes the author. The useful signal is which question forces a return to the code.
3. **Ownership became a rule.** "You buy to learn, and you build to keep." Monaco evaluated code-review products and kept Devin. It built agent workspaces, because a background agent needs a place to run the product, reproduce the failure, and test the patch.

One system, two readers: **Hal** answers an engineer's investigation request with a pull request and answers a salesperson's question with an explanation. Same investigation, two output shapes.

The bottleneck moved. The Faros study cited in the episode: high-AI-adoption teams merged 98% more pull requests, while review time was 91% longer. Review is now the constraint, which is the argument for scoping each change tightly.

### The connecting theme

Both episodes converge on the same skill. The Pragmatic Engineer episode has Maude Lemaire separating foundational from non-foundational work and verifying LLM output only for the first. The Stanford course grades whether a student understands the patch. Both say the scarce skill is **judgement about which change belongs**, not the ability to produce a change.

That is the same claim WorkflowArena makes quantitatively: orchestration quality is a separate, measurable capability.

### For Cemini

The workspace already splits architect and implementer. The curriculum adds a concrete practice worth borrowing: a diff-reading exercise after each implementer run, where the architect must answer one question that requires reopening the file.

## Snippets

> "You can ask an agent to implement a feature in an afternoon. You still have to find out whether the maintainer wants it, why the code behaves the way it does, and what else your patch might break." [Source: newsletter-rss-latent-space-2026-11-08-how-stanford-teaches-ai-native-engineering-mihai.md]
