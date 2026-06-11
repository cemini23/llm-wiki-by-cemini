#!/usr/bin/env bash
# Single harvest worker: crawl batch + top-N export append (one IP / shard).
#
# Env (required on remote):
#   CEMINI_EXPORT_SHARD_INDEX   0=prod, 1=librarian, 2=egress
#   CEMINI_EXPORT_SHARD_COUNT   3
#   S1_TOURNAMENT_COMP, ARENA_API_KEY, ARENA_API_BASE
#
# Usage:
#   bash scripts/run_export_harvest_worker.sh
#   CEMINI_EXPORT_SHARD_INDEX=1 bash scripts/run_export_harvest_worker.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

SHARD_INDEX="${CEMINI_EXPORT_SHARD_INDEX:-0}"
SHARD_COUNT="${CEMINI_EXPORT_SHARD_COUNT:-1}"
EXPORT_DIR="${CEMINI_EXPORT_DIR:-reports/exports/s1-tournament-live}"
COMP="${S1_TOURNAMENT_COMP:-${ARENA_LOBBY_COMPETITION_ID:-}}"
TOP="${CEMINI_EXPORT_TOP_AGENTS:-200}"
STATS="${CEMINI_EXPORT_STATS_TOP:-200}"
REPLAYS="${CEMINI_EXPORT_REPLAYS_TOP:-50}"
CRAWL_BATCH="${CEMINI_EXPORT_CRAWL_BATCH:-120}"

PY="${AGENT_DIR}/venv/bin/python"
if [[ ! -x "${PY}" ]]; then
  PY="$(command -v python3)"
fi

if [[ -z "${COMP}" ]]; then
  echo "ERROR: set S1_TOURNAMENT_COMP or ARENA_LOBBY_COMPETITION_ID" >&2
  exit 2
fi

echo "==> harvest worker shard ${SHARD_INDEX}/${SHARD_COUNT} → ${EXPORT_DIR}"

"${PY}" examples/export_field_crawl.py \
  --out-dir "${EXPORT_DIR}" \
  --match "${COMP}" \
  --batch-size "${CRAWL_BATCH}" \
  --sleep 0.04 \
  --no-tables \
  --shard-index "${SHARD_INDEX}" \
  --shard-count "${SHARD_COUNT}"

"${PY}" examples/export_competition_hands.py \
  --append \
  --match "${COMP}" \
  --top-agents "${TOP}" \
  --stats-top "${STATS}" \
  --replays-top-agents "${REPLAYS}" \
  --out-dir "${EXPORT_DIR}" \
  --shard-index "${SHARD_INDEX}" \
  --shard-count "${SHARD_COUNT}"

echo "==> worker shard ${SHARD_INDEX} done"
