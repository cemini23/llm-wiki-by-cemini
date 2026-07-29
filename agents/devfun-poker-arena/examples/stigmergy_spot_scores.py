"""K141 stigmergic spot-class scores (arXiv 2607.15182 pattern, light).

Bounded decaying environment memory that ranks which spot classes enter the
HL planner shortlist — after K161 DeepSearch eligibility filter, before
scaffold expand. Advisory only; never a hard submit gate.

Channels:
  pressure   — recent losses / veto fails in class
  completion — recent wins / clean folds that matched plan
  block      — spots that caused planner/HL thrash

Decay each epoch: M ← ρM + Δ (implemented as scale-by-ρ then optional Δ).
"""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable, Mapping, MutableMapping, Sequence

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG_PATH = _REPO_ROOT / "config" / "hu_stigmergy_spot_scores.json"
CHANNELS: tuple[str, ...] = ("pressure", "completion", "block")


def load_stigmergy_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not cfg_path.is_file():
        raise FileNotFoundError(f"stigmergy config not found: {cfg_path}")
    data = json.loads(cfg_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("stigmergy config must be a JSON object")
    return data


def _clamp(value: float, cap: float) -> float:
    if cap <= 0:
        return max(0.0, value)
    return max(0.0, min(float(cap), float(value)))


def _empty_channel_map() -> dict[str, float]:
    return {c: 0.0 for c in CHANNELS}


class StigmergySpotScores:
    """In-memory decaying scores keyed by spot class."""

    def __init__(self, config: dict[str, Any] | Path | str | None = None) -> None:
        if isinstance(config, (str, Path)):
            self.config = load_stigmergy_config(config)
        elif isinstance(config, dict):
            self.config = deepcopy(config)
        else:
            self.config = load_stigmergy_config()

        self.rho = float(self.config.get("rho", 0.9))
        self.cap = float(self.config.get("cap", 10.0))
        self.advisory_only = bool(self.config.get("advisory_only", True))
        weights = self.config.get("rank_weights") or {}
        self.rank_weights = {
            "pressure": float(weights.get("pressure", 1.0)),
            "block": float(weights.get("block", 1.0)),
            "completion": float(weights.get("completion", -0.25)),
        }
        raw_scores = self.config.get("scores") or {}
        self.scores: dict[str, dict[str, float]] = {}
        if isinstance(raw_scores, dict):
            for cls, chans in raw_scores.items():
                base = _empty_channel_map()
                if isinstance(chans, dict):
                    for ch in CHANNELS:
                        if ch in chans:
                            base[ch] = _clamp(float(chans[ch]), self.cap)
                self.scores[str(cls)] = base

    def _ensure_class(self, spot_class: str) -> dict[str, float]:
        key = str(spot_class)
        if key not in self.scores:
            self.scores[key] = _empty_channel_map()
        return self.scores[key]

    def update_score(
        self,
        spot_class: str,
        channel: str,
        delta: float,
    ) -> dict[str, float]:
        """Apply Δ to one channel: M[ch] ← clamp(M[ch] + Δ)."""
        ch = str(channel).strip().lower()
        if ch not in CHANNELS:
            raise KeyError(f"unknown stigmergy channel: {channel!r}; want {CHANNELS}")
        row = self._ensure_class(spot_class)
        row[ch] = _clamp(row[ch] + float(delta), self.cap)
        return dict(row)

    def decay_all(self, rho: float | None = None) -> None:
        """Epoch decay: M ← ρM for every class/channel."""
        r = self.rho if rho is None else float(rho)
        for row in self.scores.values():
            for ch in CHANNELS:
                row[ch] = _clamp(row[ch] * r, self.cap)

    def channel_scores(self, spot_class: str) -> dict[str, float]:
        return dict(self._ensure_class(spot_class))

    def rank_score(self, spot_class: str) -> float:
        """Scalar used for shortlist order (higher = earlier in planner)."""
        row = self._ensure_class(spot_class)
        total = 0.0
        for ch in CHANNELS:
            total += self.rank_weights.get(ch, 0.0) * row.get(ch, 0.0)
        return total

    def rank_classes(self, eligible: Sequence[str] | Iterable[str]) -> list[str]:
        """Order eligible spot classes by stigmergic rank (desc), stable on ties."""
        items = [str(c) for c in eligible]
        # Stable sort: higher rank first; preserve relative order on equal scores.
        indexed = list(enumerate(items))
        indexed.sort(key=lambda iv: (-self.rank_score(iv[1]), iv[0]))
        return [c for _, c in indexed]

    def rank_units(
        self,
        eligible_units: Sequence[Mapping[str, Any]],
        *,
        class_key: str = "spot_class",
    ) -> list[dict[str, Any]]:
        """Re-order K161-eligible unit dicts by stigmergy (advisory).

        Units without a class key sort last (score 0), preserving relative order.
        """
        decorated: list[tuple[int, float, Mapping[str, Any]]] = []
        for i, unit in enumerate(eligible_units):
            sc = unit.get(class_key) if isinstance(unit, Mapping) else None
            if sc is None and isinstance(unit, Mapping):
                sc = unit.get("spotClass") or unit.get("class")
            score = self.rank_score(str(sc)) if sc is not None else 0.0
            decorated.append((i, score, unit))
        decorated.sort(key=lambda t: (-t[1], t[0]))
        out: list[dict[str, Any]] = []
        for _, score, unit in decorated:
            row = dict(unit)
            row["_stigmergy_rank_score"] = score
            row["_stigmergy_advisory_only"] = self.advisory_only
            out.append(row)
        return out

    def to_config_dict(self) -> dict[str, Any]:
        """Serialize current state for optional persist (operator / tests)."""
        return {
            "schema": self.config.get("schema", "devfun.hu_stigmergy_spot_scores.v1"),
            "rho": self.rho,
            "cap": self.cap,
            "channels": list(CHANNELS),
            "rank_weights": dict(self.rank_weights),
            "scores": {k: dict(v) for k, v in self.scores.items()},
            "advisory_only": self.advisory_only,
            "notes": self.config.get("notes", ""),
        }

    def snapshot(self) -> dict[str, Any]:
        return {
            "schema": "devfun.stigmergy_snapshot.v1",
            "advisory_only": self.advisory_only,
            "rho": self.rho,
            "cap": self.cap,
            "n_classes": len(self.scores),
            "scores": {k: dict(v) for k, v in self.scores.items()},
            "reference": "references/stigmergy-spot-scores.md",
        }


def rank_eligible_spot_classes(
    eligible: Sequence[str] | Iterable[str],
    *,
    config: dict[str, Any] | Path | str | None = None,
    scores: StigmergySpotScores | None = None,
) -> list[str]:
    """Module-level helper: order eligible classes by stigmergy."""
    store = scores if scores is not None else StigmergySpotScores(config)
    return store.rank_classes(eligible)


def apply_stigmergy_to_deepsearch_filter(
    filter_out: Mapping[str, Any],
    *,
    config: dict[str, Any] | Path | str | None = None,
    scores: StigmergySpotScores | None = None,
) -> dict[str, Any]:
    """After K161 filter: re-rank eligible units by stigmergy (advisory).

    Does not change eligibility — only shortlist order for HL mix/scaffold.
    """
    store = scores if scores is not None else StigmergySpotScores(config)
    eligible = list(filter_out.get("eligible") or [])
    ranked = store.rank_units(eligible)
    classes = []
    seen: set[str] = set()
    for u in ranked:
        sc = str(u.get("spot_class") or "")
        if sc and sc not in seen:
            seen.add(sc)
            classes.append(sc)
    return {
        **dict(filter_out),
        "eligible": ranked,
        "eligible_ranked_by_stigmergy": True,
        "stigmergy_ranked_classes": classes,
        "stigmergy_advisory_only": store.advisory_only,
        "stigmergy": store.snapshot(),
    }


def stigmergy_brief_section(
    eligible_classes: Sequence[str] | None = None,
    *,
    config: dict[str, Any] | Path | str | None = None,
    scores: StigmergySpotScores | None = None,
) -> str:
    """Markdown block for HL analyst brief (advisory shortlist order)."""
    store = scores if scores is not None else StigmergySpotScores(config)
    classes = list(eligible_classes or [])
    if not classes and store.scores:
        classes = list(store.scores.keys())
    ranked = store.rank_classes(classes) if classes else []
    lines = [
        "### Stigmergic spot shortlist (K141 — advisory)",
        "",
        "After K161 DeepSearch eligibility, re-rank spot classes by decaying",
        "pressure/block (prefer thrash/loss classes) before scaffold expand.",
        f"**advisory_only={store.advisory_only}** — not a submit gate.",
        "",
    ]
    if not ranked:
        lines.append("(no eligible classes / empty scores — default K161 order)")
    else:
        lines.append("| Rank | Spot class | Score | pressure | block | completion |")
        lines.append("|------|------------|-------|----------|-------|------------|")
        for i, sc in enumerate(ranked, 1):
            row = store.channel_scores(sc)
            lines.append(
                f"| {i} | `{sc}` | {store.rank_score(sc):.2f} | "
                f"{row['pressure']:.2f} | {row['block']:.2f} | "
                f"{row['completion']:.2f} |"
            )
    lines.append("")
    lines.append("See `references/stigmergy-spot-scores.md`.")
    return "\n".join(lines) + "\n"
