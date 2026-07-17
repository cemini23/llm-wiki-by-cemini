# Master plan — K170 theory shelf + timeout harden v2 (2026-07-16)

**Author:** Cursor (today's briefs + live Failed).  
**Implementer:** Grok CLI.  
**Submit/replace:** Cursor only after gates.

## Target

`agents/devfun-poker-arena/` — harden the Researcher HU ladder agent after the second static-timeout failure.

## Summary

Widen the tight-deadline band, reduce simulation caps, move the wall-clock guard earlier, and add K170 fictitious-play provenance without putting FBSDE numerics in the hot path.

## Live posture

| Field | Value |
|-------|-------|
| Pin | `researcher-ladder-s1.evening-steals.2026-07-15` |
| Submission | `18b2ee80-508f-43c9-93cb-a0771b9dbbde` |
| PvP | **Failed** @ **991** hands |
| Error | `422: static submission timed out` (again) |
| Adj bb/100 before fail | ~+16.4 |
| μ | ~−59.8 |

Evening WP0 (`deadline_s < 3` → 80 sims) was not enough — season survived past 122 but still died at ~1k on the same Arena class.

## Today's briefs triage

| Brief | Fit | Ship? |
|-------|-----|-------|
| **K170** fictitious-play FBSDE theory | Cite backing for MAFP bake; no online FBSDE | **YES — docs/provenance only** |
| (no other 2026-07-16 poker briefs) | — | — |

## Goal

1. **Timeout harden v2** — wider tight band, lower sim caps, earlier wall-clock guard; prove with tests.
2. **K170** — stamp MAFP provenance + short reference page citing arXiv 2607.08861; never add FBSDE to hot path.
3. Local critical tests green → Cursor `--replace`.

## Non-goals

- Online FBSDE / PDE solvers in `decide()`
- gin flip, DeepCFR, runtime LLM
- New river-guard micro-patches
- Grok must **not** `--replace`

---

## WP0 — Timeout harden v2 (blocking)

**Hypothesis:** Arena often presents remaining time ≥3s so we still run 350–500 MC sims and occasionally exceed static timeout; SIGALRM may fire too late (`guard = deadline - 0.35`, capped 7.5s).

**Do (concrete)**

1. **Widen tight band:** treat `deadline_s < 5.0` as tight (was `< 3.0`) — skip PokerSkill/HL/chat/jackpot; use tight sim budget.
2. **Lower sim ladder:** e.g. `>5s → 250`, `≥3s → 150`, `<3s → max(20, CEMINI_TIGHT_DEADLINE_SIMS default **40**)`. Keep env overrides.
3. **Earlier SIGALRM:** in `harness/strategy.py`, tighten `_guard_s` (e.g. `min(deadline_s - 0.5, 4.5)` or `0.6 * deadline_s` capped) so emergency check/fold trips sooner.
4. **Default deadline floor:** if Arena deadline missing/unparsed, prefer lower `CEMINI_DECIDE_DEADLINE_S` default (**5.0** not 8.0) so we don't assume a long budget.
5. **Warm caches at import:** once in harness cemini path, call MAFP/postflop loaders so first Action isn't cold I/O.
6. **Tests:** extend `tests/test_sandbox_deadline_guard.py` — assert tight path at `deadline_s=4.5`; assert sims env; assert choose_action returns under short guard.

**Files:** `examples/cemini_decide.py`, `harness/strategy.py`, `tests/test_sandbox_deadline_guard.py` (± research_static_chart / postflop warm helpers).

**Acceptance**
```bash
uv run pytest tests/test_sandbox_deadline_guard.py tests/test_strategy_wall_clock_guard.py tests/test_mafp_chart_wire.py tests/test_postflop_buckets.py -q --tb=line
```

---

## WP1 — K170 MAFP theory shelf (docs/provenance)

**Do**

1. Add `references/mafp-fbsde-theory-shelf.md` — 1 page: arXiv 2607.08861 supports FP convergence under coupling; **explicit** "no FBSDE on Arena clock / decide()".
2. Update `research/mafp_hu_chart.json` `solver_provenance.notes` (and/or meta) to cite `2607.08861` as theory shelf (keep `solver_family=mafp`).
3. One-line cross-link from `briefs/2026-07-16_k170-fictitious-play-fbsde-theory.md` Body → the new reference (checklist done).
4. Tiny test optional: provenance JSON still loads; notes contain `2607.08861`.

**Do not** import any FBSDE numerics or change decide() for K170.

**Acceptance**
```bash
test -f references/mafp-fbsde-theory-shelf.md
python3 -c "import json; n=json.load(open('research/mafp_hu_chart.json')).get('solver_provenance',{}).get('notes',''); assert '2607.08861' in n, n"
```

---

## WP2 — Gate slice + escalate brief (no replace)

```bash
uv run pytest tests/test_sandbox_deadline_guard.py tests/test_strategy_wall_clock_guard.py tests/test_mafp_chart_wire.py tests/test_postflop_buckets.py tests/test_cemini_hu_ladder_guards.py -q --tb=line
# Prefer focused gate if full script is slow; at least:
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only
```

Write `briefs/2026-07-16_k170-timeout-v2-escalate.md` with: timeout v2 deltas, K170 cite path, gate numbers, proposed pin `researcher-ladder-s1.timeout-v2-k170.2026-07-16`.

---

## Cursor later

Review escalate → rsync → `--build --replace` → poll: no 422 in first **1000+** hands.

## Grok paste-ready

```
ROLE: Implementer. CWD: agents/devfun-poker-arena
READ: briefs/2026-07-16_k170-timeout-v2-master-plan.md + briefs/2026-07-16_k170-fictitious-play-fbsde-theory.md
EXECUTE WP0→WP2. No --replace. No FBSDE in hot path. No gin/LLM.
Avoid pytest|tail (hangs). Print STATUS: timeout_v2_summary, k170_cite, gate_result, NO_REPLACE=confirmed.
```

## Sources

- Internal Researcher HU ladder timeout telemetry, 2026-07-16
- arXiv 2607.08861 fictitious-play FBSDE theory shelf
