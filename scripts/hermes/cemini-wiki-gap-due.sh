#!/usr/bin/env bash
# Hermes cron watchdog — wiki gap Tier 1. Alerts ONLY when due (degraded).
# No-agent cron: empty stdout = silent tick (no Telegram message).
set -euo pipefail

if [[ -n "${CEMINI_OSINT_ROOT:-}" && -d "${CEMINI_OSINT_ROOT}/scripts" ]]; then
  ROOT="${CEMINI_OSINT_ROOT}"
elif [[ -d "/opt/cemini-osint-workspace/scripts" ]]; then
  ROOT="/opt/cemini-osint-workspace"
elif [[ -d "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts" ]]; then
  ROOT="/Users/claudiobarone/Desktop/OSINT WORKSPACE"
else
  echo "CRITICAL wiki-gap-detect: cannot resolve OSINT root (set CEMINI_OSINT_ROOT)"
  exit 1
fi

CHECK="$ROOT/scripts/check_wiki_gap_detect_due.sh"
RUN="$ROOT/scripts/run_wiki_gap_detect.sh"

if [[ ! -x "$CHECK" ]]; then
  echo "CRITICAL wiki-gap-detect: check script missing at $CHECK"
  exit 1
fi

if "$CHECK" >/dev/null 2>&1; then
  echo "⚠️ DEGRADED — Wiki gap detect Tier 1 is overdue (≥7d since last run)."
  echo "Run: bash $RUN"
  echo "Meta: $ROOT/wiki/meta/wiki-gap-detect-cadence.md"
fi
