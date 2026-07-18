#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec "${ROOT}/.local/venvs/airllm/bin/python" -c "import airllm; print(\"airllm OK\")"
