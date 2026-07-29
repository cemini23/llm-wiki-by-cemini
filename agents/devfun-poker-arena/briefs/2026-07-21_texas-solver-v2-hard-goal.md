---
title: /goal — texas_solver_v2 dense blueprint + hard policy
type: brief
target: Poker Arena
created: 2026-07-21
updated: 2026-07-21
---

## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-v2-hard-goal.md).

# /goal Ship texas_solver_v2 dense offline blueprint + hard σ sampling; replace Active; μ better than −37.6 @ ≥3k

── CONTEXT ──
- Project: agents/devfun-poker-arena — cemini_wiki_poker HU S1 ladder
- Stack: cemini decide, TexasSolver offline bake, MAFP preflop, O(1) JSON lookup
- Current: Active `e3574bb4` texas_solver_v1 soft-bias, μ≈−37.6 @8.2k, rank ~204/264
- Working dir: agents/devfun-poker-arena
- Constraints: cemini engine only; no runtime solver/LLM/torch in zip; Grok out until Jul 24; Cursor/Fable hard; DeepSeek easy; Codex verify; super-audit after
- Audience: operator (competitive ladder)

── SUCCESS CRITERIA (ALL MUST BE TRUE) ──
1. `texas_solver_v2` bake artifact with denser keys (SPR × facing × board cluster × equity) — ≥200 spots attempted OR documented max feasible on M4 with ≥4× key-count vs v1’s 90
2. Hot path `CEMINI_SOLVER_HARD=1`: coverage≥τ samples mixed strategy from bake; flag-off ≡ current soft-bias path
3. Critical pytest + HU sandbox gate PASS
4. Cursor `--replace` new Active continuous
5. Codex/GPT-Sol verify report attached (pass or fixed)
6. Super-audit (Opus, Kimi, GLM Cursor + Fusion OR) run; blocking issues fixed
7. Proof: poll shows new Active; μ bar after ≥3k = better than −37.6 (stretch ≤−28); rollback if ≤−43
8. Honest: top-15 not claimed this week — target exit bottom third / top half stretch

── OPERATING RULES — NON-NEGOTIABLE ──
1. PLAN FIRST (this brief + Fable WPs)
2. WORK AUTONOMOUSLY
3. SELF-VERIFY after each WP
4. DEBUG YOURSELF
5. USE TOOLS (research already: Fable + Brave; TexasSolver local)
6. NO PLACEHOLDERS
7. PROGRESS LOG in escalate + hot.md
8. STAY ON GOAL — no docs-steal μ theater
9. IF BLOCKED — parallelize
10. CHECK SUCCESS BEFORE STOPPING

── QUALITY BAR ──
Hard policy owns actions when covered; provenance stamped; fail-open uncovered; no gin/DeepCFR-lite/opponent-modes re-stack

── FINAL DELIVERABLE ──
Pin `researcher-ladder-s1.texas-solver-v2-hard.2026-07-21` · escalate with gate numbers · Active id · SC checklist


## Summary

Operator brief: /goal — texas_solver_v2 dense blueprint + hard policy. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-21_texas-solver-v2-hard-goal.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Fable research summary
Tops: blueprint CFR + action abstraction + **play σ**. We soft-bias 90 keys. Architecture: denser TexasSolver bake + hard sample. P(top-15)≪5%; P(exit bottom third)~50%.

## WP assignment
| WP | Lane |
|----|------|
| 1–4, 6 | HARD — Cursor (Fable-directed) |
| 5 docs/light tests | EASY — DeepSeek if available else Cursor |
| Verify | Codex GPT-Sol |
| Council | Super-audit Opus/Kimi/GLM + Fusion |

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
