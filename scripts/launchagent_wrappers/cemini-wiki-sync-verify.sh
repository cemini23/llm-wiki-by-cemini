#!/usr/bin/env bash
# Wiki sync verify — LaunchAgent entrypoint (~/bin only; never exec .sh on Desktop).
# Reads repo path from ~/.cemini/osint-workspace.path and pipes script via stdin.

set -uo pipefail

REPO_FILE="${HOME}/.cemini/osint-workspace.path"
LOG_FILE="${HOME}/Library/Logs/cemini-wiki-sync.log"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE" >&2
}

if [[ ! -r "${REPO_FILE}" ]]; then
  log "ERROR: missing ${REPO_FILE}"
  exit 1
fi

ROOT="$(tr -d '\r\n' < "${REPO_FILE}")"
SCRIPT="${HOME}/.cemini/launchagent/osint/verify_wiki_sync.sh"

if [[ ! -f "$SCRIPT" ]]; then
  log "ERROR: missing ${SCRIPT} — run: bash scripts/reinstall_morning_launchagents.sh"
  exit 1
fi

export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
export CEMINI_LIBRARIAN_HOST="${CEMINI_LIBRARIAN_HOST:-cemini-librarian}"

if ! cd "${ROOT}"; then
  log "ERROR: cannot cd to ROOT=${ROOT}"
  exit 1
fi

export CEMINI_OSINT_ROOT="${ROOT}"
set +e
# Payload lives under ~/.cemini (not Desktop) — safe for launchd bash redirect
bash -s < "$SCRIPT" 2>&1 | tee -a "$LOG_FILE"
RC=${PIPESTATUS[0]}
set -e

exit "$RC"
