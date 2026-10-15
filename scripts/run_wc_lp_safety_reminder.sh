#!/usr/bin/env bash
# run_wc_lp_safety_reminder.sh — weekly LP safety DR reminder (K84).
# RETIRED 2026-07-28 — World Cup over; no-op.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
LOG="$HOME/Library/Logs/cemini-wc-lp-safety.log"
META="$ROOT/wiki/osint/meta/wc-lp-safety-cadence.md"

mkdir -p "$(dirname "$LOG")"

{
  echo "[$TODAY] WC LP safety reminder — RETIRED (world-cup-bot dropped 2026-07-28)"
  echo "  No Gemini DR / conviction.yaml updates. See wiki/osint/meta/wc-lp-safety-cadence.md"
} | tee -a "$LOG"

exit 0
