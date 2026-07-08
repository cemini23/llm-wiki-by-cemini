#!/usr/bin/env bash
# run_gov_asset_procurement_monitor.sh — USASpending diligence-signal watcher (gov-asset-rerate)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"

ARGS=()
for arg in "$@"; do
  ARGS+=("$arg")
done

if ((${#ARGS[@]})); then
  python3 scripts/intel/monitors/procurement.py "${ARGS[@]}"
else
  python3 scripts/intel/monitors/procurement.py
fi
