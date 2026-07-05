#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE="$ROOT/.local/reports/ice-facility-jobs/last_run_state.json"
TODAY="$(date +%F)"

if [[ ! -f "$STATE" ]]; then
  echo "DUE: no ICE facility jobs monitor state found"
  exit 0
fi

LAST_RUN="$(python3 - <<'PY' "$STATE"
import json, sys
from pathlib import Path
path = Path(sys.argv[1])
try:
    print(json.loads(path.read_text(encoding="utf-8")).get("last_run", ""))
except Exception:
    print("")
PY
)"

if [[ "$LAST_RUN" != "$TODAY" ]]; then
  echo "DUE: last ICE facility jobs monitor run was ${LAST_RUN:-unknown}"
  exit 0
fi

echo "OK: ICE facility jobs monitor already ran today ($LAST_RUN)"
exit 1
