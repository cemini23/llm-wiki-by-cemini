#!/usr/bin/env bash
# Exit 0 if PM LP backtest cadence is due (≥90 days since last run in wiki meta).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/meta/pm-lp-backtest-cadence.md"
DAYS="${PM_LP_BACKTEST_CADENCE_DAYS:-90}"

if [[ ! -f "$META" ]]; then
  echo "pm-lp-backtest: no cadence file"
  exit 0
fi

LAST=$(grep -E '^\| \*\*Last run\*\*' "$META" | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) .*/\1/' | head -1)
if [[ -z "$LAST" ]]; then
  exit 0
fi

LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST" "+%s" 2>/dev/null || date -d "$LAST" "+%s")
NOW_EPOCH=$(date "+%s")
AGE=$(( (NOW_EPOCH - LAST_EPOCH) / 86400 ))

if [[ "$AGE" -ge "$DAYS" ]]; then
  echo "pm-lp-backtest DUE (${AGE}d since ${LAST})"
  exit 0
fi
echo "pm-lp-backtest ok (${AGE}d since ${LAST}, due in $((DAYS - AGE))d)"
exit 1
