#!/usr/bin/env bash
# AutoTS laptop resource benchmark — Phase-0 condition #2 (autots.md).
# Requires: pip install autots[mcp]  (never [additional]; no torch/TVA)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/scripts${PYTHONPATH:+:$PYTHONPATH}"
PY="${PY:-python3}"
"$PY" scripts/autots_benchmark/run.py "$@"
