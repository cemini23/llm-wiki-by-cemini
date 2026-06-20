#!/usr/bin/env bash
# Pull DISCORD_WEBHOOK_URL from cemini-prod (preferred) or local CeminiSuite .env
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/.env"
TMP="$(mktemp)"

cleanup() { rm -f "$TMP"; }
trap cleanup EXIT

PROD_ENV="${CEMINI_PROD_ENV:-/opt/cemini/.env}"
LOCAL_ENV="${CEMINI_LOCAL_ENV:-$HOME/Desktop/projects/CeminiSuite/.env}"

webhook=""
source_label=""
if command -v ssh >/dev/null 2>&1; then
  webhook="$(ssh cemini-prod "grep -E '^DISCORD_WEBHOOK_URL=' '$PROD_ENV' 2>/dev/null | head -1" 2>/dev/null || true)"
  [[ -n "$webhook" ]] && source_label="cemini-prod"
fi

if [[ -z "$webhook" && -f "$LOCAL_ENV" ]]; then
  webhook="$(grep -E '^DISCORD_WEBHOOK_URL=' "$LOCAL_ENV" | head -1 || true)"
  [[ -n "$webhook" ]] && source_label="local CeminiSuite .env"
fi

if [[ -z "$webhook" ]]; then
  echo "Could not find DISCORD_WEBHOOK_URL on cemini-prod or $LOCAL_ENV" >&2
  exit 1
fi

{
  echo "# synced $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "$webhook"
  echo "PRICE_THRESHOLD_USD=1500"
  echo "POLL_INTERVAL_MINUTES=60"
  echo "ALERT_COOLDOWN_HOURS=24"
} > "$TMP"

if [[ -f "$OUT" ]]; then
  # preserve manual overrides except webhook
  while IFS= read -r line; do
    [[ "$line" =~ ^DISCORD_WEBHOOK_URL= ]] && continue
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    echo "$line" >> "$TMP"
  done < "$OUT"
fi

mv "$TMP" "$OUT"
chmod 600 "$OUT"
trap - EXIT
echo "Wrote $OUT (DISCORD_WEBHOOK_URL from ${source_label})"
