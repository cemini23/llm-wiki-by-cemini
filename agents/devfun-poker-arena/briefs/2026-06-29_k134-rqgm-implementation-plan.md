## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox tri-verifier stack. Implementation plan for K134 **RQGM** (arXiv 2606.26294) controlled-utility-evolution steal: versioned rubric epochs, GT-gated evaluator promotion (advisory), selective erasure of stale leaderboard rows. Pairs with K132 tri-verifier (`examples/sandbox_tri_verifier.py`) and K131 ToolBench-X hazard taxonomy.

Implementing agent: read this whole brief, then `examples/sandbox_tri_verifier.py`, `references/sandbox_tri_verifier_schema.json`, `tests/test_sandbox_tri_verifier.py`, `tests/helpers/cemini_tables.py`, `scripts/run_sandbox_tri_verifier.sh`, `scripts/run_hu_sandbox_gate.sh` before writing code. Honor `AGENTS.md` Hard NEVERs and "no new pip deps".

## Summary

Add an **epoch layer** on top of the existing stateless tri-verifier so evaluator weights/thresholds are versioned, frozen per submit batch, and only promoted when a held-out spot suite improves. Old reports without `rubric_epoch` stay valid (backward compat). Three phases:

- **P0** — rubric versioning: new `config/rubric_epoch.json`, new stdlib module `examples/sandbox_rubric_epoch.py`, optional `rubric_epoch`/`evaluator_id`/`rubric_version` fields in the report schema, advisory promotion gate over a hold-out spot suite built from `cemini_tables` helpers.
- **P1** — selective erasure: stamp `superseded_by_epoch` onto prior rows in `reports/hl-loop/researcher_trajectory_index.jsonl` (and per-bundle `axis_summary.json`) when the epoch bumps. **Never delete raw trajectories** (`selfplay_trajectory.jsonl`).
- **P2** — adversarial epoch (optional, log-only): detect LLM-judge over-acceptance vs harness legality, write an advisory audit record.

Out of scope: full Thompson-sampling archive tree (RQGM §3.1), scientific-paper-reviewing domain, any live PokerKit-in-the-loop oracle (use golden-labeled fixtures), any auto-promotion that mutates `config/rubric_epoch.json` without `--promote` opt-in.

## Body

### Constraints / invariants (apply to all phases)

1. **Stdlib only** on the verifier path. `sandbox_rubric_epoch.py` imports only `json`, `hashlib`, `pathlib`, `datetime`, `re`, `argparse`, `typing`. No `pyyaml`, no `pokerkit`, no `httpx`.
2. **Backward compat**: a report dict with no `rubric_epoch` key is still schema-valid and still passes every existing test in `test_sandbox_tri_verifier.py`. All new schema fields are **optional** (not in any `required` array).
3. **No mutation of `sandbox_tri_verifier.py` scoring semantics.** K134 wraps/annotates; it does not change pass/fail logic of `score_action` / `score_trajectory`. The only allowed edit to `sandbox_tri_verifier.py` is exposing the three module-level thresholds (`_EFFICIENCY_HARD_DEADLINE_S`, `_EFFICIENCY_SOFT_RATIO`, `_MAX_IDLE_POLL_LOOPS`) as overridable params (see P0 step 4) — defaults unchanged.
4. **Frozen epoch**: within one submit batch the active epoch's weights/thresholds are read once and never re-read mid-batch.
5. **Promotion + erasure are user-gated** (`--promote`, `--supersede` flags). Default runs are read-only/advisory and exit 0.

---

### P0 — rubric versioning (schema + frozen epoch + advisory promotion gate)

#### P0.1 — Config file: `config/rubric_epoch.json`

Create `agents/devfun-poker-arena/config/rubric_epoch.json`:

