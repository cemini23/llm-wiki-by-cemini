## Target

`agents/devfun-poker-arena/` — K130 poker stack baseline (source brief: `2026-06-26_k130-poker-stack-baseline-steal.md`). **Plan-first, then parallel subagents.** Not the HU sandbox K131/K131b lane.

## Summary

K130 confirms **PokerKit** as the canonical Arena engine (already deployed) and adds **RLCard** for isolated offline HU/Leduc baseline ablations. **PokerHandEvaluator** is a profiling-gated spike only. GPL poker repos stay rejected.

This master plan is the **single gate** before any Track subagent runs. Subagents must not start until this file exists and the parent agent has assigned track ownership.

### Agent orchestration ritual (mandatory)

1. **Read** `briefs/2026-06-26_k130-poker-stack-baseline-steal.md` (scope / tier table).
2. **Write** this master plan (tracks, file ownership, acceptance criteria).
3. **Parent integrates** cross-track wiring only after both tracks report green tests (serialize `cemini_decide.py` / shared scripts if needed).
4. **Parallel subagents** — one per track, **no overlapping owner files**.
5. **Integration gate** — parent runs verify scripts + `pytest` + logs results; user-gated commit/push.

**Why K131b felt wrong:** Track A/B subagents were dispatched against `k131b-bb-lag-tune-plan.md` while the parent was still fixing stack-off ordering and v008 trim — i.e. execution overlapped planning/integration. Correct order: plan → parallel implement → parent merge → gate.

---

## Tracks (parallel-safe)

| Track | Priority | Owner agent | Scope |
|-------|----------|-------------|--------|
| **A** | P0 | GPT | PokerKit pin + selfplay/Arena adapter parity checks (no new deps) |
| **B** | P1 | Kimi | RLCard isolated venv + offline Leduc/HU baseline ablation (log only) |
| **C** | P2 | Deferred | PokerHandEvaluator spike — **only if** Track A profiling shows hand-rank eval >5% of `decide()` |

**Hard invariant:** `rlcard` never enters `pyproject.toml` core deps. GPL repos never vendored.

---

### Track A — P0 PokerKit stack confirmation

**Owner files (exclusive):** `scripts/verify_pokerkit_stack.sh` (new), `tests/test_pokerkit_stack_smoke.py` (new), `briefs/2026-06-26_k130-poker-stack-baseline-steal.md` (append verification note only).

**A1 — Pin + import smoke**
- Assert `pyproject.toml` pins `pokerkit>=0.5` and `uv run python -c "import pokerkit"` succeeds in arena venv.
- Document installed version in script output.

**A2 — Selfplay ↔ PokerKit card repr parity**
- `examples/selfplay.py` and `gin_style._normalize_card` already assume PokerKit-style `Ah` / `[Ah]` strings.
- New test: round-trip a small set of hole/board strings through selfplay table builder + `research_static_chart._hand_class` without parse failures.
- New script `scripts/verify_pokerkit_stack.sh`: runs A1 smoke + `uv run pytest tests/test_pokerkit_stack_smoke.py -q` + `bash -n` on any new shell scripts.

**A3 — Season parity checklist (read-only)**
- Script prints checklist for operator: `pokerkit run --max-hands 5` smoke after each Researcher season (no auto-submit from this track).

**A4 — Optional profiling hook for Track C**
- If cheap: one-liner in verify script timing `estimate_equity` / treys on 1000 samples; log ms — **do not** implement PokerHandEvaluator unless >5% of a synthetic `decide()` budget.

**Tests**
```bash
cd agents/devfun-poker-arena
uv run pytest tests/test_pokerkit_stack_smoke.py -q
bash scripts/verify_pokerkit_stack.sh
```

---

### Track B — P1 RLCard offline ablation

**Owner files (exclusive):** `scripts/setup_rlcard_venv.sh` (new), `scripts/run_rlcard_baseline_ablation.sh` (new), `examples/rlcard_baseline_ablation.py` (new), `tests/test_rlcard_venv_gate.py` (new — asserts scripts exist, no `rlcard` in `pyproject.toml`).

**B1 — Isolated venv**
- Pattern: mirror `../../scripts/gambling_research_venv.sh` but arena-local: `agents/devfun-poker-arena/.venv-rlcard` OR document wrapper calling OSINT `scripts/gambling_research_venv.sh` + `$ROOT/.local/venv-gambling-research/bin/python`.
- `setup_rlcard_venv.sh`: create venv, `pip install rlcard>=1.2.0,<2`, import smoke.

**B2 — Offline baseline ablation (log only)**
- `examples/rlcard_baseline_ablation.py`: run RLCard Leduc or limit-HU env for N episodes; log action frequencies / simple VPIP proxy.
- Compare **one** static chart cell (e.g. BTN open frequency proxy) vs treys MC equity on same synthetic hands — output JSONL to `reports/rlcard-ablation/` (gitignored path under arena).
- **No Arena submit claims** — research log only.

**B3 — Cross-wiki handoff stub**
- Print at end of ablation: pointer to gambling-wiki `rlcard` entity + future `2026-06-26_k130-rlcard-offline-baseline-adopt.md` (gambling-wiki owns depth).

**Tests**
```bash
cd agents/devfun-poker-arena
bash scripts/setup_rlcard_venv.sh   # once
bash scripts/run_rlcard_baseline_ablation.sh --episodes 50
uv run pytest tests/test_rlcard_venv_gate.py -q
```

---

### Track C — P2 PokerHandEvaluator (gated)

**Do not spawn a subagent until Track A profiling documents treys/hand-eval >5% of decide latency.**

If triggered: spike Apache-2.0 bindings in isolated script; compare correctness vs treys on 10k random 7-card evals; no prod wiring without user GO.

---

## Integration (parent only, after A + B green)

```bash
cd agents/devfun-poker-arena
bash scripts/verify_pokerkit_stack.sh
uv run pytest tests/test_pokerkit_stack_smoke.py tests/test_rlcard_venv_gate.py -q
# Optional slow:
# bash scripts/run_rlcard_baseline_ablation.sh --episodes 200
```

Append one line to `wiki/log.md` (OSINT) or arena CHANGELOG if posture changes.

---

## Acceptance criteria

| # | Criterion | Track |
|---|-----------|-------|
| AC1 | `pokerkit` import + pin documented | A |
| AC2 | `test_pokerkit_stack_smoke.py` green | A |
| AC3 | `verify_pokerkit_stack.sh` exits 0 | A |
| AC4 | RLCard venv isolated; **not** in `pyproject.toml` | B |
| AC5 | Ablation script runs 50+ episodes without crash | B |
| AC6 | `test_rlcard_venv_gate.py` green | B |
| AC7 | No GPL deps added | A+B |
| AC8 | Full arena `pytest tests/ -q` still green | Parent |

**GO** when AC1–AC8 pass. Track C is optional follow-up.

---

## Risks / don't-break

1. **No `rlcard` in core deps** — breaks prod venv size / license boundary.
2. **No GPL** (pokerth, dickreuter/*) — ever.
3. **Sandbox K131/K131b** is a separate brief chain; this K130 stack work does not edit `gin_style.py` / `cemini_decide.py` unless profiling (Track C) explicitly scoped later.
4. **Commits user-gated** — no push, no Arena submit from ablation scripts.

## Sources

- `briefs/2026-06-26_k130-poker-stack-baseline-steal.md`
- `scripts/gambling_research_venv.sh`, `scripts/gambling_research_requirements.txt`
- `pyproject.toml` (`pokerkit>=0.5`)
- @wiki/entities/tools/pokerkit.md, @wiki/entities/tools/rlcard.md
