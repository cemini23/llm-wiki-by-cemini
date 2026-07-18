#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OSSIE="${ROOT}/.local/adopts/ossie"
ls "${OSSIE}/examples" | head
echo "See ${OSSIE}/validation/ — Watch-tier semantic model interchange."
