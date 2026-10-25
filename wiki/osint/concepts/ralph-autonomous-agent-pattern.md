---
title: Ralph autonomous-agent pattern — file-based memory for Claude Code loops
type: concept
tags: [concept, autonomous-agent, claude-code, prompt-engineering, file-based-memory, ralph, workflow]
keywords: [ralph, autonomous coding, prd.json, progress.txt, PROMPT_build.md, PROMPT_plan.md, agent loop, fresh context, planning mode, building mode]
related:
  - sources/evaluating-github-repos-trading-stack-2026-05-12.md
  - sources/autonomous-agent-meta-prompt-2026-05.md
  - entities/tools/awesome-ralph.md
  - concepts/tool-evaluation-framework.md
  - entities/tools/smart-ralph.md
  - entities/tools/she-safety-harness.md
  - sources/arxiv-2608.09885-she-safety-harness-2026-08-11.md
maturity: draft
created: 2026-05-12
updated: 2026-08-11
---

## Relations

- @entities/tools/smart-ralph.md
- `@sources/evaluating-github-repos-trading-stack-2026-05-12.md` — Doc1 URL 1 (`awesome-ralph` evaluation)
- `@sources/autonomous-agent-meta-prompt-2026-05.md` — sibling "THE FULL PROMPT" meta-template
- `@entities/tools/awesome-ralph.md` — repo entity
- `@concepts/tool-evaluation-framework.md` — sibling workflow concept
- `@ccc-wiki/entities/patterns/ralph-loop.md` — CCC-side adoption brief for the same pattern (laptop-only meta-wiki on Cemini's Claude Code workflow)

## Raw Concept

Distilled from `github.com/snwfdhmp/awesome-ralph` (Doc1 URL 1, Gemini eval verdict: Steal-from). Ralph is an autonomous-AI-coding pattern that runs Claude Code / Amp / OpenCode in continuous loops until requirements are demonstrably fulfilled. Critical design choice: **isolate each iteration with a fresh context window**, manage state via persistent file structures rather than relying on degrading long-context coherence.

## Narrative

### Why fresh-context-per-iteration

Long Claude Code sessions degrade as context fills:
- Earlier instructions get forgotten / overridden
- File-state snapshots from earlier in the session conflict with current disk state
- Hallucinations compound once the model "remembers" something inaccurate from earlier in the same turn

Ralph's answer: **don't extend context — checkpoint to disk and restart**. Each loop iteration is a fresh agent with the same persistent-file state. The agent re-reads `prd.json` + `progress.txt` + recent git log + relevant code, decides next step, executes, commits, exits. Next loop iteration: fresh context, same persistent state.

### The three persistent artifacts

1. **`prd.json`** — Product Requirements Document. Structured task list: user stories, acceptance criteria, completion status per task. Source of truth for "what done looks like."
2. **`progress.txt`** — ledger. Append-only log of what the agent did each iteration. Survives across restarts.
3. **Git history** — the actual code state. Each loop iteration commits its work.

### The two-mode workflow

**Plan mode** — gap analysis without implementation:
- Read `prd.json`, identify next incomplete task
- Read existing code, identify the gap between current state and target state
- Output: a `PROMPT_build.md` describing the implementation plan
- **Does not write code.**

**Build mode** — execute the plan:
- Read `PROMPT_build.md`
- Implement the change
- Run tests
- Commit
- Update `progress.txt`

Loop: plan → build → verify → plan → build → verify... until `prd.json` reports all tasks complete.

### Two segregated prompt files

- `PROMPT_plan.md` — system prompt for plan-mode invocations
- `PROMPT_build.md` — system prompt for build-mode invocations

Keeping them separate prevents the planner from drifting into implementation and the builder from second-guessing the plan.

### What's reusable for Cemini / workspace (Steal-from candidates)

Per the Gemini eval verdict (Steal-from, MIT, no transitive license risk):

1. **`prd.json` schema** — applicable to any multi-step workspace task. Cemini's K-series ingest workflow is itself loop-able (preingest_check → read → discuss → write pages → lint → commit → push). A `K-series-prd.json` template could formalize what's currently informal.

2. **`progress.txt` ledger pattern** — Cemini already has `wiki/log.md` (append-only). The Ralph progress.txt is for *agent-loop state* specifically, not human-readable narrative. Different artifact for different consumer.

3. **Segregated `PROMPT_*.md` files** — workspace-laptop has CLAUDE.md as the single system prompt. A `PROMPT_plan.md` + `PROMPT_build.md` split could be experimented with for specific workflows (e.g., the brief-staging workflow has a clear plan-phase and a clear ship-phase).

### What's NOT reusable

- Ralph's shell-script orchestration loops — not Python, not safe for production trading server, and Cemini's existing skill / agent infrastructure (FastMCP, LangGraph) already handles loop orchestration.
- Bash-driven autonomous Git operations — operational hazard (per Gemini eval section 6 risks).

### Comparison to "THE FULL PROMPT _goal" template

Sibling source — also a meta-prompt template, but single-shot (one big invocation with `/goal`, context, success criteria, operating rules) rather than loop-based. Different abstraction: Ralph is "how to structure a loop," THE FULL PROMPT is "how to specify one task to a non-looping agent." Both are reference templates for prompt-engineering hygiene.

### Risks (per source eval)

- Autonomous git operations with unconstrained write access → destructive operations from hallucinating agents (force-overwrites, erroneous merges).
- Downstream-tool risk — awesome-ralph references third-party Rust orchestrators + CLI tools, each requiring independent license/security audit.

### Verification needed

- `[OPEN QUESTION 2026-05-12]` `awesome-ralph` commit velocity + top-contributor list (Gemini eval flagged: "could not be programmatically extracted from the retrieved primary sources").

## Snippets

From Gemini eval (Doc1 URL 1):

> Rather than relying on continuous context windows that degrade over time, the methodology isolates iterations, granting each agent loop a fresh computational context. The system manages state and project memory exclusively through persistent file structures, specifically utilizing Git history, a progress.txt ledger, and a structured prd.json file to track user stories and task completion statuses.

## Dead Ends

- Trying to make Ralph the *primary* orchestrator for Cemini → eval Reject grade on production-stack fit (shell + bash + git autonomy = wrong for 24/7 trading). Steal-from-only.
- Wiring shell-scripted git autonomy into the workspace laptop → operational hazard for the curated wiki repository.
