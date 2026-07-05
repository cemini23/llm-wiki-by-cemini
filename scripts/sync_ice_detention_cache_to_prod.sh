#!/usr/bin/env bash
# Push laptop ICE detention xlsx cache to prod (ICE.gov blocks datacenter IPs).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROD_HOST="${PROD_HOST:-cemini-prod}"
REMOTE_ROOT="/opt/cemini/intel/ice-facility-jobs"
LOCAL_CACHE="$ROOT/.local/ice-detention-stats"

if [[ ! -d "$LOCAL_CACHE" ]] || [[ -z "$(ls -A "$LOCAL_CACHE"/*.xlsx 2>/dev/null)" ]]; then
  echo "No local ICE detention xlsx cache at $LOCAL_CACHE — run detention stats monitor on laptop first." >&2
  exit 1
fi

ssh "$PROD_HOST" "mkdir -p '$REMOTE_ROOT/.local/ice-detention-stats'"
scp "$LOCAL_CACHE"/*.xlsx "$PROD_HOST:$REMOTE_ROOT/.local/ice-detention-stats/"
echo "Synced $(ls -1 "$LOCAL_CACHE"/*.xlsx | wc -l | tr -d ' ') workbook(s) to $PROD_HOST:$REMOTE_ROOT/.local/ice-detention-stats/"
