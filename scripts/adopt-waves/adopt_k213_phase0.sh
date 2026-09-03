#!/usr/bin/env bash
# K213 Phase-0 — MIT/Apache Extracts (+ small prenotami pattern refs). Cap <<500MB.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/.local/adopts"
mkdir -p "$DEST"
clone() {
  local repo="$1" name="$2"
  if [[ -d "$DEST/$name/.git" ]]; then echo "ok $name"; du -sh "$DEST/$name"; return; fi
  echo "==> $repo"
  git clone --depth 1 "https://github.com/$repo.git" "$DEST/$name"
  du -sh "$DEST/$name"
}
clone clifton/rstructor rstructor
clone capazme/mcp-legal-it mcp-legal-it
clone digimata/quill digimata-quill
clone umpire274/cod_fiscale cod_fiscale
clone caiosweet/Home-Assistant-custom-components-DPC-Alert dpc-alert
clone DiegoRiccardi1234/deal-finder deal-finder
clone kamerozkan/italy-fatturapa-validator-sample fatturapa-validator
clone RubenSab/AnsaOverview ansa-overview
clone adamcavendish/aioduct aioduct
clone trouze/prenotami-bot prenotami-bot
clone saml7n/prenotami-booker prenotami-booker
clone chessbr/giustizia-scrap giustizia-scrap
echo "BATCH:"
du -sh "$DEST"/rstructor "$DEST"/mcp-legal-it "$DEST"/digimata-quill "$DEST"/cod_fiscale \
  "$DEST"/dpc-alert "$DEST"/deal-finder "$DEST"/fatturapa-validator "$DEST"/ansa-overview \
  "$DEST"/aioduct "$DEST"/prenotami-bot "$DEST"/prenotami-booker "$DEST"/giustizia-scrap 2>/dev/null
