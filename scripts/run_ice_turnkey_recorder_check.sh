#!/usr/bin/env bash
# run_ice_turnkey_recorder_check.sh — county recorder deed sweep for ICE turnkey sale signals
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"

ARGS=()
for arg in "$@"; do
  ARGS+=("$arg")
done

if ((${#ARGS[@]})); then
  python3 scripts/intel/monitors/recorder.py "${ARGS[@]}"
else
  python3 scripts/intel/monitors/recorder.py
fi
