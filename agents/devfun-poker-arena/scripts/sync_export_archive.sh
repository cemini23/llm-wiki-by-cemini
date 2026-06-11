#!/usr/bin/env bash
# Rsync prod export dir to laptop archive (gitignored).
#
# Usage:
#   ./scripts/sync_export_archive.sh playground-s1-live
#   ./scripts/sync_export_archive.sh playground-s1b-live
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
SLUG="${1:-s1-tournament-live}"
HOST="${CEMINI_PROD_HOST:-cemini-prod}"
REMOTE="/opt/devfun-poker-arena/reports/exports/${SLUG}"
LOCAL="${AGENT_DIR}/reports/exports/${SLUG}-archive"

mkdir -p "${LOCAL}"
echo "==> ${HOST}:${REMOTE} → ${LOCAL}"
rsync -avz --progress \
  "${HOST}:${REMOTE}/" \
  "${LOCAL}/"

echo "==> Local sizes"
du -sh "${LOCAL}"/* 2>/dev/null | head -20 || true
wc -l "${LOCAL}"/*.jsonl 2>/dev/null | tail -5 || true
