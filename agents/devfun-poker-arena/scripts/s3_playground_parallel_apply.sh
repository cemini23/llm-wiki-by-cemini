#!/usr/bin/env bash
# Playground S3 — parallel lobby (top 20 → free Tournament S3 entry).
# Main lobby stays on Tournament S2 wait (cemini-devfun-poker-lobby.service).
#
# Usage:
#   ./scripts/s3_playground_parallel_apply.sh
#   ./scripts/s3_playground_parallel_apply.sh cmqf827h30u7dfca3x2aqvzjv
#
# Gates (local):
#   uv run pytest tests/test_cemini_regression.py tests/test_s2_audit_patches.py -q
#   uv run python examples/gin_style_gate.py
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
COMP="${1:-${S3_PLAYGROUND_COMP:-cmqf827h30u7dfca3x2aqvzjv}}"
EXPORT_SLUG="${S3_EXPORT_SLUG:-s3-playground-live}"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
AGENT_VERSION="${AGENT_VERSION:-s3p.${GIT_SHA}.playground-s3}"

echo "==> Playground S3 parallel: comp=${COMP} export=${EXPORT_SLUG} version=${AGENT_VERSION}"

rsync -avz \
  --exclude '.venv/' --exclude 'venv/' --exclude '.git/' \
  --exclude '__pycache__/' --exclude '.env' --exclude '.env.*' \
  --exclude '.arena-credentials' --exclude '.arena-poker-state*' \
  --exclude '.arena-credentials.jackpot*' --exclude 'reports/' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
COMP="${COMP}"
EXPORT_SLUG="${EXPORT_SLUG}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/\${EXPORT_SLUG}"
AGENT_VERSION="${AGENT_VERSION}"

echo "==> Clear kill switch (S3 qual)"
./venv/bin/python examples/arena_kill_switch.py clear --reason "Playground S3 enter" || true

set_kv() {
  local key="\$1" val="\$2"
  if grep -q "^\${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^\${key}=.*|\${key}=\${val}|" .env
  else
    echo "\${key}=\${val}" >> .env
  fi
}

set_kv S3_PLAYGROUND_COMP "\${COMP}"
set_kv AGENT_VERSION "\${AGENT_VERSION}"
if systemctl is-enabled cemini-devfun-poker-lobby-s2.service 2>/dev/null | grep -q enabled; then
  systemctl stop cemini-devfun-poker-lobby-s2.service 2>/dev/null || true
  systemctl disable cemini-devfun-poker-lobby-s2.service 2>/dev/null || true
fi

cp -f deploy/cemini-devfun-poker-lobby-s3.service /etc/systemd/system/
sed -i "s|--competition-id .*|--competition-id \${COMP}|" \
  /etc/systemd/system/cemini-devfun-poker-lobby-s3.service

mkdir -p "\${EXPORT_DIR}"
if [[ ! -f "\${EXPORT_DIR}/crawl_state.json" ]]; then
  echo '{"completed_agent_ids":[],"cycles":0,"leaderboard_total":0}' > "\${EXPORT_DIR}/crawl_state.json"
fi

if [[ -f /etc/systemd/system/cemini-devfun-poker-export-crawl.service ]]; then
  sed -i "s|Environment=CEMINI_EXPORT_DIR=.*|Environment=CEMINI_EXPORT_DIR=\${EXPORT_DIR}|" \
    /etc/systemd/system/cemini-devfun-poker-export-crawl.service 2>/dev/null || true
fi

systemctl daemon-reload
systemctl enable cemini-devfun-poker-lobby-s3.service
systemctl restart cemini-devfun-poker-lobby-s3.service
systemctl enable cemini-devfun-poker-export-crawl.timer 2>/dev/null || true
systemctl start cemini-devfun-poker-export-crawl.service 2>/dev/null || true

# Tournament money > playground qual — pause S3 when S2 tournament goes Active
if [[ -f deploy/cemini-tournament-priority.service ]]; then
  cp -f deploy/cemini-tournament-priority.service deploy/cemini-tournament-priority.timer \
    /etc/systemd/system/
  systemctl daemon-reload
  systemctl enable cemini-tournament-priority.timer
  systemctl start cemini-tournament-priority.timer
  CEMINI_TOURNAMENT_PRIORITY_LOCAL=1 ./scripts/tournament_priority_guard.sh || true
fi

sleep 3

echo "==> Main lobby (Tournament S2 wait):"
systemctl is-active cemini-devfun-poker-lobby.service
echo "==> Parallel S3 playground:"
systemctl is-active cemini-devfun-poker-lobby-s3.service

./venv/bin/python - <<PY
import os, json, sys
sys.path.insert(0, "examples")
from dotenv import load_dotenv
load_dotenv(".env")
from arena_client import ArenaClient, DEFAULT_BASE
from qualification_guard import cutoff_rank_threshold, fetch_qualification_status
key = json.load(open(".arena-credentials")).get("apiKey")
c = ArenaClient(os.environ.get("ARENA_API_BASE", DEFAULT_BASE), api_key=key)
comp = "${COMP}"
st = fetch_qualification_status(c, comp)
lb = c.get(f"/competition/leaderboard?competitionId={comp}&limit=1&offset={cutoff_rank_threshold()-1}")
floor = (lb.get("data") or [None])[0]
me = next((x for x in (c.get("/agent/me").get("leaderboard") or []) if x.get("arenaId") == comp), {})
print(f"S3 cutoff_rank={cutoff_rank_threshold()} field={lb.get('total')}")
if floor:
    print(f"  rank{floor.get('rank')} floor={floor.get('totalScore')} chips")
print(f"  us rank={me.get('rank')} chips={me.get('totalScore')}")
c.close()
PY
REMOTE

echo ""
echo "✓ Tournament S2: cemini-devfun-poker-lobby.service (poll until Active)"
echo "✓ Playground S3:  cemini-devfun-poker-lobby-s3.service"
echo "  Logs: ssh ${HOST} journalctl -u cemini-devfun-poker-lobby-s3.service -f"
echo "  Status: ./scripts/cemini_playground_status.sh --competition ${COMP}"
