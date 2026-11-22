---
title: "Repeated-correction mining — turning what you keep retyping into a rule"
type: concept
related:
  - "@osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md"
  - "@osint-wiki/concepts/agent-link-evaluation-gates-v1013.md"
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/claude-code-skills-md-institutional-memory.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/agent-harness-tooling-2026-11.md
updated: 2026-11-22
---

## Raw Concept

Five tools from the 2026-11-17 batch solve the same problem from different angles:
**the agent repeats a mistake you have already corrected.** The question this page
answers: **what is the cheapest way to stop the repeat?**

Source: @osint-wiki/sources/2026-11-17-deep-research-link-eval-design-motion-harness.md.

## Narrative

### The five, by mechanism

| Tool | Stars | Mechanism | Reads |
|------|-------|-----------|-------|
| `globalmpc/nomore` | 106 | Scans 30 days of session transcripts for repeated instructions; flags CLAUDE.md rules the model keeps breaking | transcripts |
| `Umair/stalemap` | 109 | Diffs pre-cutoff vs pinned `.d.ts` exports; injects the delta into AGENTS.md under a token budget | type definitions |
| `devanshranjan10/landmines` | 10 | Known open bugs in your exact pinned dependency versions, surfaced in context | issue trackers |
| `mdalexandre/claude-code-lean-agents` | 19 | Two subagents that start at ~7.5k tokens instead of a full harness | agent config |
| `disinfeqt/rulebook` | 22 | Native macOS app to find, untangle, and edit the CLAUDE.md rules themselves | rule files |

All MIT. All local. All frozen from installation.

### The insight worth keeping

`nomore` makes the sharpest observation: **a rule in `CLAUDE.md` that the model keeps
violating is not a rule, it is noise.** The file grows, and the model attends to it
less. Adding a tenth rule to fix a violation of the third makes the whole file weaker.

That is the opposite of how most of us maintain these files. We append. We do not
measure.

The measurable version is simple and needs no tool: for one month, every time you
correct the same thing twice, write it down with the date. At the end of the month,
count. Anything corrected three or more times becomes a rule. Anything corrected once
does not. Then delete the rules that have not fired.

`stalemap` addresses a different failure — the model's knowledge stops at a date, and
its dependency advice is confidently stale. A pinned version's type definitions are
the ground truth, and the delta between the model's assumption and the pinned reality
is exactly what breaks a build. Its 1,800-token budget is the interesting design
choice: the delta is injected, not the whole definition file.

`landmines` is the same idea pointed at issue trackers.

### What we already have

The federation already carries
@concepts/agent-token-discipline-openclaw-hermes.md and
@concepts/agent-memory-stack-comparison.md. The new contribution here is not a tool —
it is the **pruning rule**: a rules file that only grows is a rules file that stops
working.

Apply it to the workspace `CLAUDE.md`, which is long. The cut should be evidence-based,
not aesthetic.

### Cost side

`TokenEconomizer` (Microsoft Research plus UC Berkeley, arXiv 2610.22732) is the
quantitative companion: 18.4–30.9% mean cost reduction across 30 repository-model pairs
on 277 SWE-Bench tasks. Its mechanism is a micro-skill library confirmed across three
non-overlapping tasks, with decay factor 0.8 and a single-contradiction penalty weight
of 5.

The decay and penalty terms are the transferable part: confidence in a learned skill
should fall with age and collapse on one contradiction. That is a two-line rule for any
self-improving loop we build, and it needs no dependency.

### Why nothing is queued

Every tool installs a hook, a skill, or an MCP server. Gate 3 freezes all three.

## Snippets

> Finds the corrections you keep repeating to Claude Code.
> [`globalmpc/nomore`, repository description, 2026-11-17]

> 18.4%–30.9% mean token savings on 277 SWE-Bench tasks.
> [Source: Cemini Multi-Wiki Link Evaluation.docx, URL 15]

## Dead Ends

- **Appending a rule after every correction.** It grows the file and dilutes the rules
  that matter. Measure first, then promote.
- **Trusting model knowledge about a pinned dependency.** Diff the actual type
  definitions.
