"""
dashboard.py

Terminal dashboard using Rich (static output).
"""
from __future__ import annotations

import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align

console = Console()


def show_dashboard(
    tickers: list[str],
    mu: pd.Series,
    w_min: pd.Series,
    w_tan: pd.Series,
    min_ret: float,
    min_vol: float,
    min_sr: float,
    tan_ret: float,
    tan_vol: float,
    tan_sr: float,
    rf: float,
    years: int,
) -> None:
    table = Table(title="Markowitz Portfolio Results", show_lines=True)

    table.add_column("Asset", justify="left")
    table.add_column("μ (annual)", justify="right")
    table.add_column("Min-Var w", justify="right")
    table.add_column("Max-Sharpe w", justify="right")


    for asset in mu.index:
        table.add_row(
            str(asset),
            f"{float(mu[asset]):.4f}",
            f"{float(w_min.get(asset, 0.0)):.4f}",
            f"{float(w_tan.get(asset, 0.0)):.4f}",
        )

    header = (
        f"[bold]Tickers[/bold]: {', '.join(tickers)}\n"
        f"[bold]Years[/bold]: {years}    [bold]rf[/bold]: {rf:.4f}"
    )

    metrics = (
        f"[bold]Min-Variance[/bold]\n"
        f"Return: {min_ret:.4f}\n"
        f"Vol:    {min_vol:.4f}\n"
        f"Sharpe: {min_sr:.4f}\n\n"
        f"[bold]Max-Sharpe[/bold]\n"
        f"Return: {tan_ret:.4f}\n"
        f"Vol:    {tan_vol:.4f}\n"
        f"Sharpe: {tan_sr:.4f}"
    )

    console.print(Panel(header, title = "Run settings", border_style = "blue"))
    console.print(Panel(Align.center(table), title = "Weights + μ", border_style = "cyan"))
    console.print(Panel(metrics, title = "Metrics (annualized)", border_style = "green"))