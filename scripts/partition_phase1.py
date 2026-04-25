#!/usr/bin/env python3
"""Partition phase-1 clusters across 4 subagents. Each paper is assigned to exactly
one subagent (its 'home' cluster = the smallest of its clusters that's in scope).
Papers with zero target-cluster overlap are skipped for this phase."""
import json
import re
from pathlib import Path
from collections import defaultdict

WIKI = Path("/Users/claudiobarone/Desktop/OSINT WORKSPACE/wiki/sources")
CORPUS_JSON = Path("/tmp/bootstrap_corpus.json")
OUT = Path("/tmp/phase1_partition.json")

TARGET_CLUSTERS = [
    "game-theory", "data-engineering", "audit-security", "alt-data",
    "time-series", "options-derivatives", "ml-methods", "infrastructure",
    "portfolio-strategy", "crypto",
]
# cluster size (clean counts from earlier, for ordering 'smallest first')
CLUSTER_SIZE_ORDER = {c: i for i, c in enumerate(TARGET_CLUSTERS)}

AGENT_ASSIGNMENTS = {
    "agent1_small": ["game-theory", "data-engineering", "audit-security", "alt-data", "time-series"],
    "agent2_method": ["options-derivatives", "ml-methods"],
    "agent3_infra_strat": ["infrastructure", "portfolio-strategy"],
    "agent4_crypto": ["crypto"],
}

# --- load corpus + stubs ---
corpus = {r["filename"]: r for r in json.loads(CORPUS_JSON.read_text())}

papers = []
for p in WIKI.glob("*.md"):
    content = p.read_text()
    m_clusters = re.search(r"^clusters: \[(.*?)\]$", content, re.MULTILINE)
    if not m_clusters:
        continue
    clusters = [c.strip() for c in m_clusters.group(1).split(",") if c.strip() and c.strip() != "uncategorized"]
    if not clusters:
        continue
    # skip link-evaluation docs — separate phase
    if "link-evaluation" in content:
        continue
    # find home cluster = smallest in-target cluster, or skip if none
    in_target = [c for c in clusters if c in TARGET_CLUSTERS]
    if not in_target:
        continue
    home = min(in_target, key=lambda c: CLUSTER_SIZE_ORDER[c])
    # pull filename from the stub
    m_loc = re.search(r"\*\*Location\*\*: research for cemini/(.+)", content)
    filename = m_loc.group(1).strip() if m_loc else None
    papers.append({
        "slug": p.stem,
        "filename": filename,
        "home_cluster": home,
        "all_clusters": clusters,
    })

# assign to agents
assignments = defaultdict(list)
for paper in papers:
    for agent_id, cluster_list in AGENT_ASSIGNMENTS.items():
        if paper["home_cluster"] in cluster_list:
            assignments[agent_id].append(paper)
            break

print(f"Total papers in scope: {len(papers)}")
for agent_id, papers_list in assignments.items():
    print(f"\n{agent_id} — {len(papers_list)} papers")
    cluster_counts = defaultdict(int)
    for p in papers_list:
        cluster_counts[p["home_cluster"]] += 1
    for c, n in sorted(cluster_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {c}: {n}")

OUT.write_text(json.dumps({k: list(v) for k, v in assignments.items()}, indent=2))
print(f"\nPartition → {OUT}")
