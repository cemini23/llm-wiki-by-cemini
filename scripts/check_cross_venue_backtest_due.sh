#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/meta/cross-venue-backtest-cadence.md"
DAYS="${CROSS_VENUE_BACKTEST_CADENCE_DAYS:-90}"
[[ ! -f "$META" ]] && exit 0
LAST=$(grep -E '^\| \*\*Last run\*\*' "$META" | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) .*/\1/' | head -1)
[[ -z "$LAST" ]] && exit 0
LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST" "+%s" 2>/dev/null || date -d "$LAST" "+%s")
AGE=$(( ($(date "+%s") - LAST_EPOCH) / 86400 ))
[[ "$AGE" -ge "$DAYS" ]] && { echo "cross-venue-backtest DUE (${AGE}d)"; exit 0; }
echo "cross-venue-backtest ok"; exit 1
