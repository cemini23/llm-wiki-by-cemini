#!/usr/bin/env bash
# Run Playground S2 lobby alongside Tournament S1 (separate comp + state file).
# Arena allows one table per competition; same agent, two systemd services.
#
# Usage: ./scripts/enable_s2_parallel_lobby.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
S2_COMP="${S2_PLAYGROUND_COMP:-cmq57o53r0bhw18g23qkydb08}"

echo "==> Deploy lobby logging + S2 parallel service to ${HOST}"

scp "${AGENT_DIR}/examples/arena_client.py" \
    "${AGENT_DIR}/examples/run_cemini_lobby.py" \
    "${AGENT_DIR}/examples/playground_timeseries.py" \
    "${HOST}:${REMOTE_DIR}/examples/"
scp "${AGENT_DIR}/deploy/cemini-devfun-poker-lobby-s2.service" \
    "${HOST}:${REMOTE_DIR}/deploy/"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
S2_COMP="${S2_COMP}"

cp -f deploy/cemini-devfun-poker-lobby-s2.service /etc/systemd/system/
sed -i "s|--competition-id .*|--competition-id ${S2_COMP}|" \
  /etc/systemd/system/cemini-devfun-poker-lobby-s2.service

# Tournament primary lobby tags (main service reads .env ARENA_LOBBY=tournament)
grep -q '^CEMINI_LOBBY_LABEL=' .env 2>/dev/null || echo 'CEMINI_LOBBY_LABEL=Tournament S1' >> .env
grep -q '^CEMINI_LOBBY_ROLE=' .env 2>/dev/null || echo 'CEMINI_LOBBY_ROLE=s1_tournament' >> .env
grep -q '^S2_PLAYGROUND_COMP=' .env 2>/dev/null || echo "S2_PLAYGROUND_COMP=${S2_COMP}" >> .env

systemctl daemon-reload
systemctl enable cemini-devfun-poker-lobby-s2.service
systemctl restart cemini-devfun-poker-lobby.service
systemctl start cemini-devfun-poker-lobby-s2.service
sleep 2
systemctl --no-pager status cemini-devfun-poker-lobby.service | head -5
systemctl --no-pager status cemini-devfun-poker-lobby-s2.service | head -5
REMOTE

echo ""
echo "✓ Tournament S1: cemini-devfun-poker-lobby.service"
echo "✓ Playground S2:  cemini-devfun-poker-lobby-s2.service"
echo "  Logs: journalctl -u cemini-devfun-poker-lobby-s2.service -f"
