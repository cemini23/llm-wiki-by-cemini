#!/usr/bin/env bash
# install_workflow_launchagents.sh — K84/K85 script-first workflow automations (laptop).
#
# Installs LaunchAgents for:
#   - inbox_notify (WatchPaths on research to be indexed/)
#   - verify_wiki_sync hourly backstop
#   - daily_research_digest @ 08:00 local
#   - wc_lp_safety weekly reminder
#   - wiki_gap_detect weekly report
#
# Also runs setup_obsidian_vault.sh (local .obsidian chrome).
#
# Usage:
#   bash scripts/install_workflow_launchagents.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT_DIR="$HOME/Library/LaunchAgents"
INBOX="$ROOT/research to be indexed"
WEEKLY=$((7 * 24 * 3600))

for s in inbox_notify verify_wiki_sync daily_research_digest run_daily_research_digest \
  check_daily_research_digest_due append_inbox_to_daily_sweep license_spot_check \
  post_tool_eval_license run_wc_lp_safety_reminder run_wiki_gap_detect \
  check_wc_lp_safety_due check_wiki_gap_detect_due notebooklm_export_brief \
  setup_obsidian_vault; do
  chmod +x "$ROOT/scripts/${s}.sh" 2>/dev/null || true
done
chmod +x "$ROOT/scripts/daily_research_digest_run.py" \
  "$ROOT/scripts/append_inbox_to_daily_sweep.py" \
  "$ROOT/scripts/ingest_session_gate.py" 2>/dev/null || true

bash "$ROOT/scripts/setup_obsidian_vault.sh"

mkdir -p "$AGENT_DIR"
mkdir -p "$INBOX"
mkdir -p "$HOME/Library/Logs"
mkdir -p "$ROOT/.local/reports"

write_agent() {
  local label="$1"
  local script="$2"
  local interval="${3:-}"
  local plist="$AGENT_DIR/${label}.plist"

  if [[ -n "$interval" ]]; then
    cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/${script}</string>
  </array>
  <key>StartInterval</key>
  <integer>${interval}</integer>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-workflow.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-workflow.log</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF
  else
    cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/${script}</string>
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
  fi

  launchctl bootout "gui/$(id -u)/${label}" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$plist"
  launchctl enable "gui/$(id -u)/${label}"
  echo "  $plist"
}

write_agent_calendar() {
  local label="$1"
  local script="$2"
  local hour="$3"
  local minute="$4"
  local plist="$AGENT_DIR/${label}.plist"

  cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>${ROOT}/scripts/${script}</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>${hour}</integer>
    <key>Minute</key>
    <integer>${minute}</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-daily-digest.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-daily-digest.log</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF

  launchctl bootout "gui/$(id -u)/${label}" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$plist"
  launchctl enable "gui/$(id -u)/${label}"
  echo "  $plist"
}

echo "Installing LaunchAgents..."
write_agent "com.cemini.inbox-notify" "inbox_notify.sh" ""
write_agent "com.cemini.wiki-sync-verify" "verify_wiki_sync.sh" "3600"
write_agent_calendar "com.cemini.daily-research-digest" "daily_research_digest.sh" "8" "0"
write_agent "com.cemini.wc-lp-safety-reminder" "run_wc_lp_safety_reminder.sh" "$WEEKLY"
write_agent "com.cemini.wiki-gap-detect" "run_wiki_gap_detect.sh" "$WEEKLY"

echo ""
echo "Obsidian vault: wiki/.obsidian/ (run with --open to launch app)"
echo "Logs: ~/Library/Logs/cemini-{inbox-watch,wiki-sync,daily-digest,workflow,wc-lp-safety,wiki-gap-detect}.log"
echo "Optional webhook: echo 'https://...' > ~/.cemini/inbox-webhook.url"
