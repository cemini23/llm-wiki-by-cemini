## Target

`agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-25_playground-s10-climb-grok-prompt.md).

# Grok task — Playground S10 climb (HL + selective widen)

ROLE: Implementer. Cursor monitors S10 lobby. You analyze + patch + escalate.
Always-approve. CWD: `/Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena`


## Summary

Operator brief: 2026-07-25 playground-s10-climb-grok-prompt. `agents/devfun-poker-arena/` — Poker Arena operator brief (2026-07-25_playground-s10-climb-grok-prompt.md).

## Regime disclosure

Comparisons in this brief are **single-regime** (HU Researcher sandbox and/or 6-max Playground chip-qual only). Not a multi-regime leaderboard claim; no free cross-regime superiority asserted.
## Status (2026-07-25 ~22:13 UTC)

- Comp: Playground S10 `cms0bwufmf3n8kyykdpxi6d2i`
- Us: **#48 @ 988 chips / 359 hands / 31 won** (~8.6% win) — ~flat vs 1000 start
- #20 floor ≈ **1662** · gap **+674**
- Prior wave (same day): S9 trash-flat folds shipped + lobby deployed — survival OK, **climb missing**
- Posture stays chip-qual: gin/MAFP/solver/eval/ladder **OFF**. No Tournament buy. No Arena `--replace`.

## Goal

Improve **chip accumulation** for top-20 qual without re-bleeding stack.

## Do

1. **HL analyze S10 from prod** — `python3 examples/analyze.py --match cms0bwufmf3n8kyykdpxi6d2i --limit 100 --top 15` (and wider preflop decision log if helpers exist). Focus SB + pot-capture misses, not more EP nit.
2. **Patch `examples/cemini_decide.py`** (minimal):
   - Confirm/fix remaining **SB bleed** only if evidence supports.
   - **Selective widen (S1b-style):** BTN/CO steals vs confirmed **loose-passive** HUD only (`rock_steal_eq` / existing HUD exploit paths). Do **not** global VPIP widen. Do **not** gin.
   - **Value vs maniac** (VPIP≫45% / grok*): slightly wider call-downs for value; still fold trash preflop to them.
3. Add pytest regressions for each new guard/steal gate.
4. Write `briefs/2026-07-25_playground-s10-climb-escalate.md` with leak table, files, gate numbers, and **DEPLOY lobby vs NO** recommendation (rsync+restart if patches land; **NO_REPLACE** Arena/Eval).

## Done when

```bash
uv run pytest tests/test_cemini_preflop_guards.py tests/test_cold_start_hud.py -q --tb=line
# + any new tests you add
```

Escalate exists with chip-climb rationale.

## Do NOT

- `CEMINI_GIN_*` / MAFP / solver V3 / researcher HU / eval crush
- Arena `--replace` / sandbox submit / Tournament S9 buy
- Touch prod `.env` (Cursor owns enter)
- Blind global steal widen without HUD gate

Canon: `briefs/2026-06-04_playground-s1-competition-intel.md`, `briefs/2026-07-25_playground-s10-hl-escalate.md`, `docs/TESTING-CEMINI.md`.

## Sources

- Internal Arena ops briefs / escalate packages in `agents/devfun-poker-arena/briefs/`
- Related references under `agents/devfun-poker-arena/references/`
