#!/usr/bin/env bash
# Regenerate HL funding HTML from reference-clone sweep artifacts.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/scripts${PYTHONPATH:+:$PYTHONPATH}"
PY="${PY:-python3}"
"$PY" scripts/hl_funding_backtest/regenerate_report.py "$@"
