#!/usr/bin/env bash
# Exit 0 if recorder sweep not run in the last 3 days (user-gated cadence).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE="$ROOT/.local/reports/ice-turnkey-recorder/last_run_state.json"

if [[ ! -f "$STATE" ]]; then
  exit 0
fi

last="$(python3 -c "import json; print(json.load(open('$STATE'))['last_run'])")"
today="$(date +%Y-%m-%d)"
# macOS date
last_epoch=$(date -j -f "%Y-%m-%d" "$last" +%s 2>/dev/null || date -d "$last" +%s)
today_epoch=$(date -j -f "%Y-%m-%d" "$today" +%s 2>/dev/null || date -d "$today" +%s)
diff_days=$(( (today_epoch - last_epoch) / 86400 ))

if [[ "$diff_days" -ge 3 ]]; then
  exit 0
fi
exit 1
