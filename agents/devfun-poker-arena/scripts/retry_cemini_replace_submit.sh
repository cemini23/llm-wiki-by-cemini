#!/usr/bin/env bash
# Retry cemini --replace submit until daily limit clears or success.
# Run on prod: bash scripts/retry_cemini_replace_submit.sh
set -euo pipefail
cd "$(dirname "$0")/.."
COMP="${ARENA_RESEARCHER_COMP_ID:-cmr0jmqlt08bi13n8neory9xb}"
LOG="reports/researcher-round/retry-cemini-replace.log"
mkdir -p reports/researcher-round
PY="./venv/bin/python"
[[ -x "$PY" ]] || PY="python3"
INTERVAL="${RETRY_INTERVAL_S:-900}"
MAX="${RETRY_MAX_ATTEMPTS:-96}"

attempt=0
while (( attempt < MAX )); do
  attempt=$((attempt + 1))
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "[$ts] attempt $attempt/$MAX" | tee -a "$LOG"
  set +e
  out="$($PY examples/submit_sandbox_pvp.py --build --replace --competition-id "$COMP" 2>&1)"
  code=$?
  set -e
  echo "$out" | tee -a "$LOG"
  if [[ $code -eq 0 ]]; then
    sid="$(echo "$out" | python3 -c "import sys,re; m=re.search(r'\"id\":\s*\"([^\"]+)\"', sys.stdin.read()); print(m.group(1) if m else '')" 2>/dev/null || true)"
    echo "[$ts] SUCCESS submission=${sid:-unknown}" | tee -a "$LOG"
    if [[ -n "$sid" ]]; then
      python3 - "$sid" <<'PY'
import json, sys
from pathlib import Path
sid = sys.argv[1]
pin_path = Path("config/researcher_sandbox_submit.pin.json")
pin = json.loads(pin_path.read_text())
pin["activeSubmissionId"] = sid
watch = list(pin.get("watchSubmissionIds") or [])
if sid not in watch:
    watch.insert(0, sid)
pin["watchSubmissionIds"] = watch[:5]
pin_path.write_text(json.dumps(pin, indent=2) + "\n")
print(f"Updated pin activeSubmissionId -> {sid}")
PY
    fi
    exit 0
  fi
  if echo "$out" | grep -q sandbox_daily_limit; then
    echo "[$ts] daily limit — sleep ${INTERVAL}s" | tee -a "$LOG"
    sleep "$INTERVAL"
    continue
  fi
  if echo "$out" | grep -q sandbox_agent_already_running; then
    echo "[$ts] agent running — retry replace in ${INTERVAL}s" | tee -a "$LOG"
    sleep "$INTERVAL"
    continue
  fi
  echo "[$ts] FAIL non-retryable exit=$code" | tee -a "$LOG"
  exit "$code"
done
echo "[$ts] exhausted $MAX attempts" | tee -a "$LOG"
exit 1
