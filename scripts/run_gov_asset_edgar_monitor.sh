#!/usr/bin/env bash
# run_gov_asset_edgar_monitor.sh — SEC EDGAR full-text watcher (gov-asset-rerate thesis)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"

ARGS=()
for arg in "$@"; do
  ARGS+=("$arg")
done

if ((${#ARGS[@]})); then
  python3 scripts/intel/monitors/edgar_fulltext.py "${ARGS[@]}"
else
  python3 scripts/intel/monitors/edgar_fulltext.py
fi
