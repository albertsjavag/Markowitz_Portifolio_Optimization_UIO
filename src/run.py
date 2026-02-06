"""
run.py

End-to-end demo:
tickers -> prices -> returns -> mu/cov -> Markowitz weights -> metrics
"""

from src.data import fetch_prices, clean_prices
from src.returns import compute_returns, estimate_mean_returns, estimate_covariance
from src.markowitz import minimum_variance_weights, max_sharpe_weights
from src.indicators import portfolio_return, portfolio_volatility, sharpe_ratio


def main():
    tickers = ["EQNR.OL", "DNB.OL", "TEL.OL", "AAPL", "MSFT"]
    years = 3
    rf = 0.0

    # 1) Fetch + clean prices
    prices, fetch_report = fetch_prices(tickers, years=years, progress=False)
    prices, clean_report = clean_prices(prices, method="dropna", min_obs=252)

    print("\n=== Fetch report ===")
    print(fetch_report)
    print("\n=== Clean report ===")
    print(clean_report)

    if prices.empty or prices.shape[1] < 2:
        print("\nNot enough usable price series to continue.")
        return

    # Returns + parameter estimates
    rets = compute_returns(prices, kind="log")
    mu = estimate_mean_returns(rets, periods=252)
    cov = estimate_covariance(rets, periods=252)

    print("\n=== Expected returns (mu, annualized) ===")
    print(mu.sort_values(ascending=False))

    # Markowitz portfolios
    w_min = minimum_variance_weights(cov)
    w_tan = max_sharpe_weights(mu, cov, rf=rf)

    print("\n=== Minimum-variance weights ===")
    print(w_min.sort_values(ascending=False))
    print(f"Sum weights: {w_min.sum():.6f}")

    print("\n=== Max-Sharpe (tangency) weights ===")
    print(w_tan.sort_values(ascending=False))
    print(f"Sum weights: {w_tan.sum():.6f}")

    # Portfolio metrics
    min_ret = portfolio_return(w_min.values, mu)
    min_vol = portfolio_volatility(w_min.values, cov)
    min_sr = sharpe_ratio(w_min.values, mu, cov, rf=rf)

    tan_ret = portfolio_return(w_tan.values, mu)
    tan_vol = portfolio_volatility(w_tan.values, cov)
    tan_sr = sharpe_ratio(w_tan.values, mu, cov, rf=rf)

    print("\n=== Metrics (annualized) ===")
    print(f"Min-Var:   return={min_ret:.4f}, vol={min_vol:.4f}, Sharpe={min_sr:.4f}")
    print(f"MaxSharpe: return={tan_ret:.4f}, vol={tan_vol:.4f}, Sharpe={tan_sr:.4f}")


if __name__ == "__main__":
    main()