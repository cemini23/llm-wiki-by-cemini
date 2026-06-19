#!/usr/bin/env bash
# Researcher Round prod prep — ship code + env; Researcher track PRIMARY over Playground.
#
# Playground S3 stays on main lobby as slow background intel until Researcher comp id
# is pinned (Jun 21+). Parallel S3 volume service is stopped.
#
# Run local gate first:
#   CEMINI_TABLE_FORMAT=hu bash scripts/run_hu_sandbox_gate.sh --hands 500
#
# Then:
#   ./scripts/researcher_prod_prep_apply.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
DEPLOY_DATE="$(date -u +%Y-%m-%d)"
AGENT_VERSION="${AGENT_VERSION:-researcher-hu.${GIT_SHA}.${DEPLOY_DATE}}"
PLAYGROUND_COMP="${S3_PLAYGROUND_COMP:-cmqf827h30u7dfca3x2aqvzjv}"

echo "==> Researcher PRIMARY deploy: version=${AGENT_VERSION} playground_intel=${PLAYGROUND_COMP}"

export ARENA_LOBBY_COMPETITION_ID="${PLAYGROUND_COMP}"
export CEMINI_SKIP_ENV=1
export CEMINI_SKIP_CREDS=1
"${AGENT_DIR}/deploy/deploy_to_cemini_prod.sh"

ssh -q "${HOST}" env PLAYGROUND_COMP="${PLAYGROUND_COMP}" AGENT_VERSION="${AGENT_VERSION}" REMOTE_DIR="${REMOTE_DIR}" bash -s <<'REMOTE'
set -euo pipefail
cd "${REMOTE_DIR}"
PLAYGROUND_COMP="${PLAYGROUND_COMP}"
AGENT_VERSION="${AGENT_VERSION}"

set_kv() {
  local key="$1" val="$2"
  if grep -q "^${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^${key}=.*|${key}=${val}|" .env
  else
    echo "${key}=${val}" >> .env
  fi
}

# Main lobby: Playground S3 slow intel until Researcher comp live
set_kv ARENA_LOBBY_COMPETITION_ID "${PLAYGROUND_COMP}"
set_kv S3_PLAYGROUND_COMP "${PLAYGROUND_COMP}"
set_kv AGENT_VERSION "${AGENT_VERSION}"
set_kv CEMINI_PRIMARY_TRACK researcher
set_kv CEMINI_LOBBY_LABEL "Researcher_HU_primary"
set_kv CEMINI_LOBBY_ROLE researcher_primary

# Researcher block — flip mode when comp id appears
set_kv ARENA_RESEARCHER_COMP_ID ""
set_kv CEMINI_RESEARCHER_MODE 0
set_kv CEMINI_PLACEMENT_CHASE 0
set_kv CEMINI_EVAL_PANEL_MODE 0
# Playground S3 is 6-max — use auto until Researcher HU comp pinned
set_kv CEMINI_TABLE_FORMAT auto
set_kv CEMINI_SANITIZE_OUTPUT 1
set_kv CEMINI_SESSION_MEMORY 1
set_kv CEMINI_EXPORT_TOP_AGENTS 50
set_kv CEMINI_MIX_POSTFLOP 1

# De-prioritize Playground rank chase / volume
set_kv CEMINI_FIRST_RANK 0
set_kv CEMINI_STAGGER_LOCKS 0
set_kv CEMINI_PLAYGROUND_TIMESERIES 0
set_kv CEMINI_FIELD_EXPORT_HUD 0
set_kv CEMINI_PACE_PHASE intel
set_kv CEMINI_JOIN_RETRY_S 3600
set_kv CEMINI_IN_QUEUE_RETRY_S 600
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 3600

# HL auto-analyst off during Researcher PRIMARY — Playground analyze misfits HU axis eval
set_kv CEMINI_HL_AUTO_ANALYST 0
set_kv CEMINI_HL_AUTO_APPLY 0
set_kv CEMINI_S1B_EXPLOIT 1

grep -E '^(AGENT_VERSION|CEMINI_PRIMARY|ARENA_LOBBY|ARENA_RESEARCHER|CEMINI_RESEARCHER|CEMINI_TABLE_FORMAT|CEMINI_LOBBY_ROLE|CEMINI_JOIN_RETRY|CEMINI_HL_AUTO)=' .env

# Drop stale 6-max Playground fold guards (Researcher HU pivot)
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p reports/hl-loop
printf '%s\n' "{\"updated_at\":\"${TS}\",\"source\":\"researcher_primary_pivot\",\"guards\":[]}" \
  > reports/hl-loop/runtime_guards.json
if [[ -f .arena-kill-switch.json ]]; then
  printf '%s\n' "{\"active\":false,\"reason\":\"researcher primary pivot\",\"cleared_at\":\"${TS}\"}" \
    > .arena-kill-switch.json
fi
echo "    cleared runtime_guards.json (+ kill switch if present)"

systemctl restart cemini-devfun-poker-lobby.service

# Stop parallel Playground volume lane — Researcher prep owns compute budget
if systemctl list-unit-files cemini-devfun-poker-lobby-s3.service --no-legend 2>/dev/null | grep -q enabled; then
  systemctl stop cemini-devfun-poker-lobby-s3.service || true
  systemctl disable cemini-devfun-poker-lobby-s3.service || true
  echo "    stopped cemini-devfun-poker-lobby-s3.service (Playground volume lane)"
fi

sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
REMOTE

echo ""
echo "✓ Researcher PRIMARY on ${HOST}"
echo "  Playground: slow intel only (1h join cadence, no S3 parallel service)"
echo "  When comp live: ARENA_RESEARCHER_COMP_ID=<id> CEMINI_RESEARCHER_MODE=1"
echo "  Flip lobby: ARENA_LOBBY_COMPETITION_ID=<researcher id> + restart lobby"
echo "  Daily: bash scripts/list_arena_competitions.sh"
