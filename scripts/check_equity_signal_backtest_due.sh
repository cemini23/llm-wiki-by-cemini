#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/meta/equity-signal-backtest-cadence.md"
DAYS="${EQUITY_SIGNAL_BACKTEST_CADENCE_DAYS:-90}"
[[ ! -f "$META" ]] && exit 0
LAST=$(grep -E '^\| \*\*Last run\*\*' "$META" | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) .*/\1/' | head -1)
[[ -z "$LAST" ]] && exit 0
LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST" "+%s" 2>/dev/null || date -d "$LAST" "+%s")
AGE=$(( ($(date "+%s") - LAST_EPOCH) / 86400 ))
[[ "$AGE" -ge "$DAYS" ]] && { echo "equity-signal-backtest DUE (${AGE}d)"; exit 0; }
echo "equity-signal-backtest ok"; exit 1
