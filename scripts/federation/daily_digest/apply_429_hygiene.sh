#!/usr/bin/env bash
# Apply sibling-wiki digest hygiene (SEO query, game-dev query, gambling RSS
# inbox stubs) then sync the federation Python bundle and reinstall LaunchAgents.
#
# OSINT arXiv retry/flock + +7m stagger already live in this repo.
# This script is needed when the Grok session is workspace-sandboxed and cannot
# write sibling repos / ~/.cemini / ~/Library/LaunchAgents.
#
# Usage (from OSINT root, no --backfill):
#   bash scripts/federation/daily_digest/apply_429_hygiene.sh

set -euo pipefail

OSINT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
PAYLOAD="${OSINT_ROOT}/scripts/federation/daily_digest/gambling_payload"
PROJECTS="${CEMINI_PROJECTS_ROOT:-$HOME/Projects}"

SEO_CFG="${PROJECTS}/SEO:GEO B&M Business/scripts/daily_research_config.yaml"
GAME_CFG="${PROJECTS}/Game Dev wiki/scripts/daily_research_config.yaml"
GAMBLE="${PROJECTS}/Gambling wiki"

cp -f "${PAYLOAD}/seo_daily_research_config.yaml" "${SEO_CFG}"
echo "  SEO config → ${SEO_CFG}"

cp -f "${PAYLOAD}/gamedev_daily_research_config.yaml" "${GAME_CFG}"
echo "  game-dev config → ${GAME_CFG}"

cp -f "${PAYLOAD}/rss_digest.py" "${GAMBLE}/scripts/rss_digest.py"
cp -f "${PAYLOAD}/daily_research_digest_run.py" "${GAMBLE}/scripts/daily_research_digest_run.py"
cp -f "${PAYLOAD}/daily_research_config.yaml" "${GAMBLE}/scripts/daily_research_config.yaml"
mkdir -p "${GAMBLE}/tests"
cp -f "${PAYLOAD}/test_rss_digest.py" "${GAMBLE}/tests/test_rss_digest.py"
echo "  gambling RSS inbox writer + tests → ${GAMBLE}"

bash "${OSINT_ROOT}/scripts/federation/daily_digest/sync_federation_digest_bundle.sh"
bash "${OSINT_ROOT}/scripts/reinstall_morning_launchagents.sh"

echo "Done. Run Verify from OSINT root (no git commit)."
