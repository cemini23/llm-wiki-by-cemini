#!/usr/bin/env bash
# Reinstall morning LaunchAgents with ~/bin wrappers (launchd-safe repo access).
#
# Fixes:
#   - verify_wiki_sync: bash < script (no exec of repo .sh from launchd)
#   - federated digests: PATH + logging + ~/.cemini/wiki-paths/*.path
#   - federation summary: path file + logging
#   - Desktop/OSINT WORKSPACE inbox symlink → canonical ~/Projects/OSINT WORKSPACE inbox
#
# Usage:
#   bash scripts/reinstall_morning_launchagents.sh
#   bash scripts/reinstall_morning_launchagents.sh --backfill   # run today's digests + federation

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT_DIR="$HOME/Library/LaunchAgents"
BIN_DIR="$HOME/bin"
CEMINI_DIR="$HOME/.cemini"
PATHS_DIR="$CEMINI_DIR/wiki-paths"
WEEKLY=$((7 * 24 * 3600))
BACKFILL=0
[[ "${1:-}" == "--backfill" ]] && BACKFILL=1

WRAPPER_SRC="$ROOT/scripts/launchagent_wrappers"
PAYLOAD_DIR="$CEMINI_DIR/launchagent"
PROJECTS="${CEMINI_PROJECTS_ROOT:-$HOME/Projects}"
FED_HUB="${PROJECTS}/cemini-federation-hub"
DESKTOP_OSINT="$HOME/Desktop/OSINT WORKSPACE"

resolve_3d_printing_repo() {
  local candidate
  for candidate in "${PROJECTS}/3D printing" "${PROJECTS}/3d printing"; do
    if [[ -d "$candidate" ]]; then
      printf '%s\n' "$candidate"
      return 0
    fi
  done
  printf '%s\n' "${PROJECTS}/3D printing"
}

# id|absolute-path (bash 3.2 safe — no associative arrays)
WIKI_REPOS=(
  "seo|${PROJECTS}/SEO:GEO B&M Business"
  "ccc|${PROJECTS}/Cemini claude code CCC"
  "cybersec|${PROJECTS}/Cybersecurity wiki"
  "gambling|${PROJECTS}/Gambling wiki"
  "game-dev|${PROJECTS}/Game Dev wiki"
  "image-gen|${PROJECTS}/Image gen"
  "3d-printing|$(resolve_3d_printing_repo)"
)

ensure_desktop_inbox_symlink() {
  local canonical_root="$1"
  local canonical_inbox="${canonical_root}/research to be indexed"
  local desktop_inbox="${DESKTOP_OSINT}/research to be indexed"

  mkdir -p "$canonical_inbox"
  [[ -d "$DESKTOP_OSINT" ]] || return 0

  if [[ -L "$desktop_inbox" ]]; then
    echo "  Desktop inbox symlink already present"
    return 0
  fi
  if [[ -d "$desktop_inbox" && ! -L "$desktop_inbox" ]]; then
    echo "WARN: ${desktop_inbox} exists as a real directory — not replacing with symlink" >&2
    return 0
  fi
  ln -s "$canonical_inbox" "$desktop_inbox"
  echo "  ${desktop_inbox} → ${canonical_inbox}"
}

mkdir -p "$BIN_DIR" "$CEMINI_DIR" "$PATHS_DIR" "$HOME/Library/Logs"

