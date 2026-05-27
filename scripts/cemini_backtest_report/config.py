from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional, Sequence, Tuple


HeatmapSpec = Tuple[str, str, str, str, str]  # x, y, metric, title_suffix, colorscale


@dataclass
class ReportConfig:
    """Venue/strategy metadata for generate_report()."""

    title: str
    subtitle: str = ""
    param_cols: Sequence[str] = ()
    metric_cols: Sequence[str] = (
        "n_trades",
        "hit_rate",
        "total_pnl_usd",
        "total_pnl_pct",
        "sharpe_annual",
        "max_drawdown_pct",
        "profit_factor",
        "avg_pnl_pct",
    )
    heatmap_pairs: Sequence[HeatmapSpec] = ()
    format_config: Optional[Callable] = None
    segment_col: str = "segment"
    trade_pnl_col: str = "net_pnl_pct"
    disclaimer_html: str = ""
    heatmap_note: str = (
        "Each cell = BEST value of the metric across all other parameters for that (x, y) pair."
    )
    top_n: int = 20

    def format_config_row(self, row) -> str:
        if self.format_config:
            return self.format_config(row)
        parts = [f"{c}={row[c]}" for c in self.param_cols if c in row.index]
        return " · ".join(parts)
