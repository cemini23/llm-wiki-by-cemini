#!/usr/bin/env bash
# Researcher Round pre-submit gate.
#
# Table format is controlled by CEMINI_TABLE_FORMAT:
#   hu (default)   -> Researcher sandbox is HU [CONFIRMED dev.fun 2026-06-08]
#   6max           -> 6-max regression + selfplay (Playground intel only)
#   auto           -> run both 6-max and HU bundles, then merge trajectories
#                     into one combined gate summary at the bundle root
#
# Usage:
#   ./scripts/run_hu_sandbox_gate.sh
#   ./scripts/run_hu_sandbox_gate.sh --hands 500
set -euo pipefail
cd "$(dirname "$0")/.."

HANDS=200
FINALE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --hands)
      HANDS="${2:-200}"
      shift 2
      ;;
    --finale)
      FINALE="${2:-}"
      shift 2
      ;;
    *)
      echo "ERROR: unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

TABLE_FORMAT="${CEMINI_TABLE_FORMAT:-hu}"
case "$TABLE_FORMAT" in
  auto|hu|6max) ;;
  *)
    echo "ERROR: CEMINI_TABLE_FORMAT must be one of auto|hu|6max" >&2
    exit 2
    ;;
esac

TS=$(date -u +%Y%m%dT%H%M%SZ)
BUNDLE_DIR="reports/researcher-round/gate-${TABLE_FORMAT}-${TS}"
MERGED_TRAJ_FILE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
mkdir -p "$BUNDLE_DIR"

run_summary() {
  local traj_file="$1"
  local out_dir="$2"
  local gate_flag="${3:-0}"
  ./scripts/export_researcher_trajectory.sh \
    --selfplay "$traj_file" \
    --out-dir "$out_dir"
  if [[ "$gate_flag" == "1" ]]; then
    uv run python examples/researcher_trajectory_summary.py \
      --selfplay "$traj_file" \
      --out-dir "$out_dir" \
      --gate
  else
    uv run python examples/researcher_trajectory_summary.py \
      --selfplay "$traj_file" \
      --out-dir "$out_dir"
  fi
}

run_selfplay_bundle() {
  local label="$1"
  local players="$2"
  local opponent="$3"
  local out_dir="$4"
  local traj_file="${out_dir}/selfplay_trajectory.jsonl"
  local summary_file="${out_dir}/selfplay_summary.txt"
  mkdir -p "$out_dir"
  echo "==> ${label} selfplay gate (${HANDS} hands, players=${players}, opponent=${opponent})"
  CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 CEMINI_GIN_V008=1 \
    CEMINI_S1B_EXPLOIT=1 CEMINI_RESEARCHER_MODE=1 \
    uv run python examples/selfplay.py \
    --agent examples/harness_sandbox_agent.py \
    --hands "$HANDS" \
    --players "$players" \
    --opponent "$opponent" \
    --seed 42 \
    --trajectory-out "$traj_file" | tee "$summary_file"
  if [[ "$players" == "2" ]]; then
    match_line="$(grep -E 'match_win_rate:' "$summary_file" || true)"
    if [[ -n "$match_line" ]]; then
      echo "==> ${label} ${match_line#  }"
    fi
  fi
  run_summary "$traj_file" "$out_dir" 0
}

run_finale_gate() {
  local villain="$1"
  local opponent="$2"
  local out_dir="$3"
  local traj_file="${out_dir}/selfplay_trajectory.jsonl"
  mkdir -p "$out_dir"
  echo "==> Finale gate (${villain}, ${HANDS}h vs ${opponent})"
  CEMINI_TABLE_FORMAT=hu CEMINI_RESEARCHER_MODE=1 \
    CEMINI_FINALE_EXPLOIT=1 CEMINI_FINALE_VILLAIN="${villain}" \
    CEMINI_S1B_EXPLOIT=0 CEMINI_NEMESIS_EXPLOIT=0 \
    uv run python examples/selfplay.py \
    --agent examples/harness_sandbox_agent.py \
    --hands "$HANDS" \
    --players 2 \
    --opponent "$opponent" \
    --seed 42 \
    --trajectory-out "$traj_file" | tee "${out_dir}/finale_summary.txt"
  run_summary "$traj_file" "$out_dir" 0
}

