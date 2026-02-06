# Markowitz_Portifolio_Optimization_UIO
This is a repo used for portifolio optimization. 

## Author
Albert Sjåvåg 
Quantitative Finance | University of Oslo
Email: albert.sjaavaag@gmail.com

Github repo link: https://github.com/albertsjavag/Markowitz_Portifolio_Optimization_UIO


## Expected return (estimation)

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


