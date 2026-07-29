#!/usr/bin/env bash
# Enter Playground S9 — 6-max chip qual (top 20 → Tournament S9 free entry).
# Canon: briefs/2026-06-03_playground-top20-qualification.md + S1a/S2 playground audits.
# NOT ladder HU / Eval crush / gin width.
#
# Usage:
#   ./scripts/s9_playground_enter.sh
#   ./scripts/s9_playground_enter.sh cmrt1wzu40jm911suskj9qebe playground-s9-live
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-cmrt1wzu40jm911suskj9qebe}"
EXPORT_SLUG="${2:-playground-s9-live}"

echo "==> S9 enter: ${COMP} export=${EXPORT_SLUG} on ${HOST}"

if [[ -x "${AGENT_DIR}/scripts/playground_rollover_preflight.sh" ]]; then
  "${AGENT_DIR}/scripts/playground_rollover_preflight.sh" "${COMP}" "${EXPORT_SLUG}" || true
fi

# Rsync code so posture wiring + apply_env land before restart
bash "${AGENT_DIR}/scripts/rsync_poker_arena_code.sh"

ssh -q "${HOST}" bash -s -- "${COMP}" "${EXPORT_SLUG}" "${REMOTE_DIR}" <<'REMOTE'
set -euo pipefail
COMP="$1"
EXPORT_SLUG="$2"
REMOTE_DIR="$3"
cd "${REMOTE_DIR}"

./venv/bin/python examples/arena_kill_switch.py clear --reason "Playground S9 enter" 2>/dev/null || true

./venv/bin/python scripts/s9_playground_apply_env.py \
  --comp "${COMP}" \
  --export "${EXPORT_SLUG}" \
  --env-path .env

mkdir -p "reports/exports/${EXPORT_SLUG}"
systemctl restart cemini-devfun-poker-lobby.service
sleep 3
systemctl is-active cemini-devfun-poker-lobby.service
journalctl -u cemini-devfun-poker-lobby.service -n 30 --no-pager
REMOTE

echo "Done. Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
echo "Tail: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
