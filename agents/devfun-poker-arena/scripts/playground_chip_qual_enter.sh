#!/usr/bin/env bash
# Enter Playground chip-qual season (top 20 → paired Tournament free entry).
# Canon: briefs/2026-06-03_playground-top20-qualification.md + S1a/S2 audits.
# NOT ladder HU / Eval crush / gin width.
#
# Usage:
#   ./scripts/playground_chip_qual_enter.sh              # S10 default
#   ./scripts/playground_chip_qual_enter.sh 10
#   ./scripts/playground_chip_qual_enter.sh 10 cms0bwufmf3n8kyykdpxi6d2i playground-s10-live
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
SEASON="${1:-10}"
case "${SEASON}" in
  9) DEFAULT_COMP="cmrt1wzu40jm911suskj9qebe" ;;
  10) DEFAULT_COMP="cms0bwufmf3n8kyykdpxi6d2i" ;;
  11) DEFAULT_COMP="cms7hrnjg20czv7oi85cho570" ;;
  *) DEFAULT_COMP="" ;;
esac
COMP="${2:-${DEFAULT_COMP}}"
EXPORT_SLUG="${3:-playground-s${SEASON}-live}"

if [[ -z "${COMP}" ]]; then
  echo "Need competition id for season ${SEASON}" >&2
  exit 1
fi

echo "==> Playground S${SEASON} enter: ${COMP} export=${EXPORT_SLUG} on ${HOST}"

if [[ -x "${AGENT_DIR}/scripts/playground_rollover_preflight.sh" ]]; then
  "${AGENT_DIR}/scripts/playground_rollover_preflight.sh" "${COMP}" "${EXPORT_SLUG}" || true
fi

bash "${AGENT_DIR}/scripts/rsync_poker_arena_code.sh"

ssh -q "${HOST}" bash -s -- "${SEASON}" "${COMP}" "${EXPORT_SLUG}" "${REMOTE_DIR}" <<'REMOTE'
set -euo pipefail
SEASON="$1"
COMP="$2"
EXPORT_SLUG="$3"
REMOTE_DIR="$4"
cd "${REMOTE_DIR}"

./venv/bin/python examples/arena_kill_switch.py clear --reason "Playground S${SEASON} enter" 2>/dev/null || true

./venv/bin/python scripts/playground_chip_qual_apply_env.py \
  --season "${SEASON}" \
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
