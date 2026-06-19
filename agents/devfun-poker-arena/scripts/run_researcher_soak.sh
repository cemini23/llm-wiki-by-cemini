#!/usr/bin/env bash
# Researcher Track soak runner.
#
# Runs a HU (2-player) local selfplay soak with trajectory export, generates the
# researcher axis summary, enforces --gate thresholds, then appends a deploy
# audit row tagged source=researcher_soak so long-run readiness checks land in
# reports/hl-loop/deploys.jsonl.
#
# Usage:
#   ./scripts/run_researcher_soak.sh
#   ./scripts/run_researcher_soak.sh --hands 4000
set -euo pipefail
cd "$(dirname "$0")/.."

HANDS=2000
while [[ $# -gt 0 ]]; do
  case "$1" in
    --hands)
      HANDS="${2:-2000}"
      shift 2
      ;;
    *)
      echo "ERROR: unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

TS=$(date -u +%Y%m%dT%H%M%SZ)
BUNDLE_DIR="reports/researcher-round/soak-${TS}"
TRAJ_FILE="${BUNDLE_DIR}/selfplay_trajectory.jsonl"
mkdir -p "$BUNDLE_DIR"

echo "==> Researcher soak selfplay (${HANDS} hands, HU)"
CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 CEMINI_GIN_V008=1 \
  CEMINI_TABLE_FORMAT=hu \
  uv run python examples/selfplay.py \
  --agent examples/cemini_decide.py \
  --hands "$HANDS" \
  --players 2 \
  --opponent tight \
  --seed 42 \
  --trajectory-out "$TRAJ_FILE"

echo "==> Trajectory + axis summary"
./scripts/export_researcher_trajectory.sh \
  --selfplay "$TRAJ_FILE" \
  --out-dir "$BUNDLE_DIR"

uv run python examples/researcher_trajectory_summary.py \
  --selfplay "$TRAJ_FILE" \
  --out-dir "$BUNDLE_DIR" \
  --gate

echo "==> Append deploy record"
uv run python - "$BUNDLE_DIR/axis_summary.json" "$HANDS" "$BUNDLE_DIR" <<'PY'
from __future__ import annotations

import json
import sys
from pathlib import Path

root = Path.cwd()
examples = root / "examples"
if str(examples) not in sys.path:
    sys.path.insert(0, str(examples))

from deploy_registry import append_deploy_record  # noqa: E402

axis_path = Path(sys.argv[1])
hands = int(sys.argv[2])
bundle_dir = sys.argv[3]
manifest = json.loads(axis_path.read_text(encoding="utf-8"))
gate_pass = bool(manifest.get("gate_pass"))
row = append_deploy_record(
    source="researcher_soak",
    hands=hands,
    preflight="researcher_gate",
    notes=f"gate_pass={str(gate_pass).lower()} hands={hands} bundle={bundle_dir}",
)
print(json.dumps(row, indent=2, sort_keys=True))
PY

echo ""
echo "RESEARCHER SOAK OK — bundle: ${BUNDLE_DIR}"
