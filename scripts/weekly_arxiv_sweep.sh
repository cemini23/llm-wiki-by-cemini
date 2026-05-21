#!/usr/bin/env bash
# weekly_arxiv_sweep.sh
#
# Tier 2 of the proactive-search design (per @concepts/high-signal-paper-patterns.md).
# Fires 5 cluster-aligned queries against Exa's /search REST API, scoped to the
# last 14 days, category=research paper. Writes a candidate report to
# wiki/sweeps/YYYY-MM-DD.md for the next Claude Code session to triage.
#
# DOES NOT INGEST. Tier 2 is user-gated-commit: the LLM presents candidates;
# the user approves; the LLM ingests selected items.
#
# WHY: matches the workflow used in the manual Workflow A run on 2026-04-29
# that surfaced 4 high-signal papers (LOB regime detection, MoE Efficiency
# Leverage, MoE-Surpass-Dense, LBS/Yale Polymarket) — all rubric-passing.
# See @sources/lob-regime-detection-hiremath-2026.md et al for outcomes.
#
# ONE-TIME SETUP REQUIRED before cron-enabling this script:
#   1. Get your Exa API key from https://dashboard.exa.ai
#   2. Either set EXA_API_KEY in your shell environment (~/.zshrc) and
#      reference it from the cron entry, OR drop the key to a file:
#        mkdir -p ~/.cemini && chmod 700 ~/.cemini
#        echo 'YOUR_EXA_API_KEY' > ~/.cemini/exa-api-key
#        chmod 600 ~/.cemini/exa-api-key
#   3. Test manually:  ./scripts/weekly_arxiv_sweep.sh
#   4. Verify the report in wiki/sweeps/YYYY-MM-DD.md
#   5. Add the cron entry (laptop crontab — macOS):
#        0 8 * * 0 "/Users/claudiobarone/Desktop/OSINT WORKSPACE/scripts/weekly_arxiv_sweep.sh"
#      (Fires Sunday 08:00 EDT = 12:00 UTC, after the librarian snapshot fires
#      at 03:32 UTC. macOS cron does not run while the laptop sleeps; the next
#      sweep fires whenever the laptop next wakes after the trigger time.)
#
# Cost: ~$0.25/sweep (5 advanced searches × ~$0.05 each, per the 2026-04-29
# Workflow A manual run).
#
# Exit codes:
#   0 — sweep completed successfully (any number of candidates is fine)
#   1 — Exa API key missing or unreadable
#   2 — date(1) flag detection failed (need GNU date or BSD date)
#   3 — at least one query failed; report written but partial
#   4 — failed to write the report file

set -uo pipefail

# --- 1. Locate the Exa API key -----------------------------------------------

EXA_KEY=""
if [[ -n "${EXA_API_KEY:-}" ]]; then
  EXA_KEY="$EXA_API_KEY"
elif [[ -r "$HOME/.cemini/exa-api-key" ]]; then
  EXA_KEY=$(cat "$HOME/.cemini/exa-api-key")
fi

if [[ -z "$EXA_KEY" ]]; then
  echo "ERROR: Exa API key not found. Set EXA_API_KEY env var or write the key to ~/.cemini/exa-api-key" >&2
  echo "See script header for one-time setup instructions." >&2
  exit 1
fi

# --- 2. Compute date window (last 14 days) ----------------------------------

# Try GNU date first (Linux), then BSD date (macOS)
if FROM_DATE=$(date -d "14 days ago" +%Y-%m-%d 2>/dev/null); then
  : # GNU date worked
elif FROM_DATE=$(date -v -14d +%Y-%m-%d 2>/dev/null); then
  : # BSD date worked
else
  echo "ERROR: cannot compute date (neither GNU date -d nor BSD date -v worked)" >&2
  exit 2
fi
TODAY=$(date +%Y-%m-%d)

# --- 3. Set up paths ---------------------------------------------------------

REPO=$(cd "$(dirname "$0")/.." && pwd)
SWEEPS_DIR="$REPO/wiki/sweeps"
mkdir -p "$SWEEPS_DIR"
REPORT_FILE="$SWEEPS_DIR/${TODAY}.md"
LOG_FILE="$HOME/Library/Logs/cemini-arxiv-sweep.log"
mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE" >&2
}

log "Starting weekly arXiv sweep"
log "  date window: $FROM_DATE → $TODAY (14 days)"
log "  report file: $REPORT_FILE"

# --- 4. Define the 5 cluster queries -----------------------------------------

declare -a QUERY_LABELS=(
  "agent-harness"
  "options-pricing"
  "moe-scaling-parameter-estimation"
  "financial-rl-multi-agent"
  "prediction-markets-microstructure"
)

declare -a QUERY_TEXTS=(
  "research paper on coding agent harness optimization, LLM agent orchestration framework, or autonomous agent observability"
  "research paper presenting closed-form solution or computational breakthrough in options pricing, implied volatility, or Greeks calculation"
  "research paper on mixture of experts scaling laws, LLM parameter count estimation, or DeepSeek model evaluation"
  "research paper on reinforcement learning for algorithmic trading, multi-agent financial systems, or RL portfolio optimization"
  "research paper on prediction market microstructure, event contract pricing, Kalshi or Polymarket order-book analysis"
)

# --- 5–6. Run Exa queries and write report (Python — avoids bash quoting bugs) -

set +e
python3 "$REPO/scripts/arxiv_sweep_run.py" 2>&1 | tee -a "$LOG_FILE"
SWEEP_RC=${PIPESTATUS[0]}
set -e

if [[ ! -f "$REPORT_FILE" ]]; then
  log "ERROR: report file missing after arxiv_sweep_run.py"
  exit 4
fi

# --- 7. Done -----------------------------------------------------------------

if [[ "$SWEEP_RC" -eq 3 ]]; then
  log "Sweep completed with partial failures"
  log "Report written: $REPORT_FILE"
  exit 3
fi
if [[ "$SWEEP_RC" -ne 0 ]]; then
  log "Sweep failed (exit $SWEEP_RC)"
  exit "$SWEEP_RC"
fi
log "Sweep completed successfully"
log "Report written: $REPORT_FILE"
exit 0
