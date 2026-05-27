#!/usr/bin/env bash
# One-shot PM LP backtest → HTML under .local/reports/
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/scripts${PYTHONPATH:+:$PYTHONPATH}"

PY="${PY:-python3}"
if ! "$PY" -c "import plotly, pandas, requests" 2>/dev/null; then
  echo "Install deps: pip install pandas plotly requests pyarrow" >&2
  exit 1
fi

"$PY" scripts/pm_lp_backtest/run.py "$@"
