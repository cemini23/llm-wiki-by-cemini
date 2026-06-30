## Target

`agents/devfun-poker-arena/` — Researcher Round sandbox (equilibrium baseline literacy). Implementation plan for K136 **Nash-solver provenance + FP→PED spike** (arXiv 2606.28308 solver-selection + 2606.29169 projected exploitability descent). Pairs with K124 MAFP (`examples/mafp_chart_refinement.py`), K126 Kuhn SFT reference, K122 axes (M₇ entropy).

Implementing agent (Kimi / GPT): read this whole plan, then `examples/deploy_registry.py`, `examples/mafp_chart_refinement.py`, `examples/research_static_chart.py`, `research/mafp_hu_chart.json`, `tests/test_mafp_chart_refinement.py`, `tests/test_deploy_registry.py`, `tests/test_sandbox_rubric_epoch.py` (resilient import style), `scripts/run_mafp_chart_refinement.sh`, `scripts/run_kuhn_sft_reference_analysis.sh`. Honor `AGENTS.md` Hard NEVERs, "no new pip deps", and the file-scope rule (edits only under `examples/`, `research/`, `scripts/`, `tests/`, `config/`).

## Summary

Two phases, both **offline / reference-only** — neither touches the NLHE `decide()` hot path:

- **P0 — solver provenance** (required): new stdlib module `examples/solver_provenance.py` defines a canonical `solver_family` vocabulary, stamps a `solver_provenance` block onto chart/baseline JSON (`research/mafp_hu_chart.json`, `research/preflop.json`) and onto `deploys.jsonl` rows, and **refuses to diff two profiles** unless they share a solver family OR the caller passes an explicit `--disclose` flag documenting the Nash-polytope asymmetry (2606.28308 core claim). All new fields are **optional**; pre-K136 charts without provenance still load.
- **P1 — FP→PED spike on 3-player Kuhn** (optional, literacy): new stdlib module `examples/kuhn3p_solver.py` builds a pure-Python tabular 3p Kuhn game (deck size ≤6, no `pokerkit`, no `treys`), runs CFR-only vs **FP burn-in → exploitability-descent refinement (FP-PED)** at an equal iteration budget, logs the generalized-exploitability (NashConv) curve to `research/kuhn3p_ped_spike.json` (provenance-stamped), and records one `deploys.jsonl` row. **Stop at the spike** — results inform whether late-stage refinement helps multiway toy games before any chart-space steal.

Out of scope (from brief): installing the PED reference repo (no public code), multiplayer NLHE equilibrium on the Arena clock, any change to `decide()` / `agent.py` runtime behavior.

## Body

### Constraints / invariants (apply to all phases)

1. **Stdlib only** on both new modules. `solver_provenance.py` and `kuhn3p_solver.py` import only `json`, `hashlib`, `pathlib`, `datetime`, `argparse`, `random`, `itertools`, `math`, `copy`, `sys`, `typing`. **No** `pokerkit`, `treys`, `httpx`, `numpy`, `pyyaml`. No new entry in `pyproject.toml`.
2. **No NLHE hot-path change.** Do **not** edit `agent.py:decide()` logic. The only edits to existing files are: (a) additive provenance stamping inside `mafp_chart_refinement.write_mafp_chart` and `research_static_chart._export_preflop_json`; (b) one optional `solver_family` kwarg on `deploy_registry.append_deploy_record`. All three are backward-compatible (defaults preserve current output shape except for one new optional key).
3. **Backward compat.** A chart JSON with no `solver_provenance` key still loads via every existing loader (`load_mafp_chart_ranges`, `load_preflop_chart`). A `deploys.jsonl` row with no `solver_family` is still valid. Existing tests (`test_mafp_chart_refinement.py`, `test_deploy_registry.py`) must stay green unchanged.
4. **Provenance guard is fail-closed for diffs only.** `assert_diffable` / `diff_charts` raise `SolverProvenanceError` when families differ (or singleton status is unknown/false) and `disclose=False`. Stamping and reading never raise on missing provenance — they return `None`/`unknown`.
5. **Deterministic.** `kuhn3p_solver` takes a `seed`; the full-tree solvers are deterministic given the tree. Fingerprints (`hashlib.sha256`, `sort_keys=True`) are order-independent.
6. **Atomic writes** for any JSON the modules emit: write to `path + ".tmp"` then `os.replace` (mirror `write_mafp_chart`).

