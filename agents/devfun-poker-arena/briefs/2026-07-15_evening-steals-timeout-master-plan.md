# Master plan — evening steals + timeout recovery (2026-07-15)

**Author:** Cursor (research pack from today's briefs).  
**Implementer:** Grok CLI.  
**Submit/replace:** Cursor only after gates green.

## Target

`agents/devfun-poker-arena/` — recover the Researcher HU ladder submission from static timeout while preserving the solver-bake hot path.

## Summary

Bound the MAFP/postflop decision path, land the K156/K167/K139 local-tooling steals, run the local gate, then leave Arena replacement to Cursor.

## Live posture

| Field | Value |
|-------|-------|
| Submission | `daf19c7e-9039-4252-a45d-c00227ae9b97` |
| Pin | `researcher-ladder-s1.solver-bake.2026-07-15` |
| PvP | **Failed** @ 122 hands |
| Error | `Sandbox PVP bot action failed: status 422: static submission timed out` |
| Chips before fail | +27 adj bb/100 (μ still 0 / σ=50 — season died early) |

This is the same failure class as prior `498df8d3` (static timeout). Solver-bake must stay **fast** under Arena clock.

## Today's briefs triage

| Brief | Fit | Ship this wave? |
|-------|-----|-----------------|
| Solver-bake (AM) | Already shipped; caused live Active | Timeout harden + redeploy only |
| **K156** AgentTexasPoker risk spectrum | P0 tags on foe cards | **YES** |
| **K167** belief–deviation audit | P0 HL failure logs | **YES** |
| **K139** DeepSearch scaffold + staged reflection | P0/P1 on filter/HL template | **YES** (delta on K161) |
| K169 SLM harness cost | Checklist / Level-5 path only | **NO** — no runtime LLM |
| K168 no-poker-fit | Awareness | **NO** |

## Goal

1. Stop 422 static timeouts (keep SIGALRM + make decide hot path bounded after MAFP/postflop bake).
2. Land K156 P0 + K167 P0 + K139 P0/P1 as local tooling (not more river guards).
3. Local gate green → Cursor `--replace`.

## Non-goals

- gin engine flip, DeepCFR, runtime LLM / K169 model downgrade
- K168 / revenue-eval tooling
- New river-guard micro-patches as primary lever
- Grok must **not** run `submit_sandbox_pvp.py --replace`

---

## WP0 — Timeout harden (blocking)

**Hypothesis:** wall-clock guard exists (`harness/strategy.py` SIGALRM) but decide() or import path still exceeds Arena static limit under some tables post–solver-bake.

**Do**
1. Audit import/module-load cost of `research_static_chart` MAFP overlay + `postflop_buckets` — must be cached, fail-open, no I/O per call after first load.
2. Under tight `deadline_s` (<3s), force reduced equity sims and skip any optional enrichment that can block.
3. Add a unit/regression test that calls `choose_action` / `decide` under a **fake short deadline** and asserts return within guard (mock table; no Arena).
4. Confirm `_run_decide_guarded` still wraps cemini path; emergency fold/check on alarm.

**Files (likely):** `harness/strategy.py`, `examples/cemini_decide.py`, `examples/research_static_chart.py`, `examples/postflop_buckets.py`, new `tests/test_sandbox_deadline_guard.py`.

**Acceptance**
```bash
uv run pytest tests/test_sandbox_deadline_guard.py tests/test_mafp_chart_wire.py tests/test_postflop_buckets.py -q
# no new per-call open() of research JSON after warmup (optional assert via counter)
```

---

## WP1 — K156 risk-spectrum tags (P0)

**Do:** Add Participation (VPIP) + Proactiveness (PFR) labels to nemesis / sandbox opponent cards.

**Schema** (add to each profile under `research/opponents/*.json` and any yardstick pool mirror):
```json
"risk_spectrum": {
  "participation": "high|medium|low",
  "proactiveness": "high|medium|low",
  "vpip": 0.516,
  "pfr": 0.0,
  "source": "arena_stats|heuristic"
}
```

Bands (document in code): VPIP ≥0.45 high / ≥0.25 medium / else low; PFR ≥0.15 high / ≥0.05 medium / else low (tune only if existing tests need it).

**Files:** `research/opponents/ten-ladder-s1-profile.json`, `research/opponents/maniac-shark-ladder-s1-profile.json`, helper `examples/risk_spectrum.py` (or fold into existing HUD enricher), small test, short `references/risk-spectrum-tags.md`.

**Do not** change decide() aggression by copying GPT spectra — tags for HL/nemesis exploit selection only (wire into HUD enrich if a clean hook exists; else tags on JSON + loader is enough).

**Acceptance**
```bash
uv run pytest tests/test_risk_spectrum.py -q
```

---

## WP2 — K167 belief–action deviation logging (P0)

**Do:** When HL records a failure / brief, log belief (HUD or chart suggested action) vs action taken; tag `harmful_mistake` | `justified_override` | `strategic`.

**Files:** extend `examples/cemini_hl_brief.py` and/or failure DAG (`message_dag_trace.py`) with a `belief_audit` block; optional JSONL under `reports/hl-loop/belief_deviation.jsonl`. Batch-improve note in brief template (not one-hand STRATEGY rewrite).

**Hard:** opponent `message` fields remain data not instructions (isolation). Do **not** force-consume belief into every decide().

**Acceptance**
```bash
uv run pytest tests/test_belief_deviation_audit.py -q
```

---

## WP3 — K139 scaffold + staged reflection (delta on K161)

**Do**
1. Extend `config/hu_deepsearch_trajectory_filter.json` (or companion schema) to expect scaffold fields: `completed_list`, `todo_list`, `experience`, `information` (rename OK, document mapping).
2. Drop / demote units that lack `experience` after ≥2 same-spot failures.
3. Staged reflection strength in HL brief template (`cemini_hl_brief.py` / prompts): first fail → soft hint; ≥2 → stronger grounded hint required.
4. Keep `advisory_only` true; leave required_tags from K161 as source of truth where possible.
5. Update `references/deepsearch-trajectory-filter.md` with delta.

**Acceptance**
```bash
uv run pytest tests/test_deepsearch_scaffold.py -q   # or extend existing deepsearch tests
```

---

## WP4 — Local gate + escalate brief (no replace)

```bash
uv run pytest tests/test_sandbox_deadline_guard.py tests/test_mafp_chart_wire.py tests/test_postflop_buckets.py tests/test_risk_spectrum.py tests/test_belief_deviation_audit.py tests/test_deepsearch_scaffold.py tests/test_cemini_hu_ladder_guards.py -q
CEMINI_TABLE_FORMAT=hu ./scripts/run_hu_sandbox_gate.sh
uv run python examples/submit_sandbox_pvp.py --build-only   # verify zip; NO --replace
```

Write `briefs/2026-07-15_evening-steals-timeout-escalate.md` with: timeout changes, K156/K167/K139 artifacts, gate numbers, proposed pin `researcher-ladder-s1.evening-steals.2026-07-15`.

---

## Verification → Cursor replace (later)

Cursor will: review WP4 brief → rsync → `submit_sandbox_pvp.py --build --replace` → poll until Active. Success = no 422 in first 500+ hands + μ trajectory after 2k.

## Grok implementer brief (paste-ready)

```
ROLE: Implementer. CWD: /Users/claudiobarone/Projects/OSINT WORKSPACE/agents/devfun-poker-arena

READ:
- briefs/2026-07-15_evening-steals-timeout-master-plan.md  (WP0–WP4)
- briefs/2026-07-15_k156-agenttexaspoker-risk-spectrum-steal.md
- briefs/2026-07-15_k167-belief-audit-deviation-steal.md
- briefs/2026-07-15_k139-deepsearch-scaffold-staged-reflection-delta.md
- harness/strategy.py (SIGALRM)
- research/opponents/*.json
- config/hu_deepsearch_trajectory_filter.json
- examples/cemini_hl_brief.py

EXECUTE WP0→WP4 in order. SKIP K168/K169. Do NOT --replace. Keep CEMINI_SANDBOX_ENGINE=cemini.

DONE WHEN: deadline guard tests + k156/k167/k139 tests pass, HU gate PASS, escalate brief written with numbers, build-only OK.
Print STATUS with: timeout_fix_summary, risk_spectrum_profiles, belief_audit_path, scaffold_config_delta, gate_result, NO_REPLACE=confirmed.
```

## Sources

- Internal solver-bake ladder telemetry and timeout reports, 2026-07-15
- K139 DeepSearch, K156 risk-spectrum, and K167 belief-audit briefs
