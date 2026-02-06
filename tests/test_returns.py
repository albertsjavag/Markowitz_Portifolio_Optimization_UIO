"""
test_returns.py

Simple tests for functions in src.returns.

Run with:
    python -m tests.test_returns
"""

import pandas as pd
import numpy as np

from src.returns import compute_returns


def sample_prices():
    dates = pd.date_range("2024-01-01", periods=4, freq="D")
    return pd.DataFrame(
        {
            "A": [100, 101, 102, 103],
            "B": [200, 198, 202, 204],
        },
        index = dates,
    )


def test_compute_returns():
    prices = sample_prices()
    returns = compute_returns(prices, kind="log")

    assert not returns.empty
    assert returns.shape[1] == 2
    assert isinstance(returns.iloc[0, 0], float)

    print("test_compute_returns passed")