```json
{
  "rubric_version": 1,
  "epoch": 1,
  "frozen": true,
  "weights": {
    "correctness": 1.0,
    "efficiency": 1.0,
    "critical_point": 1.0
  },
  "thresholds": {
    "efficiency_hard_deadline_s": 10.0,
    "efficiency_soft_ratio": 0.9,
    "max_idle_poll_loops": 3
  },
  "promotion": {
    "epsilon": 0.0,
    "holdout_suite": "k134_holdout_v1",
    "advisory_only": true
  },
  "history": [
    {
      "epoch": 1,
      "rubric_version": 1,
      "promoted_at": "2026-06-29T00:00:00Z",
      "reason": "genesis epoch (K132 thresholds frozen)",
      "evaluator_id": "PLACEHOLDER_FILL_AT_RUNTIME"
    }
  ]
}
```

- `weights` mirror the three tri-verifier dimensions (reserved for future weighting; v1 all 1.0).
- `thresholds` mirror the three constants currently hardcoded in `sandbox_tri_verifier.py` so the genesis epoch is behavior-identical to K132.
- `epsilon` = minimum hold-out pass-rate delta a challenger must beat the incumbent by to be promotion-eligible (`0.0` = strictly greater).
- `history` is append-only; each promotion appends one record.

#### P0.2 — New module: `examples/sandbox_rubric_epoch.py`

Stdlib only. Public API (exact names — tests bind to them):

| Function | Signature | Behavior |
|---|---|---|
| `load_rubric_config` | `(path: str \| Path \| None = None) -> dict` | Load `config/rubric_epoch.json`; default path resolved relative to repo root (`Path(__file__).resolve().parents[1] / "config" / "rubric_epoch.json"`). Raise `FileNotFoundError` if missing and no default. |
| `current_epoch` | `(config: dict) -> int` | Return `config["epoch"]`. |
| `rubric_fingerprint` | `(config: dict) -> str` | `hashlib.sha256` over `json.dumps({weights, thresholds}, sort_keys=True)`; return full hex digest. Deterministic, order-independent. |
| `evaluator_id` | `(config: dict) -> str` | Return `f"tri-v{config['rubric_version']}-e{config['epoch']}-{rubric_fingerprint(config)[:8]}"`. |
| `annotate_report` | `(report: dict, config: dict) -> dict` | Return a shallow copy of `report` with keys `rubric_epoch`, `rubric_version`, `evaluator_id` added at top level. Does not mutate input. Works on both `ActionScore` and `TrajectoryScore` shapes. |
| `thresholds_from_config` | `(config: dict) -> dict` | Return `{"deadline_hard_s": ..., "soft_ratio": ..., "max_poll_loops": ...}` for passing into the (now-parameterized) verifier helpers. |
| `score_holdout_suite` | `(config: dict, suite: list[dict] \| None = None) -> dict` | Score the golden-labeled hold-out suite (P0.3) under `config`'s thresholds using `sandbox_tri_verifier.score_action`. Return `{"suite": name, "total": int, "passed": int, "pass_rate": float, "evaluator_id": str, "epoch": int}`. |
| `promotion_gate` | `(incumbent: dict, challenger: dict, config: dict) -> dict` | Compare two `score_holdout_suite` results. Return `{"verdict": "PROMOTE"\|"HOLD", "advisory": bool, "incumbent_pass_rate": float, "challenger_pass_rate": float, "epsilon": float, "delta": float, "reason": str}`. `verdict == "PROMOTE"` iff `challenger.pass_rate - incumbent.pass_rate > epsilon`. When `promotion.advisory_only` is true, set `advisory=True` and **never** write config. |
| `promote_epoch` | `(config: dict, gate: dict, *, path=None, dry_run=True) -> dict` | If `gate["verdict"]=="PROMOTE"` and `dry_run` False and not advisory-only: bump `epoch`+1 (and `rubric_version` if challenger weights differ), append a `history` record with new `evaluator_id`, atomic-write config. Return updated config. `dry_run=True` (default) returns the would-be config without writing. |
| `mark_superseded` | `(index_path, new_epoch, *, prior_epoch=None, dry_run=True) -> int` | P1 — see P1.1. Lives in this module. |
| `adversarial_audit` | `(events: list[dict], config: dict) -> dict` | P2 — see P2.1. |

`main(argv)` CLI (argparse), subcommands / flags:

