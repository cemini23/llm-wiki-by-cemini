#!/usr/bin/env bash
# Jun 21 Researcher closed-beta prod apply — code deploy + full HU researcher env.
#
# Without ARENA_RESEARCHER_COMP_ID: Researcher PRIMARY posture, Playground slow intel,
# RESEARCHER_MODE=0 until comp pinned.
#
# With ARENA_RESEARCHER_COMP_ID (or auto-detect): lobby → researcher comp, MODE=1, hu.
#
# Usage:
#   ./scripts/researcher_jun21_beta_apply.sh
#   ARENA_RESEARCHER_COMP_ID=<id> ./scripts/researcher_jun21_beta_apply.sh
#   ./scripts/researcher_jun21_beta_apply.sh --auto-comp
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
GIT_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
DEPLOY_DATE="$(date -u +%Y-%m-%d)"
AGENT_VERSION="${AGENT_VERSION:-researcher-jun21.${GIT_SHA}.${DEPLOY_DATE}"
PLAYGROUND_COMP="${S3_PLAYGROUND_COMP:-cmqf827h30u7dfca3x2aqvzjv}"
AUTO_COMP=0
SKIP_CHECKLIST=0
RESEARCHER_COMP="${ARENA_RESEARCHER_COMP_ID:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --auto-comp) AUTO_COMP=1; shift ;;
    --skip-checklist) SKIP_CHECKLIST=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ "$AUTO_COMP" == "1" && -z "$RESEARCHER_COMP" ]]; then
  if RESEARCHER_COMP="$(uv run python "${AGENT_DIR}/examples/pick_researcher_competition.py" 2>/dev/null | sed -n 's/^candidate_id=//p')"; then
    [[ -n "$RESEARCHER_COMP" ]] || RESEARCHER_COMP=""
  fi
fi

RESEARCHER_MODE=0
LOBBY_COMP="$PLAYGROUND_COMP"
TABLE_FORMAT="hu"
if [[ -n "$RESEARCHER_COMP" ]]; then
  RESEARCHER_MODE=1
  LOBBY_COMP="$RESEARCHER_COMP"
  echo "==> Researcher comp pinned: ${RESEARCHER_COMP}"
else
  echo "==> No researcher comp id — PRIMARY posture, Playground intel (${PLAYGROUND_COMP})"
fi

echo "==> Local Jun 21 checklist (CI gate)"
if [[ "$SKIP_CHECKLIST" != "1" ]]; then
  bash "${SCRIPT_DIR}/run_researcher_jun21_checklist.sh" --ci
fi

echo "==> Deploy code: version=${AGENT_VERSION}"
export ARENA_LOBBY_COMPETITION_ID="${PLAYGROUND_COMP}"
export CEMINI_SKIP_ENV=1
export CEMINI_SKIP_CREDS=1
export CEMINI_SKIP_COMP_CHECK="${CEMINI_SKIP_COMP_CHECK:-1}"
"${AGENT_DIR}/deploy/deploy_to_cemini_prod.sh"

ssh -q "${HOST}" env \
  PLAYGROUND_COMP="${PLAYGROUND_COMP}" \
  RESEARCHER_COMP="${RESEARCHER_COMP}" \
  LOBBY_COMP="${LOBBY_COMP}" \
  RESEARCHER_MODE="${RESEARCHER_MODE}" \
  TABLE_FORMAT="${TABLE_FORMAT}" \
  AGENT_VERSION="${AGENT_VERSION}" \
  REMOTE_DIR="${REMOTE_DIR}" bash -s <<'REMOTE'
set -eo pipefail
cd "${REMOTE_DIR}"

set_kv() {
  local key="$1" val="$2"
  if grep -q "^${key}=" .env 2>/dev/null; then
    sed -i.bak "s|^${key}=.*|${key}=${val}|" .env
  else
    echo "${key}=${val}" >> .env
  fi
}

set_kv ARENA_LOBBY_COMPETITION_ID "${LOBBY_COMP}"
set_kv S3_PLAYGROUND_COMP "${PLAYGROUND_COMP}"
set_kv ARENA_RESEARCHER_COMP_ID "${RESEARCHER_COMP}"
set_kv AGENT_VERSION "${AGENT_VERSION}"
set_kv CEMINI_PRIMARY_TRACK researcher
set_kv CEMINI_LOBBY_LABEL "Researcher_Jun21_beta"
set_kv CEMINI_LOBBY_ROLE researcher_primary
set_kv CEMINI_RESEARCHER_MODE "${RESEARCHER_MODE}"
set_kv CEMINI_PLACEMENT_CHASE 0
set_kv CEMINI_EVAL_PANEL_MODE 0
set_kv CEMINI_TABLE_FORMAT "${TABLE_FORMAT}"
set_kv CEMINI_MAFP_CHART 1
set_kv CEMINI_TRAJECTORY_BOUND 1
set_kv CEMINI_SANITIZE_OUTPUT 1
set_kv CEMINI_SESSION_MEMORY 1
set_kv CEMINI_MIX_POSTFLOP 1
set_kv CEMINI_EXPORT_TOP_AGENTS 50
set_kv CEMINI_S1B_EXPLOIT 1

# Gin-style HU aggression (K118/K122 Jungleman band)
set_kv CEMINI_GIN_STYLE 1
set_kv CEMINI_GIN_STYLE_PREFLOP 1
set_kv CEMINI_GIN_STYLE_POSTFLOP 1
set_kv CEMINI_GIN_V008 1

# Playground background intel only
set_kv CEMINI_FIRST_RANK 0
set_kv CEMINI_STAGGER_LOCKS 0
set_kv CEMINI_PLAYGROUND_TIMESERIES 0
set_kv CEMINI_FIELD_EXPORT_HUD 0
set_kv CEMINI_PACE_PHASE intel
set_kv CEMINI_JOIN_RETRY_S 3600
set_kv CEMINI_IN_QUEUE_RETRY_S 600
set_kv CEMINI_LOW_STACK_JOIN_RETRY_S 3600
set_kv CEMINI_HL_AUTO_ANALYST 0
set_kv CEMINI_HL_AUTO_APPLY 0

grep -E '^(AGENT_VERSION|CEMINI_PRIMARY|ARENA_LOBBY|ARENA_RESEARCHER|CEMINI_RESEARCHER|CEMINI_TABLE_FORMAT|CEMINI_MAFP|CEMINI_GIN_STYLE)=' .env

TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
mkdir -p reports/hl-loop
printf '%s\n' "{\"updated_at\":\"${TS}\",\"source\":\"jun21_beta_apply\",\"guards\":[]}" \
  > reports/hl-loop/runtime_guards.json

systemctl restart cemini-devfun-poker-lobby.service
if systemctl list-unit-files cemini-devfun-poker-lobby-s3.service --no-legend 2>/dev/null | grep -q enabled; then
  systemctl stop cemini-devfun-poker-lobby-s3.service || true
  systemctl disable cemini-devfun-poker-lobby-s3.service || true
fi
sleep 2
systemctl is-active cemini-devfun-poker-lobby.service
REMOTE

echo ""
echo "✓ Jun 21 beta apply on ${HOST}"
echo "  researcher_comp=${RESEARCHER_COMP:-<pending>}"
echo "  researcher_mode=${RESEARCHER_MODE}"
echo "  table_format=hu  mafp_chart=1  gin_style=1"
