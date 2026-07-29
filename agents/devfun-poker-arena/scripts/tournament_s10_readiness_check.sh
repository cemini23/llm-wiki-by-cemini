#!/usr/bin/env bash
# Pre-flight readiness for Tournament S10 — does NOT swap lobby.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
PG="${S10_PLAYGROUND_COMP:-cms0bwufmf3n8kyykdpxi6d2i}"

echo "==> Tournament S10 readiness (no lobby swap)"
fail=0

need() {
  local p="$1"
  if [[ -x "${AGENT_DIR}/${p}" || -f "${AGENT_DIR}/${p}" ]]; then
    echo "  OK  ${p}"
  else
    echo "  MISSING ${p}"; fail=1
  fi
}

need scripts/s10_tournament_prod_apply.sh
need scripts/wait_tournament_s10_and_apply.sh
need briefs/2026-07-28_tournament-s10-go-live.md
need reports/hl-loop/tournament_s10_candidate.json

echo "==> Prod lobby must still be Playground S10"
ssh -q "${HOST}" "cd ${REMOTE_DIR} && grep -E '^(ARENA_LOBBY_COMPETITION_ID|CEMINI_LOBBY_ROLE|CEMINI_TOURNAMENT_MODE)=' .env && systemctl is-active cemini-devfun-poker-lobby.service" \
  | tee /tmp/s10-ready-env.txt
if ! grep -q "ARENA_LOBBY_COMPETITION_ID=${PG}" /tmp/s10-ready-env.txt; then
  echo "  WARN: lobby not on Playground S10 ${PG}"
  fail=1
fi
if ! grep -q "CEMINI_LOBBY_ROLE=s10_playground" /tmp/s10-ready-env.txt; then  # pragma: allowlist secret
  echo "  WARN: role not s10_playground"
  fail=1
fi
if grep -q "CEMINI_TOURNAMENT_MODE=1" /tmp/s10-ready-env.txt; then
  echo "  WARN: tournament mode already ON — unexpected before T10"
  fail=1
fi

echo "==> Qual status"
"${AGENT_DIR}/scripts/cemini_playground_status.sh" --competition "${PG}" 2>&1 | tail -18

echo "==> Is Tournament S10 listed yet?"
bash "${AGENT_DIR}/scripts/list_arena_competitions.sh" 2>&1 | grep -i 'Tournament S10' || echo "  (not listed — expected until season rollover)"

if [[ "${fail}" -ne 0 ]]; then
  echo "==> READY CHECK: FAIL"
  exit 1
fi
echo "==> READY CHECK: PASS — stay on Playground; run wait script when you want auto-swap at T10 open"
echo "    ./scripts/wait_tournament_s10_and_apply.sh"
