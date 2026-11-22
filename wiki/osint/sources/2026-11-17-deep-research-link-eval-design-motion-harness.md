---
title: "Deep Research link evaluation — design and motion skills, agent memory and cost control, verification (2026-11-17)"
type: source
related:
  - concepts/agent-link-evaluation-gates-v1013.md
  - sources/2026-11-16-deep-research-link-eval-agentic-harnesses.md
  - "@ccc-wiki/concepts/design-skill-cluster-2026-11.md"
  - "@ccc-wiki/concepts/repeated-correction-mining.md"
  - "@ccc-wiki/concepts/agent-verification-patterns.md"
  - "@ccc-wiki/concepts/agent-presentation-generation.md"
  - "@gambling-wiki/concepts/nfl-matchup-projection-feeds.md"
  - "@ccc-wiki/entities/bot-browser.md"
  - sources/2026-11-22-deep-research-link-eval-abliterated-harness.md
updated: 2026-11-17
---

## Raw Concept

- **Title:** Cemini Multi-Wiki Link Evaluation (batch C)
- **Author:** Deep Research evaluation run, operator-supplied rubric v10.12 under v10.13 discovery
- **Type:** vendor-link evaluation report (DOCX)
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/Cemini Multi-Wiki Link Evaluation.docx`
- **Retrieved:** 2026-11-17
- **Pages:** 20 URL records
- **Read status:** read

Batch theme: AI coding-agent harnesses, UI/UX design and motion skills, agent memory
and cost-control controllers, automated verification workflows, presentation
generators, and NFL matchup projections.

## Narrative

This is the first batch with **no winners**. Zero URLs earned Integrate or Extract.
Fifteen graded Context, one graded Watch, and four graded UNAVAILABLE. Every URL
routed `wiki-only`.

The rubric explains it. Gate 3 of v10.13 freezes new local Claude Code hooks, skills,
plugins, routers, and `.cursor/rules` wires. Sixteen of the twenty URLs are exactly
that — agent skills for a workstation. The freeze caps them at Context regardless of
quality, and several are high quality.

### Graded outcomes

| Tier | Count | Items |
|------|-------|-------|
| Integrate | 0 | — |
| Extract | 0 | — |
| Context | 15 | `ui-ux-pro-max-skill`, `benjitaylor/skills`, `make-interfaces-feel-better`, `hallmark`, `emilkowalski/skills`, `muse-agent-operations-kit`, `brijr/gui`, `nomore`, `stalemap`, `TokenEconomizer`, `agent-beacon`, verification blog, `bot-browser`, `frontend-slides`, `ppt-master` |
| Watch | 1 | Armchair Logan NFL projections |
| UNAVAILABLE | 4 | `openclaw-ci-cost-reduction`, `landmines`, `rulebook`, `claude-code-lean-agents` |

### The UNAVAILABLE verdicts are wrong

The report graded four URLs UNAVAILABLE — "inaccessible" or "404" — and skipped
analysis under its anti-hallucination rule. Direct checks on 2026-11-17 return
**HTTP 200 for all four**:

| URL | Reported | Actual |
|-----|----------|--------|
| `vincent.build/openclaw-ci-cost-reduction/` | unreachable | 200, full article on cutting OpenClaw CI cost |
| `github.com/devanshranjan10/landmines` | 404 | 200, MIT, 10 stars, known open bugs in pinned dependency versions |
| `github.com/disinfeqt/rulebook` | 404 | 200, MIT, 22 stars, native macOS app to edit CLAUDE.md rules |
| `github.com/mdalexandre/claude-code-lean-agents` | 404 | 200, MIT, 19 stars, two subagents at ~7.5k tokens |

[CONFIRMED — curl 2026-11-17]

This matters beyond bookkeeping. Three of the four are real tools that address the
same gaps as graded Context items, and one is a cost-reduction case study that belongs
with the memory and cost-control cluster. A batch reported as "four dead links" was in
fact a full twenty live URLs.

The pattern: a fetch failure was recorded as a missing resource. A 404, a timeout, and
a rate limit are not the same verdict, and none of them means the resource does not
exist.

### What the batch is actually worth

Not queue entries — the freeze holds — but three coherent reference clusters:

- **Design and motion skills** (six URLs, all MIT or unlicensed)
- **Repeated-correction mining and cost control** (`nomore`, `stalemap`,
  `landmines`, `lean-agents`, `TokenEconomizer`, `agent-beacon`)
- **Verification patterns** (the Claude Code team blog, the muse defect protocol)

Plus two presentation generators and one betting feed worth watching.

### Licence notes

`benjitaylor/skills` shows **no SPDX licence** on the GitHub API despite 3.5k stars.
Under Gate 1 that is all rights reserved, so nothing may be copied from it. It is
Context only and would be excluded from any queue on that ground alone.

Every other item is MIT, except `brijr/gui` which is Apache-2.0.

## Snippets

> Actionable budget: Max 2 URLs total across this batch may earn Integrate or Extract
> under v10.12, subject to v10.13 Uncapped Discovery on true product merit and Gate #3
> (Workstation Harness Freeze).
> [Source: Cemini Multi-Wiki Link Evaluation.docx, research plan]

> The repository `https://github.com/devanshranjan10/landmines` is inaccessible. Per
> strict anti-hallucination rules, it is graded UNAVAILABLE.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 12]

## Dead Ends

- **Recording a fetch failure as a missing resource.** All four UNAVAILABLE URLs were
  live. Re-check a dead URL before accepting the verdict.
- **Treating "no winners" as "nothing to learn".** The batch produced four useful
  reference clusters; none of them needed a code extraction to be worth keeping.
