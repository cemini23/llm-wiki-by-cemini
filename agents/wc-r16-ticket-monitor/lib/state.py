"""Persistent alert dedupe state."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class AlertRecord:
    event_id: str
    platform: str
    price_usd: float
    alerted_at: str


class StateStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self._records: dict[str, AlertRecord] = {}
        self.load()

    def _key(self, event_id: str, platform: str) -> str:
        return f"{event_id}::{platform.lower()}"

    def load(self) -> None:
        if not self.path.exists():
            return
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        for item in raw.get("alerts", []):
            rec = AlertRecord(**item)
            self._records[self._key(rec.event_id, rec.platform)] = rec

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "updated_at": _utcnow().isoformat(),
            "alerts": [
                {
                    "event_id": r.event_id,
                    "platform": r.platform,
                    "price_usd": r.price_usd,
                    "alerted_at": r.alerted_at,
                }
                for r in self._records.values()
            ],
        }
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def should_alert(
        self,
        *,
        event_id: str,
        platform: str,
        price_usd: float,
        cooldown_hours: float,
        drop_realert_usd: float,
    ) -> bool:
        key = self._key(event_id, platform)
        prev = self._records.get(key)
        if prev is None:
            return True

        prev_price = prev.price_usd
        if price_usd < prev_price - drop_realert_usd:
            return True

        try:
            last = datetime.fromisoformat(prev.alerted_at)
        except ValueError:
            return True

        age_hours = (_utcnow() - last).total_seconds() / 3600.0
        if age_hours >= cooldown_hours and price_usd < prev_price:
            return True

        return False

    def mark_alerted(self, *, event_id: str, platform: str, price_usd: float) -> None:
        self._records[self._key(event_id, platform)] = AlertRecord(
            event_id=event_id,
            platform=platform,
            price_usd=price_usd,
            alerted_at=_utcnow().isoformat(),
        )

    def last_scan_path(self, base: Path) -> Path:
        return base / "last_scan.json"

    def write_scan_snapshot(self, base: Path, snapshot: dict) -> None:
        path = self.last_scan_path(base)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