```
python examples/sandbox_rubric_epoch.py --print            # print active epoch + evaluator_id (exit 0)
python examples/sandbox_rubric_epoch.py --holdout          # score hold-out suite under active epoch, print pass_rate
python examples/sandbox_rubric_epoch.py --gate             # advisory promotion gate (incumbent=active, challenger=active) -> always HOLD on identity; exit 0
python examples/sandbox_rubric_epoch.py --supersede N      # P1: stamp superseded_by_epoch=N on index rows (dry-run unless --apply)
python examples/sandbox_rubric_epoch.py --adversarial-audit <trajectory.jsonl>  # P2 log-only
python examples/sandbox_rubric_epoch.py --apply            # opt-in: actually write (promotion / supersede)
```

Default (no `--apply`) is read-only and exits 0. `--print` is what the gate scripts call.

#### P0.3 — Hold-out spot suite (golden-labeled, stdlib)

Add helper `tests/helpers/k134_holdout.py` (importable by both module and tests). Build a frozen "GT anchor" suite from existing `cemini_tables` helpers — **no PokerKit**. Each entry is a dict the verifier can score plus a `gt_pass` golden label:

```python
# tests/helpers/k134_holdout.py
from cemini_tables import (
    hu_sb_unopened, hu_bb_vs_minraise, hu_btn_vs_shove,
    nuts_quads_facing_bet, second_nut_flush_river,
)

def holdout_suite_v1() -> list[dict]:
    """K134 GT anchor: HU + nuts spots with golden legal/illegal labels.
    Each row: {name, action, allowed_actions, elapsed_s, deadline_s, payload, table, gt_pass}.
    gt_pass = the action+reasoning a competent agent should produce (oracle label).
    """
    ...
```

Minimum **6 hold-out spots**, mixing:
- legal premium open (`hu_sb_unopened(["As","Ah"])`, raise amount in `raiseRange`, hand-specific reasoning) → `gt_pass=True`
- illegal action (action not in `availableActions`) → `gt_pass=False`
- generic-reasoning fail (reuse `FALLBACK_REASONING` from `output_sanitize`) → `gt_pass=False`
- bad-amount fail (raise below `raiseRange.min`) → `gt_pass=False`
- timeout fail (`elapsed_s` > `deadline_s`) → `gt_pass=False`
- nuts value bet legal (`nuts_quads_facing_bet`) → `gt_pass=True`

`score_holdout_suite` scores each row with `score_action(...)` under config thresholds; `pass_rate` = fraction where `score.pass == gt_pass` (i.e. evaluator agreement with GT, RQGM §3 ground-truth anchor). This is the metric the promotion gate compares between epochs.

#### P0.4 — Parameterize verifier thresholds (minimal edit to `sandbox_tri_verifier.py`)

Change `verify_efficiency` and `score_action` to accept optional overrides; keep defaults = current module constants so all K132 tests stay green:

```python
def verify_efficiency(elapsed_s, deadline_s, poll_loops=0, *,
                      hard_deadline_s=_EFFICIENCY_HARD_DEADLINE_S,
                      soft_ratio=_EFFICIENCY_SOFT_RATIO,
                      max_poll_loops=_MAX_IDLE_POLL_LOOPS) -> dict: ...

def score_action(..., *, thresholds: dict | None = None) -> dict:
    # if thresholds: pass through to verify_efficiency
```

`thresholds` keys: `deadline_hard_s`, `soft_ratio`, `max_poll_loops` (match `thresholds_from_config`). This is the ONLY change to `sandbox_tri_verifier.py`; do not touch hazard codes or pass/fail logic.

#### P0.5 — Schema additions: `references/sandbox_tri_verifier_schema.json`

Add three **optional** top-level properties to BOTH `$defs/TrajectoryScore` and `$defs/ActionScore` (do NOT add to `required`):

