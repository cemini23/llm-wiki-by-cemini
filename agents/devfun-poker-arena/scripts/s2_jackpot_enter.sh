#!/usr/bin/env bash
# Enable S2 27o jackpot hunt on the claimed qual bot (cemini_wiki_poker).
# No separate probe agent — hunt runs inside cemini_decide.py.
#
# Usage:
#   ./scripts/s2_jackpot_enter.sh
#   ./scripts/s2_jackpot_enter.sh cmq57o53r0bhw18g23qkydb08
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-cmq57o53r0bhw18g23qkydb08}"

echo "==> S2 jackpot on main bot: comp=${COMP}"
"${AGENT_DIR}/scripts/jackpot_27_preflight.sh"
"${AGENT_DIR}/deploy/deploy_to_cemini_prod.sh"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"

# Never run a parallel probe lobby alongside qual bot.
systemctl stop jackpot-27-lobby.service 2>/dev/null || true
systemctl disable jackpot-27-lobby.service 2>/dev/null || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

set_kv JACKPOT_27_HUNT_ENABLED 1
set_kv JACKPOT_27_MAX_ATTEMPTS 5
set_kv JACKPOT_27_COMPETITION_ID "${COMP}"
set_kv JACKPOT_27_COMPETITION_ONLY 1
set_kv JACKPOT_27_INSTANCE cemini_wiki_poker

grep -E '^(JACKPOT_27_|ARENA_LOBBY_COMPETITION_ID)=' .env

systemctl restart cemini-devfun-poker-lobby.service
sleep 2
systemctl --no-pager status cemini-devfun-poker-lobby.service || true
REMOTE

echo ""
echo "✓ 27o hunt enabled on cemini_wiki_poker (no probe service)."
echo "  ssh ${HOST} journalctl -u cemini-devfun-poker-lobby.service -f"
echo "  ssh ${HOST} tail -f ${REMOTE_DIR}/reports/jackpot-27/cemini_wiki_poker/dealt.jsonl"