merge_trajectories() {
  local out_file="$1"
  shift
  uv run python - "$out_file" "$@" <<'PY'
import json
import sys
from pathlib import Path

out_path = Path(sys.argv[1])
inputs = [Path(p) for p in sys.argv[2:]]
rows_out: list[str] = []
hand_offset = 0

for path in inputs:
    max_hand = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        row = json.loads(raw)
        hand_id = row.get("hand_id")
        if hand_id is not None:
            new_id = int(hand_id) + hand_offset
            row["hand_id"] = new_id
            max_hand = max(max_hand, new_id)
        rows_out.append(json.dumps(row, sort_keys=True))
    hand_offset = max_hand

out_path.write_text("\n".join(rows_out) + ("\n" if rows_out else ""), encoding="utf-8")
PY
}

SELFPLAY_TRAJ_FOR_GATE=""

case "$TABLE_FORMAT" in
  6max)
    echo "==> 6-max regression (full + HU smoke)"
    uv run pytest tests/test_cemini_regression.py tests/test_hu_regression.py -q --tb=line
    run_selfplay_bundle "6-max" 6 mixed "$BUNDLE_DIR"
    SELFPLAY_TRAJ_FOR_GATE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
    ;;
  hu)
    echo "==> HU regression"
    uv run pytest tests/test_hu_regression.py -q --tb=line
    echo "==> K146 substrate gate (docs CLI + AST audit)"
    bash scripts/run_substrate_gate.sh "${BUNDLE_DIR}/substrate"
    run_selfplay_bundle "HU-tight" 2 tight "$BUNDLE_DIR"
    echo "==> HU TEN wide-passive advisory (K150 ladder nemesis)"
    mkdir -p "${BUNDLE_DIR}/ten-audit"
    CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_V008=1 \
      CEMINI_S1B_EXPLOIT=1 CEMINI_RESEARCHER_MODE=1 \
      CEMINI_NEMESIS_EXPLOIT=1 CEMINI_NEMESIS_TIGHT=1 CEMINI_NEMESIS_ARCHETYPE=1 \
      CEMINI_NEMESIS_WIDE_PASSIVE=1 CEMINI_ISO_PASSIVE_LP=1 \
      CEMINI_SELFPLAY_VILLAIN_HANDLE=TEN \
      uv run python examples/selfplay.py \
        --agent examples/harness_sandbox_agent.py \
        --hands "$HANDS" --players 2 --opponent ten --seed 42 \
        --trajectory-out "${BUNDLE_DIR}/ten-audit/selfplay_trajectory.jsonl" \
        | tee "${BUNDLE_DIR}/ten-audit/summary.txt"
    ten_bb="$(grep -E 'bb/100' "${BUNDLE_DIR}/ten-audit/summary.txt" | tail -1 || true)"
    if [[ -n "$ten_bb" ]]; then
      echo "==> Advisory TEN: ${ten_bb#  } (target ≥0 bb/100 vs wide_passive steal)"
    fi
    echo "==> HU maniac_shark_lite_2 LAG advisory (K151 ladder nemesis)"
    mkdir -p "${BUNDLE_DIR}/maniac-shark-audit"
    CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_V008=1 \
      CEMINI_S1B_EXPLOIT=1 CEMINI_RESEARCHER_MODE=1 \
      CEMINI_NEMESIS_EXPLOIT=1 CEMINI_NEMESIS_TIGHT=1 CEMINI_NEMESIS_ARCHETYPE=1 \
      CEMINI_NEMESIS_LINEAR_AGGRO=1 \
      CEMINI_SELFPLAY_VILLAIN_HANDLE=maniac_shark_lite_2 \
      uv run python examples/selfplay.py \
        --agent examples/harness_sandbox_agent.py \
        --hands "$HANDS" --players 2 --opponent maniac_shark_lag --seed 43 \
        --trajectory-out "${BUNDLE_DIR}/maniac-shark-audit/selfplay_trajectory.jsonl" \
        | tee "${BUNDLE_DIR}/maniac-shark-audit/summary.txt"
    shark_bb="$(grep -E 'bb/100' "${BUNDLE_DIR}/maniac-shark-audit/summary.txt" | tail -1 || true)"
    if [[ -n "$shark_bb" ]]; then
      echo "==> Advisory maniac_shark: ${shark_bb#  } (target ≥0 bb/100 vs linear_aggro steal)"
    fi
    echo "==> HU maniac/lag series audit (400h, 80h/match)"
    mkdir -p "${BUNDLE_DIR}/maniac-audit"
    CEMINI_TABLE_FORMAT=hu CEMINI_GIN_STYLE=1 CEMINI_S1B_EXPLOIT=1 CEMINI_RESEARCHER_MODE=1 \
      uv run python examples/cemini_selfplay_audit.py \
        --hands 400 --players 2 --gate \
        --match-hands 80 \
        --min-match-win-rate 0.55 \
        --min-match-win-maniac 0 \
        --min-match-win-lag 0.45 \
        | tee "${BUNDLE_DIR}/maniac-audit/audit_gate.txt"
    maniac_swr="$(grep 'series_win_rate (maniac):' "${BUNDLE_DIR}/maniac-audit/audit_gate.txt" | tail -1 || true)"
    if [[ -n "$maniac_swr" ]]; then
      echo "==> Advisory maniac: ${maniac_swr#  } (target ≥38% pre-Jun 21)"
    fi
    lag_swr="$(grep 'series_win_rate (lag):' "${BUNDLE_DIR}/maniac-audit/audit_gate.txt" | tail -1 || true)"
    if [[ -n "$lag_swr" ]]; then
      echo "==> Advisory lag: ${lag_swr#  } (gated target ≥45%)"
    fi
    SELFPLAY_TRAJ_FOR_GATE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
    ;;
  auto)
    echo "==> 6-max regression (full + HU smoke)"
    uv run pytest tests/test_cemini_regression.py tests/test_hu_regression.py -q --tb=line
    run_selfplay_bundle "6-max" 6 mixed "${BUNDLE_DIR}/6max"
    echo "==> HU regression"
    uv run pytest tests/test_hu_regression.py -q --tb=line
    echo "==> K146 substrate gate (docs CLI + AST audit)"
    bash scripts/run_substrate_gate.sh "${BUNDLE_DIR}/substrate"
    run_selfplay_bundle "HU" 2 tight "${BUNDLE_DIR}/hu"
    echo "==> Merge 6-max + HU trajectories for combined gate"
    merge_trajectories \
      "$MERGED_TRAJ_FILE" \
      "${BUNDLE_DIR}/6max/selfplay_trajectory.jsonl" \
      "${BUNDLE_DIR}/hu/selfplay_trajectory.jsonl"
    SELFPLAY_TRAJ_FOR_GATE="$MERGED_TRAJ_FILE"
    ;;
