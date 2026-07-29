## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-25_playground-s10-hl-grok-prompt.md).

# Grok task — Playground S9 postmortem → S10 leak patches (chip qual)

ROLE: Implementer. Cursor already rolled lobby to Playground S10.
You analyze S9 hands and ship Playground-safe decide() leak patches + tests + escalate.


## Summary

Operator brief: 2026-07-25 playground-s10-hl-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-25_playground-s10-hl-grok-prompt.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Context

- Playground S9 closed ~2026-07-25 13:05 UTC. Final: **#51 @ 3721 chips / 607 hands / 53 won** (win≈8.7%). #20 floor ≈9505 — **missed Tournament S9 free entry**.
- Playground S10 live: `cms0bwufmf3n8kyykdpxi6d2i` (fresh 1000-chip runway). Prod lobby already on S10 chip-qual posture (gin/ladder/eval OFF).
- Objective: **totalChips / top-20**, not TrueSkill or Eval bb/100.
- Canon briefs: `briefs/2026-06-03_playground-top20-qualification.md`, `briefs/2026-06-04_playground-s1-competition-intel.md`, `docs/TESTING-CEMINI.md`.

## Do

1. Pull/analyze recent S9 (or prod) hand history via existing HL helpers (`examples/cemini_hl_loop.sh --from-prod` patterns, analyze scripts already in tree). Focus worst 15–30 hands + position bleed (SB/EP).
2. Patch `examples/cemini_decide.py` (and minimal helpers) for **6-max Playground** leaks only — survival + modest TAG width (~10–16% VPIP early). No gin widen, no HU ladder, no eval crush.
3. Add/adjust pytest for each guard.
4. Write `briefs/2026-07-25_playground-s10-hl-escalate.md` with: leak table, files touched, gate commands + numbers, **NO_REPLACE** vs deploy recommendation for lobby (lobby uses decide live — escalate must say whether Cursor should rsync+restart).

## Done when

```bash
cd agents/devfun-poker-arena
uv run pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# plus any new tests you add
```

Escalate brief exists with concrete chip-survival rationale.

## Do NOT

- Arena `--replace` / sandbox submit / Eval profile
- Turn on `CEMINI_GIN_*`, MAFP, solver V3, researcher HU
- Buy Tournament S9 (we did not qualify top-20)
- Touch prod `.env` (Cursor owns enter scripts)

CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
