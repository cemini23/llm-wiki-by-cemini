#!/usr/bin/env bash
# Poll until Tournament S2 is Active (or Upcoming with ID), then s2_tournament_prod_apply.sh.
#
# Usage:
#   ./scripts/wait_tournament_s2_and_apply.sh
#   INTERVAL_S=30 MAX_MINUTES=120 ./scripts/wait_tournament_s2_and_apply.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
INTERVAL_S="${INTERVAL_S:-30}"
MAX_MINUTES="${MAX_MINUTES:-120}"
DEADLINE=$((SECONDS + MAX_MINUTES * 60))
DEFAULT_COMP="${TOURNAMENT_COMP:-cmqggiv9k37am11ydmppz466e}"

echo "==> Waiting for Tournament S2 (season 2) — apply when Active (every ${INTERVAL_S}s, max ${MAX_MINUTES}m)"

while (( SECONDS < DEADLINE )); do
  out="$(ssh -q "${HOST}" "cd ${REMOTE_DIR} && ./venv/bin/python examples/multi_comp_registry.py discover --season 2 2>&1" || true)"
  echo "[$(date -u +%H:%M:%SZ)] ${out}"
  cid="$(echo "${out}" | sed -n 's/^primary competition_id=//p' | head -1 | awk '{print $1}')"
  if [[ -z "${cid}" || "${cid}" == "NOT" ]]; then
    cid="${DEFAULT_COMP}"
  fi
  status="$(ssh -q "${HOST}" "cd ${REMOTE_DIR} && ./venv/bin/python - <<'PY'
import os, json
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path('.env'))
import sys
sys.path.insert(0,'examples')
from arena_client import ArenaClient, DEFAULT_BASE, load_or_register
c = ArenaClient(os.environ.get('ARENA_API_BASE', DEFAULT_BASE))
load_or_register(c, 'cemini_wiki_poker', 'c', 'q')
body = c.get('/competition/list-all')
for x in body.get('data') or []:
    if x.get('id') == '${cid}':
        print(x.get('status') or '')
        break
PY" 2>/dev/null || echo "")"
  if [[ "${status}" == "Active" || "${status}" == "Upcoming" ]]; then
    echo "==> Tournament S2 ${cid} status=${status} — applying"
    TOURNAMENT_COMP="${cid}" "${SCRIPT_DIR}/s2_tournament_prod_apply.sh" "${cid}"
    exit 0
  fi
  sleep "${INTERVAL_S}"
done

echo "ERROR: Tournament S2 not ready after ${MAX_MINUTES} minutes." >&2
echo "  Manual: TOURNAMENT_COMP=${DEFAULT_COMP} ${SCRIPT_DIR}/s2_tournament_prod_apply.sh" >&2
exit 1
