#!/usr/bin/env bash
# run_gov_asset_monitors.sh — run all gov-asset-rerate lanes in sequence.
#   Lane 1: SEC EDGAR full-text (coincident 8-K)
#   Lane 2: USASpending procurement (earliest pre-diligence)
#   Lane 3: Federal Register DoD/DOE catalysts (days–weeks)
#   Lane 4: Target Hospitality hiring (Tier-A jobs; UltiPro)
#
# Usage: bash scripts/run_gov_asset_monitors.sh [--notify]
# A lane failing (e.g. transient network) does not abort the others.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}:${PYTHONPATH:-}"
export CEMINI_THESIS_ID="${CEMINI_THESIS_ID:-gov-asset-rerate}"

ARGS=("$@")

rc=0
for entry in \
  "scripts/intel/monitors/edgar_fulltext.py" \
  "scripts/intel/monitors/procurement.py" \
  "scripts/intel/monitors/fedreg.py" \
  "scripts/intel/monitors/th_jobs.py"; do
  echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) running ${entry} ==="
  if ((${#ARGS[@]})); then
    python3 "$entry" --thesis gov-asset-rerate "${ARGS[@]}" || { echo "WARN: ${entry} exited $?"; rc=1; }
  else
    python3 "$entry" --thesis gov-asset-rerate || { echo "WARN: ${entry} exited $?"; rc=1; }
  fi
done

exit "$rc"
