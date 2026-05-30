#!/usr/bin/env bash
# Exit 0 if WC LP safety DR re-run is due (≥7 days since last run).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/meta/wc-lp-safety-cadence.md"
DAYS="${WC_LP_SAFETY_CADENCE_DAYS:-7}"

if [[ ! -f "$META" ]]; then
  echo "wc-lp-safety: no cadence file"
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
  echo "wc-lp-safety DUE (${AGE}d since ${LAST})"
  exit 0
fi
echo "wc-lp-safety ok (${AGE}d since ${LAST}, due in $((DAYS - AGE))d)"
exit 1
