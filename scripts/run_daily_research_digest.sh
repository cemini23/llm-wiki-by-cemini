#!/usr/bin/env bash
# run_daily_research_digest.sh — morning discovery digest (Phase 1).
#
# Usage:
#   bash scripts/run_daily_research_digest.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
REPORT="$ROOT/wiki/sweeps/${TODAY}-daily.md"
LOG="$HOME/Library/Logs/cemini-daily-digest.log"

mkdir -p "$(dirname "$LOG")"

bash "$ROOT/scripts/daily_research_digest.sh" | tee -a "$LOG"

echo "Report: $REPORT"
