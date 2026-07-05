#!/usr/bin/env bash
# Run all ICE turnkey weak-signal monitors (detention stats → jobs).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"

python3 scripts/intel/monitors/detention_stats.py "$@"
python3 scripts/intel/monitors/jobs.py "$@"
