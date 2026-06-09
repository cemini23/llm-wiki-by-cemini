#!/usr/bin/env bash
# Poll list-active until Tournament S1 appears, then run s1_tournament_prod_apply.sh.
#
# Usage:
#   ./scripts/wait_tournament_s1_and_apply.sh          # laptop → ssh prod discover loop
#   INTERVAL_S=30 MAX_MINUTES=60 ./scripts/wait_tournament_s1_and_apply.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
INTERVAL_S="${INTERVAL_S:-30}"
MAX_MINUTES="${MAX_MINUTES:-90}"
DEADLINE=$((SECONDS + MAX_MINUTES * 60))

echo "==> Waiting for Tournament S1 in list-active (every ${INTERVAL_S}s, max ${MAX_MINUTES}m)"

while (( SECONDS < DEADLINE )); do
  out="$(ssh -q "${HOST}" "cd ${REMOTE_DIR} && ./venv/bin/python examples/multi_comp_registry.py discover 2>&1" || true)"
  echo "[$(date -u +%H:%M:%SZ)] ${out}"
  cid="$(echo "${out}" | sed -n 's/^primary competition_id=//p' | head -1)"
  if [[ -n "${cid}" && "${cid}" != "NOT FOUND" ]]; then
    echo "==> Found ${cid} — applying tournament posture"
    TOURNAMENT_COMP="${cid}" "${SCRIPT_DIR}/s1_tournament_prod_apply.sh"
    exit 0
  fi
  sleep "${INTERVAL_S}"
done

echo "ERROR: Tournament S1 not found after ${MAX_MINUTES} minutes." >&2
echo "  Check arena.dev.fun UI / Discord; then:" >&2
echo "  TOURNAMENT_COMP=cmp... ${SCRIPT_DIR}/s1_tournament_prod_apply.sh" >&2
exit 1
