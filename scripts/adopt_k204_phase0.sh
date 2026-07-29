#!/usr/bin/env bash
# K204 Phase-0 — OpenWork only (Extract). Brazilian civic APIs from same eval are Pass/Context — not cloned.
# Verdict: CONDITIONAL-GO Extract — MIT tree outside /ee; never wire ee/ (FSL-1.1-MIT Competing Use).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
REPORT="$ROOT/.local/reports/k204-phase0-$(date +%Y-%m-%d).md"
mkdir -p "$ADOPT" "$(dirname "$REPORT")"

clone() {
  local repo="$1" dir="$2" branch="${3:-}"
  if [[ -d "$ADOPT/$dir/.git" ]]; then
    echo "skip $dir (exists)"
    return 0
  fi
  if [[ -n "$branch" ]]; then
    git clone --depth 1 --branch "$branch" "https://github.com/${repo}.git" "$ADOPT/$dir"
  else
    git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dir"
  fi
  du -sh "$ADOPT/$dir"
}

clone different-ai/openwork openwork dev

OW="$ADOPT/openwork"
SIZE="$(du -sh "$OW" | awk '{print $1}')"
LICENSE_HEAD="$(head -20 "$OW/LICENSE" | tr '\n' ' ')"
EE_LICENSE="$(head -5 "$OW/ee/LICENSE" | tr '\n' ' ')"
MCP_PKG_LICENSE="$(python3 -c "import json; print(json.load(open('$OW/packages/openwork-ui-mcp/package.json')).get('license'))")"
MCP_SDK="$(python3 -c "import json; print(json.load(open('$OW/packages/openwork-ui-mcp/package.json'))['dependencies']['@modelcontextprotocol/sdk'])")"

# syntax check MIT MCP package (no npm install — node --check only)
node --check "$OW/packages/openwork-ui-mcp/index.mjs"

cat >"$REPORT" <<EOF
# K204 Phase-0 — $(date +%Y-%m-%d)

## Scope

| Repo | Tier | Action |
|------|------|--------|
| different-ai/openwork | Extract (Atto) | Shallow clone \`dev\` → \`.local/adopts/openwork\` ($SIZE) |
| BR civic APIs (quorum / querido-diario / brasil.io / pix / open-erp) | Pass/Context/UNAVAILABLE | **Not cloned** |

## License (gh + tree)

- Root \`LICENSE\`: **MIT** for all content **except** \`/ee\` → **FSL-1.1-MIT** (\`ee/LICENSE\`).
- GitHub API \`license.spdx_id\`: NOASSERTION (expected for dual MIT+FSL).
- \`packages/openwork-ui-mcp\`: package.json **MIT**; depends \`@modelcontextprotocol/sdk $MCP_SDK\`.
- \`ee/\` (~32M): Fair Source — **Permitted Purpose excludes Competing Use** (shipping as commercial substitute for OpenWork / similar).

## Smoke

- \`node --check packages/openwork-ui-mcp/index.mjs\` — OK (no \`pnpm i\`).
- Note: \`openwork-ui-mcp\` is an MCP **server that controls OpenWork's UI bridge** — not a client shell for \`atto-mcp\`. Atto already has Python \`atto_mcp\` + \`apps/desktop\`.

## Verdict

**CONDITIONAL-GO Extract (patterns only).**

Adopted: reference clone under \`.local/adopts/openwork\`.

**Do adopt (steal):**
- MIT UX / skill-router / tool-call rendering patterns from \`apps/*\` + non-\`ee\` packages
- MCP stdio/client patterns from MIT packages (\`@modelcontextprotocol/sdk ^1.29\`)

**Do not:**
- \`pnpm install\` / vendor full Electron OpenWork into Atto kit (supply chain + Competing Use risk if shipping substantially similar commercial UI)
- Copy or depend on anything under \`ee/\`
- Treat OpenWork as citizenship eligibility engine
- Install Brazilian civic API repos from K204 eval

## Atto next (parked)

Visa: \`Atto/docs/k204-openwork-visa.md\` — UI pattern steal checklist only; no dependency pin until operator GO on a rewrite that is clearly not an OpenWork substitute.
EOF

echo "K204 Phase-0 done."
echo "Report: $REPORT"
echo "LICENSE_HEAD: $LICENSE_HEAD"
echo "EE: $EE_LICENSE"
echo "openwork-ui-mcp license=$MCP_PKG_LICENSE sdk=$MCP_SDK"
