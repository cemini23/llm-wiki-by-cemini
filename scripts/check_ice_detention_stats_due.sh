#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE="$ROOT/.local/reports/ice-detention-stats/last_run_state.json"
TODAY="$(date +%F)"
BIWEEKLY_DAYS=14

if [[ ! -f "$STATE" ]]; then
  echo "DUE: no ICE detention stats monitor state found"
  exit 0
fi

read -r LAST_RUN PUBLISH_DATE DAYS_SINCE <<<"$(python3 - <<'PY' "$STATE" "$TODAY" "$BIWEEKLY_DAYS"
import datetime as dt
import json
import sys
from pathlib import Path

state = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
today = dt.date.fromisoformat(sys.argv[2])
biweekly = int(sys.argv[3])
last_run = state.get("last_run", "")
publish = state.get("last_publish_date", "")
days = ""
if publish:
    days = str((today - dt.date.fromisoformat(publish)).days)
print(last_run, publish, days)
PY
)"

if [[ "$LAST_RUN" != "$TODAY" ]]; then
  echo "DUE: last ICE detention stats monitor run was ${LAST_RUN:-unknown}"
  exit 0
fi

if [[ -n "$DAYS_SINCE" && "$DAYS_SINCE" -ge "$BIWEEKLY_DAYS" ]]; then
  echo "DUE: ICE workbook publish is ${DAYS_SINCE}d old (statutory biweekly cadence)"
  exit 0
fi

echo "OK: ICE detention stats monitor ran today; workbook age ${DAYS_SINCE:-unknown}d"
exit 1
