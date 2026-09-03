#!/usr/bin/env bash
set -euo pipefail
echo "K170 Phase-0"
for repo in awslabs/git-secrets Terrastories/terrastories RyanCodrai/turbovec xai-org/grok-build xai-org/grok-build-plugin-cc; do
  gh api "repos/$repo" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | size_kb=\(.size)"' 2>/dev/null || true
done
echo "Inkling: Watch only — Unsloth docs; NO weight download (>>500MB)"
echo "Integrate: turbovec, grok-build(+plugin)"
echo "Extract: git-secrets, terrastories"
echo "Briefs: xsp+pm scp; poker FP theory; TipDrop; CCC; cybersec; gambling; family"
