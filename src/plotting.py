"""
plotting.py

Plots for the efficient frontier.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt


def plot_frontier(
    frontier: pd.DataFrame,
    title: str = "Efficient Frontier",
    show: bool = True,
    savepath: Optional[str] = None,
) -> None:
    """
    Plot efficient frontier (volatility on x-axis, return on y-axis).

    Expects columns: "vol", "ret"
    """
    required = {"vol", "ret"}
    if not required.issubset(frontier.columns):
        raise ValueError(f"frontier must contain columns {required}")

    x = frontier["vol"].to_numpy()
    y = frontier["ret"].to_numpy()

    plt.figure()
    plt.plot(x, y, marker="o", linestyle="-")
    plt.xlabel("Volatility (annualized)")
    plt.ylabel("Expected return (annualized)")
    plt.title(title)
    plt.grid(True)

    if savepath is not None:
        plt.savefig(savepath, bbox_inches="tight")

    if show:
        plt.show()
    else:
        plt.close()