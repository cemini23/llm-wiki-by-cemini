#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/osint/meta/kalshi-lp-backtest-cadence.md"
DAYS="${KALSHI_LP_BACKTEST_CADENCE_DAYS:-90}"

if [[ ! -f "$META" ]]; then
  echo "kalshi-lp-backtest: no cadence file"
  exit 0
fi

LAST=$(grep -E '^\| \*\*Last run\*\*' "$META" | sed -E 's/.*\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) .*/\1/' | head -1)
[[ -z "$LAST" ]] && exit 0

LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST" "+%s" 2>/dev/null || date -d "$LAST" "+%s")
NOW_EPOCH=$(date "+%s")
AGE=$(( (NOW_EPOCH - LAST_EPOCH) / 86400 ))

if [[ "$AGE" -ge "$DAYS" ]]; then
  echo "kalshi-lp-backtest DUE (${AGE}d since ${LAST})"
  exit 0
fi
echo "kalshi-lp-backtest ok (${AGE}d since ${LAST}, due in $((DAYS - AGE))d)"
exit 1
