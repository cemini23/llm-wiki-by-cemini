#!/usr/bin/env bash
# K202 Phase-0 shallow adopts (<500MB): FlareSolverr, heroicons, undetected-chromedriver,
# cardkit, chrome-devtools-mcp refresh, daisyui npm-pack only. No puppeteer/SingleFile/browserless clones.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ADOPT="$ROOT/.local/adopts"
mkdir -p "$ADOPT"
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

clone() {
  local repo="$1" dir="$2"
  if [[ -d "$ADOPT/$dir/.git" ]]; then
    echo "skip $dir (exists)"
    return 0
  fi
  git clone --depth 1 "https://github.com/${repo}.git" "$ADOPT/$dir"
  du -sh "$ADOPT/$dir"
}

clone FlareSolverr/FlareSolverr flaresolverr
clone tailwindlabs/heroicons heroicons
clone ultrafunkamsterdam/undetected-chromedriver undetected-chromedriver
clone times/cardkit cardkit
clone ChromeDevTools/chrome-devtools-mcp chrome-devtools-mcp

if [[ ! -d "$ADOPT/daisyui-npm/package" ]]; then
  mkdir -p "$ADOPT/daisyui-npm"
  (cd "$ADOPT/daisyui-npm" && npm pack daisyui@latest --silent && tar -xzf daisyui-*.tgz)
  du -sh "$ADOPT/daisyui-npm"
fi

if command -v brew >/dev/null; then
  brew list mkcert >/dev/null 2>&1 || brew install mkcert
  mkcert -version || true
else
  echo "WARN: brew missing — install mkcert manually (BSD-3-Clause Extract)"
fi

echo "K202 Phase-0 done. Skip: puppeteer monorepo, SingleFile (AGPL), browserless (SSPL)."
echo "Report: $ROOT/.local/reports/k202-phase0-2026-07-28.md"