---

### P0 — solver provenance in baselines

#### P0.1 — New module: `examples/solver_provenance.py`

Stdlib only. Canonical vocabulary + public API (exact names — tests bind to them).

Module constants:

```python
SOLVER_FAMILIES = frozenset({
    "cfr",            # vanilla counterfactual regret minimization (time average)
    "cfr_plus",       # CFR+ (time average, regret-matching+)
    "fictitious_play",# FP (time average)
    "rnad",           # R-NaD / regularized last-iterate (max-entropy member)
    "ped",            # projected exploitability descent (last iterate)
    "fp_ped",         # FP burn-in -> PED refinement hybrid
    "exploitability_descent",  # ED (tabular, last iterate)
    "mafp",           # K124 multi-agent fictitious play (stance FP in chart space)
    "static_chart",   # hand-authored / heuristic chart (no solver)
    "unknown",        # provenance not recorded
})

EQUILIBRIUM_SELECTION = frozenset({
    "time_average", "last_iterate", "max_entropy", "heuristic", "unknown",
})

PROVENANCE_SCHEMA = "solver-provenance-v1"
```

| Function | Signature | Behavior |
|---|---|---|
| `normalize_family` | `(name: str \| None) -> str` | Lowercase/strip; map common aliases (`"cfr+" -> "cfr_plus"`, `"r-nad"/"rnad" -> "rnad"`, `"fp" -> "fictitious_play"`, `""/None -> "unknown"`). Return `"unknown"` for any token not in `SOLVER_FAMILIES`. |
| `solver_provenance` | `(family, *, version="1", equilibrium_selection="unknown", nash_set_singleton=None, notes="") -> dict` | Build a provenance block (see schema below). `family` normalized; raise `ValueError` if `equilibrium_selection` not in `EQUILIBRIUM_SELECTION`. `nash_set_singleton` is `True`/`False`/`None` (None = not analyzed). Adds `schema=PROVENANCE_SCHEMA` and `stamped_at` UTC ISO. |
| `stamp_chart_provenance` | `(payload: dict, provenance: dict) -> dict` | Return a shallow copy of `payload` with top-level key `solver_provenance` set. Does not mutate input. Works on any chart payload dict (mafp/preflop/spike). |
| `read_chart_provenance` | `(payload: dict) -> dict \| None` | Return `payload.get("solver_provenance")` or `None`. Never raises. |
| `read_chart_file_provenance` | `(path: str \| Path) -> dict \| None` | Load JSON file, return its provenance block (or `None` if file/key missing or unparseable). |
| `family_of` | `(payload_or_prov: dict \| None) -> str` | Extract normalized family from a payload (with `solver_provenance`) or a provenance dict directly; `"unknown"` if absent. |
| `same_family` | `(a, b) -> bool` | `family_of(a) == family_of(b)` and both `!= "unknown"`. |
| `provenance_fingerprint` | `(provenance: dict) -> str` | `sha256` over `json.dumps({family, version, equilibrium_selection, nash_set_singleton}, sort_keys=True)`; full hex. |
| `assert_diffable` | `(prov_a, prov_b, *, disclose=False) -> dict` | Guard. Raise `SolverProvenanceError` unless `same_family(prov_a, prov_b)` **or** `disclose=True`. Additionally, if either side has `nash_set_singleton is False` (known non-singleton) and `disclose=False`, raise even when families match (cross-member ambiguity, 2606.28308). Return a disclosure record `{"diffable": True, "same_family": bool, "disclosed": bool, "family_a": str, "family_b": str, "nash_set_singleton_a": ..., "nash_set_singleton_b": ..., "reason": str}`. |
| `diff_charts` | `(payload_a, payload_b, *, disclose=False) -> dict` | Call `assert_diffable(read_chart_provenance(a), read_chart_provenance(b), disclose=disclose)` first, then diff the `ranges` dicts (per-position `{hand: action}`): return `{"disclosure": <record>, "added": [...], "removed": [...], "changed": [{position, hand, from, to}], "n_changed": int}`. Hands present in A not B → removed; B not A → added; action mismatch → changed. |

