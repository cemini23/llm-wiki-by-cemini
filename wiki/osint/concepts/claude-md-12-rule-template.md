---
title: "CLAUDE.md 12-rule template (Karpathy → Forrest Chang → Mnilax)"
type: concept
tags: [concept, claude-code-prompting, claude-md, agent-orchestration, prompting-discipline, karpathy-derivative, k41]
keywords: [claude-md-12-rules, mnilax-extension, forrest-chang-4-rules, karpathy-jan-2026-thread, checkpoint-discipline, fail-loud, token-budget, surface-conflicts]
related:
  - sources/x-docx-polymarket-claude-md-2026-04-23.md
  - entities/people/forrest-chang.md
  - entities/people/mnilax.md
  - sources/llms-get-lost-multi-turn-laban-2025.md
  - concepts/llms-get-lost-mitigation-audit.md
  - concepts/agent-trajectory-triage-signals.md
  - entities/tools/openspec.md
maturity: draft
created: 2026-05-13
updated: 2026-05-15
---

## Relations

- @sources/x-docx-polymarket-claude-md-2026-04-23.md — primary source (Section 2)
- @entities/people/forrest-chang.md — 4-rule originator
- @entities/people/mnilax.md — 12-rule extension author
- @sources/llms-get-lost-multi-turn-laban-2025.md — operational sibling (Rule 10 checkpoint discipline ≈ measured premature-commitment failure mode)
- @concepts/agent-trajectory-triage-signals.md — same failure-mode-mitigation lineage

## Raw Concept

What prompted this page: K41 ingest of X.docx Section 2 — Mnilax's 12-rule extension of Forrest Chang's 4-rule CLAUDE.md template (which derives from Karpathy's late-January-2026 X thread on Claude code-writing failures).

## Narrative

### Lineage

1. **Andrej Karpathy (late Jan 2026, X thread)** — complaint about silent assumptions, over-engineering, unverified completions in Claude code work. Diagnostic-only; no template.
2. **Forrest Chang (GitHub repo `forrestchang/andrej-karpathy-skills`, created 2026-01-27)** — 4-rule template distilling Karpathy's complaints into prescriptive form. Repo hit ~110k stars by early May 2026 and ~130k by mid-May [CONFIRMED 2026-05-15 — live GitHub API + trade-press coverage; see @entities/people/forrest-chang.md].
3. **@Mnilax (X article, ~Apr 2026)** — 8 additional rules covering May 2026 agent-orchestration failure modes Forrest Chang's 4 don't address.

### The 4 Forrest Chang rules

1. **Think Before Coding** — no silent assumptions, surface tradeoffs
2. **Simplicity First** — minimum code that solves the problem
3. **Surgical Changes** — touch only what you must
4. **Goal-Driven Execution** — define success criteria; loop until verified

### The 8 Mnilax additions (rules 5-12)

Per @Mnilax's article (paraphrased; not verbatim — full text in source page):

5. **Token Budget** — keep CLAUDE.md under 200 lines; budget context allocation
6. **Fail Loud** — no silent fallbacks; errors should surface immediately
7. **Checkpoint Discipline** — after every meaningful step, restate goal + state + next action
8. **Surface Conflicts** — when user instructions contradict each other or earlier decisions, flag explicitly
9. **No Mid-Stream Refactor** — finish the requested task first; defer cleanup to a separate ask
10. **Verify Before Claim** — never say "done" without running the actual verification
11. **One In-Progress at a Time** — concurrency discipline for multi-step work
12. **State Resumption Recipe** — every CLAUDE.md should explain how to resume after compaction/context-loss

### Empirical claims (author-asserted, not externally verified)

@Mnilax tracked 50 tasks × 30 codebases × 6 weeks across three configurations:

| Configuration | Mistake rate | Compliance |
|---|---|---|
| No template | 41% | n/a |
| Karpathy 4 (Forrest Chang) | ~9% | 78% |
| Mnilax 12 | **3%** | 76% |

**Methodology caveats**: not peer-reviewed; no open methodology repo Cemini has visibility on; author-asserted only. Treat as illustrative not measured.

### Cross-paper corroboration

Rule 10 (checkpoint discipline) is the **operational sibling** of the measured premature-commitment mechanism in @sources/llms-get-lost-multi-turn-laban-2025.md (39% multi-turn performance drop, mechanism: LLMs commit to early hypotheses and cannot revise). Mnilax's mitigation = Laban et al.'s explanation, independently arrived at.

### Cemini posture

- **Structural framework** is operationally portable to Cemini's CLAUDE.md hygiene. Current Cemini CLAUDE.md is **322 lines** — over Mnilax's claimed 200-line ceiling.
- **Rule-by-rule application**:
  - **Already in Cemini practice**: Rules 1-4 (Forrest Chang), 6 (fail loud), 8 (surface conflicts), 10 (verify before claim), 11 (one in-progress — see TodoWrite discipline)
  - **Partial in Cemini**: Rule 5 (token budget — currently over), Rule 7 (checkpoint discipline — present but not codified), Rule 12 (state resumption — `hot.md` + session-start ritual)
  - **Gap**: Rule 9 (no mid-stream refactor) — Cemini does this implicitly but doesn't codify it
- **Empirical numbers** (41% → 3%) illustrative not measured; the structural framework is useful regardless
- **Action item candidate**: a CLAUDE.md audit pass against this 12-rule taxonomy is a low-cost, high-leverage tech-debt task

## Snippets

> "The 200-line CLAUDE.md isn't a style choice — past 200 lines the model starts down-weighting instructions in proportion to position." [Source: x.docx Section 2, paraphrased Mnilax]
