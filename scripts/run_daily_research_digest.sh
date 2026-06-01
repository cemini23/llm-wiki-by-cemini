#!/usr/bin/env bash
# run_daily_research_digest.sh — morning discovery digest (Phase 1).
#
# Usage (from anywhere, after install_workflow_launchagents.sh):
#   cemini-daily-research-digest
#   bash scripts/run_daily_research_digest.sh   # only when cwd is the repo

set -euo pipefail

WRAPPER="$HOME/bin/cemini-daily-research-digest"
if [[ -x "$WRAPPER" ]]; then
  exec "$WRAPPER"
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
REPORT="$ROOT/wiki/sweeps/${TODAY}-daily.md"
LOG="$HOME/Library/Logs/cemini-daily-digest.log"

mkdir -p "$(dirname "$LOG")"

bash "$ROOT/scripts/daily_research_digest.sh" | tee -a "$LOG"

echo "Report: $REPORT"