Define `class SolverProvenanceError(Exception): ...` at module top.

`solver_provenance` block schema (stamped onto chart JSON):

```json
"solver_provenance": {
  "schema": "solver-provenance-v1",
  "solver_family": "cfr_plus",
  "solver_version": "1",
  "equilibrium_selection": "time_average",
  "nash_set_singleton": null,
  "stamped_at": "2026-06-30T00:00:00Z",
  "notes": "K124 MAFP stance fictitious play in chart space"
}
```

`main(argv)` CLI (argparse):

```
python examples/solver_provenance.py --print <chart.json>
        # print the provenance block (or "unknown" if absent); exit 0

python examples/solver_provenance.py --stamp <chart.json> --family cfr_plus \
        [--version 1] [--selection time_average] [--singleton true|false|unknown] \
        [--notes "..."] [--apply]
        # show the would-be stamped provenance; --apply rewrites file atomically

python examples/solver_provenance.py --diff <a.json> <b.json> [--disclose]
        # guarded diff; exit 3 (SolverProvenanceError) if cross-family and not --disclose
```

Default (no `--apply`) is read-only and exits 0. `--diff` without `--disclose` on cross-family inputs prints the guard error and exits 3.

#### P0.2 — Stamp existing chart writers (additive, backward-compatible)

**`examples/mafp_chart_refinement.py`** — in `write_mafp_chart`, after building `payload` (line ~305-311), stamp provenance before the atomic write:

```python
from solver_provenance import solver_provenance, stamp_chart_provenance  # add to imports
...
prov = solver_provenance(
    "mafp",
    version="1",
    equilibrium_selection="time_average",   # FP time-average member
    nash_set_singleton=None,                 # not analyzed for HU NLHE chart space
    notes="K124 MAFP stance fictitious play; not a tabular NE solver",
)
payload = stamp_chart_provenance(payload, prov)
```

`mafp-hu-chart-v1` schema is unchanged except the new optional top-level `solver_provenance` key. `load_mafp_chart_ranges` already reads only `ranges`, so it is unaffected.

**`examples/research_static_chart.py`** — in `_export_preflop_json`, after building `payload` (line ~225-231), stamp:

```python
from solver_provenance import solver_provenance, stamp_chart_provenance  # local import inside fn (file currently does lazy imports)
...
payload = stamp_chart_provenance(payload, solver_provenance(
    "static_chart",
    equilibrium_selection="heuristic",
    notes="hand-authored 6-max opening caricature; not solver output",
))
```

`load_preflop_chart` reads only `ranges` — unaffected.

#### P0.3 — Tag `deploys.jsonl` rows with `solver_family` (one optional kwarg)

**`examples/deploy_registry.py`** — add an optional kwarg to `append_deploy_record`:

```python
def append_deploy_record(*, source, commit="", ..., notes="", solver_family=""):
    ...
    if solver_family:
        from solver_provenance import normalize_family  # local import; keeps stdlib-only top
        row["solver_family"] = normalize_family(solver_family)
```

Place the assignment after the `notes` block (line ~192-196), before `_append_jsonl`. Default `""` → key omitted → existing rows/tests unchanged. `DEPLOY_SCHEMA` string stays `devfun.deploy_record.v1` (additive optional field).

