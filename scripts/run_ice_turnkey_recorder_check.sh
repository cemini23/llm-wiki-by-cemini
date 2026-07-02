#!/usr/bin/env bash
# run_ice_turnkey_recorder_check.sh — county recorder deed sweep for ICE turnkey sale signals
#
# Usage:
#   bash scripts/run_ice_turnkey_recorder_check.sh              # checklist + baseline index notes
#   bash scripts/run_ice_turnkey_recorder_check.sh --browser    # Playwright
#   bash scripts/run_ice_turnkey_recorder_check.sh --notify     # + Discord on new sale signals
#   bash scripts/run_ice_turnkey_recorder_check.sh --test-discord

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ARGS=()
for arg in "$@"; do
  ARGS+=("$arg")
done

if [[ -n "${LOOKBACK_DAYS:-}" ]]; then
  ARGS+=(--lookback-days "$LOOKBACK_DAYS")
fi

if ((${#ARGS[@]})); then
  python3 scripts/ice_turnkey_recorder_check.py "${ARGS[@]}"
else
  python3 scripts/ice_turnkey_recorder_check.py
fi