sync_launchagent_payload() {
  echo "=== Sync ~/.cemini/launchagent payload (launchd-safe, not Desktop) ==="
  mkdir -p "$PAYLOAD_DIR/osint" "$PAYLOAD_DIR/federation"
  cp "$WRAPPER_SRC/_python3.sh" "$PAYLOAD_DIR/_python3.sh"
  chmod 644 "$PAYLOAD_DIR/_python3.sh"
  cp "$ROOT/scripts/verify_wiki_sync.sh" "$PAYLOAD_DIR/osint/verify_wiki_sync.sh"
  cp "$ROOT/scripts/inbox_notify.sh" "$PAYLOAD_DIR/osint/inbox_notify.sh"
  cp "$ROOT/scripts/daily_research_digest_run.py" "$PAYLOAD_DIR/osint/daily_research_digest_run.py"
  cp "$ROOT/scripts/daily_research_fetch.py" "$PAYLOAD_DIR/osint/daily_research_fetch.py"
  cp "$ROOT/scripts/arxiv_api_search.py" "$PAYLOAD_DIR/osint/arxiv_api_search.py"
  cp "$ROOT/scripts/wiki_source_index.py" "$PAYLOAD_DIR/osint/wiki_source_index.py"
  cp "$ROOT/scripts/agent_reach_daily_social.py" "$PAYLOAD_DIR/osint/agent_reach_daily_social.py"
  rm -rf "$PAYLOAD_DIR/osint/agent_reach_wrapper"
  cp -R "$ROOT/scripts/agent_reach_wrapper" "$PAYLOAD_DIR/osint/agent_reach_wrapper"
  chmod 755 "$PAYLOAD_DIR/osint/"*.sh
  chmod 644 "$PAYLOAD_DIR/osint/"*.py
  if [[ -f "$FED_HUB/scripts/run_federation_morning_summary.py" ]]; then
    cp "$FED_HUB/scripts/run_federation_morning_summary.py" \
      "$PAYLOAD_DIR/federation/run_federation_morning_summary.py"
    chmod 644 "$PAYLOAD_DIR/federation/run_federation_morning_summary.py"
  else
    echo "WARN: federation hub script missing — skip federation payload" >&2
  fi
  echo "  $PAYLOAD_DIR"
}

install_wrapper() {
  local name="$1"
  local src="$WRAPPER_SRC/${name}.sh"
  local dest="$BIN_DIR/${name}"
  if [[ ! -f "$src" ]]; then
    echo "ERROR: missing $src" >&2
    exit 1
  fi
  cp "$src" "$dest"
  chmod 755 "$dest"
  echo "  $dest"
}

write_path() {
  local file="$1"
  local dir="$2"
  printf '%s\n' "$dir" > "$file"
  chmod 600 "$file"
}

bootstrap_agent() {
  local label="$1"
  shift
  local -a prog=("$@")
  local plist="$AGENT_DIR/${label}.plist"

  launchctl bootout "gui/$(id -u)/${label}" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$plist"
  launchctl enable "gui/$(id -u)/${label}"
}

write_calendar_plist() {
  local label="$1"
  local program="$2"
  local hour="$3"
  local minute="$4"
  local log_key="$5"
  local plist="$AGENT_DIR/${label}.plist"
  local log_file="${HOME}/Library/Logs/${log_key}.log"

  cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${program}</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>${hour}</integer>
    <key>Minute</key>
    <integer>${minute}</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>${log_file}</string>
  <key>StandardErrorPath</key>
  <string>${log_file}</string>
  <key>LimitLoadToSessionType</key>
  <string>Aqua</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF
  bootstrap_agent "$label"
  echo "  $plist"
}

write_interval_plist() {
  local label="$1"
  local program="$2"
  local interval="$3"
  local log_key="$4"
  local plist="$AGENT_DIR/${label}.plist"
  local log_file="${HOME}/Library/Logs/${log_key}.log"

  cat > "$plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${program}</string>
  </array>
  <key>StartInterval</key>
  <integer>${interval}</integer>
  <key>StandardOutPath</key>
  <string>${log_file}</string>
  <key>StandardErrorPath</key>
  <string>${log_file}</string>
  <key>LimitLoadToSessionType</key>
  <string>Aqua</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF
  bootstrap_agent "$label"
  echo "  $plist"
}

echo "=== OSINT workspace path ==="
sync_launchagent_payload
bash "$ROOT/scripts/federation/daily_digest/sync_federation_digest_bundle.sh"
write_path "$CEMINI_DIR/osint-workspace.path" "$ROOT"
ensure_desktop_inbox_symlink "$ROOT"

echo "=== Federation hub path ==="
write_path "$CEMINI_DIR/federation-hub.path" "${PROJECTS}/cemini-federation-hub"

echo "=== Installing ~/bin wrappers ==="
install_wrapper cemini-daily-research-digest
cp "$WRAPPER_SRC/cemini-daily-research-digest.sh" "$BIN_DIR/cemini-daily-research-digest"
chmod 755 "$BIN_DIR/cemini-daily-research-digest"
echo "  $BIN_DIR/cemini-daily-research-digest"
install_wrapper cemini-wiki-sync-verify
install_wrapper cemini-federation-morning-summary
install_wrapper cemini-daily-research-digest-wiki
# wiki-ingester disabled by default (Grok Build weekly quota / HITL). Re-enable:
#   mv ~/Library/LaunchAgents/com.cemini.wiki-ingester.plist.disabled-* ~/Library/LaunchAgents/com.cemini.wiki-ingester.plist
#   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cemini.wiki-ingester.plist
# Or: CEMINI_ENABLE_WIKI_INGESTER=1 bash scripts/reinstall_morning_launchagents.sh
if [[ "${CEMINI_ENABLE_WIKI_INGESTER:-0}" == "1" ]]; then
  install_wrapper cemini-wiki-ingester
