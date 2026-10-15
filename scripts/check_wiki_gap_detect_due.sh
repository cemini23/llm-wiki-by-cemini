#!/usr/bin/env bash
# Exit 0 if wiki gap detect Tier 1 report is due (≥7 days since last run).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/osint/meta/wiki-gap-detect-cadence.md"
DAYS="${WIKI_GAP_DETECT_CADENCE_DAYS:-7}"

if [[ ! -f "$META" ]]; then
  echo "wiki-gap-detect: no cadence file"
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
  echo "wiki-gap-detect DUE (${AGE}d since ${LAST})"
  exit 0
fi
echo "wiki-gap-detect ok (${AGE}d since ${LAST}, due in $((DAYS - AGE))d)"
exit 1
