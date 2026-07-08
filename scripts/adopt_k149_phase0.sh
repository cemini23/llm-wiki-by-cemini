#!/usr/bin/env bash
# adopt_k149_phase0.sh — Phase-0 metadata for K149 ingest (2026-07-08)
set -euo pipefail
repos=(
  muratcankoylan/Agent-Skills-for-Context-Engineering
  unitedstates/congress-legislators
  APIs-guru/openapi-directory
  gchq/CyberChef
  nasa/openmct
  NatLabRockies/api-umbrella
  MadsLorentzen/ai-job-search
  Diolinux/PhotoGIMP
)
for r in "${repos[@]}"; do
  gh api "repos/$r" --jq '"\(.full_name) | \(.license.spdx_id // "NOASSERTION") | \(.stargazers_count)★ | pushed \(.pushed_at)"' 2>/dev/null || echo "$r | ERR"
done
echo "---"
echo "Integrate: Agent-Skills-for-Context-Engineering (MIT) → poker + TipDrop/David + CCC"
echo "Extract: congress-legislators (CC0) → pm; openapi-directory (CC0) → CCC; DoorDash hybrid review → CCC"
echo "Watch: openmct (NOASSERTION); api-umbrella (MIT) → TipDrop arch decision"
echo "Context: CyberChef (Apache-2.0)"
echo "Reject/ops: castle.io fingerprint evasion (no spoof brief)"
echo "Pass: ai-job-search, PhotoGIMP, gov playbooks, CERN, madison, wet-boew, …"