#### P0.4 — Tests: `tests/test_solver_provenance.py` (minimum **9 tests**)

Resilient style (sys.path insert of `examples/`; `importlib.import_module("solver_provenance")`; `_require_attr` helper like `test_sandbox_rubric_epoch.py`). Use `tmp_path` for file writes — never write into the real `research/`.

1. `test_normalize_family_aliases` — `"cfr+"→"cfr_plus"`, `"FP"→"fictitious_play"`, `"r-nad"→"rnad"`, `""/None→"unknown"`, junk→`"unknown"`.
2. `test_solver_provenance_block_shape` — returns dict with `schema=="solver-provenance-v1"`, normalized `solver_family`, ISO `stamped_at`; bad `equilibrium_selection` raises `ValueError`.
3. `test_stamp_does_not_mutate_input` — input payload unchanged; output has `solver_provenance`.
4. `test_read_chart_provenance_absent_returns_none` — payload without the key → `None`; never raises.
5. `test_same_family_true_false_unknown` — same family True; different families False; `unknown` vs `unknown` → False.
6. `test_assert_diffable_same_family_ok` — same family, singleton `None` → returns record `diffable True`, no raise.
7. `test_assert_diffable_cross_family_raises` — `cfr_plus` vs `rnad`, `disclose=False` → `SolverProvenanceError`; `disclose=True` → returns record with `disclosed True`.
8. `test_assert_diffable_known_nonsingleton_raises` — same family but `nash_set_singleton=False` and `disclose=False` → raises; `disclose=True` → ok.
9. `test_diff_charts_guarded_and_payload` — two same-family chart payloads with differing `ranges` → returns `changed`/`added`/`removed` correctly; cross-family without disclose → raises before diffing.
10. (optional) `test_read_chart_file_provenance_roundtrip` — `tmp_path` write of a stamped payload → `read_chart_file_provenance` returns the block.

Also add **2 backward-compat regression assertions** (can live in this file or extend existing tests):
- `test_mafp_writer_stamps_provenance` (extend `test_mafp_chart_refinement.py` or new): `write_mafp_chart(...)` output JSON now has `solver_provenance.solver_family == "mafp"` AND `load_mafp_chart_ranges` still returns the ranges dict.
- `test_append_deploy_record_solver_family_optional` (extend `test_deploy_registry.py`): row with `solver_family="cfr+"` writes `"cfr_plus"`; row without the kwarg has no `solver_family` key.

#### P0.5 — Script: `scripts/run_solver_provenance.sh`

```bash
#!/usr/bin/env bash
# K136 P0 — solver provenance stamp + guarded diff demo (offline).
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Provenance unit suite"
uv run pytest tests/test_solver_provenance.py -q

echo "==> Print provenance on existing charts (if present)"
for f in research/mafp_hu_chart.json research/preflop.json; do
  [[ -f "$f" ]] && uv run python examples/solver_provenance.py --print "$f" || true
done

echo "==> Guarded diff demo (same file -> diffable, exit 0)"
uv run python examples/solver_provenance.py --diff research/mafp_hu_chart.json research/mafp_hu_chart.json || true

echo "K136 P0 provenance checks complete."
```

---

### P1 — FP→PED spike on 3-player Kuhn (optional literacy)

#### P1.1 — New module: `examples/kuhn3p_solver.py`

Pure-Python tabular game + solvers. Stdlib only. **No** `pokerkit`/`treys` — the game is a hand-rolled extensive-form tree.

**Game definition (`KuhnPoker3P`):**