```json
"rubric_epoch":   { "type": "integer", "minimum": 1,
                    "description": "RQGM epoch under which this report was produced. Absent on pre-K134 reports (backward compatible)." },
"rubric_version": { "type": "integer", "minimum": 1,
                    "description": "Rubric weight/threshold schema version. Absent on pre-K134 reports." },
"evaluator_id":   { "type": "string",
                    "pattern": "^tri-v[0-9]+-e[0-9]+-[0-9a-f]{8}$",
                    "description": "Deterministic id of the frozen evaluator (tri-v{ver}-e{epoch}-{fp8})." }
```

Add a new `$defs/PromotionGate` block (referenced by tests/tooling, not by `oneOf`):

```json
"PromotionGate": {
  "type": "object",
  "required": ["verdict", "incumbent_pass_rate", "challenger_pass_rate", "epsilon", "delta", "advisory"],
  "properties": {
    "verdict": { "enum": ["PROMOTE", "HOLD"] },
    "advisory": { "type": "boolean" },
    "incumbent_pass_rate": { "type": "number", "minimum": 0, "maximum": 1 },
    "challenger_pass_rate": { "type": "number", "minimum": 0, "maximum": 1 },
    "epsilon": { "type": "number", "minimum": 0 },
    "delta": { "type": "number" },
    "reason": { "type": "string" }
  }
}
```

Bump `$id` comment or add `"x-rubric-schema-version": 2` at root (optional, non-breaking). Add a third entry to `examples[]` showing a trajectory with `rubric_epoch`/`evaluator_id` populated.

#### P0.6 — Integrate into `scripts/run_sandbox_tri_verifier.sh`

Append after the pytest line (keep existing line intact):

```bash
uv run pytest tests/test_sandbox_tri_verifier.py tests/test_sandbox_rubric_epoch.py -q
echo "==> K134 rubric epoch:"
uv run python examples/sandbox_rubric_epoch.py --print
uv run python examples/sandbox_rubric_epoch.py --holdout
```

(Replace the single pytest invocation with the combined one so both suites run.)

#### P0.7 — Integrate into `scripts/run_hu_sandbox_gate.sh`

In the existing K132 block (around the `bash scripts/run_sandbox_tri_verifier.sh` call, line ~174), append an advisory epoch stamp + promotion gate (log only, never fail the gate):

```bash
echo "==> K134 RQGM epoch stamp + advisory promotion gate"
uv run python examples/sandbox_rubric_epoch.py --print | tee "${BUNDLE_DIR}/rubric_epoch.txt"
uv run python examples/sandbox_rubric_epoch.py --gate  | tee "${BUNDLE_DIR}/promotion_gate.txt" || true
```

Write `evaluator_id` + `rubric_epoch` into the bundle so each submit batch records which frozen evaluator scored it.

---

### P1 — selective erasure (`superseded_by_epoch`, never delete trajectories)

#### P1.1 — `mark_superseded` in `examples/sandbox_rubric_epoch.py`

LB rows live in `reports/hl-loop/researcher_trajectory_index.jsonl` (one JSON row per bundle, appended by `researcher_trajectory_summary.py:main`). Each row currently has `at`, `bundle_dir`, `selfplay_decisions`, `arena_tables`, `vpip_proxy`, `bb100`, `gate_pass`.

`mark_superseded(index_path, new_epoch, *, prior_epoch=None, dry_run=True) -> int`:
1. Read every line of the index JSONL.
2. For each row whose `rubric_epoch` is absent OR `< new_epoch` (and not already superseded), set `row["superseded_by_epoch"] = new_epoch`.
3. **Never** delete or rewrite the referenced `selfplay_trajectory.jsonl` raw files — only annotate index rows.
4. If `dry_run` (default): return count of rows that *would* change, write nothing. If `--apply`: atomic-rewrite the index file (write to `index_path + ".tmp"`, `os.replace`).
5. Return number of rows superseded.

Also stamp per-bundle `axis_summary.json` when present: if `bundle_dir/axis_summary.json` exists, add `"superseded_by_epoch": new_epoch` at top level (dry-run aware). Do not touch `manifest.json` raw counts.

#### P1.2 — Wire epoch onto new rows

