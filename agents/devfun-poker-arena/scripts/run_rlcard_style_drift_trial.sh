#!/usr/bin/env bash
# K153: Leduc stylized archetype + D_policy style-drift trial (RLCard isolated venv).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

VENV_DIR="${AGENT_DIR}/.venv-rlcard"
PYTHON_BIN="${VENV_DIR}/bin/python"

if [[ ! -x "${PYTHON_BIN}" ]]; then
  echo "[arena-pokerkit] Error: venv python not found at ${PYTHON_BIN}. Run setup_rlcard_venv.sh first." >&2
  exit 1
fi

EPISODES=100
EXTRA_ARGS=()
while [[ $# -gt 0 ]]; do
  case $1 in
    --episodes)
      EPISODES="$2"
      shift 2
      ;;
    *)
      EXTRA_ARGS+=("$1")
      shift
      ;;
  esac
done

echo "[arena-pokerkit] Running K153 Leduc style-drift trial (${EPISODES} episodes)..."
"${PYTHON_BIN}" examples/rlcard_style_drift_trial.py --episodes "${EPISODES}" "${EXTRA_ARGS[@]+"${EXTRA_ARGS[@]}"}"
