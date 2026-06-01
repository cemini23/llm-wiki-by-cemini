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
mkdir -p "$HOME/bin"
mkdir -p "$HOME/.cemini"
mkdir -p "$ROOT/.local/reports"

install_daily_digest_wrapper() {
  local wrapper_src="$ROOT/scripts/launchagent_wrappers/cemini-daily-research-digest.sh"
  local wrapper_bin="$HOME/bin/cemini-daily-research-digest"
  local repo_path_file="$HOME/.cemini/osint-workspace.path"

  if [[ ! -f "$wrapper_src" ]]; then
    echo "ERROR: missing $wrapper_src" >&2
    exit 1
  fi
  printf '%s\n' "$ROOT" > "$repo_path_file"
  chmod 600 "$repo_path_file"
  cp "$wrapper_src" "$wrapper_bin"
  chmod 755 "$wrapper_bin"
  echo "  $wrapper_bin"
  echo "  $repo_path_file"
}

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
  local program="${5:-}"
  local plist="$AGENT_DIR/${label}.plist"
  local -a prog_args=("/bin/bash")

  if [[ -n "$program" ]]; then
    prog_args+=("$program")
  else
    prog_args+=("${ROOT}/scripts/${script}")
  fi

  cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${prog_args[0]}</string>
    <string>${prog_args[1]}</string>
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
install_daily_digest_wrapper
write_agent "com.cemini.inbox-notify" "inbox_notify.sh" ""
write_agent "com.cemini.wiki-sync-verify" "verify_wiki_sync.sh" "3600"
write_agent_calendar "com.cemini.daily-research-digest" "" "8" "0" "$HOME/bin/cemini-daily-research-digest"
write_agent "com.cemini.wc-lp-safety-reminder" "run_wc_lp_safety_reminder.sh" "$WEEKLY"
write_agent "com.cemini.wiki-gap-detect" "run_wiki_gap_detect.sh" "$WEEKLY"

echo ""
echo "Obsidian vault: wiki/.obsidian/ (run with --open to launch app)"
echo "Logs: ~/Library/Logs/cemini-{inbox-watch,wiki-sync,daily-digest,workflow,wc-lp-safety,wiki-gap-detect}.log"
echo "Daily digest (any directory): cemini-daily-research-digest"
echo "Optional webhook: echo 'https://...' > ~/.cemini/inbox-webhook.url"
