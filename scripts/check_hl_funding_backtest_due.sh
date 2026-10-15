#!/usr/bin/env bash
# Exit 0 if HL funding Dune backtest is due (today >= next_due). For session-start ritual.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
META="$ROOT/wiki/osint/meta/hl-funding-backtest-cadence.md"
if [[ ! -f "$META" ]]; then
  echo "hl-funding-backtest: no cadence file"
  exit 1
fi
NEXT=$(grep -E '^\| Next due \|' "$META" | sed -E 's/.*\*\*([0-9]{4}-[0-9]{2}-[0-9]{2})\*\*.*/\1/')
TODAY=$(date +%Y-%m-%d)
if [[ "$TODAY" < "$NEXT" ]]; then
  echo "hl-funding-backtest: not due until $NEXT (today $TODAY)"
  exit 1
fi
echo "hl-funding-backtest: DUE (next_due=$NEXT, today=$TODAY)"
exit 0