fi

echo "=== Federated wiki paths + digest bins ==="
FED_TEMPLATE="$BIN_DIR/cemini-daily-research-digest-wiki"
for entry in "${WIKI_REPOS[@]}"; do
  id="${entry%%|*}"
  repo="${entry#*|}"
  if [[ ! -d "$repo" ]]; then
    echo "WARN: skip $id — missing $repo" >&2
    continue
  fi
  mkdir -p "${repo}/research to be indexed"
  write_path "$PATHS_DIR/${id}.path" "$repo"
  dest="$BIN_DIR/cemini-daily-research-digest-${id}"
  cp "$FED_TEMPLATE" "$dest"
  chmod 755 "$dest"
  echo "  $id → $repo"
done

echo "=== LaunchAgents (reload) ==="
# OSINT first @ 08:00. Sibling digests stagger +3min each (avoid arXiv 429 herd).
# Federation summary after last sibling (~08:28) so hub table sees today's sweeps.
write_calendar_plist com.cemini.daily-research-digest "$BIN_DIR/cemini-daily-research-digest" 8 0 cemini-daily-digest

fed_minute=10
for entry in "${WIKI_REPOS[@]}"; do
  id="${entry%%|*}"
  [[ -f "$PATHS_DIR/${id}.path" ]] || continue
  write_calendar_plist "com.cemini.daily-research-digest.${id}" \
    "$BIN_DIR/cemini-daily-research-digest-${id}" 8 "$fed_minute" cemini-daily-digest
  echo "  schedule ${id} → 08:$(printf '%02d' "$fed_minute")"
  fed_minute=$((fed_minute + 3))
done

write_calendar_plist com.cemini.federation-morning-summary \
  "$BIN_DIR/cemini-federation-morning-summary" 8 "$fed_minute" cemini-federation-summary
echo "  schedule federation-morning-summary → 08:$(printf '%02d' "$fed_minute")"

# Headless Grok CLI ingest (not Grok Bot GUI). Disabled by default — Grok Build quota + HITL.
if [[ "${CEMINI_ENABLE_WIKI_INGESTER:-0}" == "1" ]]; then
  write_calendar_plist com.cemini.wiki-ingester \
    "$BIN_DIR/cemini-wiki-ingester" 9 0 cemini-wiki-ingester
  echo "  schedule wiki-ingester (Grok CLI) → 09:00"
else
  launchctl bootout "gui/$(id -u)/com.cemini.wiki-ingester" 2>/dev/null || true
  if [[ -f "$AGENT_DIR/com.cemini.wiki-ingester.plist" ]]; then
    disabled="$AGENT_DIR/com.cemini.wiki-ingester.plist.disabled-$(date +%Y%m%d)"
    if [[ ! -f "$disabled" ]]; then
      mv "$AGENT_DIR/com.cemini.wiki-ingester.plist" "$disabled" 2>/dev/null || true
    fi
  fi
  echo "  skip wiki-ingester (set CEMINI_ENABLE_WIKI_INGESTER=1 to install)"
fi

# Inbox watch (unchanged pattern — script on Desktop is OK for WatchPaths trigger? use wrapper)
INBOX="$ROOT/research to be indexed"
cat > "$AGENT_DIR/com.cemini.inbox-notify.plist" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.cemini.inbox-notify</string>
  <key>ProgramArguments</key>
  <array>
    <string>${BIN_DIR}/cemini-inbox-notify</string>
  </array>
  <key>WatchPaths</key>
  <array>
    <string>${INBOX}</string>
  </array>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/cemini-inbox-watch.log</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/cemini-inbox-watch.log</string>
  <key>LimitLoadToSessionType</key>
  <string>Aqua</string>
  <key>RunAtLoad</key>
  <false/>
</dict>
</plist>
EOF

