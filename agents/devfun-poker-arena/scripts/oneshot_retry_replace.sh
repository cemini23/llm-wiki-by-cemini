#!/usr/bin/env bash
# One-shot: after Arena daily-limit reset, do EXACTLY ONE replace submit of the
# current bundle to the **pinned ladder competition**, then poll bench result.
# Scheduled via 'at' (single run). Retries ONLY on sandbox_daily_limit.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

PY="${AGENT_DIR}/venv/bin/python"
if [[ ! -x "${PY}" ]]; then
  PY="$(command -v python3)"
fi

# systemd loads .env for the timer service; bare 'at' jobs must source it explicitly.
if [[ -f "${AGENT_DIR}/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "${AGENT_DIR}/.env"
  set +a
fi

_resolve_competition_id() {
  local from_pin from_env
  from_pin="$("${PY}" -c "import json; print(json.load(open('config/researcher_sandbox_submit.pin.json')).get('competitionId',''))" 2>/dev/null || true)"
  from_env="${ARENA_RESEARCHER_COMP_ID:-}"
  if [[ -n "${from_pin}" ]]; then
    echo "${from_pin}"
  elif [[ -n "${from_env}" ]]; then
    echo "${from_env}"
  else
    echo "cmr3n8tft01nilecm1u5jlny7"
  fi
}

COMP_ID="$(_resolve_competition_id)"
STATE_DIR="${AGENT_DIR}/reports/researcher-round"
STATE="${STATE_DIR}/oneshot-retry-state.json"
LOG="${STATE_DIR}/oneshot-retry-$(date -u +%Y%m%dT%H%M%SZ).log"
mkdir -p "${STATE_DIR}"

{
  echo "== oneshot replace retry START @ $(date -u) =="
  echo "competitionId=${COMP_ID} (pin > ARENA_RESEARCHER_COMP_ID > ladder fallback)"
  echo "-- building bundle --"
  "${PY}" examples/submit_sandbox_pvp.py --build-only

  submitted=0
  for attempt in 1 2 3 4 5 6 7 8; do
    echo "-- submit attempt ${attempt} @ $(date -u) --"
    "${PY}" examples/submit_sandbox_pvp.py \
      --replace \
      --competition-id "${COMP_ID}" \
      --tolerate-daily-limit \
      --state-file "${STATE}"
    status="$("${PY}" -c "import json; print(json.load(open('${STATE}')).get('status',''))" 2>/dev/null || true)"
    reason="$("${PY}" -c "import json; print(json.load(open('${STATE}')).get('reason',''))" 2>/dev/null || true)"
    echo "   status=${status} reason=${reason}"
    if [[ "${status}" == "submitted" ]]; then
      submitted=1
      break
    fi
    if [[ "${reason}" != "sandbox_daily_limit" ]]; then
      echo "   non-limit outcome — stop"
      break
    fi
    echo "   still daily-limited — wait 30m"
    sleep 1800
  done

  if [[ "${submitted}" == "1" ]]; then
    SID="$("${PY}" -c "import json; print(json.load(open('${STATE}')).get('submission',{}).get('id',''))" 2>/dev/null || true)"
    echo "submission id: ${SID}"
    for _ in 1 2 3 4 5 6 7 8; do
      sleep 60
      echo "-- poll @ $(date -u) --"
      rec="$("${PY}" examples/submit_sandbox_pvp.py --poll "${SID}" 2>/dev/null || true)"
      echo "${rec}" | "${PY}" -c "import sys,json; d=json.load(sys.stdin); print({k:d.get(k) for k in ('status','competitionId','completedHands','targetHands','errorCode','error')})" 2>/dev/null || true
      st="$(echo "${rec}" | "${PY}" -c "import sys,json; print(json.load(sys.stdin).get('status',''))" 2>/dev/null || true)"
      if [[ "${st}" == "Succeeded" || "${st}" == "Failed" ]]; then
        echo "   terminal: ${st}"
        break
      fi
    done
  fi
  echo "== oneshot replace retry DONE @ $(date -u) =="
} >> "${LOG}" 2>&1

echo "${LOG}"
