"""DeepCFR-lite — train smoke + flag-gated hot-path resolve."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "examples"))

from deepcfr_lite_train import main as train_main  # noqa: E402
from postflop_buckets import (  # noqa: E402
    _reset_bucket_cache,
    bias_scale_params,
    deepcfr_enabled,
    get_buckets_payload,
    lookup_freqs,
    resolve_deepcfr_buckets_path,
    resolve_postflop_buckets_path,
)


@pytest.fixture(autouse=True)
def _isolate_env(monkeypatch):
    monkeypatch.delenv("CEMINI_POSTFLOP_BUCKETS", raising=False)
    monkeypatch.delenv("CEMINI_POSTFLOP_BUCKETS_PATH", raising=False)
    monkeypatch.delenv("CEMINI_DEEPCFR", raising=False)
    monkeypatch.delenv("CEMINI_DEEPCFR_PATH", raising=False)
    _reset_bucket_cache()
    yield
    _reset_bucket_cache()


def test_train_smoke_writes_schema(tmp_path):
    prior = ROOT / "research" / "postflop_hu_buckets.json"
    out = tmp_path / "deepcfr_hu_buckets.json"
    rc = train_main(
        ["--prior", str(prior), "--out", str(out), "--iters", "200", "--seed", "3", "--force"]
    )
    assert rc == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["meta"]["generator"] == "deepcfr_lite_v1"
    assert len(data["buckets"]) >= 90
    sample = next(iter(data["buckets"].values()))
    for k in ("bet", "check", "call", "fold", "raise", "size_pot_frac"):
        assert k in sample


def test_flag_off_ignores_deepcfr_path(monkeypatch, tmp_path):
    deep = tmp_path / "deepcfr_hu_buckets.json"
    deep.write_text(
        json.dumps(
            {
                "meta": {"generator": "deepcfr_lite_v1"},
                "buckets": {
                    "flop|ip|dry|air": {
                        "bet": 0.9,
                        "check": 0.1,
                        "call": 0.0,
                        "fold": 0.0,
                        "raise": 0.0,
                        "size_pot_frac": 0.5,
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_DEEPCFR_PATH", str(deep))
    monkeypatch.setenv("CEMINI_DEEPCFR", "0")
    assert deepcfr_enabled() is False
    # Without POSTFLOP flag, resolve may still find texas path; DeepCFR must not win
    path = resolve_postflop_buckets_path()
    if path is not None:
        assert path.resolve() != deep.resolve()


def test_flag_on_prefers_deepcfr(monkeypatch, tmp_path):
    deep = tmp_path / "deepcfr_hu_buckets.json"
    deep.write_text(
        json.dumps(
            {
                "schema": "postflop-hu-buckets-v1",
                "meta": {"generator": "deepcfr_lite_v1", "key_count": 1},
                "buckets": {
                    "flop|ip|dry|air": {
                        "bet": 0.91,
                        "check": 0.09,
                        "call": 0.0,
                        "fold": 0.0,
                        "raise": 0.0,
                        "size_pot_frac": 0.5,
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("CEMINI_POSTFLOP_BUCKETS", "1")
    monkeypatch.setenv("CEMINI_DEEPCFR", "1")
    monkeypatch.setenv("CEMINI_DEEPCFR_PATH", str(deep))
    _reset_bucket_cache()
    assert resolve_deepcfr_buckets_path() == deep
    assert resolve_postflop_buckets_path() == deep
    payload = get_buckets_payload()
    assert payload is not None
    assert payload["meta"]["generator"] == "deepcfr_lite_v1"
    freqs = lookup_freqs("flop", "ip", "dry", "air")
    assert freqs is not None
    assert freqs["bet"] == pytest.approx(0.91)


def test_deepcfr_bias_scale_phase1():
    p = bias_scale_params("deepcfr_lite_v1")
    assert p["clamp"] == pytest.approx(0.14)
    assert p["free_mult"] == pytest.approx(0.15)


def test_repo_bake_present_or_skip():
    bake = ROOT / "research" / "deepcfr_hu_buckets.json"
    if not bake.is_file():
        pytest.skip("deepcfr bake not generated yet")
    data = json.loads(bake.read_text(encoding="utf-8"))
    assert data["meta"]["generator"] == "deepcfr_lite_v1"
    assert len(data["buckets"]) >= 90
