#!/usr/bin/env bash
# K130 Track B: setup isolated rlcard venv for offline baseline ablation.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${AGENT_DIR}"

VENV_DIR="${AGENT_DIR}/.venv-rlcard"

echo "[arena-pokerkit] Setting up isolated venv at ${VENV_DIR}..."
python3 -m venv "${VENV_DIR}"

echo "[arena-pokerkit] Installing dependencies (rlcard>=1.2.0,<2)..."
"${VENV_DIR}/bin/pip" install -U pip wheel setuptools
"${VENV_DIR}/bin/pip" install "rlcard>=1.2.0,<2" "treys>=0.1.8"

echo "[arena-pokerkit] Verifying rlcard import..."
"${VENV_DIR}/bin/python" -c "import rlcard; print('[arena-pokerkit] rlcard', rlcard.__version__, 'OK at', '${VENV_DIR}')"