- `__init__(self, deck_size: int = 4)` — `4 <= deck_size <= 6`; raise `ValueError` otherwise. Cards are ints `0..deck_size-1` (higher = stronger). `N_PLAYERS = 3`, `ANTE = 1`, `BET = 1`.
- **Chance:** uniform over all ordered 3-card deals without replacement (`itertools.permutations(range(deck_size), 3)`); deck_size=4 → 24 deals, deck_size=6 → 120 deals.
- **Betting (single round, one bet cap):** action order is round-robin starting at P0. Legal actions: when no bet is outstanding → `"check"` / `"bet"`; when a bet is outstanding → `"call"` / `"fold"`. Round closes when either (a) all three players checked (showdown among all), or (b) a bet was made and every other still-live player has called or folded. Players who checked before a bet get exactly one later call/fold decision when the bet reaches them.
- **Payoffs (zero-sum, 3-vector summing to 0):** pot = antes + calls. At showdown the live player with the highest card wins the pot; each player's payoff = (chips won from pot) − (chips put in). If all but one fold, the last live player takes the pot. Helper `terminal_payoffs(deal, history) -> tuple[float, float, float]`.
- **Information set key:** `infoset_key(player: int, card: int, history: str) -> str` → `f"P{player}|c{card}|{history}"` where `history` is the public action string (e.g. `"xxb"` = P0 check, P1 check, P2 bet). Private cards of others are never in the key.
- **Tree walk:** `iter_infosets()` enumerates all `(player, card, history)` reachable infosets and their legal action lists. `legal_actions(history) -> list[str]`.

**Strategy representation:** behavioral strategy `dict[str, list[float]]` keyed by infoset → probability over `legal_actions` (in canonical order). Helper `uniform_strategy(game) -> dict`.

**Core evaluation:**

| Function | Signature | Behavior |
|---|---|---|
| `expected_payoffs` | `(game, strategy) -> tuple[float,float,float]` | Full-tree expectation of each player's payoff under a behavioral profile (average over chance deals). Recursive tree traversal; deterministic. |
| `best_response_value` | `(game, strategy, player) -> float` | Player `player`'s value when they best-respond to the others' fixed `strategy` (others keep behavioral probs). Full-tree DP over `player`'s infosets. |
| `nashconv` | `(game, strategy) -> float` | Generalized exploitability = `sum_i (best_response_value(i) - expected_payoffs[i])`. This is the **PED objective** for multiplayer (2606.29169). Always `>= 0`. |

**Solvers (all return `SolveResult`):**

```python
@dataclass
class SolveResult:
    method: str                 # "cfr" | "fp" | "ped" | "fp_ped"
    iters: int
    strategy: dict[str, list[float]]      # final average (CFR/FP) or last-iterate (PED)
    exploitability_curve: list[tuple[int, float]]  # (iter, nashconv) samples
    final_exploitability: float
    seed: int
```

| Function | Signature | Behavior |
|---|---|---|
| `run_cfr` | `(game, iters, *, seed=0, log_every=10) -> SolveResult` | Vanilla full-tree CFR (regret matching) across all 3 players; track **average** strategy; sample `nashconv(average)` every `log_every` iters. |
| `run_fp` | `(game, iters, *, seed=0, log_every=10) -> SolveResult` | Fictitious play: each iter, every player best-responds (pure) to opponents' running average; update averages; log `nashconv(average)`. |
| `run_exploitability_descent` | `(game, iters, *, init=None, step=0.1, seed=0, log_every=10) -> SolveResult` | **PED-style refinement.** Behavioral-form exploitability descent: each iter, for every player `i`, compute counterfactual action values vs opponents' current behavioral strategy, take a gradient-ascent step on `i`'s own value, then **project each infoset distribution onto the probability simplex** (Euclidean projection; per-infoset simplex projection is the documented simplification of the full sequence-form realization-polytope projection — note this in the docstring and the spike JSON `notes`). Track last-iterate `nashconv`. `init` lets FP-PED hand off a warm strategy. Decaying `step` (e.g. `step / (1 + 0.01*t)`) is acceptable. |
| `run_fp_ped` | `(game, fp_iters, ped_iters, *, seed=0, log_every=10, step=0.1) -> SolveResult` | FP burn-in for `fp_iters` (seed the descent with FP average), then exploitability descent for `ped_iters`. Concatenate curves with a continuous iteration axis; `method="fp_ped"`. Mirrors 2606.29169 FP-PED. |
| `compare_equal_budget` | `(game, budget, *, fp_frac=0.5, seed=0) -> dict` | Run `run_cfr(budget)` vs `run_fp_ped(fp_iters=int(budget*fp_frac), ped_iters=budget-int(budget*fp_frac))`. Return `{"deck_size", "budget", "cfr_final", "fp_ped_final", "winner": "cfr"|"fp_ped"|"tie", "delta": cfr_final - fp_ped_final, "cfr_curve", "fp_ped_curve"}`. Lower `final_exploitability` wins. |

