---
title: "Latent Space AINews — math proofs are landing faster than we can read them (2026-11-25)"
type: source
related:
  - concepts/model-vs-harness-performance-variance.md
  - concepts/frontier-model-release-cadence.md
  - concepts/benchmark-maintenance-debt.md
  - "@osint-wiki/entities/people/thariq-trq212.md"
updated: 2026-11-26
read_status: read
maturity: draft
---

## Raw Concept

| Field | Value |
|-------|-------|
| Title | [AINews] Math Proofs Are Landing Faster Than We Can Read Them |
| Author | Latent Space AINews (swyx et al.) |
| Type | Daily digest (RSS, free tier) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/newsletter-rss-latent-space-2026-11-25-ainews-math-proofs-are-landing-faster-than-we-ca.md` |
| Retrieved | 2026-11-26 (published 2026-11-25) |
| File | `newsletter-rss-latent-space-2026-11-25-ainews-math-proofs-are-landing-faster-than-we-ca.md` |
| Pages | n/a |
| Read status | read |

## Narrative

The digest leads with AI-generated mathematics. That is noise for CCC. Four sections carry
harness-relevant material, and one carries a hard qualification of the ShellBench result.

### The harness datum: OpenCode is a weak harness

A community benchmark ran 7 local Qwen 3.8 builds on 54 tasks, fully autonomous, on one RTX 5090.
The author frames the result as a floor, not a best case, and gives the reason. On FrontierHarness,
OpenCode passes about **50%** and DSH Creator passes about **63%**. Same task class, same rough
model class, 13 points apart.

This is the coding-task branch of `@concepts/model-vs-harness-performance-variance.md`. It also
matches the qualification the workspace already holds from ShellBench. ShellBench puts the harness
effect for everyday tasks at roughly 3 points, against about 44 points of model span. Here, on a
coding harness, the harness moves the score by about 13 points. **Read the task class before quoting
either number.** OpenCode is also the tool the workspace rejected for a `/route` mid-lane swap, so
this is a second, independent signal that its autonomy quality is the weak part.

### Benchmark hygiene

- Eugene Yan reviewed 12 public evals and found buggy graders and misconfigured harnesses.
- FrontierPhysics (54 physicist-written tasks) shows a numeric-pass against review-pass gap. Gemini 4
  Neon passes numeric checks 54% of the time and review 28% of the time.
- AA-Robotics-Sim: seven of nine models broke a dish they were told was fragile.
- RSI reading list: harness overfitting and grader validity.

All four are `@concepts/benchmark-maintenance-debt.md` cases. The FrontierPhysics gap is the clearest
one: a checker that passes is not a result that is correct.

### Cost and routing

- ComputeWise: agents waste about 48% of GPU time.
- Delegent: routing routine subtasks to a local model cut frontier cost 59–67%.
- Anthropic's Rust API migration used the old service as an oracle, with agent teams reconciling
  non-deterministic differences. The Pragmatic Engineer interview in this batch gives the same
  migration in detail.
- Google reportedly raised effective subscription usage about 75% through caching and harness work.

The Delegent figure is already filed at `@concepts/timeout-cascade-cost-aware-routing.md`.

### Model releases

Gemini 4 Neon, GPT-6.2 Astra, MAI-Code-2.1 and GLM-5.4 all appear with scores. Filed to
`@concepts/frontier-model-release-cadence.md`. The one structural item is Inkling 2 Mini, a looped
transformer at 48 effective layers from 3.4B unique active parameters, free to train on Tinker.

### People

Thariq Shihipar announced his move from Anthropic to OpenAI. This is the second senior
Anthropic-to-OpenAI move in recent months, after Cat Wu. See
`@osint-wiki/entities/people/thariq-trq212.md`. The same batch also holds his Latent Space episode,
which was recorded before the move:
`@sources/newsletter-rss-latent-space-2026-11-25-the-revolution-vs-the-renaissance-thariq-shihipa.md`.

Everything here is a newsletter report, not a paper read in this workspace. Tag as `[TENTATIVE]`.

## Snippets

> "The author cautions OpenCode is a weak fully autonomous harness—citing FrontierHarness where
> OpenCode is ~50% pass vs DSH Creator ~63%—so results are framed as a floor, not best-case assisted
> performance." [Source: `newsletter-rss-latent-space-2026-11-25-ainews-math-proofs-are-landing-faster-than-we-ca.md`]

> "Neon passes numeric checks most often (54%) but passes review only 28% of the time." [Source: same]

> "ComputeWise: Agents waste ~48% of GPU time." [Source: same]
