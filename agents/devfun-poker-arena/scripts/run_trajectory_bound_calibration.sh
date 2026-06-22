#!/usr/bin/env bash
# K125 trajectory-bound calibration smoke runner.
#
# Usage:
#   ./scripts/run_trajectory_bound_calibration.sh
set -euo pipefail
cd "$(dirname "$0")/.."

BUNDLE_DIR="reports/researcher-round/traj-bound-cal/smoke"
TRAJ_FILE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
CALIBRATION_JSON="${BUNDLE_DIR}/trajectory_bound_calibration.json"
SUMMARY_JSON="${BUNDLE_DIR}/summary.json"

mkdir -p "$BUNDLE_DIR"

export CEMINI_TABLE_FORMAT=hu
export CEMINI_GIN_STYLE=1
export CEMINI_GIN_STYLE_PREFLOP=1
export CEMINI_GIN_STYLE_POSTFLOP=1
export CEMINI_GIN_V008=1
export CEMINI_S1B_EXPLOIT=1
export CEMINI_RESEARCHER_MODE=1

echo "==> K125 trajectory-bound smoke selfplay (50 hands, HU tight)"
uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands 50 \
  --players 2 \
  --opponent tight \
  --seed 42 \
  --trajectory-out "$TRAJ_FILE"

echo "==> K125 calibrate trajectory bounds"
uv run python scripts/calibrate_trajectory_bounds.py \
  --trajectory "$TRAJ_FILE" \
  --out "$CALIBRATION_JSON"

echo "==> K125 trajectory bound report"
uv run python examples/trajectory_bound_report.py \
  --selfplay "$TRAJ_FILE" \
  --config "$CALIBRATION_JSON" \
  --out-dir "$BUNDLE_DIR"
REPORT_JSON="${BUNDLE_DIR}/trajectory_bound_summary.json"

uv run python - "$SUMMARY_JSON" "$TRAJ_FILE" "$CALIBRATION_JSON" "$REPORT_JSON" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

summary_path = Path(sys.argv[1])
payload = {
    "trajectory_jsonl": sys.argv[2],
    "calibration_json": sys.argv[3],
    "report_json": sys.argv[4],
}
summary_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
PY

echo ""
echo "K125 TRAJECTORY BOUND CALIBRATION OK"
echo "  trajectory_jsonl: ${TRAJ_FILE}"
echo "  calibration_json: ${CALIBRATION_JSON}"
echo "  report_json: ${REPORT_JSON}"
echo "  summary_json: ${SUMMARY_JSON}"
