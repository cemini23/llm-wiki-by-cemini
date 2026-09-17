#!/usr/bin/env bash
# LaunchAgent entrypoint (~/bin/cemini-wiki-ingester). Does not exec Desktop paths.

set -uo pipefail

REPO_FILE="${HOME}/.cemini/osint-workspace.path"
LOG_FILE="${HOME}/Library/Logs/cemini-wiki-ingester.log"

mkdir -p "$(dirname "$LOG_FILE")"

if [[ ! -r "${REPO_FILE}" ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: missing ${REPO_FILE}" >>"$LOG_FILE"
  exit 1
fi

ROOT="$(tr -d '\r\n' < "${REPO_FILE}")"
SCRIPT="${ROOT}/scripts/run_wiki_ingester_grok_cli.sh"

if [[ ! -f "$SCRIPT" ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: missing ${SCRIPT}" >>"$LOG_FILE"
  exit 1
fi

export PATH="${HOME}/.grok/bin:/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin}"
exec /bin/bash "$SCRIPT"
