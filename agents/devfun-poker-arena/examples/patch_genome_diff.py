"""K155 GenomeDiff validator — Inherited/Mutated/Lost/Novel compositional gate.

IdeaGene-Bench (2607.08758) pattern: parent + delta + verification must agree
before an HL patch ships. Advisory by default (config advisory_only=true).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = _REPO_ROOT / "config" / "hu_patch_genome_diff.json"

_DELTA_MUTATE = "mutate"
_DELTA_NOVEL = "novel"
_VALID_DELTAS = frozenset({_DELTA_MUTATE, _DELTA_NOVEL})


def load_genome_diff_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"genome diff config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("genome diff config must be a JSON object")
    return data


def empty_genome_diff(
    *,
    parent_mechanism: str = "",
    delta: str = _DELTA_MUTATE,
) -> dict[str, Any]:
    return {
        "schema": "devfun.patch_genome_diff.v1",
        "parent_mechanism": parent_mechanism,
        "delta": delta,
        "inherited": [],
        "mutated": [],
        "lost": [],
        "novel": [],
        "verification": "",
    }


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        text = value.strip()
        return [text] if text else []
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value if str(x).strip()]
    return [str(value).strip()] if str(value).strip() else []


def normalize_genome_diff(record: dict[str, Any]) -> dict[str, Any]:
    out = empty_genome_diff(
        parent_mechanism=str(record.get("parent_mechanism") or "").strip(),
        delta=str(record.get("delta") or _DELTA_MUTATE).strip().lower(),
    )
    out["inherited"] = _as_list(record.get("inherited"))
    out["mutated"] = _as_list(record.get("mutated"))
    out["lost"] = _as_list(record.get("lost"))
    out["novel"] = _as_list(record.get("novel"))
    out["verification"] = str(record.get("verification") or "").strip()
    if record.get("notes"):
        out["notes"] = str(record["notes"]).strip()
    return out


def validate_genome_diff(
    record: dict[str, Any],
    *,
    config: dict[str, Any] | str | Path | None = None,
) -> dict[str, Any]:
    """Return compositional gate result. Does not raise on FAIL."""
    cfg = (
        load_genome_diff_config(config)
        if config is None or isinstance(config, (str, Path))
        else config
    )
    norm = normalize_genome_diff(record)
    failures: list[str] = []

    if not norm["parent_mechanism"]:
        failures.append("missing_parent_mechanism")
    if norm["delta"] not in _VALID_DELTAS:
        failures.append(f"invalid_delta:{norm['delta']!r}")

    lineage_nonempty = any(
        norm[k] for k in ("inherited", "mutated", "lost", "novel")
    )
    if not lineage_nonempty:
        failures.append("empty_lineage_fields")

    if not norm["verification"]:
        failures.append("missing_verification")

    if norm["delta"] == _DELTA_MUTATE and not (norm["mutated"] or norm["lost"]):
        failures.append("mutate_requires_mutated_or_lost")
    if norm["delta"] == _DELTA_NOVEL and not norm["novel"]:
        failures.append("novel_requires_novel_field")

    # Reject ecology-only steals: parent that is just a paper topic tag
    parent_l = norm["parent_mechanism"].lower()
    ecology_only = (
        "imperfect" in parent_l
        and "info" in parent_l
        and "decide" not in parent_l
        and "nemesis" not in parent_l
        and "guard" not in parent_l
        and "_" not in parent_l
    )
    if ecology_only and not (norm["mutated"] or norm["novel"]):
        failures.append("ecology_only_parent_no_driver")

    ok = not failures
    return {
        "schema": "devfun.patch_genome_diff.gate.v1",
        "ok": ok,
        "advisory_only": bool(cfg.get("advisory_only", True)),
        "failures": failures,
        "record": norm,
        "reference": "references/patch-genome-diff.md",
    }


def genome_diff_markdown_table(record: dict[str, Any]) -> str:
    """Render a one-row GenomeDiff table for HL briefs."""
    n = normalize_genome_diff(record)

    def _join(items: list[str]) -> str:
        return "; ".join(items) if items else "—"

    return (
        "| Field | Value |\n"
        "|-------|-------|\n"
        f"| Parent mechanism | `{n['parent_mechanism'] or '—'}` |\n"
        f"| Delta | `{n['delta']}` |\n"
        f"| Inherited | {_join(n['inherited'])} |\n"
        f"| Mutated | {_join(n['mutated'])} |\n"
        f"| Lost | {_join(n['lost'])} |\n"
        f"| Novel | {_join(n['novel'])} |\n"
        f"| Verification | `{n['verification'] or '—'}` |\n"
    )


def genome_diff_brief_section() -> str:
    """Empty GenomeDiff scaffold injected into HL analyst briefs."""
    return """### GenomeDiff (K155 — required before ship)

Fill before deploy. Task co-location ≠ lineage — name the **driver mechanism**.

| Field | Value |
|-------|-------|
| Parent mechanism | (named heuristic/guard being extended) |
| Delta | `mutate` \\| `novel` |
| Inherited | … |
| Mutated | … |
| Lost | … (and why) |
| Novel | … |
| Verification | regression spot id / pytest / gate command |

Compositional gate: parent + delta + verification must agree
(`uv run python -c "from patch_genome_diff import validate_genome_diff; …"`).
See `references/patch-genome-diff.md`.
"""
