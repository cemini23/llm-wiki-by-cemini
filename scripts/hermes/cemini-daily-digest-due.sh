#!/usr/bin/env bash
# Hermes cron watchdog — daily research digest. Alerts ONLY when due (no report today).
# No-agent cron: empty stdout = silent tick (no Telegram message).
set -euo pipefail

if [[ -n "${CEMINI_OSINT_ROOT:-}" && -d "${CEMINI_OSINT_ROOT}/scripts" ]]; then
  ROOT="${CEMINI_OSINT_ROOT}"
elif [[ -d "/opt/cemini-osint-workspace/scripts" ]]; then
  ROOT="/opt/cemini-osint-workspace"
elif [[ -d "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts" ]]; then
  ROOT="/Users/claudiobarone/Desktop/OSINT WORKSPACE"
else
  echo "CRITICAL daily-digest: cannot resolve OSINT root (set CEMINI_OSINT_ROOT)"
  exit 1
fi

CHECK="$ROOT/scripts/check_daily_research_digest_due.sh"
RUN="$ROOT/scripts/run_daily_research_digest.sh"

if [[ ! -x "$CHECK" ]]; then
  echo "CRITICAL daily-digest: check script missing at $CHECK"
  exit 1
fi

if "$CHECK" >/dev/null 2>&1; then
  echo "⚠️ DEGRADED — Daily research digest not run for $(date +%Y-%m-%d)."
  echo "Run on laptop: bash $RUN"
  echo "Meta: $ROOT/wiki/meta/daily-research-digest-cadence.md"
fi
