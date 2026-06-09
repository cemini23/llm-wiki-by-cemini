#!/usr/bin/env bash
# Multi-comp oracle — S1 tournament (primary) + S2 playground (intel).
# Appends multi_comp_timeseries.jsonl; exports hands only for primary.
#
# Usage:
#   ./scripts/run_multi_comp_snapshot.sh
#   ./scripts/run_multi_comp_snapshot.sh --export
#   CEMINI_PROD_HOST=cemini-prod ./scripts/run_multi_comp_snapshot.sh --on-prod
set -euo pipefail
cd "$(dirname "$0")/.."

EXPORT=0
ON_PROD=0
for arg in "$@"; do
  case "$arg" in
    --export) EXPORT=1 ;;
    --on-prod) ON_PROD=1 ;;
  esac
done

run_local() {
  local extra=()
  if [[ "${EXPORT}" -eq 1 ]]; then
    extra+=(--export)
  fi
  uv run python examples/multi_comp_registry.py discover || true
  uv run python examples/multi_comp_registry.py snapshot "${extra[@]}"
}

if [[ "${ON_PROD}" -eq 1 ]]; then
  HOST="${CEMINI_PROD_HOST:-cemini-prod}"
  REMOTE="/opt/devfun-poker-arena"
  ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE}"
EXTRA=""
if [[ "${EXPORT}" -eq 1 ]]; then EXTRA="--export"; fi
./venv/bin/python examples/multi_comp_registry.py discover || true
./venv/bin/python examples/multi_comp_registry.py snapshot \${EXTRA}
REMOTE
  echo "==> Pull oracle to laptop"
  scp -q "${HOST}:${REMOTE}/reports/hl-loop/multi_comp_timeseries.jsonl" \
    reports/hl-loop/multi_comp_timeseries.jsonl 2>/dev/null || true
  scp -q "${HOST}:${REMOTE}/reports/hl-loop/multi_comp_config.json" \
    reports/hl-loop/multi_comp_config.json 2>/dev/null || true
else
  run_local
fi

echo "==> Oracle: reports/hl-loop/multi_comp_timeseries.jsonl"
