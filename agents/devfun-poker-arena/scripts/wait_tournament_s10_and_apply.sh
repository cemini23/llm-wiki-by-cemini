#!/usr/bin/env bash
# Poll until Tournament S10 is Active, then apply KO posture (CONFIRM baked in).
#
# Usage:
#   ./scripts/wait_tournament_s10_and_apply.sh
#   INTERVAL_S=60 MAX_MINUTES=720 ./scripts/wait_tournament_s10_and_apply.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
INTERVAL_S="${INTERVAL_S:-60}"
MAX_MINUTES="${MAX_MINUTES:-720}"
DEADLINE=$((SECONDS + MAX_MINUTES * 60))

echo "==> Waiting for Tournament S10 (season 10) — apply when Active"
echo "    interval=${INTERVAL_S}s max=${MAX_MINUTES}m host=${HOST}"

while (( SECONDS < DEADLINE )); do
  out="$(ssh -q "${HOST}" "cd ${REMOTE_DIR} && ./venv/bin/python - <<'PY'
import json, os, sys
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path('.env'))
sys.path.insert(0, 'examples')
from arena_client import ArenaClient, DEFAULT_BASE, load_or_register
c = ArenaClient(os.environ.get('ARENA_API_BASE', DEFAULT_BASE))
load_or_register(c, 'cemini_wiki_poker', 'c', 'q')
body = c.get('/competition/list-active')
items = body if isinstance(body, list) else body.get('data') or body.get('competitions') or []
for x in items:
    name = (x.get('name') or '')
    if 'Tournament' in name and int(x.get('seasonNumber') or 0) == 10:
        print(x.get('id'), x.get('status') or 'Active', name)
        break
else:
    # also scan list-all for Upcoming
    try:
        body = c.get('/competition/list-all')
        items = body.get('data') or []
    except Exception:
        items = []
    for x in items:
        name = (x.get('name') or '')
        if 'Tournament' in name and int(x.get('seasonNumber') or 0) == 10:
            print(x.get('id'), x.get('status') or '', name)
            break
    else:
        print('NONE')
PY" 2>/dev/null || echo "NONE")"
  echo "[$(date -u +%H:%M:%SZ)] ${out}"
  cid="$(echo "${out}" | awk '{print $1}')"
  status="$(echo "${out}" | awk '{print $2}')"
  if [[ "${cid}" != "NONE" && -n "${cid}" && "${status}" == "Active" ]]; then
    echo "==> Tournament S10 ${cid} Active — applying (CONFIRM=1)"
    CONFIRM=1 TOURNAMENT_COMP="${cid}" "${SCRIPT_DIR}/s10_tournament_prod_apply.sh" "${cid}"
    exit 0
  fi
  if [[ "${cid}" != "NONE" && -n "${cid}" && "${status}" == "Upcoming" && "${APPLY_ON_UPCOMING:-0}" == "1" ]]; then
    echo "==> Tournament S10 ${cid} Upcoming + APPLY_ON_UPCOMING=1 — applying"
    CONFIRM=1 TOURNAMENT_COMP="${cid}" "${SCRIPT_DIR}/s10_tournament_prod_apply.sh" "${cid}"
    exit 0
  fi
  sleep "${INTERVAL_S}"
done

echo "ERROR: Tournament S10 not Active after ${MAX_MINUTES} minutes." >&2
echo "  Manual when live: CONFIRM=1 ./scripts/s10_tournament_prod_apply.sh <comp-id>" >&2
exit 1
