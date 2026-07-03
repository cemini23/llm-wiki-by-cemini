#!/usr/bin/env bash
# Retry cemini --replace submit until daily limit clears or success.
# Run on prod: bash scripts/retry_cemini_replace_submit.sh
set -euo pipefail
cd "$(dirname "$0")/.."
COMP="${ARENA_RESEARCHER_COMP_ID:-cmr3n8tft01nilecm1u5jlny7}"
PIN="config/researcher_sandbox_submit.pin.json"
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
  in_flight_msg="$("$PY" -c "
import json, sys
from pathlib import Path
sys.path.insert(0, 'examples')
from researcher_sandbox_auto_submit import _poll_submission_safe, pvp_progress

pin_path = Path('${PIN}')
if not pin_path.is_file():
    sys.exit(0)
pin = json.loads(pin_path.read_text(encoding='utf-8'))
sid = str(pin.get('activeSubmissionId') or '')
if not sid:
    sys.exit(0)
rec = _poll_submission_safe(sid)
if not rec:
    sys.exit(0)
ch, th, status = pvp_progress(rec)
if th > 0 and 0 < ch < th:
    print(f'REFUSE: in-flight PvP {ch}/{th} ({status}) — activeSubmissionId={sid}')
    sys.exit(2)
" 2>&1)"
  in_flight_code=$?
  set -e
  if [[ "${in_flight_code}" -eq 2 ]]; then
    echo "[$ts] ${in_flight_msg}" | tee -a "$LOG"
    exit 0
  fi

  set +e
  out="$($PY examples/submit_sandbox_pvp.py --build --replace --competition-id "$COMP" 2>&1)"
  code=$?
  set -e
  echo "$out" | tee -a "$LOG"
  if [[ $code -eq 0 ]]; then
    sid="$(echo "$out" | python3 -c "import sys,re; m=re.search(r'\"id\":\s*\"([^\"]+)\"', sys.stdin.read()); print(m.group(1) if m else '')" 2>/dev/null || true)"
    echo "[$ts] SUCCESS submission=${sid:-unknown}" | tee -a "$LOG"
    if [[ -n "$sid" ]]; then
      "$PY" -c "
import json, sys
from pathlib import Path
sys.path.insert(0, 'examples')
from researcher_sandbox_auto_submit import sync_pin_from_submission, _git_head_short

sid = sys.argv[1]
pin_path = Path('${PIN}')
pin = json.loads(pin_path.read_text(encoding='utf-8'))
sync_pin_from_submission(
    pin_path,
    pin,
    sid,
    git_commit=_git_head_short(),
    agent_version=str(pin.get('agentVersion') or ''),
)
print(f'Updated pin activeSubmissionId -> {sid}')
" "$sid"
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
