#!/usr/bin/env bash
# K178 Phase-0 — no clones (Context/newsletter only).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT="${ROOT}/.local/reports/k178-phase0-$(date +%Y-%m-%d).md"
mkdir -p "$(dirname "$REPORT")"
cat >"$REPORT" <<'R'
# K178 Phase-0 — no Integrate/Extract clones

Art-theory paper + RSS only. Local adopt size: 0 MB.
R
echo "Wrote $REPORT (0 MB adopts)"
