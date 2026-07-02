#!/usr/bin/env bash
# Install LaunchAgent: ICE county recorder sweep every 4h + Discord on new sale signals.
#
# Prereqs:
#   bash scripts/setup_recorder_discord_webhook.sh '<discord webhook url>'
#   playwright install   # for --browser sweeps
#
# Usage:
#   bash scripts/install_recorder_discord_launchagent.sh
#   bash scripts/install_recorder_discord_launchagent.sh --uninstall

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.cemini.ice-recorder-watch"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
BIN="$HOME/bin/cemini-ice-recorder-watch"
LOG="$HOME/Library/Logs/cemini-ice-recorder-watch.log"
INTERVAL=14400  # 4 hours

if [[ "${1:-}" == "--uninstall" ]]; then
  launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
  rm -f "$PLIST" "$BIN"
  echo "Removed $LABEL"
  exit 0
fi

if [[ ! -f "$HOME/.cemini/recorder-discord-webhook.url" ]] \
  && [[ ! -f "$HOME/.cemini/inbox-webhook.url" ]] \
  && [[ -z "${DISCORD_WEBHOOK_URL:-}" ]]; then
  echo "WARN: no Discord webhook configured. Run:" >&2
  echo "  bash scripts/setup_recorder_discord_webhook.sh" >&2
fi

mkdir -p "$HOME/bin" "$HOME/Library/LaunchAgents" "$(dirname "$LOG")"
printf '%s\n' "$ROOT" > "$HOME/.cemini/osint-workspace.path"

cat > "$BIN" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cat "$HOME/.cemini/osint-workspace.path")"
LOG="$HOME/Library/Logs/cemini-ice-recorder-watch.log"
exec >>"$LOG" 2>&1
echo "=== $(date '+%Y-%m-%d %H:%M:%S') ice-recorder-watch ==="
cd "$ROOT"
if command -v playwright >/dev/null 2>&1 && [[ -d "$HOME/Library/Caches/ms-playwright" ]]; then
  bash scripts/run_ice_turnkey_recorder_check.sh --browser --notify
else
  bash scripts/run_ice_turnkey_recorder_check.sh --notify
fi
EOF
chmod 755 "$BIN"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${BIN}</string>
  </array>
  <key>StartInterval</key>
  <integer>${INTERVAL}</integer>
  <key>StandardOutPath</key>
  <string>${LOG}</string>
  <key>StandardErrorPath</key>
  <string>${LOG}</string>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl enable "gui/$(id -u)/${LABEL}"

echo "Installed $LABEL (every ${INTERVAL}s / 4h)"
echo "  Runner: $BIN"
echo "  Log:    $LOG"
echo "  Test:   bash scripts/run_ice_turnkey_recorder_check.sh --test-discord"
