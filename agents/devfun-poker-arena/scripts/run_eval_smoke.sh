#!/usr/bin/env bash
# Run eval-panel smoke (50 hands) on prod; optionally extend to 500 if smoke ≥ threshold.
#
# Usage:
#   ./scripts/run_eval_smoke.sh              # 50-hand smoke only
#   ./scripts/run_eval_smoke.sh --full       # 500-hand confirm if smoke ≥ −12 bb/100
#   ./scripts/run_eval_smoke.sh --local      # run on laptop (needs .arena-credentials)
#
# Logs adjustedBbPer100 to reports/hl-loop/eval_timeseries.jsonl
set -euo pipefail

cd "$(dirname "$0")/.."
AGENT_DIR="$(pwd)"

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
EVAL_COMP="${ARENA_EVAL_COMPETITION_ID:-seed_poker_eval_s1}"
SMOKE_HANDS="${EVAL_SMOKE_HANDS:-50}"
FULL_HANDS="${EVAL_FULL_HANDS:-500}"
SMOKE_FLOOR="${EVAL_SMOKE_FLOOR:-−12}"
# bash doesn't like unicode minus — use ASCII
SMOKE_FLOOR="${EVAL_SMOKE_FLOOR:--12}"
TIMESERIES="${AGENT_DIR}/reports/hl-loop/eval_timeseries.jsonl"
LOG_DIR="${AGENT_DIR}/reports/hl-loop"
FULL=0
LOCAL=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --full) FULL=1; shift ;;
    --local) LOCAL=1; shift ;;
    -h|--help)
      sed -n '2,12p' "$0"
      exit 0
      ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

mkdir -p "${LOG_DIR}"

run_eval() {
  local hands="$1"
  local tag="$2"
  local log="${LOG_DIR}/eval_${tag}_${hands}h.log"

  if [[ "${LOCAL}" -eq 1 ]]; then
    echo "==> Local eval ${hands} hands (${EVAL_COMP}) → ${log}"
    uv run python examples/run_cemini.py \
      --competition-id "${EVAL_COMP}" \
      --max-hands "${hands}" \
      2>&1 | tee "${log}"
    return
  fi

  echo "==> Prod eval ${hands} hands on ${HOST} (${EVAL_COMP})"
  ssh "${HOST}" bash -s <<REMOTE 2>&1 | tee "${log}"
set -euo pipefail
cd "${REMOTE_DIR}"
set -a && source .env && set +a
export ARENA_COMPETITION_ID="${EVAL_COMP}"
./venv/bin/python examples/run_cemini.py \
  --competition-id "${EVAL_COMP}" \
  --max-hands "${hands}"
REMOTE
}

extract_bb100() {
  local log="$1"
  uv run python - <<'PY' "${log}"
import re, sys
text = open(sys.argv[1], errors="replace").read()
# Last adjustedBbPer100= in log (terminal status line)
hits = re.findall(r"adjustedBbPer100=([-+]?\d+(?:\.\d+)?|None|null)", text)
for h in reversed(hits):
    if h not in ("None", "null"):
        print(h)
        break
else:
    sys.exit(1)
PY
}

append_timeseries() {
  local hands="$1"
  local bb100="$2"
  local tag="$3"
  uv run python - <<PY "${TIMESERIES}" "${hands}" "${bb100}" "${tag}" "${EVAL_COMP}"
import json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

path, hands, bb100, tag, comp = sys.argv[1:6]
try:
    sha = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        stderr=subprocess.DEVNULL, text=True,
    ).strip()
except Exception:
    sha = "unknown"
row = {
    "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "tag": tag,
    "competition_id": comp,
    "hands": int(hands),
    "adjustedBbPer100": float(bb100),
    "commit": sha,
}
p = Path(path)
p.parent.mkdir(parents=True, exist_ok=True)
with p.open("a") as f:
    f.write(json.dumps(row) + "\n")
print(f"logged → {p}")
PY
}

SMOKE_LOG="${LOG_DIR}/eval_smoke_${SMOKE_HANDS}h.log"
run_eval "${SMOKE_HANDS}" "smoke"
SMOKE_BB="$(extract_bb100 "${SMOKE_LOG}")"
append_timeseries "${SMOKE_HANDS}" "${SMOKE_BB}" "smoke"

echo ""
echo "Eval smoke: ${SMOKE_HANDS} hands | adjustedBbPer100=${SMOKE_BB} | floor=${SMOKE_FLOOR}"

if [[ "${FULL}" -eq 0 ]]; then
  echo "Pass --full to run ${FULL_HANDS}-hand confirm when smoke ≥ ${SMOKE_FLOOR}"
  exit 0
fi

if uv run python -c "import sys; sys.exit(0 if float('${SMOKE_BB}') >= float('${SMOKE_FLOOR}') else 1)"; then
  FULL_LOG="${LOG_DIR}/eval_full_${FULL_HANDS}h.log"
  run_eval "${FULL_HANDS}" "full"
  FULL_BB="$(extract_bb100 "${FULL_LOG}")"
  append_timeseries "${FULL_HANDS}" "${FULL_BB}" "full"
  echo ""
  echo "Eval full: ${FULL_HANDS} hands | adjustedBbPer100=${FULL_BB}"
else
  echo "Smoke ${SMOKE_BB} < ${SMOKE_FLOOR} — skipping ${FULL_HANDS}-hand confirm"
  exit 1
fi
