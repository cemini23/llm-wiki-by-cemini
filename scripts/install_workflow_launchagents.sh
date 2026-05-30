#!/usr/bin/env bash
# install_workflow_launchagents.sh — K84 script-first workflow automations (laptop).
#
# Installs LaunchAgents for:
#   - inbox_notify (WatchPaths on research to be indexed/)
#   - verify_wiki_sync hourly backstop (sync still fires on git post-commit)
#
# Does NOT install n8n — matches @concepts/cemini-workflow-tooling-audit-2026-05-30.md.
#
# Usage:
#   bash scripts/install_workflow_launchagents.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT_DIR="$HOME/Library/LaunchAgents"
INBOX="$ROOT/research to be indexed"

chmod +x "$ROOT/scripts/inbox_notify.sh"
chmod +x "$ROOT/scripts/verify_wiki_sync.sh"
chmod +x "$ROOT/scripts/license_spot_check.sh"

mkdir -p "$AGENT_DIR"
mkdir -p "$INBOX"
mkdir -p "$HOME/Library/Logs"

INBOX_PLIST="$AGENT_DIR/com.cemini.inbox-notify.plist"
SYNC_PLIST="$AGENT_DIR/com.cemini.wiki-sync-verify.plist"

cat > "$INBOX_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cemini.inbox-notify</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/inbox_notify.sh</string>
  </array>
  <key>WatchPaths</key>
  <array>
    <string>${INBOX}</string>
  </array>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-inbox-watch.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-inbox-watch.log</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF

cat > "$SYNC_PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cemini.wiki-sync-verify</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/verify_wiki_sync.sh</string>
  </array>
  <key>StartInterval</key>
  <integer>3600</integer>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-wiki-sync.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-wiki-sync.log</string>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/com.cemini.inbox-notify" 2>/dev/null || true
launchctl bootout "gui/$(id -u)/com.cemini.wiki-sync-verify" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$INBOX_PLIST"
launchctl bootstrap "gui/$(id -u)" "$SYNC_PLIST"
launchctl enable "gui/$(id -u)/com.cemini.inbox-notify"
launchctl enable "gui/$(id -u)/com.cemini.wiki-sync-verify"

echo "Installed LaunchAgents:"
echo "  $INBOX_PLIST"
echo "  $SYNC_PLIST"
echo ""
echo "Logs:"
echo "  ~/Library/Logs/cemini-inbox-watch.log"
echo "  ~/Library/Logs/cemini-wiki-sync.log"
echo ""
echo "Optional webhook: echo 'https://...' > ~/.cemini/inbox-webhook.url"
