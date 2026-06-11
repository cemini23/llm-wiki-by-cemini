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
CEMINI_GIN_STYLE=0 CEMINI_GIN_STYLE_PREFLOP=0 CEMINI_GIN_STYLE_POSTFLOP=0 \
  uv run python -m pytest tests/test_cemini_regression.py tests/test_cemini_nuts.py -q --tb=short

echo ""
echo "==> [2/3] dry-run lobby path (no network)"
uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 15

if uv run python -c "import os; exit(0 if os.environ.get('CEMINI_GIN_STYLE_GATE','').strip().lower() in ('1','true','yes','on') else 1)" 2>/dev/null; then
  echo ""
  echo "==> [3/3] gin-style gate (VPIP + bb/100 vs tight-passive)"
  CEMINI_GIN_STYLE=1 CEMINI_GIN_STYLE_PREFLOP=1 CEMINI_GIN_STYLE_POSTFLOP=1 \
    CEMINI_COLD_START_NO_STEAL=0 uv run python examples/gin_style_gate.py --gate --hands 200
else
  echo ""
  echo "==> [3/3] gin-style gate skipped (set CEMINI_GIN_STYLE_GATE=1 to enable)"
fi

echo ""
echo "PREFLIGHT FAST OK — safe for code-only deploy."
