#!/usr/bin/env bash
# Rsync code-only to prod — never overwrite .arena-credentials, .env, or venv.
set -euo pipefail

HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE_DIR="/opt/devfun-poker-arena"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

rsync -avz \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude '.git/' \
  --exclude '__pycache__/' \
  --exclude '.arena-credentials' \
  --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' \
  --exclude '.env' \
  --exclude '.env.bak' \
  --exclude '.env.*' \
  --exclude 'dist/' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

echo "Done (creds + .env preserved on ${HOST})."
