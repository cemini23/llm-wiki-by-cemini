#!/usr/bin/env bash
# run_gov_asset_fedreg_monitor.sh — DoD/DOE Federal Register catalyst watcher (gov-asset-rerate)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"

ARGS=()
for arg in "$@"; do
  ARGS+=("$arg")
done

if ((${#ARGS[@]})); then
  python3 scripts/intel/monitors/fedreg.py "${ARGS[@]}"
else
  python3 scripts/intel/monitors/fedreg.py
fi
