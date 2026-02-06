"""
This file is for obtaining and cleaning data. 

We use yfinance to get open sourse stock data to later analyze

standard usage:
prices, report = fetch_adj_close(tickers, years=3)
prices_clean, clean_report = clean_prices(prices, min_obs=252)
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Iterable, Optional, Tuple, Dict, List, Union

import numpy as np
import pandas as pd
import yfinance as yf


def _as_list(x: Union[str, Iterable[str]]) -> List[str]:
    if isinstance(x, str):
        return [x]
    return [t.strip() for t in x if str(t).strip()]


def _end_as_timestamp(end: Optional[Union[str, date, datetime]]) -> pd.Timestamp:
    if end is None:
        return pd.Timestamp.today().normalize()
    return pd.to_datetime(end).normalize()


def _start_from_years(end_ts: pd.Timestamp, years: int) -> pd.Timestamp:
    days = int(round(years * 365.25))
    return (end_ts - pd.Timedelta(days=days)).normalize()
