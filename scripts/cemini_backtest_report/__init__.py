"""Cemini venue-agnostic backtest HTML reports (Plotly)."""

from .config import ReportConfig
from .report import generate_report

__all__ = ["ReportConfig", "generate_report"]
