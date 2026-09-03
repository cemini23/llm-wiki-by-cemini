#!/usr/bin/env bash
# K220 Phase-0 — cyber/agent-harness revenue eval Extracts (<500MB).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.local/adopts"
REPORT="$ROOT/.local/reports/k220-phase0-$(date +%Y-%m-%d).md"
mkdir -p "$DEST" "$(dirname "$REPORT")"

clone() {
  local repo="$1" name="$2"
  if [[ -d "$DEST/$name/.git" ]]; then echo "ok $name"; du -sh "$DEST/$name"; return; fi
  git clone --depth 1 "https://github.com/$repo.git" "$DEST/$name"
  du -sh "$DEST/$name"
}

# AGPL Watch — must NOT be under adopts/
if [[ -d "$DEST/worldmonitor" ]]; then
  echo "FAIL: worldmonitor still in adopts (AGPL Watch)" >&2
  exit 1
fi

# Black-cat null SPDX — must NOT be cloned
if [[ -d "$DEST/Black-cat" || -d "$DEST/black-cat" ]]; then
  echo "FAIL: Black-cat cloned despite null SPDX" >&2
  exit 1
fi

clone boldsoftware/meat meat
clone vercel-labs/marketing-team-eve-template marketing-team-eve-template
clone AeternaLabsHQ/pullmd pullmd

SIZE_MB=$(du -sm "$DEST/meat" "$DEST/marketing-team-eve-template" "$DEST/pullmd" 2>/dev/null | awk '{s+=$1} END{print s+0}')
cat >"$REPORT" <<R
# K220 Phase-0 — $(date +%Y-%m-%d)

| Dir | Role |
|-----|------|
| meat | Extract Apache-2.0 (LICENSE file) → CCC |
| marketing-team-eve-template | Extract MIT → SEO + Atto GTM |
| pullmd | Extract **AGPL-3.0 isolate** → Atto vault ingest patterns |

**Skipped:** Black-cat (null SPDX); worldmonitor (AGPL Watch K182); ds4 / cloudflare/computer / Flue (Watch only).

**Disk (these three):** ~${SIZE_MB} MB.
**No HF weight downloads. No Black-cat / worldmonitor clones.**
R
echo "Wrote $REPORT (${SIZE_MB} MB these adopts)"
du -sh "$DEST/meat" "$DEST/marketing-team-eve-template" "$DEST/pullmd"
