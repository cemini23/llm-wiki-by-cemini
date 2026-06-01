#!/usr/bin/env bash
# daily_research_digest.sh
#
# Daily digest: Exa research papers (wiki-deduped) → inbox PDFs + news sweep report.
# Does NOT ingest wiki — morning "full ingest" in Cursor handles that.
#
# Complements weekly_arxiv_sweep.sh (papers, 14d window) with broader
# news/web coverage (7d window) aligned to ROADMAP active topics.
#
# ONE-TIME SETUP:
#   1. Exa key: EXA_API_KEY env or ~/.cemini/exa-api-key (same as arxiv sweep)
#   2. Test:     ./scripts/daily_research_digest.sh
#   3. Schedule:  bash scripts/install_workflow_launchagents.sh
#      (adds com.cemini.daily-research-digest @ 08:00 via ~/bin wrapper)
#   Manual (any cwd): cemini-daily-research-digest
#
# Cost: ~$0.15/day (5 queries × 3 hits).
#
# Exit codes:
#   0 — digest completed
#   1 — Exa API key missing
#   3 — partial Exa failures (report still written)
#   4 — report file missing after run

set -uo pipefail

REPO=$(cd "$(dirname "$0")/.." && pwd)
LOG_FILE="$HOME/Library/Logs/cemini-daily-digest.log"
TODAY=$(date +%Y-%m-%d)
REPORT="$REPO/wiki/sweeps/${TODAY}-daily.md"

mkdir -p "$(dirname "$LOG_FILE")"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE" >&2
}

log "Starting daily research digest"

set +e
python3 "$REPO/scripts/daily_research_digest_run.py" 2>&1 | tee -a "$LOG_FILE"
DIGEST_RC=${PIPESTATUS[0]}
set -e

if [[ ! -f "$REPORT" ]]; then
  log "ERROR: report missing after daily_research_digest_run.py"
  exit 4
fi

if [[ "$DIGEST_RC" -eq 3 ]]; then
  log "Digest completed with partial Exa failures"
  log "Report: $REPORT"
  exit 3
fi
if [[ "$DIGEST_RC" -ne 0 ]]; then
  log "Digest failed (exit $DIGEST_RC)"
  exit "$DIGEST_RC"
fi

log "Digest completed successfully"
log "Report: $REPORT"
exit 0
