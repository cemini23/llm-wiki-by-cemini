#!/usr/bin/env bash
# Fast pre-deploy gate (~30–60s) — regression spots + dry-run only.
#
# Use after a full preflight passed recently, or for small decide() patches:
#   ./scripts/cemini_preflight_fast.sh
# Full gate (anti-profiling 400h + self-play 250h) remains:
#   ./scripts/cemini_preflight.sh
set -euo pipefail
cd "$(dirname "$0")/.."

STAMP="${CEMINI_PREFLIGHT_STAMP:-reports/hl-loop/preflight_ok.timestamp}"
MAX_AGE_HOURS="${CEMINI_PREFLIGHT_MAX_AGE_HOURS:-24}"

if [[ -f "${STAMP}" ]]; then
  age_s=$(( $(date +%s) - $(stat -f %m "${STAMP}" 2>/dev/null || stat -c %Y "${STAMP}") ))
  if (( age_s < MAX_AGE_HOURS * 3600 )); then
    echo "==> Full preflight OK ${age_s}s ago (<${MAX_AGE_HOURS}h) — fast path"
  fi
fi

echo "==> [1/2] pytest regression spots only"
uv run python -m pytest tests/test_cemini_regression.py tests/test_cemini_nuts.py -q --tb=short

echo ""
echo "==> [2/2] dry-run lobby path (no network)"
uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 15

echo ""
echo "PREFLIGHT FAST OK — safe for code-only deploy."
