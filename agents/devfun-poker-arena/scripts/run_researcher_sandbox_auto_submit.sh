#!/usr/bin/env bash
# Auto-submit Researcher HU sandbox bundle when daily Arena limit allows.
#
# Orchestration (examples/researcher_sandbox_auto_submit.py):
#   1. Try --replace when pin allows
#   2. On sandbox_agent_already_running → wait for active PvP to finish
#   3. Submit fresh bundle (no replace) when slot is free
#
# Writes reports/researcher-round/auto-submit-state.json
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

STATE_DIR="${AGENT_DIR}/reports/researcher-round"
STATE="${STATE_DIR}/auto-submit-state.json"
LOG="${STATE_DIR}/auto-submit.log"
DRY_RUN=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

run_py() {
  if [[ -x "${AGENT_DIR}/venv/bin/python" ]]; then
    "${AGENT_DIR}/venv/bin/python" "$@"
  elif command -v uv >/dev/null 2>&1; then
    uv run python "$@"
  else
    python3 "$@"
  fi
}

mkdir -p "${STATE_DIR}"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

log() {
  echo "[${TS}] $*" | tee -a "${LOG}"
}

if [[ "${DRY_RUN}" == "1" ]]; then
  log "DRY_RUN: would run researcher_sandbox_auto_submit.py"
  exit 0
fi

PIN="${AGENT_DIR}/config/researcher_sandbox_submit.pin.json"
HEAD_SHA="$(git -C "${AGENT_DIR}" rev-parse --short HEAD 2>/dev/null || echo unknown)"
PIN_SHA="$(python3 -c "import json; print(json.load(open('${PIN}')).get('gitCommit',''))" 2>/dev/null || true)"
if [[ "${CEMINI_SUBMIT_SKIP_REV_CHECK:-}" != "1" && -n "${PIN_SHA}" && "${HEAD_SHA}" != "${PIN_SHA}" ]]; then
  log "WARN: git HEAD ${HEAD_SHA} != pin gitCommit ${PIN_SHA} — skip submit (CEMINI_SUBMIT_SKIP_REV_CHECK=1 to override)"
  exit 0
fi

log "auto-submit orchestrator start"
if [[ -z "${CEMINI_SANDBOX_ENGINE:-}" && -f config/researcher_sandbox_submit.pin.json ]]; then
  export CEMINI_SANDBOX_ENGINE="$(python3 -c "import json; print(json.load(open('config/researcher_sandbox_submit.pin.json')).get('sandboxEngine','cemini'))")"
fi
set +e
run_py examples/researcher_sandbox_auto_submit.py --state-file "${STATE}" 2>&1 | tee -a "${LOG}"
EXIT=$?
set -e

if [[ "${EXIT}" -ne 0 ]]; then
  log "FAIL: orchestrator exited ${EXIT}"
  exit 1
fi

if [[ -f "${AGENT_DIR}/dist/sandbox-pvp-bundle.zip" ]]; then
  bash "${SCRIPT_DIR}/verify_sandbox_bundle_layout.sh" "${AGENT_DIR}/dist/sandbox-pvp-bundle.zip" 2>&1 | tee -a "${LOG}" || {
    log "WARN: bundle layout verify failed"
  }
fi

STATUS="$(python3 -c "import json; print(json.load(open('${STATE}')).get('status',''))" 2>/dev/null || true)"
case "${STATUS}" in
  submitted) log "OK: submitted mode=$(python3 -c "import json; print(json.load(open('${STATE}')).get('mode',''))")" ;;
  waiting_for_finish)
    log "WAIT: $(python3 -c "import json; d=json.load(open('${STATE}')); print(d.get('completedHands'),'/',d.get('targetHands'))")"
    ;;
  skipped) log "SKIP: $(python3 -c "import json; print(json.load(open('${STATE}')).get('reason',''))")" ;;
  *) log "state=${STATUS}" ;;
esac
