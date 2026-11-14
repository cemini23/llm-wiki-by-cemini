---
title: "Generation-verification gap — a produced artifact is not an accepted artifact"
type: concept
related:
  - sources/arxiv-controlharbor-control-design-coding-agents-2611.16867.md
  - sources/arxiv-analoglayoutworld-agentic-analog-layout-2611.16991.md
  - sources/newsletter-rss-latent-space-2026-11-13-ai-ambition-artcraft-cloned-photoshop-and-now-wa.md
  - concepts/harness-as-eval-artifact.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/harbor.md
  - entities/tools/analoglayoutworld.md
updated: 2026-11-14
---

## Raw Concept

What question does this page answer: for long-horizon engineering tasks, how wide is the gap between producing an artifact and proving it meets the specification? Sources: ControlHarbor (2611.16867), AnalogLayoutWorld (2611.16991), and the ArtCraft talk.

## Narrative

Both benchmark papers use a single checkable artifact as the task unit. ControlHarbor takes one Python controller file. AnalogLayoutWorld takes one GDS layout from a fixed netlist. Both grade the artifact against an external specification, not the transcript.

The gap is wide and it is measurable:

| Benchmark | Artifact produced | Meets acceptance |
|-----------|-------------------|------------------|
| AnalogLayoutWorld | 91.1% GDS layouts | 21.3% |
| ControlHarbor | Parity controllers reached in a minority of sessions | 1–3 of 9 sessions per task |

Agents rarely fail to produce something. They fail to prove it.

Four causes appear in both papers.

1. **The specification has more than one axis.** A controller that is fast is not robust. A layout that passes DRC is not compact or electrically sound. Acceptance needs all axes at once.
2. **Visible tests are weak evidence.** ControlHarbor calculates a 0.45 failure probability from five visible seeds, against 0.072 from 40 held-out seeds. A pass on the seeds the agent can see does not carry.
3. **Some quality checks are outside the prescribed suite.** In AnalogLayoutWorld, two layouts pass every functional test, and a via-current check still separates them.
4. **Scale cuts quality.** AnalogLayoutWorld finds a negative correlation between device count and score (rho = −0.73). ControlHarbor sees shorter sessions on light plants and full-hour sessions on hard ones.

The ArtCraft talk gives an industry version. PhotoCraft is reported at 60% parity, while its GitHub claims 76% for feature breadth and 46% for professional readiness. Three numbers measure the same artifact. The most useful one is the lowest.

**Authorship boundary.** ArtCraft's rule is a practical consequence. Agents fit where the artifact is fixed and checkable: desktop apps, games, immutable deliverables. Humans keep schema migrations and API design, where a wrong change is costly and hard to reverse.

For Cemini: state the acceptance test before the agent writes the artifact, and keep the held-out set outside the agent's reach.

## Snippets

> "91.1% of attempts produce GDS layouts, but only 21.3% satisfy the benchmark's acceptance criteria." [Source: arxiv-2611.16991-analoglayoutworld-an-open-benchmark-for-agentic.pdf p.1]

> "the designed controllers … reach the RL return on every parity task, but only in a minority of sessions" [Source: arxiv-2611.16867-controlharbor-a-benchmark-for-control-design-by.pdf p.1]
