#!/usr/bin/env bash
# Preflight for jackpot satellite — pytest only (no EP VPIP gate).
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${SCRIPT_DIR}/.."
echo "==> jackpot-27 pytest"
uv run pytest tests/test_jackpot_27_spots.py tests/test_cemini_regression.py -q
echo "==> jackpot-27 dry-run smoke"
uv run examples/agent.py --agent examples/jackpot_27_decide.py --dry-run --max-hands 5
echo "JACKPOT-27 PREFLIGHT OK"
