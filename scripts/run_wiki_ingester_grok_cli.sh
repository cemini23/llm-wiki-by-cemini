#!/usr/bin/env bash
# Headless OSINT wiki ingest via Grok CLI (no Grok Bot GUI / no focused window).
# LaunchAgent: com.cemini.wiki-ingester @ 09:00 local (after 08:00 digest).
#
# Manual:
#   bash scripts/run_wiki_ingester_grok_cli.sh
# Opt out one morning:
#   touch ~/.cemini/wiki-ingester.skip

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG="${HOME}/Library/Logs/cemini-wiki-ingester.log"
LOCK="${HOME}/.cemini/wiki-ingester.lock"
SKIP="${HOME}/.cemini/wiki-ingester.skip"
PROMPT="${ROOT}/scripts/prompts/wiki-ingester-grok.md"
GROK="${GROK_BIN:-${HOME}/.grok/bin/grok}"

mkdir -p "$(dirname "$LOG")" "${HOME}/.cemini"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG" >&2
}

if [[ -f "$SKIP" ]]; then
  log "SKIP: ${SKIP} present"
  exit 0
fi

if [[ ! -x "$GROK" ]]; then
  if command -v grok >/dev/null 2>&1; then
    GROK="$(command -v grok)"
  else
    log "ERROR: grok CLI not found (${HOME}/.grok/bin/grok)"
    exit 1
  fi
fi

if [[ ! -f "$PROMPT" ]]; then
  log "ERROR: missing ${PROMPT}"
  exit 1
fi

if [[ -f "$LOCK" ]]; then
  old_pid="$(tr -d '[:space:]' < "$LOCK" || true)"
  if [[ -n "${old_pid}" ]] && kill -0 "$old_pid" 2>/dev/null; then
    log "ERROR: already running (pid ${old_pid})"
    exit 2
  fi
  log "WARN: stale lock (pid ${old_pid:-none}); continuing"
fi
echo "$$" > "$LOCK"
trap 'rm -f "$LOCK"' EXIT

cd "$ROOT"

export PATH="${HOME}/.grok/bin:/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin}"
# Do not inherit Cursor/Claude MCP stdio (handoff-to-grok hang at 0% CPU).
export GROK_CURSOR_MCPS_ENABLED=0
export GROK_CLAUDE_MCPS_ENABLED=0

log "Starting headless wiki ingest cwd=${ROOT} grok=$($GROK --version 2>/dev/null | head -1)"

set +e
"$GROK" \
  --cwd "$ROOT" \
  --always-approve \
  --prompt-file "$PROMPT" \
  --deny "Read(**/.env)" \
  --deny "Read(**/.env.*)" \
  --deny "Edit(**/.env)" \
  --deny "Edit(**/.env.*)" \
  --deny "Bash(git push --force*)" \
  --deny "Bash(git push -f*)" \
  >>"$LOG" 2>&1
rc=$?
set -e

if [[ "$rc" -ne 0 ]]; then
  log "FAILED exit=${rc} — see ${LOG}"
  exit "$rc"
fi
log "Completed"
exit 0
