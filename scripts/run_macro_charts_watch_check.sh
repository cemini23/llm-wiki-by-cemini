#!/usr/bin/env bash
# Prod / laptop runner for Macro Charts watches → Discord.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "$HERE/macro-charts-watch.yaml" && -f "$HERE/macro_charts_watch.py" ]]; then
  # Prod pack: /opt/cemini/macro-charts-watch/
  SCRIPT="$HERE/macro_charts_watch.py"
  CONFIG="$HERE/macro-charts-watch.yaml"
  export MC_WATCH_STATE="${MC_WATCH_STATE:-/opt/cemini/state/macro-charts-watches.json}"
  export MC_WATCH_UW_ENV_FILE="${MC_WATCH_UW_ENV_FILE:-/opt/tipdrop-scanner/.env}"
  LOG="${MC_WATCH_LOG:-/opt/cemini/logs/macro-charts-watch.log}"
  if [[ "$LOG" == "/dev/stdout" ]]; then
    exec python3 "$SCRIPT" --config "$CONFIG" check "$@"
  fi
  mkdir -p "$(dirname "$LOG")"
  {
    echo "==== $(date -u +%Y-%m-%dT%H:%M:%SZ) ===="
    python3 "$SCRIPT" --config "$CONFIG" check "$@"
  } >>"$LOG" 2>&1
else
  # Laptop repo: scripts/ + config/
  ROOT="$(cd "$HERE/.." && pwd)"
  exec python3 "$ROOT/scripts/macro_charts_watch.py" \
    --config "$ROOT/config/macro-charts-watch.yaml" \
    check "$@"
fi
