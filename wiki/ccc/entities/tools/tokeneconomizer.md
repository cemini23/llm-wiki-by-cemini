---
title: "TokenEconomizer — micro-skills, tool pruning, loop guard (Apache-2.0)"
type: entity
tags: [tool, claude-code, codex, cost, context, microsoft]
keywords: [tokeneconomizer, micro-skills, tool pruning, loop guard, swe-bench, harness]
related:
  - "@osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md"
maturity: draft
created: 2026-11-02
updated: 2026-11-02
---

## Raw Concept

Surfaced by @osint-wiki/sources/eval-multi-wiki-link-revenue-v10.10-batch-c-2026-11-02.md, URL 20, **Integrate** tier. Routed to Atto and Collectibles agent sessions, and to CCC.

The question this page answers: **what can cut agent cost without touching the agent?**

## Narrative

### What it is

Microsoft, **Apache-2.0**. Three optimisations that sit outside the agent and require no change to agent internals.

**1. Micro-skills.** Extract confirmed repository facts — the correct test command, build steps, environment variables, generated-file paths — after about three sessions. Inject them at session start. Prune facts that are later contradicted.

This is the highest-value piece. The most expensive recurring agent error is re-deriving something already known and getting it wrong the same way.

**2. Tool pruning.** Drop tools that go unused across enough prompts and sessions. Applied through each agent's own settings, and **reversible**.

**3. Failure-loop intervention.** A judge model checks whether a turn is stuck. If so, redirect. If it stays stuck, tell the user how to stop it.

### Phase-0, 2026-11-02 — the metric is cost, not tokens

The report states the tool "cuts Claude Code and Codex token burn by 18.4%–30.9%".

The README reports **cost**: "18.4–30.9% lower mean cost" on SWE-Bench — 277 tasks across six repositories and five agent–model combinations, lower in **all 30** cells, per-combination range 5–40%. Web-Bench 16–21% lower. Two security-auditing benchmarks 6–20% lower. Pass@1 improved in 4 of 5 combinations.

Two corrections follow:

- **It is cost, not token count.** Cost depends on the model mix as well as token volume, so a cost saving does not translate one-for-one into a context saving.
- **The benchmark is software engineering**, not record triage, not comp ingestion. The transferability to Atto and Collectibles is plausible but unmeasured.

Checked: **Apache-2.0** confirmed at the LICENSE file.

### The privacy question

Learned state lives in **`~/.tokeneconomizer`**. Micro-skills extract facts from your repository and keep them there.

For Atto, that directory becomes a new place where repository facts accumulate. The Atto boundary is about vault records and family data, not build commands — but the operator should know the directory exists, should know what is in it, and should confirm that no vault path or record content is ever extracted into a micro-skill.

Make that an explicit check, not an assumption.

### Recommendation

Adopt **micro-skills and tool pruning**. Both are reversible, both are mechanical, and both target real waste.

Treat the loop guard as optional: a judge model inspecting turns is another model call, and on a local-first setup the round-trip may cost more than the loop it catches.

### Status

Integrate. Audit `~/.tokeneconomizer` before trusting it near Atto.

## Snippets

> "18.4–30.9% lower mean cost" on SWE-Bench, 277 tasks across six repositories and five agent–model combinations, lower in "all 30" cells. [README, fetched 2026-11-02]

> "Apache 2.0; see LICENSE." [README, fetched 2026-11-02]

> Learned data is stored on your machine in `~/.tokeneconomizer`. [README, fetched 2026-11-02]

## Dead Ends

- **Quoting an 18–31% token saving.** The published number is cost, on SWE-Bench.
- **Assuming the micro-skills cannot capture anything sensitive.** They extract repository facts. Check the directory.
