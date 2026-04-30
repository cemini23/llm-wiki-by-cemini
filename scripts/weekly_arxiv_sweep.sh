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

# --- 5. Run queries via Exa /search REST API ---------------------------------

# We accumulate JSON results in a temp dir, then process all together with python
# at the end to produce the Markdown report.

TMPDIR_=$(mktemp -d)
trap 'rm -rf "$TMPDIR_"' EXIT

PARTIAL_FAIL=0
for i in "${!QUERY_LABELS[@]}"; do
  label="${QUERY_LABELS[$i]}"
  query="${QUERY_TEXTS[$i]}"
  out="$TMPDIR_/${i}_${label}.json"
  log "  Q$((i+1)) ($label): firing query"
  http_status=$(curl -s -m 60 -o "$out" -w "%{http_code}" \
    -X POST "https://api.exa.ai/search" \
    -H "Authorization: Bearer $EXA_KEY" \
    -H "Content-Type: application/json" \
    -d "$(python3 -c "
import json, sys
print(json.dumps({
    'query': sys.argv[1],
    'category': 'research paper',
    'startPublishedDate': sys.argv[2],
    'numResults': 5,
    'type': 'auto',
}))
" "$query" "$FROM_DATE")")
  if [[ "$http_status" != "200" ]]; then
    log "    WARNING: Q$((i+1)) returned HTTP $http_status (continuing)"
    PARTIAL_FAIL=1
    # Write a stub so the report still has something for this query
    echo "{\"results\":[],\"_error\":\"http_$http_status\"}" > "$out"
  else
    n=$(python3 -c "import json; d=json.load(open('$out')); print(len(d.get('results',[])))" 2>/dev/null || echo "0")
    log "    Q$((i+1)) returned $n results"
  fi
done

# --- 6. Process JSON → Markdown report ---------------------------------------

# We use python for this; bash + jq is too brittle for the URL/title cleanup
# the report needs.

python3 - <<EOF >"$REPORT_FILE" || { log "ERROR: failed to write report file"; exit 4; }
import json
from pathlib import Path
from datetime import date

tmpdir = Path("$TMPDIR_")
labels = ["agent-harness", "options-pricing", "moe-scaling-parameter-estimation",
          "financial-rl-multi-agent", "prediction-markets-microstructure"]
queries = ${QUERY_TEXTS[@]@Q}.split('\\n') if False else [
${QUERY_TEXTS[0]@Q}.replace("\\n",""),
${QUERY_TEXTS[1]@Q}.replace("\\n",""),
${QUERY_TEXTS[2]@Q}.replace("\\n",""),
${QUERY_TEXTS[3]@Q}.replace("\\n",""),
${QUERY_TEXTS[4]@Q}.replace("\\n",""),
]
today = "$TODAY"
from_date = "$FROM_DATE"

print(f"# Tier-2 arXiv sweep — {today}")
print()
print(f"Date window: \`{from_date}\` → \`{today}\` (14 days). Category: \`research paper\`. \`numResults=5\` per query.")
print()
print(f"Reference rubric: see \`@concepts/high-signal-paper-patterns.md\`. Tier-2 is descriptive only — this report does NOT ingest. Decide which candidates to act on, then ask the LLM in the next session.")
print()
print("---")
print()

total_results = 0
for i, label in enumerate(labels):
    fp = tmpdir / f"{i}_{label}.json"
    if not fp.exists():
        continue
    try:
        d = json.load(fp.open())
    except Exception as e:
        print(f"## Q{i+1}: {label} — ERROR: {e}\\n")
        continue
    if d.get("_error"):
        print(f"## Q{i+1}: {label} — ERROR: {d['_error']}\\n")
        continue
    results = d.get("results", [])
    print(f"## Q{i+1}: {label} ({len(results)} results)")
    print()
    print(f"Query: \`{queries[i] if i<len(queries) else label}\`")
    print()
    for r in results:
        url = r.get("url", "")
        title = (r.get("title") or "").strip()
        if not title:
            text = r.get("text", "") or ""
            for line in text.splitlines():
                line = line.strip()
                if 30 <= len(line) <= 200 and not line.startswith("[") and not line.startswith("#"):
                    title = line
                    break
        date_str = (r.get("publishedDate") or "")[:10]
        print(f"- **[{date_str}]** [{title[:160]}]({url})")
        # Try to find an arXiv ID in the URL
        import re
        m = re.search(r'arxiv\\.org/(abs|pdf|html)/(\\d{4}\\.\\d{4,5})', url)
        if m:
            arxiv_id = m.group(2)
            print(f"  - arXiv ID: \`{arxiv_id}\` — preingest_check.py will dedupe automatically on next ingest")
    print()
    total_results += len(results)

print("---")
print()
print(f"## Sweep summary")
print()
print(f"Total candidates: **{total_results}** across 5 queries.")
print()
print(f"### Next steps (per Tier-2 user-gated-commit pattern)")
print()
print(f"1. **LLM**: in the next session, score each candidate against \`@concepts/high-signal-paper-patterns.md\` rubric (3 filters / 6 quality / 3 operational signals).")
print(f"2. **LLM**: dedupe via \`scripts/preingest_check.py\` against the existing wiki.")
print(f"3. **LLM**: present a ranked candidate list (Tier-A / Tier-B / Skip) to the user.")
print(f"4. **User**: approve which to ingest.")
print(f"5. **LLM**: download PDFs (where available), ingest each per the standard CLAUDE.md workflow.")
print()
print(f"### How to discard this sweep")
print()
print(f"If nothing in this sweep looks promising, just delete this file: \`rm wiki/sweeps/{today}.md\`. The cost is amortized; no follow-up needed.")
EOF

# --- 7. Done -----------------------------------------------------------------

if [[ "$PARTIAL_FAIL" -eq 1 ]]; then
  log "Sweep completed with partial failures (some queries returned non-200)"
  log "Report written: $REPORT_FILE"
  exit 3
fi
log "Sweep completed successfully"
log "Report written: $REPORT_FILE"
exit 0
