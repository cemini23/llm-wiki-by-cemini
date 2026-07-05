"""Publish cadence / staleness metrics."""

from __future__ import annotations

import datetime as dt
from typing import Any


def staleness_metrics(publish_date: str, today: dt.date, biweekly_days: int) -> dict[str, Any]:
    if not publish_date:
        return {"days_since_publish": None, "missed_cycles": None, "status": "unknown"}
    pub = dt.date.fromisoformat(publish_date)
    days = (today - pub).days
    missed = max(0, (days - biweekly_days) // biweekly_days) if days > biweekly_days else 0
    if days <= biweekly_days:
        status = "current"
    elif days <= biweekly_days * 2:
        status = "late"
    else:
        status = "stale"
    return {
        "days_since_publish": days,
        "missed_cycles": missed,
        "status": status,
        "publish_date": publish_date,
    }