Helper `simplex_project(vec: list[float]) -> list[float]` (Euclidean projection onto the probability simplex; standard sort-based algorithm, stdlib only).

#### P1.2 — Spike sidecar output + deploy log

`write_spike_report(result_cmp: dict, path: Path, *, deck_size: int, seed: int) -> Path` writes `research/kuhn3p_ped_spike.json`, atomic, schema `kuhn3p-ped-spike-v1`, **provenance-stamped** via `solver_provenance`:

```json
{
  "schema": "kuhn3p-ped-spike-v1",
  "source": "examples/kuhn3p_solver.py",
  "deck_size": 4,
  "seed": 42,
  "budget": 200,
  "cfr_final_exploitability": 0.0123,
  "fp_ped_final_exploitability": 0.0098,
  "winner": "fp_ped",
  "delta": 0.0025,
  "cfr_curve": [[10, 0.21], [20, 0.14], ...],
  "fp_ped_curve": [[10, 0.19], [20, 0.11], ...],
  "solver_provenance": {
    "schema": "solver-provenance-v1",
    "solver_family": "fp_ped",
    "solver_version": "1",
    "equilibrium_selection": "last_iterate",
    "nash_set_singleton": false,
    "stamped_at": "...Z",
    "notes": "3p Kuhn deck=4; per-infoset simplex projection (sequence-form polytope projection simplified); literacy spike, not transferable to NLHE"
  }
}
```

On completion, log one `deploys.jsonl` row (only if not `--no-deploy-log`):

```python
append_deploy_record(
    source="kuhn3p_ped_spike",
    commit=git_commit_short(),
    solver_family="fp_ped",
    notes=json.dumps({
        "deck_size": deck_size, "budget": budget,
        "cfr_final": cfr_final, "fp_ped_final": fp_ped_final, "winner": winner,
    }),
)
```

#### P1.3 — `main(argv)` CLI

```
python examples/kuhn3p_solver.py [--deck-size 4] [--budget 200] [--fp-frac 0.5]
        [--seed 42] [--step 0.1] [--no-write] [--no-deploy-log]
```

Prints a short table: deck size, budget split, CFR final exploitability, FP-PED final exploitability, winner, delta. Writes `research/kuhn3p_ped_spike.json` unless `--no-write`. Exit 0 on success, 1 if no result.

#### P1.4 — Tests: `tests/test_kuhn3p_solver.py` (minimum **12 tests**)

Resilient import style (sys.path insert; `importlib.import_module("kuhn3p_solver")`; `_require_attr`). Keep iteration counts tiny so the suite stays fast (<5 s); use `deck_size=4`, budgets ≤ 60 in tests.

