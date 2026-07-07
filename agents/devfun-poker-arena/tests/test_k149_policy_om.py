"""K149 policy-representation embedding + ADVENT predicate invention."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in (ROOT, ROOT / "examples", ROOT / "scripts"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import policy_ssl_embedding as ssl  # noqa: E402
import predicate_invention as pi  # noqa: E402


def test_policy_embedding_separates_aggression():
    # Fast: skip selfplay payoff eval; just check the linear aggression probe.
    report = ssl.run(hands=0, seed=42, with_payoff=False)
    probe = report["aggression_probe"]
    assert probe["separates"] is True, probe
    assert probe["min_aggressive_score"] > probe["max_passive_score"]


def test_policy_embedding_shape():
    report = ssl.run(with_payoff=False)
    for name, emb in report["embeddings"].items():
        assert len(emb) == len(ssl.EMBED_KEYS), name
        assert all(0.0 <= v <= 1.0 for v in emb), name


def test_predicates_verified_no_live_leak():
    report = pi.evaluate()
    assert report["predicate_count"] >= 3
    assert report["live_leak_count"] == 0, report["live_leaks"]
    # Every predicate should apply to at least one frozen spot and be verified.
    for r in report["results"]:
        assert r["applicable_spots"] >= 1, r["name"]
        assert r["verified"] is True, r["name"]


def test_predicate_pool_domains_distinct():
    names = [p.name for p in pi._predicate_pool()]
    assert len(names) == len(set(names))
