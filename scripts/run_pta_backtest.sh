#!/usr/bin/env bash
# PTA reproduction pilot — laptop orchestrates; data from librarian ArcticDB (SSH).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/scripts${PYTHONPATH:+:$PYTHONPATH}"
PY="${PY:-python3}"
"$PY" scripts/equity_signal_backtest/pta_pilot.py "$@"
