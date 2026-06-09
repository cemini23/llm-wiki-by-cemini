#!/usr/bin/env bash
# S2 parallel lobby — top-20 qual posture + royal jackpot (27o slots claimed).
# Tournament S1 stays on cemini-devfun-poker-lobby.service (separate comp + state).
#
# Usage: ./scripts/s2_parallel_qual_posture.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
S2_COMP="${S2_PLAYGROUND_COMP:-cmq57o53r0bhw18g23qkydb08}"

echo "==> S2 qual posture (top 20 → Tournament S2) on parallel lobby"

scp "${AGENT_DIR}/examples/qualification_guard.py" "${HOST}:${REMOTE_DIR}/examples/"
scp "${AGENT_DIR}/deploy/cemini-devfun-poker-lobby-s2.service" "${HOST}:${REMOTE_DIR}/deploy/"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
S2_COMP="${S2_COMP}"

cp -f deploy/cemini-devfun-poker-lobby-s2.service /etc/systemd/system/
sed -i "s|--competition-id .*|--competition-id ${S2_COMP}|" \
  /etc/systemd/system/cemini-devfun-poker-lobby-s2.service

systemctl daemon-reload
systemctl enable cemini-devfun-poker-lobby-s2.service
# S2 only — do not restart tournament lobby
systemctl restart cemini-devfun-poker-lobby-s2.service
sleep 2

export PYTHONPATH=examples
./venv/bin/python - <<PY
import os, json, sys
sys.path.insert(0, "examples")
from dotenv import load_dotenv
load_dotenv(".env")
from arena_client import ArenaClient, DEFAULT_BASE
from qualification_guard import cutoff_rank_threshold
key = json.load(open(".arena-credentials")).get("apiKey")
c = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=key)
comp = "${S2_COMP}"
from qualification_guard import fetch_qualification_status
st = fetch_qualification_status(c, comp)
me = next((x for x in (c.get("/agent/me").get("leaderboard") or []) if x.get("arenaId") == comp), {})
lb = c.get(f"/competition/leaderboard?competitionId={comp}&limit=1&offset={cutoff_rank_threshold()-1}")
floor = (lb.get("data") or [None])[0]
print(f"cutoff_rank={cutoff_rank_threshold()} field={lb.get('total')}")
if floor:
    print(f"rank{floor.get('rank')} floor={floor.get('totalScore')} chips")
print(f"us rank={me.get('rank')} chips={me.get('totalScore')}")
c.close()
PY

systemctl --no-pager status cemini-devfun-poker-lobby-s2.service | head -6
REMOTE

echo ""
echo "✓ S2: royal ON, 27 hunt OFF, volume push join=12s queue=25s low_stack=15s"
echo "  Status: ./scripts/cemini_playground_status.sh --competition ${S2_COMP}"