# inbox wrapper — payload under ~/.cemini (not Desktop)
cat > "$BIN_DIR/cemini-inbox-notify" <<'INBOX_EOF'
#!/usr/bin/env bash
set -uo pipefail
REPO_FILE="${HOME}/.cemini/osint-workspace.path"
LOG_FILE="${HOME}/Library/Logs/cemini-inbox-watch.log"
ROOT="$(tr -d '\r\n' < "${REPO_FILE}")"
export PATH="/opt/homebrew/bin:/usr/local/bin:${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
cd "${ROOT}" || exit 1
export CEMINI_OSINT_ROOT="${ROOT}"
bash -s < "${HOME}/.cemini/launchagent/osint/inbox_notify.sh" 2>&1 | tee -a "$LOG_FILE"
exit "${PIPESTATUS[0]}"
INBOX_EOF
chmod 755 "$BIN_DIR/cemini-inbox-notify"
bootstrap_agent com.cemini.inbox-notify
echo "  com.cemini.inbox-notify.plist"

# wiki-sync-verify targeted cemini-librarian (decommissioned 2026-06-14) — keep unloaded.
if launchctl print "gui/$(id -u)/com.cemini.wiki-sync-verify" &>/dev/null; then
  launchctl bootout "gui/$(id -u)/com.cemini.wiki-sync-verify" 2>/dev/null || true
fi
if [[ -f "$AGENT_DIR/com.cemini.wiki-sync-verify.plist" ]]; then
  mv -f "$AGENT_DIR/com.cemini.wiki-sync-verify.plist" \
    "$AGENT_DIR/com.cemini.wiki-sync-verify.plist.disabled"
  echo "  disabled com.cemini.wiki-sync-verify (librarian offline)"
fi

# WC LP safety — RETIRED 2026-07-28 (World Cup over / world-cup-bot dropped)
if launchctl print "gui/$(id -u)/com.cemini.wc-lp-safety-reminder" &>/dev/null; then
  launchctl bootout "gui/$(id -u)/com.cemini.wc-lp-safety-reminder" 2>/dev/null || true
fi
if [[ -f "$AGENT_DIR/com.cemini.wc-lp-safety-reminder.plist" ]]; then
  mv -f "$AGENT_DIR/com.cemini.wc-lp-safety-reminder.plist" \
    "$AGENT_DIR/com.cemini.wc-lp-safety-reminder.plist.disabled"
  echo "  disabled com.cemini.wc-lp-safety-reminder (WC LP cadence retired)"
fi

# Weekly agents still call scripts via stdin wrappers
for pair in "com.cemini.wiki-gap-detect:run_wiki_gap_detect.sh"; do
  label="${pair%%:*}"
  script="${pair##*:}"
  bin="$BIN_DIR/${label##com.cemini.}"
  cat > "$bin" <<WRAP
#!/usr/bin/env bash
set -uo pipefail
REPO_FILE="\${HOME}/.cemini/osint-workspace.path"
ROOT="\$(tr -d '\r\n' < "\${REPO_FILE}")"
export PATH="/opt/homebrew/bin:/usr/local/bin:\${PATH:-/usr/bin:/bin:/usr/sbin:/sbin}"
cd "\${ROOT}" || exit 1
bash -s < "\${ROOT}/scripts/${script}" 
WRAP
  chmod 755 "$bin"
  write_interval_plist "$label" "$bin" "$WEEKLY" cemini-workflow
done

echo ""
echo "Done. Logs: ~/Library/Logs/cemini-{daily-digest,federation-summary,wiki-sync,inbox-watch,workflow,wiki-ingester}.log"
echo ""
echo "macOS TCC: Full Disk Access on Cursor or /bin/bash does NOT cover launchd jobs."
echo "  Wrappers run from ~/bin; scripts/python from ~/.cemini/launchagent/."
echo "  If digest still fails at 08:00 while logged out, add FDA to:"
echo "    $(/Library/Developer/CommandLineTools/usr/bin/python3 -c 'import sys; print(sys.executable)' 2>/dev/null || echo '/Library/Developer/CommandLineTools/usr/bin/python3')"
echo "  Scheduled 08:00 runs use Aqua session; launchctl kickstart may still fail without FDA."

if [[ "$BACKFILL" -eq 1 ]]; then
  echo ""
  echo "=== Backfill today ==="
  "$BIN_DIR/cemini-federation-morning-summary" || true
  for entry in "${WIKI_REPOS[@]}"; do
    id="${entry%%|*}"
    [[ -x "$BIN_DIR/cemini-daily-research-digest-${id}" ]] || continue
    echo "--- $id ---"
    "$BIN_DIR/cemini-daily-research-digest-${id}" || true
  done
fi
