#!/usr/bin/env bash
# Pull prod HL artifacts to laptop for version/performance tracking.
#
# Usage:
#   ./scripts/sync_hl_artifacts.sh
#   CEMINI_PROD_HOST=cemini-prod ./scripts/sync_hl_artifacts.sh
set -euo pipefail

cd "$(dirname "$0")/.."
AGENT_DIR="$(pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
LOCAL="${AGENT_DIR}/reports/hl-loop"

mkdir -p "${LOCAL}"

PULL_STATE=0
for arg in "$@"; do
  case "$arg" in
    --pull-state) PULL_STATE=1 ;;
  esac
done

FILES=(
  deploy_grace.json
  deploys.jsonl
  eval_timeseries.jsonl
  playground_timeseries.jsonl
  tournament_candidate.json
  tournament_candidates.jsonl
  preflight_metrics.json
  preflight_ok.timestamp
)

echo "==> Sync HL artifacts from ${HOST}:${REMOTE_DIR}/reports/hl-loop/"
if [[ "${PULL_STATE}" -eq 1 ]]; then
  FILES=(state.json "${FILES[@]}")
else
  echo "  (skip state.json — laptop is canonical; use --pull-state to overwrite)"
fi
for f in "${FILES[@]}"; do
  if scp -q "${HOST}:${REMOTE_DIR}/reports/hl-loop/${f}" "${LOCAL}/${f}" 2>/dev/null; then
    echo "  ✓ ${f}"
  else
    echo "  · ${f} (missing on prod)"
  fi
done

echo ""
echo "==> Sync analyze history (last 200 lines)"
mkdir -p "${AGENT_DIR}/reports/analyze"
ssh -q "${HOST}" "tail -200 ${REMOTE_DIR}/reports/analyze/history.jsonl 2>/dev/null || true" \
  > "${AGENT_DIR}/reports/analyze/history.jsonl" || true

echo ""
echo "Done. Pick candidate:"
echo "  uv run python scripts/pick_deploy_for_tournament.py"