In `researcher_trajectory_summary.py:main`, when building `index_row` (line ~466), add the active epoch so future rows are self-describing:

```python
from sandbox_rubric_epoch import load_rubric_config, current_epoch, evaluator_id
_cfg = load_rubric_config()
index_row["rubric_epoch"] = current_epoch(_cfg)
index_row["evaluator_id"] = evaluator_id(_cfg)
```

Guard the import with try/except so the summary tool still works if the config is absent (backward compat / partial checkout): on ImportError or FileNotFoundError, skip the two keys.

#### P1.3 — CLI

`python examples/sandbox_rubric_epoch.py --supersede N` → dry-run report (counts). `--supersede N --apply` → write. Print a one-line summary: `superseded R rows < epoch N (raw trajectories preserved)`.

---

### P2 — adversarial epoch (optional, log-only)

#### P2.1 — `adversarial_audit` in `examples/sandbox_rubric_epoch.py`

Detect the RQGM §5.4 failure mode: an LLM judge over-accepts reasoning YAML that the harness would rule illegal/generic. Pure heuristic, stdlib only:

`adversarial_audit(events, config) -> dict`:
- For each event, compute `harness_pass = score_action(...).pass` (objective tri-verifier) and `judge_pass` = a permissive proxy: `True` unless reasoning is empty. (We don't call an LLM; we model "LLM over-acceptance" as "accepts anything non-empty".)
- Count `over_accept` = events where `judge_pass and not harness_pass` (judge said OK, harness says hazard).
- Return `{"total": n, "over_accept": k, "over_accept_rate": k/n, "by_hazard": {...}, "recommend_debias_epoch": bool}` where `recommend_debias_epoch = over_accept_rate > 0.2` (advisory threshold).
- **Log only**: write `reports/hl-loop/adversarial_audit-<ts>.json`. Never bump epoch, never fail any gate.

#### P2.2 — CLI

`python examples/sandbox_rubric_epoch.py --adversarial-audit <trajectory.jsonl>` reads a selfplay/export trajectory JSONL, runs the audit, prints the summary, writes the JSON. Exit 0 always.

---

### Tests — `tests/test_sandbox_rubric_epoch.py` (minimum 12 tests)

Follow the resilient style of `test_sandbox_tri_verifier.py` (sys.path insert of `examples/` + `tests/helpers/`, `importlib.import_module("sandbox_rubric_epoch")`, `_require_attr`). Minimum cases:

1. `test_load_rubric_config_genesis` — config loads; `epoch==1`, `rubric_version==1`, `frozen is True`.
2. `test_rubric_fingerprint_deterministic` — same config → same digest; key reorder → same digest; threshold change → different digest.
3. `test_evaluator_id_format` — matches regex `^tri-v\d+-e\d+-[0-9a-f]{8}$`.
4. `test_annotate_report_adds_fields_without_mutation` — input report unchanged; output has `rubric_epoch`/`rubric_version`/`evaluator_id`.
5. `test_backward_compat_report_without_epoch_still_valid` — a K132-shaped trajectory report (no epoch keys) passes `score_trajectory` + has no epoch fields; assert old reports remain acceptable (no KeyError anywhere).
6. `test_thresholds_from_config_roundtrip` — genesis thresholds equal `sandbox_tri_verifier` defaults (10.0 / 0.9 / 3).
7. `test_holdout_suite_min_size_and_labels` — `holdout_suite_v1()` has ≥6 rows; each has `gt_pass` bool.
8. `test_score_holdout_suite_genesis_agreement` — under genesis epoch, evaluator agreement with GT ≥ 5/6 (legal/illegal/bad-amount/generic/timeout/nuts all classified correctly).
9. `test_promotion_gate_identity_holds` — incumbent==challenger → verdict `HOLD`, delta 0.
10. `test_promotion_gate_promote_on_improvement` — synthetic challenger result with higher pass_rate → verdict `PROMOTE`, `advisory True` when config advisory_only.
11. `test_promote_epoch_dry_run_does_not_write` — `promote_epoch(..., dry_run=True)` returns bumped epoch but on-disk config unchanged (read mtime/content before+after).
12. `test_mark_superseded_annotates_not_deletes` — build a temp index JSONL with 2 pre-epoch rows + a referenced (empty) `selfplay_trajectory.jsonl`; `mark_superseded(..., new_epoch=2, dry_run=False)` sets `superseded_by_epoch=2` on both rows AND the raw trajectory file still exists with identical bytes.
13. (P2) `test_adversarial_audit_log_only` — over-accept events produce `over_accept_rate>0`, `recommend_debias_epoch` set per threshold, returns dict, writes no epoch change.

Use `tmp_path` for any file-writing tests; never write into the real `config/` or `reports/` from tests.

### Commands

```bash
cd agents/devfun-poker-arena

# Unit suite (K132 + K134)
uv run pytest tests/test_sandbox_tri_verifier.py tests/test_sandbox_rubric_epoch.py -q

# K134 epoch path
bash scripts/run_sandbox_tri_verifier.sh
uv run python examples/sandbox_rubric_epoch.py --print
uv run python examples/sandbox_rubric_epoch.py --holdout
uv run python examples/sandbox_rubric_epoch.py --gate

# Selective erasure (dry-run then apply)
uv run python examples/sandbox_rubric_epoch.py --supersede 2
uv run python examples/sandbox_rubric_epoch.py --supersede 2 --apply

# Adversarial audit (log only)
uv run python examples/sandbox_rubric_epoch.py --adversarial-audit reports/researcher-round/<bundle>/selfplay_trajectory.jsonl

# Full pre-submit gate (K134 advisory stamp included)
bash scripts/run_hu_sandbox_gate.sh
python -m py_compile examples/sandbox_rubric_epoch.py
```

### Acceptance criteria

- [ ] `config/rubric_epoch.json` exists; genesis thresholds equal `sandbox_tri_verifier` defaults (epoch behavior-identical to K132).
- [ ] `examples/sandbox_rubric_epoch.py` imports stdlib only (`python -m py_compile` clean; no new entry in `pyproject.toml`).
- [ ] All existing `test_sandbox_tri_verifier.py` tests still pass unchanged (backward compat).
- [ ] `test_sandbox_rubric_epoch.py` green with ≥12 tests.
- [ ] Schema additions are **optional**: a report with no `rubric_epoch` validates; a report with epoch fields validates against the new pattern.
- [ ] Promotion gate is **advisory** by default (`advisory_only: true`); no run mutates `config/rubric_epoch.json` without `--apply` + non-advisory config.
- [ ] `mark_superseded --apply` annotates index rows with `superseded_by_epoch` and leaves every `selfplay_trajectory.jsonl` byte-identical (no deletions).
- [ ] `run_sandbox_tri_verifier.sh` runs both test files + prints epoch/holdout; `run_hu_sandbox_gate.sh` writes `rubric_epoch.txt` + `promotion_gate.txt` into the bundle and never fails on the K134 step.
- [ ] P2 adversarial audit writes `reports/hl-loop/adversarial_audit-*.json` and never changes epoch or gate exit code.
- [ ] No edits outside `examples/`, `config/`, `references/`, `scripts/`, `tests/` (AGENTS.md file-scope rule).

## Sources

- `briefs/2026-06-29_k134-rqgm-co-evolving-evaluator-steal.md` — scope
- `briefs/2026-06-27_k132-fara-implementation-plan.md` — format template + shipped tri-verifier
- @wiki/concepts/red-queen-controlled-utility-evolution.md — RQGM core loop (epoch / challenger / promotion / selective erasure)
- @wiki/sources/arxiv-red-queen-godel-machine-2606.26294-2026-06-29.md
- `examples/sandbox_tri_verifier.py`, `references/sandbox_tri_verifier_schema.json`, `tests/test_sandbox_tri_verifier.py`, `tests/helpers/cemini_tables.py`
- `scripts/run_sandbox_tri_verifier.sh`, `scripts/run_hu_sandbox_gate.sh`, `examples/researcher_trajectory_summary.py`
