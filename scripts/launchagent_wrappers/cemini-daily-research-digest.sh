#!/usr/bin/env bash
# LaunchAgent entrypoint (installed to ~/bin/cemini-daily-research-digest).
# launchd cannot execute .sh files under Desktop; this wrapper lives in ~/bin,
# cds into the repo, and runs the Python collector directly.
#
# Repo path: ~/.cemini/osint-workspace.path (written by install_workflow_launchagents.sh)

set -uo pipefail

# shellcheck source=/dev/null
source "${HOME}/.cemini/launchagent/_python3.sh"

REPO_FILE="${HOME}/.cemini/osint-workspace.path"
LOG_FILE="${HOME}/Library/Logs/cemini-daily-digest.log"
TODAY="$(date +%Y-%m-%d)"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE" >&2
}

if [[ ! -r "${REPO_FILE}" ]]; then
  log "ERROR: missing ${REPO_FILE} — run: bash scripts/install_workflow_launchagents.sh"
  exit 1
fi

ROOT="$(tr -d '\r\n' < "${REPO_FILE}")"
REPORT="${ROOT}/wiki/sweeps/${TODAY}-daily.md"

log "Starting daily research digest (wrapper → ${ROOT})"

if ! cd "${ROOT}"; then
  log "ERROR: cannot cd to ROOT=${ROOT}"
  exit 1
fi

export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
export CEMINI_WIKI_ROOT="${ROOT}"
PY="$(cemini_launchagent_python3)"

REPO_RUNNER="${ROOT}/scripts/daily_research_digest_run.py"
BUNDLE_RUNNER="${HOME}/.cemini/launchagent/osint/daily_research_digest_run.py"
if [[ -f "$REPO_RUNNER" ]]; then
  PAYLOAD="$REPO_RUNNER"
else
  PAYLOAD="$BUNDLE_RUNNER"
fi
log "Digest runner: ${PAYLOAD}"

if [[ ! -f "$PAYLOAD" ]]; then
  log "ERROR: missing ${PAYLOAD} — run: bash scripts/reinstall_morning_launchagents.sh"
  exit 1
fi

set +e
"$PY" "$PAYLOAD" 2>&1 | tee -a "$LOG_FILE"
DIGEST_RC=${PIPESTATUS[0]}
set -e

if [[ ! -f "$REPORT" ]]; then
  log "ERROR: report missing after daily_research_digest_run.py"
  exit 4
fi

if [[ "$DIGEST_RC" -eq 3 ]]; then
  log "Digest completed with partial Exa failures"
  log "Report: $REPORT"
  exit 3
fi
if [[ "$DIGEST_RC" -ne 0 ]]; then
  log "Digest failed (exit $DIGEST_RC)"
  exit "$DIGEST_RC"
fi

log "Digest completed successfully"
log "Report: $REPORT"
exit 0
