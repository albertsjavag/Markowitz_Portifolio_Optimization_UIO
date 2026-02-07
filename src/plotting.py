"""
plotting.py

Plots for the efficient frontier.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_frontier(
    frontier: pd.DataFrame,
    mu: Optional[pd.Series] = None,
    cov: Optional[pd.DataFrame] = None,
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
    plt.plot(x, y, marker="o", linestyle="-", label="Efficient frontier")
    plt.xlabel("Volatility (annualized)")
    plt.ylabel("Expected return (annualized)")
    plt.title(title)
    plt.grid(True)

    
    if mu is not None and cov is not None:
        assets = list(mu.index)
        cov_aligned = cov.loc[assets, assets]

        vols = np.sqrt(np.diag(cov_aligned.to_numpy(dtype=float)))
        rets = mu.to_numpy(dtype=float)

        plt.scatter(
            vols,
            rets,
            marker="x",
            color="black",
            label="Individual assets"
        )

        for a, vx, vy in zip(assets, vols, rets):
            plt.annotate(
                a,
                (vx, vy),
                textcoords="offset points",
                xytext=(6, 4),
                fontsize=9,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.7)
            )

    if savepath is not None:
        plt.savefig(savepath, bbox_inches="tight")

    if show:
        plt.legend()
        plt.show()
    else:
        plt.close()