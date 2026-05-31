#!/usr/bin/env bash
# Exit 0 if today's daily digest has not run yet (no YYYY-MM-DD-daily.md for today).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
REPORT="$ROOT/wiki/sweeps/${TODAY}-daily.md"

if [[ ! -f "$REPORT" ]]; then
  echo "daily-research-digest DUE (no report for ${TODAY})"
  exit 0
fi

# Stale if file exists but predates today (shouldn't happen with date in name)
mtime=$(stat -f "%Sm" -t "%Y-%m-%d" "$REPORT" 2>/dev/null || stat -c "%y" "$REPORT" | cut -d' ' -f1)
if [[ "$mtime" != "$TODAY" ]]; then
  echo "daily-research-digest DUE (report mtime ${mtime})"
  exit 0
fi

echo "daily-research-digest ok (${TODAY})"
exit 1
