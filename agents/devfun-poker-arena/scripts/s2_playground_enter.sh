#!/usr/bin/env bash
# Enter Playground S2 — rollover preflight, clear kill switch, enable S1b exploit lane.
#
# Usage:
#   ./scripts/s2_playground_enter.sh cmq57o53r0bhw18g23qkydb08
#   PLAYGROUND_ROLLOVER_RESTART=1 ./scripts/s2_playground_enter.sh <comp_id>
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-cmq57o53r0bhw18g23qkydb08}"
EXPORT_SLUG="${2:-playground-s2-live}"

echo "==> S2 enter: ${COMP} export=${EXPORT_SLUG} on ${HOST}"

"${AGENT_DIR}/scripts/playground_rollover_preflight.sh" "${COMP}" "${EXPORT_SLUG}"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"

echo "==> Clear kill switch (S1/eval false alarms)"
./venv/bin/python examples/arena_kill_switch.py clear --reason "S2 playground enter"

grep -q '^CEMINI_S1B_EXPLOIT=' .env 2>/dev/null || echo 'CEMINI_S1B_EXPLOIT=1' >> .env
grep -q '^CEMINI_S1B_MIN_STACK_BB=' .env 2>/dev/null || echo 'CEMINI_S1B_MIN_STACK_BB=60' >> .env
sed -i.bak 's/^CEMINI_S1B_EXPLOIT=.*/CEMINI_S1B_EXPLOIT=1/' .env
if grep -q '^CEMINI_NEMESIS_HANDLES=' .env; then
  sed -i.bak 's/^CEMINI_NEMESIS_HANDLES=.*/CEMINI_NEMESIS_HANDLES=hunterguy102,thaddius,v_16,0xJeff_ai/' .env
else
  echo 'CEMINI_NEMESIS_HANDLES=hunterguy102,thaddius,v_16,0xJeff_ai' >> .env
fi
grep -q '^CEMINI_NEMESIS_EXPLOIT=' .env 2>/dev/null || echo 'CEMINI_NEMESIS_EXPLOIT=1' >> .env

grep -E '^(ARENA_LOBBY_COMPETITION_ID|CEMINI_S1B_EXPLOIT)=' .env

if [[ "\${PLAYGROUND_ROLLOVER_RESTART:-0}" == "1" ]]; then
  systemctl restart cemini-devfun-poker-lobby.service
  echo "==> Lobby restarted for S2"
fi
REMOTE

echo "Done. Tail: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
