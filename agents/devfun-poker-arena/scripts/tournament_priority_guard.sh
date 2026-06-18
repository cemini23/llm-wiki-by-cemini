#!/usr/bin/env bash
# Tournament money priority — pause Playground S3 while Tournament S2 is Active.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
S2T="${S2_TOURNAMENT_COMP:-cmqggiv9k37am11ydmppz466e}"
S3="${S3_PLAYGROUND_COMP:-cmqf827h30u7dfca3x2aqvzjv}"

if [[ "${CEMINI_TOURNAMENT_PRIORITY_LOCAL:-}" == "1" ]]; then
  cd "${REMOTE_DIR:-${AGENT_DIR}}"
  state="$(./venv/bin/python examples/tournament_priority.py \
    --tournament-comp "${S2T}" --playground-comp "${S3}" --json)"
  pause="$(echo "${state}" | ./venv/bin/python -c "import sys,json; print(json.load(sys.stdin).get('pause_playground'))")"
  resume="$(echo "${state}" | ./venv/bin/python -c "import sys,json; print(json.load(sys.stdin).get('resume_playground'))")"
  echo "[tournament-priority] ${state}"
  if [[ "${pause}" == "True" ]]; then
    if systemctl is-active cemini-devfun-poker-lobby-s3.service 2>/dev/null | grep -q active; then
      echo "[tournament-priority] S2 tournament Active — stopping Playground S3 lobby"
      systemctl stop cemini-devfun-poker-lobby-s3.service
      ./venv/bin/python scripts/playground_drain_competition.py "${S3}" || true
    fi
    systemctl start cemini-devfun-poker-lobby.service 2>/dev/null || true
  elif [[ "${resume}" == "True" ]]; then
    # Main lobby already on this playground comp — do not start parallel S3 (1-table agent limit).
    lobby_comp="$(grep -E '^ARENA_LOBBY_COMPETITION_ID=' .env 2>/dev/null | cut -d= -f2- | tr -d '"' || true)"
    if [[ -n "${lobby_comp}" && "${lobby_comp}" == "${S3}" ]]; then
      echo "[tournament-priority] Main lobby owns playground ${S3} — skip S3 parallel unit"
      if systemctl is-active cemini-devfun-poker-lobby-s3.service 2>/dev/null | grep -q active; then
        systemctl stop cemini-devfun-poker-lobby-s3.service || true
      fi
    elif ! systemctl is-active cemini-devfun-poker-lobby-s3.service 2>/dev/null | grep -q active; then
      if systemctl is-enabled cemini-devfun-poker-lobby-s3.service 2>/dev/null | grep -q enabled; then
        echo "[tournament-priority] Tournament not blocking — resuming Playground S3 qual"
        systemctl start cemini-devfun-poker-lobby-s3.service
      fi
    fi
  fi
  exit 0
fi

ssh -q "${HOST}" "CEMINI_TOURNAMENT_PRIORITY_LOCAL=1 S2_TOURNAMENT_COMP='${S2T}' S3_PLAYGROUND_COMP='${S3}' bash ${REMOTE_DIR}/scripts/tournament_priority_guard.sh"
