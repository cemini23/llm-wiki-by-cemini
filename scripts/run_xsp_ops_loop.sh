#!/usr/bin/env bash
# run_xsp_ops_loop.sh — XSP Ops Loop (Macro Charts → brain → queue → packets).
#
# Optional LaunchAgent (Cursor wires install_workflow_launchagents.sh after green):
#   Label:        com.cemini.xsp-ops-loop
#   StartInterval: 3600
#   Program:      this script
#
# Usage:
#   bash scripts/run_xsp_ops_loop.sh
#   bash scripts/run_xsp_ops_loop.sh --dry-run
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="${HOME}/Library/Logs/cemini-xsp-ops.log"
mkdir -p "$(dirname "$LOG")"

# When stdout is a TTY (manual dry-run), tee so operator sees output; LaunchAgent is non-TTY → log only.
run_loop() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] xsp_ops_loop start args=$*"
  set +e
  python3 "$ROOT/scripts/xsp_ops/cli.py" loop "$@"
  local rc=$?
  set -e
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] xsp_ops_loop done exit=${rc}"
  return "${rc}"
}

if [[ -t 1 ]]; then
  run_loop "$@" 2>&1 | tee -a "$LOG"
  # pipeline exit: use PIPESTATUS from tee pipeline
  exit "${PIPESTATUS[0]}"
else
  run_loop "$@" >>"$LOG" 2>&1
fi
