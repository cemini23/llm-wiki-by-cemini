#!/usr/bin/env bash
# K182 Phase-0 — URL revenue eval Integrate/Extract clones (<500MB).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPTS="${ROOT}/.local/adopts"
REPORT="${ROOT}/.local/reports/k182-phase0-$(date +%Y-%m-%d).md"
mkdir -p "$ADOPTS" "$(dirname "$REPORT")"

# Expected: outlines, cloudflare-temp-email, omlx, likec4, pi-web, gigatoken
# worldmonitor = AGPL Watch — must NOT be under adopts/
if [[ -d "$ADOPTS/worldmonitor" ]]; then
  echo "FAIL: worldmonitor still in adopts (AGPL Watch)" >&2
  exit 1
fi

SIZE_MB=$(du -sm "$ADOPTS" | awk '{print $1}')
cat >"$REPORT" <<R
# K182 Phase-0 — $(date +%Y-%m-%d)

Local adopts under \`.local/adopts/\` (ex-worldmonitor AGPL):

| Dir | Role |
|-----|------|
| outlines | Integrate Apache-2.0 |
| cloudflare-temp-email | Integrate MIT (Atto) |
| omlx | Integrate Apache-2.0 (Atto local LLM) |
| likec4 | Extract MIT |
| pi-web | Extract MIT |
| gigatoken | Extract MIT |

**Disk:** ~${SIZE_MB} MB (cap 500 MB).
**No HF weight downloads.**
R
echo "Wrote $REPORT (${SIZE_MB} MB adopts)"
du -sh "$ADOPTS"/*/
