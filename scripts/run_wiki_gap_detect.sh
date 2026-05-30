#!/usr/bin/env bash
# run_wiki_gap_detect.sh — Tier 1 gap report to .local/reports/ (K84 workflow).
#
# Usage:
#   bash scripts/run_wiki_gap_detect.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
REPORT_DIR="$ROOT/.local/reports"
REPORT="$REPORT_DIR/wiki-gap-detect-${TODAY}.txt"
META="$ROOT/wiki/meta/wiki-gap-detect-cadence.md"
LOG="$HOME/Library/Logs/cemini-wiki-gap-detect.log"

mkdir -p "$REPORT_DIR"
mkdir -p "$(dirname "$LOG")"

python3 "$ROOT/scripts/wiki_gap_detect.py" | tee "$REPORT" >> "$LOG"

if [[ -f "$META" ]]; then
  NEXT=$(date -v+7d +%Y-%m-%d 2>/dev/null || date -d "+7 days" +%Y-%m-%d)
  sed -i.bak "s/| \*\*Last run\*\* | .*/| **Last run** | ${TODAY} |/" "$META"
  sed -i.bak "s/| \*\*Next due\*\* | .*/| **Next due** | ${NEXT} |/" "$META"
  rm -f "${META}.bak"
fi

echo "Report: $REPORT"
