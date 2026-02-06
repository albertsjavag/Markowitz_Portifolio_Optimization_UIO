# Markowitz_Portifolio_Optimization_UIO
This is a repo used for portifolio optimization. 

## Author
Albert Sjåvåg 
Quantitative Finance | University of Oslo
Email: albert.sjaavaag@gmail.com

Github repo link: https://github.com/albertsjavag/Markowitz_Portifolio_Optimization_UIO


## Expected return

Let $r_{i,t}$ denote the return of asset $i$ at time $t$.
The expected return is defined as

$$
    E[r_i]
$$

Since $E[r_i]$ is unknown, we estimate it from historical data using the sample mean

$$
    \bar{r}_i
    =
    \frac{1}{T}\sum_{t=1}^{T} r_{i,t}
$$

For daily data, the annualized expected return is

$$
    \mu_i
    =
    252\,\bar{r}_i
    =
    252\cdot\frac{1}{T}\sum_{t=1}^{T} r_{i,t}
$$


## Covariance matrix

Let $r_{i,t}$ and $r_{j,t}$ denote the returns of assets $i$ and $j$ at time $t$.
The covariance between assets $i$ and $j$ is defined as

$$
    \Sigma_{ij}
    =
    E\!\left[(r_i - E[r_i])(r_j - E[r_j])\right]
$$

Since the true covariance is unknown, it is estimated from historical data as

$$
    \hat{\Sigma}_{ij}
    =
    \frac{1}{T-1}
    \sum_{t=1}^{T}
    (r_{i,t} - \bar{r}_i)(r_{j,t} - \bar{r}_j)
$$

Collecting all covariances yields the covariance matrix

$$
    \boldsymbol{\Sigma}
    =
    \begin{pmatrix}
    \Sigma_{11} & \Sigma_{12} & \cdots & \Sigma_{1N} \\
    \Sigma_{21} & \Sigma_{22} & \cdots & \Sigma_{2N} \\
    \vdots      & \vdots      & \ddots & \vdots      \\
    \Sigma_{N1} & \Sigma_{N2} & \cdots & \Sigma_{NN}
    \end{pmatrix}
$$

## Portfolio expected return

Let $\mathbf{w} = (w_1, \dots, w_N)^\top$ denote the portfolio weights.
The expected portfolio return is given by

$$
    E[r_p]
    =
    \mathbf{w}^\top \boldsymbol{\mu}
    =
    \sum_{i=1}^{N} w_i \mu_i
$$

## Portfolio variance and volatility

The variance of the portfolio return is given by

$$
    \mathrm{Var}(r_p)
    =
    \mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}
$$

The portfolio volatility (standard deviation) is therefore

$$
    \sigma_p
    =
    \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}}
$$

## Sharpe ratio

Let $r_f$ denote the risk-free rate.
The Sharpe ratio of the portfolio is defined as

$$
    \mathrm{SR}
    =
    \frac{E[r_p] - r_f}{\sigma_p}
    =
    \frac{\mathbf{w}^\top \boldsymbol{\mu} - r_f}
    {\sqrt{\mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}}}
$$

## Markowitz mean–variance optimization

Given expected returns $\boldsymbol{\mu}$ and covariance matrix $\boldsymbol{\Sigma}$,
the mean–variance optimization problem can be written as

$$
    \min_{\mathbf{w}}
    \ \mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}
    \quad \text{subject to} \quad
    \mathbf{w}^\top \boldsymbol{\mu} = \mu_{\text{target}},
    \ \sum_{i=1}^{N} w_i = 1
$$

A common alternative formulation is the risk-aversion (quadratic utility) form

$$
    \max_{\mathbf{w}}
    \left(
    \mathbf{w}^\top \boldsymbol{\mu}
    -
    \frac{\lambda}{2}\mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}
    \right)
    \quad \text{subject to} \quad
    \sum_{i=1}^{N} w_i = 1
$$


#### Note to self: 
bash: conda activate markowitz


