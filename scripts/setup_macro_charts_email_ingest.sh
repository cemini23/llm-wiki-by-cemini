#!/usr/bin/env bash
# setup_macro_charts_email_ingest.sh — Macro Charts RSS (free) + Gmail (paid forwards).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT_DIR="$HOME/Library/LaunchAgents"
EMAIL_LABEL="com.cemini.macro-charts-email-poller"
RSS_LABEL="com.cemini.substack-rss-poller"
LEGACY_RSS_LABEL="com.cemini.macro-charts-rss-poller"
EMAIL_INTERVAL=900   # 15 min
RSS_INTERVAL=1800    # 30 min
COUSIN_EMAIL="vinnyb64@gmail.com"

echo "=== Macro Charts + Substack RSS ingest setup ==="
echo ""
echo "Config:"
echo "  RSS feeds:  $ROOT/config/substack-rss-ingest.yaml"
echo "  Gmail paid: $ROOT/config/macro-charts-ingest.yaml"
echo "  Free posts  → Substack RSS poller (every ${RSS_INTERVAL}s)"
echo "  Paid posts  → Vincent (${COUSIN_EMAIL}) Gmail forwards (every ${EMAIL_INTERVAL}s)"
echo ""

echo "1) Gmail labels (Settings → Labels → Create):"
echo "   - Cemini/Macro-Charts"
echo "   - Cemini/Macro-Charts/processed"
echo ""
echo "2) Gmail filter (Settings → Filters → Create):"
echo "   From:    ${COUSIN_EMAIL}"
echo "   Has the words: macrocharts OR \"Macro Charts\" OR macrocharts.com"
echo "   Actions: Apply label Cemini/Macro-Charts"
echo ""
echo "   Vincent's non-Macro-Charts mail stays out of the pipeline."
echo ""
read -r -p "Press Enter after Gmail filter is saved…" _

echo ""
echo "3) Google Cloud OAuth for Gmail poller (one-time):"
echo "   - https://console.cloud.google.com/apis/credentials"
echo "   - Create OAuth client → Desktop app"
echo "   - Enable Gmail API"
echo "   - Download JSON → ~/.cemini/gmail-oauth-client.json"
echo ""
if [[ ! -f "$HOME/.cemini/gmail-oauth-client.json" ]]; then
  echo "WARN: ~/.cemini/gmail-oauth-client.json not found yet."
else
  echo "OK: found gmail-oauth-client.json"
fi
read -r -p "Press Enter when OAuth client JSON is in place (or skip email for now)…" _

echo ""
echo "4) Python deps:"
pip3 install --user pyyaml google-api-python-client google-auth-httplib2 google-auth-oauthlib 2>/dev/null || \
  pip3 install pyyaml google-api-python-client google-auth-httplib2 google-auth-oauthlib
echo ""

chmod +x "$ROOT/scripts/run_macro_charts_email_poller.sh"
chmod +x "$ROOT/scripts/run_macro_charts_rss_poller.sh"
chmod +x "$ROOT/scripts/run_substack_rss_poller.sh"
chmod +x "$ROOT/scripts/macro_charts_email_poller.py"
chmod +x "$ROOT/scripts/macro_charts_rss_poller.py"
chmod +x "$ROOT/scripts/substack_rss_poller.py"

echo "5) RSS dry-run (no OAuth needed):"
python3 "$ROOT/scripts/substack_rss_poller.py" --dry-run || true
echo ""
echo "6) Email dry-run (OAuth browser on first run):"
if [[ -f "$HOME/.cemini/gmail-oauth-client.json" ]]; then
  python3 "$ROOT/scripts/gmail_macro_charts_bootstrap.py" || true
  python3 "$ROOT/scripts/macro_charts_email_poller.py" --dry-run || true
else
  echo "Skipping email bootstrap — place OAuth client at ~/.cemini/gmail-oauth-client.json then run:"
  echo "  python3 scripts/gmail_macro_charts_bootstrap.py"
fi
echo ""

install_interval_agent() {
  local label="$1"
  local script="$2"
  local interval="$3"
  local log_name="$4"
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
  <key>StartInterval</key>
  <integer>${interval}</integer>
  <key>StandardOutPath</key>
  <string>${HOME}/Library/Logs/${log_name}</string>
  <key>StandardErrorPath</key>
  <string>${HOME}/Library/Logs/${log_name}</string>
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

echo "Installing LaunchAgents…"
launchctl bootout "gui/$(id -u)/${LEGACY_RSS_LABEL}" 2>/dev/null || true
install_interval_agent "$RSS_LABEL" "run_substack_rss_poller.sh" "$RSS_INTERVAL" "cemini-substack-rss.log"
install_interval_agent "$EMAIL_LABEL" "run_macro_charts_email_poller.sh" "$EMAIL_INTERVAL" "cemini-macro-charts-email.log"

echo ""
echo "Done."
echo "  RSS log:   ~/Library/Logs/cemini-substack-rss.log"
echo "  Email log: ~/Library/Logs/cemini-macro-charts-email.log"
echo ""
echo "Manual: bash scripts/run_substack_rss_poller.sh"
echo "        bash scripts/run_macro_charts_email_poller.sh"
echo ""
echo "Ingest in Cursor: prefer macro-charts-paid-forward-* over macro-charts-rss-* for same issue."
