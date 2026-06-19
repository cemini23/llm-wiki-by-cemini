#!/usr/bin/env bash
# Pre-deploy gate for cemini Playground / tournament seasons.
#
# Run before rsync to prod or after any decide() / HUD change:
#   ./scripts/cemini_preflight.sh
#   ./scripts/cemini_preflight.sh --full   # slower self-play audit with --gate
set -euo pipefail
cd "$(dirname "$0")/.."

FULL=0
for arg in "$@"; do
  case "$arg" in
    --full) FULL=1 ;;
  esac
done

echo "==> [1/5] pytest (unit + cemini regression + scenarios)"
uv run python -m pytest tests/ -q --tb=short

echo ""
echo "==> [2/5] anti-profiling deep audit (mix+s sanitize ON)"
uv run python examples/cemini_anti_profiling_audit.py --gate --hands 400 --seed 42

echo ""
echo "==> [3/5] cemini self-play KPI audit (report, mix OFF baseline)"
if [[ "$FULL" -eq 1 ]]; then
  uv run python examples/cemini_selfplay_audit.py --hands 600 --seed 42 --gate
else
  uv run python examples/cemini_selfplay_audit.py --hands 250 --seed 42 --gate
fi

echo ""
echo "==> [4/5] eval-panel gate (tournament-shaped self-play)"
EVAL_GATE_HANDS="${CEMINI_EVAL_GATE_HANDS:-150}"
if uv run python -c "import os; exit(0 if os.environ.get('CEMINI_EVAL_PANEL_GATE','').strip() in ('1','true','yes','on') else 1)" 2>/dev/null; then
  uv run python examples/eval_panel_gate.py --gate --hands "${EVAL_GATE_HANDS}" --write-metrics
else
  echo "    CEMINI_EVAL_PANEL_GATE off — report only (no gate)"
  uv run python examples/eval_panel_gate.py --hands "${EVAL_GATE_HANDS}" --write-metrics
fi

if uv run python -c "import os; exit(0 if os.environ.get('CEMINI_RESEARCHER_MODE','').strip() in ('1','true','yes','on') else 1)" 2>/dev/null; then
  echo ""
  RESEARCHER_GATE_HANDS="${CEMINI_RESEARCHER_GATE_HANDS:-100}"
  echo "==> [4b] Researcher sandbox gate (${RESEARCHER_GATE_HANDS} hands, axis gates)"
  bash scripts/run_hu_sandbox_gate.sh --hands "$RESEARCHER_GATE_HANDS"
fi

echo ""
echo "==> [5/5] dry-run lobby path (no network)"
uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 15

mkdir -p reports/hl-loop
date -u +%Y-%m-%dT%H:%M:%SZ > reports/hl-loop/preflight_ok.timestamp

echo ""
echo "PREFLIGHT OK — safe to deploy (rsync + systemctl restart)."
echo "    stamp → reports/hl-loop/preflight_ok.timestamp (fast deploy valid 24h)"
