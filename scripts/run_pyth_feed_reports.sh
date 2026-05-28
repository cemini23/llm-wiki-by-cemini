#!/usr/bin/env bash
# Regenerate Desktop Pyth CSV + JSON reports (Pro API when .env key is set).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${PYTH_REPORT_DIR:-$HOME/Desktop/pyth-reports-$(date +%Y-%m-%d)}"
exec python3 "$ROOT/scripts/pyth_feed_report.py" --out-dir "$OUT" "$@"