1. `test_deck_size_bounds` — `KuhnPoker3P(3)` and `KuhnPoker3P(7)` raise `ValueError`; 4/5/6 ok.
2. `test_deal_count` — deck_size=4 → 24 ordered deals; deck_size=6 → 120.
3. `test_infoset_key_hides_opponent_cards` — key contains only own card + public history; two deals with same (player, card, history) map to the same key.
4. `test_legal_actions_transitions` — empty history → `["check","bet"]`; after a `"bet"` → `["call","fold"]`.
5. `test_terminal_payoffs_zero_sum` — for several deals/histories, payoffs sum to 0.0 (within 1e-9).
6. `test_terminal_payoffs_all_check_showdown` — all-check line: highest card wins the antes; explicit numeric check on a known deal.
7. `test_terminal_payoffs_fold_gives_pot` — bet then two folds → bettor nets the antes; numeric check.
8. `test_nashconv_nonneg` — `nashconv(uniform_strategy)` ≥ 0.
9. `test_simplex_project_valid` — projects an arbitrary vector to nonneg entries summing to 1.0; already-valid distribution is unchanged (within 1e-9).
10. `test_cfr_reduces_exploitability` — `run_cfr(game, 60)` final exploitability < `nashconv(uniform)` (monotone-ish improvement, allow small slack).
11. `test_fp_reduces_exploitability` — `run_fp(game, 60)` final exploitability < `nashconv(uniform)`.
12. `test_exploitability_descent_last_iterate_improves` — `run_exploitability_descent(game, 60)` final < uniform; curve is a list of `(int, float)`.
13. `test_fp_ped_curve_continuous` — `run_fp_ped(game, fp_iters=30, ped_iters=30)` curve length ≥ 2, iteration axis strictly increasing, `method=="fp_ped"`.
14. `test_compare_equal_budget_shape` — `compare_equal_budget(game, budget=60)` returns required keys, `winner in {"cfr","fp_ped","tie"}`, `delta == cfr_final - fp_ped_final`.
15. `test_write_spike_report_provenance` (`tmp_path`) — `write_spike_report` JSON has `schema=="kuhn3p-ped-spike-v1"` and `solver_provenance.solver_family=="fp_ped"`; readable back via `read_chart_file_provenance`.

#### P1.5 — Script: `scripts/run_kuhn3p_ped_spike.sh`

```bash
#!/usr/bin/env bash
# K136 P1 — FP->PED spike on 3-player Kuhn (offline, reference-only literacy).
#   ./scripts/run_kuhn3p_ped_spike.sh
#   ./scripts/run_kuhn3p_ped_spike.sh --deck-size 6 --budget 400
set -euo pipefail
cd "$(dirname "$0")/.."

DECK=4
BUDGET=200
EXTRA_ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --deck-size) DECK="${2:-4}"; shift 2 ;;
    --budget)    BUDGET="${2:-200}"; shift 2 ;;
    *) EXTRA_ARGS+=("$1"); shift ;;
  esac
done

echo "==> kuhn3p solver unit suite"
uv run pytest tests/test_kuhn3p_solver.py -q

echo "==> FP->PED vs CFR equal-budget spike (deck=${DECK}, budget=${BUDGET})"
CMD=(uv run python examples/kuhn3p_solver.py --deck-size "$DECK" --budget "$BUDGET" --seed 42)
[[ ${#EXTRA_ARGS[@]} -gt 0 ]] && CMD+=("${EXTRA_ARGS[@]}")
"${CMD[@]}"

echo "Spike complete — report: research/kuhn3p_ped_spike.json"
```

---

### Commands

```bash
cd agents/devfun-poker-arena

# P0 — provenance
uv run pytest tests/test_solver_provenance.py -q
uv run pytest tests/test_mafp_chart_refinement.py tests/test_deploy_registry.py -q   # backward compat
bash scripts/run_solver_provenance.sh
uv run python examples/solver_provenance.py --print research/mafp_hu_chart.json
uv run python examples/solver_provenance.py --diff research/mafp_hu_chart.json research/preflop.json   # cross-family -> exit 3
uv run python examples/solver_provenance.py --diff research/mafp_hu_chart.json research/preflop.json --disclose

# P1 — spike
uv run pytest tests/test_kuhn3p_solver.py -q
bash scripts/run_kuhn3p_ped_spike.sh
uv run python examples/kuhn3p_solver.py --deck-size 4 --budget 200 --no-deploy-log

# syntax
python -m py_compile examples/solver_provenance.py examples/kuhn3p_solver.py

# full suite (must stay green)
uv run pytest tests/ -q
```

