---
title: "THE FULL PROMPT" — autonomous-agent meta-prompt template (May 2026)
type: source
tags: [source, prompt, claude-code, autonomous-agent, meta-prompt, template, workflow]
keywords: [the full prompt, /goal, success criteria, operating rules, plan first, work autonomously, self-verify, debug yourself, no placeholders, progress log]
related:
  - concepts/ralph-autonomous-agent-pattern.md
  - concepts/tool-evaluation-framework.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- `@concepts/ralph-autonomous-agent-pattern.md` — sibling pattern (loop-based vs this single-shot meta-prompt)
- `@concepts/tool-evaluation-framework.md` — workflow concept frame
- `@ccc-wiki/entities/patterns/full-prompt-goal-template.md` — CCC-side adoption page (Cemini's modal session-seeding template)

## Raw Concept

- **Title**: "THE FULL PROMPT" (with `/goal [final outcome]` placeholder)
- **Source filename**: `THE FULL PROMPT _goal.docx`
- **Sha256**: `b9f610e397758bd2...`
- **Size**: 8,031 bytes
- **Retrieved**: 2026-05-12
- **Read status**: deep-read
- **Location** (canonical): `cemini-librarian:/opt/cemini-bulk/research/THE FULL PROMPT _goal.docx`

## Narrative

A single-shot meta-prompt template for autonomous Claude Code / Codex agent tasks. Different abstraction from the Ralph loop-based pattern (`@concepts/ralph-autonomous-agent-pattern.md`): Ralph is "how to structure a loop," THE FULL PROMPT is "how to specify ONE task to a non-looping agent for end-to-end execution."

### Template structure

5 numbered sections + operating rules:

1. **`/goal`** — one-line statement of what "done" looks like
2. **`── CONTEXT ──`** — Project / Stack / Current state / Working dir / Constraints / Audience
3. **`── SUCCESS CRITERIA (ALL MUST BE TRUE) ──`** — numbered list, each specific and measurable; ends with "runs without errors" + "you can show proof (screenshot · test output · URL)"
4. **`── OPERATING RULES — NON-NEGOTIABLE ──`** — 10 rules:
   1. PLAN FIRST. Output a numbered task list before writing any code.
   2. WORK AUTONOMOUSLY. Don't ask clarifying Qs unless genuinely blocked.
   3. SELF-VERIFY. After every step: run tests, inspect output, confirm.
   4. DEBUG YOURSELF. If it fails, diagnose + fix. Don't hand it back.
   5. USE EVERY TOOL. MCPs · terminal · web · code exec · pull real data.
   6. NO PLACEHOLDERS. No TODOs · no stubs · real components + real states.
   7. PROGRESS LOG. Track completed · in-flight · decisions · blockers.
   8. STAY ON GOAL. Discoveries off-spec? Note + keep moving.
   9. IF BLOCKED. Log the wall · continue everything parallelizable.
   10. CHECK SUCCESS BEFORE STOPPING. Re-read criteria · confirm each is met.
5. **`── QUALITY BAR ──`** + **`── FINAL DELIVERABLE ──`** — code clean/typed, design "looks like a well-funded startup shipped it," docs every new pattern; deliverable = confirmation per criterion + every file modified + run/test/deploy instructions + proof + decisions + known limitations.

### Where this fits in the workspace

Useful as a reference template when invoking Claude Code for a non-trivial single-shot task (not loop-based). Concrete adoption candidates:

1. **Brief-staging skill** — the 5-section structure (goal / context / success / rules / quality bar) maps cleanly to `briefs/<date>_<slug>.md` template.
2. **Phase-0 audit skill** — invocation prompt for Phase-0 audits could lift the "WORK AUTONOMOUSLY" + "SELF-VERIFY" + "STAY ON GOAL" rules.
3. **Skill-audit script invocations** — when calling `scripts/skill_audit.py` against a brief, the "CHECK SUCCESS BEFORE STOPPING" rule is the right framing.

What NOT to lift wholesale: the "10/10 operating rules" framing is heavy for routine tasks. Default to a lighter prompt envelope for short tasks; reserve the full template for genuinely multi-step autonomous runs.

### Comparison: Ralph vs THE FULL PROMPT

| Dimension | Ralph (loop-based) | THE FULL PROMPT (single-shot) |
|---|---|---|
| Iteration model | Fresh context per loop iteration | One context window, end-to-end |
| State management | `prd.json` + `progress.txt` files | Inline `PROGRESS LOG` rule + final deliverable summary |
| Failure handling | Loop continues until prd.json all complete | Self-verify + debug-yourself, don't hand back |
| Best for | Long-running multi-task projects | Single complex task with clear success criteria |
| Cost profile | Many fresh-context loops = many startup tokens | One long context, may degrade past 100K tokens |

Both are reference templates; pick by task shape.

## Snippets

### Operating rules (verbatim)

> 1. PLAN FIRST. Output a numbered task list before writing any code.
> 2. WORK AUTONOMOUSLY. Don't ask clarifying Qs unless genuinely blocked.
> 3. SELF-VERIFY. After every step: run tests, inspect output, confirm it worked.
> 4. DEBUG YOURSELF. If it fails, diagnose + fix. Don't hand it back.
> 5. USE EVERY TOOL. MCPs · terminal · web · code exec · pull real data.
> 6. NO PLACEHOLDERS. No TODOs · no stubs · real components + real states.
> 7. PROGRESS LOG. Track completed · in-flight · decisions · blockers.
> 8. STAY ON GOAL. Discoveries off-spec? Note + keep moving.
> 9. IF BLOCKED. Log the wall · continue everything parallelizable.
> 10. CHECK SUCCESS BEFORE STOPPING. Re-read criteria · confirm each is met.

### Final deliverable structure (verbatim)

> ✅ Confirmation each criterion is satisfied
> 📂 Every file created / modified
> 🚀 How to run / test / deploy
> 📊 Proof (screenshot · test output · URL)
> 📝 Decisions made + anything to know
> ⚠️ Known limitations + follow-ups

## Dead Ends

- "Don't ask clarifying Qs unless genuinely blocked" — useful default for solo-dev with clear specs; risky for ambiguous tasks where the autonomous agent will guess wrong rather than ask.
- "USE EVERY TOOL" — over-broad; in Cemini contexts this could include unsafe tools (production database writes); needs constraint per task.

## NEEDS VERIFICATION

- `[NEEDS VERIFICATION 2026-05-12]` Original author — appears to be a generic template circulated on X; could verify upstream source.
