"""
run.py

End-to-end demo:
tickers -> prices -> returns -> mu/cov -> Markowitz weights -> metrics
"""

from src.data import fetch_prices, clean_prices
from src.returns import compute_returns, estimate_mean_returns, estimate_covariance
from src.markowitz import minimum_variance_weights, max_sharpe_weights
from src.indicators import portfolio_return, portfolio_volatility, sharpe_ratio
from src.dashboard import show_dashboard
from src.frontier import efficient_frontier
from src.plotting import plot_frontier



def main():
    tickers = ["EQNR.OL", "DNB.OL", "TEL.OL", "AAPL", "MSFT", "NVDA",
               "SUBC.OL", "BTC-USD"]
    years = 3
    rf = 0.0

    prices, fetch_report = fetch_prices(tickers, years=years, progress=False)
    prices, clean_report = clean_prices(prices, method="dropna", min_obs=252)

    if prices.empty or prices.shape[1] < 2:
        print(fetch_report)
        print(clean_report)
        print("Not enough usable price series to continue.")
        return

    rets = compute_returns(prices, kind="log")
    mu = estimate_mean_returns(rets, periods=252)
    cov = estimate_covariance(rets, periods=252)

    # Markowitz weights
    w_min = minimum_variance_weights(cov)
    w_tan = max_sharpe_weights(mu, cov, rf=rf)

    # Metrics
    min_ret = portfolio_return(w_min.values, mu)
    min_vol = portfolio_volatility(w_min.values, cov)
    min_sr = sharpe_ratio(w_min.values, mu, cov, rf=rf)

    tan_ret = portfolio_return(w_tan.values, mu)
    tan_vol = portfolio_volatility(w_tan.values, cov)
    tan_sr = sharpe_ratio(w_tan.values, mu, cov, rf=rf)

    # Pretty output
    show_dashboard(
        tickers=list(prices.columns),
        mu=mu.loc[prices.columns],
        w_min=w_min.loc[prices.columns],
        w_tan=w_tan.loc[prices.columns],
        min_ret=min_ret,
        min_vol=min_vol,
        min_sr=min_sr,
        tan_ret=tan_ret,
        tan_vol=tan_vol,
        tan_sr=tan_sr,
        rf=rf,
        years=years,
    )

    frontier_df, _ = efficient_frontier(mu, cov, n_points=50)
    plot_frontier(
        frontier_df,
        mu=mu,
        cov=cov,
        min_var=(min_vol, min_ret),
        max_sharpe=(tan_vol, tan_ret),
        rf=rf,
        title="Efficient Frontier",
    )


if __name__ == "__main__":
    main()