#!/usr/bin/env bash
# Federation morning summary — LaunchAgent entrypoint.
# Repo path: ~/.cemini/federation-hub.path

set -uo pipefail

# shellcheck source=/dev/null
source "${HOME}/.cemini/launchagent/_python3.sh"

REPO_FILE="${HOME}/.cemini/federation-hub.path"
PAYLOAD="${HOME}/.cemini/launchagent/federation/run_federation_morning_summary.py"
LOG_FILE="${HOME}/Library/Logs/cemini-federation-summary.log"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE" >&2
}

if [[ ! -r "${REPO_FILE}" ]]; then
  log "ERROR: missing ${REPO_FILE} — run: bash scripts/reinstall_morning_launchagents.sh"
  exit 1
fi

ROOT="$(tr -d '\r\n' < "${REPO_FILE}")"

if [[ ! -f "$PAYLOAD" ]]; then
  log "ERROR: missing ${PAYLOAD} — run: bash scripts/reinstall_morning_launchagents.sh"
  exit 1
fi

export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
export CEMINI_FEDERATION_ROOT="${ROOT}"
PY="$(cemini_launchagent_python3)"

if ! cd "${ROOT}"; then
  log "ERROR: cannot cd to ROOT=${ROOT}"
  exit 1
fi

set +e
"$PY" "$PAYLOAD" 2>&1 | tee -a "$LOG_FILE"
RC=${PIPESTATUS[0]}
set -e

if [[ "$RC" -ne 0 ]]; then
  log "Federation summary failed (exit $RC)"
fi
exit "$RC"
