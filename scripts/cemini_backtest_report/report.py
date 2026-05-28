"""Self-contained Plotly HTML backtest reports (HL-funding layout)."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from .config import ReportConfig

DEFAULT_METRIC_COLS = [
    "n_trades",
    "hit_rate",
    "total_pnl_usd",
    "total_pnl_pct",
    "sharpe_annual",
    "max_drawdown_pct",
    "profit_factor",
    "avg_pnl_pct",
    "pct_tp",
    "pct_sl",
    "avg_hours_held",
]


def _heatmap_pair(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    value_col: str,
    title_suffix: str = "",
    colorscale: str = "RdYlGn",
) -> go.Figure:
    pivot = df.groupby([y_col, x_col])[value_col].max().unstack()
    fig = go.Figure(
        go.Heatmap(
            z=pivot.values,
            x=[str(v) for v in pivot.columns],
            y=[str(v) for v in pivot.index],
            colorscale=colorscale,
            zmid=0
            if value_col in ("sharpe_annual", "total_pnl_usd", "total_pnl_pct")
            else None,
            text=[
                [f"{v:.2f}" if pd.notna(v) else "" for v in row]
                for row in pivot.values
            ],
            texttemplate="%{text}",
            colorbar=dict(title=value_col),
        )
    )
    fig.update_layout(
        title=f"Best {value_col} by {x_col} × {y_col}{title_suffix}",
        xaxis_title=x_col,
        yaxis_title=y_col,
        height=420,
        margin=dict(l=80, r=40, t=80, b=60),
    )
    return fig


def _trade_count_per_param(df: pd.DataFrame, param: str) -> go.Figure:
    agg = df.groupby(param).agg(
        avg_n_trades=("n_trades", "mean"),
        avg_sharpe=("sharpe_annual", "mean"),
        avg_pnl=("total_pnl_usd", "mean"),
    ).reset_index()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=agg[param].astype(str),
            y=agg["avg_n_trades"],
            name="Avg # trades",
            marker_color="#4c78a8",
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=agg[param].astype(str),
            y=agg["avg_sharpe"],
            name="Avg Sharpe",
            marker_color="#f58518",
            mode="lines+markers",
        ),
        secondary_y=True,
    )
    fig.update_layout(
        title=f"Trade count & Sharpe by {param}",
        height=350,
        margin=dict(l=60, r=40, t=60, b=60),
        xaxis_title=param,
    )
    fig.update_yaxes(title_text="Avg # trades", secondary_y=False)
    fig.update_yaxes(title_text="Avg Sharpe annual", secondary_y=True)
    return fig


def _equity_curve_fig(eq_df: pd.DataFrame, title: str) -> go.Figure:
    fig = go.Figure()
    if eq_df is None or eq_df.empty:
        fig.update_layout(title=f"{title} — no trades")
        return fig
    fig.add_trace(
        go.Scatter(
            x=eq_df["ts"],
            y=eq_df["cum_pnl_usd"],
            mode="lines",
            line=dict(color="#2ca02c", width=2),
            name="Cum PnL",
        )
    )
    peak = eq_df["cum_pnl_usd"].cummax()
    fig.add_trace(
        go.Scatter(
            x=eq_df["ts"],
            y=peak,
            mode="lines",
            line=dict(color="rgba(0,0,0,0.2)", width=1, dash="dot"),
            name="Peak",
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Cumulative PnL ($)",
        height=400,
        margin=dict(l=60, r=40, t=60, b=60),
        hovermode="x unified",
    )
    return fig


def _trade_distribution_fig(
    trades_df: pd.DataFrame, title: str, pnl_col: str
) -> go.Figure:
    if trades_df is None or trades_df.empty:
        fig = go.Figure()
        fig.update_layout(title=f"{title} — no trades")
        return fig
    fig = px.histogram(
        trades_df,
        x=pnl_col,
        nbins=40,
        color_discrete_sequence=["#1f77b4"],
        title=title,
    )
    fig.add_vline(x=0, line_dash="dash", line_color="black")
    fig.update_layout(
        height=350,
        margin=dict(l=60, r=40, t=60, b=60),
        xaxis_title=pnl_col,
        yaxis_title="# trades",
    )
    return fig


def _exit_reasons_fig(trades_df: pd.DataFrame, title: str) -> go.Figure:
    if trades_df is None or trades_df.empty or "exit_reason" not in trades_df:
        fig = go.Figure()
        fig.update_layout(title=f"{title} — no trades")
        return fig
    counts = trades_df["exit_reason"].value_counts().reset_index()
    counts.columns = ["exit_reason", "count"]
    fig = px.bar(counts, x="exit_reason", y="count", color="exit_reason", title=title)
    fig.update_layout(
        height=350,
        margin=dict(l=60, r=40, t=60, b=60),
        showlegend=False,
        xaxis_title="",
        yaxis_title="# events",
    )
    return fig


def _per_segment_fig(per_seg_df: pd.DataFrame, segment_col: str) -> go.Figure:
    if per_seg_df is None or per_seg_df.empty:
        fig = go.Figure()
        fig.update_layout(title="Per-segment breakdown — no trades")
        return fig
    df = per_seg_df.copy()
    label = segment_col if segment_col in df.columns else "segment"
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    colors = [
        "#2ca02c" if v >= 0 else "#d62728" for v in df["total_pnl_usd"]
    ]
    fig.add_trace(
        go.Bar(
            x=df[label],
            y=df["total_pnl_usd"],
            name="Total PnL ($)",
            marker_color=colors,
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=df[label],
            y=df["n_trades"],
            name="# trades",
            marker_color="#ff7f0e",
            mode="markers",
            marker=dict(size=10),
        ),
        secondary_y=True,
    )
    fig.update_layout(
        title=f"Per-segment: total PnL ($) and event count",
        height=400,
        margin=dict(l=60, r=40, t=60, b=60),
        xaxis_title="",
        hovermode="x unified",
    )
    fig.update_yaxes(title_text="Total PnL ($)", secondary_y=False)
    fig.update_yaxes(title_text="# events", secondary_y=True)
    return fig


def _top_configs_html(
    sweep_df: pd.DataFrame, config: ReportConfig, n: int = 20
) -> str:
    df = sweep_df.copy().sort_values("sharpe_annual", ascending=False).head(n)
    cols_show = list(config.param_cols) + [
        c
        for c in [
            "n_trades",
            "hit_rate",
            "total_pnl_usd",
            "sharpe_annual",
            "max_drawdown_pct",
            "profit_factor",
            "avg_pnl_pct",
        ]
        if c in df.columns
    ]
    cols_show = [c for c in cols_show if c in df.columns]
    return df[cols_show].round(2).to_html(index=False, classes="dataframe", escape=False)


def _summary_html(
    sweep_df: pd.DataFrame,
    config: ReportConfig,
    data_summary: str,
    period_trade_count: int,
) -> str:
    if sweep_df.empty:
        return "<p>No sweep results.</p>"
    best_sharpe = sweep_df.loc[sweep_df["sharpe_annual"].idxmax()]
    best_pnl = sweep_df.loc[sweep_df["total_pnl_usd"].idxmax()]
    pos_pnl = int((sweep_df["total_pnl_usd"] > 0).sum())

    return f"""
    <div class="summary">
      <div class="card">
        <h3>Best Sharpe</h3>
        <div class="big">{best_sharpe['sharpe_annual']:.2f}</div>
        <div class="small">
          PnL: ${best_sharpe['total_pnl_usd']:,.2f} ·
          MaxDD: {best_sharpe.get('max_drawdown_pct', 0):.1f}% ·
          Hit: {best_sharpe.get('hit_rate', 0):.1f}% ·
          N: {int(best_sharpe['n_trades'])}
        </div>
        <div class="config">{config.format_config_row(best_sharpe)}</div>
      </div>
      <div class="card">
        <h3>Best total PnL</h3>
        <div class="big">${best_pnl['total_pnl_usd']:,.2f}</div>
        <div class="small">
          Sharpe: {best_pnl['sharpe_annual']:.2f} ·
          MaxDD: {best_pnl.get('max_drawdown_pct', 0):.1f}% ·
          N: {int(best_pnl['n_trades'])}
        </div>
        <div class="config">{config.format_config_row(best_pnl)}</div>
      </div>
      <div class="card">
        <h3>Sweep</h3>
        <div class="big">{len(sweep_df)}</div>
        <div class="small">combinations · {pos_pnl} with PnL &gt; 0</div>
        <div class="config">
          {(sweep_df['sharpe_annual'] > 1).sum()} configs Sharpe &gt; 1<br/>
          Median Sharpe: {sweep_df['sharpe_annual'].median():.2f}
        </div>
      </div>
      <div class="card">
        <h3>Data window</h3>
        <div class="small">Trades in window (best Sharpe): {period_trade_count:,}</div>
        <pre class="small">{data_summary}</pre>
      </div>
    </div>
    """


def _default_heatmaps(sweep_df: pd.DataFrame, config: ReportConfig) -> List[go.Figure]:
    params = [p for p in config.param_cols if p in sweep_df.columns]
    if len(params) < 2:
        return []
    pairs = list(config.heatmap_pairs)
    if not pairs:
        pairs = [
            (params[0], params[1], "sharpe_annual", "", "RdYlGn"),
            (params[0], params[1], "total_pnl_usd", "", "RdYlGn"),
        ]
        if len(params) >= 3:
            pairs.append((params[0], params[2], "n_trades", "", "Blues"))
    figs = []
    for spec in pairs:
        x, y, metric = spec[0], spec[1], spec[2]
        suffix = spec[3] if len(spec) > 3 else ""
        cs = spec[4] if len(spec) > 4 else "RdYlGn"
        if x in sweep_df.columns and y in sweep_df.columns:
            figs.append(_heatmap_pair(sweep_df, x, y, metric, suffix, cs))
    return figs


def generate_report(
    config: ReportConfig,
    sweep_df: pd.DataFrame,
    best_trades_df: pd.DataFrame,
    best_eq_df: pd.DataFrame,
    per_segment_df: pd.DataFrame,
    data_summary: str,
    output_path: str | Path,
) -> Path:
    """Write full HTML report; returns output Path."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    heatmap_figs = _default_heatmaps(sweep_df, config)
    per_param_figs = [
        _trade_count_per_param(sweep_df, p)
        for p in config.param_cols
        if p in sweep_df.columns
    ]

    eq_fig = _equity_curve_fig(best_eq_df, "Equity curve — best Sharpe config")
    dist_fig = _trade_distribution_fig(
        best_trades_df,
        "Event PnL distribution — best Sharpe config",
        config.trade_pnl_col,
    )
    exit_fig = _exit_reasons_fig(
        best_trades_df, "Exit / event reasons — best Sharpe config"
    )
    seg_fig = _per_segment_fig(per_segment_df, config.segment_col)

    def _div(fig: go.Figure) -> str:
        return fig.to_html(full_html=False, include_plotlyjs=False, div_id=None)

    disclaimer = ""
    if config.disclaimer_html:
        disclaimer = f'<div class="disclaimer">{config.disclaimer_html}</div>'

    subtitle = f"<p class=\"meta\">{config.subtitle}</p>" if config.subtitle else ""
    heatmap_grid = (
        f'<div class="grid-3">{"".join(f"<div>{_div(f)}</div>" for f in heatmap_figs)}</div>'
        if heatmap_figs
        else "<p>No heatmaps (need ≥2 param columns).</p>"
    )

    html = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{config.title}</title>
  <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      max-width: 1400px; margin: 0 auto; padding: 24px;
      background: #fafafa; color: #222;
    }}
    h1 {{ font-size: 28px; margin-bottom: 6px; }}
    h2 {{ font-size: 20px; margin-top: 36px; border-bottom: 1px solid #ddd; padding-bottom: 6px; }}
    .meta {{ color: #777; font-size: 13px; margin-bottom: 24px; }}
    .disclaimer {{
      background: #fff8e6; border: 1px solid #f0d78c; border-radius: 6px;
      padding: 12px 16px; font-size: 13px; margin: 12px 0 20px 0;
    }}
    .summary {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 16px 0; }}
    .card {{
      background: white; border: 1px solid #e5e5e5; border-radius: 8px;
      padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}
    .card h3 {{ margin: 0 0 8px 0; font-size: 14px; color: #555; }}
    .card .big {{ font-size: 28px; font-weight: 600; color: #2c5fd6; }}
    .card .small {{ font-size: 12px; color: #777; margin: 4px 0; }}
    .card .config {{ font-size: 11px; color: #444; margin-top: 8px; font-family: monospace; }}
    .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    table.dataframe {{
      border-collapse: collapse; font-size: 12px; width: 100%; margin: 12px 0;
      background: white;
    }}
    table.dataframe th, table.dataframe td {{
      border: 1px solid #e5e5e5; padding: 6px 10px; text-align: right;
    }}
    table.dataframe th {{ background: #f0f0f0; font-weight: 600; }}
    pre.small {{ font-size: 11px; margin: 0; white-space: pre-wrap; }}
  </style>
</head>
<body>
  <h1>{config.title}</h1>
  <div class="meta">Generated {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}</div>
  {subtitle}
  {disclaimer}

  <h2>1. Summary</h2>
  {_summary_html(sweep_df, config, data_summary, len(best_trades_df))}

  <h2>2. Heatmaps</h2>
  <p style="color:#666; font-size:13px;">{config.heatmap_note}</p>
  {heatmap_grid}

  <h2>3. Top {config.top_n} configurations (by Sharpe)</h2>
  {_top_configs_html(sweep_df, config, config.top_n)}

  <h2>4. Sensitivity per parameter</h2>
  <div class="grid-2">
    {"".join(f'<div>{_div(f)}</div>' for f in per_param_figs)}
  </div>

  <h2>5. Best configuration — detailed</h2>
  <div class="grid-2">
    <div>{_div(eq_fig)}</div>
    <div>{_div(dist_fig)}</div>
  </div>
  <div class="grid-2">
    <div>{_div(exit_fig)}</div>
    <div>{_div(seg_fig)}</div>
  </div>
</body>
</html>
"""
    output_path.write_text(html, encoding="utf-8")
    return output_path
