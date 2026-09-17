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
  14) DEFAULT_COMP="cmsrglcro33ttvijti3slinjh" ;;
  15) DEFAULT_COMP="cmt03w83o3xzxtofxdqnupos8" ;;
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
if [[ ! -f "reports/exports/${EXPORT_SLUG}/crawl_state.json" ]]; then
  printf '%s\n' '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' \
    > "reports/exports/${EXPORT_SLUG}/crawl_state.json"
fi

# Retarget export units to .env MATCH/DIR (do not leave S1_TOURNAMENT_COMP winning).
if [[ -d deploy ]]; then
  cp -f deploy/cemini-devfun-poker-export-crawl.service /etc/systemd/system/ 2>/dev/null || true
  cp -f deploy/cemini-devfun-poker-export.service /etc/systemd/system/ 2>/dev/null || true
  cp -f deploy/cemini-devfun-poker-export-crawl.timer /etc/systemd/system/ 2>/dev/null || true
  cp -f deploy/cemini-devfun-poker-export.timer /etc/systemd/system/ 2>/dev/null || true
fi
systemctl daemon-reload
systemctl enable cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl enable cemini-devfun-poker-export.timer 2>/dev/null || true
# Do not block enter on long oneshot export/crawl — timers own the schedule.
systemctl start --no-block cemini-devfun-poker-export.service 2>/dev/null || true

systemctl restart cemini-devfun-poker-lobby.service
sleep 3
systemctl is-active cemini-devfun-poker-lobby.service
# Cap journal so SSH does not hang on pager
timeout 15 journalctl -u cemini-devfun-poker-lobby.service -n 30 --no-pager || true
echo "==> export match/dir:"
grep -E '^(CEMINI_EXPORT_MATCH|CEMINI_EXPORT_DIR|ARENA_LOBBY_COMPETITION_ID)=' .env || true
systemctl is-enabled cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl is-enabled cemini-devfun-poker-export.timer 2>/dev/null || true
REMOTE

echo "Done. Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
echo "Tail: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
echo "Export: ssh ${HOST} journalctl -u cemini-devfun-poker-export.service -n 40 --no-pager"
