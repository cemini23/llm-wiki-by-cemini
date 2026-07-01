#!/usr/bin/env bash
# Sync gin/poker-bot v3 hu004 into vendor/gin_hu004/ (Option A sandbox engine).
#
# Usage:
#   ./scripts/sync_gin_hu004.sh
#   GIN_POKER_BOT_SRC=/path/to/poker-bot ./scripts/sync_gin_hu004.sh
set -euo pipefail
cd "$(dirname "$0")/.."

SRC="${GIN_POKER_BOT_SRC:-}"
if [[ -z "${SRC}" ]]; then
  TMP="$(mktemp -d)"
  trap 'rm -rf "${TMP}"' EXIT
  git clone --depth 1 --branch v3 https://github.com/gin/poker-bot.git "${TMP}/poker-bot"
  SRC="${TMP}/poker-bot/src/poker_bot/strategies/hu004.py"
else
  if [[ -d "${SRC}" ]]; then
    SRC="${SRC}/src/poker_bot/strategies/hu004.py"
  fi
fi

DEST="vendor/gin_hu004/hu004.py"
mkdir -p vendor/gin_hu004
{
  echo "# Vendored from https://github.com/gin/poker-bot/tree/v3 (hu004.py)"
  echo "# Sync: bash scripts/sync_gin_hu004.sh — no LICENSE in upstream; algorithm port only."
  echo "# Retrieved: $(date -u +%Y-%m-%d)"
  echo
  cat "${SRC}"
} > "${DEST}"
echo "Synced $(wc -c < "${DEST}") bytes -> ${DEST}"