esac

echo "==> Trajectory + axis summary (submit gates)"
run_summary "$SELFPLAY_TRAJ_FOR_GATE" "$BUNDLE_DIR" 1

echo "==> K132 tri-verifier (Fara harness regression)"
bash scripts/run_sandbox_tri_verifier.sh

echo "==> K134 RQGM epoch stamp + advisory promotion gate"
uv run python examples/sandbox_rubric_epoch.py --print | tee "${BUNDLE_DIR}/rubric_epoch.txt"
uv run python examples/sandbox_rubric_epoch.py --gate  | tee "${BUNDLE_DIR}/promotion_gate.txt" || true

if [[ -n "$FINALE" ]]; then
  case "$FINALE" in
    durrrr)
      run_finale_gate durrrr durrrr_bomb "${BUNDLE_DIR}/finale-durrrr"
      ;;
    jungleman)
      run_finale_gate jungleman jungleman_calldown "${BUNDLE_DIR}/finale-jungleman"
      ;;
    all)
      run_finale_gate durrrr durrrr_bomb "${BUNDLE_DIR}/finale-durrrr"
      run_finale_gate jungleman jungleman_calldown "${BUNDLE_DIR}/finale-jungleman"
      ;;
    *)
      echo "ERROR: --finale must be durrrr, jungleman, or all" >&2
      exit 2
      ;;
  esac
fi

if [[ -n "${ARENA_RESEARCHER_COMP_ID:-}" ]]; then
  echo "==> Arena trajectory pull (ARENA_RESEARCHER_COMP_ID)"
  if ./scripts/export_researcher_trajectory.sh \
    --competition-id "$ARENA_RESEARCHER_COMP_ID" \
    --out-dir "${BUNDLE_DIR}/arena"; then
    uv run python examples/researcher_trajectory_summary.py \
      --selfplay "$SELFPLAY_TRAJ_FOR_GATE" \
      --export-dir "${BUNDLE_DIR}/arena/arena-export" \
      --out-dir "$BUNDLE_DIR"
  else
    echo "WARN: Arena export skipped — comp may have no recent-tables yet (bundle submit path OK)"
  fi
fi

echo ""
echo "RESEARCHER SANDBOX GATE OK — bundle: ${BUNDLE_DIR}"
echo "Table format: ${TABLE_FORMAT}"
echo "Arena submit: pokerkit run --max-hands 50 (smoke); full season multi-day when Researcher comp live"