### Acceptance criteria

- [ ] `examples/solver_provenance.py` imports stdlib only (`py_compile` clean; no `pyproject.toml` change); defines `SOLVER_FAMILIES`, `SolverProvenanceError`, and every function in P0.1.
- [ ] `solver_provenance(...)` produces a `solver-provenance-v1` block; `stamp_chart_provenance` does not mutate input; `read_chart_provenance` returns `None` (never raises) on pre-K136 payloads.
- [ ] `assert_diffable` / `diff_charts` **raise** on cross-family or known-non-singleton inputs unless `disclose=True`; same-family singleton-unknown inputs diff cleanly.
- [ ] `write_mafp_chart` now stamps `solver_family="mafp"`; `_export_preflop_json` stamps `"static_chart"`; both `load_mafp_chart_ranges` and `load_preflop_chart` still return ranges (backward compat).
- [ ] `append_deploy_record(..., solver_family="cfr+")` writes `"cfr_plus"`; omitting the kwarg leaves rows unchanged; `DEPLOY_SCHEMA` unchanged.
- [ ] Existing `test_mafp_chart_refinement.py` and `test_deploy_registry.py` pass unchanged.
- [ ] `tests/test_solver_provenance.py` green with ≥9 tests (+2 backward-compat regression assertions).
- [ ] `examples/kuhn3p_solver.py` imports stdlib only; builds a 3p Kuhn tree with no `pokerkit`/`treys`; deals = 24 (deck 4) / 120 (deck 6); terminal payoffs zero-sum.
- [ ] `nashconv(uniform) >= 0`; `run_cfr`, `run_fp`, `run_exploitability_descent`, `run_fp_ped` all reduce final exploitability below uniform on deck=4; `compare_equal_budget` returns a `winner` and matching `delta`.
- [ ] `research/kuhn3p_ped_spike.json` is `kuhn3p-ped-spike-v1`, provenance-stamped `solver_family="fp_ped"`, includes both exploitability curves and the equal-budget verdict; one `deploys.jsonl` row logged (unless `--no-deploy-log`).
- [ ] `tests/test_kuhn3p_solver.py` green with ≥12 tests; full `uv run pytest tests/ -q` green.
- [ ] No edits to `agent.py` `decide()` logic; no edits outside `examples/`, `research/`, `scripts/`, `tests/`, `config/` (AGENTS.md file-scope rule).
- [ ] Spike JSON + module docstrings explicitly disclose: (a) per-infoset simplex projection is a documented simplification of sequence-form polytope projection; (b) Kuhn results do **not** transfer to NLHE without measurement (2606.28308 / 2606.29169 regime caveat).

## Sources

- `briefs/2026-06-30_k136-nash-solver-fp-ped-steal.md` — scope (P0/P1, out-of-scope, constraints)
- `briefs/2026-06-29_k134-rqgm-implementation-plan.md` — format template (phases / schema / tests / acceptance)
- `examples/deploy_registry.py` — `append_deploy_record`, `deploys.jsonl` (`devfun.deploy_record.v1`)
- `examples/mafp_chart_refinement.py` — K124 pattern (offline spike, atomic chart write, deploy log)
- `examples/research_static_chart.py` — chart export + `_export_preflop_json` provenance hook
- `research/mafp_hu_chart.json` — `mafp-hu-chart-v1` sidecar schema
- @wiki/concepts/nash-equilibrium-solver-selection.md — 2606.28308 solver-family selection (P0 motivation)
- @wiki/concepts/projected-exploitability-descent.md — 2606.29169 FP-PED hybrid (P1 motivation)
- @wiki/concepts/kuhn-poker-sft-curriculum-reference.md — Kuhn≠NLHE regime disclosure
- [Source: arXiv:2606.28308 (retrieved 2026-06-30)], [Source: arXiv:2606.29169 (retrieved 2026-06-30)]
