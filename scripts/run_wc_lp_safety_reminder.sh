#!/usr/bin/env bash
# run_wc_lp_safety_reminder.sh — weekly LP safety DR reminder (K84 workflow).
#
# Logs checklist + prompt path. Does NOT auto-run Gemini (operator-gated).
# Updates cadence meta last_run on execution.
#
# Usage:
#   bash scripts/run_wc_lp_safety_reminder.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY=$(date +%Y-%m-%d)
LOG="$HOME/Library/Logs/cemini-wc-lp-safety.log"
PROMPT="/Users/claudiobarone/Desktop/projects/world-cup-bot/prompts/gemini-deep-research/03-team-lp-risk.md"
META="$ROOT/wiki/meta/wc-lp-safety-cadence.md"

mkdir -p "$(dirname "$LOG")"
mkdir -p "$ROOT/.local/reports"

{
  echo "[$TODAY] WC LP safety re-run reminder"
  echo "  Prompt: $PROMPT"
  echo "  Teams (K84 gates): Spain skip | Brazil reduce | Morocco human_review"
  echo "  After DR: update world-cup-bot config/conviction.yaml + prod pull"
  echo "  Canvas: wc-lp-safety-k84 (Issue 3 prep — no static mids in copy)"
  echo "  Wiki: sources/gemini-wc-lp-team-safety-assessments-2026-05-30.md"
} | tee -a "$LOG"

if [[ -f "$PROMPT" ]]; then
  echo "  Prompt exists ($(wc -l < "$PROMPT" | tr -d ' ') lines)" | tee -a "$LOG"
else
  echo "  WARN: prompt not found at $PROMPT" | tee -a "$LOG"
fi

# Bump cadence
if [[ -f "$META" ]]; then
  NEXT=$(date -v+7d +%Y-%m-%d 2>/dev/null || date -d "+7 days" +%Y-%m-%d)
  sed -i.bak "s/| \*\*Last run\*\* | .*/| **Last run** | ${TODAY} |/" "$META"
  sed -i.bak "s/| \*\*Next due\*\* | .*/| **Next due** | ${NEXT} |/" "$META"
  rm -f "${META}.bak"
fi

WEBHOOK="$HOME/.cemini/inbox-webhook.url"
if [[ -f "$WEBHOOK" ]]; then
  url=$(tr -d '[:space:]' < "$WEBHOOK")
  msg="WC LP safety DR due ($TODAY) — run 03-team-lp-risk.md before updating conviction.yaml"
  curl -sS -X POST -H 'Content-Type: application/json' \
    -d "$(python3 -c "import json; print(json.dumps({'text': '''$msg'''}))")" "$url" >> "$LOG" 2>&1 || true
fi

exit 0
