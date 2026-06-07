#!/usr/bin/env bash
# Preflight for next playground season — new competitionId, fresh export dir, scoring detect.
#
# Usage (from repo root):
#   ./agents/devfun-poker-arena/scripts/playground_rollover_preflight.sh <NEW_COMPETITION_ID> [export-slug]
#
# Prod (after rsync deploy):
#   ssh cemini-prod 'cd /opt/devfun-poker-arena && ./scripts/playground_rollover_preflight.sh cmpNEW... playground-s1b-live'
#
# Does NOT auto-restart lobby unless PLAYGROUND_ROLLOVER_RESTART=1
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"

NEW_COMP="${1:-}"
EXPORT_SLUG="${2:-playground-next}"

if [[ -z "${NEW_COMP}" ]]; then
  echo "Usage: $0 <NEW_COMPETITION_ID> [export-slug]" >&2
  exit 2
fi

run_remote() {
  ssh -q "${HOST}" bash -s <<REMOTE
set -euo pipefail
cd "${REMOTE_DIR}"
NEW_COMP="${NEW_COMP}"
EXPORT_SLUG="${EXPORT_SLUG}"
EXPORT_DIR="${REMOTE_DIR}/reports/exports/\${EXPORT_SLUG}"

echo "==> Detect scoring mode for \${NEW_COMP}"
./venv/bin/python examples/detect_scoring_mode.py --match "\${NEW_COMP}" \\
  --json-out "\${EXPORT_DIR}/scoring_mode.json" || true

echo "==> Prepare export directory \${EXPORT_DIR}"
mkdir -p "\${EXPORT_DIR}"
cat > "\${EXPORT_DIR}/crawl_state.json" <<'JSON'
{
  "completed_agent_ids": [],
  "cycles": 0,
  "leaderboard_total": 0
}
JSON

echo "==> Update prod .env competition id"
if grep -q '^ARENA_LOBBY_COMPETITION_ID=' .env; then
  sed -i.bak "s/^ARENA_LOBBY_COMPETITION_ID=.*/ARENA_LOBBY_COMPETITION_ID=\${NEW_COMP}/" .env
else
  echo "ARENA_LOBBY_COMPETITION_ID=\${NEW_COMP}" >> .env
fi
grep '^ARENA_LOBBY_COMPETITION_ID=' .env

echo "==> Point export services at new dir (manual review recommended)"
echo "    Set CEMINI_EXPORT_DIR=\${EXPORT_DIR} in:"
echo "      deploy/cemini-devfun-poker-export.service"
echo "      deploy/cemini-devfun-poker-export-crawl.service"
echo "    Then: systemctl daemon-reload && systemctl restart timers"

if [[ "\${PLAYGROUND_ROLLOVER_RESTART:-0}" == "1" ]]; then
  systemctl restart cemini-devfun-poker-lobby.service
  echo "==> Lobby restarted"
else
  echo "==> Lobby NOT restarted (set PLAYGROUND_ROLLOVER_RESTART=1 to restart)"
fi

echo "==> Scoring report:"
cat "\${EXPORT_DIR}/scoring_mode.json" 2>/dev/null || echo "(detect failed — check arena API)"
REMOTE
}

echo "==> Playground rollover preflight → ${HOST}"
echo "    competition: ${NEW_COMP}"
echo "    export slug: ${EXPORT_SLUG}"
run_remote
