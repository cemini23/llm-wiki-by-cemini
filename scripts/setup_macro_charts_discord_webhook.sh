#!/usr/bin/env bash
# One-time: save Discord incoming webhook for Macro Charts parameter watches.
#
# Discord: Channel → Edit Channel → Integrations → Webhooks → New Webhook → Copy URL
#
# Usage:
#   bash scripts/setup_macro_charts_discord_webhook.sh
#   bash scripts/setup_macro_charts_discord_webhook.sh 'https://discord.com/api/webhooks/...'
#   python3 scripts/macro_charts_watch.py test-discord

set -euo pipefail

DEST="$HOME/.cemini/macro-charts-discord-webhook.url"
mkdir -p "$(dirname "$DEST")"

if [[ -n "${1:-}" ]]; then
  url="$1"
else
  echo "Paste Discord incoming webhook URL (channel → Integrations → Webhooks):"
  read -r url
fi

url=$(echo "$url" | tr -d '[:space:]')
if [[ ! "$url" =~ ^https://discord\.com/api/webhooks/ ]]; then
  echo "ERROR: expected https://discord.com/api/webhooks/..." >&2
  exit 1
fi

printf '%s\n' "$url" > "$DEST"
chmod 600 "$DEST"
echo "Saved to $DEST"

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/scripts/macro_charts_watch.py" test-discord
