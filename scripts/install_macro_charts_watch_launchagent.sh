#!/usr/bin/env bash
# Optional LaunchAgent: poll Macro Charts watches every 15 min → Discord.
#
# Prereq: bash scripts/setup_macro_charts_discord_webhook.sh '<url>'
#          python3 scripts/macro_charts_watch.py add ...  (or propose --arm)
#
# Usage:
#   bash scripts/install_macro_charts_watch_launchagent.sh
#   bash scripts/install_macro_charts_watch_launchagent.sh --uninstall

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.cemini.macro-charts-watch"
AGENT_DIR="$HOME/Library/LaunchAgents"
PLIST="$AGENT_DIR/${LABEL}.plist"
INTERVAL=900

chmod +x "$ROOT/scripts/run_macro_charts_watch_check.sh"

if [[ "${1:-}" == "--uninstall" ]]; then
  launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
  rm -f "$PLIST"
  echo "Removed $LABEL"
  exit 0
fi

mkdir -p "$AGENT_DIR" "$HOME/Library/Logs"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/run_macro_charts_watch_check.sh</string>
  </array>
  <key>StartInterval</key>
  <integer>${INTERVAL}</integer>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-macro-charts-watch.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-macro-charts-watch.log</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl enable "gui/$(id -u)/${LABEL}"
echo "Installed $PLIST (every ${INTERVAL}s)"
echo "Log: ~/Library/Logs/cemini-macro-charts-watch.log"
echo "Manual: bash scripts/run_macro_charts_watch_check.sh --dry-run"
