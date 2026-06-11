#!/usr/bin/env bash
# Orchestrate 3-IP harvest: prod (shard 0) + librarian (1) + egress (2), merge on prod.
#
# Usage:
#   bash scripts/export_harvest_fleet_deploy.sh   # once
#   bash scripts/run_export_harvest_fleet.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

PROD_HOST="${CEMINI_PROD_HOST:-cemini-prod}"
LIB_HOST="${CEMINI_LIBRARIAN_HOST:-cemini-librarian}"
EGR_HOST="${CEMINI_EGRESS_HOST:-cemini-egress-fi}"
PROD_DIR="${CEMINI_PROD_HARVEST_DIR:-/opt/devfun-poker-arena}"
LIB_DIR="${CEMINI_LIBRARIAN_HARVEST_DIR:-/opt/devfun-poker-arena-harvest}"
EGR_DIR="${CEMINI_EGRESS_HARVEST_DIR:-/opt/devfun-poker-arena-harvest}"
EXPORT_SLUG="${CEMINI_EXPORT_SLUG:-s1-tournament-live}"

run_shard() {
  local host="$1" dir="$2" idx="$3"
  echo "==> [shard ${idx}] ${host}"
  ssh "${host}" "cd ${dir} && \
    CEMINI_EXPORT_SHARD_INDEX=${idx} CEMINI_EXPORT_SHARD_COUNT=3 \
    bash scripts/run_export_harvest_worker.sh"
}

echo "==> Fleet harvest (3 IPs) competition export: ${EXPORT_SLUG}"

run_shard "${PROD_HOST}" "${PROD_DIR}" 0 &
PID0=$!
run_shard "${LIB_HOST}" "${LIB_DIR}" 1 &
PID1=$!
run_shard "${EGR_HOST}" "${EGR_DIR}" 2 &
PID2=$!

wait "${PID0}" || echo "WARN: prod shard 0 failed" >&2
wait "${PID1}" || echo "WARN: librarian shard 1 failed" >&2
wait "${PID2}" || echo "WARN: egress shard 2 failed" >&2

echo "==> Push shard 1/2 JSONL to prod incoming"
ssh "${PROD_HOST}" "mkdir -p ${PROD_DIR}/reports/exports/${EXPORT_SLUG}-incoming/shard1 \
  ${PROD_DIR}/reports/exports/${EXPORT_SLUG}-incoming/shard2"
rsync -avz --delete \
  "${LIB_HOST}:${LIB_DIR}/reports/exports/${EXPORT_SLUG}/" \
  "${PROD_HOST}:${PROD_DIR}/reports/exports/${EXPORT_SLUG}-incoming/shard1/"
rsync -avz --delete \
  "${EGR_HOST}:${EGR_DIR}/reports/exports/${EXPORT_SLUG}/" \
  "${PROD_HOST}:${PROD_DIR}/reports/exports/${EXPORT_SLUG}-incoming/shard2/"

echo "==> Merge shards into canonical on prod"
ssh "${PROD_HOST}" "cd ${PROD_DIR} && ./venv/bin/python scripts/merge_export_harvest.py \
  --canonical reports/exports/${EXPORT_SLUG} \
  --worker reports/exports/${EXPORT_SLUG}-incoming/shard1 \
  --worker reports/exports/${EXPORT_SLUG}-incoming/shard2"

echo "✓ Fleet harvest complete (canonical on ${PROD_HOST}:${PROD_DIR}/reports/exports/${EXPORT_SLUG})"
